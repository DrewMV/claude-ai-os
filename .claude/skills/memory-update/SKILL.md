---
name: memory-update
description: Write what was learned or decided during a session into the appropriate Memory.md. Determines the right level automatically based on the scope of the new information.
---

# memory-update

Persist session learnings to the correct Memory.md level.

## Usage

```
/memory-update                  # auto-determine level from session context
/memory-update project          # force write to project Memory.md
/memory-update workspace        # force write to workspace Memory.md
/memory-update root             # force write to root Memory.md
```

## Level Decision Rules

Write at **project level** when the new context is:
- Specific to the current project (a decision, a discovery, a blocker)
- A source that was ingested for this project
- A status change for this project

Write at **workspace level** when the new context is:
- A pattern that applies across multiple projects in this workspace
- A constraint or standing fact true for the whole workspace
- A recurring theme that has now appeared in at least two projects

Write at **root level** when the new context is:
- A concept or principle that applies across workspaces
- A preference or rule that should hold everywhere
- A cross-workspace decision

When in doubt, write at the most specific level that applies.

## Steps

1. Review the current session — what was learned, decided, or discovered that is worth keeping?
2. Filter out ephemeral details — keep only what would still matter in 3 months
3. Determine the target level using the decision rules above
4. Read the target Memory.md
5. Merge new information into the relevant sections:
   - New decisions → **Key Decisions**
   - New status → **Current State**
   - Questions that were answered → remove from **Open Questions**
   - New unresolved questions → **Open Questions**
   - New ingested sources → **Sources** (project level only)
   - New recurring theme → **Recurring Themes** (workspace level)
6. Update the `updated` frontmatter date to today
7. Write the file
8. Confirm what was added and to which level

## Rules

- Never rewrite a Memory.md from scratch — merge and preserve existing entries
- Never add speculation — only document what was actually decided, learned, or confirmed
- Keep each entry to one or two sentences
- Do not duplicate information that already exists in the file
- If the same information belongs at two levels, write a brief entry at both — do not skip the more specific level
