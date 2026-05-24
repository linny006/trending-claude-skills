# trending-claude-skills

> Ranking auto-atualizado dos repos claude-skills e agentes de IA mais em alta, atualizado a cada 15 minutos

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · **Português**

[![Stars](https://img.shields.io/github/stars/linny006/trending-claude-skills?style=for-the-badge&logo=github)](https://github.com/linny006/trending-claude-skills/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/trending-claude-skills?style=for-the-badge)](https://github.com/linny006/trending-claude-skills/commits)

---

Um tracker ao vivo que consulta a GitHub Search API em busca de repositórios de habilidades de agentes de IA criados e atualizados recentemente, os ordena por frescor e momentum (não por estrelas acumuladas) e publica um leaderboard no README que se atualiza automaticamente via GitHub Actions.

Esta lista é **atualizada automaticamente a cada 15 minutos** por um cron do GitHub Actions. Cada commit reflete uma mudança real na fonte de dados — novos itens adicionados, itens expirados removidos — então o que você vê está sempre atualizado.

---

A cada 15 minutos, um GitHub Action executa o `tracker.py`. Esse script:

1. Busca o estado mais recente da `GitHub Search API`.
2. Faz um diff contra `data/items.json` (o snapshot anterior).
3. Reescreve a tabela acima entre os marcadores `<!-- TRACKER_TABLE_* -->`.
4. Faz commit com `feat: +N added, -M removed (timestamp)` se houver mudanças.

Sem serviços externos. Sem APIs pagas. Só uma fonte de dados pública e um GitHub Action gratuito.

---

## 📋 Live data

Os dados ao vivo estão no README em inglês

---

## 🔗 Related live trackers

- [mcp-servers-live](https://github.com/linny006/mcp-servers-live) — Live index of newest MCP servers (`topic:mcp-server`)
- [cursor-rules-live](https://github.com/linny006/cursor-rules-live) — Newest Cursor rules and .cursorrules patterns (`topic:cursor-rules`)
- [claude-code-plugin-tracker](https://github.com/linny006/claude-code-plugin-tracker) — Claude Code plugins and hook configs (`topic:claude-code`)
- [llm-agents-radar](https://github.com/linny006/llm-agents-radar) — Newest LLM agent frameworks (`topic:llm-agent`)
- [rag-radar](https://github.com/linny006/rag-radar) — Newest RAG implementations and tools (`topic:rag`)
- [llm-eval-tracker](https://github.com/linny006/llm-eval-tracker) — Newest LLM evaluation tools and benchmarks (`topic:llm-eval`)
- [agent-framework-radar](https://github.com/linny006/agent-framework-radar) — Newest agent frameworks shipping on GitHub (`topic:agent-framework`)
- [vector-db-live](https://github.com/linny006/vector-db-live) — Newest vector DB projects and integrations (`topic:vector-database`)
- [llmops-radar](https://github.com/linny006/llmops-radar) — Newest LLMOps tooling (observability, deployment) (`topic:llmops`)
- [prompt-tools-live](https://github.com/linny006/prompt-tools-live) — Newest prompt-engineering tools and prompt repos (`topic:prompt-engineering`)
- [agent-eval-harness](https://github.com/linny006/agent-eval-harness) — Live benchmark of AI coding agents (`topic:llm-eval`)
- [skills-tracker](https://github.com/linny006/skills-tracker) — Tracking new GitHub 'skills' repos (`topic:agent-skills`)
- [awesome-agent-skills](https://github.com/linny006/awesome-agent-skills) — Curated auto-updated awesome-list of AI agent skills (`topic:agent-skills`)

---

## 📜 License

MIT — see `LICENSE`.
