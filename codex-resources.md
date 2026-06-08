# Codex 生态资源手册

> 本文档是 Codex 工具链的学习笔记和资源索引，与 digest.py 配合使用。

---

## 📦 核心概念

| 概念 | 说明 |
|------|------|
| **Skill** | 可复用的行为指南，存储在 SKILL.md 中，按场景触发 |
| **Plugin** | Skill + MCP Server + App 的打包单元 |
| **AGENTS.md** | 项目级指令文件，指导 AI 代理的行为规范 |
| **MCP Server** | Model Context Protocol 服务器，扩展 AI 能力边界 |

## 🛠 常用命令

`
codex skills list                    # 列出已安装技能
codex skills search <keyword>        # 搜索技能
codex install <name>                 # 安装技能
codex agent                          # 启动代理模式
`

## 📚 Skill 分类推荐

### 开发效率
- \yeet\ — 一键提交 → 推送 → 建 PR
- \gh-address-comments\ — 处理 PR Review 反馈
- \gh-fix-ci\ — 修复 CI 失败
- \changelog-generator\ — 从 git 日志生成更新日志

### 前端 / Web
- \uild-web-apps\ — 前端应用构建全套技能
- \shadcn\ — shadcn/ui 组件管理
- \igma-implement-design\ — Figma 设计稿转代码

### AI / LLM
- \llm-application-dev\ — LLM 应用开发指南
- \mcp-builder\ — 构建 MCP Server

### 运维 / 部署
- \ercel-deploy\ — 部署到 Vercel
- \cloudflare-deploy\ — 部署到 Cloudflare
- ender-deploy\ — 部署到 Render

### 内容 / 文档
- \code-documentation\ — 编写高质量文档
- \presentations\ — 创建 PPTX 演示文稿
- \spreadsheets\ — 创建和编辑电子表格

## 🔗 官方资源

- [Codex GitHub 仓库](https://github.com/openai/codex)
- [OpenAI 平台文档](https://platform.openai.com/docs)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

## 📝 个人笔记

> *（在此记录你自己的 Codex 使用心得）*

`
2026-06-08: 初始化资源手册
`
