---
name: project-create
description: Create a new project under a workspace. Initializes the folder structure and a Memory.md, then updates the parent workspace Memory.md to list the new project.
---

# project-create

Create a new project under a workspace.

## Usage

```
/project-create Work/<project-name>
/project-create Research/<project-name>
/project-create Personal/<project-name>
```

If you are already in a workspace context (from `/workspace-switch`), you can omit the workspace prefix:

```
/project-create <project-name>
```

## Steps

1. Confirm the target workspace exists
2. Validate the project name — must be lowercase with hyphens, no spaces (e.g., `q3-planning`, `llm-research`)
3. Check that the project does not already exist at `/Workspaces/<workspace>/Projects/<project-name>/`
4. Create the folder `/Workspaces/<workspace>/Projects/<project-name>/`
5. Create `/Workspaces/<workspace>/Projects/<project-name>/Memory.md` using the template below
6. Read `/Workspaces/<workspace>/Memory.md` and add the new project to the Active Projects section:
   `- <project-name> — Active, just created (<today's date>)`
7. Write the updated workspace Memory.md
8. Confirm creation and show the full path

## Project Memory.md Template

```markdown
---
level: project
workspace: <workspace>
project: <project-name>
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
tags: [<workspace-tag>]
---

## Goal

[State the project goal here. Should be specific and checkable — what does done look like?]

## Current State

Just created. No work logged yet.

## Key Decisions

_No decisions yet._

## Active Context

[What should the agent know before picking this project up mid-session?]

## Open Questions

[What needs to be figured out before meaningful progress can happen?]

## Sources

_No sources ingested yet. Use `/wiki-ingest` or `/ingest-url` to add sources._
```

## Rules

- Never create a project outside of the `/Workspaces/` hierarchy
- Project names must be lowercase-hyphenated — no spaces, no uppercase
- Always update the parent workspace Memory.md after creating the project
- If the user did not provide a goal, leave the template placeholder and note that `/memory-update` should be run once the goal is defined
