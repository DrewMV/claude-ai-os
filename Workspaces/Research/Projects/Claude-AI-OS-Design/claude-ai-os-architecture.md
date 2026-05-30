---
type: project-note
workspace: Research
project: Claude-AI-OS-Design
tags: [research, ai, productivity, concept]
updated: 2026-05-30
summary: "Design of the Claude AI OS — an Obsidian vault used as an LLM-powered second brain, with Memory.md cascade, workspace/project hierarchy, and ar9av/obsidian-wiki skills."
base_confidence: 0.85
lifecycle: draft
lifecycle_changed: 2026-05-30
provenance: "Distilled from one substantive design-critique conversation (May 2026). Partially inferred — synthesizing the design principles from back-and-forth critique."
---

# Claude AI OS Architecture

Design of the Claude AI OS: an Obsidian vault used as a personal knowledge management system, with Claude Code as the AI agent that reads, writes, and navigates it.

## Core Idea

The vault acts as an **AI second brain**: a structured filesystem that Claude can read from and write to, preserving knowledge across sessions via Memory.md files rather than relying on conversation context.

This is distinct from just using Obsidian for notes — the key differentiator is that Claude Code is the primary reader/writer, and the structure is designed for machine legibility (YAML frontmatter, consistent schemas, skill-based operations) as much as human legibility.

## Memory Cascade

A three-level context loading hierarchy at the start of each session:

1. **Root `Memory.md`** — global context, always loaded
2. **Workspace `Memory.md`** — focus area (Work / Research / Personal)
3. **Project `Memory.md`** — specific initiative context

This solves the "lost context" problem: instead of relying on conversation history (which gets summarized), durable facts are written to Memory.md files and reloaded fresh each session.

## Workspace / Project Hierarchy

```
Workspaces/
├── Work/         ← professional initiatives
├── Research/     ← learning, AI, knowledge building
└── Personal/     ← goals, health, habits
```

Each workspace has projects. Projects are the atomic unit of ongoing work.

## ar9av/obsidian-wiki Skills

The vault uses the [ar9av/obsidian-wiki](https://github.com/ar9av/obsidian-wiki) skill library as its operational toolkit — `/wiki-ingest`, `/wiki-query`, `/cross-linker`, etc. These are installed globally as Claude Code skills.

## Design Critique Notes

^[inferred] The "Karpathy LLM Wiki pattern" referenced in early design documents is misattributed — Karpathy did not write about this specific pattern. The actual design derives from community patterns around LLM-as-archivist.

Key open design questions surfaced in the critique session:
- How to handle wiki page growth over time (when does the vault become too large to load?)
- How to prevent Memory.md files from growing unbounded
- Whether workspace/project boundaries are the right granularity

## Related Pages

- [[obsidian-git-sync]] — how to keep this vault synced across devices
- [[mcp-server-configuration]] — MCP tool setup that powers the vault's web research capabilities
