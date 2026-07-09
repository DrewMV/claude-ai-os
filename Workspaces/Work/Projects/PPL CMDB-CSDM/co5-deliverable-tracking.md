---
type: contract-tracker
workspace: Work
project: PPL CMDB-CSDM
contract: CO5 (Change Order #5)
updated: 2026-06-30
tags: [work, cmdb-csdm, contract, deliverables, traceability]
---

# CO5 Deliverable → Story Traceability Matrix

Validates every **Change Order #5** contractual deliverable against PI-2 ADO features/stories.

- **Source contract:** [[Contract/CO5-signed-2026-05-26.pdf]] — signed 2026-05-26 (Caitriona Sharkey / Accenture; Jacquelyn English / PPL). PO# 1000002225.
- **Story source:** [[PI-2/pi2-objectives-features-stories]] — ADO snapshot **6/30 (Iter 2.4 grid)** for 2.4 items (see [§ 2.4 Acceptance Mapping](#24-acceptance-mapping-630-ado-grid--authoritative-for-24-item-states) below); 6/19 grid for everything else.
- **Alias note:** logged as **"CR5"** in [[Memory]] Contract table; the signed document is **Change Order #5 (CO5)**. Same instrument.
- **Successor:** [[co6-deliverable-tracking]] (CO6, **DRAFT/unsigned**) re-baselines 5 of 6 gaps below to Jul 31 → Oct 30 — **if executed before July 1**. See the gap-closure map there.

> ⚠️ **THE GOVERNING CONSTRAINT — read first.**
> All three CO5 deliverables are **due June 30, 2026**. CO5 term = Mar 31 → **Jun 30, 2026**.
> **PI-2 runs to Aug 4, 2026** — five weeks *past* the contractual deadline.
> **$533,775 of June fees are held back until final acceptance of these deliverables.**
> ⇒ A story existing in ADO is **not** sufficient. It must be **delivered & accepted by 6/30**.
> Stories in **Iter 2.4 (Jun 24–Jul 7), 2.5 (Jul 8–21), 2.6/IP (Jul 22–Aug 4)** are **post-deadline** ⛔.
> Code freezes compress this further: **Dev freeze Jul 4–18**, **Test freeze Jul 18–Aug 15**.
> Today: **2026-06-30 → deadline today.** Per the 6/29 CO5 Alignment email, most acceptance dates now fall *after* 6/30 (Data Dictionary CCB approval **7/21**) — the holdback risk stands unless CO6 signs before **7/1**.

**Verdict legend:** ✅ Covered & on track · 🟡 Partial / gaps · 🔴 Gap, blocked, or post-deadline risk · ⚪ Needs confirmation

---

## Coverage Scorecard

| CO5 Deliverable | Sub-items | Covered | Partial | Gap/Risk | Headline risk |
|-----------------|-----------|---------|---------|----------|---------------|
| **1. Governance** | 5 | 2 | 3 | 0 | 🔄 6/29: G1 (Databases) & G5 (CCB) now have acceptance stories — gaps closed at artifact level; 1406668-Removed still to resolve |
| **2. Automated Data Ingestion** | 3 | 1 | 2 | 0 | 🔄 6/30: Computer/Server/DB **audit-dashboard spikes** + inventory/retirement cluster now in 2.4 (G2/G3 progressing); no formal 90%-measurement acceptance story yet |
| **3. Other Enhancement** | 1 | 0 | 1 | 0 | 🔄 6/29: Qualys 1428703 (Part 1) now Active in 2.4 (was Blocked); confirm Part 2 |

> **No CO5-relevant story is confirmed Done as of the 6/19 grid.** Closest to acceptance: Data Cert dashboard (1402727, UAT signed off, PROD deploy 6/23).

---

## 🔴 Hard Gaps — Tracked

> **Definition:** a *hard gap* = a CO5 acceptance item with **no story at all**, or **fully blocked**. These threaten the 6/30 holdback most directly. Review every status sync.

| ID | CO5 item | Gap | Owner | CO6 disposition (draft) | Status |
|----|----------|-----|-------|--------------------------|--------|
| **G1** | D1.1 Database data dictionary | ~~No Database CI-class data-dictionary story exists~~ → **Story 1480098** (Data Dictionary: Databases) **🟣 Validation** per 6/30 grid (Kiran) + CMP Stage 1 DB dictionary drafted | Manuel → Joe/Sonika | ✅ CO6 "CMDB Governance" includes **Databases** → **Jul 31** *(if signed)* | 🟢 **CLOSED at artifact level (6/30)** — story in Validation + CMP draft exist; acceptance pending CCB |
| **G2** | D2.1 Computers 90% coverage | ~~No coverage-measurement/validation story~~ → 2.4 has **1480114** Computer audit-dashboard spike (Ready DoR) + inventory/retirement cluster; still **no formal 90%-measurement acceptance story** | Manuel → Joe | ✅ CO6 "CI Coverage – Computers" → **Sep 30** | 🟡 **PROGRESSING (6/30)** — validation spike in 2.4; acceptance story still gap |
| **G3** | D2.2 Servers 90% non-NERC-CIP coverage | ~~No coverage-measurement/validation story~~ → 2.4 has **1480112** Server audit-dashboard spike (Ready DoR) + **1454371** Extract servers w/o support groups (Active) + inventory cluster; still **no formal 90%-measurement acceptance story** | Manuel → Joe | ✅ CO6 "CI Coverage – Servers" → **Oct 30** | 🟡 **PROGRESSING (6/30)** — validation/cleanup in 2.4; acceptance story still gap |
| **G4** | D3 Qualys integration | **1428703 (Part 1) Active in Iter 2.4**, no longer Blocked (confirmed 6/30); 1465952 Closed. **1428704 (Part 2) status unconfirmed** | Manuel → Rich/Stan | ✅ CO6 "Qualys Integration" full PROD → **Oct 27** | 🟡 **IN PROGRESS (6/30)** — Part 1 unblocked; confirm Part 2 + vendor plugin landed |
| **G5** | D1.5 Monthly CCB | Acceptance **story 1480107** under clean parent feature 1480087 — **🟢 Ready DoR (2.4)** per 6/30 (Manuel). **Underlying 1406668-Removed contradiction** for the CCB meeting stories (1406672/683/687) still open | Manuel → Joe | ❌ **Not carried in CO6** — CO5-only obligation | 🟡 **PARTIAL (6/30)** — acceptance story exists; 1406668 Removed still to resolve |

> **Soft gaps (story exists but thin / unowned):** D1.2 KB Articles owner; D1.3 ESS-02 (single spike, parent Removed); D2.3 DB enhanced Discovery (cred tasks only, no demonstrable story). Track in the action list, not here.

**Gap status key:** 🔴 OPEN · 🟡 IN PROGRESS · 🟢 CLOSED (story created / unblocked) · ⚪ ACCEPTED-AS-RISK (formally deferred to CO6)

---

## 2.4 Acceptance Mapping (6/30 ADO grid) — authoritative for 2.4 item states

> 🔄 **6/30 reconciliation.** Per the **CO5 Deliverable Alignment** email (Manuel → Joe/Stan/Tony, 6/29) the team **deprioritized Service Mapping / Airlift / NowAssist / Network Discovery** to focus on CO5. The Iter-2.4 board is the CO5 work slice — **38 items · 61 pts (45 pts CO5-aligned across 30 items)**. Per-deliverable acceptance/validation stories now hang off **Feature 1480087 — Governance Validation & Acceptance** (Manuel). **These 2.4 states supersede the 6/19-grid states in the Master/Acceptance tables below.** Full mapping + non-CO5 buckets + CO5 acceptance timeline: [[PI-2/pi2-iteration-activity]] (Iteration 2.4).

**Deliverable 1 — Governance** *(acceptance stories = Feature 1480087)*

| # | Deliverable | Acceptance story (6/30 state) | Pts | Gap |
|---|---|---|---|---|
| 1.1a | Data Dictionary — Servers | 1480088 (Vinay · 🟣 Validation) | 2 | |
| 1.1b | Data Dictionary — Computers | 1480090 (Bhushan · 🟣 Validation) | 2 | |
| 1.1c | Data Dictionary — Business Apps | 1480097 (Kiran · 🟣 Validation) + data-pop 1475582 (🔵 Active), 1478286 (🟢 Ready DoR), 1480111 BA audit spike (Joe · 🟢 Ready DoR) | 10 | |
| 1.1d | Data Dictionary — Databases | 1480098 (Kiran · 🟣 Validation) | 2 | ✅ closes **G1** |
| 1.2 | Data Certification | 1480099 (Joe · 🟢 Ready DoR) + 1402727 (PROD-deployed) | 2 | |
| 1.3 | ESS-02 Alignment | 1480102 (Manuel · 🟢 Ready DoR) | 1 | |
| 1.4 | SOX BA review | 1480105 (Uloma · 🟢 Ready DoR) | 2 | |
| 1.5 | Monthly CCB | 1480107 (Manuel · 🟢 Ready DoR) | 1 | ✅ closes **G5** |

**Deliverable 2 — Automated Data Ingestion**

| # | Deliverable | 2.4 story (6/30 state) | Pts | Gap |
|---|---|---|---|---|
| 2.1a | Computers — SCCM/Discovery | — reported complete (email) | 0 | |
| 2.1b | Computers — 90% Coverage | 1480114 Computer audit spike (Anthony · 🟢 Ready DoR) | 2 | 🟡 **G2** progressing |
| 2.1c | Computers — Build Lifecycle | — no 2.4 story (validation TBD) | 0 | |
| 2.2a | Server — SCCM/Discovery | — reported complete (email) | 0 | |
| 2.2b | Server — 90% Coverage / cleanup | 1480112 Server audit spike (Anthony · 🟢 Ready DoR); 1454371 (Bhushan · 🔵 Active); 1455832 (Vinay · 🟢 Ready DoR); inventory+retirement 1487863–1487897 (13) ⚠️ | 18 | 🟡 **G3** progressing |
| 2.2c | Server — SOX Indicators | — reported complete (email) | 0 | |
| 2.x | Credentials enabling Discovery | — reported complete (email); ⚠️ prior 1444864 child tasks were Active in 2.2 | 0 | |
| 2.3a | Database — SQL/Oracle Discovery | — reported complete (email) | 0 | |
| 2.3b | Database — SOX Indicators | — reported complete (email) | 0 | |
| 2.3c | Database — 90% Coverage | 1480113 Database audit spike (Stan · 🔵 Active) | 2 | |

**Deliverable 3 — Other Enhancement**

| # | Deliverable | 2.4 story (6/30 state) | Pts | Gap |
|---|---|---|---|---|
| 3 | Evaluate Qualys Integration | 1428703 Install plugin Part 1 (Stan · 🔵 Active) | 1 | 🟡 **G4** Part 1 unblocked; Part 2 (1428704) unconfirmed |

**CO5-aligned 2.4 total: 45 pts (30 items).** Non-CO5 in 2.4: upgrade-readiness 11 pts, network 3 pts (deprioritized), NowAssist 2 pts (Closed).

> ⚠️ **Inventory + bulk-retirement cluster (1487863–1487897, 13 pts)** booked under Server 90% (2.2b) but is VMware/Physical PA/KY — may split with Computer 90% (2.1b). No feature parent in ADO; confirm home.
> ⚠️ **8 deliverables have no 2.4 acceptance story** (SCCM-Discovery ×3, SOX Indicators ×2, Credentials, Computers Build Lifecycle) — reported complete per email but lack a validation/acceptance artifact for CCB sign-off.

---

## Master Deliverable Table

> Every CO5 deliverable → associated ADO feature/story → status (**6/19 grid** — for 2.4 items, the **§ 2.4 Acceptance Mapping** above is authoritative). Hard gaps flagged **[G#]**.

| CO5 Deliverable | Sub-item | ADO Feature / Story (ID — title) | Status |
|---|---|---|---|
| **1. Governance** | 1.1 Data Dictionary — **Servers** | Feature **1354797** Server Class Data & Form Updates | 🟢 Ready (Iter 2.3) |
| | | Spike **1421790** Gap Analysis for Servers (Linux & Windows) | 🟣 Validation |
| | | Story **1454371** Extract Servers Without Support Groups | 🟢 Active |
| | 1.1 Data Dictionary — **Computers** | Feature **1354794** Computer Class Data & Form Improvements | 🟢 In progress |
| | | Story **1313400** Add Asset Tags to Computer Class CIs | 🟢 Resolved |
| | | Story **1399547** Identify Shared Devices | 🟣 Validation |
| | | Story **1455858** Virtual Location Management | 🟢 Active |
| | 1.1 Data Dictionary — **Business Apps** | Story **1475584** Populate Missing Technical Owner Group *(Manuel)* | ⚪ New |
| | | Story **1475585** Populate Missing Approval Groups *(Manuel)* | ⚪ New |
| | | Story **1475582** Populate Missing Support Groups | 🟢 Refinement Ready (2.4) |
| | | Story **1478286** Populate Classification field values | 🟢 Refinement Ready (2.4) |
| | | Story **1474892** Analyze Value Stream population for Business App | ⚪ New |
| | 1.1 Data Dictionary — **Databases** **[G1]** | ⚠️ **No dedicated Database-class data-dictionary story found** | 🔴 **HARD GAP** |
| | 1.2 Data Certification | Feature **1247179** / Story **1435307** Data Cert Pilot Changes | 🟣 Validation |
| | | Feature **1402979** / Story **1402727** Update Data Cert Dashboard | 🟢 **UAT signed off (6/10); PROD 6/23** |
| | | Feature **1402958** stories: **1402962** kick-off, **1402976** execute policies, **1402980** monitor, **1402984** office hours, **1402985** feedback | 🔵 Defining / ⚪ New |
| | | Story **1402959** Identify Pilot group of Business Apps | ⚪ Closed |
| | | Feature **1371672** Governance Model for New Business App Requests | 🟢 (feature-level) |
| | | KB Articles / User Documentation | ⚠️ No story — owner TBD |
| | 1.3 ESS-02 Alignment | Spike **1420244** ESS-02 Policy and CMDB Alignment *(Joe)* | 🟢 Active *(parent 1406668 Removed)* |
| | 1.4 SOX Business App review *(SOX only, not NERC/CIP)* | Issue **1438967** PMDB App Service SOX & DR Customization Governance | ⚪ Closed (approved) |
| | | Story **1455827** Notification for SOX Team on Ownership Changes | 🟢 Refinement Ready (**2.5 — post-deadline**) |
| | | Story **1399787** Add all CI-Owners to CMDB Full Access Group | 🟣 Validation *(no feature home)* |
| | 1.5 Monthly CCB Meetings + future-PI backlog **[G5]** | Feature **1406668** CMDB Governance & Monthly CCB Meetings | 🔴 **Removed in ADO** |
| | | Stories **1406672** May / **1406683** June / **1406687** July CCB *(Joe)* | ⚪ New *(under Removed feature)* |
| | | Spike **1339116** Monitor/Update CI Owners Who Left PPL | 🟢 Refinement Ready |
| **2. Automated Data Ingestion** | 2.1 Computers — SCCM/Discovery precedence | Stories **1348712 / 1348716 / 1348717** SCCM Computer precedence | 🟢 Resolved |
| | | Story **1348715** SCCM Computers — Last Time Seen alignment | 🟣 Validation |
| | 2.1 Computers — bulk Life Cycle | Story **1402790** Update Lifecycle Status for Retired Computers | ⚪ Closed |
| | 2.1 Computers — 90% coverage **[G2]** | ⚠️ No coverage-measurement story | 🔴 **HARD GAP** |
| | 2.2 Servers — SCCM/Discovery precedence | Feature **1356826** / Stories **1403763 / 1403760 / 1403762 / 1403759** | 🟣 Validation (all, approval gate cleared) |
| | 2.2 Servers — credentials enabling discovery | Story **1444864** Fix Credentials Servers/DB/Network; Story **1459721** SNMP/MID test | 🟣 Validation *(6 child tasks still Active)* |
| | 2.2 Servers — 90% non-NERC-CIP coverage **[G3]** | ⚠️ No coverage-measurement story | 🔴 **HARD GAP** |
| | 2.2 Servers — SOX indicators | *Manual — excluded from automation per CO5* | n/a |
| | 2.3 Databases — enhanced Discovery (MS-SQL/Oracle) | Credential work under **1444864** (GWIZ Oracle cred, PA Oracle DB discovery test) | 🟡 In progress (task level) |
| | 2.3 Databases — SOX indicators | *Manual — excluded per CO5* | n/a |
| **3. Other Enhancement** | 3 Evaluate 1 integration (Tanium **or** Qualys) → team chose **Qualys** **[G4]** | Story **1428703** Install Qualys plugin (Part 1) | 🔴 **Active — BLOCKED** |
| | | Story **1428704** Configure Qualys integration (Part 2) | 🔴 **Active — BLOCKED** |
| | | Spike **1234585** Define Data Scope / Import Views | 🟢 Ready (DoR) *(no ADO parent)* |
| | | Issue **1465952** Qualys Plugin Replacement (vendor approval) | ⚪ Closed *(may unblock — confirm)* |
| | | Dependency **1383519** Qualys Dev/Support Team *(Rich Santillo)* | 🟢 Active |

**Legend:** 🟢 Active/Ready/Resolved · 🟣 Validation · 🔵 Defining · ⚪ New/Closed · 🔴 Blocked/Gap · ⚠️ needs action

---

## Acceptance Tracking

> 🔗 **Acceptance vehicle:** the per-deliverable validation/acceptance stories are drafted in [[Backlog/co5-governance-validation-stories]] (Governance / Deliverable 1) under the parent feature *"[Enabler · Compliance] CO5 Governance Validation & Acceptance"* — **reference drafts, not yet in ADO**. As those are created, reconcile their ADO IDs back here.
> The **one story/artifact that constitutes acceptance evidence** for each CO5 deliverable, its acceptance status, and **what CO6 (draft) does to the deliverable**.
> **Acceptance status:** ⛔ No acceptance story (gap) · ⚪ Not started · 🟡 In progress · 🟣 In Validation · 🟢 UAT/Deploying · ✅ Accepted · 🔴 Blocked
> **CO6 effect:** 🔁 re-baselined (later date) · ➕ scope expanded · ⬆️ escalated · ⛔ not carried

| CO5 Deliverable | Acceptance story / evidence | Acceptance status | CO6 effect on deliverable |
|---|---|---|---|
| **1.1 Data Dictionary — Servers** | **1421790** Gap Analysis Servers + Feature **1354797** | 🟣 In Validation | 🔁 → **Jul 31** (CMDB Governance) |
| **1.1 Data Dictionary — Computers** | **1348715/1313400/1399547** + Feature **1354794** | 🟡 In progress (some Resolved) | 🔁 → **Jul 31** |
| **1.1 Data Dictionary — Business Apps** | **1475582 / 1478286** (Refinement Ready); 1475584/85 (New) | ⚪ Not started | 🔁 → **Jul 31** |
| **1.1 Data Dictionary — Databases [G1]** | *(none)* | ⛔ **No acceptance story** | 🔁 ➕ CO6 adds **Databases** explicitly → **Jul 31** |
| **1.2 Data Certification** | **1402727** Update Data Cert Dashboard | 🟢 **UAT signed (6/10); PROD 6/23; Todd validates 6/24–25** | ➕ pilot expanded to **ALL CI classes** → **Jul 31** |
| **1.3 ESS-02 Alignment** | **1420244** ESS-02 Policy & CMDB Alignment (spike) | 🟡 In progress (analysis only) | 🔁 → **Jul 31** |
| **1.4 SOX BA Review** | **1438967** (Closed/approved) + **1455827** Notification to SOX Team | 🟡 Partial — 1455827 in **2.5 (post-6/30)** | 🔁 → **Jul 31** |
| **1.5 Monthly CCB [G5]** | **1406672/683/687** CCB Meetings — under **Removed** feature 1406668 | 🔴 Cadence happening (CCB 6/16) but **evidence filed under dead feature** | ⛔ **Not carried in CO6** — CO5-only |
| **2.1 Computers — precedence** | **1348712/716/717** (Resolved) + **1348715** (Validation) | 🟢 Mostly accepted-ready | 🔁 → **Jul 31** (CI Coverage – Computers) |
| **2.1 Computers — bulk Life Cycle** | **1402790** Lifecycle for Retired Computers | ⚪ Closed | 🔁 → **Jul 31** (Asset Mgmt defines process) |
| **2.1 Computers — 90% coverage [G2]** | *(none)* | ⛔ **No acceptance story** | 🔁 CO6 coverage validation → **Sep 30** |
| **2.2 Servers — precedence** | **1403759/760/762/763** SCCM Server precedence | 🟣 In Validation (gate cleared) | 🔁 → **Jul 31** (CI Coverage – Servers) |
| **2.2 Servers — credentials** | **1444864** Fix Credentials (Servers/DB/Network) | 🟣 Validation ⚠️ **6 child tasks still Active** | 🔁 → **Jul 31** |
| **2.2 Servers — 90% coverage [G3]** | *(none)* | ⛔ **No acceptance story** | 🔁 CO6 coverage validation → **Oct 30** |
| **2.3 Databases — enhanced Discovery** | Credential tasks under **1444864** (Oracle creds) | 🟡 In progress (task-level only) | 🔁 carried → **Jul 31** |
| **3 Qualys Integration [G4]** | **1428703 / 1428704** | 🔴 **BLOCKED** (vendor approval; 1465952 now Closed — confirm) | ⬆️ escalated **evaluate → full PROD** → **Oct 27** |

> **Reading it:** Only **1402727** (Data Cert dashboard) is genuinely near *acceptance* (deploying 6/23). Everything else is Validation-or-earlier, blocked, or has no acceptance story. **CO6 re-baselines all but G5** to Jul 31 → Oct 30 — *contingent on signature before July 1.*

---

## Deliverable 1 — Governance  ·  Due 2026-06-30

### 1.1 Data Dictionary / Class Attribute definitions
*(Servers Win/Linux · Computers Physical/Virtual · Business Applications · Databases)*  — Verdict: 🟡 **Partial**

| Class | ADO Feature / Stories | Status | 6/30? |
|-------|----------------------|--------|-------|
| Servers (Win/Linux) | Feature **1354797** Server Class Data & Form Updates; Spike **1421790** Gap Analysis Servers (Validation); **1454371** Extract Servers w/o Support Groups (Active) | 🟢 In progress | At risk — Iter 2.3 |
| Computers (Phys/Virtual) | Feature **1354794** Computer Class Data & Form Improvements; **1313400** Add Asset Tags (Resolved); **1399547** Identify Shared Devices (Validation); **1455858** Virtual Location Mgmt (Active) | 🟢 In progress | Partly on track |
| Business Applications | BA data-population cluster: **1475584/1475585** (Manuel), **1475582**, **1478286**, **1474892**; Feature **1371672** | ⚪ Mostly New/Refinement | 🔴 Most in 2.4 (post-deadline) |
| **Databases** | ⚠️ **No dedicated Database-class data-dictionary story found.** DB work appears only as *discovery* (D2.3) + credentials. | 🔴 **GAP** | 🔴 Unstaffed for 6/30 |

> **Action:** Confirm whether a Database CI-class attribute/data-dictionary deliverable exists in ADO. If not, this is the clearest contractual gap in Deliverable 1.

### 1.2 Data Certification  — Verdict: ✅ **Covered (strongest area)**
*(Process Definition · Intake for New · E2E flow · Pilot Release for Business App CI Class · KB/User docs)*

| CO5 piece | ADO | Status | 6/30? |
|-----------|-----|--------|-------|
| Pilot functionality | **1247179** / Story **1435307** Data Cert Pilot Changes | 🟣 Validation | ✅ likely |
| Dashboard / monitoring | **1402979** / Story **1402727** Update Data Cert Dashboard | 🟢 **UAT signed off (Sonika 6/10); PROD deploy 6/23** | ✅ **on track** |
| Pilot implementation | **1402958** stories: 1402962 (kick-off), 1402976 (execute policies), 1402980 (monitor), 1402984 (office hours), 1402985 (feedback) | 🔵 Defining/New | 🟡 several need iteration assignment |
| Pilot group identified | **1402959** | ⚪ Closed | ✅ done |
| Governance model (new BA requests) | Feature **1371672** | — | — |

> **Pilot Release for the Business Application CI Class** (the named CO5 acceptance item) is the deployment landing **6/23 → Todd validates 6/24–25** — i.e. acceptance evidence available *just before* the 6/30 deadline. **This is the single most important date for the holdback.**
> **Risk to watch:** Issue **1416676** (EA Bus App data readiness vs Data Cert) — Closed, but BA data readiness underpins the pilot.
> **Action:** Confirm KB Articles / User Documentation sub-item has an owner — not clearly storied.

### 1.3 ESS-02 Alignment with Cyber Security & Compliance  — Verdict: 🟡 **Partial**

| ADO | Status | 6/30? |
|-----|--------|-------|
| Spike **1420244** ESS-02 Policy and CMDB Alignment (Joe Dames) | 🟢 Active | ⚠️ Parent feature **1406668 is Removed** in ADO |

> ESS-02 is a single Active **spike**, not implementation stories. Open actions: *engage Jason Dubreuil (ESS-02 consulting member), document CMP.* **Action:** confirm whether alignment = analysis only (spike sufficient) or requires deliverable artifacts by 6/30.

### 1.4 Support review of SOX Business Applications  — Verdict: 🟡 **Partial**
*(Ensure SOX BAs identified in CMDB + update-rights controls. CO5 scope: **SOX only — explicitly NOT NERC/CIP**.)*

| ADO | Status |
|-----|--------|
| Issue **1438967** PMDB Application Service SOX & DR Customization governance | ⚪ Closed (approved 6/08; edit rights restricted to Cyber Risk & DR) |
| Story **1455827** Notification for SOX Team on Ownership Changes to CI | 🟢 Refinement Ready — **Iter 2.5** 🔴 (post-deadline) + open Joe decision "PI-2 or PI-3?" |
| Story **1399787** Add all CI-Owners to CMDB Full Access Group | 🟣 Validation — ⚠️ no feature home |

> **Contractual boundary to honor:** CO5 says this applies to **SOX data, not NERC/CIP**. NERC-CIP work (Stream B, feature 1370224) is *separate* and not part of this acceptance item. **Action:** get Joe's PI-2-vs-PI-3 ruling on 1455827 — if it slips to 2.5 it's after 6/30.

### 1.5 Facilitate Monthly CCB Meetings + backlog for future PIs  — Verdict: 🔴 **At Risk (data-integrity contradiction)**

| ADO | Status |
|-----|--------|
| Feature **1406668** CMDB Governance & Monthly CCB Meetings | 🔴 **Removed in ADO** — but has 3 live child stories |
| **1406672** May CCB / **1406683** June CCB / **1406687** July CCB (Joe Dames) | ⚪ New (live under a Removed feature) |
| Spike **1339116** Monitor/Update CI Owners who left PPL | 🟢 Refinement Ready |

> The actual CCB cadence **is** happening (CCB meeting held 6/16; Audit Sync 6/18; Manuel attending). But the **feature that proves it contractually is marked Removed** — a feature-vs-story contradiction that would undermine acceptance evidence.
> **Action (high priority):** un-Remove 1406668 **or** re-parent the CCB stories to a live feature, so the monthly-CCB deliverable is demonstrable. Also confirm the "backlog for future PIs" artifact exists.

---

## Deliverable 2 — Automated Data Ingestion  ·  Due 2026-06-30

### 2.1 Computers  — Verdict: 🟡 **Partial**
*(SCCM/Discovery precedence reconciliation · 90% devices managed · bulk Life Cycle Stage/Status updates)*

| CO5 piece | ADO | Status | 6/30? |
|-----------|-----|--------|-------|
| SCCM/Discovery precedence | SCCM **Computer** Class precedence: **1348712/1348716/1348717** (Resolved), **1348715** (Validation) | 🟢 Mostly Resolved | ✅ likely |
| Bulk Life Cycle Stage/Status | **1402790** Update Lifecycle Status for Retired Computers (Closed) | ⚪ Closed | ✅ |
| 90% coverage validation | ⚠️ No explicit "coverage validation / 90%" measurement story found | 🔴 measurement gap | — |

> **CO5-documented risk (verbatim):** *"no current reliable source to compare with for physical devices; only on-network devices discovered."* Plus **CO5 dependency:** Life Cycle process must be **defined by the Asset Management team** (external to this team). **Action:** confirm where the 90% coverage metric is measured/reported.

### 2.2 Servers  — Verdict: 🟡 **Partial**
*(SOX indicators **manual** — out of scope · SCCM/Discovery precedence · 90% non-NERC-CIP discovery)*

| CO5 piece | ADO | Status | 6/30? |
|-----------|-----|--------|-------|
| SCCM/Discovery precedence | Feature **1356826** SCCM Server Class Precedence: **1403763/1403760/1403762/1403759** (all Validation, 1pt each) | 🟣 Validation — Sonika approval gate cleared | ✅ likely |
| Credentials enabling discovery | **1444864** Fix Credentials Servers/DB/Network (Validation) + child tasks; **1459721** SNMP/MID test | 🟡 6 active child tasks stuck in 2.2 | ⚠️ gates discovery |
| 90% non-NERC-CIP coverage | ⚠️ no explicit coverage-measurement story | 🔴 measurement gap | — |
| SOX indicators | **Manual** per CO5 — *intentionally excluded from automation* | n/a | n/a |

> ⚠️ **Precedence-baseline risk (Risk #12):** SCCM-vs-Discovery authoritative precedence not fully mapped field-by-field; stories making isolated decisions — rework risk before acceptance.

### 2.3 Databases  — Verdict: 🟡 **Partial**
*(Enhanced Discovery for MS-SQL & Oracle · SOX indicators **manual** — out of scope)*

| CO5 piece | ADO | Status |
|-----------|-----|--------|
| MS-SQL / Oracle enhanced Discovery | Credential work **1444864** (GWIZ_MON_ORACLE_DB cred, PA Oracle DB discovery test); Discovery now surfacing Oracle DBs/listeners (6/9) | 🟡 In progress at task level |
| SOX indicators | **Manual** per CO5 — excluded | n/a |

> **CO5-documented risk (verbatim):** *"no scalable solution for the distribution of credentials to target CIs."* This is your active credential/SolarWinds workstream. **Action:** confirm a discrete "enhanced DB Discovery (MS-SQL/Oracle)" story exists, or whether it lives only as credential tasks — acceptance needs a demonstrable deliverable.

---

## Deliverable 3 — Other Enhancement  ·  Due 2026-06-30

### 3 Evaluate 1 Integration (Tanium **or** Qualys)  — Verdict: 🔴 **At Risk (BLOCKED)**
*(Gather & document CMDB-specific requirements for one integration)*

| ADO | Status | 6/30? |
|-----|--------|-------|
| Team chose **Qualys** (Stream C). Parent: "Integration Qualys & ServiceNow (CMDB Data Read Only) (PI2)" | — | — |
| Story **1428703** Install Qualys plugin (Part 1) | 🔴 **Active — BLOCKED** | ⛔ |
| Story **1428704** Configure Qualys integration (Part 2) | 🔴 **Active — BLOCKED** | ⛔ |
| Spike **1234585** Define data scope / import views | 🟢 Ready (DoR) — ⚠️ no ADO parent | — |
| Issue **1465952** Qualys Plugin Replacement (vendor approval) | ⚪ **Closed per 6/19 grid** — **may unblock** 1428703/04, NOT auto-flipped | ⚠️ confirm |
| Dependency **1383519** Qualys Dev/Support Team (Rich Santillo) | 🟢 Active | — |

> CO5 only requires **evaluate + document requirements for ONE** integration — a *lighter* bar than full implementation. But both Qualys stories are flagged **Blocked** on vendor plugin approval. Issue 1465952 now shows **Closed**, which *may* release them — **not confirmed**.
> **Action (high priority):** confirm with **Rich Santillo / Stan** that vendor approval landed and flip 1428703/1428704. If Qualys can't clear, **Tanium is the contractual alternative** — but no Tanium stories exist, so a pivot this late is unrealistic for 6/30.

---

## Consolidated Action List (for 6/30 acceptance)

| # | Action | Owner | Priority | Ties to |
|---|--------|-------|----------|---------|
| 1 | Confirm vendor approval landed → flip Qualys **1428703/1428704** (or accept Deliverable 3 at risk) | Manuel → Rich/Stan | 🔴 | D3 |
| 2 | Resolve CCB feature **1406668 Removed** vs 3 live CCB stories — un-Remove or re-parent | Manuel → Joe | 🔴 | D1.5 |
| 3 | Confirm/create **Database CI-class data-dictionary** deliverable | Manuel → Joe/Sonika | 🔴 | D1.1 |
| 4 | Get Joe's ruling on SOX story **1455827** (PI-2 vs PI-3; currently 2.5 = post-deadline) | Manuel → Joe | 🔴 | D1.4 |
| 5 | Protect Data Cert pilot deployment chain (PROD 6/23 → Todd validates 6/24–25) — **holdback-critical** | Manuel | 🔴 | D1.2 |
| 6 | Confirm where 90% coverage (computers + non-NERC-CIP servers) is **measured/reported** | Manuel → Joe | 🟡 | D2.1 / D2.2 |
| 7 | Confirm enhanced **DB Discovery (MS-SQL/Oracle)** has a demonstrable story, not just cred tasks | Manuel → Stan/Tony | 🟡 | D2.3 |
| 8 | Confirm KB Articles / User Docs sub-item owner for Data Cert | Manuel | 🟡 | D1.2 |
| 9 | Confirm ESS-02 scope = analysis-only (spike) vs artifact-by-6/30 | Manuel → Joe/Jason Dubreuil | 🟡 | D1.3 |

---

## Open Confirmations (do not report as fact until verified)

- Whether the 6/30 contractual deadline has any agreed grace given PI-2 extends to 8/4 (the holdback language implies firm acceptance).
- Database CI-class attribute scope — present in ADO or genuine gap.
- Qualys unblock status post Issue 1465952 closure.
- Whether "backlog for future PIs" (D1.5) is a tracked artifact.
