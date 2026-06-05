---
level: workspace
workspace: Work
updated: 2026-06-05
---

## Purpose

Professional projects, responsibilities, and career context. Everything related to work that is worth preserving across sessions.

## Active Projects

- knowledge-scraping — Active (2026-05-30) — SAFe knowledge base complete: 17 wiki pages from 165 sources
- nerc-cip — Active (2026-06-03) — NERC CIP compliance research; Spike 1402602 blocked pending Joe Dames return
- ServiceNow/CMDB-CSDM — Active (2026-06-05) — PI2 in progress; Sprint 2.2 closes 6/9, Sprint 2.3 starts 6/10

## Key Context

- **SAFe knowledge base** is live in knowledge-scraping project. Use `/wiki-query` to search it.
- Scraping infrastructure in place: `/scrape-url` skill + `_meta/scrape-registry.json` for dedup.
- **CMDB-CSDM role:** Manuel Vazquez (SM), co-SM Alex Phan, PO Joe Dames. Team works with EVT SMEs.
- **PI2 top priorities:** (1) CI Data Certification Program, (2) Regulatory/Security integrations (Qualys, NERC-CIP), (2) Service Mapping + Discovery Coverage, (3) NowAssist AI activation
- **Sprint 2.3 risks:** NowAssist overloaded (13 stories), SCCM carry-over from 2.2, Data Certification implementation gaps, NERC-CIP spike unplanned

## Recurring Themes

- CI ownership gaps — recurring across Server, Computer, and governance features
- Authoritative source conflicts — SCCM precedence, IRE behavior, attribute "flapping"
- Dependency on external teams — Qualys, Airlift migration, EVT SMEs

## Open Questions

- When is Joe Dames back? (NERC-CIP spike + Data Certification planning blocked)
- Is NowAssist 2.3 scope realistic, or should Phases 3–5 move to 2.4?
- Are unplanned backlog items (SOX notification, network device config stories) PI2 committed or PI3?
- What is the exact ServiceNow upgrade version and sandbox date? (gates Sprint 2.3 upgrade analysis work)
- Data Certification OOTB decision — who owns formal sign-off? (Joe Dames / Architecture team)
- SOX notification Story 1455827 — priority decision needed from Joe before it becomes an unspoken expectation
- Dashboard capability request — create story or formally park it?
- Is Anuradha Rai's access fully resolved (ADO, Dev, SharePoint)?

## Decisions Made

- **Data Certification: Stay OOTB** — No customization of OOB certification code. Train users instead. Agreed week of June 5, 2026 via email. Formal sign-off pending.
