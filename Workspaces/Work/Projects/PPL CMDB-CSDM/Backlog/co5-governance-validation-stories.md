---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: created-in-ado
updated: 2026-06-23
tags: [work, cmdb-csdm, backlog, contract, deliverables]
---

# CO5 Governance — Validation Story Drafts (reference)

Draft SAFe-compliant **validation stories**, one per CO5 Deliverable 1 (Governance) sub-item — with **1.1 split per CI class**. Each story gives its deliverable a single, demonstrable acceptance hook for CO5 sign-off.

> **Status: CREATED IN ADO (6/23).** All 9 items now exist as **Feature 1480087 "Governance Validation & Acceptance" (owner Manuel, Ready)** + 8 child stories — ADO IDs filled into the index below. ADO is authoritative; **still to add: points + iteration** (no iteration assigned yet; states are Ready/Refinement/New).
> **Source deliverable text:** [[../co5-deliverable-tracking]] · contract [[../Contract/CO5-signed-2026-05-26.pdf]].
> **Role note (RECOMMENDED — scoped to these stories only):** for the purpose of these draft validation stories, **Manuel Vazquez is listed as the acting Process Owner (PO-support capacity)** — a recommendation pending confirmation. The system-of-record CMDB Configuration Management Process Owner & CCB Chairperson remains **Josh Sterling** (unchanged elsewhere; e.g., still CCB Chair in story 1.5).

## How these are shaped (SAFe / INVEST)
- Each is a **vertical, independently acceptable slice** mapped 1:1 to a CO5 sub-item — sized for one sprint.
- **Acceptance criteria are testable** and double as the deliverable's *acceptance evidence*: artifact exists → reviewed by CCB Class Manager → PO sign-off → stored → linked in ADO.
- **Story vs Enabler:** 1.3 (ESS-02) and 1.4 (SOX) are **Enabler – Compliance** items; the rest are **User Story (Validation)**. Use the team's ADO convention (User Story + "Validation"/"Compliance" tag is fine if Enabler type isn't used).
- **Points** left blank — the team sets them at refinement.
- **All stories must also satisfy the team [[definition-of-done]]** (PO acceptance by Joe Dames, code/docs as applicable, demo accepted at Sprint Review, no open impediments).

## Parent Feature (draft)

### `[Enabler · Compliance] CO5 Deliverable Validation & Acceptance`
- **Feature type:** Enabler – Compliance
- **Owner / approver:** Product Management (**Sonika Das**) + PO (**Joe Dames**); driven by **Manuel Vazquez** (acting PO-support / SM — *recommended, scoped to this work*)
- **Target iterations:** **2.4 – 2.6** (Sprints 4–6)
- **Milestones:** CO5 acceptance — **Jun 30, 2026**; CO6 (if signed) Governance — **Jul 31, 2026**
- **Supports:** CO5 Governance objective (cross-cutting compliance) — not net-new scope

- **Benefit hypothesis:** *If* each CO5 deliverable is formally validated with captured acceptance evidence and PPL sign-off, *then* PPL can accept the deliverables and release the **$533,775 June holdback**, and the team holds an auditable compliance record — reducing acceptance disputes at contract close.

- **Description:** Enabler (Compliance) feature grouping the validation/acceptance work for the CO5 (Change Order #5) deliverables. Validation is largely **non-development** (documentation, review, sign-off, evidence capture, demo), making it well-suited to **Sprints 4–6** — including the **IP iteration (2.6)** and the **code-freeze windows** (Dev Jul 4–18, Test Jul 18–Aug 15) where deployment work is restricted. Children are the per-deliverable validation stories below.

- **Feature acceptance criteria:**
  - [ ] Every CO5 deliverable has a **completed validation story** with acceptance evidence captured (artifact + sign-off)
  - [ ] CCB Class Manager / Process Owner approvals recorded where required (per child story)
  - [ ] PO (Joe Dames) acceptance at Sprint Review; Product Management (Sonika) aware
  - [ ] Evidence stored in the agreed location and **linked in ADO to each CO5 deliverable**
  - [ ] Acceptance milestone met for the **operative contract** (CO5 Jun 30, or CO6 Jul 31 if signed)
  - [ ] Reconciled against [[../co5-deliverable-tracking]] → Acceptance Tracking

- **WSJF / priority:** High — **gates the holdback** and is **time-critical** (fixed deadline); **small job size** (non-dev validation) ⇒ high WSJF, prioritize into S4.

- **Dependencies / risks:**
  - **Validation ≠ delivery** — the underlying work must be complete before its validation story can pass.
  - **Hard gaps limit what can be validated:** G1 (Databases dictionary — no story), G4 (Qualys — blocked), G5 (CCB feature Removed). See [[../co5-deliverable-tracking]].
  - **CO6 signature timing** determines which milestone applies (Jun 30 vs Jul 31).

- **Scope / non-goals:** SOW deliverables only. **Excludes** the non-SOW Health & Lifecycle work — tracked separately under its own enabler (see [[cmdb-health-lifecycle-validation-stories]]).

- **Children — drafted (Governance / Deliverable 1):** 1.1a, 1.1b, 1.1c, 1.1d, 1.2, 1.3, 1.4, 1.5 (below).
  **To add:** validation stories for **Deliverable 2** (Computers / Servers / Databases ingestion) and **Deliverable 3** (Qualys) — only Governance stories are drafted today.

---

## Story index
_The stories below are the children of the parent feature above._


> **🟢 RECONCILED with ADO** — all 8 stories + parent feature **1480087** exist (synced 6/23; **states refreshed 6/29** from the Iter 2.4 board view). All committed to **Iteration 2.4**. **G1 (Databases) & G5 (Monthly CCB) closed at story level** (1480098, 1480107 exist). Reconcile further changes against [[../co5-deliverable-tracking]] → Acceptance Tracking. ADO authoritative.
> **ADO owners (6/29):** 1.1a Vinay Geddannavar · 1.1b Bhushan Salsekar · 1.1c Kiran Dhobale · 1.1d Kiran Dhobale · 1.2 Joe Dames · 1.3 Manuel Vazquez · 1.4 Uloma Adelufosi · 1.5 Manuel Vazquez. ⚠️ ADO owners are story *implementers*, distinct from the CCB Class Mgr *reviewers* below. ⚠️ 1.1c ADO title broadened to "Business Applications/**Application Instances**".

| # | CO5 sub-item | Title | Type | Suggested parent | CCB Class Mgr | ADO ID | State (6/29) |
|---|--------------|-------|------|------------------|---------------|--------|-------------|
| — | **PARENT FEATURE** | Governance Validation & Acceptance | Feature | — | — | **1480087** | Ready (Manuel) — *6/23; not in 6/29 story view* |
| 1.1a | Data Dictionary – Servers | Data Dictionary defined & approved – Servers (Win/Linux) | User Story (Validation) | 1354797 | Ray Reuter | **1480088** | 🟣 Validation |
| 1.1b | Data Dictionary – Computers | Data Dictionary defined & approved – Computers (Phys/Virtual) | User Story (Validation) | 1354794 (+ 2 untracked — see note) | Monica Green / Paul Becker | **1480090** | 🟣 Validation |
| 1.1c | Data Dictionary – Business Apps | Data Dictionary defined & approved – Business Applications | User Story (Validation) | BA governance (confirm) | Todd Dierksheide | **1480097** | 🟣 Validation |
| 1.1d | Data Dictionary – Databases **[G1 ✅ story created]** | Data Dictionary defined & approved – Databases | User Story (Validation) | governance (confirm — no home) | Ray Reuter | **1480098** | 🟣 Validation |
| 1.2 | Data Certification | Data Certification process defined & BA pilot validated | User Story (Validation) | 1247179 / 1402979 | — | **1480099** | 🟢 Ready DoR |
| 1.3 | ESS-02 Alignment | CMDB alignment to ESS-02 confirmed | Enabler – Compliance | confirm (not 1406668-Removed) | Jason Dubreuil | **1480102** | 🟢 Ready DoR |
| 1.4 | SOX BA Review | SOX Business Apps identified + update-access controls | Enabler – Compliance | 1371672 / governance | — | **1480105** | 🟢 Ready DoR |
| 1.5 | Monthly CCB **[G5 ✅ story created]** | Monthly CCB cadence operating + future-PI backlog | User Story (Validation) | 1406668 (un-Remove) | Josh Sterling | **1480107** | 🟢 Ready DoR |

> ✅ **Note (6/23):** All 9 created under a **single real parent Feature 1480087 "Governance Validation & Acceptance"** — the open "no clean feature home for 1.1c / 1.1d / 1.3" question is now moot for *parentage* (they all hang off 1480087). The **CCB Class Manager review/sign-off** mappings above still apply as acceptance gates. Points + iteration still TBD at refinement.

---

## 1.1a — Data Dictionary: Servers (Windows/Linux)
- **Type:** User Story (Validation) · **Suggested parent:** 1354797 — Server Class Data & Form Updates
- **Story:** *As the* CMDB Configuration Management Process Owner, *I want* a documented, CCB-approved data dictionary defining the mandatory attributes for the **Server (Windows/Linux)** CI class, *so that* server data quality can be governed and CO5 Deliverable 1.1 (Servers) can be accepted.
- **Acceptance criteria:**
  - [ ] Mandatory attributes for the Server class documented (attribute, data type, source of record, owning group, mandatory flag)
  - [ ] Reviewed & approved by CCB Class Manager for Servers (**Ray Reuter**) and Process Owner (**Manuel Vazquez — acting / PO-support**)
  - [ ] PO (**Joe Dames**) sign-off; accepted at Sprint Review
  - [ ] Artifact stored in agreed location (PPL Teams › 18 – CMDB 2026 / CMP)
  - [ ] Linked in ADO to CO5 Deliverable 1.1 (Servers)
- **Evidence (real ADO items under 1354797):** 1454371 Extract Servers w/o Support Groups (Active); 1421790 Gap Analysis Servers (Validation); 1355167 BA→Service Instance spike (Active); CI auto-population (CI Owner/Support/Tech Owner) + custom-fields stories (**ADO IDs pending** — Anu); issues 1438967 / 1402520 (Closed).
- **Notes:** Confirm scope: *documented dictionary* vs *implemented form attributes*. Validation can't pass until the pending auto-population/custom-fields stories get IDs and reach Done.

## 1.1b — Data Dictionary: Computers (Physical/Virtual)
- **Type:** User Story (Validation) · **Suggested parent:** 1354794 — Computer Class Data & Form Improvements
- **Story:** *As the* CMDB Configuration Management Process Owner, *I want* a documented, CCB-approved data dictionary defining the mandatory attributes for the **Computer (Physical & Virtual)** CI class, *so that* computer data quality can be governed and CO5 Deliverable 1.1 (Computers) can be accepted.
- **Acceptance criteria:**
  - [ ] Mandatory attributes documented for **both** Physical and Virtual computers (attribute, data type, source of record, owning group, mandatory flag)
  - [ ] Reviewed & approved by CCB Class Managers — Physical (**Monica Green**) and Virtual (**Paul Becker**) — and Process Owner (Manuel Vazquez — acting / PO-support)
  - [ ] PO (Joe Dames) sign-off; accepted at Sprint Review
  - [ ] Artifact stored in agreed location; linked in ADO to CO5 Deliverable 1.1 (Computers)
- **Evidence (real ADO items):** 1313400 Add Asset Tags (Resolved); 1399547 Identify Shared Devices (Validation); 1455858 Virtual Location Mgmt (Active); SCCM Computer precedence 1348712 / 1348716 / 1348717 (Resolved), 1348715 (Validation).
- **⚠️ Notes:** Delivery work spans **three** features — 1354794 **plus** untracked **"Computer Class Data Reconciliation"** (real ADO parent of 1455858 / 1399547) and **"SCCM Computer Class Precedence Updates"** (parent of 1348712/716/717/715). **Get those two feature IDs and reconcile the duplicate computer-class feature names before linking.** Physical vs Virtual have different stakeholder groups (per 6/08 decision) — keep both covered.

## 1.1c — Data Dictionary: Business Applications
- **Type:** User Story (Validation) · **Suggested parent:** Business Application governance feature (confirm)
- **Story:** *As the* CMDB Configuration Management Process Owner, *I want* a documented, CCB-approved data dictionary defining the mandatory attributes for the **Business Application** CI class, *so that* BA data quality can be governed and CO5 Deliverable 1.1 (Business Applications) can be accepted.
- **Acceptance criteria:**
  - [ ] Mandatory attributes documented (e.g., technical owner group, approval groups, support groups, classification, value stream) with source/owning group
  - [ ] Reviewed & approved by CCB Class Manager for Business Application CI (**Todd Dierksheide**) and Process Owner (Manuel Vazquez — acting / PO-support)
  - [ ] PO (Joe Dames) sign-off; accepted at Sprint Review
  - [ ] Artifact stored in agreed location; linked in ADO to CO5 Deliverable 1.1 (Business Applications)
- **Evidence (BA data-population cluster — no feature parent shown):** 1474892 Analyze Value Stream; 1475584 Technical Owner Group *(Manuel)*; 1475585 Approval Groups *(Manuel)*; 1475582 Support Groups; 1478286 Classification.
- **Notes:** Business Apps are **not network-discoverable** — this is governance/data-quality work, not Discovery. Confirm feature home (speculated untracked parent "CMDB Correctness & Data Integrity").

## 1.1d — Data Dictionary: Databases  **[closes hard gap G1]**
- **Type:** User Story (Validation) · **Suggested parent:** governance feature (confirm — no ADO home today)
- **Story:** *As the* CMDB Configuration Management Process Owner, *I want* a documented, CCB-approved data dictionary defining the mandatory attributes for the **Database** CI class, *so that* database data quality can be governed and CO5 Deliverable 1.1 (Databases) can be accepted.
- **Acceptance criteria:**
  - [ ] Mandatory attributes for the Database class documented (attribute, data type, source of record, owning group, mandatory flag)
  - [ ] Reviewed & approved by CCB Class Manager for Database CIs (**Ray Reuter**) and Process Owner (Manuel Vazquez — acting / PO-support)
  - [ ] PO (Joe Dames) sign-off; accepted at Sprint Review
  - [ ] Artifact stored in agreed location; linked in ADO to CO5 Deliverable 1.1 (Databases)
- **Notes:** **This is the clean CO5 gap (G1)** — Databases is named in the contract with equal weight to the other classes but has no story today. Distinct from D2.3 (enhanced *Discovery* for MS-SQL/Oracle) — this is the *attribute definition*, not ingestion.

---

## 1.2 — Data Certification process defined & Business App pilot validated
- **Type:** User Story (Validation) · **Suggested parent:** 1247179 / 1402979
- **Story:** *As a* CI Data Owner, *I want* the data-certification process defined and proven through the Business Application CI-class pilot, *so that* CI accuracy is attested on a repeatable cadence and CO5 Deliverable 1.2 can be accepted.
- **Acceptance criteria:**
  - [ ] Process definition documented: intake for new certifications + end-to-end process flow overview
  - [ ] Pilot executed for the **Business Application CI class**; completion + results captured
  - [ ] Supporting **KB / user documentation** published *(currently unowned — assign owner)*
  - [ ] Sonika UAT sign-off (6/10) and PROD validation by Todd (6/24–25) recorded
  - [ ] PO demo accepted at Sprint Review; evidence linked to CO5 Deliverable 1.2
- **Evidence (real ADO items):** 1435307 Pilot Changes (Validation); **1402727** Update Data Cert Dashboard (**UAT signed 6/10; PROD 6/23**); 1402958 cluster — 1402962/976/980/984/985 (Defining/New); 1402959 Pilot group (Closed).
- **Notes:** Strongest-covered sub-item; dashboard (1402727) deploys PROD 6/23 — the **holdback-critical** acceptance date. This story consolidates the pieces into one acceptance artifact.

## 1.3 — CMDB alignment to ESS-02 confirmed
- **Type:** Enabler – Compliance (or User Story + Compliance tag)
- **Story:** *As a* Cybersecurity & Compliance stakeholder, *I want* CMDB alignment to ESS-02 documented and confirmed, *so that* CMDB meets security/compliance requirements and CO5 Deliverable 1.3 can be accepted.
- **Acceptance criteria:**
  - [ ] ESS-02 requirements identified and mapped to CMDB classes / attributes / controls
  - [ ] Gaps documented with a remediation owner and target
  - [ ] Reviewed and confirmed with **Jason Dubreuil** (CCB Cyber/Compliance member)
  - [ ] Agreed scope explicit: **analysis-only** (spike sufficient) **vs.** implementation required — AC reflects the decision
  - [ ] Signed off; linked to CO5 Deliverable 1.3
- **Notes:** Confirm what "ESS-02" stands for (not defined in the contract). Today: spike 1420244 under feature 1406668 (Removed).

## 1.4 — SOX Business Apps identified + update-access controls
- **Type:** Enabler – Compliance (or User Story + Compliance tag)
- **Story:** *As a* SOX / Audit stakeholder, *I want* SOX-relevant Business Applications correctly identified in the CMDB with the right update-access controls, *so that* SOX data integrity is governed and CO5 Deliverable 1.4 can be accepted.
- **Acceptance criteria:**
  - [ ] SOX-relevant Business Applications flagged/identified in the CMDB
  - [ ] Update rules restrict edits to the correct groups (e.g., Cyber Risk & DR per the 6/08 decision)
  - [ ] SOX-team ownership-change notification validated (ties to story 1455827)
  - [ ] **Scope boundary honored: SOX data only — NERC/CIP indicators explicitly excluded**
  - [ ] Reviewed with Audit/SOX stakeholders; PO sign-off; linked to CO5 Deliverable 1.4
- **Notes:** Watch 1455827 — currently Iter 2.5 (post-6/30) with an open Joe PI-2-vs-PI-3 decision.

## 1.5 — Monthly CCB cadence operating + future-PI backlog
- **Type:** User Story (Validation) · **Suggested parent:** 1406668 *(must be un-Removed — see notes)*
- **Story:** *As the* CCB Chairperson (Configuration Management Process Owner), *I want* the monthly CCB cadence running and a future-PI backlog established, *so that* CMDB governance is demonstrable and CO5 Deliverable 1.5 can be accepted.
- **Acceptance criteria:**
  - [ ] Monthly CCB meetings held with agenda, minutes, and attendance recorded (May/Jun/Jul evidence)
  - [ ] A backlog of CMDB items for future PIs created and visible in ADO
  - [ ] **The ADO feature/stories representing CCB are Active (not Removed)** — un-Remove 1406668 or re-parent the CCB stories so the evidence is valid *(closes gap G5)*
  - [ ] Stored in agreed location; PO sign-off; linked to CO5 Deliverable 1.5
- **Notes:** Cadence is already happening (CCB 6/16, Audit Sync 6/18) — the gap is that the proving feature (1406668) is marked Removed.

---

## To confirm before creating in ADO
- Parent features for **1.1c (Business Apps)**, **1.1d (Databases)**, and **1.3 (ESS-02)** — no clean live feature home today.
- Whether 1.1 deliverable = **documented data dictionary** vs **implemented form attributes** (changes AC).
- Whether the ART tracks compliance work as **Enabler** type (affects 1.3 / 1.4).
- ESS-02 definition (with Jason Dubreuil).

_When the real ADO items exist, add their IDs/points/iteration to the Story index above and reconcile against [[../co5-deliverable-tracking]] Acceptance Tracking._
