---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: reference-draft
scope: NON-SOW
updated: 2026-06-20
tags: [work, cmdb-csdm, backlog, quality-governance]
---

# CMDB Health & Lifecycle — Validation Story Drafts (NON-SOW)

> 🟠 **NOT CO5 SOW deliverables.** Team-added quality governance. These **require acceptance** but **do NOT gate CO5 acceptance or the $533,775 holdback**. Tracked in a **separate quality lane** — deliberately kept apart from the SOW validation stories in [[co5-governance-validation-stories]].

One **Health & Lifecycle** validation story per CI class. Complements (does not replace) the SOW data-dictionary stories: 1.1 *defines* the attributes (CCB-accepted, contractual); these *measure and maintain* data quality over time (PO/PM-accepted, non-contractual).

- **Source/related:** [[co5-governance-validation-stories]] (SOW) · [[../co5-deliverable-tracking]] · health baseline spikes 1436581 / 1470837.
- **Status: REFERENCE / DRAFT.** Manuel creates the real items in ADO and reconciles back (IDs/points/iteration).
- **Role note (RECOMMENDED — scoped to these stories only):** the "CMDB Configuration Management Process Owner" persona in these stories is filled by **Manuel Vazquez (acting / PO-support)** — a recommendation pending confirmation, consistent with [[co5-governance-validation-stories]]. System-of-record Process Owner & CCB Chairperson remains **Josh Sterling**. (Acceptance lane here stays PM **Sonika Das** + PO **Joe Dames**; CCB informed.)

## Conventions (apply to all four stories)
- **Health dimensions** (ServiceNow CMDB Health): **Completeness** (required attributes/relationships populated), **Compliance** (rule conformance — duplicates, orphans, required fields), **Correctness** (accurate, current values).
- **Target:** working **85–90%** health score — *confirm formally with Sonika* before committing.
- **Acceptance lane (non-SOW):** Product Manager **Sonika Das** accepts the targets; PO **Joe Dames** sign-off; accepted at Sprint Review. CCB **informed** (visibility only) — *not* contractual CCB acceptance.
- **Tracking:** logged in the quality-governance register; **NOT linked to a CO5 deliverable number**; tag `NON-SOW` / `Quality-Governance`.
- **Suggested parent:** *CMDB Health & Data Quality* feature (confirm/create — not a CO5 deliverable).
- **Version caveat:** validate KPI definitions against the deployed **Australia** release.
- Must also meet the team [[definition-of-done]].

## Story index

| ID | CI Class | Staleness basis | Class Mgr (informed) |
|----|----------|-----------------|----------------------|
| HL-1 | Servers (Win/Linux) | Discovery last-seen | Ray Reuter |
| HL-2 | Computers (Phys/Virtual) | Discovery last-seen | Monica Green / Paul Becker |
| HL-3 | Databases | Discovery last-seen (MS-SQL/Oracle) | Ray Reuter |
| HL-4 | Business Applications | **Certification recency + ownership validity** (NOT discovery) | Todd Dierksheide |

---

## HL-1 — CMDB Health & Lifecycle: Servers (Windows/Linux)
- **Type:** User Story (Validation · NON-SOW)
- **Story:** *As the* CMDB Configuration Management Process Owner, *I want* CMDB Health KPIs configured and measured against target for the **Server (Win/Linux)** class, with a discovery-based staleness/lifecycle policy, *so that* server data quality is continuously governed.
- **Acceptance criteria:**
  - [ ] Completeness / Compliance / Correctness KPIs configured for the Server class; each scored vs target (85–90%, confirm)
  - [ ] Server class included in the CMDB Health dashboard / baseline (ties spikes 1436581 / 1470837)
  - [ ] Staleness policy: Server CIs not seen by Discovery within **N days** (threshold agreed, e.g. 30/45) are flagged
  - [ ] Lifecycle Stage / Status transitions defined for stale/retired servers; demoed on a sample of live CIs
  - [ ] PM (Sonika) accepts targets; PO (Joe) sign-off; CCB informed; logged in quality register (not a CO5 deliverable)
- **Notes:** Builds on SCCM/Discovery precedence (1403759/760/762/763) and credential work (1444864).

## HL-2 — CMDB Health & Lifecycle: Computers (Physical/Virtual)
- **Type:** User Story (Validation · NON-SOW)
- **Story:** *As the* CMDB Configuration Management Process Owner, *I want* CMDB Health KPIs configured and measured against target for the **Computer (Physical & Virtual)** class, with a discovery-based staleness/lifecycle policy, *so that* computer data quality is continuously governed.
- **Acceptance criteria:**
  - [ ] Completeness / Compliance / Correctness KPIs configured for **both** Physical and Virtual computers; each scored vs target
  - [ ] Computer class included in the CMDB Health dashboard / baseline
  - [ ] Staleness policy: Computer CIs not seen by Discovery/SCCM within **N days** are flagged (note: physical-device coverage RISK — offline devices may not update)
  - [ ] Lifecycle Stage / Status transitions for stale/retired computers (cf. 1402790 retired-computers pattern); demoed on a sample
  - [ ] PM (Sonika) accepts targets; PO (Joe) sign-off; CCB informed; logged in quality register
- **Notes:** Physical vs Virtual have different stakeholder groups — keep both covered. Ties SCCM precedence 1348712/716/717.

## HL-3 — CMDB Health & Lifecycle: Databases
- **Type:** User Story (Validation · NON-SOW)
- **Story:** *As the* CMDB Configuration Management Process Owner, *I want* CMDB Health KPIs configured and measured against target for the **Database** class, with a discovery-based staleness/lifecycle policy, *so that* database data quality is continuously governed.
- **Acceptance criteria:**
  - [ ] Completeness / Compliance / Correctness KPIs configured for the Database class; each scored vs target
  - [ ] Database class included in the CMDB Health dashboard / baseline
  - [ ] Staleness policy: MS-SQL/Oracle DB CIs not seen by Discovery within **N days** are flagged
  - [ ] Lifecycle Stage / Status transitions for stale/retired databases; demoed on a sample
  - [ ] PM (Sonika) accepts targets; PO (Joe) sign-off; CCB informed; logged in quality register
- **Notes:** Depends on enhanced DB Discovery (D2.3) and the credential-distribution RISK (1444864) — staleness measurement is only as good as DB discovery coverage.

## HL-4 — CMDB Health & Lifecycle: Business Applications  *(adapted — not discovery-based)*
- **Type:** User Story (Validation · NON-SOW)
- **Story:** *As the* CMDB Configuration Management Process Owner, *I want* CMDB Health KPIs configured for the **Business Application** class, with a **certification- and ownership-based** staleness/lifecycle policy, *so that* BA data quality is continuously governed despite BAs not being discoverable.
- **Acceptance criteria:**
  - [ ] **Completeness:** required BA attributes populated (technical owner group, approval groups, support groups, classification, value stream) — scored vs target *(manual/governance source, not Discovery)*
  - [ ] **Compliance:** duplicates/orphans/required-field rules **plus valid ownership** (CI owner still active at PPL)
  - [ ] **Correctness:** values confirmed via owner attestation
  - [ ] **Staleness (adapted):** measured by **data-certification recency** (certification overdue → stale) and **ownership validity** (owner left PPL → flagged) — **NOT** a Discovery "last seen" date
  - [ ] Lifecycle Stage / Status transitions for decommissioned/stale BAs via governance (not auto-discovery); demoed on a sample
  - [ ] PM (Sonika) accepts targets; PO (Joe) sign-off; CCB informed; logged in quality register
- **Notes:** This is the deliberate divergence from HL-1/2/3. Ties to Data Certification (SOW 1.2), Inactive CI Owners reporting (1402776), Monitor/Update CI owners who left PPL (1339116), and the BA data-population cluster (1475582/1478286/1475584/1475585/1474892).

---

## Why HL-4 (Business Apps) differs
| | HL-1/2/3 (Servers/Computers/DBs) | HL-4 (Business Apps) |
|---|---|---|
| Discoverable? | Yes (agent/scan) | **No** |
| Completeness source | Discovery + SCCM | **Manual / governance** |
| Staleness basis | Discovery "last seen in N days" | **Certification overdue + ownership validity** |
| Lifecycle trigger | Discovery-driven | **Governance/attestation-driven** |

## To confirm before creating in ADO
- The 85–90% health target (Sonika) — and whether targets differ per class.
- The staleness threshold(s) **N** per class (discovery cadence dependent).
- Parent feature for the quality lane (create a *CMDB Health & Data Quality* feature?).
- Whether BA staleness should fold into Data Certification (1.2) rather than stand alone.
