Create a new project under a workspace with the correct folder structure and an initialized Memory.md.

Project path from arguments: $ARGUMENTS
Expected format: Work/<project-name>, Research/<project-name>, or Personal/<project-name>
If workspace is omitted, ask which workspace to use.

Steps:
1. Parse $ARGUMENTS to extract workspace and project-name
2. Validate: project name must be lowercase-hyphenated (no spaces, no uppercase)
3. Check the project does not already exist at /Workspaces/<workspace>/Projects/<project-name>/
4. Create the folder /Workspaces/<workspace>/Projects/<project-name>/
5. Create /Workspaces/<workspace>/Projects/<project-name>/Memory.md using the template below
6. Read /Workspaces/<workspace>/Memory.md and add to Active Projects:
   "- <project-name> — Active, created <today's date>"
7. Write the updated workspace Memory.md
8. Confirm creation and show the full path

Memory.md template to write:
---
level: project
workspace: <workspace>
project: <project-name>
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
tags: [<workspace-lowercase>]
---

## Goal

[State the project goal here — what does done look like?]

## Current State

Just created. No work logged yet.

## Key Decisions

_No decisions yet._

## Active Context

[What should the agent know before picking this project up mid-session?]

## Open Questions

[What needs to be resolved before meaningful progress can happen?]

## Sources

_No sources ingested yet. Use /wiki-ingest or /ingest-url to add sources._

Rules:
- Never create a project outside of the /Workspaces/ hierarchy
- Project names must be lowercase-hyphenated
- Always update parent workspace Memory.md after creation
