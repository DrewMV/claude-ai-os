---
type: ado-tracking
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
contract: CO6 (Change Order #6)
source: Azure DevOps (A-INFOPS\FY26\PI3)
sources:
  - "Azure DevOps (A-INFOPS\\FY26\\PI3)"
  - "C:\\Users\\manuel.b.vazquez\\Desktop\\PI3-Objectives-Features-2026-07-22.pptx"
as-of: 2026-07-28
updated: 2026-07-28
summary: "CMDB/CSDM team PI-3 ADO objectives (4) and features (11), mapped to CO6, with sprint assignments and delivery gate compliance check."
base_confidence: 0.9
lifecycle: draft
lifecycle_changed: "2026-07-27"
tier: supporting
provenance:
  extracted: 0.95
  inferred: 0.05
  ambiguous: 0.0
tags: [work, cmdb-csdm, safe, pi-planning, co6]
---

# PI-3 — CMDB/CSDM Team ADO Objectives & Features

**What this is:** The authoritative record of the **CMDB/CSDM team's** PI-3 objectives and features **as they exist in Azure DevOps** (ADO). The CMDB/CSDM focus area is a **subset of CO6** — it is the slice of the contract this team owns, executes, and reports on.

**What this is not:** The full CO6 contract scope. The 7 governing CO6 objectives are unchanged and live in [[PI-3/pi3-objectives]]. CO6 does not change; this file tracks only the CMDB/CSDM ADO items and keeps them traceable back to CO6.

> **Subset relationship:** 4 ADO objectives here map to CO6 Objectives 2, 3, 4, and 5. CO6 Objectives 1 (Platform Ops), 6 (NERC-CIP Strategy), and 7 (Legacy Migration) are real CO6 scope but sit outside the CMDB/CSDM focus area, so they are intentionally absent from this list.

---

## Snapshot (as of 2026-07-28)

| Metric | Value |
|--------|-------|
| ADO area path | `A-INFOPS\FY26\PI3` |
| Objectives | 4 |
| Features | 11 |
| State | Objectives + 3.2–3.5 features: **New**; the three 3.1 features (1516993, 1517650, 1517065): **Defining** |
| PI-3 window | Aug 5 – Oct 27, 2026 |
| Sprints in use | 3.1 – 3.5 (2–3 features each; 3.6 IP empty) |

**Revision 2026-07-28:** State refresh from the ADO board — the three Iteration-3.1 features (1516993 Network Discovery, 1517650 Silver Service Maps, 1517065 Qualys) have moved New → **Defining**; all objectives and the 3.2–3.5 features remain New. Sprint assignments unchanged.
**Revision 2026-07-22:** ADO re-sequenced feature sprint assignments — features now span 3.1–3.5 (previously front-loaded in 3.1–3.4). CO6 compliance re-checked below.

---

## Objectives (4)

| ADO ID | Objective | Owner | State | Maps to CO6 |
|--------|-----------|-------|-------|-------------|
| 1516954 | Automate Network Device Discovery in the CMDB | Vazquez, Manuel (Contractor) | New | CO6 Obj 4 |
| 1516955 | Build & Validate Service Maps for Priority Business Apps | Adam Griffis | New | CO6 Obj 5 |
| 1516956 | Certify CMDB Data Across the Four Major CI Classes | Vazquez, Manuel (Contractor) | New | CO6 Obj 3 |
| 1516957 | Activate the ServiceNow → Qualys Attribute Sync in Production | Vazquez, Manuel (Contractor) | New | CO6 Obj 2 |

**Objective descriptions** (from PI Planning deck, Jul 22):

| ADO ID | One-line description |
|--------|----------------------|
| 1516954 | Automated credentialed discovery of all network device types, mandatory attribute population, and ≥90% owner-validated coverage. |
| 1516955 | Owner-validated Silver- and Gold-tier service maps, with ≥75% of the business-service inventory represented. |
| 1516956 | End-to-end data certification — process, PROD build, dashboards, training — across Computers, Servers, Databases, Network Devices. |
| 1516957 | One-way ServiceNow → Qualys sync of owner, support group, and SOX flag, live in production on a defined schedule. |

---

## Features by Objective (11)

### Automate Network Device Discovery in the CMDB — 1516954 (CO6 Obj 4)
Owner: Vazquez, Manuel (Contractor) · Breakdown: [[PI-3/pi3-network-discovery-feature-breakdown]]

| ADO ID | Feature | Owner | State | Iteration | Start | CO6 Delivery |
|--------|---------|-------|-------|-----------|-------|--------------|
| 1516993 | Automated Credentialed Discovery Live — All Network Device Types | Vazquez, Manuel (Contractor) | Defining | 3.1 | 8/5/2026 | Aug 31, 2026 |
| 1517005 | Mandatory Attribute Population via Discovery — Network Devices | Vazquez, Manuel (Contractor) | New | 3.3 | 9/2/2026 | Sep 30, 2026 |
| 1356646 | Network Inventory Coverage Reconciliation & Owner Validation (≥90%) | Vazquez, Manuel (Contractor) | New | 3.5 | 9/30/2026 | Oct 30, 2026 |

### Build & Validate Service Maps for Priority Business Apps — 1516955 (CO6 Obj 5)
Owner: Adam Griffis · Breakdown: [[PI-3/pi3-service-mapping-feature-breakdown]]

| ADO ID | Feature | Owner | State | Iteration | Start | CO6 Delivery |
|--------|---------|-------|-------|-----------|-------|--------------|
| 1517650 | Silver-Tier Service Maps (App → Infrastructure) + ≥75% Business-Service Inventory | Adam Griffis | Defining | 3.1 | 8/5/2026 | Aug 31, 2026 |
| 1517655 | Gold-Tier Service Maps (Service → App) + Silver Validation Pass | Adam Griffis | New | 3.3 | 9/2/2026 | Sep 30, 2026 |
| 1518000 | Remaining Contractor-Managed Silver-Tier Maps + All-Silver Service → App Layer | Adam Griffis | New | 3.5 | 9/30/2026 | Oct 30, 2026 |

### Certify CMDB Data Across the Four Major CI Classes — 1516956 (CO6 Obj 3)
Owner: Vazquez, Manuel (Contractor) · Breakdown: [[PI-3/pi3-data-certification-feature-breakdown]]
Story + dependency drafts (SAFe), all four classes:
- **1517029** Computers → [[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]] (5 stories + 6 deps)
- **1517032** Servers → [[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]] (5 stories + 7 deps)
- **1517037** Databases → [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]] (5 stories + 6 deps)
- **1517040** Network Devices → [[PI-3/pi3-cert-1517040-certify-network-devices-stories-dependencies]] (6 stories + 5 deps; highest-risk — depends on Obj 4 1517005)

| ADO ID | Feature | Owner | State | Iteration | Start | CO6 Delivery |
|--------|---------|-------|-------|-----------|-------|--------------|
| 1517029 | Certify Computers — CMDB Data Certification | Vazquez, Manuel (Contractor) | New | 3.2 | 8/19/2026 | Sep 30, 2026 |
| 1517032 | Certify Servers — CMDB Data Certification | Vazquez, Manuel (Contractor) | New | 3.2 | 8/19/2026 | Sep 30, 2026 |
| 1517037 | Certify Databases — CMDB Data Certification | Vazquez, Manuel (Contractor) | New | 3.4 | 9/16/2026 | Oct 30, 2026 |
| 1517040 | Certify Network Devices — CMDB Data Certification | Vazquez, Manuel (Contractor) | New | 3.4 | 9/16/2026 | Oct 30, 2026 |

### Activate the ServiceNow → Qualys Attribute Sync in Production — 1516957 (CO6 Obj 2)
Owner: Vazquez, Manuel (Contractor) · Breakdown: [[PI-3/pi3-qualys-integration-feature-breakdown]]

| ADO ID | Feature | Owner | State | Iteration | Start | CO6 Delivery |
|--------|---------|-------|-------|-----------|-------|--------------|
| 1517065 | Activate ServiceNow → Qualys Attribute Sync (PROD) | Tomberg, Stan (Contractor) | Defining | 3.1 | 8/5/2026 | Sep 30, 2026 |

---

## Features by Iteration (load view)

| Iteration | Start | Features |
|-----------|-------|----------|
| 3.1 | 8/5/2026 | 1516993, 1517650, 1517065 (3) |
| 3.2 | 8/19/2026 | 1517029, 1517032 (2) |
| 3.3 | 9/2/2026 | 1517005, 1517655 (2) |
| 3.4 | 9/16/2026 | 1517037, 1517040 (2) |
| 3.5 | 9/30/2026 | 1356646, 1518000 (2) |

---

## CO6 Delivery Gates — Compliance Check (2026-07-22)

Each feature delivers a CO6 acceptance criterion with a fixed completion date. Check: does each feature's assigned sprint close on/before its CO6 delivery date?

| CO6 gate | Features | Latest sprint | Sprint ends | Verdict |
|----------|----------|---------------|-------------|---------|
| Aug 31, 2026 | 1516993, 1517650 | 3.1 | Aug 18 | ✅ ahead (13 days) |
| Sep 30, 2026 | 1517065, 1517029, 1517032, 1517005, 1517655 | 3.3 | Sep 15 | ✅ ahead (15 days) |
| Oct 30, 2026 | 1517037, 1517040, 1356646, 1518000 | 3.5 | Oct 13 | ✅ ahead (17 days) |

**Result: PASS** — the ADO schedule fits within CO6. Every feature completes in a sprint that closes before its CO6 delivery date. The two Aug 31 items stayed in Sprint 3.1 (the only tight gate). The Oct 30 gates fall after PI-3 close (Oct 27); those features complete by Sprint 3.5 (Oct 13), leaving the 3.6 IP iteration (Oct 14–27) as validation/hardening buffer before the external date.

---

## CO6 Traceability

| CMDB/CSDM ADO Objective | CO6 Objective | In CMDB/CSDM focus area? |
|-------------------------|---------------|--------------------------|
| Automate Network Device Discovery in the CMDB (1516954) | Obj 4 — Automate Network Device Discovery | Yes |
| Build & Validate Service Maps for Priority Business Apps (1516955) | Obj 5 — Build Service Maps for Business Applications | Yes |
| Certify CMDB Data Across the Four Major CI Classes (1516956) | Obj 3 — Expand CI Data Certification | Yes |
| Activate ServiceNow → Qualys Attribute Sync in Production (1516957) | Obj 2 — Activate Qualys Integration | Yes |
| — | Obj 1 — Sustain ServiceNow Platform Operations | No (outside CMDB/CSDM focus) |
| — | Obj 6 — NERC-CIP ServiceNow Platform Strategy | No (outside CMDB/CSDM focus) |
| — | Obj 7 — Legacy Platform Migration | No (outside CMDB/CSDM focus) |

Full CO6 objective detail and acceptance criteria: [[PI-3/pi3-objectives]].

---

## Reconciliation Notes (confirm in ADO)

- **1356646** carries a work-item ID from a much lower range than the other PI-3 items (1.35M vs 1.51M) — likely a pre-existing item pulled into PI-3. Confirm it is the intended Feature.
- **1356646** now sits in **Iteration 3.5** with start **9/30/2026** (per ADO re-sequencing, 2026-07-22) — consistent with the 3.5 window (Sep 30 – Oct 13); CO6 delivery Oct 30. (Earlier 3.4 / 9-16 placement superseded.) — resolved

---

## Maintenance

Update this file whenever ADO changes for the CMDB/CSDM PI-3 items: refresh the `State` column as items move (New → Active → Closed), add/remove features, and bump `as-of` / `updated`. This file is the reporting source for CMDB/CSDM PI-3 objective and feature status.
