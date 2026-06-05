---
level: project
workspace: Work
project: CMDB-CSDM
status: active
created: 2026-06-01
updated: 2026-06-03
tags: [work, agile, safe, cmdb-csdm, servicenow]
---

## Goal

Track and manage the CMDB-CSDM team's delivery from the Scrum Master and PO Support perspective across PI2 and PI3, including team ceremonies, ART interactions, cross-team dependencies, and process improvement identification.

## Current State

Active in PI2, Iteration 2.2 (May 27 – Jun 9, 2026). Joe Dames is out this week; returning Tuesday 2026-06-09.

## ART Context

| Role | Name |
|------|------|
| RTE | Nolan LeBlanc |
| Systems Architect | Joe Dunn |
| ART Coach | Tom Westervelt |
| Value Stream Business Lead | Dan Johnson |
| Value Stream IT Lead | Todd Dierksheide |

**Business Owners:** Dave Quier, Alan LaBarre, Tom Jessee, Tina Rauch, Gregory Belanger, Salim Salet

## CMDB-CSDM Team

| Name | Title | Location |
|------|-------|---------|
| Sonika Das | Product Manager (EVT) | — |
| Joe Dames | Solution Architect / PO | Onshore |
| Alex Phan | Scrum Master (transitioning to ITSM primary focus 2026-06-09; continuing CMDB support during transition) | Onsite / PPL |
| Manuel Vazquez (Manny) | Scrum Master / PO Support (hybrid — effective 2026-06-09; leading CMDB ceremonies, delivery tracking, backlog support with Joe) | — |
| Stan Tomberg | CMDB Discovery / Senior IS (Architect) | Onshore |
| Tanzeel Rehman | Team Lead Service Mapping | Onshore |
| Bhushan Salsekar | Implementation Specialist | Offshore |
| Kiran Dhobale | Implementation Specialist | Offshore |
| Vinay Geddannavar | Implementation Specialist | Offshore |
| Tony De Araujo | Developer | Onshore |
| Venkateswarlu Manikanta | QA Tester | Offshore |
| Ruchita Rohini | Project Manager | Offshore |
| Anuradha Rai (Anu) | Functional Designer | Offshore |
| Uloma Adelufosi | Product Analyst | Onshore |
| Roland Wornor | SME (EVT) | — |
| Laurent Israel Shlomi | SME (EVT, shared with SNOW Enhancements) | — |
| Benjamin Walczyk | SME (EVT) | — |
| Tricia L Hicks | SME (EVT, rolling off another project) | — |

## Accenture Delivery Leadership

| Name | Role |
|------|------|
| Chris | Accenture delivery manager overseeing Manuel and Alex; directed the role transition and org changes |
| Christian Aguilar Rodriguez | Account Manager / Service Delivery; coordinating scope clarifications and CR6 role segmentations |
| Aaron Simeon | Contract role segmentation contact for CR6 (coordinating with Christian) |
| Narayan | OPS team contact; point of contact for upgrade activity scheduling and team availability confirmations |
| Kostas | Change management coordination; owns any follow-on process changes post-approval |
| Ray Reuter | Server support group assignments; point of contact for new P1 story on assigning support groups to servers |
| Pepper | IAM team; contact for SOX-flagged CI ownership change notification content and recipients |

## Contract Context

| Contract | Status | Notes |
|----------|--------|-------|
| CR5 | Current | Active contract; scope discrepancies being addressed |
| CR6 | Upcoming | New contract; role segmentations being confirmed with Aaron Simeon |

Christian will provide Manuel with detailed focus areas for delivery under CR6.

## ServiceNow Product Line Peers

| Team | Product Owner | Scrum Master | Tech Lead |
|------|--------------|-------------|----------|
| ServiceNow Enhancements | JP Nair | Karen Hodges | Hari Medikondu |

## Active PIs

| PI | Start | End | Status |
|----|-------|-----|--------|
| PI-2 | 2026-05-13 | 2026-08-04 | Active |
| PI-3 | 2026-08-05 | 2026-10-27 | Future |

## Priority Framework (Sonica-set)

| Priority | Focus Area | Owner |
|----------|-----------|-------|
| P0 | Airlift / migration stories | Laurent, Alex Lim |
| P1 | Service Mapping + server class data fixes | Tanzeel |
| P2 | Regulatory / security integrations (Qualys) | Stan |
| P3 | Now Assist AI feature | TBD |

Data certification is a hot topic and largely developed; feedback incorporation ongoing (Bhushan).

## Key Decisions

**2026-06-09 — SM Role Transition:** Alex Phan shifts primary focus to ITSM (working with JP Nair, Karen Hodges, Sonika Das, and ITSM stakeholders). Manuel takes over as CMDB Scrum Master in a "Scrum Master Plus" hybrid role — 100% SM responsibilities plus PO support alongside Joe Dames (translating technical priorities into business value, coordinating work assignments, demand intake support). Manuel will also interface with JP and Karen on ITSM-related matters alongside Alex. Alex continues to support CMDB during transition. Sonika Das is aligned and supports the role changes, including Manuel taking on PO-adjacent tasks. Confirmed in 2026-06-03 meeting with Chris, Christian, Alex, and Manuel.

**2026-06-03 — CMDB Management Plan (CMP) identified as audit compliance need:** Manuel raised the need for a documented CMP defining CI classes, attributes, and health targets to support audit readiness. Follow-up with Joe on NERC SIP CI requirements. Not yet formally tracked as a deliverable — needs scoping with Joe and Sonica.

**2026-06-03 — Process Improvement Mandate:** Manuel is explicitly tasked with evaluating SAFe Agile overhead on this project, identifying inefficiencies and blockers, and escalating to Christian and Sonika. Sonika is open to feedback and improvements in the delivery process.

_See [[PI-2/Memory]] for PI-level decisions._

## Key References

- [[Team/working-agreements]] — full team roster, emails, onshore/offshore split
- [[Team/capacity]] — iteration velocity tracker
- [[Team/impediments-log]] — active and resolved blockers
- [[Backlog/features]] — features mapped to PI objectives
- [[Backlog/definition-of-ready]] — story readiness gates
- [[Backlog/definition-of-done]] — story acceptance criteria
- [[requirements-process]] — end-to-end requirements flow
- [[Dependencies/servicenow-enhancements]] — cross-team dependency tracker
- [[nowassist-implementation-plan]] — 5-phase NowAssist AI roadmap (Duplicate CI Elimination → NL Search → Guided CI Creation → Governance Advice → NASK); primary driver for PI-2 Obj 5 and PI-3 objectives

## Open Action Items

| Owner | Item | Due |
|-------|------|-----|
| Manuel | Confirm role transition and responsibilities with Sonika | 2026-06-09 |
| Manuel | Begin CMDB SM role and ceremonies | 2026-06-09 |
| Alex | Validate metal tier field customization; clarify data classification vs. SOX indicator | 2026-06-04 |
| Alex | Coordinate credential fix with Tony/Christian; confirm resolution via email | 2026-06-06 |
| Alex | Provide Laurent and Alex Lim with ServiceNow access | 2026-06-06 |
| Alex | Follow up with Joe on outstanding issues (Joe returns) | 2026-06-09 |
| Alex | Provide Manuel with credentials and system access | 2026-06-06 |
| Tony | Resolve ServiceNow credential issues | 2026-06-06 |
| Christian | Send credential issue updates to Alex, Todd, and others | 2026-06-06 |
| Christian | Share detailed focus areas and scope clarifications with Manuel | ASAP |
| Christian | Coordinate with Aaron Simeon to confirm role segmentations in CR6 | ASAP |
| Karen | Quantify OPS team unavailability impact on CMDB backlog; analyze PI-2 story assignments | ASAP |
| Karen | Obtain written confirmation from Narayan on OPS availability and upgrade breakdown | ASAP |
| Manuel | Follow up with Joe on NERC SIP CI requirements and CMP documentation | ASAP (Joe returns 2026-06-09) |
| Manuel | Coordinate with Christian on CCB charter and compliance requirements | ASAP |

## Open Questions

- Specific ceremony dates within each iteration (pending confirmation from Manuel / Joe Dames)
- Alex Phan email (Accenture contractor)
- Ruchita Rohini email — verify lprasad@pplweb.com discrepancy
- CR6 detailed scope and focus areas (pending from Christian)
- Now Assist priority: listed as P3 in framework but individual stories approved as "P2 priority" by Manuel — clarify with Anu or Joe whether Now Assist was promoted or if P2 refers to a story-level ADO field
- CMDB health score targets (85–90% previously agreed with Sonica) — need formal confirmation; compliance measurement blocked pending data certification
- Manuel's ADO access and PPL stakeholder list — Anu facilitating, currently blocked
