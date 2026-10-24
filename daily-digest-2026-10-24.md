# My Daily Digest - 2026-10-24

> Sources: GitHub Search, GitHub Trending, Hacker News

---

## GitHub 热门开源项目

> 说明：近7天新创建的 GitHub 仓库，按 Star 增长速度排名。适合发现新兴工具、热门框架和有趣的开源项目。

1. ### [simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv)

A fast, ad-free home screen for Google TV, LG webOS and Samsung Tizen. One button to undo.

? 4005  |  ?? Java  |  _GitHub Search_  `android-tv` `claude-code` `google-tv` `home-screen` `launcher`

2. ### [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv)

给国产电视的一块干净桌面：参照 tvOS 设计的开源 Android TV 桌面，没有广告，开机自动接管。A tvOS-style launcher for Xiaomi, TCL and other China-market TVs.

? 3960  |  ?? Kotlin  |  _GitHub Search_  

3. ### [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy)

数学（小学到高中）、英语（三年级到高中）、初中物理的知识图谱：1644 个知识点、2403 条先修边、6723 道题，对齐课标，附自适应前置诊断。

? 2890  |  ?? Python  |  _GitHub Search_  `chinese` `curriculum` `diagnostic` `edtech` `education`

4. ### [JoasASantos/REA-Prompts](https://github.com/JoasASantos/REA-Prompts)

REAP - Prompts for you to use REA (Reverse Engineer Anything), get the most out of it, and clone or break down any progr...

? 1783  |  ?? N/A  |  _GitHub Search_  `prompt-engineering` `rea` `reverse-enginnering`

5. ### [ikow/php2shell-poc](https://github.com/ikow/php2shell-poc)

CVE-2026-109618/109619 — 5 RCE chains + detection rules (Suricata, Sigma, ModSecurity). PHP session.upload_progress pre-...

? 1707  |  ?? Python  |  _GitHub Search_  `cve-2026-109618` `cve-2026-109619` `detection-rules` `exploit` `php-exploit`

6. ### [EthanArbuckle/fairplay-decrypt](https://github.com/EthanArbuckle/fairplay-decrypt)

Offline FairPlay App Store IPA decryption with independent key derivation

? 1681  |  ?? C  |  _GitHub Search_  

7. ### [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion)

让你的agent一键直出商业级产品宣传片：会作曲，能指着画面改。Commercial-grade launch films by your coding agent — point at the frame to change it.

? 1550  |  ?? JavaScript  |  _GitHub Search_  `agent-skills` `animation` `claude-code` `codex` `gsap`

8. ### [humblemuzzu/dumbtv](https://github.com/humblemuzzu/dumbtv)

Take the ads, tracking and clutter out of your Fire TV over ADB, no root. Every step can be undone. Comes with its own o...

? 1404  |  ?? Java  |  _GitHub Search_  `ad-blocking` `adb` `android-tv` `debloat` `dns-filter`

9. ### [Ansub/tv-detox](https://github.com/Ansub/tv-detox)

Make an old Android TV fast again with Claude Code or Codex: a tiny ad-free home screen plus the prompt to clean it up

? 1394  |  ?? Java  |  _GitHub Search_  

10. ### [9bie/php2shell-bypass-aslr-exp](https://github.com/9bie/php2shell-bypass-aslr-exp)

A php2shell exploit that requires no modifications to the official version, and does not require display_errors or limit...

? 1303  |  ?? Python  |  _GitHub Search_  

---

## Hacker News 热门讨论

> 说明：Hacker News 社区当前最热的讨论帖，涉及技术趋势、新工具发布和程序员热点话题。

- [Kimi K3.1 Pro and K3.1 Pro Highspeed](https://www.kimi.ai/blog/kimi-k3-1-pro)  ?809  by _Jowsey_
- [Twelve years of distributed SQLite](https://philipotoole.com/twelve-years-of-distributed-sqlite/)  ?95  by _otoolep_
- [Apple Music 404 Not Found](https://music.apple.com/this-url-doesnt-exist)  ?675  by _frizlab_
- [How close can pure functional programming get to C?](https://rtfeldman.com/fp-vs-c)  ?16  by _stmonty_
- [Local Wikipedia: Wikipedia, but only for things a half hour walk from you](https://edjefferson.com/localwiki/)  ?1318  by _sohkamyung_

---

## Codex 实用 Skills

> 说明：Codex Skills 是可复用的 AI 行为指南，安装后可在对话中直接调用。安装：codex install <skill-name>

| Skill | 能干什么 |
|-------|----------|
| `build-web-apps` | Frontend app builder - Build frontend apps with AI |
| `agent-browser` | Browser automation CLI |
| `figma` | Figma design to code workflow |
| `notion-knowledge-capture` | Capture conversations into structured Notion pages |
| `yeet` | One-click Stage-Commit-Push-PR workflow |
| `gh-fix-ci` | Debug GitHub Actions CI failures |
| `mcp-builder` | Guide for creating high-quality MCP Servers |
| `diagnose` | Structured debugging loop for hard-to-reproduce bugs |
| `codebase-migrate` | Large-scale codebase migration / multi-file refactoring |
| `transcribe` | Transcribe audio to text with speaker diarization |

---

## Codex 学习资料

> 说明：Codex 学习资料汇总。建议从 Karpathy 编码准则开始读，它能帮你写出更简洁、更可靠的代码。

- **Karpathy Coding Guidelines** - Reduce common LLM coding mistakes, emphasizing simplicity and precision
- **Using-Superpowers** - Checklist before starting long tasks
- **AGENTS.md Spec** - Repository-level instruction files guiding AI agent behavior
- **Skill-Creator Workflow** - Encapsulate repeated workflows as reusable Skills

---

## 常用链接

> 说明：日常开发常用工具和社区入口。

- [Codex GitHub](https://github.com/openai/codex)
- [OpenAI Docs](https://platform.openai.com/docs)
- [GitHub Trending](https://github.com/trending)
- [Hacker News](https://news.ycombinator.com)

---

## 常用命令

> 说明：本项目相关命令速查。可将 python digest.py 加到定时任务或 GitHub Actions 实现每日自动生成。

```
# Generate digest
python digest.py

# Start dashboard server
python digest.py --serve

# Open dashboard
http://localhost:8080
```

---

## Notes

> (write your notes here)
