# My Daily Digest - 2026-10-23

> Sources: GitHub Search, GitHub Trending, Hacker News

---

## GitHub 热门开源项目

> 说明：近7天新创建的 GitHub 仓库，按 Star 增长速度排名。适合发现新兴工具、热门框架和有趣的开源项目。

1. ### [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv)

Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home.

? 25016  |  ?? Java  |  _GitHub Search_  `adb` `adblock` `android-tv` `android-tv-launcher` `apple-tv`

2. ### [ly05010419/MacNativeGames](https://github.com/ly05010419/MacNativeGames)

(no description)

? 4595  |  ?? C  |  _GitHub Search_  

3. ### [simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv)

A fast, ad-free home screen for Google TV. Open source, built with Claude Code. One button to undo.

? 3558  |  ?? Java  |  _GitHub Search_  `android-tv` `claude-code` `google-tv` `home-screen` `launcher`

4. ### [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv)

给国产电视的一块干净桌面：参照 tvOS 设计的开源 Android TV 桌面，没有广告，开机自动接管。A tvOS-style launcher for Xiaomi, TCL and other China-market TVs.

? 3341  |  ?? Kotlin  |  _GitHub Search_  

5. ### [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy)

数学（小学到高中）、英语（三年级到高中）、初中物理的知识图谱：1644 个知识点、2403 条先修边、6723 道题，对齐课标，附自适应前置诊断。

? 2340  |  ?? Python  |  _GitHub Search_  `chinese` `curriculum` `diagnostic` `edtech` `education`

6. ### [tek-sys-hub/Rubix-lang](https://github.com/tek-sys-hub/Rubix-lang)

The 100% Pure x86-64 Assembly Systems Language

? 1904  |  ?? Assembly  |  _GitHub Search_  `assembler` `assembly` `assembly-lang` `assembly-language` `assembly-language-programming`

7. ### [ikow/php2shell-poc](https://github.com/ikow/php2shell-poc)

CVE-2026-109618/109619 — 5 RCE chains + detection rules (Suricata, Sigma, ModSecurity). PHP session.upload_progress pre-...

? 1574  |  ?? Python  |  _GitHub Search_  `cve-2026-109618` `cve-2026-109619` `detection-rules` `exploit` `php-exploit`

8. ### [JoasASantos/REA-Prompts](https://github.com/JoasASantos/REA-Prompts)

REAP - Prompts for you to use REA (Reverse Engineer Anything), get the most out of it, and clone or break down any progr...

? 1504  |  ?? N/A  |  _GitHub Search_  `prompt-engineering` `rea` `reverse-enginnering`

9. ### [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion)

让你的agent一键直出商业级产品宣传片：会作曲，能指着画面改。Commercial-grade launch films by your coding agent — point at the frame to change it.

? 1468  |  ?? JavaScript  |  _GitHub Search_  `agent-skills` `animation` `claude-code` `codex` `gsap`

10. ### [aicodeking/leanrea](https://github.com/aicodeking/leanrea)

One 8 KB skill that replaces REA (Reverse Engineer Anything): plain CLI tools, no MCP. Benchmarked: 38% faster, 35% chea...

? 1387  |  ?? Python  |  _GitHub Search_  

---

## Hacker News 热门讨论

> 说明：Hacker News 社区当前最热的讨论帖，涉及技术趋势、新工具发布和程序员热点话题。

- [Move Slow and Fix Things](https://endler.dev/2024/move-slow-and-fix-things/)  ?23  by _ahmedhossamdev_
- [Docker is weird](https://codeandcake.dev/posts/2026-10-22-docker-is-weird)  ?289  by _psxuaw_
- [LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification)  ?235  by _johnbender_
- [Quad9 (DNS Resolver) to Exit France](https://quad9.net/news/blog/au-revoir-france/)  ?1093  by _farrokhi_
- [The Secret Life of Circuits is now in stock everywhere](https://blog.coredump.cx/p/the-secret-life-of-circuits-is-now)  ?82  by _surprisetalk_

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
