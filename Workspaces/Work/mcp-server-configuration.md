---
type: concept
workspace: Work
tags: [work, engineering, tool]
updated: 2026-05-30
summary: "How to configure MCP servers for Claude Code and Claude Desktop, including the session-restart requirement and key config file locations."
base_confidence: 0.90
lifecycle: draft
lifecycle_changed: 2026-05-30
provenance: "Distilled from ~6 Claude conversations (May 2026) where Firecrawl and NotebookLM MCP setup was repeatedly troubleshot. High confidence — same pattern confirmed across multiple sessions."
---

# MCP Server Configuration

Patterns for setting up MCP (Model Context Protocol) servers in Claude Code and Claude Desktop.

## Key Config Files

| File | Scope | Purpose |
|---|---|---|
| `~/.claude/settings.json` | CLI (all projects) | Global MCP server definitions |
| `~/.claude/settings.local.json` | CLI (all projects) | Local overrides, permission allowlists |
| `%APPDATA%\Claude\claude_desktop_config.json` | Desktop app | MCP server definitions for desktop |

## Critical Pattern: Session Restart Required

**Adding or modifying MCP server config does not take effect in the current session.** The new config is only picked up when a fresh conversation is opened.

- In Claude Code CLI: open a new terminal session / start a new conversation with `Ctrl+N`
- In Claude Desktop: restart the app or open a new conversation

This caused repeated confusion across multiple sessions — the config was correct but MCP tools were still not showing because the session was stale. ^[extracted]

## Installed MCP Servers (as of May 2026)

- **Firecrawl** — web scraping, search, crawling via Firecrawl API
- **NotebookLM** — research via Google NotebookLM notebooks
- **mcp-registry** — lists and searches available MCP connectors

## Verifying MCP Visibility

Ask Claude "can you see [tool name]?" — it will list available tools. If the tool isn't listed despite correct config, the fix is always to open a new conversation.

## Related Pages

- [[claude-ai-os-architecture]] — the broader Claude Code + vault setup this sits within
