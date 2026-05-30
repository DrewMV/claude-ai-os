---
name: workspace-switch
description: Activate a workspace and load its memory context. Reads root Memory.md and the target workspace Memory.md, then outputs a combined session context.
---

# workspace-switch

Switch the active workspace and load its context chain.

## Usage

```
/workspace-switch Work
/workspace-switch Research
/workspace-switch Personal
```

## Steps

1. Confirm the workspace exists at `/Workspaces/<name>/`
2. Read `/Memory.md` (root level)
3. Read `/Workspaces/<name>/Memory.md`
4. Extract the Active Projects list from the workspace Memory.md
5. Output the combined context summary below
6. State which workspace is now active and what projects are available

## Output Format

```
Active Workspace: <name>

Global Context:
[2-3 sentence summary of root Memory.md — what applies everywhere]

Workspace Context:
[2-3 sentence summary of workspace Memory.md — what defines this domain]

Active Projects:
- <project-name> — <one-line status>
- ...
(none if no projects exist yet)

Ready. What would you like to work on?
```

## Rules

- Do not read project Memory.md files unless the user specifies a project
- Do not read Memory.md files from other workspaces
- If `/Workspaces/<name>/Memory.md` is missing, note it and offer to create it using the workspace Memory.md template
- The valid workspace names are: Work, Research, Personal
