# Claude OS

This is the root of your personal knowledge workspace. Read this file at the start of every session before doing anything else.

## Operational Rules

> **Tradeoff:** These rules bias toward caution over speed. For trivial tasks, use judgment.

1. **Think Before Coding** — Before acting, state what you assume about the task scope, the active workspace, and which files are in scope. Never act on ambiguous instructions without first making your interpretation explicit.
   - State your assumptions explicitly. If uncertain, ask.
   - If multiple interpretations exist, present them — don't pick silently.
   - If a simpler approach exists, say so. Push back when warranted.
   - If something is unclear, stop. Name what's confusing. Ask.

2. **Simplicity First** — Use the simplest approach that meets the goal. Do not introduce abstractions, extra files, or structural changes beyond what was asked.
   - No features beyond what was asked.
   - No abstractions for single-use code.
   - No "flexibility" or "configurability" that wasn't requested.
   - No error handling for impossible scenarios.
   - If you write 200 lines and it could be 50, rewrite it.
   - Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

3. **Restrict Scope** — Only read or modify files within the active workspace and its projects. Do not traverse other workspaces without explicit instruction.

4. **Surgical Changes** — Touch only what you must. Clean up only your own mess.
   - Don't "improve" adjacent code, comments, or formatting.
   - Don't refactor things that aren't broken.
   - Match existing style, even if you'd do it differently.
   - If you notice unrelated dead code, mention it — don't delete it.
   - Remove imports/variables/functions that YOUR changes made unused — but don't remove pre-existing dead code unless asked.
   - Every changed line should trace directly to the user's request.

5. **Goal-Driven Execution** — Every task must have a stated, checkable outcome. If you cannot define what "done" looks like, ask before starting.
   - Transform imperative tasks into verifiable goals:
     - "Add validation" → "Write tests for invalid inputs, then make them pass"
     - "Fix the bug" → "Write a test that reproduces it, then make it pass"
     - "Refactor X" → "Ensure tests pass before and after"
   - For multi-step tasks, state a brief plan before starting:
     ```
     1. [Step] → verify: [check]
     2. [Step] → verify: [check]
     3. [Step] → verify: [check]
     ```
   - Strong success criteria allow independent looping. Weak criteria ("make it work") require constant clarification.

**These rules are working if:** fewer unnecessary changes appear in diffs, fewer rewrites occur due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

## Vault Structure

```
Claude AI OS/
├── CLAUDE.md                    ← Root rules (you are here)
├── Memory.md                    ← Global context — read every session
├── SETUP.md                     ← First-run setup instructions
├── _meta/
│   ├── schema.md                ← Wiki page schema and conventions
│   ├── taxonomy.md              ← Canonical tag vocabulary
│   └── index.md                 ← Master index of all wiki pages
├── _raw/                        ← Drop raw sources here for ingestion
├── .manifest.json               ← Ingest tracking (do not edit manually)
└── Workspaces/
    ├── Work/
    │   ├── Memory.md            ← Work workspace context
    │   └── Projects/            ← One folder per work initiative
    ├── Research/
    │   ├── Memory.md            ← Research workspace context
    │   └── Projects/            ← One folder per research topic
    └── Personal/
        ├── Memory.md            ← Personal workspace context
        └── Projects/            ← One folder per personal initiative
```

## Memory Cascade

At the start of every session, load context in this order:

1. Read `/Memory.md` — global context, every session, no exceptions
2. Identify the active workspace (ask if not clear from the request)
3. Read `/Workspaces/<workspace>/Memory.md`
4. If the session is project-specific: read `/Workspaces/<workspace>/Projects/<project>/Memory.md`

Do not skip levels. Do not read memory files from workspaces that are not active.

## Skills

Custom skills are in `/.skills/`. ar9av/obsidian-wiki skills are installed globally after running setup.

### Custom Skills (this vault)

| Command | What it does |
|---------|-------------|
| `/workspace-switch <name>` | Load the context for a workspace (Work, Research, Personal) |
| `/project-create <name>` | Create a new project under the active workspace |
| `/memory-cascade` | Read and synthesize the full memory chain |
| `/memory-update` | Write session learnings to the appropriate Memory.md |

### ar9av/obsidian-wiki Skills (installed globally)

| Command | What it does |
|---------|-------------|
| `/wiki-ingest` | Distill documents or files into wiki pages |
| `/ingest-url <url>` | Fetch and ingest a URL into the wiki |
| `/wiki-query <question>` | Answer questions from the wiki |
| `/wiki-update` | Sync current project knowledge into the vault |
| `/wiki-research <topic>` | Multi-round web research, self-filed into wiki |
| `/cross-linker` | Auto-discover and insert missing wikilinks |
| `/wiki-lint` | Find broken links, orphans, contradictions |
| `/wiki-status` | Show what's ingested, what's pending |
| `/daily-update` | Daily maintenance cycle |
| `/wiki-synthesize` | Discover and fill synthesis gaps across concepts |

## Writing to the Wiki

- Every new wiki page must have YAML frontmatter: `workspace`, `tags`, `updated`
- Use `[[wikilinks]]` to cross-reference pages — never bare filenames
- Never rewrite a Memory.md from scratch — merge and preserve existing content
- Sources ingested into a project go into that project's `Sources` section in Memory.md
- Tag vocabulary is defined in `/_meta/taxonomy.md` — use those tags, do not invent new ones
