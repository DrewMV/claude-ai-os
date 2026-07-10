---
level: project
workspace: Work
project: PPL CMDB-CSDM
status: active
created: 2026-06-01
updated: 2026-07-10
tags: [work, agile, safe, cmdb-csdm, servicenow]
---

## Goal

Track and manage the CMDB-CSDM team's delivery from the Scrum Master and PO Support perspective across PI2 and PI3, including team ceremonies, ART interactions, cross-team dependencies, and process improvement identification.

## Current State

Active in PI2, Iteration 2.3 (Jun 10 – Jun 23, 2026). Data Certification UAT signed off by Sonika (6/10); deployment targets PROD 06/23. Service Mapping discovery now active — credentials resolved, single test subnet complete, additional scans in progress. CCB Meeting 06/16; CMDB Audit Sync 06/18.

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
| Jordan Yung | Program Manager / Delivery Lead — supports Christian as a DL; heavily involved in **CO6** development. Key resource for the scope & purpose of deliverables going forward. Highly active on Service Mapping, Airlift, and cross-team CMDB coordination. |
| Narayan | OPS team contact; point of contact for upgrade activity scheduling and team availability confirmations |
| Kostas | Change management coordination; owns any follow-on process changes post-approval |
| Ray Reuter | Server support group assignments; point of contact for new P1 story on assigning support groups to servers |
| Pepper | IAM team; contact for SOX-flagged CI ownership change notification content and recipients |

## Contract Context

| Contract | Status | Notes |
|----------|--------|-------|
| CR5 / CO5 | Current | Active contract (signed **Change Order #5**, executed 2026-05-26). Term Mar 31 → **Jun 30, 2026**. Deliverable acceptance tracked in [[co5-deliverable-tracking]]; signed PDF at [[Contract/CO5-signed-2026-05-26.pdf]]. **$533,775 June holdback** gated on final acceptance. Scope discrepancies being addressed. |
| CR6 / CO6 | Upcoming — **DRAFT/unsigned** | **Change Order #6**, proposed term Jul 1 → **Oct 30, 2026**. Re-baselines the at-risk CO5 deliverables (Databases, 90% coverage, Qualys) to Jul 31 → Oct 30 and adds **ITSM PO + Platform Support (BAU) + ATF** workstreams. Tracked in [[co6-deliverable-tracking]]; draft at [[Contract/CO6-DRAFT-3.27-unsigned.docx]]. Role segmentations being confirmed with Aaron Simeon. |

Christian will provide Manuel with detailed focus areas for delivery under CR6/CO6.

> ⚠️ **CO5 timeline risk:** all 3 deliverables due **Jun 30, 2026**, but PI-2 runs to **Aug 4** — stories in Iter 2.4/2.5/2.6 land after the contractual deadline. See [[co5-deliverable-tracking]].
> 🟠 **CO6 is the re-baselining vehicle but is UNSIGNED.** If not executed before **July 1**, the CO5 6/30 deadline + **$533,775 holdback stand with no relief**. CO6 closes 5 of 6 CO5 gaps (not the monthly-CCB item). See [[co6-deliverable-tracking]] for the gap-closure map.

## ServiceNow Product Line Peers

| Team | Product Owner | Scrum Master | Tech Lead |
|------|--------------|-------------|----------|
| ServiceNow Enhancements | JP Nair | Karen Hodges | Hari Medikondu |

## Business Stakeholders & Governance

Supplemental stakeholder mapping for the CMDB effort (added 2026-06-12). Additive — does not override roles recorded elsewhere in this file.

| Stakeholder | Function / Job | PPL Team | CMDB Related Function / Class |
|-------------|----------------|----------|-------------------------------|
| Michele Coan | PPL Audit | — | CMDB Governance |
| Aaron J Yocum | PPL Audit | — | CMDB Governance |
| Shane Wisecarver | PPL Audit | — | CMDB Governance |
| Andy Schwartzberg | PPL IT Leadership | — | CMDB Governance |
| Michael Basso | PPL IT Leadership | — | CMDB Governance |
| Sam Hamilton | Enterprise Architecture | — | Business Application record clean-up |
| Matt Newhouse | Enterprise Architecture | — | Business Application record clean-up |

**Also mapped to CMDB functions (primary roles recorded above — not redefined here):**

- **Tom Westervelt** — ART Coach → SAFe / Agile Support (see ART Context)
- **Nolan LeBlanc** — RTE (InfoOps) → SAFe / Agile Support (see ART Context)
- **Todd Dierksheide** — Value Stream IT Lead → CMDB Governance / PPL IT Leadership (see ART Context)
- **Gregory Belanger** — ART Business Owner → CMDB Governance / PPL IT Leadership (see ART Context Business Owners)

_PPL Team column left blank as provided. Source list framed these as "PPL IT Leadership" for Dierksheide and Belanger; their existing roles (Value Stream IT Lead, Business Owner) take precedence._

## CCB Roster

Change Control Board membership for the CMDB effort (added 2026-06-12). Additive — does not override roles recorded elsewhere in this file. Ray Reuter and JP Nair each appear under more than one class/process by design.

| Member | CCB Role | Area of Focus | Email |
|--------|----------|---------------|-------|
| Josh Sterling | Chairperson | Configuration Management Process Owner | jsterling@pplweb.com |
| Todd Dierksheide | Class Manager | Business Application CI | tddierksheide@pplweb.com |
| Ray Reuter | Class Manager | Servers and Storage CIs | rbreuter@pplweb.com |
| Ray Reuter | Class Manager | Database CIs | rbreuter@pplweb.com |
| Monica Green | Class Manager | Computers CIs – Physical | mmgreen@pplweb.com |
| Paul Becker | Class Manager | Computers CIs – Virtual | PBecker@pplweb.com |
| Mark Smith | Class Manager | Azure CIs | MSSmith@pplweb.com |
| Adam Gross | Class Manager | Network Gear CIs | AGross@pplweb.com |
| Jason Finn | Class Manager | Communication Devices CIs | jfinn@pplweb.com |
| Cheryl Guia | Class Manager | Printer CIs | CLGuia@pplweb.com |
| Jason Dubreuil | Consulting Member | Cybersecurity & Compliance | JRDubreuil@pplweb.com |
| Gaurav Parmar | Consulting Member | Enterprise Architecture | GDParmar@pplweb.com |
| Sonika Das | Consulting Member | ServiceNow Platform | SDas2@pplweb.com |
| JP Nair | Consulting Member | Request and Change Management Process | JNair@pplweb.com |
| JP Nair | Consulting Member | Incident and Problem Management Process | JNair@pplweb.com |
| Nora Lizenberg | OCM Support | OCM | nflizenberg@pplweb.com |

**Cross-reference (primary roles recorded above — not redefined here):** Todd Dierksheide (Value Stream IT Lead), Sonika Das (Product Manager, EVT), JP Nair (ServiceNow Enhancements PO), Ray Reuter (server support group assignments contact).

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

**2026-07-10 — Application Service / Service Instance modification via Service Request — story split:** Decomposed the "modify an Application Service" requirement into two sequential SAFe stories. **Story A** ([[Backlog/service-instance-modify-storyA-core]]) — core modify: 5-role ownership integrity (Owned By, CI Owner, Support Group, Technical Owner Group, Approval Group), field validation, baseline approval (pending Joe); near-ready, target end PI-2. **Story B** ([[Backlog/service-instance-modify-storyB-sox]]) — governed handling for SOX-flagged CIs; target early PI-3. Chose **Option a**: Story A *blocks* modification of SOX-flagged CIs and keeps SOX Indicator/Type read-only; Story B is the governed path that enables them — no interim gap. SOX notifications go to a **single team** ("SOX team", Pepa = POC). **Open decisions for Joe/Compliance:** SOX approval vs. informational notification (#2), and governance scope — every change vs. ownership/classification only (#3). **NERC CIP parked.** Adopted **CSDM 5 (Yokohama)** terminology: Application Service → Service Instance ([[csdm5-terminology]]). **Follow-ups:** recover the truncated Pepa email requirement ("…IAM wants to ensure that the CMDB/CI business owner…") — may add an AC to Story A; get Joe's baseline approval design + Decisions #2/#3.

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
- [[Leadership-Status]] — weekly customer-leadership status deck (PowerPoint + Marp markdown), regenerated from `build_status_deck.py`; shows progress PI/Iteration/Week over week. **Baseline template (DRAFT):** slide 4 (PI-2 Objectives Scorecard) uses the executive-tiles layout (Variation C — 3×2 grid, explicit per-objective RAG); the 2026-06-11 edition is the in-draft baseline pending finalization. _Note: the `.md` mirror still renders the scorecard as a table (tiles don't translate to markdown)._
- [[PI-2/pi2-objectives-features-stories]] — full PI-2 traceability: objectives → features → stories with status
- [[Backlog/features]] — features mapped to PI objectives
- [[Backlog/definition-of-ready]] — story readiness gates
- [[Backlog/definition-of-done]] — story acceptance criteria
- [[Backlog/co5-governance-validation-stories]] — DRAFT parent feature *"CO5 Governance Validation & Acceptance"* + 8 SAFe validation stories (1 per CO5 Governance sub-item, 1.1 split per CI class), each grounded in real ADO evidence IDs, with an `ADO ID (fill on creation)` reconciliation column; reference only until created in ADO (then reconcile back to [[co5-deliverable-tracking]] Acceptance Tracking)
- [[Backlog/cmdb-health-lifecycle-validation-stories]] — DRAFT **NON-SOW** quality-governance validation stories (Health & Lifecycle, 1 per CI class); separate lane, does not gate CO5 holdback
- [[Backlog/audit-dashboard-accuracy-spike]] — DRAFT **NON-SOW** Spike (target Iter 2.4, **due 6/30**): validate BA audit-dashboard scope + each of 11 quality audits, build compliance-prioritized remediation plan (owner/target date/solution type), apply safe quick fixes (BA-pause-limited). **Simplified, team-shareable format** Manuel finalized 6/23.
- [[Backlog/audit-dashboard-spike-template]] — reusable TEMPLATE of the audit-dashboard spike, to apply the same approach to the next audit areas (Servers, Database, Computer, Groups)
- [[Backlog/audit-dashboard-servers-spike]] — DRAFT **NON-SOW** Servers-tab audit spike (Iter 2.4, due 6/30; scope = Active Servers Count 15,218; 11 audits). Watch: Missing Value Stream = 100%, two 0-count audits.
- [[Backlog/audit-dashboard-database-spike]] — DRAFT **NON-SOW** Database-tab audit spike (Iter 2.4, due 6/30; scope = Active Database CI Count 3,113; 6 audits). Watch: Missing Value Stream = 100%, Missing Approval Group ~99.9%.
- [[Backlog/audit-dashboard-computer-spike]] — DRAFT **NON-SOW** Computer-tab audit spike (Iter 2.4, due 6/30; scope = Active Computer CIs 28,203 + virtual subset 6,530; 11 audits). Watch: Missing Approval Group = 100%, two 0-count audits, phys/virtual split.
- [[PI-2/weekly-activity-reference-2026-07-08]] — Week of ~Jul 6–8 comms/activity reference (Go Green, Airlift exec focus, Service Mapping, PI-3 kickoff, audit request); source pointer for the Airlift decomposition
- **Go Green** — weekly **CMDB & Service Mapping status deck to Sonika from the broader team** (deck title *"CMDB and Service Mapping Status Update"*); **distinct from [[Leadership-Status]]** (Manuel's customer-leadership deck). 7/7 edition: **At-Risk**; Airlift flagged **possible postponement**. Content captured in [[PI-2/weekly-activity-reference-2026-07-08]] §1.
- [[Backlog/airlift-plan-evaluation]] — evaluation of the draft ServiceNow × Airlift CMDB plan (for **CO6**): 4 workstreams, operating model, gaps (no owners/dates, no Data Dictionary linkage, resourcing TBD, BA→App Service collision). Reference only; source xlsx in Downloads, not in vault.
- [[Backlog/service-instance-modify-storyA-core]] — **Story A (foundation):** Modify SR core — attributes + 5-role ownership integrity; SOX fields read-only, SOX-flagged CIs blocked (Option a). Buildable now, target end PI-2. Pairs with Story B.
- [[Backlog/service-instance-modify-storyB-sox]] — **Story B:** governed modify path for SOX-flagged CIs (enables what Story A blocks). Blocked on Decision #2 (SOX approval vs notification) & #3 (governance scope); SOX recipient list from Pepa. Target early PI-3.
- [[csdm5-terminology]] — **CSDM 5 (Yokohama):** Application Service renamed to Service Instance (Application Service now a *type* of Service Instance). Use "Service Instance / Application Service"; verify PPL's version with Stan Tomberg.
- [[requirements-process]] — end-to-end requirements flow
- [[Dependencies/servicenow-enhancements]] — cross-team dependency tracker
- [[nowassist-implementation-plan]] — 5-phase NowAssist AI roadmap (Duplicate CI Elimination → NL Search → Guided CI Creation → Governance Advice → NASK); primary driver for PI-2 Obj 5 and PI-3 objectives

## Open Action Items

### 🔴 Immediate — Week of June 10

| Owner | Item | Context |
|-------|------|---------|
| Manuel | **Attend CMDB CCB Meeting** | Scheduled 06/16 — ref PPL MS Teams > 18 - CMDB 2026 > CCB Meetings |
| Manuel | **Attend CMDB Audit Sync** | Scheduled 06/18 |
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
| Manuel | **Data Certification PROD deployment** — CR 06/19, PROD 06/23, Todd validates 06/24–25 | Sonika signed off UAT 6/10; UAT target 06/15 |
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
- Data Certification: UAT by 06/15 → CR 06/19 → PROD 06/23 → Todd validates 06/24–25 ✅ timeline confirmed
- Dashboard capability request — story or parking decision pending
- ART demo status — has it already occurred? If not, when? Business Value scoring is a hard prerequisite
- Reverse DNS fix — who owns it? Needs escalation if unassigned
- Service Mapping app owner validation — which app owners are missing and who is responsible for chasing them?
