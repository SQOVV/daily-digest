# My Daily Digest - 2026-10-18

> Sources: GitHub Search, GitHub Trending, Hacker News

---

## GitHub 热门开源项目

> 说明：近7天新创建的 GitHub 仓库，按 Star 增长速度排名。适合发现新兴工具、热门框架和有趣的开源项目。

1. ### [jhaizhou-ops/d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile)

Open-source iOS / macOS compatibility layer for Diablo II: Resurrected with the Reign of the Warlock expansion. Runs you...

? 3741  |  ?? C  |  _GitHub Search_  `compatibility-layer` `diablo-2-resurrected` `diablo2` `game-port` `ios`

2. ### [Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)

Qwen-Image 2.1 NSFW/姿势出图 skill：作者级提示词配方 + NSFW LoRA + 136 姿势 VNCCS 人偶控制；适用 Claude Code / Codex / Cursor / OpenClaw

? 2661  |  ?? Python  |  _GitHub Search_  `agent-skill` `comfyui` `image-generation` `openclaw` `pose-control`

3. ### [HeyPuter/everything](https://github.com/HeyPuter/everything)

We're rebuilding and open-sourcing the world’s software from scratch.

? 2082  |  ?? JavaScript  |  _GitHub Search_  `adobe` `cad` `office` `photoshop` `saas`

4. ### [deeplethe/solid-glass](https://github.com/deeplethe/solid-glass)

A design system for AI applications. Material, physical, tactile, technical.

? 1826  |  ?? TypeScript  |  _GitHub Search_  `agent-ui` `ai` `ai-agents` `chat-ui` `design-system`

5. ### [ahwootech/BRUTAL](https://github.com/ahwootech/BRUTAL)

A free, open source C# framework for making games, or your own game engine. Direct access to native APIs and Vulkan, wit...

? 1812  |  ?? C#  |  _GitHub Search_  `csharp` `dotnet` `game-engine` `gamedev` `vulkan`

6. ### [chenglou/handwired](https://github.com/chenglou/handwired)

Turn your regular JavaScript code into a neural net.

? 1686  |  ?? TypeScript  |  _GitHub Search_  

7. ### [Supermedo/uncharted_pc](https://github.com/Supermedo/uncharted_pc)

Uncharted: The Nathan Drake Collection running natively on Windows - by SuperMedo

? 1291  |  ?? C++  |  _GitHub Search_  

8. ### [feder-cr/git-ai](https://github.com/feder-cr/git-ai)

Git designed for AI agents.

? 1148  |  ?? Go  |  _GitHub Search_  `ai-agents` `coding-agents` `git` `golang` `scion`

9. ### [Caho1/open-claude-ui](https://github.com/Caho1/open-claude-ui)

基于 REA 深度拆解并高保真还原 Claude 官方桌面端 UI。还原 30 个独立 React 组件与 8 项硬核交互物理算法，附带 3000+ 行逆向分析手册。

? 1146  |  ?? TypeScript  |  _GitHub Search_  `anthropic` `audioworklet` `claude` `design-system` `framer-motion`

10. ### [zhuyansen/new-term-radar](https://github.com/zhuyansen/new-term-radar)

Daily radar for new AI terms: names of new models, products and repos, caught on X, Hugging Face, GitHub and sitemaps be...

? 1086  |  ?? Python  |  _GitHub Search_  `agent-skills` `ai` `aisa` `claude-code` `claude-skills`

---

## Hacker News 热门讨论

> 说明：Hacker News 社区当前最热的讨论帖，涉及技术趋势、新工具发布和程序员热点话题。

- [Show HN: Sphinx – a hook that quizzes you on your AI's code before shipping](https://sphinx-six-theta.vercel.app/)  ?12  by _critiquebrowser_
- [Bleached corals thrive within days when touching healthy neighbour](https://www.nature.com/articles/d41586-026-03266-x)  ?392  by _alkyon_
- [Lean now ships with verified kernels](https://leodemoura.github.io/blog/2026-10-15-lean-now-ships-with-verified-kernels/)  ?69  by _matt_d_
- [Dam removals are bringing fish back across the northeastern United States](https://www.smithsonianmag.com/science-nature/dam-removals-are-bringing-fish-back-across-the-northeastern-united-states-striking-down-one-tiny-barrier-at-a-time-180989679/)  ?243  by _sohkamyung_
- [DeepSeek-v4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)  ?776  by _theykk_

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
