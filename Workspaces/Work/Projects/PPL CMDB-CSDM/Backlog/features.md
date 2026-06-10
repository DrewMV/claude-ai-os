---
type: team-artifact
workspace: Work
project: CMDB-CSDM
updated: 2026-06-01
tags: [work, cmdb-csdm, backlog, features]
---

# Features — CMDB-CSDM

Feature-level tracking mapped to PI objectives. Features are owned by PO (Joe Dames) and broken into stories by the team. See [[PI-2/pi-planning]] for full objective text and [[Backlog/definition-of-ready]] for story readiness criteria.

## PI-2 Features

Operational priorities (0 = most urgent) reflect team discussion from 2026-05-26. ADO feature and story IDs confirmed.

---

### PI Obj 1 — Automate Network Gear Discovery | Op Priority: 1 | ADO Obj: 1366657

| ADO Feature ID | Feature | Known Stories | Status |
|---|---|---|---|
| 1383523 | Unplanned Backlog - CMDB Workstream | Spike 1421790: Gap analysis for Servers Linux & Windows (Tony) | Active |
| 1356646 | Network Device Coverage Reconciliation - Group 1 | — | Active |
| 1356826 | SCCM Server Class Precedence Updates | — | Active |
| 1354797 | Server Class Data & Form Updates | — | Active |
| 1411480 | CMDB PI2.26 Enhancements | — | Active |
| 1354794 | Computer Class Data & Form Improvements | — | Active |
| 1355888 | Update Operational Monitoring Activities P2 | — | Active |
| 1355890 | Support ServiceNow Upgrade Analysis | — | Active |

**Blockers:** DB and SNMP credentials in progress (Tony); Server ownership not yet accurate; HCM needed for computer location (Sonika); CI Ownership for servers — Joe has plan, pending OCM review and impact assessment for incident/request creators and CI owners

---

### PI Obj 2 — Establish CI Data Certification Program | Op Priority: 1 | ADO Obj: 1420082

| ADO Feature ID | Feature | Known Stories | Status |
|---|---|---|---|
| 1247179 | Data Certification Pilot - Functionality | — | Active |
| 1371672 | Governance Model for Requesting New Business Applications | — | Active |
| 1382404 | Data Certification Rollout | — | Active |
| 1402958 | Data Certification Pilot - Implementation Planning | — | Active |
| 1402979 | Data Certification Pilot - Implementation Support | US 1402727: Update Data Certification Dashboard (Kiran) | Active |

---

### PI Obj 3 — Expand Service Mapping Foundation | Op Priority: 2 | ADO Obj: 1366660

| ADO Feature ID | Feature | Known Stories | Status |
|---|---|---|---|
| 1355866 | Service Mapping PI2 Wave 17 & 18 | US 1380747: MV90 User Access (Tanzeel); US 1380757: RIE Electric Wholesale Settlement; US 1400703: Vault Inspection System; US 1281161: WATT | Active |
| 1355868 | Service Mapping PI2 Wave 19 & 20 | Spike 1420634: Review Apps being migrated & Impact to Service Mapping; Spike 1326754: Evaluate Automated Service Mapping via Endpoint-Based Discovery | Active |
| 1355871 | Service Mapping PI2 Wave 20 & 21 | — | Active |

**Blockers:** Missing server credentials for automated scanning (Sonika support needed); DNS issue ongoing — Alex to add Christian's email update and attempt email resolution before scheduling additional meetings

---

### PI Obj 4 — Prepare CMDB for Regulatory and Security Integrations | ADO Obj: 1366662
**Features:** 1250905 (Qualys & ServiceNow Integration), 1370224 (NERC-CIP CI Security Requirements)
This objective covers three distinct activity streams:

#### Stream A — Governance | Op Priority: 2
Formalizing CCB ceremony cadence and compliance process.
**Next:** Formalize CCB cadence (ref: PPL MS Teams > General > Accenture & PPL - Working Documents > 18 - CMDB 2026 > CCB Meetings); engage Jason Dubriel; document CMP.

#### Stream B — NERC-CIP Security Requirements | Op Priority: 4
ESS 02 scope. Early engagement phase.
**Next:** Talk to Alex on where docs are (action from 5/20); engage Sonika / Cyber compliance team; engage Jason Dubriel; document CMP.

#### Stream C — Qualys Integration | Op Priority: 5

| ADO ID | Title | Owner | PI Scope |
|---|---|---|---|
| US 1428703 | Install x_qual5_itam_nwapp plugin on dev, test and Prod (Part 1) | Stan | PI2 |
| US 1428704 | Configure Qualys integration for CMDB to Qualys (Part 2) | Stan | PI2 |
| Spike 1234585 | Define and Configure Data Scope and Import Views in Qualys | Stan | PI2 |

**Phase 1 (PI2):** Read-only integration
**Phase 2 (PI3):** Two-way integration — if needed; long-term data completeness value

---

### PI Obj 5 — Embed NowAssist AI Across CMDB and ITSM Workflows | Op Priority: 3 | ADO Obj: 1408764

**⚠️ ADO features still missing at feature level — Anu to provide feature IDs upon return**

Stories created in ADO by Alex Phan on 2026-06-08. Feature-level linkage unconfirmed.

| ADO Story ID | Story | Owner | Size | Status |
|---|---|---|---|---|
| 1436576 | NowAssist: Confirm Platform Prerequisites for NowAssist Activation (Part 1) | Karen | 1 pt | Sprint 2.3 |
| 1436579 | NowAssist: Activate Now Assist for CMDB Plugin | Karen | 1 pt | Sprint 2.3 |
| 1436593 | NowAssist: Activate Contextual CI Form Help Skill | Karen | 1 pt | Sprint 2.3 |
| 1436592 | NowAssist: Activate CI Summarization Skill | Karen | 1 pt | Sprint 2.3 |

PI-2 scope is an OOB capability assessment, not full deployment:
- NowAssist for CMDB out-of-box features
- CI Summarization and contextual form help
- **Pending (from 5/20):** Assess what NowAssist capabilities are available in Australia vs Yokohama

> The 5-phase NowAssist implementation plan (OBJ-2.x Duplicate CI Elimination, OBJ-3.x NL CMDB Search) is PI-3 scope. PI-2 establishes the baseline capability picture. See [[PI-3/pi3-planning-readiness]] and [[nowassist-implementation-plan]].

---

### PI Obj 6 — Enable Governed VMware-to-Azure Migration | Op Priority: 0 (most urgent) | ADO Obj: 1420079

| ADO Feature ID | Feature | Known Stories | Status |
|---|---|---|---|
| 1420613 | CMDB Support for Air Lift | US 1418610: Airlift to Azure Pre-Migration; US 1418618: Airlift to Azure During Migration; US 1418621: Airlift to Azure Post-Migration; US 1416384: Auto Populate CI Owner / Support Group / Technical Owner for Server Class | Active |

---

## Backlog Gap Check — Updated

| Objective | ADO Features | Stories in ADO | Status |
|---|---|---|---|
| PI Obj 1 — Network Gear Discovery | 8 features confirmed | Spike 1421790 + others in progress | ✅ Covered |
| PI Obj 2 — Data Certification | 5 features confirmed | US 1402727 confirmed; others TBD | ✅ Covered |
| PI Obj 3 — Service Mapping | 3 features confirmed | Multiple stories confirmed | ✅ Covered |
| PI Obj 4 — Governance (Stream A) | 1250905, 1370224 | No stories yet | ⚠️ Light |
| PI Obj 4 — NERC-CIP (Stream B) | 1250905, 1370224 | No stories yet | ⚠️ Light |
| PI Obj 4 — Qualys (Stream C) | 1250905, 1370224 | 3 stories/spikes confirmed (Stan) | ✅ Covered |
| PI Obj 5 — NowAssist | **None — Joe to create** | None | ❌ Gap |
| PI Obj 6 — Azure Migration | 1420613 confirmed | 4 stories confirmed | ✅ Covered |

## PI-3 Features

_Confirmed at PI3 Planning (Jul 22–Aug 4, 2026 during PI2 IP iteration). Candidates below from [[nowassist-implementation-plan]]._

| Feature | PI Objective # | Description | Iterations | Status |
|---------|--------------|-------------|-----------|--------|
| NowAssist — Duplicate CI Elimination | TBD | OBJ-2.1: Activate Manage Duplicate CIs skill; OBJ-2.2: Root cause analysis → IRE rule improvements. Target: ≥25% CI count reduction within 4 weeks of activation. Deferred from PI-2 (PI-2 scope = OOB assessment only) | 3.1–3.2 | Candidate |
| NowAssist — NL CMDB Search | TBD | OBJ-3.1: Activate Search CMDB workflow, validate against 10–15 PPL query use cases; OBJ-3.2: Roll out to secondary user groups (incident, change, security). Deferred from PI-2 | 3.2–3.4 | Candidate |
| NowAssist — Guided CI Creation | TBD | OBJ-4.1: Activate Create Configuration Item guided workflow; validate for top 5 CI classes (Servers, Business Apps, Network Devices, Databases, Cloud VMs). OBJ-4.2: Integrate into PPL CMDB onboarding process | 3.1–3.3 | Candidate |
| NowAssist — Governance Advice Workflow | TBD | OBJ-5.1: Activate Provide Advice on CMDB Governance workflow; complete first end-to-end governance advice session. OBJ-5.2: Establish quarterly NowAssist governance review cycle with AI-generated health narratives replacing manual dashboard reporting | 3.3–3.5 | Candidate |
| Qualys Phase 2 — Two-Way Integration | TBD | Full bidirectional Qualys-CMDB integration for data completeness; deferred from PI-2 Phase 1 (read-only) | TBD | Candidate |
| CI Certification — Extended Scope | TBD | Extend certification program beyond Business Apps (deferred from PI2) | TBD | Candidate |

## Backlog (Future PIs)

| Feature | Description | Priority | Notes |
|---------|-------------|---------|-------|
| NowAssist — Custom Skills (NASK) | OBJ-6.1: Identify and prioritize NASK use cases from observed gaps in Phases 1–5; get top 1–2 candidates approved by Demand Board | P2 | Requires Phases 1–5 operational experience; NASK capability must be available on instance |
