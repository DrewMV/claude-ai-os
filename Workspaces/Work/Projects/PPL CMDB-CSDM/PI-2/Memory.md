---
level: pi
workspace: Work
project: CMDB-CSDM
pi: PI-2
status: active
start: 2026-05-13
end: 2026-08-04
updated: 2026-06-01
tags: [work, safe, pi-planning, cmdb-csdm]
---

## PI Objectives

| # | Objective | BV | Priority |
|---|-----------|-----|---------|
| 1 | Automate Discovery Coverage for Network Gear CI Classes (≥90% quality by Aug 4) | 10 | Highest |
| 2 | Establish CI Data Certification Program (framework + pilot for Business Apps) | 8 | High |
| 3 | Expand Service Mapping Foundation (10 business-critical platforms/month) | 9 | High |
| 4 | Prepare CMDB for Regulatory and Security Integrations (NERC CIP + Qualys) | 8 | High |
| 5 | Embed NowAssist AI Across CMDB and ITSM Workflows | 7 | Medium |
| 6 | **Enable Governed VMware-to-Azure Migration via CMDB-Driven Intelligence** | 10 | Highest |

See full objective text in [[PI-2/pi-planning]].
See iteration-by-iteration activity in [[PI-2/pi2-iteration-activity]].
See [[PI-2/pi2-story-validation-worksheet]] — work-item list with blank State/Points/Assigned To for ADO validation (also `.csv`).
See objectives → features → stories traceability in [[PI-2/pi2-objectives-features-stories]].

## Iterations

| Iteration | Start | End | Status |
|-----------|-------|-----|--------|
| 2.1 | 2026-05-13 | 2026-05-26 | Completed |
| 2.2 | 2026-05-27 | 2026-06-09 | Completed |
| 2.3 | 2026-06-10 | 2026-06-23 | Active |
| 2.4 | 2026-06-24 | 2026-07-07 | Upcoming |
| 2.5 | 2026-07-08 | 2026-07-21 | Upcoming |
| 2.6 (IP) | 2026-07-22 | 2026-08-04 | IP Iteration |

## Team Capacity

_Fill in per iteration from sprint-planning notes._

## Risks and Dependencies

| # | Risk | Severity | Status | Notes |
|---|------|---------|--------|-------|
| 1 | Credential readiness (SNMP, CyberArk) blocking discovery and service mapping | High | Open | Carried from Iter 2.1 into 2.2 |
| 2 | Post-clone data integrity — missing configs identified (Major Incident templates) | High | Open | Full validation not confirmed |
| 3 | Discovery strategy (DEV/QA vs PROD) not documented or approved | High | Open | Debate ongoing, no resolution |
| 4 | External dependency bottlenecks — Network, Ops team responsiveness | Medium | Open | Recurring pattern in Iter 2.1 |
| 5 | Service Mapping blocked — credential and access gaps | High | Partially Resolved | Credentials now working (6/9); single subnet discovery active; DNS issue still open; remaining subnets in progress |
| 6 | Reverse DNS not functioning — blocking CMDB discovery, Airlift planning, and ServiceNow visibility | High | Open | Raised at PO Sync 2026-05-28 |
| 7 | AVD + Windows 11 unplanned work consuming ART capacity | High | Open | Displacing PI commitments across shared services |
| 8 | Airlift migration wave dates not finalized — limiting Airlift planning confidence | Medium | Open | PI Obj 6 directly at risk; see [[Dependencies/infra-ops-technology]] |
| 9 | **Sandbox upgrade to Australia version June 6** — clone + upgrade **completed** (confirmed 2026-06-19 platform-team FYI); all teams must restore update sets/backups in sandbox and validate environment before proceeding with upgrade-dependent work; NowAssist stories and upgrade analysis spikes (Feature 1355890) gate on this validation | **High** | Open — restore in progress | See [[Dependencies/external]] — CHG70100867 |
| 10 | **Dev code freeze July 4 – July 18** (revised 2026-06-19 — slipped ~1 wk later; was June 27 – July 18) — DEV clone June 27, upgrade July 4; no deployments to pplwebdev during the freeze, which spans the tail of Iter 2.4 (Jul 4–7) and first half of 2.5 (Jul 8–18); stories requiring dev changes must land **before July 4** or wait until July 18; first ~10 days of Iter 2.4 (Jun 24 – Jul 3) now freed up | **High** | Open | See [[Dependencies/external]] — CHG70100870 |
| 11 | **Test code freeze July 18 – Aug 15** — spans end of 2.5, all of IP (2.6), and extends 10 days into PI-3 Iter 3.1; no test deployments during IP iteration; PI-3 planning must account for reduced test environment availability at start | **High** | Open | See [[Dependencies/external]] — CHG70100865 |
| 13 | **Ray's 450-server application-instance request (Azure migration blocker)** — Ray requested the application instances running on ~450 virtual servers he manages, flagged urgent and a blocker for the VMware-to-Azure migration (PI Obj 6). Request carries no context on purpose, required fidelity, or deadline. **Core finding — directional mismatch:** the request is *server-first* ("what apps run on these servers?") but Service Mapping is *application-first* (starts from a known app, traces to infra) — so it cannot be deliberately targeted at a server. The 21 servers mapped via Service Mapping were *incidental* overlaps. The true gap is the missing **application↔server relationship layer**: we have ~2,100 known application instances but no reliable app→server linkage, and those apps are **not confined to these 450 servers**, so the 2,100 cannot be filtered to Ray's list. Coverage to date: **82 of ~450** — 21 incidental Service Mapping, 61 via **iTeam** (PPL homegrown CMDB); app-owner outreach limited. **Most promising paths:** (1) iTeam validation (active — only source that may already hold server→app relationships); (2) ServiceNow Discovery, which IS server-first and likely already scans the subnets containing most of Ray's 450 — so raw installed-software data likely already exists; remaining work = correlating that footprint to named application instances (needs technical validation). Assessment email to leadership reframed around this and drafted 2026-06-18. Next step: working session with the right technical owners + Ray to confirm iTeam payoff, validate Discovery correlation path, and capture requirements (deadline, fidelity, priority). | **High** | Open — assessment email to leadership in progress | Surfaced 2026-06-18; ties to PI Obj 6; Ray also SCCM data owner (Risk #12); technical validation likely Joe, possibly Tony (Anthony) |
| 12 | **SCCM vs. ServiceNow Discovery authoritative precedence not fully resolved** — June 8 decision locked SCCM as authoritative for 6 hardware attributes, but a complete field-by-field precedence map does not exist. Stories 1403760, 1403762, 1403759, and spike 1421790 are each making isolated precedence decisions without a governing baseline. Risk of conflicting rules across stories, dirty data in CMDB, or rework if a later ruling overrides earlier sprint commitments. Needs a decision owner, full attribute map agreed with Ray (SCCM data owner) and Sonica, before further precedence stories are committed to sprints. | **High** | Open | Surfaced 2026-06-08 SCCM refinement; Spike 1403759 (asset tag / OU name) on hold pending Ray review; see [[PI-2/Iterations/Iteration-2.2/backlog-refinement-2026-06-08-sccm]] |

## Key Decisions This PI

- **2026-06-10 — Data Certification deployment timeline confirmed:** Sonika signed off on UAT (6/10). Deployment sequence: UAT by 06/15 → PROD Change Request 06/19 (Friday) → PROD deployment 06/23 (Tuesday) → Todd validates in PROD 06/24–06/25.
- **2026-06-10 — Service Mapping credentials resolved (partial):** Credential updates now working. Discovery is successfully connecting to devices and surfacing Linux servers, Oracle databases, listeners, and related services previously not visible. Single test subnet completed; additional subnet scans in progress.
- **2026-06-09 — Airlift dev admin access resolved:** Carry-over finding on dev admin access has been resolved. Stories 1418610, 1418618, 1418621, 1416384 active.
- **2026-06-08 — CCB and Audit Sync dates confirmed:** CMDB CCB Meeting scheduled 06/16; CMDB Audit Sync scheduled 06/18. Reference: PPL MS Teams > General > Accenture & PPL - Working Documents > 18 - CMDB 2026 > CCB Meetings.

- ADO discipline enforced as delivery standard: daily status updates, decision documentation, progress validation before DSU required of all team members
- **OOTB-first policy**: evaluate out-of-box ServiceNow suitability before any customization; complex UI filters flagged as high-risk customization area; decisions treated as product-level choices, not individual preferences
- **AI work sequencing**: NowAssist AI stories (PI Obj 5) enter backlog refinement in Iter 2.2 after Azure Airlift review completes in Iter 2.1
- **Azure Airlift story sequencing**: Pre-Migration → During Migration → Post-Migration; dependency order must be reflected in ADO linkage
- **2026-06-08 — SCCM authoritative source confirmed:** SCCM is the authoritative source for Manufacturer, Model, BIOS serial, CPU, Disk, and RAM. ServiceNow Discovery updates these fields only if the value is blank. Agreed in backlog refinement session.
- **2026-06-08 — Physical Computer CI Owner Autopopulation approved:** CI owner, support group, and tech owner group fields automated for new physical computer CIs. Existing records updated via PixScript. Virtual computers explicitly excluded (different stakeholder groups). Story accepted in PO showback.
- **2026-06-08 — PMDB Application Service Custom Fields approved:** Eight fields added to PMDB CI service ITO table (asset criticality, RPO, RTO, recovery tier meter, tier data classification, stocks indicator, stocks type). Edit permissions for four fields restricted to Cyber Risk and DR teams. Story accepted in PO showback; moving to QA/UAT.
- **2026-06-08 — CC User Location root cause identified:** LDAP integration writes plain text into the location field instead of referencing the common location table — affects 18,000+ user records. Azure, HCM, and PeopleSoft integrations do not populate this field. Proposed fix: technical safeguards and scripts to correct LDAP handling. Review meeting with Joe pending. Directly gates US 1455858 (Virtual Location Management).
- **2026-06-08 — Customization governance process established:** Stories involving custom logic, scripts, or workflows must be tagged "Customization" in ADO, have a RAID/Decision issue logged and linked, and receive Sonica Das approval before implementation. Configuration changes (fields, forms, basic updates) are exempt. See [[requirements-process#Customization Governance]].
- **2026-06-08 — Spike 1403759 (De-prioritize SCCM) on hold:** Pending attribute mapping review with Ray. Approval status unclear. Follow-up call required with Alex, Vinay, Joe, Manuel before sprint commitment.
- **2026-06-08 — NowAssist stories assigned to Karen:** Stories 1436576, 1436579, 1436593, 1436592 assigned to Karen (1 pt each) due to Vinay's SCCM workload. Created in ADO by Alex Phan per 6/8 email. Feature-level linkage in ADO pending — Anu to confirm feature IDs upon return.

## ART Delivery Context (from PO Sync 2026-05-28)

- Execution becoming reactive across the ART — unplanned work displacing PI commitments
- Poor intake quality and late engagement is a recurring ART pattern (solutions submitted instead of requirements)
- Push for ROAM-based risk visibility and standard intake templates — watch for ART-level governance changes
- Architecture diagrams and process flow visualizations being adopted early as coordination tools

## Open Questions

- What is the approved discovery/testing strategy for DEV/QA vs PROD environments?
- Is post-clone validation complete for all CMDB objects and templates?
- What is the timeline for full CyberArk/SNMP credential resolution?
- When are Airlift migration wave dates being finalized?
- Is Reverse DNS fix being tracked as an ART impediment or CMDB-CSDM impediment?
- What NowAssist capabilities are available in Australia vs Yokohama? (Joe — action from 5/20)
- Where are the NERC-CIP documentation and ESS 02 docs? (Alex — action from 5/20)
- What is Jason Dubriel's role and availability for NERC-CIP / ESS 02 engagement?
- What is the OCM impact of CI Ownership change for servers — who are the affected incident/request creators and CI owners?
- What is Laurent's capacity split between CMDB-CSDM and SNOW Enhancements?

## Action Items Log

| Action | Owner | Source | Status |
|---|---|---|---|
| Provide initial NowAssist features and stories in ADO | Joe Dames | Team discussion 5/26 | Partially done — Alex Phan created 4 stories (1436576, 1436579, 1436593, 1436592) on 2026-06-08; feature-level ADO linkage still pending; Anu to confirm feature IDs |
| Assess NowAssist capabilities: Australia vs Yokohama | Joe Dames | Team discussion 5/20 | Open |
| Add DNS email update from Christian to thread; attempt email resolution before scheduling meetings | Alex Phan | Team discussion 5/26 | Open |
| Get Sonika support for missing server credentials (Service Mapping scanning) | Manuel / Joe | Team discussion 5/26 | Open |
| Engage Jason Dubriel on NERC-CIP / ESS 02 | TBD | Team discussion | Open |
| Document CMP | TBD | Team discussion | Open |
| Formalize CCB ceremony cadence | TBD | Team discussion 5/26 | Open |
| Locate NERC-CIP documentation | Alex Phan | Team discussion 5/20 | Open |
| Engage Sonika / Cyber compliance on NERC-CIP requirements | TBD | Team discussion 5/20 | Open |
| Review CI Ownership plan for servers with OCM; assess impact to incident/request creators | Joe Dames | Team discussion | Open |
| Assign developer to CI Ownership server work | Joe Dames | Team discussion | Open |
| HCM integration for computer location — engage Sonika | Manuel / Joe | Team discussion | Open |
| Clarify scope of Cherwell laptop import vs US 1452028 (iteam import) — confirm whether new vendor purchase feed is covered by existing ADO story or needs a new one; review with Alex Phan and Anu, but **Uloma (Adelufosi) is primary contact** as meeting organizer and process owner | Manuel / Alex / Anu → Uloma | Cherwell meeting 2026-06-08 | Open |
| Resolve Spike 1403759 (De-prioritize SCCM asset tag / OU name) approval status — dedicated call needed with Alex, Vinay, Joe, Manuel before sprint commitment | Manuel / Alex / Vinay / Joe | SCCM Backlog Refinement 2026-06-08 | Open |
| Obtain Sonica approval for 2 new SCCM timestamp attributes (Story 1403762) before moving from dev to production — Stan to send customization details to Alex for approval issue creation | Stan → Alex → Sonica | SCCM Backlog Refinement 2026-06-08 | ✅ Closed — ADO Issue **1464224** "SCCM Two Date Time New Fields Required – Decision" (Sonika Das) Closed per 6/19 issue grid = approved |
| Send (reframed) assessment email to leadership on Ray's 450-server application-instance request — directional mismatch + missing app↔server relationship layer; then schedule working session with technical owners (Joe, possibly Tony) + Ray to confirm iTeam payoff, validate Discovery correlation path, and capture requirements (deadline, fidelity, priority) (see Risk #13) | Manuel | Escalation 2026-06-18 | Open — draft ready |
