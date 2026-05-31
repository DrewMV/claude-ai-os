---
level: project
workspace: Work
project: knowledge-scraping
status: active
created: 2026-05-30
updated: 2026-05-30
tags: [work, agile, safe, knowledge]
---

## Goal

Knowledge base of SAFe (Scaled Agile Framework) — 165 source articles distilled into 17 wiki pages covering the full SAFe 6.0 framework.

## Current State

Wiki pages created and ready for ongoing use. The 17 pages cover all major SAFe disciplines, roles, practices, and concepts. Source files remain in `_raw/` for reference.

## Key Decisions

- Distilled 165 scraped SAFe articles into 17 thematic wiki pages rather than creating 165 individual pages
- Organized around disciplines, roles, events, and cross-cutting concerns
- Used `[[wikilinks]]` throughout for cross-referencing between pages
- All source files tagged as `ingested: true` in scrape-registry.json

## Active Context

- Project focus: SAFe 6.0 framework knowledge base
- Source: framework.scaledagile.com (165 articles scraped 2026-05-30)
- Output: 17 wiki pages under `Workspaces/Work/Projects/knowledge-scraping/`
- Tooling available: wiki pages ready for `/wiki-query` queries

## Sources (17 Wiki Pages Created)

| Wiki Page | Description |
|---|---|
| SAFe-overview.md | Big Picture, 5 disciplines, 4 configurations, SAFe 6.0 changes |
| SAFe-core-values-and-principles.md | 4 core values + all 10 Lean-Agile principles |
| SAFe-lean-portfolio-management.md | LPM discipline, funding, governance, 9+ competencies |
| SAFe-team-and-technical-agility.md | Agile Teams, ART, Built-in Quality, CDP, 6 competencies |
| SAFe-product-development-flow.md | Product vision, Lean UX, Design Thinking, 8 competencies |
| SAFe-large-solution-delivery.md | Solution Train, LSID discipline, 6 competencies |
| SAFe-leadership-and-culture.md | Business Agility, dual OS, Kotter's 8 accelerators, CLC |
| SAFe-roles.md | All SAFe roles at team, ART, Solution Train, and portfolio level |
| SAFe-planning-and-events.md | PI Planning, iterations, I&A, WSJF, all ART/team events |
| SAFe-backlogs-and-artifacts.md | 4-tier requirements hierarchy, stories, enablers, NFRs |
| SAFe-flow-and-delivery.md | CDP, flow metrics, Measure and Grow, OKRs |
| SAFe-devops-and-technical-practices.md | CALMR, TDD, BDD, Agile Architecture, Set-Based Design |
| SAFe-implementation-roadmap.md | 13-step implementation roadmap, SAFe customization |
| SAFe-ai-and-emerging-topics.md | AI in SAFe, Responsible AI, AI-augmented workforce, Cloud, Big Data |
| SAFe-governance-and-compliance.md | Lean governance, compliance in Agile, risk, CapEx/OpEx, Government |
| SAFe-roles-and-responsibilities-extended.md | Value streams, customers, CoPs, suppliers, release on demand |
| SAFe-reference-glossary.md | Quick-reference: terms, metrics, events, acronyms |

## Open Questions

- Are there specific SAFe topics the team wants deeper coverage on?
- Should any pages be expanded into sub-pages for specific competencies?
