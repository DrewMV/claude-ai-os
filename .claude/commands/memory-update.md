Write what was learned or decided during this session into the appropriate Memory.md level.

Optional level argument: $ARGUMENTS (project / workspace / root)
If no argument, auto-determine the level from session context.

Level decision rules:
- Write at PROJECT level: decision or discovery specific to current project, source ingested, status change
- Write at WORKSPACE level: pattern spanning multiple projects, workspace-wide constraint or theme
- Write at ROOT level: concept applying across workspaces, global preference or rule

Steps:
1. Review the current session — what was learned, decided, or discovered worth keeping?
2. Filter: keep only what would still matter in 3 months. Drop ephemeral details.
3. Determine target level using $ARGUMENTS or decision rules above
4. Read the target Memory.md
5. Merge new information into sections:
   - New decisions → Key Decisions
   - Status changes → Current State
   - Answered questions → remove from Open Questions
   - New unresolved items → Open Questions
   - New sources → Sources (project level only)
   - Recurring patterns → Recurring Themes (workspace level only)
6. Update the `updated` frontmatter date to today
7. Write the file
8. Confirm what was written and at which level

Rules:
- Never rewrite Memory.md from scratch — merge and preserve existing entries
- Never add speculation — only document what was actually decided, learned, or confirmed
- Keep each entry to 1-2 sentences
- Do not duplicate information already in the file
- Always update the `updated` date field
