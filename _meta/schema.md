---
type: meta
updated: 2026-05-30
---

# Wiki Schema

## Page Types

Every wiki page belongs to one of these types. Use the `type` frontmatter field.

| Type | Purpose | Location |
|------|---------|---------|
| `concept` | A reusable idea, pattern, or principle | Any workspace |
| `person` | A person relevant to your work or research | Any workspace |
| `project-note` | Notes tied to a specific project | Under its project folder |
| `reference` | A summarized external source (article, book, paper) | Any workspace |
| `decision` | A recorded decision with rationale and date | Any workspace |
| `question` | An open question worth tracking | Any workspace |
| `meta` | Vault infrastructure (schema, taxonomy, index) | `_meta/` only |

## Required Frontmatter

Every page (except `_meta/` files) must have:

```yaml
---
type: <page-type>
workspace: <Work|Research|Personal>
tags: [<tag1>, <tag2>]
updated: <YYYY-MM-DD>
---
```

Project pages additionally need:

```yaml
project: <project-name>
```

## Wikilinks

- Always use `[[Page Title]]` to link between pages
- Never use relative file paths for cross-references
- If a target page does not exist yet, use the wikilink anyway — it marks a gap to fill

## Source Attribution

When content comes from an external source, add a `sources` block to frontmatter:

```yaml
sources:
  - url: https://...
    title: "Article Title"
    ingested: 2026-05-30
```

## Provenance Tags

Mark inline claims with provenance when the origin matters:

- No tag = directly extracted from source
- `^[inferred]` = LLM synthesis or interpretation
- `^[ambiguous]` = sources disagree on this point
