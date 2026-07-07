---
type: team-artifact
workspace: Work
project: CMDB-CSDM
pi: PI-2
updated: 2026-07-06
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

## Iteration 2.3 — Jun 10–23, 2026 | ✅ Completed

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

## Iteration 2.4 — Jun 24 – Jul 7, 2026 | 🟡 Closing

> 🔄 **Transition in progress (7/7).** Final ADO updates for 2.4 closeout and 2.5 story moves expected today / tomorrow. This section will be reconciled against the end-of-sprint grid once received. States below reflect the 7/6 ADO pull — treat as near-final, not closed.

> 🎯 **CO5-focused iteration.** Per Manuel's **"CO5 Deliverable Alignment"** email (6/29 → Joe Dames, Stan, Tony; cc Chad Hayden, Chris Mizrany, Christian Aguilar, Ruchita, Anu, Jordan Yung, Alex), the team **temporarily deprioritized Service Mapping, Airlift, NowAssist, and Network Discovery** to direct resources at CO5 deliverables. The 6/30 ADO 2.4 grid reflects this — it is essentially the CO5 work slice. Deliverable detail + acceptance state: [[../co5-deliverable-tracking]]; full story states: [[pi2-objectives-features-stories]].

### Committed Load (6/30 ADO grid)
**38 work items · 61 story points.**

| Bucket | Items | Points | % |
|--------|-------|--------|---|
| **CO5-aligned** | 30 | **45** | 74% |
| Non-CO5 — ServiceNow upgrade readiness (enabling) | 6 | 11 | 18% |
| Non-CO5 — Network discovery (deprioritized) | 1 | 3 | 5% |
| Non-CO5 — NowAssist (deprioritized; already Closed) | 1 | 2 | 3% |
| **Total** | **38** | **61** | 100% |

> ⚠️ The 6/30 grid is a **filtered slice** — the deprioritized **Service Mapping (12 stories)**, NowAssist spikes (1451941/1451943), and upgrade spike 1403738 are **not** in it. They remain in backlog, postponed per the email — so **61 pts is the effective CO5-focused commitment**, not every 2.4-tagged item.

### CO5 Deliverable → 2.4 Story / Spike Mapping (individual deliverables)
One row per individual line item in the 6/29 alignment email. **"— reported complete (email)"** = the email reports the work done/operational with no open 2.4 story; **"— no 2.4 story"** = gap or validation not yet storied.

**Deliverable 1 — Governance** *(2.4 work hangs off Feature 1480087)*

| # | Individual deliverable | Lead | 2.4 ADO item (assignee · state · pts) | Pts |
|---|---|---|---|---|
| 1.1a | Data Dictionary — **Servers** | Manuel | 1480088 (Vinay · 🟣 Validation · 2) | 2 |
| 1.1b | Data Dictionary — **Computers** | Manuel | 1480090 (Bhushan · 🟣 Validation · 2) | 2 |
| 1.1c | Data Dictionary — **Business Apps** | Manuel | 1480097 (Kiran · 🟣 Validation · 2); + data-population: 1475582 Support Groups 496 (Kiran · 🔵 Active · 3), 1478286 Classification 938 (Anthony · 🟢 Ready DoR · 3), 1480111 BA audit spike (Joe · 🟢 Ready DoR · 2) | 10 |
| 1.1d | Data Dictionary — **Databases** **[closes G1]** | Manuel | 1480098 (Kiran · 🟣 Validation · 2) | 2 |
| 1.2 | Data Certification (pilot) | Joe | 1480099 (Joe · 🟢 Ready DoR · 2) | 2 |
| 1.3 | ESS-02 Alignment | Joe | 1480102 (Manuel · 🟢 Ready DoR · 1) | 1 |
| 1.4 | SOX BA review *(SOX only)* | Manuel | 1480105 (Uloma · 🟢 Closed · 1) ✅ | 1 |
| 1.5 | Monthly CCB **[closes G5]** | Manuel | 1480107 (Manuel · 🟢 Ready DoR · 1) | 1 |
| | | | **Subtotal** | **22** |

**Deliverable 2 — Automated Data Ingestion**

| # | Individual deliverable | Lead | 2.4 ADO item (assignee · state · pts) | Pts |
|---|---|---|---|---|
| 2.1a | Computers — SCCM/Discovery | Stan | — reported complete (email); prior-iter 1348712/715/716/717 | 0 |
| 2.1b | Computers — 90% Coverage | Stan | 1480114 Computer audit spike (Stan · 🔵 Active · 2) ⚠️ reassigned from Anthony | 2 |
| 2.1c | Computers — Build Lifecycle | Stan | — no 2.4 story (PM/stakeholder validation TBD; prior 1402790 Closed) | 0 |
| 2.2a | Server — SCCM/Discovery | Tony | — reported complete (email); prior-iter 1403759/760/762/763 (Validation) | 0 |
| 2.2b | Server — 90% Coverage / cleanup | Tony | 1480112 Server audit spike (Anthony · 🔵 Active · 2); 1454371 Extract servers w/o support groups (Bhushan · 🔵 Active · 2); 1455832 env-field rec (Vinay · 🟣 Validation · 2); inventory + bulk-retirement cluster 1487863–1490398 (14 incl. new 1490398) ⚠️ | 19 |
| 2.2c | Server — SOX Indicators | Tony | — reported complete (email) | 0 |
| 2.x | Credentials enabling Discovery | — | — reported complete (email); ⚠️ prior 1444864 child cred tasks were Active in 2.2 | 0 |
| 2.3a | Database — SQL/Oracle Discovery | Stan | — reported complete (email) | 0 |
| 2.3b | Database — SOX Indicators | Stan | — reported complete (email) | 0 |
| 2.3c | Database — 90% Coverage | Stan | 1480113 Database audit spike (Stan · 🔵 Active · 2) | 2 |
| | | | **Subtotal** | **22** |

> ⚠️ **Inventory + bulk-retirement cluster (1487863–1487897, 13 pts)** is booked under **Server 90% (2.2b)**, but the data is **VMware (virtual) + Physical, split PA/KY** — it may also serve **Computer 90% Coverage (2.1b)**. Confirm the server-vs-computer split; the 13 pts may need to divide across 2.1b / 2.2b.

**Deliverable 3 — Other Enhancement**

| # | Individual deliverable | Lead | 2.4 ADO item | Pts |
|---|---|---|---|---|
| 3 | Evaluate Qualys Integration | Stan | 1428703 Install plugin Part 1 (Stan · 🔵 Active · 1) | 1 |

**CO5-aligned total: 22 + 22 + 1 = 45 pts** (30 items).

> **Deliverables with no 2.4 story** (reported complete in the email, or pending validation): Computers / Server / Database SCCM-Discovery · Server / Database SOX Indicators · Credentials enabling Discovery · Computers Build Lifecycle. These are either done per the email or need a **validation/acceptance** story — confirm whether each requires a 2.4 acceptance item for CCB sign-off (cf. the acceptance-story pattern in [[../co5-deliverable-tracking]]).

**Not mapped to a CO5 deliverable (16 pts):**

| Stream | Disposition (per 6/29 email) | 2.4 items | Pts |
|--------|------------------------------|-----------|-----|
| ServiceNow Australia upgrade readiness | Enabling — not a named CO5 deliverable | 1403721 (3), 1403722 (2), 1403723 (2), 1403725 (1), 1403731 (1), 1411237 (2) | 11 |
| Network CI-class discovery | **Deprioritized** | 1402559 Compare CI Class Sources (3) | 3 |
| NowAssist Duplicate CI | **Deprioritized** (1451940 already Closed) | 1451940 (2) | 2 |

### 2.4 By Deliverable — Staffing & Coverage
Each formal CO5 deliverable → who is staffed on it (pts) → coverage flag. **Unstaffed / thin / unmapped flagged.**

| CO5 Deliverable | Staffed by (pts) | Stories | Pts | State | Flag |
|---|---|--:|--:|---|---|
| 1.1a DD — Servers | Vinay (2) | 1 | 2 | 🟣 Validation | |
| 1.1b DD — Computers | Bhushan (2) | 1 | 2 | 🟣 Validation | |
| 1.1c DD — Business Apps | Kiran (5), Anthony (3), Joe (2) | 4 | 10 | 🟣/🔵/🟢 mixed | best-staffed governance item |
| 1.1d DD — Databases | Kiran (2) | 1 | 2 | 🟣 Validation | ✅ closes **G1** |
| 1.2 Data Certification | Joe (1) | 1 | 1 | 🟢 Ready DoR | |
| 1.3 ESS-02 Alignment | Manuel (1) | 1 | 1 | 🟢 Ready DoR | |
| 1.4 SOX BA review | Uloma (1) | 1 | 1 | 🟢 Closed ✅ | ✅ **DONE** |
| 1.5 Monthly CCB | Manuel (1) | 1 | 1 | 🟢 Ready DoR | ✅ closes **G5** |
| 2.1a Computers — SCCM/Discovery | — | 0 | 0 | done (email) | |
| 2.1b Computers — 90% Coverage | Stan (2) | 1 | 2 | 🔵 Active | 🟡 **G2 — thin** (1 spike only; ⚠️ reassigned to Stan) |
| 2.1c Computers — Build Lifecycle | — | 0 | 0 | — | 🔴 **no 2.4 story** (validation TBD) |
| 2.2a Server — SCCM/Discovery | — | 0 | 0 | done (email) | |
| 2.2b Server — 90% / cleanup | Bhushan (7), Vinay (4), Anthony (3), Kiran (3), Anu (1) | 17 | 19 | mixed 🔵/🟣/✅ advancing | 🟡 **G3**; ⚠️ 14 pts = unparented inventory cluster (incl. new 1490398) |
| 2.2c Server — SOX Indicators | — | 0 | 0 | done (email) | |
| 2.x Credentials enabling Discovery | — | 0 | 0 | done (email) | ⚠️ prior 1444864 tasks were Active in 2.2 |
| 2.3a Database — SQL/Oracle Discovery | — | 0 | 0 | done (email) | |
| 2.3b Database — SOX Indicators | — | 0 | 0 | done (email) | |
| 2.3c Database — 90% Coverage | Stan (2) | 1 | 2 | 🔵 Active | 🟡 **thin** (1 spike only) |
| 3 Evaluate Qualys Integration | Stan (1) | 1 | 1 | 🔵 Active | 🟡 **G4** — Part 2 (1428704) unconfirmed |
| **CO5 total** | | **30** | **45** | | |

> **Reading it — coverage observations:**
> - **90%-coverage deliverables are lopsided:** Server (2.2b) carries **18 pts / 5 people**, but **Computers (2.1b) and Databases (2.3c) are 2 pts each — a single validation spike**. If 90% coverage is a CO5 acceptance target, Computer + DB cleanup look **under-resourced** vs Servers.
> - **Most governance deliverables are single-owner / single-story** (1.1a, 1.1b, 1.1d, 1.2, 1.3, 1.4, 1.5) — normal for documentation, but a bus-factor of 1 each.
> - **2.2b's 13-pt bulk is the unparented inventory/retirement cluster** — well-staffed but not formally tied to a deliverable in ADO (see flag below).
> - **Gaps:** 2.1c Computers Build Lifecycle has **no 2.4 story**; the "done per email" rows (SCCM/Discovery ×3, SOX Indicators ×2, Credentials) have **no validation/acceptance story** for CCB sign-off.

**🔴 NOT mapped to a CO5 deliverable (16 pts):**

| Stream | Staffed by (pts) | Stories | Pts | Disposition |
|--------|------------------|--------:|----:|-------------|
| ServiceNow upgrade readiness | Stan (9), Vinay (2) | 6 | 11 | Enabling — not a named CO5 deliverable; keep in 2.4 or move to 2.5/IP? |
| Network CI-class discovery | Stan (3) | 1 | 3 | **Deprioritized** per 6/29 email — pause? |
| NowAssist Duplicate CI | Kiran (2) | 1 | 2 | **Deprioritized**; already Closed — no action |

### 2.4 By Owner — Effort Alignment to CO5
Who is working on what, mapped to the formal CO5 deliverable. **Non-CO5 / unmapped work flagged 🔴.**

**Alignment summary (per owner):**

| Owner | CO5 pts | Non-CO5 pts | Total | % on CO5 |
|-------|--------:|------------:|------:|---------:|
| Stan Tomberg | 3 | 🔴 12 | 15 | **20%** |
| Kiran Dhobale | 10 | 🔴 2* | 12 | 83% |
| Bhushan Salsekar | 9 | 0 | 9 | 100% |
| Anthony de Araujo | 8 | 0 | 8 | 100% |
| Vinay Geddannavar | 6 | 🔴 2 | 8 | 75% |
| Joe Dames | 4 | 0 | 4 | 100% |
| Manuel Vazquez | 2 | 0 | 2 | 100% |
| Uloma Adelufosi | 2 | 0 | 2 | 100% |
| Anuradha Rai | 1 | 0 | 1 | 100% |
| **Total** | **45** | **16** | **61** | **74%** |

> \* Kiran's 2 non-CO5 pts = 1451940 NowAssist, already **Closed** — no active drain.
> 🔴 **Alignment flag — Stan Tomberg:** 12 of 15 pts (80%) on **non-CO5** work — the upgrade-readiness spike block (1403721/722/723/725/731, 9 pts) + the **deprioritized** network spike 1402559 (3 pts). Only 3 pts (Qualys 1428703 + DB audit spike 1480113) serve CO5. Given the 6/29 email's CO5 focus + Network Discovery deprioritization, Stan is the **least-aligned resource** — confirm the upgrade spikes belong in 2.4 (vs 2.5/IP) and whether 1402559 should pause.

**Owner → Story → CO5 Deliverable (aligned, 45 pts):**

| Owner | Story | CO5 Deliverable | State | Pts |
|-------|-------|-----------------|-------|----:|
| Bhushan Salsekar | 1480090 Data Dictionary: Computers | 1.1b DD-Computers | 🟣 Validation | 2 |
| Bhushan Salsekar | 1454371 Extract servers w/o support groups | 2.2b Server 90% | 🔵 Active | 2 |
| Bhushan Salsekar | 1487864/865/866 Export PA VMware / KY VMware / PA Physical | 2.2b Server 90% (inventory) | 🟢 Closed ✅ | 3 |
| Bhushan Salsekar | 1487871 Review Staged Retirement | 2.2b Server 90% (inventory) | 🟢 Closed ✅ | 1 |
| Bhushan Salsekar | 1487878 Execute Bulk CI Retirement | 2.2b Server 90% (inventory) | 🔵 Active | 1 |
| Bhushan Salsekar | 1490398 Retired Servers from the Server Table *(new)* | 2.2b Server 90% (inventory) | 🟣 Validation | 1 |
| Kiran Dhobale | 1480097 Data Dictionary: Business Apps | 1.1c DD-BizApps | 🟣 Validation | 2 |
| Kiran Dhobale | 1480098 Data Dictionary: Databases | 1.1d DD-Databases **[G1]** | 🟣 Validation | 2 |
| Kiran Dhobale | 1475582 BA Support Groups (496) | 1.1c DD-BizApps (data-pop) | 🔵 Active | 3 |
| Kiran Dhobale | 1487863 Create Custom Tables | 2.2b Server 90% (inventory) | 🟣 Resolved | 1 |
| Kiran Dhobale | 1487870 Stage Retirement Candidates | 2.2b Server 90% (inventory) | 🟣 Validation | 1 |
| Kiran Dhobale | 1487897 Drop Custom / Staging Tables | 2.2b Server 90% (inventory) | 🟣 Validation | 1 |
| Anthony de Araujo | 1478286 BA Classification (938) | 1.1c DD-BizApps (data-pop) | 🟢 Ready DoR | 2 |
| Anthony de Araujo | 1480112 Server audit-dashboard spike | 2.2b Server 90% | 🔵 Active | 2 |
| Anthony de Araujo | 1487872 Validate Staged Retirement | 2.2b Server 90% (inventory) | 🔵 Active | 1 |
| Vinay Geddannavar | 1480088 Data Dictionary: Servers | 1.1a DD-Servers | 🟣 Validation | 2 |
| Vinay Geddannavar | 1455832 Server env-field recommendation | 2.2b Server 90% | 🟣 Validation | 2 |
| Vinay Geddannavar | 1487867/868/869 Import PA VMware / KY VMware / PA Physical | 2.2b Server 90% (inventory) | 🟣 Validation | 3 |
| Joe Dames | 1480099 Data Certification pilot | 1.2 Data Cert | 🟢 Ready DoR | 1 |
| Joe Dames | 1480111 BA audit-dashboard spike | 1.1c DD-BizApps | 🟣 Validation | 2 |
| Stan Tomberg | 1480113 Database audit-dashboard spike | 2.3c Database 90% | 🔵 Active | 2 |
| Stan Tomberg | 1480114 Computer audit-dashboard spike *(reassigned from Anthony)* | 2.1b Computer 90% | 🔵 Active | 2 |
| Stan Tomberg | 1428703 Qualys plugin Part 1 | 3 Qualys | 🔵 Active | 1 |
| Stan Tomberg | 1504314 Populate CI Owner *(new)* | — unparented | 🟢 Refinement Ready | — |
| Manuel Vazquez | 1480102 ESS-02 alignment confirmed | 1.3 ESS-02 | 🟢 Ready DoR | 1 |
| Manuel Vazquez | 1480107 Monthly CCB cadence | 1.5 Monthly CCB **[G5]** | 🟢 Ready DoR | 2 |
| Uloma Adelufosi | 1480105 SOX BA identified + access controls | 1.4 SOX BA | 🟢 Closed ✅ | 1 |
| Anuradha Rai | 1487883 Verify Retirement Results | 2.2b Server 90% (inventory) | 🟢 Refinement Ready | 1 |

**🔴 UNMAPPED / NON-CO5 — needs a disposition decision (16 pts):**

| Owner | Story | Why flagged | State | Pts |
|-------|-------|-------------|-------|----:|
| Stan Tomberg | 1403721 Analyze impact: CI class hierarchy / customizations | Upgrade readiness — not a CO5 deliverable | 🟢 Refinement Ready | 3 |
| Stan Tomberg | 1403722 Assess upgrade impact on IRE | Upgrade readiness — not CO5 | 🟢 Refinement Ready | 2 |
| Stan Tomberg | 1403723 Validate authoritative sources / precedence / flapping | Upgrade readiness — not CO5 | 🟢 Refinement Ready | 2 |
| Stan Tomberg | 1403725 Impact: Discovery / integration touchpoints | Upgrade readiness — not CO5 | 🟢 Refinement Ready | 1 |
| Stan Tomberg | 1403731 Impact: governance controls / KPIs / operating model | Upgrade readiness — not CO5 | ⚪ New | 1 |
| Vinay Geddannavar | 1411237 Validate Dynamic IRE Post-Australia | Upgrade readiness — not CO5 | 🔵 Active | 2 |
| Stan Tomberg | 1402559 Compare CI Class Sources | **Network Discovery — deprioritized** per 6/29 email | 🟢 Refinement Ready | 3 |
| Bhushan Salsekar | 1490398 Retired Servers from the Server Table *(new)* | Retirement cleanup — likely CO5 2.2b Server 90%; unparented | 🟣 Validation | 1 |
| — | 1504372 Filter Retired CIs from CI field selection across Incidents *(new)* | Retirement hygiene — no assignee yet | ⚪ New | — |
| Kiran Dhobale | 1451940 NowAssist: Activate Manage Duplicate CIs (Part 1) | **NowAssist — deprioritized**; already Closed | ⚪ Closed | 2 |

> 🔶 **Mapped by inference, but no formal ADO parent:** the **inventory + bulk-retirement cluster (1487863–1487897, 13 pts)** is mapped to Server 90% (2.2b) above, yet has **no feature/objective parent in ADO** and may split with Computer 90%. *Operationally* CO5-aligned, *formally* unmapped — confirm its feature home so it can count toward a deliverable at acceptance.

### CO5 Acceptance Timeline (from the alignment email)

| Milestone | Date | Deliverable |
|-----------|------|-------------|
| Data Certification pilot start | 6/29 | Data Cert |
| Qualys — formalize/document requirement | 6/29 → PM Validation 6/30 | Qualys |
| Data Dictionary — finalize docs | 6/30 | Governance |
| SOX BA + Monthly CCB — PM Validation (Sonika) | 6/30 | SOX, CCB |
| Data Dictionary — Customer Validation (Sonika) | 7/1 | Governance |
| ESS-02 — validate scope (Jason Dubreuil) → finalize 7/3 → Sonika 7/6 → Jason 7/7 | 7/1–7/7 | ESS-02 |
| Data/audit cleanup — meet audit targets (Computers/Servers/DB) | 7/7 (aggressive) – 7/20 | Data Ingestion |
| Data Dictionary — **CCB Review/Feedback** | 7/7 – 7/20 | Governance |
| Data Dictionary — **CCB Approval (next CMDB CCB)** | **7/21** | Governance |

> 🔗 The 7/21 Data Dictionary CCB approval is the same monthly CCB that the [[../Config-Mgmt-Plan/configuration-management-plan-stage1]] Stage 1 `[CCB confirm]` ratification agenda targets.

### Watch / Risks
- **Most CO5 acceptance dates land *after* the 6/30 contractual deadline** (CCB approval 7/21). The $533,775 holdback risk in [[../co5-deliverable-tracking]] stands unless CO6 is signed before 7/1.
- **Dev code freeze Jul 4–18** spans the tail of 2.4 — dev-dependent CO5 work must land before 7/4 (PI-2 Risk #10).
- **16 pts (26%) sit outside CO5** — confirm the 11-pt upgrade-readiness spike block is intended for 2.4 given the CO5 focus, or can shift to 2.5/IP.
- **Inventory + retirement cluster (14 pts incl. new 1490398) has no feature/objective parent** — confirm home + planned scope (flagged in [[pi2-objectives-features-stories]]).
- ⚠️ **1403721 / 1403722 / 1403723 (Stan's upgrade spikes, 7 pts) not visible in 7/6 ADO grid** — confirm whether moved to another iteration or removed from 2.4.
- 🆕 **Two new unparented items added:** 1504314 Populate CI Owner (Stan) and 1504372 Filter Retired CIs (unassigned) — confirm feature parent, owner for 1504372, and points.
- ✅ **CO5 Deliverable 1.4 (SOX BA) closed** — 1480105 Closed. Confirm with Sonika for CO5 acceptance sign-off.

### Ceremonies
- Sprint Planning 2.4 — ~06/24 · Backlog Refinement — TBD · Review/Showback + Retro — ~07/07

---

---

## Iteration 2.5 — Jul 8 – Jul 21, 2026 | ⏳ Planning

> ADO sprint planning and story-move updates expected 7/7. Section will be populated once the 2.5 board grid is received.

### Known carry-ins from 2.4 (pending confirmation)

Items likely to roll into 2.5 based on state as of 7/6:
- Upgrade-readiness spike block (1403721/722/723/725/731 — Stan, ~9 pts) — confirm carry-in vs. defer to 2.6/IP
- 1411237 Validate Dynamic IRE Post-Australia (Vinay, Active) — likely continues
- 1480099 Data Certification pilot (Joe, Ready DoR) — confirm if starting in 2.5
- 1480102 ESS-02 alignment (Manuel, Ready DoR) — per CO5 timeline, closes by 7/7
- 1480107 Monthly CCB cadence (Manuel, Ready DoR) — 7/21 CCB is the target gate
- 1487872 Validate Staged Retirement (Anthony, Active) — likely completes or carries
- 1487878 Execute Bulk CI Retirement (Bhushan, Active) — likely completes or carries
- 1487883 Verify Retirement Results (Anu, Refinement Ready) — follows 1487878
- 1504314 Populate CI Owner (Stan, Refinement Ready) — unpointed; needs refinement
- 1504372 Filter Retired CIs (Unassigned, New) — needs owner + points before carry-in

> ⚠️ **1402559 Compare CI Class Sources** (Stan, deprioritized) — confirm whether it moves to 2.5 or stays parked.

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
