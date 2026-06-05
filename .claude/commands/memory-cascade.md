Read and synthesize the full memory chain for the current workspace context.

Arguments (optional): $ARGUMENTS
- No argument: read root Memory.md then ask which workspace
- Workspace name (e.g. "Work"): read root + that workspace
- Workspace/project (e.g. "Work/knowledge-scraping"): read full chain to project level

Steps:
1. Read /Memory.md (always, no exceptions)
2. Determine target workspace from $ARGUMENTS or ask: "Which workspace? (Work / Research / Personal)"
3. Read /Workspaces/<workspace>/Memory.md
4. If a project is specified in $ARGUMENTS or mentioned by the user, read /Workspaces/<workspace>/Projects/<project>/Memory.md
5. Synthesize into the output format below — extract what is actionable, do not just concatenate

Output format:
---
Memory Cascade — <workspace>[/<project>]

Global: [2-3 sentences from root Memory.md]
Workspace (<name>): [2-3 sentences from workspace Memory.md]
Project (<name>): [2-3 sentences — only if project was loaded]

Active Context:
• [Most relevant fact or decision for this session]
• [Second most relevant]
• [Third if applicable]

Open Questions:
• [Unresolved items from all levels read]
---

Rules:
- Never modify any Memory.md during a cascade read
- If a Memory.md is missing at any level, note it and continue
- After outputting, ask: "What would you like to work on?"
