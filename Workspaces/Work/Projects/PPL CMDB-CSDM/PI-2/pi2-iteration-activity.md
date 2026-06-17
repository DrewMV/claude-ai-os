---
type: team-artifact
workspace: Work
project: CMDB-CSDM
pi: PI-2
updated: 2026-06-11
tags: [work, cmdb-csdm, pi-planning, iterations]
---

# PI-2 Activity by Iteration

Activity reconstructed from backlog refinement notes, PBR sessions, PI Memory, and team decisions.
Sprint planning committed-story tables were not filled in — story assignments come from refinement and PBR records.

---

## Iteration 2.1 — May 13–26, 2026 | ✅ Completed

### Stories Refined / In Progress

| ADO ID | Title | PI Obj | Owner | Status |
|--------|-------|--------|-------|--------|
| TBD → 1418610 | Airlift to Azure — Pre-Migration CMDB Preparation | P0 | Laurent / Alex Lim | Refined; sequenced as must-complete first |
| TBD → 1418618 | Airlift to Azure — During Migration CMDB Tracking | P0 | Laurent / Alex Lim | Refined; depends on Pre-Migration |
| TBD → 1418621 | Airlift to Azure — Post-Migration CMDB Validation | P0 | Laurent / Alex Lim | Refined; depends on During Migration |
| TBD → 1416384 | CI Attribute Auto-Population: CI Owner, Support Group, Technical Owner | P1 | — | Refined; ADO IDs pending Anu |
| TBD | Custom Fields: Asset Criticality, RPO, RTO, Recovery Tier, Tier Data Classification, Stocks, Stocks Type | P1 | — | Refined; ADO IDs pending Anu |
| TBD | SCCM Ingestion Validation | P1 | — | Refined; ADO ID pending Anu |
| TBD | IRE Behavior Validation Post-Upgrade | P1 | — | Refined; ADO ID pending Anu |

> **Note:** ADO IDs for 2.1 stories were TBD pending Anuradha Rai's confirmation. NowAssist AI stories noted as next wave — entering refinement in 2.2.

### Key Decisions

| Date | Decision |
|------|----------|
| 2026-05-13 | **OOTB-first policy** — evaluate out-of-box suitability before any customization; complex UI filters flagged as high-risk |
| 2026-05-13 | **Azure Airlift story sequence** — Pre-Migration → During Migration → Post-Migration; dependency order must be reflected in ADO |
| 2026-05-13 | **NowAssist AI sequencing** — stories enter backlog refinement in Iter 2.2 after Azure Airlift review completes |
| 2026-06-08 | **Physical Computer CI Owner Autopopulation approved** — CI owner, support group, tech owner automated for new physical CIs; virtual computers explicitly excluded; accepted at PO showback |
| 2026-06-08 | **PMDB Application Service custom fields approved** — 8 fields added; edit rights on 4 fields restricted to Cyber Risk and DR teams; moving to QA/UAT |

### Retrospective Highlights

**What Went Well:**
- Strong Daily Standup structure and consistency
- Clear leadership and direction from Alex Phan
- Good ADO hygiene — tracking, ownership, accountability maintained
- Effective onshore / offshore / contractor collaboration
- Successful transition from PI Planning into structured execution
- Dependency-sequenced task breakdown shows disciplined delivery governance

**What Didn't Go Well:**
- Credential dependencies (SNMP, CyberArk) unresolved all iteration — blocked discovery and service mapping
- Post-clone data integrity gaps identified late (Major Incident templates missing)
- Service Mapping blocked by missing credentials and environment restrictions
- External team responsiveness (Network, Ops) unpredictable
- Discovery strategy (DEV/QA vs PROD) debated but never formally resolved
- Delivery highly dependency-driven; limited ability to pull ahead

### Retro Action Items (all carried into 2.2)

| Action | Owner |
|--------|-------|
| Confirm post-clone completeness — validate all CMDB objects, templates, relationships | TBD |
| Confirm SNMP credentials fully working across all device types | TBD |
| Confirm CyberArk integration complete | TBD |
| Document and approve discovery/testing strategy (DEV/QA vs PROD) | TBD |
| Resolve credential/access issues blocking Service Mapping | TBD |
| Finalize Data Certification pilot scope | TBD |
| Identify and escalate stalled external dependency requests (Network, Ops) | Alex Phan |

---

## Iteration 2.2 — May 27 – Jun 9, 2026 | ✅ Completed

### Carry-In Blockers (from 2.1)

| # | Item | Severity |
|---|------|----------|
| 1 | Credential readiness — SNMP / CyberArk not confirmed complete | High |
| 2 | Post-clone data integrity — full validation not confirmed | High |
| 3 | Discovery strategy (DEV/QA vs PROD) undocumented | High |
| 4 | Service Mapping blocked by credentials/access | High |
| 5 | External dependency bottlenecks (Network, Ops) | Medium |

### Stories Refined / Worked

#### SCCM Stories — Feature 1356826

| ADO ID | Title | Owner | Decision | Status at End of 2.2 |
|--------|-------|-------|----------|----------------------|
| 1403763 | SCCM Server Hardware & Software Attribute Data Precedence | Vinay | ✅ Approved | Ready → carries into 2.3 |
| 1403760 | SCCM: Servers — Domain and Network Attribute Data Precedence | Vinay | ✅ Approved (P2) | Ready → carries into 2.3 |
| 1403762 | SCCM: Servers — Last Seen Timestamp Alignment | Vinay | ⚠️ Blocked | Pending Sonika approval; 2 new attributes created in dev → carries into 2.3 |
| 1403759 | SCCM: Servers — De-Prioritize SCCM Attributes (asset tag, OU name) | — | 🔴 On Hold | Pending Ray attribute mapping review; call needed → carries into 2.3 |

#### Spike Stories

| ADO ID | Title | Owner | Points | Decision | Status at End of 2.2 |
|--------|-------|-------|--------|----------|----------------------|
| 1402555 | CMDB: Identify CI Classes for Group 1 | Stan + Joe | 2 pts | ✅ Approved | Ready → carries into 2.3 |
| 1403733 | Identify deprecated plugins/features impacting CMDB capabilities | — | — | ✅ Approved | Ready → carries into 2.3 |

#### NowAssist Stories — Feature 1436574 (ADO linkage unconfirmed)

| ADO ID | Title | Owner | Points | Status at End of 2.2 |
|--------|-------|-------|--------|----------------------|
| 1436576 | Confirm Platform Prerequisites for NowAssist Activation (Part 1) | Karen | 1 pt | Assigned → 2.3 ⚠️ Karen rolling off |
| 1436579 | Activate NowAssist for CMDB Plugin | Karen | 1 pt | Assigned → 2.3 ⚠️ Karen rolling off |
| 1436593 | Activate Contextual CI Form Help Skill | Karen | 1 pt | Assigned → 2.3 ⚠️ Karen rolling off |
| 1436592 | Activate CI Summarization Skill | Karen | 1 pt | Assigned → 2.3 ⚠️ Karen rolling off |

#### Data Certification

| ADO ID | Title | Owner | Status at End of 2.2 |
|--------|-------|-------|----------------------|
| 1402727 | Update Data Certification Dashboard | Kiran | In progress; UAT signed off by Sonika 06/10 (day 1 of 2.3) |

#### Service Mapping / Discovery

| Item | Owner | Status at End of 2.2 |
|------|-------|----------------------|
| Credential updates for server scanning | Tanzeel / Sonika | ✅ Resolved — credentials working as of 6/9; single test subnet active |
| DNS issue | Alex (via Christian) | 🔴 Still open — email resolution attempted |
| Airlift dev admin access | Laurent / Stan | ✅ Resolved 06/09 |

### Key Decisions (2.2)

| Date | Decision |
|------|----------|
| 2026-06-08 | **SCCM authoritative source confirmed** — SCCM is authoritative for Manufacturer, Model, BIOS serial, CPU, Disk, RAM; ServiceNow Discovery updates only if value is blank |
| 2026-06-08 | **Customization governance established** — all customization stories must be tagged "Customization," have a RAID/Decision issue logged, and receive Sonika Das approval before implementation |
| 2026-06-08 | **CC User Location root cause identified** — LDAP writes plain text into location field instead of referencing common location table; 18,000+ user records affected; gates Story 1455858 |
| 2026-06-08 | **Spike 1403759 placed on hold** — pending attribute mapping review with Ray; separate call needed |
| 2026-06-08 | **NowAssist stories assigned to Karen** — Stories 1436576, 1436579, 1436593, 1436592 (1 pt each); created in ADO by Alex Phan |
| 2026-06-08 | **Business app enhancements paused** — all new Business Application enhancements paused until App Services migration complete; OCM required before changes |
| 2026-06-09 | **SM Role Transition** — Alex Phan shifts primary focus to ITSM; Manuel Vazquez takes over as CMDB SM in hybrid "SM Plus" role |

### Capacity Assignments into 2.3 (confirmed at SCCM refinement 06/08)

| Team Member | 2.3 Focus |
|-------------|-----------|
| Vinay | SCCM domain/network attributes (1403760) + timestamp alignment (1403762) |
| Karen | NowAssist activation stories (1436576, 1436579, 1436593, 1436592) |
| Tony | Business app cleanup + credentials (ongoing); begin app migration |
| Laurent | Azure Airlift stories; dev admin access resolved 06/09 |
| Alex Lim | Azure Airlift stories |
| Stan | SCCM customization approval packaging; admin access resolution |
| Kiran | Data Certification Dashboard (1402727) — in UAT |
| Tanzeel | Service Mapping — subnet discovery scans |

### Retrospective

> ⚠️ Retro file for 2.2 was not filled in. No recorded findings.

---

## Iteration 2.3 — Jun 10–23, 2026 | 🟢 Active

### Stories Committed / In Progress

#### PI Obj 0 — Airlift

| ADO ID | Title | Owner | Status |
|--------|-------|-------|--------|
| 1418610 | Airlift to Azure — Pre-Migration | Laurent / Alex Lim | 🟢 Active — dev access resolved |
| 1418618 | Airlift to Azure — During Migration | Laurent / Alex Lim | 🟢 Active |
| 1418621 | Airlift to Azure — Post-Migration | Laurent / Alex Lim | 🟢 Active |
| 1416384 | Auto Populate CI Owner / Support Group / Tech Owner for Server Class | — | 🟢 Active |

#### PI Obj 1 — Discovery / SCCM

| ADO ID | Title | Owner | Status |
|--------|-------|-------|--------|
| 1403760 | SCCM: Servers — Domain and Network Attribute Data Precedence | Vinay | 🟢 Ready |
| 1403762 | SCCM: Servers — Last Seen Timestamp Alignment | Vinay | 🔴 Blocked — awaiting Sonika approval |
| 1402555 | CMDB: Identify CI Classes for Group 1 (Spike) | Stan + Joe | 🟢 Ready |
| 1403733 | Identify deprecated plugins/features impacting CMDB (Spike) | — | 🟢 Ready — gated on sandbox restore |
| 1421790 | Gap Analysis for Servers — Linux & Windows (Spike) | Tony | 🟢 In Progress |

#### PI Obj 2 — Data Certification

| ADO ID | Title | Owner | Status |
|--------|-------|-------|--------|
| 1402727 | Update Data Certification Dashboard | Kiran | 🟢 UAT signed off 06/10 — PROD deploy 06/23 |

**Data Certification deployment schedule:**

| Milestone | Date |
|-----------|------|
| UAT gate | 06/15 |
| PROD Change Request | 06/19 (Friday) |
| PROD Deployment | 06/23 (Tuesday) |
| Todd validates in PROD | 06/24–06/25 |

#### PI Obj 3 — Service Mapping

| Item | Owner | Status |
|------|-------|--------|
| Discovery — additional subnet scans | Tanzeel | 🟢 In Progress — single subnet ✅; more in progress |
| DNS issue resolution | Alex / Christian | 🔴 Open — email thread in progress |
| App owner sign-off validation | — | ⚠️ Owner not confirmed |

#### PI Obj 4 — Qualys (Stan)

| ADO ID | Title | Owner | Status |
|--------|-------|-------|--------|
| 1428703 | Install x_qual5_itam_nwapp Plugin (Part 1) | Stan | 🟢 Active |
| 1428704 | Configure Qualys Integration for CMDB to Qualys (Part 2) | Stan | 🟢 Active |
| 1234585 | Define and Configure Data Scope and Import Views in Qualys (Spike) | Stan | 🟢 Active |

#### PI Obj 5 — NowAssist

| ADO ID | Title | Owner | Status |
|--------|-------|-------|--------|
| 1436576 | Confirm Platform Prerequisites for NowAssist Activation | Karen | 🟡 Assigned — **reassignment needed** (Karen rolling off) |
| 1436579 | Activate NowAssist for CMDB Plugin | Karen | 🟡 Assigned — **reassignment needed** |
| 1436593 | Activate Contextual CI Form Help Skill | Karen | 🟡 Assigned — **reassignment needed** |
| 1436592 | Activate CI Summarization Skill | Karen | 🟡 Assigned — **reassignment needed** |

### Key Dates This Sprint

| Date | Event |
|------|-------|
| 06/15 | Data Certification UAT gate |
| 06/16 | CMDB CCB Meeting |
| 06/17 | Backlog Refinement 2.3 |
| 06/18 | CMDB Audit Sync |
| 06/19 | PROD Change Request — Data Certification |
| 06/23 | Sprint End + PROD Deployment — Data Certification |

### Open Risks This Sprint

| Risk | Severity | Owner |
|------|----------|-------|
| NowAssist 4 stories unassigned — Karen rolling off | High | Manuel |
| Story 1403762 blocked on Sonika approval | High | Manuel / Stan |
| Spike 1403759 still on hold — call not yet scheduled | Medium | Manuel / Alex / Joe |
| DNS issue blocking Service Mapping full coverage | High | Alex / Christian |
| Sandbox restore not confirmed — gates Spike 1403733 | High | OPS / Narayan |
| Data Certification UAT must pass by 06/15 | High | Kiran / Bhushan |

### Ceremonies Scheduled

| Ceremony | Date |
|----------|------|
| Backlog Refinement 2.3 | 06/17 |
| Sprint Review 2.3 / Showback | ~06/23 |
| Retrospective 2.3 | ~06/23 |
| Sprint Planning 2.4 | ~06/23 |

---

## Cross-Iteration Summary

| Story / Item | 2.1 | 2.2 | 2.3 |
|---|---|---|---|
| Airlift Pre/During/Post (1418610–1421) | Refined | — | 🟢 Active |
| CI Owner / Support Group Autopopulation (1416384) | Refined | Approved | 🟢 Active |
| CMDB Custom Fields (PMDB App Service) | Refined | Approved → QA/UAT | — |
| SCCM Hardware/Software Precedence (1403763) | — | ✅ Approved | → 2.3 |
| SCCM Domain/Network Precedence (1403760) | — | ✅ Approved | 🟢 Ready |
| SCCM Timestamp Alignment (1403762) | — | ⚠️ Blocked | 🔴 Still blocked |
| SCCM De-Prioritize Attributes (1403759) | — | 🔴 On Hold | ⏸️ Still on hold |
| CI Classes Group 1 Spike (1402555) | — | ✅ Approved | 🟢 Ready |
| Deprecated Plugins Spike (1403733) | — | ✅ Approved | 🟢 Ready |
| Server Gap Analysis Spike (1421790) | — | Started | 🟢 In Progress |
| Data Cert Dashboard (1402727) | — | In Progress | 🟢 UAT → PROD 06/23 |
| NowAssist Stories (1436576–1436592) | — | Created / Assigned (Karen) | 🟡 Reassignment needed |
| Service Mapping Credentials | 🔴 Blocked | 🟡 Partial | ✅ Resolved 06/09 |
| Service Mapping DNS | 🔴 Blocked | 🔴 Ongoing | 🔴 Still open |
| Airlift Dev Admin Access | — | 🔴 Blocked | ✅ Resolved 06/09 |
| Qualys Stories (1428703–1234585) | — | Assigned (Stan) | 🟢 Active |
