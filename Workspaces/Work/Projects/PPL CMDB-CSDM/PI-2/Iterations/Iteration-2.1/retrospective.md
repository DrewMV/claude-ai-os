---
type: ceremony
ceremony: retrospective
pi: PI-2
iteration: 2.1
iteration-start: 2026-05-13
iteration-end: 2026-05-26
date: 2026-05-26
status: completed
workspace: Work
project: CMDB-CSDM
attendees: [Alex Phan (SM - facilitator), Joe Dames (PO), Bhushan Salsekar (TL), Tanzeel Rehman (TL), Stan Tomberg (TL), Dev Team]
tags: [work, agile, safe, retrospective, cmdb-csdm]
---

# Retrospective — Iteration 2.1

> **Status: COMPLETED** — Backfill notes if available.

## What Went Well

- Strong Daily Standup structure and consistency throughout iteration
- Clear leadership and direction from Alex Phan (SM)
- Good ADO hygiene — tracking, ownership, accountability maintained
- Effective collaboration across onshore, offshore, and contractor resources
- Successful transition from PI Planning into structured execution
- Dependency-sequenced task breakdown shows disciplined delivery governance

## What Didn't Go Well

- Credential dependencies (SNMP, CyberArk) unresolved all iteration — blocked discovery accuracy and service mapping
- Post-clone data integrity gaps identified late (Major Incident templates missing) — raised questions about validation process rigor
- Service Mapping blocked by missing credentials and environment restrictions for full iteration
- External team responsiveness (Network, Ops) created unpredictable delivery risk
- Discovery strategy (DEV/QA vs PROD) debated but never formally documented or resolved
- Delivery remained highly dependency-driven with limited ability to pull ahead on work

## Action Items

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| Confirm post-clone completeness — validate all CMDB objects, templates, relationships intact | TBD | Iter 2.2 | Open |
| Confirm SNMP credentials fully working across all device types | TBD | Iter 2.2 | Open |
| Confirm CyberArk integration complete and credentials propagated across environments | TBD | Iter 2.2 | Open |
| Document and get approval on discovery/testing strategy (DEV/QA vs PROD) | TBD | Iter 2.2 | Open |
| Resolve all credential and access issues blocking Service Mapping | TBD | Iter 2.2 | Open |
| Finalize Data Certification pilot scope, data inputs, and reporting alignment | TBD | Iter 2.2 | Open |
| Identify and escalate stalled external dependency requests (Network, Ops) | Alex Phan | Iter 2.2 | Open |

## Team Health (1-5)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Collaboration | | Cross-functional collaboration noted as strong across global team |
| Clarity | | Discovery strategy gap and unresolved credentials suggest room to improve |
| Morale | | |
| Technical Quality | | ADO hygiene strong; post-clone validation gaps noted |

## Carry Forward from Last Retro

_First iteration of PI2 — no prior retro items._
