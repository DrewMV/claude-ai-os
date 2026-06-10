---
level: project
workspace: Work
project: PPL CMDB-CSDM
status: active
created: 2026-06-01
updated: 2026-06-10
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

**2026-06-10 — Business App enhancements paused:** Team agreed to pause all new Business Application enhancements until Application Services migration is complete. Tony to execute migration off Business Application table and retire legacy records. OCM communications required before changes.

**2026-06-10 — AI tools approved:** Use of AI tools (e.g., Claude) confirmed approved with appropriate approval flow.

**2026-06-10 — HRSD BA change:** Chris Williams is no longer on the project. Lisa Yearick takes over BA responsibilities for HRSD.

**2026-06-10 — Karen rolling off:** Karen Hodges rolling off the project. Impacts NowAssist story assignments (1436576, 1436579, 1436593, 1436592 currently assigned to Karen) and capacity planning for Sprint 2.3+. Reassignment needed.

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

### 🔴 Immediate — Week of June 10

| Owner | Item | Context |
|-------|------|---------|
| Manuel | **Approve Spike 1403733** — identify deprecated plugins/features impacting CMDB capabilities | Anuradha waiting on approval; unblock ASAP |
| Manuel | **Complete Business Value scoring for PI objectives** | Required before ART demo — confirm whether demo has already occurred before actioning |
| Manuel | **Assign owner to Reverse DNS fix** | Program-level risk, currently unowned; escalate to Nolan or OPS |
| Manuel | **Surface Service Mapping app owner validation blocker** | Tanzeel's P1 work stalled not only on CyberArk/infra but also missing app owner sign-off; get name/owner |
| Manuel | Confirm role transition and responsibilities with Sonika | Due June 9 |
| Manuel | Follow up with Joe — NERC SIP CI requirements + CMP documentation | Spike 1402602 unblocks June 9 |
| Manuel | Clarify NowAssist priority with Joe — P2 story-level vs P3 framework | Open question |
| Manuel | Get Joe's decision on SOX Story 1455827 — PI2 committed or PI3? | Active email discussion, no sprint assignment |
| Manuel | Confirm Data Certification OOTB decision formal sign-off owner (Joe / Architecture team) | Decision made in email, not formally recorded |
| Manuel | Confirm Anuradha's access fully resolved — ADO, Dev, SharePoint | Active blocker |
| Alex | Verify overdue credential/access items are closed (Tony, Christian) | Due Jun 4–6, status unknown |

### 🟡 This Sprint — Before June 23

| Owner | Item | Context |
|-------|------|---------|
| Manuel | Schedule Sprint 2.3 end ceremonies — Showback, Retro, Sprint 2.4 Planning (~June 23) | Not on calendar |
| Manuel | Confirm NowAssist 2.3 scope with Joe — all 13 stories or defer Phases 3–5 to 2.4? | Sprint overload risk |
| Manuel | Assign Story 1402976 (Execute Data Cert Policies) to an iteration | No iteration; Priority 1 objective |
| Manuel | Confirm Data Certification UAT date and AC items | UAT scheduled, exact date TBD |
| Manuel | Capture sandbox upgrade version and exact dates from upgrade email | Gates Sprint 2.3 upgrade analysis work |
| Manuel | Formalize or park dashboard capability request as a story | Floating demand, no backlog item |
| Manuel | Log correctness metric data blocker as impediment under Story 1435307 | Blocking Sprint 2.2 acceptance |
| Manuel | Add active impediments to impediments-log.md (correctness data + Anuradha access) | Team tracking |

### 🟠 Backlog Hygiene — ADO Cleanup

| Owner | Item | Context |
|-------|------|---------|
| Manuel | Fix NowAssist feature-level dates for Phases 3–5 | Nolan's risk list — quick hygiene fix |
| Manuel | Resolve duplicate Story 1452028 (assigned to two features) | Backlog data quality |
| Manuel | Close/remove Story 1281209 (OEM Service Map — marked "removed") | Still on board |
| Manuel | Remove duplicate row for Objective 1366662 | Appears twice in backlog |
| Manuel | Assign start/end dates to Data Cert support stories in Sprint 2.3 | Stories in sprint but no dates |

### 🔵 Pending Others — ASAP

| Owner | Item | Context |
|-------|------|---------|
| Christian | Share CR6 detailed focus areas and scope clarifications with Manuel | Still outstanding |
| Manuel | Coordinate with Christian on CCB charter compliance requirements | Open from prior session |
| Manuel | Confirm CMDB health score targets 85–90% formally with Sonika | Blocked on Data Certification confirmation |
| Karen | Quantify OPS team unavailability impact on CMDB backlog + PI-2 story assignments | Still outstanding |
| Karen | Get written confirmation from Narayan on OPS availability and upgrade breakdown | Connects to sandbox dates |

## Open Questions

- Sprint 2.3 end ceremony dates — Showback, Retro, Sprint 2.4 Planning not yet scheduled (~June 23)
- Alex Phan email (Accenture contractor)
- Ruchita Rohini email — verify lprasad@pplweb.com discrepancy
- CR6 detailed scope and focus areas (pending from Christian)
- NowAssist priority — P3 in Sonika's framework but stories tagged P2 in ADO; clarify with Joe today
- CMDB health score targets 85–90% — agreed with Sonika, needs formal confirmation; blocked on Data Certification
- Manuel's ADO access — Anuradha facilitating; partially resolved but access issues still surfaced week of June 5
- Sandbox upgrade version and exact dates — communicated via email, not yet captured
- Data Certification UAT exact date — session scheduled, date TBD
- Dashboard capability request — story or parking decision pending
- ART demo status — has it already occurred? If not, when? Business Value scoring is a hard prerequisite
- Reverse DNS fix — who owns it? Needs escalation if unassigned
- Service Mapping app owner validation — which app owners are missing and who is responsible for chasing them?
