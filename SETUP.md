# Setup Guide

## Step 1 — Install ar9av/obsidian-wiki

Open a terminal and run:

```bash
pip install obsidian-wiki
obsidian-wiki setup --vault "C:\Users\manuel.b.vazquez\Documents\Claude AI OS"
```

This writes your vault path to `~/.obsidian-wiki/config` and symlinks all wiki skills into Claude Code and any other agents you have installed.

Verify the install:

```bash
obsidian-wiki list    # shows all available skills
obsidian-wiki info    # shows install paths and vault config
```

## Step 2 — Open the Vault in Obsidian

1. Open Obsidian
2. Click "Open folder as vault"
3. Select `C:\Users\manuel.b.vazquez\Documents\Claude AI OS`

Obsidian will create a `.obsidian/` folder automatically. The first open may be slow while it indexes.

Recommended Obsidian plugins to enable (Community Plugins):
- **Dataview** — query your notes as a database
- **Templater** — for project Memory.md templates
- **Graph Analysis** — enhanced graph view metrics

## Step 3 — Initialize the Wiki in Claude Code

Open this folder in Claude Code, then run:

```
/wiki-setup
```

This initializes the ar9av vault structure (_meta, _raw, .manifest.json) and confirms everything is wired correctly.

## Step 4 — First Session

Start a session and say:

```
/memory-cascade
```

This reads root Memory.md and asks which workspace you are working in. After that, you are ready to work.

## Step 5 — Create Your First Project

To create a project:

```
/project-create <workspace>/<project-name>
```

Example:
```
/project-create Work/q3-planning
```

## Daily Workflow

| When | Command | What it does |
|------|---------|-------------|
| Session start | `/workspace-switch <name>` | Load workspace context |
| Working | `/wiki-update` | Sync learnings to vault |
| Adding source | `/wiki-ingest` or `/ingest-url <url>` | Add to knowledge base |
| Asking questions | `/wiki-query <question>` | Pull from vault |
| Session end | `/memory-update` | Persist session context |
| Daily | `/daily-update` | Maintenance + freshness pass |

## Upgrading ar9av Skills

```bash
pip install -U obsidian-wiki
obsidian-wiki setup --vault "C:\Users\manuel.b.vazquez\Documents\Claude AI OS"
```
