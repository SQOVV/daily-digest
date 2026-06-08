import json, urllib.request, urllib.error, datetime, os, sys, re, html as html_mod, http.server, threading, webbrowser

# ?? Constants ??
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
USER_AGENT  = "Codex-Daily-Digest/2.0"
HN_API     = "https://hacker-news.firebaseio.com/v0"
GH_API     = "https://api.github.com"

# ?? Load Config ??
def load_config():
    default = {
        "title": "My Daily Digest",
        "data_sources": {"github_trending": True, "github_search": True, "hacker_news": True},
        "github": {"max_repos": 10, "days_lookback": 7, "min_stars": 50, "language_filter": ""},
        "hacker_news": {"max_posts": 5},
        "output": {"dir": ".", "filename_prefix": "daily-digest-"},
        "appearance": {"theme": "dark", "language": "zh"}
    }
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            cfg = json.load(f)
        for k, v in default.items():
            cfg.setdefault(k, v)
        return cfg
    except:
        return default

CFG = load_config()

# ?? HTTP Helper ??
def gh_headers():
    return {"User-Agent": USER_AGENT, "Accept": "application/vnd.github.v3+json"}

def fetch_json(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print(f"  [x] Fetch failed: {url[:60]}... {e}", file=sys.stderr)
        return None

def fetch_text(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode()
    except Exception as e:
        print(f"  [x] Fetch failed: {url[:60]}... {e}", file=sys.stderr)
        return ""

# ???????????????????????????????????????
# DATA SOURCES
# ???????????????????????????????????????

# ?? GitHub Search API ??
def fetch_github_search(cfg):
    g = cfg["github"]
    since = (datetime.date.today() - datetime.timedelta(days=g["days_lookback"])).isoformat()
    q = f"created:>{since}"
    if g.get("language_filter"):
        q += f"+language:{g['language_filter']}"
    url = f"{GH_API}/search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page={g['max_repos']}"
    data = fetch_json(url, headers=gh_headers())
    if not data:
        return []
    repos = []
    for item in data.get("items", []):
        if item["stargazers_count"] < g["min_stars"]:
            continue
        repos.append({
            "name": item["full_name"], "url": item["html_url"],
            "desc": item.get("description") or "(no description)",
            "stars": item["stargazers_count"],
            "lang": item.get("language") or "N/A",
            "topics": item.get("topics", [])[:5],
            "source": "GitHub Search"
        })
    return repos

# ?? GitHub Trending ??
def fetch_github_trending(cfg):
    url = "https://github.com/trending"
    html = fetch_text(url)
    if not html:
        return []
    repos = []
    pattern = re.compile(
        r'href="/([^"]+?)"[^>]*?>\s*<h2[^>]*?>\s*([^<]+?)\s*<[^>]*?>\s*</h2>'
        r'.*?<p[^>]*?class="col-9[^"]*"[^>]*?>\s*(.*?)\s*</p>'
        r'.*?<span[^>]*?class="d-inline-block float-sm-right"[^>]*?>\s*([\d,]+)\s*</span>',
        re.DOTALL
    )
    # Alternative simpler approach: find article items
    articles = re.findall(
        r'<article[^>]*class="Box-row"[^>]*>.*?</article>',
        html, re.DOTALL
    )
    for art in articles:
        match = re.search(r'href="/[^"]+/[^"]+"', art)
        if not match:
            continue
        full_name = match.group(0).replace('href="/', '').replace('"', '').strip()
        # name
        name_match = re.search(r'<h2[^>]*>.*?<a[^>]*href="/[^"]+"[^>]*>([^<]+)</a>', art, re.DOTALL)
        # description
        desc_match = re.search(r'<p[^>]*class="col-9[^"]*"[^>]*>(.*?)</p>', art, re.DOTALL)
        # stars
        star_match = re.search(r'<span[^>]*class="d-inline-block float-sm-right"[^>]*>([\d,]+)</span>', art)
        # language
        lang_el = re.search(r'<span[^>]*itemprop="programmingLanguage"[^>]*>([^<]+)</span>', art)
        lang = lang_el.group(1).strip() if lang_el else "N/A"
        desc = ""
        if desc_match:
            desc = re.sub(r'<[^>]+>', '', desc_match.group(1)).strip()
        stars = 0
        if star_match:
            stars = int(star_match.group(1).replace(",", ""))
        repos.append({
            "name": full_name or "unknown/repo",
            "url": f"https://github.com/{full_name}" if full_name and "/" in full_name else "",
            "desc": desc or "(no description)",
            "stars": stars,
            "lang": lang,
            "topics": [],
            "source": "GitHub Trending"
        })
    return repos[:cfg["github"]["max_repos"]]

# ?? Hacker News ??
def fetch_hacker_news(cfg):
    max_p = cfg["hacker_news"]["max_posts"]
    ids = fetch_json(f"{HN_API}/topstories.json")
    if not ids:
        return []
    posts = []
    for sid in ids[:30]:
        item = fetch_json(f"{HN_API}/item/{sid}.json")
        if not item or item.get("type") != "story" or item.get("title") is None:
            continue
        posts.append({
            "title": item["title"],
            "url": item.get("url") or f"https://news.ycombinator.com/item?id={sid}",
            "score": item.get("score", 0),
            "by": item.get("by", "anonymous"),
            "source": "Hacker News"
        })
        if len(posts) >= max_p:
            break
    return posts

# ???????????????????????????????????????
# FORMATTERS
# ???????????????????????????????????????

def fmt_repo_badge(r):
    topics = " ".join(f"`{t}`" for t in r["topics"]) if r["topics"] else ""
    desc = (r["desc"][:120] + "...") if len(r["desc"]) > 120 else r["desc"]
    return (
        f"### [{r['name']}]({r['url']})\n\n"
        f"{desc}\n\n"
        f"? {r['stars']}  |  ?? {r['lang']}  |  _{r.get('source', '')}_  {topics}\n"
    )

def fmt_hn_post(p):
    return f"- [{p['title']}]({p['url']})  ?{p['score']}  by _{p['by']}_"

# ???????????????????????????????????????
# DIGEST BUILDER
# ???????????????????????????????????????

COLLECTED_SKILLS = [
    ("build-web-apps", "Frontend app builder - Build frontend apps with AI"),
    ("agent-browser", "Browser automation CLI"),
    ("figma", "Figma design to code workflow"),
    ("notion-knowledge-capture", "Capture conversations into structured Notion pages"),
    ("yeet", "One-click Stage-Commit-Push-PR workflow"),
    ("gh-fix-ci", "Debug GitHub Actions CI failures"),
    ("mcp-builder", "Guide for creating high-quality MCP Servers"),
    ("diagnose", "Structured debugging loop for hard-to-reproduce bugs"),
    ("codebase-migrate", "Large-scale codebase migration / multi-file refactoring"),
    ("transcribe", "Transcribe audio to text with speaker diarization"),
]

COLLECTED_ARTICLES = [
    ("Karpathy Coding Guidelines", "Reduce common LLM coding mistakes, emphasizing simplicity and precision"),
    ("Using-Superpowers", "Checklist before starting long tasks"),
    ("AGENTS.md Spec", "Repository-level instruction files guiding AI agent behavior"),
    ("Skill-Creator Workflow", "Encapsulate repeated workflows as reusable Skills"),
]

def build_digest(repos, hn_posts):
    today = datetime.date.today().isoformat()
    lines = []
    a = lines.append
    a(f"# {CFG.get('title', 'Daily Digest')} - {today}")
    a("")
    srcs = []
    if CFG["data_sources"]["github_search"]: srcs.append("GitHub Search")
    if CFG["data_sources"]["github_trending"]: srcs.append("GitHub Trending")
    if CFG["data_sources"]["hacker_news"]: srcs.append("Hacker News")
    a(f"> Sources: {', '.join(srcs)}")
    a("")
    # ?? GitHub ??
    if repos:
        a("---")
        a("")
        a("## GitHub 热门开源项目")
        a("")
        a("> 说明：近7天新创建的 GitHub 仓库，按 Star 增长速度排名。适合发现新兴工具、热门框架和有趣的开源项目。")
        a("")
        for i, r in enumerate(repos, 1):
            a(f"{i}. {fmt_repo_badge(r)}")
    # ?? Hacker News ??
    if hn_posts:
        a("---")
        a("")
        a("## Hacker News 热门讨论")
        a("")
        a("> 说明：Hacker News 社区当前最热的讨论帖，涉及技术趋势、新工具发布和程序员热点话题。")
        a("")
        for p in hn_posts:
            a(fmt_hn_post(p))
        a("")
    # ?? Skills ??
    a("---")
    a("")
    a("## Codex 实用 Skills")
    a("")
    a("> 说明：Codex Skills 是可复用的 AI 行为指南，安装后可在对话中直接调用。安装：codex install <skill-name>")
    a("")
    a("| Skill | 能干什么 |")
    a("|-------|----------|")
    for name, desc in COLLECTED_SKILLS:
        a(f"| `{name}` | {desc} |")
    a("")
    # ?? Resources ??
    a("---")
    a("")
    a("## Codex 学习资料")
    a("")
    a("> 说明：Codex 学习资料汇总。建议从 Karpathy 编码准则开始读，它能帮你写出更简洁、更可靠的代码。")
    a("")
    for title, desc in COLLECTED_ARTICLES:
        a(f"- **{title}** - {desc}")
    a("")
    # ?? Links ??
    a("---")
    a("")
    a("## 常用链接")
    a("")
    a("> 说明：日常开发常用工具和社区入口。")
    a("")
    for title, url in [
        ("Codex GitHub", "https://github.com/openai/codex"),
        ("OpenAI Docs", "https://platform.openai.com/docs"),
        ("GitHub Trending", "https://github.com/trending"),
        ("Hacker News", "https://news.ycombinator.com"),
    ]:
        a(f"- [{title}]({url})")
    a("")
    # ?? Commands ??
    a("---")
    a("")
    a("## 常用命令")
    a("")
    a("> 说明：本项目相关命令速查。可将 python digest.py 加到定时任务或 GitHub Actions 实现每日自动生成。")
    a("")
    BT = chr(96) * 3
    a(BT)
    a("# Generate digest")
    a("python digest.py")
    a("")
    a("# Start dashboard server")
    a("python digest.py --serve")
    a("")
    a("# Open dashboard")
    a("http://localhost:8080")
    a(BT)
    a("")
    a("---")
    a("")
    a("## Notes")
    a("")
    a("> (write your notes here)")
    a("")
    return "\n".join(lines)

# ???????????????????????????????????????
# HTTP SERVER MODE (Dashboard API)
# ???????????????????????????????????????

def get_latest_digest():
    today = datetime.date.today().isoformat()
    fname = f"{CFG['output']['filename_prefix']}{today}.md"
    fpath = os.path.join(SCRIPT_DIR, CFG["output"]["dir"], fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            return f.read(), fname
    return None, fname

def list_digests():
    prefix = CFG["output"]["filename_prefix"]
    d = os.path.join(SCRIPT_DIR, CFG["output"]["dir"])
    files = sorted([f for f in os.listdir(d) if f.startswith(prefix) and f.endswith(".md")], reverse=True)
    return files

def run_generate():
    repos, hn = [], []
    if CFG["data_sources"]["github_search"]:
        print("[~] GitHub Search...")
        repos.extend(fetch_github_search(CFG))
    if CFG["data_sources"]["github_trending"]:
        print("[~] GitHub Trending...")
        repos.extend(fetch_github_trending(CFG))
    if CFG["data_sources"]["hacker_news"]:
        print("[~] Hacker News...")
        hn = fetch_hacker_news(CFG)
    # dedup by url
    seen, deduped = set(), []
    for r in repos:
        if r["url"] not in seen:
            seen.add(r["url"])
            deduped.append(r)
    repos = deduped[:CFG["github"]["max_repos"]]
    digest = build_digest(repos, hn)
    today = datetime.date.today().isoformat()
    fname = f"{CFG['output']['filename_prefix']}{today}.md"
    out = os.path.join(SCRIPT_DIR, CFG["output"]["dir"], fname)
    with open(out, "w", encoding="utf-8") as f:
        f.write(digest)
    print(f"[OK] Generated: {out}")
    return fname

def serve_dashboard():
    import http.server
    dashboard_html = os.path.join(SCRIPT_DIR, "dashboard.html")
    index_html = None
    if os.path.exists(dashboard_html):
        with open(dashboard_html, "r", encoding="utf-8") as f:
            index_html = f.read()

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/" or self.path == "/index.html":
                if index_html:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(index_html.encode("utf-8"))
                else:
                    self.send_error(404, "dashboard.html not found")
            elif self.path == "/api/latest":
                content, fname = get_latest_digest()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                resp = json.dumps({"ok": True, "content": content or "", "file": fname, "exists": content is not None})
                self.wfile.write(resp.encode("utf-8"))
            elif self.path == "/api/list":
                files = list_digests()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                resp = json.dumps({"ok": True, "files": files})
                self.wfile.write(resp.encode("utf-8"))
            elif self.path.startswith("/api/digest/"):
                fname = self.path.split("/api/digest/", 1)[-1]
                fpath = os.path.join(SCRIPT_DIR, CFG["output"]["dir"], fname)
                if os.path.exists(fpath):
                    with open(fpath, "r", encoding="utf-8") as f:
                        content = f.read()
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.end_headers()
                    resp = json.dumps({"ok": True, "content": content, "file": fname})
                    self.wfile.write(resp.encode("utf-8"))
                else:
                    self.send_response(404)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"ok": False, "error": "not found"}).encode())
            else:
                self.send_error(404)
        def do_POST(self):
            if self.path == "/api/generate":
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                def run():
                    fname = run_generate()
                    return fname
                import threading as t
                t.Thread(target=run, daemon=True).start()
                self.wfile.write(json.dumps({"ok": True, "message": "Generation started"}).encode())
            else:
                self.send_error(404)
        def log_message(self, format, *args):
            pass

    port = 8080
    server = http.server.HTTPServer(("127.0.0.1", port), Handler)
    print(f"[OK] Dashboard: http://127.0.0.1:{port}")
    webbrowser.open(f"http://127.0.0.1:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[x] Server stopped")

# ???????????????????????????????????????
# MAIN
# ???????????????????????????????????????

def main():
    import urllib.parse as _
    # ensure urllib.parse is available for the quote above
    if "--serve" in sys.argv:
        serve_dashboard()
        return
    print(f"[~] Fetching from multiple sources...")
    repos, hn = [], []
    if CFG["data_sources"]["github_search"]:
        print("  - GitHub Search API...", end=" ")
        r = fetch_github_search(CFG)
        print(f"{len(r)} repos")
        repos.extend(r)
    if CFG["data_sources"]["github_trending"]:
        print("  - GitHub Trending...", end=" ")
        r = fetch_github_trending(CFG)
        print(f"{len(r)} repos")
        repos.extend(r)
    if CFG["data_sources"]["hacker_news"]:
        print("  - Hacker News...", end=" ")
        hn = fetch_hacker_news(CFG)
        print(f"{len(hn)} posts")
    seen, deduped = set(), []
    for r in repos:
        if r["url"] not in seen:
            seen.add(r["url"])
            deduped.append(r)
    repos = deduped[:CFG["github"]["max_repos"]]
    digest = build_digest(repos, hn)
    today = datetime.date.today().isoformat()
    fname = f"{CFG['output']['filename_prefix']}{today}.md"
    out = os.path.join(SCRIPT_DIR, CFG["output"]["dir"], fname)
    with open(out, "w", encoding="utf-8") as f:
        f.write(digest)
    print(f"[OK] Generated: {out}")
    print(f"[OK] Total: {len(repos)} repos + {len(hn)} HN posts")
    if "--serve" not in sys.argv and "--no-open" not in sys.argv:
        print(f"[~] Run 'python digest.py --serve' for dashboard")

if __name__ == "__main__":
    main()

