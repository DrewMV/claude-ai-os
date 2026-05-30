---
name: memory-cascade
description: Read and synthesize the full memory chain from root to workspace to project. Use at the start of a session to load context before starting work.
---

# memory-cascade

Read the memory hierarchy and return a synthesized context summary.

## Usage

```
/memory-cascade                            # reads root + asks which workspace
/memory-cascade Work                       # reads root + Work workspace
/memory-cascade Research/llm-research      # reads root + Research + llm-research project
```

## Steps

1. Read `/Memory.md` (always)
2. Determine the target workspace:
   - If specified in the command, use it
   - If not specified, ask: "Which workspace are you working in? (Work / Research / Personal)"
3. Read `/Workspaces/<workspace>/Memory.md`
4. If a project is specified or the user mentions one:
   - Read `/Workspaces/<workspace>/Projects/<project>/Memory.md`
5. Synthesize into the output format below — do not just concatenate the files, extract what is actionable right now

## Output Format

```
Memory Cascade — <workspace>[/<project>]
─────────────────────────────────────────

Global:
[2-3 sentences summarizing root Memory.md — what is true across all workspaces]

Workspace (<name>):
[2-3 sentences summarizing the workspace — its focus and any standing context]

Project (<name>):        ← only if a project was loaded
[2-3 sentences on goal, current state, and what's blocking progress]

Active Context:
• [Most relevant fact or decision for this session]
• [Second most relevant]
• [Third most relevant — omit if fewer than 3 exist]

Open Questions:
• [Combined unresolved items from all levels read]
```

## Rules

- Do not read memory files from workspaces or projects not in the specified chain
- If a Memory.md is missing at any level, note it and continue — do not fail
- Never modify any Memory.md during a cascade read
- Keep the output concise — this is a context load, not a report
- After outputting, ask: "What would you like to work on?"
