---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1517037 — Certify Databases — CMDB Data Certification"
objective: CO6 Obj 3 — Expand CI Data Certification Across All Major Classes
sprint: "3.4 (ADO start); build 3.3–3.5, sign-off 3.6 IP"
co6-due: 2026-10-30
status: reference-draft
updated: 2026-07-28
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification]
relationships:
  - target: "[[PI-3/pi3-data-certification-feature-breakdown]]"
    type: derived_from
  - target: "[[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-cmdb-csdm-ado-tracking]]"
    type: related_to
  - target: "[[PI-3/pi3-objectives]]"
    type: related_to
  - target: "[[cmdb-health-completeness-correctness-stories]]"
    type: related_to
---

# Feature 1517037 — Stories & Dependencies

**Certify Databases — CMDB Data Certification**
ADO start Sprint 3.4 · build 3.3–3.5 · sign-off 3.6 IP · CO6 due Oct 30 · Owner: M. Vazquez

> **Status: REFERENCE / DRAFT** — Manuel creates the real items in ADO under Feature 1517037 and reconciles IDs back here (ADO authoritative). Per [[definition-of-ready]], create stories from the Feature "+" link, never standalone.
> Third of four certification features. Same PI-2 BA pilot pattern as [[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies|Computers]] and [[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies|Servers]], but on the **Oct 30** gate (not Sep 30). See [[PI-3/pi3-data-certification-feature-breakdown]] for the full feature-level breakdown.

---

## Sprint reconciliation & gate note (raise at Sprint Planning)

- **Sprint:** ADO records Feature 1517037's start as **3.4 (Sep 16)**; the [[PI-3/pi3-data-certification-feature-breakdown]] shapes it **3.3 → 3.5** with sign-off in **3.6 IP**. Process-flow (DB-1) can start in 3.3; build/run land 3.4–3.5; training/validation complete in the IP iteration. The **test code freeze (Aug 15)** is long past — no freeze constraint applies to this feature.
- **Gate date open item:** [[pi3-objectives]] and CO6 show **Oct 30** (3 days after PI-3 ends Oct 27); the objectives deck says **Oct 27**. Build must be **done by end of Sprint 3.5 (Oct 13)**, leaving 3.6 IP (Oct 14–27) as validation/training buffer ahead of the external date. Confirm the gate date at planning.

---

## Database starting position (why this feature is not a straight clone)

- **Trustworthy data is the precondition, and it's at risk.** Certification attests that data is correct; for Databases the underlying discovery data quality is threatened by the **Oracle / Kentucky visibility gap** (RAID) and DB app-probe credential coverage (1444864). Certifying against unreliable data is meaningless → **DEP-4**.
- **The attribute set is contested (blocking).** The Database managed-attribute slide (5 fields) and the audit dashboard (spike 1480113) overlap on only **3 of 8** fields — the dashboard's two worst gaps (Value Stream 100%, Approval Group ~99.9%) are not on the slide. Certifying off the wrong set makes the KPI and the governance report measure different things → **DEP-3**.
- **Dependent identity.** DB instances are identified in the context of their **host Server** — certification scope inherits whatever server-identity issues exist upstream.

---

## CO6 Acceptance Criteria this feature delivers (Oct 30)

From [[PI-3/pi3-objectives]] — Obj 3 (CO6 §4), Oct 30 gate:

> *Data certification process for **Databases**: end-to-end process documented, technical build to PROD, dashboards live, training delivered.*

"Certified" = all four artifacts present for the Database Instance class:

| Artifact | Delivered by |
|----------|--------------|
| Documented process flow | DB-1 |
| Technical build in PROD | DB-2 |
| Tracking dashboard live | DB-3 |
| Certification cycle executed + monitored | DB-4 |
| Training delivered | DB-5 |

---

## ADO item reconciliation note

Clones the PI-2 BA certification pilot pattern. Reusable story shapes (from the feature breakdown):

| PI-2 pilot item | Shape it provides | Clones to |
|-----------------|-------------------|-----------|
| 1480113 | Database audit-dashboard scope + gap-remediation plan (**anchor**) | Input to DB-1 (see DEP-1) |
| 1480098 | Data Dictionary: Databases (closes CO5 gap G1) | Attribute-set source (DEP-2) |
| 1402976 | Execute certification policies | DB-2 / DB-4 |
| 1402980 | Monitor completeness | DB-4 |
| 1402962 / 1402984 | Kick-off / training / office hours | DB-5 |
| 1402727 | Dashboard | DB-3 |

Stories DB-1 through DB-5 are **net-new** for the Database Instance class — pilot shapes re-scoped to `cmdb_ci_db_instance` (Oracle + MS SQL child classes inherit additively).

---

## Stories (5)

---

### DB-1 · [User Story] Document the Database Data Certification process flow

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517037 |
| Sprint | 3.3 |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones the BA pilot process definition, re-scoped to Database |
| Depends on | DEP-1 (1480113 gap plan), DEP-3 (attribute set), DEP-5 (Class Manager) |
| Tags | `Data-Certification` `Database` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the end-to-end Database data-certification process documented — trigger, attestation steps, roles, escalation, and remediation path — built off the 1480113 gap-remediation plan,
**So that** the certification campaign for the Database Instance class runs on an agreed, repeatable workflow before any PROD configuration is built.

**Acceptance criteria:**
- [ ] Process flow diagram covers the full cycle: campaign trigger → owner attestation → gap identification → remediation → re-attestation → sign-off
- [ ] Roles defined at each step (CI Owner, Technical Owner Group, Support Group, Process Owner) using the delivered Data Dictionary field mappings (`managed_by`, `managed_by_group`, `support_group`)
- [ ] Attested attribute set for Database confirmed against the **reconciled** set (DEP-3) and the 1480113 gap plan — no drift between certification, dictionary, and audit dashboard
- [ ] Process notes the host-Server dependency (Dependent identity) and how a hostless DB is handled
- [ ] Escalation and non-response handling defined
- [ ] Process documented in the agreed location and reviewed with the Database CCB Class Manager, Ray Reuter (DEP-5)
- [ ] Doc-only — no PROD change required

**Dependencies:** DEP-1 (audit spike 1480113 gap plan), DEP-3 (attribute-set reconciliation), DEP-5 (Class Manager confirmation).

---

### DB-2 · [Enabler – Configuration] Build Database certification policies/rules to PROD

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1517037 |
| Sprint | 3.4 |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402976 (execute policies), re-scoped to Database |
| Depends on | DB-1, DEP-2 (Data Dictionary CCB), DEP-3 (attribute set), DEP-4 (data quality) |
| Tags | `Data-Certification` `Database` `Configuration` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the ServiceNow data-certification campaign, filters, and attestation rules for `cmdb_ci_db_instance` configured and deployed to PROD,
**So that** Database CI owners can be issued attestation tasks against the agreed attribute set on a defined schedule.

**Acceptance criteria:**
- [ ] Certification definition/filter created scoping the active `cmdb_ci_db_instance` population (≈3,113; Oracle + MS SQL child classes inherit the parent set additively — DEP-5)
- [ ] Attestation rules configured for the **reconciled** Database managed attribute set per DB-1/DEP-3 (baseline slide set: CI Owner `managed_by`, Technical Owner Group `managed_by_group`, Support Group `support_group`, Environment `environment`, Location `location`)
- [ ] Certification schedule configured (frequency + first run window) and documented
- [ ] Configuration migrated to PROD via a governed update set / change
- [ ] Task routing verified — attestation tasks land with the correct owner group (`managed_by_group` / `support_group`)
- [ ] Dry-run on a bounded owner group confirms tasks generate and complete without error before full launch

**Dependencies:** DB-1, DEP-2 (attribute set locked by CCB), DEP-3 (reconciliation resolved — blocking), DEP-4 (trustworthy data), DEP-5 (active population).

---

### DB-3 · [Enabler – Configuration] Stand up the Database certification tracking dashboard

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1517037 |
| Sprint | 3.4 |
| Owner | Kiran (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402727 (dashboard), re-scoped to Database |
| Depends on | DB-2 |
| Tags | `Data-Certification` `Database` `Dashboard` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** a live tracking dashboard for the Database certification cycle — coverage, attestation status, and outstanding gaps,
**So that** certification progress against the Oct 30 gate is visible to the team and stakeholders without manual reporting.

**Acceptance criteria:**
- [ ] Dashboard shows Database certification coverage: % attested, pending, and overdue against the scoped active population
- [ ] Outstanding-gap view surfaces the attributes driving non-certification (cross-checks the 1480113 audit gaps so remediation is not double-counted — DEP-1)
- [ ] Dashboard reads from the live certification records created by DB-2 (not a static export)
- [ ] Coordinated with the CMDB Health Completeness (Database) config so the two do not build overlapping scoring — see [[cmdb-health-completeness-correctness-stories|CP-3]] (DEP-6)
- [ ] Dashboard reviewed with PO (Joe Dames) and confirmed as the reporting source for the Oct 30 gate
- [ ] Refresh cadence confirmed — scores update on schedule, not stale

**Dependencies:** DB-2 (records must exist to report on), DEP-1 (audit-gap alignment), DEP-6 (CP-3 coordination).

---

### DB-4 · [User Story] Run the Database certification cycle and monitor completeness

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517037 |
| Sprint | 3.5 |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402980 (monitor completeness), re-scoped to Database |
| Depends on | DB-2, DB-3, DEP-4 |
| Tags | `Data-Certification` `Database` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the first Database certification cycle executed end-to-end with completeness monitored on the dashboard,
**So that** attestation is actively driven to the target coverage and the process is proven before the Oct 30 gate.

**Acceptance criteria:**
- [ ] First certification cycle launched to Database CI owners via the DB-2 configuration
- [ ] Attestation progress tracked on the DB-3 dashboard through the cycle
- [ ] Gaps surfaced during attestation routed to remediation per the DB-1 process
- [ ] Coverage reaches the agreed acceptance target for Databases; shortfall documented with cause if target not met (esp. gaps traceable to the Oracle-KY discovery gap — DEP-4)
- [ ] Non-responding owners escalated per the DB-1 escalation path
- [ ] Cycle outcome (coverage %, gaps closed, gaps outstanding) recorded and reviewed at Sprint Review

**Dependencies:** DB-2 (PROD build), DB-3 (dashboard), DEP-4 (trustworthy data — gaps caused by discovery holes are not owner-attestable).

---

### DB-5 · [User Story] Deliver Database certification training to CI owners

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517037 |
| Sprint | 3.5 → 3.6 IP (sign-off) |
| Owner | Joe Dames (PO) / Manuel Vazquez |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402962 (kick-off/training) + 1402984 (office hours), re-scoped to Database |
| Depends on | DB-2, DB-4 |
| Tags | `Data-Certification` `Database` `Training` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** Database CI owners trained on the certification process — how to attest, correct gaps, and use office hours,
**So that** owners can sustain certification independently and the CO6 "training delivered" artifact is satisfied for the Database class.

**Acceptance criteria:**
- [ ] Training material produced covering the Database certification workflow (attest, remediate, re-attest) per DB-1
- [ ] Training delivered to the Database CI owner / support-group audience; attendance or distribution recorded
- [ ] Office-hours / support channel established and communicated
- [ ] Quick-reference (job aid) distributed to owners
- [ ] Training completion evidenced for the Oct 30 gate (session recording, deck, or sign-off log)
- [ ] PO (Joe Dames) confirms the training artifact satisfies the CO6 Database certification acceptance criterion

**Gate note:** build done by end of Sprint 3.5 (Oct 13); training/validation sign-off completes in **3.6 IP (Oct 14–27)** ahead of the Oct 30 external date.

---

## Dependencies (6)

**Work item type:** Dependency · **Linked to:** Feature 1517037 (Blocked By) · **Area path:** A-INFOPS\FY26\PI3

Each dependency is stated as **Problem** (why it blocks) + **Acceptance criteria** (what "resolved" looks like), per SAFe.

---

### DEP-1 · Database audit-dashboard scope + gap-remediation spike (1480113) closed

| Field | Value |
|-------|-------|
| Title | [Dependency] Close Database audit spike 1480113 — Feature 1517037 |
| Assigned To | Stan (confirm) |
| Priority | 1 |
| State | **Open** (PI-2 carryover) — ⚠️ not shown on the ADO PI2.6 view of 2026-07-28; the sibling audit spikes closed (Computer 1480114, Server 1480112) but **1480113's status is unconfirmed** — verify in ADO |
| Due Date | 2026-09-02 |

**Problem:** DB-1 documents the certification process *off the 1480113 gap-remediation plan*, and DB-3's dashboard cross-checks the same audit gaps. If 1480113 has not closed, the Database attribute gap picture is undefined and DB-1 cannot anchor to it.

**Acceptance criteria:**
- [ ] Spike 1480113 completed and its Database gap-remediation plan published
- [ ] Audited Database attribute gaps quantified (incl. Missing Environment ~1,187, Value Stream ~100%, Approval Group ~99.9%) and available as DB-1/DB-3 input
- [ ] Gap plan reviewed with the Database CCB Class Manager, Ray Reuter (links DEP-5)

---

### DEP-2 · Data Dictionary CCB approval — Database attributes (1480098)

| Field | Value |
|-------|-------|
| Title | [Dependency] Data Dictionary CCB approval covering Database attributes — Feature 1517037 |
| Assigned To | Manuel Vazquez / Josh Sterling (CCB Chair) |
| Priority | 1 |
| State | Open (story 1480098 — closes CO5 gap G1) |
| Due Date | 2026-09-02 |

**Problem:** DB-2 configures attestation rules against the Database managed-attribute set. If the Data Dictionary (1480098) is not CCB-approved, the certified attribute list can still change under the team, forcing rework of the PROD build.

**Acceptance criteria:**
- [ ] Data Dictionary CCB approval recorded covering the Database managed attributes and field mappings (`managed_by`, `managed_by_group`, `support_group`, `environment`, `location`)
- [ ] Approved attribute set matches the set configured in DB-2 — no drift
- [ ] Approval date and CCB decision referenced in DB-1 / DB-2

---

### DEP-3 · Reconcile the Database attribute set — audit dashboard vs. dictionary slide (BLOCKING)

| Field | Value |
|-------|-------|
| Title | [Dependency] Reconcile Database attribute set (slide vs audit dashboard) — Feature 1517037 |
| Assigned To | Manuel Vazquez / Ray Reuter |
| Priority | 1 |
| State | Open |
| Due Date | 2026-09-02 |

**Problem:** The Database managed-attribute slide (5 fields) and the 1480113 audit dashboard overlap on only **3 of 8** fields. The dashboard's two largest gaps — Value Stream (`business_unit`, ~100% missing) and Approval Group (~99.9% missing) — are **not** on the slide, while the slide adds Technical Owner Group and Location. If certification is configured off only the slide's 5 attributes, the certification KPI and the governance/audit report will measure different things and disagree at the gate.

**Acceptance criteria:**
- [ ] One authoritative Database certification attribute set agreed with Ray Reuter, reconciling the slide (CI Owner, Technical Owner Group, Support Group, Environment, Location) against the audit dashboard (adds Value Stream, SOX Type, Approval Group)
- [ ] Decision recorded on whether Value Stream / SOX Type / Approval Group join the certified set
- [ ] Reconciled set fed into DEP-2 (dictionary), DB-1, DB-2, and [[cmdb-health-completeness-correctness-stories|CP-3]] so all measure the same thing

---

### DEP-4 · Database discovery data quality — Oracle / Kentucky visibility gap remediated

| Field | Value |
|-------|-------|
| Title | [Dependency] Remediate Oracle-KY DB discovery gap before certification — Feature 1517037 |
| Assigned To | Stan Tomberg (confirm) |
| Priority | 2 |
| State | Open — now tracked in ADO as **Issue 1520824** "Credential Issues impacting Linux\Database(oracle) discovery" (Active); RAID / DB app-probe credential coverage 1444864 |
| Due Date | 2026-09-16 |

**Problem:** Certification attests that CMDB data is correct and current. Database instance data depends on ServiceNow application-probe discovery, which has a known **Oracle / Kentucky authentication/visibility gap** — now tracked as ADO **Issue 1520824** (Active) — plus broader DB credential-coverage risk (1444864). Related infra risk: **Issue 1520799 "MID Server Disruption" (Active)** can interrupt discovery cycles. Certifying against a population where discovery cannot see or refresh instances produces false gaps owners cannot fix, and undermines the certification's validity.

> **Related data-population item:** ADO **1504309 "Database: Populate Environment Attribute" (Ready DoR)** directly remediates the Missing-Environment gap (~1,187) that DB certification measures — track alongside this dependency.

**Acceptance criteria:**
- [ ] Oracle-KY discovery/authentication gap status confirmed — remediated, or the affected population explicitly scoped out of the first certification cycle with rationale
- [ ] DB app-probe credential coverage (1444864) confirmed sufficient for the certified population
- [ ] Any discovery-caused gaps documented and excluded from owner-attributable coverage in DB-4

---

### DEP-5 · Class Manager confirms attribute set + active-population scope

| Field | Value |
|-------|-------|
| Title | [Dependency] Ray Reuter sign-off — Database attribute set + active scope — Feature 1517037 |
| Assigned To | Manuel Vazquez |
| Priority | 2 |
| State | Open |
| Due Date | 2026-09-16 |

**Problem:** DB-2's scoped population (≈3,113 active `cmdb_ci_db_instance`, Oracle + MS SQL children) and the attested attribute set must be ratified by the Database CCB Class Manager (Ray Reuter). Certifying the wrong population or engine scope invalidates the coverage %.

**Acceptance criteria:**
- [ ] Ray Reuter confirms the Database managed-attribute set (post-DEP-3 reconciliation) to be certified
- [ ] Active-population definition (`install_status` / `operational_status`) confirmed so the scored count reconciles to 3,113
- [ ] Engine scope confirmed — which child classes (Oracle `cmdb_ci_db_ora_instance`, MS SQL `cmdb_ci_db_mssql_instance`) are in the first cycle

---

### DEP-6 · Coordinate with CMDB Health Completeness (Database) config — CP-3

| Field | Value |
|-------|-------|
| Title | [Dependency] Align cert dashboard with CMDB Health Completeness CP-3 — Feature 1517037 |
| Assigned To | Manuel Vazquez |
| Priority | 3 |
| State | Open — CP-3 exists in ADO as **US 1520425** (Validation) |
| Due Date | 2026-09-16 |

**Problem:** The CMDB Health **Completeness (Database)** KPI ([[cmdb-health-completeness-correctness-stories|CP-3]] = ADO **1520425**, parent "Governance Validation & Acceptance") scores the same Database attribute population that DB-3's certification dashboard reports on — and CP-3 carries the *same* blocking attribute-set mismatch (DEP-3). Related population story **1504309** (Populate Environment Attribute) feeds the same gap. Building the two independently risks overlapping/contradictory scoring.

**Acceptance criteria:**
- [ ] DB-3 and CP-3 use the single reconciled attribute set from DEP-3
- [ ] Agreement on which artifact is authoritative for "attribute populated" vs "owner attested"
- [ ] No double-counting of the same Database gap; coordination decision recorded (ADO comment) and reflected in DB-3 acceptance

---

## Sequence summary

```
DEP-1 (1480113 gap plan) ─┐
DEP-3 (attr reconcile) ───┤
DEP-5 (Ray — attr + scope)┼─► DB-1 (process flow, 3.3)
DEP-2 (Data Dictionary) ──┘        │
                                   ├─► DB-2 (PROD build, 3.4) ◄── DEP-4 (data quality)
                                   │        │
                                   │        ├─► DB-3 (dashboard, 3.4) ◄── DEP-6 (CP-3 align)
                                   │        │        │
                                   │        └────────┼─► DB-4 (run cycle + monitor, 3.5) ◄── DEP-4
                                   │                 │
                                   │                 └─► DB-5 (training, 3.5 → 3.6 IP)
```

**Gate:** CO6 Oct 30 falls after PI-3 ends (Oct 27). Build done by **end of Sprint 3.5 (Oct 13)**; training/validation completes in **3.6 IP (Oct 14–27)**.
**Critical path:** DEP-3 (attribute reconciliation) is blocking and gates DB-1/DB-2; DEP-4 (Oracle-KY data quality) gates meaningful acceptance in DB-4. Raise both, plus DEP-1/DEP-2 (carryover), at PI Planning.
