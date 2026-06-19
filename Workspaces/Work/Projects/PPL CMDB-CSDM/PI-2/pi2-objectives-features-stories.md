---
type: team-artifact
workspace: Work
project: CMDB-CSDM
pi: PI-2
updated: 2026-06-17
tags: [work, cmdb-csdm, pi-planning, backlog, features]
---

# PI-2 Objectives → Features → Stories

Full traceability view: PI objectives → ADO features → stories/spikes with status.
Updated as of 2026-06-17 | ADO snapshot: story status as of **6/17 (Iteration 2.3 story grid; supersedes 6/12 12:00pm pull on conflicts)** | Active iteration: **2.3** (Jun 10 – Jun 23)

> **6/17 feature-grid reconciliation** — Reconciled against the ADO feature list (feature-level State column). Added new feature **OCM 2026.PI2 (1428659)** and the four NowAssist PI-3 phase IDs (1451935/1451936/1451937/1451938). Annotated feature-level State mismatches inline (⬇️ **Feature State:** lines) where the ADO *feature* state lags its *story* states.
> **6/17 dependency reconciliation** — Reconciled against the ADO dependency grid. Added 6 new dependencies: 1383519 (Qualys, Stream C), 1420565 (Computer Class 1354794), 1383487 (Network gear, 1356646), plus 3 cross-cutting (1416953, 1420575, 1416576) in the new **Cross-Cutting Dependencies** section. Added Iter 2.3 to the two previously-tracked deps (1383493, 1383515).
> **6/19 issue-grid review** — Reconciled against the ADO Issue grid (7 issues). Already-tracked: 1465952 (Qualys), 1425785 & 1425697 (both in [[Team/impediments-log]]). **State change:** **1465952 (Qualys Plugin Replacement) is now Closed** in ADO (we had it Active/blocker) — ⚠️ may unblock stories 1428703/1428704; **not auto-flipped — confirm with Rich Santillo/Stan**. Added 4 untracked **Closed** issues inline: **1438967** (PMDB SOX/DR custom-fields governance → 1354797), **1464224** (SCCM two timestamp fields decision → 1356826/1403762; closes Sonica-approval action), **1416676** (EA Bus App data / Data Cert impact → P2), **1402520** (key-person dep on CI attribute-mapping spikes, Ray Reuter → 1354797).
> **6/19 feature-grid review** — Re-validated all 26 tracked features against the ADO feature grid. All present. Findings: (1) **1451930** (NowAssist Dup CI Elim, Phase 2) advanced **New → Active** (Anuradha Rai); (2) **1406668 "CMDB Governance & Monthly CCB Meetings" is Removed** in ADO — it is the actual parent of Stream A spike 1420244, leaving that spike orphaned to a dead feature (flag inline below); (3) three **Removed** Service Mapping features (1355872/1355873/1355875, PI2 Iter 4/5/6) exist in the grid — superseded by the Wave 17–21 features, not tracked here; (4) grid **parent anomalies** noted inline for 1383523 (parent = Airlift Pre-Migration epic) and 1411480 (parent = "Create scripted REST API for SailPoint").
> **6/17 spike/task reconciliation (ADO authoritative)** — Corrected against the ADO spike & task grids. Spikes: 1421790 re-filed 1383523→1354797 (state→Validation); 1355167→Active; 1402555→Active; 1470837→Active; 1339116→Refinement Ready; 1403725→Refinement Ready (2.4); 1411237 reclassified Story→Spike (Refinement Ready, 2.4); 1234585 flagged orphan (no ADO parent). Tasks: 1470808 parent corrected 1416384→1407572 (relocated to Feature 1354794); 1444864 flagged (Validation story w/ 6 Active child tasks in 2.2). Closed-task history intentionally NOT imported (6/17 — dismissed as not actionable).

---

## PI Obj 0 — Enable Governed VMware-to-Azure Migration Through CMDB-Driven Intelligence
**ADO Obj:** 1420079 | **Op Priority:** 0 (most urgent) | **BV:** 10

### Feature 1420613 — CMDB Support for Air Lift
⬇️ **Feature State (ADO 6/17):** **Defining** (Iter 2.1) — ⚠️ lags its stories, which are all in Validation. Confirm why the feature hasn't advanced past Defining.

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1418610 | Story | Airlift to Azure Pre-Migration | Laurent / Alex Lim | — | 2.3 | 🟣 Validation |
| 1418618 | Story | Airlift to Azure During Migration | Laurent / Alex Lim | — | 2.3 | 🟣 Validation |
| 1418621 | Story | Airlift to Azure Post-Migration | Laurent / Alex Lim | — | 2.3 | 🟣 Validation |
| 1416384 | Story | Auto Populate CI Owner / Support Group / Tech Owner for Server Class | — | — | 2.3 | 🟢 Active — ⚠️ not on ADO pulls (virtual variant 1407572 = Validation as of 6/12, NOT Done) |

> **6/9** — Dev admin access carry-over issue resolved. ✅

---

## PI Obj 1 — Automate Discovery Coverage for Network Gear CI Classes
**ADO Obj:** 1366657 | **Op Priority:** 1 | **BV:** 10

### Feature 1383523 — Unplanned Backlog - CMDB Workstream
> ⚠️ **6/19 parent anomaly:** ADO grid shows this feature's parent = **"Airlift to Azure Pre-Migration"** epic and owner **Josh Sterling** — points to **P0 Airlift**, not P1 where we file it. Confirm correct objective home. State: New.

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| — | — | No confirmed stories/spikes in ADO | — | — | — | ⚠️ 1421790 (Gap Analysis Servers) re-filed to authoritative parent 1354797 on 6/17 |

### Feature 1356646 — Network Device Coverage Reconciliation - Group 1

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1402555 | Spike | Identify CI Classes for Group 1 | Stan + Joe | 3 pts | 2.3 | 🟢 Active — updated to ADO 6/17 (was Ready DoR) |
| 1402559 | Spike | Compare CI Class Sources | — | 3 pts | — | ⚪ New |
| 1444864 | Story | Fix Credentials for Servers, Databases and Network | Tony De Araujo | 5 pts | 2.3 | 🟣 Validation |
| 1459721 | Story | Testing new SNMP credentials, new MID server parameters related to dns | Stan | — | 2.3 | 🟣 Validation — 🆕 6/17 story pull; credential/MID family (parent feature unconfirmed) |
| 1383487 | Dependency | Stakeholders requirements on network gear to Initially Assess | Dan Carabelas | — | 2.2 | ⚪ New — 🆕 6/17 |

> ⚠️ **6/17 task-layer flag (1444864):** Story is 🟣 Validation, but ADO shows **6 Active child tasks in Iteration 2.2** (CSDISCOVERY & GWIZ Oracle creds, MID `mid.dns.resolver` reconfig/test — Stan/Tony). Confirm whether the tasks are stale carryover or the story state is ahead — this credential work gates discovery for P1/P3.
> Additional **New** child tasks (6/17): **1445184** (request MID-server comms, Tony) and **1445244** (test Service Mapping after MID `mid.dns.resolver` reconfig, Tanzeel) — 1445244 explicitly links this credential/MID work to enabling **P3 Service Mapping** discovery.

### Feature 1356826 — SCCM Server Class Precedence Updates

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1403763 | Story | SCCM Server Hardware & Software Attribute Data Precedence | Vinay | 1 pt | 2.3 | 🟣 Validation |
| 1403760 | Story | SCCM: Servers — Domain and Network Attribute Data Precedence | Vinay | 1 pt | 2.3 | 🟣 Validation |
| 1403762 | Story | SCCM: Servers — Last Seen Timestamp Alignment | Vinay | 1 pt | 2.3 | 🟣 Validation — approval gate cleared (was blocked on Sonika Das) |
| 1403759 | Story | SCCM: Servers — Remove SCCM Attributes | Vinay | 1 pt | 2.3 | 🟣 Validation — ⚠️ reclassified Spike→User Story + title aligned per 6/17 story grid (was "De-Prioritize SCCM Attributes (asset tag, OU name)") |
| 1464224 | Issue | SCCM Two Date Time New Fields Required — Decision | Sonika Das | — | 2.2 | ⚪ Closed — 🆕 6/19 issue grid. Sonica-approval decision for **1403762** (two new timestamp attributes); Closed = approved → resolves the open "obtain Sonica approval" action item |

> **6/11** — Task 1468856 (Unit Testing, Venkateswarlu Manikanta) **Closed** — child of 1403762 (SCCM Last Seen Timestamp Alignment). ✅

### Feature 1354797 — Server Class Data & Form Updates
⬇️ **Feature State (ADO 6/17):** **Ready** (Iter 2.3) — has an Active child story (1454371) below.

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| — | Story | CI Auto-Population: CI Owner | — | TBD | 2.1 | ⚠️ ADO ID pending (Anu to confirm) |
| — | Story | CI Auto-Population: Support Group | — | TBD | 2.1 | ⚠️ ADO ID pending |
| — | Story | CI Auto-Population: Technical Owner | — | TBD | 2.1 | ⚠️ ADO ID pending |
| — | Story | Custom Fields: Asset Criticality, RPO, RTO, Recovery Tier, Tier Data Classification, Stocks Indicator, Stocks Type | — | TBD | 2.1 | ⚠️ ADO ID pending — in QA/UAT per 06/08 decision |
| 1355167 | Spike | Define a Solution for Migrating Business App to Service Instance | Tony De Araujo | 3 pts | 2.3 | 🟢 Active — ✅ set to ADO (authoritative) 6/17; was Validation in our tracking |
| 1454371 | Story | Extract Servers Without Support Groups and Validate Routing | Bhushan Salsekar | 2 pts | 2.3 | 🟢 Active |
| 1421790 | Spike | Gap Analysis for Servers — Linux & Windows | Tony De Araujo | 0 pts | 2.3 | 🟣 Validation — ✅ parent confirmed 1354797; re-filed from 1383523 on 6/17 |
| 1438967 | Issue | Governance Request — CMDB Application Service SOX & DR Customization Enhancement | Alex Phan | — | 2.2 | ⚪ Closed — 🆕 6/19 issue grid. RAID/governance issue for the PMDB Application Service custom fields (edit rights restricted to Cyber Risk & DR, 6/08 decision); Closed = approved. ⚠️ feature mapping inferred — confirm |
| 1402520 | Issue | Dependency on key member on CMDB CI Attribute Mapping Spikes | Raymond B. Reuter Jr | — | 2.1 | ⚪ Closed — 🆕 6/19 issue grid. Key-person dependency on **Ray Reuter** (SCCM data owner, cf. Risks #12/#13) for CI attribute-mapping spikes. ⚠️ feature mapping inferred — confirm |

> **Decisions:** CI Owner Autopopulation approved 06/08 (physical CIs only; virtual excluded). PMDB Application Service custom fields approved 06/08; edit rights for 4 fields restricted to Cyber Risk and DR teams. Both moving to QA/UAT.

### Feature 1354794 — Computer Class Data & Form Improvements

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1455858 | Story | Virtual Location Management | Kiran Dhobale | 2 pts | 2.3 | 🟢 Active — ⚠️ ADO parent is "Computer Class Data Reconciliation", not 1354794 |
| 1452028 | Story | iteam import (laptop / vendor purchase feed) | Uloma | — | — | ⚠️ Scope clarification pending — confirm vs. Cherwell import |
| 1413033 | Spike | Import User Location Values in sys_user | Vinay | 2 pts | 2.3 | ⚪ Done/Closed per 6/11 board — ⚠️ UNCONFIRMED: absent from 6/12 12pm pull; sibling "Done" item 1407572 turned out Validation |
| 1407572 | Story | Auto Populate CI Owner/Support/Tech Owner Group (Virtual Computers) | Bhushan Salsekar | 2 pts | 2.3 | 🟣 Validation — ⚠️ 6/11 board wrongly showed Done |
| 1420565 | Dependency | End User Location Mapping for Physical Computer CIs | Sonika Das | — | 2.1 | 🟢 Active — 🆕 6/17; corroborates open blocker "HCM needed for computer location (Sonika)" |

> **6/12** — Task 1460378 (CMDB:AVD Team coordination required for data, Kiran Dhobale) **Closed**. ✅ Supports 1455858 (Virtual Location Mgmt).
> **6/11** — Task 1470808 (Unit Testing, Venkateswarlu Manikanta) **Closed** — child of **1407572** (Virtual Computers Auto-Populate). ✅ ⚠️ Corrected 6/17 per authoritative ADO: previously mis-attributed to 1416384 under P0.

### Feature 1411480 — CMDB PI2.26 Enhancements
⬇️ **Feature State (ADO 6/17):** **Story Mapping** (Iter 2.5) — ⚠️ pre-commitment state, yet has a Validation child (1387236). State lag.
> ⚠️ **6/19 parent anomaly:** ADO grid shows this feature's parent = **"Create scripted REST API for SailPoint"** — not noted in our P1 mapping. Confirm linkage.

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1387236 | Story | Discovery: Install AIM API on PROD MID Servers | Tony De Araujo | 1 pt | 2.3 | 🟣 Validation |

### Feature 1355888 — Update Operational Monitoring Activities P2
> ✅ **ID corrected 6/12** — was wrongly listed as 1354797 (which belongs to "Server Class Data & Form Updates" above). True Feature ID is **1355888** (per validation worksheet).

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1339116 | Spike | Define Process to Monitor / Update CI Owners Who Have Left PPL | Anuradha Rai | 0 pts | 2.3 | 🟢 Refinement Ready — updated to ADO 6/17 (was Ready DoR) |

### Feature 1355890 — Support ServiceNow Upgrade Analysis
⬇️ **Feature State (ADO 6/17):** **Ready** (Iter 2.4) — feature targets iteration 2.4, not current 2.3.

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1403733 | Spike | Identify deprecated plugins/features impacting CMDB capabilities | Stan | 2 pts | 2.3 | 🟢 Ready (DoR) — unblocked pending sandbox restore |
| 1403725 | Spike | Impact Assessment of Discovery & Integration Touchpoints (mid-stream) | Stan | 1 pt | 2.4 | 🟢 Refinement Ready — updated to ADO 6/17 (was Ready) |
| 1411237 | Spike | Review & Validate CMDB Dynamic IRE Behaviour Post-Australia Upgrade | Stan Tomberg | 1 pt | 2.4 | 🟢 Refinement Ready — ⚠️ reclassified Story→Spike per ADO 6/17; was Defining/2.3 |

> **Blockers:** DB and SNMP credentials in progress (Tony). Server ownership not accurate. CI Ownership for servers — Joe has plan, OCM review required. HCM needed for computer location (Sonika). SCCM full attribute precedence map not yet complete — risk of conflicting rules across stories.

---

## PI Obj 2 — Establish CI Data Certification Program
**ADO Obj:** 1420082 | **Op Priority:** 1 | **BV:** 8

> ℹ️ **6/19 issue grid — Issue 1416676** "Enterprise Arc – Bus App Data Updates Not Ready & Data Cert Impact" (Joe Dames) — ⚪ **Closed**. Flagged Business App data readiness as a risk to Data Certification; ties to cross-cutting EA dep **1416576**. ⚠️ objective mapping inferred — confirm.

### Feature 1247179 — Data Certification Pilot - Functionality

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1435307 | Story | Data Certification Pilot Changes | Bhushan Salsekar | 3 pts | PI Planning | 🟣 Validation — ⚠️ re-filed from P1 (was mislabeled "correctness metric") |

### Feature 1371672 — Governance Model for Requesting New Business Applications

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| — | — | No confirmed stories in ADO | — | — | — | ⚠️ Feature-level only |

### Feature 1382404 — Data Certification Rollout

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| — | — | No confirmed stories in ADO | — | — | — | ⚠️ Feature-level only |

### Feature 1402958 — Data Certification Pilot - Implementation Planning

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| — | — | No confirmed stories in ADO | — | — | — | ⚠️ Feature-level only |

### Feature 1402979 — Data Certification Pilot - Implementation Support
⬇️ **Feature State (ADO 6/17):** **Defining** (Iter 2.1) — ⚠️ lags badly: its story (1402727) is UAT-signed-off with PROD deploy 06/23. Feature should advance.

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1402727 | Story | Update Data Certification Dashboard | Kiran | — | — | 🟢 UAT signed off (Sonika, 6/10) — PROD deploy 06/23 |

> **6/10** — Sonika signed off on UAT. ✅
> **Deployment Timeline:** UAT by 06/15 → PROD CR 06/19 → PROD Deploy 06/23 → Todd validates 06/24–06/25

---

## PI Obj 3 — Expand Service Mapping Foundation
**ADO Obj:** 1366660 | **Op Priority:** 2 | **BV:** 9

> ℹ️ **6/19:** ADO grid carries three **Removed** Service Mapping features — **1355872 / 1355873 / 1355875** (PI2 Iteration 4 / 5 / 6). Superseded by the Wave 17–21 features below; not tracked here. Documented so they aren't mistaken for missing scope.

### Feature 1355866 — Service Mapping PI2 Wave 17 & 18

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1380747 | Story | MV90 User Access | Tanzeel | — | — | 🟢 Active |
| 1380757 | Story | RIE Electric Wholesale Settlement | — | — | — | 🟢 Active |
| 1400703 | Story | Vault Inspection System | — | — | — | 🟢 Active |
| 1281161 | Story | WATT | — | — | — | 🟢 Active |

### Feature 1355868 — Service Mapping PI2 Wave 19 & 20

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1420634 | Spike | Review Apps Being Migrated & Impact to Service Mapping | — | — | — | 🟢 Active |
| 1326754 | Spike | Evaluate Automated Service Mapping via Endpoint-Based Discovery | — | — | — | 🟢 Active |
| 1383493 | Dependency | Date Mapping from App PoC — EndPoint (Credentials Support) | John Benedict Ortega | — | 2.3 | ⚪ New |

### Feature 1355871 — Service Mapping PI2 Wave 20 & 21

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| — | — | No confirmed stories in ADO | — | — | — | ⚠️ Not yet populated |

> **6/9** — Credential updates working. Discovery connecting to devices and surfacing Linux servers, Oracle databases, listeners, and related services previously not visible. Single test subnet complete; additional subnet scans in progress — discovery counts expected to increase.
> **Open:** DNS issue (Alex to attempt email resolution with Christian's update). App owner sign-off validation outstanding.

> **6/17 task-layer review (Service Mapping):** ADO task grid (all New, Tanzeel Rehman) shows end-to-end service-map work broken into a consistent 4-step pattern per app (1-Data Gathering → 2-Build Mapping → 3-Validate & Sign-off → 4-Publish). Confirms **WATT (1281161)** and **Vault Inspection System (1400703)** are already tracked.
> **Additional target apps surfaced by the task layer but NOT yet in our wave features** — parent story IDs and wave assignment not shown in the task grid; confirm with Tanzeel/Alex:
> - Oracle Opower (Iter 2.1)
> - Einstein (Iter 2.2)
> - Oracle Enterprise — likely "…Manager" (Iter 2.2)
> - Foglight for Data… — likely "…base" (Iter 2.2)
> - OEM (Iter 2.2)
> - Oceana System (Iter 2.2)
>
> **SolarWinds** — service-map **evaluation/PoC pilot** under an "*Evaluate* Service Mapping…" parent (distinct from the per-app "Gather/Build/Validate/Publish" stories; ties to spike 1326754 endpoint-based discovery). Tasks 1462418 / 1462424 New as of 6/17.
>
> Standalone task **1426578** "Add drop down box in ITEAM" (Uloma, **no parent**) — likely ITEAM/iteam-related (cf. 1452028 iteam import under Computer Class 1354794); needs triage.

---

## PI Obj 4 — Prepare CMDB for Regulatory and Security Integrations
**ADO Obj:** 1366662 | **Op Priority:** 2–5 (varies by stream) | **BV:** 8

*This objective covers three work streams.*

### Stream A — Governance / CCB | Op Priority: 2
**Features:** 1250905, 1370224
> 🔴 **6/19 flag:** Spike 1420244's actual ADO parent feature — **1406668 "CMDB Governance & Monthly CCB Meetings" (Joe Dames) — is Removed** in the ADO feature grid. That leaves the Stream A governance/CCB spike orphaned to a dead feature, and Stream A has no live feature home (1250905 = Qualys/Stream C, 1370224 = NERC-CIP/Stream B). **Action:** confirm where CCB/governance work lives now, or restore/replace 1406668.

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1420244 | Spike | ESS-02 Policy and CMDB Alignment | Joe Dames | 0 pts | — | 🟢 Active — ADO parent "CMDB Governance & Monthly…" (**1406668, Removed** — see flag above) |

> **6/8** — CCB Meeting scheduled **06/16**; CMDB Audit Sync scheduled **06/18**.
> Reference: PPL MS Teams > General > Accenture & PPL - Working Documents > 18 - CMDB 2026 > CCB Meetings
> **Open:** Engage Jason Dubriel (ESS 02). Document CMP.

### Stream B — NERC-CIP Security Requirements | Op Priority: 4
**Features:** 1250905, 1370224

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1383515 | Dependency | Cyber Security Team Coordination — NERC CIP | Sonika Das | — | 2.3 | ⚪ New |

> **Open:** Engage Sonika / Cyber compliance (action from 5/20). Engage Jason Dubriel. Document CMP.

### Stream C — Qualys Integration | Op Priority: 5
**Features:** 1250905, 1370224 | **Actual ADO parent of stories below:** "Integration Qualys & ServiceNow (CMDB Data Read Only) (PI2)"

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1428703 | Story | Install x_qual5_itam_nwapp Plugin on Dev, Test, and Prod (Part 1) | Stan | 1 pt | PI-2 | 🔴 Active — BLOCKED |
| 1428704 | Story | Configure Qualys Integration for CMDB to Qualys (Part 2) | Stan | 1 pt | PI-2 | 🔴 Active — BLOCKED |
| 1234585 | Spike | Define and Configure Data Scope and Import Views in Qualys | Stan | 1 pt | PI-2 | 🟢 Ready (DoR) — ⚠️ ADO shows NO parent (6/17); kept under Stream C by topic, needs parent link in ADO |
| 1465952 | Issue | Qualys Plugin Replacement Awaiting Vendor Approval | Rich Santillo | — | 2.3 | ⚪ **Closed per 6/19 issue grid** (was 🔴 Active blocker) — ⚠️ **may unblock 1428703/1428704; story states NOT auto-flipped — confirm vendor approval landed with Rich/Stan** |
| 1383519 | Dependency | Qualys Development / Support Team | Rich Santillo | — | 2.2 | 🟢 Active — 🆕 6/17; ties to blocker 1465952 (same owner) |

> **Phase 1 (PI-2):** Read-only integration.
> **Phase 2 (PI-3):** Two-way integration — if needed; long-term data completeness value.
> **🔴 6/12 BLOCKER (confirmed):** 1428703 & 1428704 are flagged **Blocked** in ADO — *"Qualys has replaced plugin version. Uninstalled previous plugin, requested a new one. Pending vendor approval."* This confirms Issue 1465952 is gating both stories. Track with Rich Santillo / Stan.

---

## PI Obj 5 — Embed NowAssist AI Across CMDB and ITSM Workflows
**ADO Obj:** 1408764 | **Op Priority:** 3 | **BV:** 7

### Feature 1436574 — Foundation & Readiness: Activate NowAssist for CMDB and Establish Baseline
**Owner:** Joe Dames | **State:** Ready
> ✅ **Feature ID confirmed 6/11** (was "unconfirmed — Anu to verify"). Stories created by Alex Phan 06/08.

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| 1436576 | Story | Confirm Platform Prerequisites for NowAssist Activation (Part 1) | Kiran Dhobale | 1 pt | 2.3 | ⚪ Closed — ✅ per 6/17 story pull (was Active) |
| 1436579 | Story | Activate NowAssist for CMDB Plugin | Kiran Dhobale | 1 pt | 2.3 | 🟢 Resolved — per 6/17 story pull (was Ready DoR) |
| 1436592 | Story | Activate CI Summarization Skill | Kiran Dhobale | 1 pt | 2.3 | 🟢 Active — per 6/17 story pull (was Ready DoR) |
| 1436593 | Story | Activate Contextual CI Form Help Skill | Kiran Dhobale | 1 pt | 2.3 | 🟢 Ready (DoR) |
| 1436581 | Spike | NowAssist: Establish CMDB Health Baseline Score (Last Part) | — | 2 pts | 2.3 | 🟢 Ready (DoR) |

> **Related (no ADO parent set):** Spike 1470837 — Analyze CMDB health indicators currently configured for 35 principal CI classes (🟢 Active per ADO 6/17; was Ready DoR on 6/11 board). Feeds the health baseline score.
> **PI-3 — Feature 1451930:** Now Assist Duplicate CI Elimination (Phase 2), 🟢 Active (Anuradha Rai) per 6/19 grid (was New). ⚠️ **Two phase-numbering schemes in play:** ADO labels this feature set as Foundation/Readiness = *Phase 1* (1436574) and Duplicate CI Elimination = *Phase 2* (1451930); but [[nowassist-implementation-plan]] sequences Duplicate CI Elimination as *Phase 1* of its 5-phase PI-3 rollout. Confirm which scheme leadership reporting uses.
> **PI-2 scope:** OOB capability assessment only — CI Summarization and contextual form help.
> **PI-3 scope:** Full 5-phase NowAssist rollout. ADO feature IDs now confirmed (6/17):
> | Phase | ADO ID | Feature | State |
> |-------|--------|---------|-------|
> | Phase 2 | 1451930 | NowAssist Duplicate CI Elimination | 🟢 Active (Iter 2.3) — Anuradha Rai — updated to ADO 6/19 grid (was New) |
> | Phase 3 | 1451935 | NowAssist Natural Language CMDB Search | New |
> | Phase 4 | 1451936 | NowAssist Guided CI Creation | New |
> | Phase 5 | 1451937 | NowAssist Governance Advice Agentic Workflow | New |
> | Phase 5 | 1451938 | NowAssist Custom Skills / NASK | New |
> See [[nowassist-implementation-plan]]. (Note: ADO labels Foundation/Readiness as Phase 1; phase numbering caveat above still applies.)
> **Open (5/20):** Assess NowAssist capabilities available in Australia vs Yokohama (Joe D).
> **6/12** — All 4 stories reassigned from Karen to Kiran Dhobale. Although Kiran has moved teams, the NowAssist stories supporting this objective are being delivered in iteration 2.3. ✅
> ✅ **6/12 confirmed:** 1436576 is **Active**; 1436579 / 1436592 / 1436593 remain Ready DoR. (Resolves the earlier board-vs-view variance.)

---

## Unmapped Feature — OCM (Organizational Change Management)
> 🆕 **Added 6/17** from the ADO feature grid — not previously tracked in this doc and not yet mapped to a PI objective. Confirm its objective home (likely a cross-cutting OCM/adoption stream).

### Feature 1428659 — OCM 2026.PI2
⬇️ **Feature State (ADO 6/17):** **Active** (Iter 2.6) | **Owner:** Nora Lizenberg

| ADO ID | Type | Title | Owner | Points | Sprint | Status |
|--------|------|-------|-------|--------|--------|--------|
| — | — | No stories pulled into this doc yet | Nora Lizenberg | — | 2.6 | ⚠️ Feature-level only — triage needed |

> **Open:** Map to a PI objective (or flag as standalone OCM stream). Pull child stories. Confirm scope with Nora Lizenberg.

---

## Cross-Cutting Dependencies
> 🆕 **Added 6/17** from the ADO dependency grid — dependencies that span multiple objectives or have no clear feature home. Single-objective dependencies are filed under their feature above (Qualys 1383519 → Stream C; End User Location 1420565 → 1354794; Network gear stakeholders 1383487 → 1356646).

| ADO ID | Title | Owner | State | Iter | Spans / Note |
|--------|-------|-------|-------|------|--------------|
| 1416953 | Cloud Migration Impact to CMDB Data Accuracy & Change Coordination | Alex Phan | 🟢 Active | — | **P0 Airlift** (VMware→Azure); change-coordination angle is cross-cutting |
| 1420575 | Azure Airlift Migration Impact Assessment for Discovery & Service Mapping | Andrew Ajayi | ⚪ New | 2.1 | **P0 Airlift + P3 Service Mapping** — spans two objectives |
| 1416576 | Enterprise Architect team review and update | Matthew Newhouse | ⚪ New | 2.2 | ⚠️ **No clear objective home** — generic EA review; needs triage |

---

## Past-Iteration Carryover
> 🆕 **6/17 — iteration-review artifact.** Non-closed **tasks** stranded in iterations *prior* to the active **2.3** (Jun 10–23). Compiled from the ADO task grids; reflects only the pages reviewed — if the query has more pages there may be additional carryover. ~44 non-closed tasks are sitting one-to-two iterations back.

### Iteration 2.1 — not closed (14)
**Service Mapping** (⚪ New · Tanzeel) — 4-step pattern (DG = Data Gathering, BM = Build Mapping, V&S = Validate & Sign-off, Pub = Publish):

| App | Tasks |
|-----|-------|
| WATT | 1428247 (DG), 1428250 (BM), 1428253 (V&S), 1428254 (Pub) |
| Oracle Opower | 1428245 (DG), 1428246 (DG ⚠️ parent cut off — confirm), 1428249 (BM), 1428252 (V&S), 1428255 (Pub) |
| Vault Inspection System | 1428921 (DG), 1428923 (BM), 1428924 (V&S), 1428925 (Pub) |

**Other:**
- **1426578** — Add drop down box in ITEAM (⚪ New · Uloma · no parent)

### Iteration 2.2 — not closed (30)
**Credentials — parent 1444864 "Fix Credentials for Servers, Databases and Network":**

| Task | Title | State | Owner |
|------|-------|-------|-------|
| 1445257 | Configure CSDISCOVERY credential (Linux) | 🔵 Active | Stan |
| 1445274 | Test Linux Server discovery w/ CSDISCOVERY | 🔵 Active | Stan |
| 1445306 | Configure GWIZ_MON_ORACLE_DB_PA credential | 🔵 Active | Stan |
| 1445202 | Configure MID servers `mid.dns.resolver` | 🔵 Active | Stan |
| 1445239 | Test Discovery after MID reconfig | 🔵 Active | Stan |
| 1445339 | Test PA Oracle DB discovery | 🔵 Active | Anthony |
| 1445184 | Submit request — MID-server comms | ⚪ New | Anthony |
| 1445244 | Test Service Mapping after MID reconfig | ⚪ New | Tanzeel |

**Service Mapping** (⚪ New · Tanzeel) — 4-step pattern per app:

| App | Tasks |
|-----|-------|
| Einstein | 1428261, 1428266, 1428269, 1428272 |
| Oracle Enterprise | 1428263, 1428267, 1428270, 1428273 |
| Foglight for Data… | 1428265, 1428268, 1428271, 1428275 |
| OEM | 1428929, 1428931, 1428934, 1428936 |
| Oceana System | 1428939, 1428942, 1428944, 1428947 |
| SolarWinds (Evaluate/PoC) | 1462418 (V&S), 1462424 (Pub) |

### Iteration-review read
- **36 of ~44 are Service Mapping** (all New, Tanzeel) — a large body of service-map work planned into 2.1/2.2 that hasn't started or been re-sprinted into 2.3. Decision needed: re-sprint, de-scope, or accept as backlog.
- **8 credential tasks (1444864)** are the priority — **6 are Active** (work genuinely in progress) yet stuck in 2.2 while the parent story shows Validation. Confirm true state; this work gates discovery for P1/P3 (and Service Mapping via 1445244).

---

## Status Summary

| Objective | ADO Obj | Stories Confirmed | Stories Blocked / At Risk | Stories Missing ADO IDs |
|-----------|---------|-------------------|--------------------------|------------------------|
| P0 — Airlift | 1420079 | 4 | 0 | 0 |
| P1 — Discovery / SCCM | 1366657 | 6 | 0 (1403762 & 1403759 advanced per 6/11 board) | ~6 (CI auto-population, custom fields) |
| P2 — Data Certification | 1420082 | 2 | 0 | Many (features light on stories) |
| P3 — Service Mapping | 1366660 | 6 | 0 | 0 (Wave 20 & 21 empty) |
| P4 — Governance/NERC/Qualys | 1366662 | 3 (Qualys only) | 2 (1428703 & 1428704 BLOCKED — Qualys vendor approval, Issue 1465952) | CCB and NERC-CIP have no stories yet |
| P5 — NowAssist | 1408764 | 4 + 1 spike | 0 (reassigned to Kiran; on track for 2.3) | Feature 1436574 confirmed |
| OCM (unmapped) | — | 0 | — | Feature 1428659 Active; no objective home yet |

> ⚠️ **No stories confirmed Done as of 6/12 12pm.** The 6/11 board's two "Done" items are unreliable: 1407572 shows Validation at 12pm; 1413033 is absent from the 12pm pull (unconfirmed). Do not report completed-story counts until reconfirmed.

**Legend:** 🟢 Active / Ready &nbsp; 🟡 At Risk &nbsp; 🔴 Blocked &nbsp; 🔵 Defining &nbsp; ⏸️ On Hold &nbsp; ⚪ New / Done &nbsp; ⚠️ Gap / Needs Action

---

## ADO Snapshot Notes

### 6/17 story pull — Iteration 2.3 grid (supersedes 6/12 12:00pm on conflicts)
- **NowAssist progress (Feature 1436574):** 1436576 → **Closed** (was Active); 1436579 → **Resolved** (was Ready DoR); 1436592 → **Active** (was Ready DoR); 1436593 unchanged (Ready DoR).
- **Type fix:** 1403759 reclassified **Spike → User Story**, title aligned to "SCCM:Servers Remove SCCM Attributes" (was tracked as spike "De-Prioritize SCCM Attributes").
- **New stories:** **1459721** (Testing new SNMP creds / MID dns params, Stan, Validation) — filed under 1356646 credential family, parent unconfirmed. **1399787** (Business Application: Add All CI-Owners to CMDB Full Access Group, Vinay, Validation) — ⚠️ **no feature home in our doc; needs mapping** (access/permissions governance).
- **Orphan update:** 1472365 now assigned **Harsh Deshmane** (was unassigned); still no parent.
- **Confirmed matches:** SCCM 1403760/62/63 Validation; 1444864 Validation; 1454371 Active; 1455858 Active; 1407572 Validation; 1387236 Validation; 1435307 Validation; Qualys 1428703/1428704 Active (still BLOCKED per Stream C flag).
- ⚠️ **Absent from this 2.3 story grid:** Airlift stories **1418610 / 1418618 / 1418621** and **1416384** — our doc lists them in 2.3. Confirm whether filtered, re-sprinted, or our iteration tag is stale.

### 6/12 12:00pm story pull (supersedes 6/11 board on conflicts)
- **Qualys 1428703 & 1428704** → Active **+ Blocked** (vendor approval; ties to Issue 1465952). Was Validation on 6/11 board.
- **SCCM 1403759/1403760/1403762/1403763** → all Validation (advanced past Active), 1 pt each.
- **1407572** → Validation, NOT Done (6/11 board was wrong). **1413033** absent from this pull — its "Done" is unconfirmed. ⇒ no confirmed Done stories.
- **1436576** → Active confirmed (variance closed).
- **1444864** Validation 5pts; **1454371** Active 2pts; **1387236** Validation (gives Feature 1411480 its first child); **1411237** Defining (parent confirmed = 1355890).
- **Parent corrections:** 1455858 → "Computer Class Data Reconciliation" (not 1354794); Qualys stories → "Integration Qualys & ServiceNow (CMDB Data Read Only)"; 1435307 → P2 Feature 1247179 (was misfiled P1).
- **New orphan story:** **1472365** — "Update server values post validation of data" (Ready DoR, **no parent**) — assignee now **Harsh Deshmane** (per 6/17 story pull; was unassigned). Still needs parent feature.

**Unparented tasks (no clear story link in ADO):**
- 1460404 — CMDB:Stakeholder Confirmation (New, Data Ingestion)
- 1472364 — "Please classify as Physical or Virtual." (New, Tony De Araujo, Governance)

### 6/11 11:30am board snapshot

**Reconciliations applied this snapshot:**
- Feature **1354797** was duplicated in this doc (Server Class *and* Operational Monitoring). Operational Monitoring's true Feature ID is **1355888** (per validation worksheet) — corrected.
- Spike **1421790** (Gap Analysis Servers): ADO parent is Feature 1354797 (Server Class), not 1383523 where this doc lists it — left in place, flagged inline.
- Spike **1402555**: points 2 → 3. Spikes **1234585 / 1403733**: Active/Approved → Ready (DoR) per ADO.
- **State alignment to 6/11 board (board wins):** Airlift 1418610/18/21 Active → Validation; SCCM 1403763/1403760 → Active, 1403762 Blocked → Active, 1403759 On Hold → Validation; 1421790 → Active; 1355167 → Validation; 1413033 → Done/Closed; Qualys 1428703/1428704 → Validation; 1403725 → Ready; 1339116 / 1470837 → Ready DoR.

**Open follow-ups:**
- Reconcile NowAssist phase numbering: ADO (Foundation=Phase 1, Dup CI Elim=Phase 2) vs. [[nowassist-implementation-plan]] (Dup CI Elim=Phase 1 of 5). Which scheme for leadership reporting?
- Triage orphan story **1472365** — assign owner + parent feature.
- Confirm parent feature for **1455858** ("Computer Class Data Reconciliation" vs. 1354794) and reconcile the two computer-class feature names.
- Reconfirm whether **1413033** is actually Done (absent from 6/12 pull).
- ~~NowAssist 1436576 state~~ ✅ confirmed Active 6/12. ~~Qualys 1465952 gating~~ ✅ confirmed — both Qualys stories Blocked.
