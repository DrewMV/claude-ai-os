Activate a workspace and load its memory context.

Workspace name from arguments: $ARGUMENTS
Valid values: Work, Research, Personal

Steps:
1. Confirm /Workspaces/$ARGUMENTS/ exists
2. Read /Memory.md (root)
3. Read /Workspaces/$ARGUMENTS/Memory.md
4. Extract the Active Projects list from the workspace Memory.md
5. Output the combined context summary below
6. State which workspace is now active

Output format:
---
Active Workspace: $ARGUMENTS

Global Context:
[2-3 sentences from root Memory.md — what applies everywhere]

Workspace Context:
[2-3 sentences from workspace Memory.md — what defines this domain]

Active Projects:
- <project-name> — <one-line status>
(list "None yet" if no projects exist)

Ready. What would you like to work on?
---

Rules:
- Do not read project Memory.md files unless the user specifies a project
- Do not read Memory.md files from other workspaces
- If workspace name is missing from $ARGUMENTS, ask: "Which workspace? (Work / Research / Personal)"
