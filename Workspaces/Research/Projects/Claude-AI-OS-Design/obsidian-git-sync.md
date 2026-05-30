---
type: concept
workspace: Research
tags: [research, productivity, tool, process]
updated: 2026-05-30
summary: "How to sync an Obsidian vault with GitHub for cross-device access, using the Obsidian Git community plugin and Working Copy on iOS."
base_confidence: 0.92
lifecycle: draft
lifecycle_changed: 2026-05-30
provenance: "Distilled from one Claude conversation (May 2026). High confidence — step-by-step instructions were directly extracted."
---

# Obsidian Git Sync

How to connect an Obsidian vault to GitHub and keep it synced across devices.

## Initial Setup

```bash
# In the vault directory
git init
git add .
git commit -m "initial vault commit"
gh auth login          # or configure SSH keys
git remote add origin https://github.com/<user>/<vault-repo>.git
git push -u origin main
```

## Obsidian Git Plugin

Install the **Obsidian Git** community plugin from Settings → Community Plugins.

Key settings:
- **Auto backup interval** — how often to commit and push (e.g., every 10 minutes)
- **Auto pull interval** — how often to pull from remote (e.g., on startup + every 10 minutes)
- **Commit message template** — e.g., `vault backup: {{date}}`

## .gitignore for Obsidian

Add to `.gitignore` to avoid committing local cache and workspace files:

```
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
.trash/
```

Keep `.obsidian/` config files (themes, plugins, settings) — these should sync so both machines have the same setup.

## Cross-Device Sync

- **Desktop to desktop:** Obsidian Git plugin handles both push and pull automatically
- **Desktop to mobile (iOS):** Use **Working Copy** app — it manages the git repo, and Obsidian opens the vault folder from Working Copy's sandbox
- **Merge conflicts:** The plugin auto-resolves simple conflicts; for complex ones, resolve in a standard git client

## Related Pages

- [[claude-ai-os-architecture]] — this vault uses this sync setup for cross-device access
