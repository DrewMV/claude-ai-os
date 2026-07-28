---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: reference-draft
scope: NON-SOW
updated: 2026-07-28
tags: [work, cmdb-csdm, backlog, quality-governance, cmdb-health, completeness, correctness]
---

# CMDB Health — Completeness & Correctness Configuration Story Drafts (SAFe · NON-SOW)

**7 SAFe-compliant stories** to configure and score two ServiceNow CMDB Health KPIs across the CI classes:
**4 Completeness** (Computer, Server, Database, Business Application) + **3 Correctness** (Computer, Server, Database).
All attribute lists, field names, requirements, identification rules, and CI counts are taken from the **CMDB Data
Dictionary — CCB Review & Approval (CMP Stage 1), delivered to PPL 2026-07-21** — the authoritative reference for this set.

> **Single source of truth.** This file supersedes the earlier split drafts (`cmdb-correctness-configuration-stories`,
> `cmdb-completeness-configuration-stories`) so the two KPIs share one class reference, one parent feature, and one set
> of conventions and cannot drift or contradict.
> 🟠 **NOT a CO5/CO6 SOW deliverable.** Team-added quality governance (same lane as
> [[cmdb-health-lifecycle-validation-stories]]). Requires PM/PO acceptance; does **not** gate a contractual deliverable or holdback.
> **Status: REFERENCE / DRAFT** — Manuel creates the real items in ADO under the correct Epic ▸ Feature and reconciles
> IDs / points / iteration back here (ADO authoritative). Per [[definition-of-ready]], create from the Feature "+" link, never standalone.

## Why 7 and not 8
**Business Application is Completeness-only.** A BA is not a discovered CI — it is identified by Name with no
CI-Class-Manager identification/reconciliation rules — so the Correctness sub-metrics (Duplicate / Orphan / Stale) do
not apply the same way; BA "freshness" is **certification-based**, handled in [[cmdb-health-lifecycle-validation-stories|HL-4]].
Hence 4 Completeness stories but only 3 Correctness stories.

## How these are shaped (SAFe / INVEST)
- Each story is a **vertical, independently acceptable slice** — one CI class, one KPI, sized for a single iteration.
- **Acceptance criteria are testable**: Completeness stories score the configured attribute set; Correctness stories configure the three sub-metrics — each demonstrable on the live CMDB Health dashboard.
- **Story vs Enabler:** both are platform configuration → drafted as **Enabler – Configuration**. If the ART doesn't use the Enabler type, **User Story + "Configuration"/"Quality-Governance" tag** is fine.
- **Customization gate:** completeness/orphan/staleness rules are OOTB CMDB Health configuration → no "Customization" tag expected. If scripted logic is needed, apply the [[requirements-process#Customization Governance|Customization]] gate.
- **Points** left blank — set at refinement. **All stories must satisfy the team [[definition-of-done]].**

---

## CI Class Reference (from attached slides, 2026-07-20)

| Class | Table | CCB Class Manager | Active CIs | Identification rule (duplicate basis) | Discovery source (stale basis) | Orphan (required relationship) |
|---|---|---|---|---|---|---|
| **Computer** | `cmdb_ci_computer` | Monica Green / Paul Becker | 19,901 | **PPL Computers** (Independent) — `Name` + `serial_number` (100) | SG-SCCM / ServiceNow Discovery | TBD — end-user devices are relationship-light (over-flag risk) |
| **Server** | `cmdb_ci_server` | Ray Reuter | 3,917 | **PPL Server** (Independent) — `serial_number` (100) → lookup (200) → `name` (300) | Discovery / SG-SCCM (inherited) | No link to any Application / Business Service |
| **Database Instance** | `cmdb_ci_db_instance` | Ray Reuter | 3,113 | **Database instance rule** (Dependent, host Server) — `serial_number` (100) → `Edition`+`name`+TCP port (200) | ServiceNow app probes | Not hosted on a Server (`Runs on::Runs`) |
| **Business Application** | `cmdb_ci_business_app` | Todd Dierksheide | 2,148 | by **Name** — no CI-Class-Manager rule (not discovered) | n/a — certification-based ([[cmdb-health-lifecycle-validation-stories|HL-4]]) | *(Correctness N/A — completeness only)* |

### Managed attributes → Completeness set (from the delivered CCB dictionary, 2026-07-21)
Completeness is scored on the full managed-attribute set. Per the delivered dictionary every attribute is **Recommended**
except **BA `Name` (Required, identifier)** and **Server `Environment` (Mandatory)**.

| Class | Managed attributes (completeness basis) — field name | Requirement | Audited |
|---|---|---|---|
| **Computer** (9) | Assigned To (`assigned_to`), CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Asset Tag (`asset_tag`), OS (`os`), Location (`location`), IP Address (`ip_address`), Serial Number (`serial_number`) | all Recommended | ESS-02: Assigned To, Location, Serial Number (3/9) |
| **Server** (10) | CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Asset Tag (`asset_tag`), Value Stream (`business_unit`), SOX Type (`u_sox_type`), Data Classification (`classification`), Location (`location`), IP Address (`ip_address`), **Environment (`environment`)** | all Recommended **except Environment = Mandatory** | ESS-02: CI Owner, Location, IP Address (3/9) |
| **Database Instance** (5) | CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Environment (`environment`), Location (`location`) | all Recommended | Proposed: CI Owner, Location (2/5) |
| **Business Application** (10) | Name (`name`, identifier), CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Business Owner (`owned_by`), Approval Group (`u_approval_group`), Support Group (`support_group`), Asset Tag (`asset_tag`), Value Stream/Business Unit (`business_unit`), SOX Type (`u_sox_type`), Data Classification (`data_classification`) | `Name` Required; all others Recommended | Proposed: CI Owner, Data Classification (2/9) |

> **Field-name note (per delivered dictionary):** **all four classes** map **CI Owner → `managed_by`** and **Technical Owner Group → `managed_by_group`** — no class uses `owned_by`/`u_technical_owner_group` for these. BA uses **`owned_by` for _Business Owner_** (a distinct role). "Data Classification" is **`data_classification` on BA** but **`classification` on Server**; "Value Stream" is **`business_unit`** (Server & BA). Use the field names exactly as tabled above.

---

## The two KPIs (definitions we are building to)

**Completeness** — whether the attributes (and relationships) defined **required / recommended** for a class are **populated**. Configured via the completeness metric's required + recommended attribute lists.

**Correctness** — an aggregate of three per-CI data-integrity sub-metrics (it is **not** "are the values accurate"):

| Sub-metric | Measures | Configured via |
|---|---|---|
| **Duplicate** | CIs resolving to the same identity | **Identification Rules** (IRE) |
| **Orphan** | CIs missing a required relationship | **Orphan rules** — manual, one per class; none in base |
| **Stale** | CIs not updated within a defined timeframe | **Staleness rules** |

> Sources: [ServiceNow — Understanding CMDB Health](https://www.servicenow.com/community/itsm-articles/understanding-cmdb-health/ta-p/2307033) · [KB2612771 — Correctness KPI](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2612771).
> The third KPI, **Compliance** (SOX / ESS-02 audit definitions), is out of scope for this set — but the deck's **Audit** column is a Compliance signal, and audited attributes are natural Completeness priorities.
> ⚠️ **Intent to confirm (Joe / Sonika):** if "correctness" is meant as *"are the values valid/right"*, that is **Compliance / data-validation**, a different set. The CR stories below build the ServiceNow **Correctness KPI**.

---

## Parent Feature (draft)

### `[Enabler · Configuration] CMDB Health & Data Quality — KPI Configuration`
- **Feature type:** Enabler – Configuration. Single parent for **Completeness + Correctness** (and, later, Compliance) so the KPIs don't fragment. Consolidates what were two separate feature drafts.
- **Owner / approver:** Product Management (**Sonika Das**) + PO (**Joe Dames**); driven by **Manuel Vazquez** (acting PO-support / SM — *recommended, scoped to this work*).
- **Target iterations:** **PI-3** (aligns to the Aug-2026 Computers/Servers/Network certification expansion and the CO6 Governance Sep-30 gate); baseline config can start late PI-2 (2.5/2.6). **Confirm with Sonika.**
- **Benefit hypothesis:** *If* Completeness and Correctness are configured per class from the agreed managed-attribute set and scored, *then* CMDB population and data-integrity gaps become **measurable against target and auditable** — supporting monthly audit-readiness reporting and trust in incident routing / change approval / reporting — instead of raw "Missing X" and duplicate counts with no target.
- **Feature acceptance criteria:**
  - [ ] Completeness configured & scored for **Computer, Server, Database, Business Application**
  - [ ] Correctness (Duplicate · Orphan · Stale) configured & scored for **Computer, Server, Database**
  - [ ] Each class/KPI score visible on the CMDB Health dashboard / baseline (ties spikes 1436581 / 1470837) vs an agreed target
  - [ ] Attribute sets, orphan rules, and staleness thresholds **confirmed with the CCB Class Manager** per class and recorded
  - [ ] PM (Sonika) accepts targets; PO (Joe) sign-off at Sprint Review; CCB informed (visibility only)
  - [ ] Logged in the quality-governance register; **not** linked to a CO5/CO6 deliverable number
- **WSJF / priority:** **Completeness = Medium-High** (maps to active audit-readiness gap remediation — Location, Assigned To, Classification); **Correctness = Medium** (not holdback-gating; value partly depends on Discovery / Service Mapping maturity). Both behind P0/P1 (Airlift, Service Mapping).
- **Dependencies / risks:**
  - **Orphan sub-metric depends on Service Mapping maturity** — relationships must exist before "orphan" is meaningful (esp. Server). ⚠️ **Service Mapping team lead is currently vacant** (Tanzeel Rehman off the project) — reassignment needed; this dependency is higher-risk until an owner is named.
  - **Stale sub-metric & discovered-attribute completeness depend on Discovery/credential coverage** — DB app-probe coverage risk (1444864) and the **Oracle-KY authentication gap** (RAID) skew Database; offline physical devices skew Computer.
  - **Duplicate sub-metric depends on identifier coverage** — `serial_number` coverage on Servers/Databases (Computer serial coverage already strong).
  - **Attribute-set reconciliation vs audit dashboards** — the audit "Missing X" boxes overlap these KPIs; coordinate ownership with the per-class audit spikes (BA 1480111, Computer 1480114, Server, Database 1480113). **Database has a material set mismatch — see CP-3.**
  - **Field-name confirmation** — resolved by the delivered dictionary (Server Value Stream = `business_unit`, Data Classification = `classification`; `managed_by`/`managed_by_group` on all four classes). Verify the technical field names in the live instance before configuring.
- **Scope / non-goals:** the **Completeness** and **Correctness** KPIs only. **Excludes Compliance** (SOX / ESS-02 audits) and attribute value-validation. Correctness **excludes Business Application** (not discovery-based). Deep lifecycle/staleness policy remains in [[cmdb-health-lifecycle-validation-stories]] (these stories *feed* it).
- **Children:** CP-1..CP-4 (Completeness) + CR-1..CR-3 (Correctness).

## Conventions (apply to all 8 stories)
- **Persona (scoped to these stories only):** "CMDB Configuration Management Process Owner" = **Manuel Vazquez (acting / PO-support)** — pending confirmation. System-of-record Process Owner & CCB Chairperson remains **Josh Sterling**.
- **Target:** working **85–90%** score per class/KPI — *confirm formally with Sonika*; confirm whether targets differ per class.
- **Active records only:** the scored population is **active, non-retired CIs only** — retired / decommissioned CIs are excluded (their completeness is irrelevant). Enforced once in the **CP-0 inclusion rule** (lifecycle condition), so every per-class story scores only active, in-scope CIs. **Match the lifecycle filter to the "active" definition behind the delivered dictionary counts** (Computer 19,901 · Server 3,917 · DB 3,113) so the dashboard reconciles — confirm the exact `install_status` / `operational_status` values with Ray / Stan.
- **Additive inheritance:** completeness config is **inherited and additive**, not replaced. Attributes defined at a parent class (e.g., `cmdb_ci_server`, `cmdb_ci_db_instance`) flow down to child classes automatically; any child-specific attribute **adds to** the inherited set rather than overriding it. Define the common set once at the parent; stack OS/engine-specific attributes at the child.
- **Acceptance lane (non-SOW):** PM **Sonika Das** accepts targets; PO **Joe Dames** sign-off at Sprint Review; CCB **informed** (visibility only). Tag `NON-SOW` / `Quality-Governance`.
- **Staleness threshold `N`** (Correctness) and **orphan rule** (one per class, manual): agreed with the CCB Class Manager — placeholders marked **[confirm]**.
- **Version caveat:** validate KPI mechanics (completeness weighting, sub-metric config, orphan-rule limits) against the **deployed release** — confirm version with Stan (see [[csdm5-terminology]]).

## Story index
_ADO reconciled 2026-07-28 (PI2.6 board). ADO authoritative. Completeness stories created under ADO parent **"Governance Validation & Acceptance"** (not the drafted KPI-config feature — reconcile parent naming). Correctness stories (CR-1/2/3) **not yet in ADO**._

| ID | KPI | CI Class | Type | Priority | CCB Class Mgr | ADO ID | State |
|----|-----|----------|------|----------|---------------|--------|-------|
| CP-0 | Completeness | Dashboard scope (all 4) | Enabler – Configuration | P2 (confirm) | Josh Sterling (CCB Chair) | **1526841** | Ready DoR |
| CP-1 | Completeness | Computer | Enabler – Configuration | P2 (confirm) | Monica Green / Paul Becker | **1520415** ⚠️ (poss. dup **1526839**, New) | Ready DoR |
| CP-2 | Completeness | Server | Enabler – Configuration | P2 (confirm) | Ray Reuter | **1520424** | Validation |
| CP-3 | Completeness | Database | Enabler – Configuration | P2 (confirm) | Ray Reuter | **1520425** | Validation |
| CP-4 | Completeness | Business Application | Enabler – Configuration | P2 (confirm) | Todd Dierksheide | **1520414** | Validation |
| CR-1 | Correctness | Computer | Enabler – Configuration | P3 (confirm) | Monica Green / Paul Becker | _(not yet in ADO)_ | Draft |
| CR-2 | Correctness | Server | Enabler – Configuration | P3 (confirm) | Ray Reuter | _(not yet in ADO)_ | Draft |
| CR-3 | Correctness | Database | Enabler – Configuration | P3 (confirm) | Ray Reuter | _(not yet in ADO)_ | Draft |

> **ADO reconciliation notes (PI2.6, 2026-07-28):**
> - **CP-1 duplicate to resolve** — two "Completeness for Computer" stories exist: **1520415** (Ready DoR) and **1526839** (New), both under Governance Validation & Acceptance. Confirm which is authoritative / whether one should be removed.
> - **Related server `environment` spike is now created** — ADO **Spike 1526856** "Validate Server environment Integration Source Behind the Mandatory Designation" (New) = [[server-environment-mandatory-spike]]. Feeds **CP-2** (Server Mandatory `environment`).
> - **DB discovery data-quality issue is now tracked** — ADO **Issue 1520824** "Credential Issues impacting Linux\\Database(oracle) discovery" (Active) = the Oracle-KY gap bounding **CP-3** completeness. Also **Issue 1520799** "MID Server Disruption" (Active) may affect discovered-attribute freshness.
> - **Progress since draft** — CP-2/CP-3/CP-4 are in **Validation**; CP-0/CP-1 in **Ready DoR**.

---

# Completeness stories

## CP-0 — Scope the CMDB Health Dashboard to the managed classes (Completeness view)
- **Type:** Enabler – Configuration (NON-SOW) · **Priority:** P2 *(confirm)* · **Scope:** CMDB Health Dashboard scoping — one base-level inclusion rule + view config. **Short-term** noise-reduction measure (not a governance program).
- **Intent:** keep the CMDB Health Dashboard **clean from noise** — reporting only the currently managed CI classes — while the managed-class list is still growing. As new classes are onboarded, they are **added to the same rule's class list**; this story does not build ongoing scope-governance.
- **User Story:**
  - **As the** CMDB Configuration Management Process Owner,
  - **I want** the CMDB Health Dashboard scoped — via a single inclusion rule at the base `cmdb_ci` level — to only the currently managed CI classes, showing the **Completeness** KPI,
  - **So that** stakeholders see a focused completeness picture free of noise from unmanaged classes.
- **Solution guidance (approach):**
  - **Single base-level inclusion rule.** Anchor one CMDB Health inclusion rule on the base table **`cmdb_ci`** and filter by the class attribute. `sys_class_name` is a field on `cmdb_ci` inherited by every CI class, so filtering by it at the base level returns **exact-class** matches — no per-class rules needed:
    ```
    Anchor: cmdb_ci
    Condition: sys_class_name IN (
      cmdb_ci_computer,          -- Computer, exact class (servers auto-excluded)
      cmdb_ci_win_server,        -- Windows Server
      cmdb_ci_linux_server,      -- Linux Server
      cmdb_ci_db_ora_instance,   -- Oracle Instance      (confirm exact name)
      cmdb_ci_db_mssql_instance, -- MS SQL Instance       (confirm exact name)
      cmdb_ci_business_app       -- Business Application
    )
    AND install_status != Retired          -- active records only
    [AND operational_status = Operational] -- optional tightening; confirm
    ```
  - **Why exact-class (`= class`), not "is a":** each CI's `sys_class_name` holds its own leaf class, so an `IN` list of exact class names captures precisely those classes and nothing beneath them — this is what keeps Server out of Computer, and scopes DB to Oracle/MS SQL only.
  - **Active records only:** the same rule carries the **lifecycle filter** — retired / decommissioned CIs are excluded so the score reflects only CIs we care about. Match the exact `install_status` / `operational_status` values to the "active" definition behind the delivered-dictionary counts (confirm with Ray / Stan).
  - **Maintenance:** to add a newly managed class, append its `sys_class_name` to the `IN` list — no new rule, no new story.
- **Acceptance criteria:**
  - [ ] **Single base-level inclusion rule** created on `cmdb_ci` with `sys_class_name IN (…)` = the six exact classes above, **plus a lifecycle filter excluding retired/decommissioned CIs** (active records only); dashboard scored population resolves to active CIs of those classes only, and reconciles to the dictionary "active" counts.
  - [ ] **Completeness is the only KPI configured** for these classes — Correctness (Duplicate/Orphan/Stale) and Compliance are **not configured**, so they read empty/N-A for this scope. **Do not disable the platform-wide Correctness/Compliance scheduled jobs** (that would affect other classes/teams). *Whether the empty panels can be removed from the dashboard view is a display question — validate against the deployed release with Stan; the OOB CMDB Health dashboard may not offer a per-KPI hide.*
  - [ ] **Health jobs running** — the CMDB Health **Completeness** scoring / dashboard data-collection scheduled jobs are enabled and completing without error, and the six classes' scores refresh on cadence (not stale/zero).
  - [ ] **One-time noise spot-check** — confirm no out-of-scope class still shows a score; if one does, a pre-existing broader inclusion rule is the cause → disable that one rule. *(No full audit / governance register — short-term measure.)*
  - [ ] **Accepted-gap note recorded** (deliberately excluded): bare `cmdb_ci_server` + other-OS servers (ESX/Unix/AIX); any Computer subclasses; bare `cmdb_ci_db_instance` + other DB engines (DB2/MySQL/…); all classes not in the list.
  - [ ] PM (Sonika) accepts; PO (Joe) sign-off; CCB informed; logged in quality register. Team [[definition-of-done]] met.
- **Notes:** Validate the inclusion-rule mechanics against the deployed release with **Stan** — confirm the CMDB Health config surface allows anchoring at `cmdb_ci` with a `sys_class_name` condition (normally yes; inclusion rules are table + filter), and confirm the exact Oracle / MS SQL child-class names. Dashboard-scored counts will be **narrower than the delivered-dictionary parent-class totals** (Computer 19,901 · Server 3,917 · DB 3,113) because scoping is by exact class — reconcile expectations when reading the numbers. Depends on CIs actually being classified at these leaf classes (Discovery/SCCM usually ensures this). This story owns dashboard scope only; per-class attribute configuration is CP-1..CP-4.

## CP-1 — Configure CMDB Health Completeness: Computer (Physical/Virtual)
- **Type:** Enabler – Configuration (NON-SOW) · **Priority:** P2 *(confirm)* · **Scope:** `cmdb_ci_computer` — 19,901 active (confirm full-population vs Physical/Virtual split).
- **User Story:**
  - **As the** CMDB Configuration Management Process Owner,
  - **I want** the CMDB Health **Completeness** KPI configured from the Computer managed attributes and scored,
  - **So that** computer population gaps are measurable against target and feed audit-readiness reporting.
- **Acceptance criteria:**
  - [ ] **Managed attribute set configured** as the completeness basis (all Recommended per delivered dictionary): Assigned To (`assigned_to`), CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Asset Tag (`asset_tag`), OS (`os`), Location (`location`), IP Address (`ip_address`), Serial Number (`serial_number`).
  - [ ] **Completeness scored** for `cmdb_ci_computer`; baseline captured vs target (85–90%, confirm).
  - [ ] Score cross-checks the Computer audit dashboard gaps (Missing CI Owner, Assigned To empty, Location empty, Missing IP) — coordinated with spike **1480114** so remediation isn't double-counted.
  - [ ] Any **required relationships** for completeness defined (or explicitly none).
  - [ ] PM (Sonika) accepts target; PO (Joe) sign-off; CCB informed; logged in quality register. Team [[definition-of-done]] met.
- **Notes:** ESS-02-audited attributes (Assigned To, Location, Serial Number) are natural completeness priorities. Location gap has a documented HR-system root cause; offline physical devices limit discovered-attribute population.

## CP-2 — Configure CMDB Health Completeness: Server (Windows/Linux)
- **Type:** Enabler – Configuration (NON-SOW) · **Priority:** P2 *(confirm)* · **Scope:** `cmdb_ci_server` — 3,917 active.
- **User Story:**
  - **As the** CMDB Configuration Management Process Owner,
  - **I want** the CMDB Health **Completeness** KPI configured from the Server managed attributes and scored,
  - **So that** server population gaps are measurable against target and audit-readiness on the server class is sustained.
- **Acceptance criteria:**
  - [ ] **Managed attribute set configured at the `cmdb_ci_server` parent level** per delivered dictionary — **Environment (`environment`) is Mandatory**; all others Recommended: CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Asset Tag (`asset_tag`), Value Stream (`business_unit`), SOX Type (`u_sox_type`), Data Classification (`classification`), Location (`location`), IP Address (`ip_address`). **Windows/Linux inherit this set additively** (see below).
  - [ ] **Completeness scored** for the in-scope active servers (Windows + Linux per CP-0); baseline vs target (85–90%, confirm).
  - [ ] Score reflects recent remediation (Location 44%→100%, IP 43%→91%) and coordinates with the Servers audit spike ([[audit-dashboard-servers-spike]]).
  - [ ] Requirement designations (Environment Mandatory; rest Recommended) confirmed by **Ray Reuter** at CCB.
  - [ ] Any **required relationships** defined (or explicitly none).
  - [ ] PM (Sonika) accepts target; PO (Joe) sign-off; CCB informed; logged in quality register. Team [[definition-of-done]] met.
- **Notes:** Per the delivered dictionary, Server carries a single **Mandatory** attribute (Environment); the rest are Recommended. It is already audit-ready on its ESS-02 attributes (CI Owner, Location, IP Address) — this formalizes and monitors that against target. **Additive inheritance:** configure this set once at `cmdb_ci_server`; `cmdb_ci_win_server` and `cmdb_ci_linux_server` inherit it automatically. The delivered dictionary names **no** Windows- or Linux-specific attributes, so there is nothing to add at the child level today — any future OS-specific attribute stacks additively at the child class and would need CCB (Ray Reuter) ratification as a dictionary addition. Population scoping (Win/Linux, active only) is CP-0; this story defines the attribute set only.

## CP-3 — Configure CMDB Health Completeness: Database Instance
- **Type:** Enabler – Configuration (NON-SOW) · **Priority:** P2 *(confirm)* · **Scope:** `cmdb_ci_db_instance` — 3,113 active (child classes Oracle / MS SQL inherit).
- **User Story:**
  - **As the** CMDB Configuration Management Process Owner,
  - **I want** the CMDB Health **Completeness** KPI configured from the Database managed attributes and scored,
  - **So that** database population gaps are measurable against target.
- **Acceptance criteria:**
  - [ ] **Managed attribute set configured at the `cmdb_ci_db_instance` parent level** (all Recommended per delivered dictionary), using delivered field names: CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Environment (`environment`), Location (`location`). **Oracle / MS SQL inherit this set additively** (see notes).
  - [ ] **Completeness scored** for the in-scope active DB instances (Oracle + MS SQL per CP-0); baseline vs target (85–90%, confirm).
  - [ ] **Reconcile the attribute set with the audit dashboard first (blocking)** — agree one authoritative Database attribute set with Ray Reuter so Completeness and the audit dashboard don't measure different things (see mismatch table).
  - [ ] Any **required relationships** defined (e.g., hosted-on Server) or explicitly none.
  - [ ] PM (Sonika) accepts target; PO (Joe) sign-off; CCB informed; logged in quality register. Team [[definition-of-done]] met.

**CP-3 attribute mismatch — Database audit dashboard (spike 1480113) vs. managed-attribute slide.** Overlap on only 3 of 8 fields — reconcile before configuring:

| Attribute | On slide? | Slide Audit | On audit dashboard? | Dashboard gap |
|---|---|---|---|---|
| CI Owner (`managed_by`) | ✓ | T | ✓ Missing CI Owner | 10 |
| Support Group | ✓ | F | ✓ Missing Support Group | 15 |
| Environment | ✓ | F | ✓ Missing Environment | 1,187 |
| Technical Owner Group (`managed_by_group`) | ✓ | F | ✗ not audited | — |
| Location | ✓ | **T** | ✗ not audited | — |
| Value Stream (Business Unit) | ✗ **not on slide** | — | ✓ Missing Value Stream | 3,113 (100%) |
| SOX Type | ✗ **not on slide** | — | ✓ SOX Type is Empty | 75 |
| Approval Group | ✗ **not on slide** | — | ✓ Missing Approval Group | 3,110 (~99.9%) |

> The dashboard's two worst gaps (Value Stream 100%, Approval Group ~99.9%) are **not** managed attributes on the slide; the slide's Location is flagged audited (`T`) but has no dashboard box. Configuring off only the 5 slide attributes would make the KPI and the governance report measure different things.

- **Notes:** DB uses the `managed_by` / `managed_by_group` mapping. Discovered-attribute completeness is bounded by DB discovery coverage (credential risk 1444864; Oracle-KY gap); ownership fields are manual / Data-Cert populated. **Additive inheritance:** configure this set once at `cmdb_ci_db_instance`; the scored child classes `cmdb_ci_db_ora_instance` (Oracle) and `cmdb_ci_db_mssql_instance` (MS SQL) inherit it automatically, and any engine-specific attribute stacks additively at the child. **Scope note:** per CP-0 the dashboard scores only **Oracle + MS SQL** active instances — a subset of the 3,113 `cmdb_ci_db_instance` population; bare-parent and other-engine instances are out.

## CP-4 — Configure CMDB Health Completeness: Business Application
- **Type:** Enabler – Configuration (NON-SOW) · **Priority:** P2 *(confirm)* · **Scope:** `cmdb_ci_business_app` — 2,148 records.
- **User Story:**
  - **As the** CMDB Configuration Management Process Owner,
  - **I want** the CMDB Health **Completeness** KPI configured from the Business Application managed attributes and scored,
  - **So that** BA population gaps (the largest audit-readiness gaps) are measurable against target — despite BAs not being discoverable.
- **Acceptance criteria:**
  - [ ] **Managed attribute set configured** (`Name` Required/identifier; all others Recommended per delivered dictionary), using delivered field names: CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Business Owner (`owned_by`), Approval Group (`u_approval_group`), Support Group (`support_group`), Asset Tag (`asset_tag`), Value Stream/Business Unit (`business_unit`), SOX Type (`u_sox_type`), Data Classification (`data_classification`).
  - [ ] **Completeness scored** for `cmdb_ci_business_app`; baseline vs target (85–90%, confirm) — population is **manual / Data-Certification sourced**, not Discovery.
  - [ ] Coordinated with the BA audit spike (**1480111**). **Reconcile one gap:** the BA audit dashboard also audits **Missing Recovery Tier (1,820)**, which is **not** on the BA managed-attribute slide — confirm whether Recovery Tier joins the completeness set (see note).
  - [ ] Approved by **Todd Dierksheide** (CCB Class Manager, Business Application).
  - [ ] PM (Sonika) accepts target; PO (Joe) sign-off; CCB informed; logged in quality register. Team [[definition-of-done]] met.
- **Notes:** BA slide (9 managed attributes) matches the BA audit dashboard on **9 of 10** audits — only **Recovery Tier** is audited-but-not-tabled (contrast the larger Database mismatch in CP-3). Respect the **BA enhancement pause (6/10)**: mass BA edits are logged as stories, not done inline. Ties to Data Certification (SOW 1.2), CO5 1.1c ([[co5-governance-validation-stories]]), and the BA data-population cluster (1475582 / 1475584 / 1475585 / 1478286 / 1474892). This is the completeness counterpart to [[cmdb-health-lifecycle-validation-stories|HL-4]] (which covers BA certification-based lifecycle/staleness).

---

# Correctness stories

## CR-1 — Configure CMDB Health Correctness: Computer (Physical/Virtual)
- **Type:** Enabler – Configuration (NON-SOW) · **Priority:** P3 *(confirm)* · **Scope:** `cmdb_ci_computer` — 19,901 active (confirm full-population vs Physical/Virtual split).
- **User Story:**
  - **As the** CMDB Configuration Management Process Owner,
  - **I want** the CMDB Health **Correctness** KPI (Duplicate · Orphan · Stale) configured and scored for the **Computer** class,
  - **So that** computer data integrity is measurable against target and remediation is targeted rather than a raw gap count.
- **Acceptance criteria:**
  - [ ] **Duplicate** sub-metric active and scored using the **PPL Computers** identification rule (`Name` + `serial_number`, Pri 100); duplicate set reviewed and routed to the de-duplication / CI remediation task. *(Serial coverage strong — validate `Name` uniqueness.)*
  - [ ] **Orphan** rule defined and agreed with CCB Class Managers. **Risk:** many end-user computers legitimately have no relationships → naive rule over-flags; record what makes a Computer a non-orphan (or exempt Computer from the orphan sub-metric).
  - [ ] **Stale** rule set — Computer not updated by SCCM/Discovery within **N days** *([confirm], e.g. 30/45)* is flagged. **Risk:** offline physical devices skew staleness (SCCM precedence 1348712/716/717; retired-computer 1402790). Stale CIs feed lifecycle (HL-2).
  - [ ] Computer Correctness score visible on the dashboard / baseline (ties 1436581 / 1470837), scored vs target (85–90%, confirm).
  - [ ] PM (Sonika) accepts target; PO (Joe) sign-off; CCB informed; logged in quality register. Team [[definition-of-done]] met.
- **Notes:** Coordinate with the Computer audit spike (1480114) so correctness config and audit-gap remediation don't double-count.

## CR-2 — Configure CMDB Health Correctness: Server (Windows/Linux)
- **Type:** Enabler – Configuration (NON-SOW) · **Priority:** P3 *(confirm)* · **Scope:** `cmdb_ci_server` — 3,917 active.
- **User Story:**
  - **As the** CMDB Configuration Management Process Owner,
  - **I want** the CMDB Health **Correctness** KPI (Duplicate · Orphan · Stale) configured and scored for the **Server** class,
  - **So that** server data integrity is measurable against target and remediation is targeted.
- **Acceptance criteria:**
  - [ ] **Duplicate** sub-metric active and scored using the **PPL Server** identification rule — `serial_number` (100) → serial lookup (200) → `name` (300). **Note:** `serial_number` is the primary identifier though it is **not** in the Server managed-attribute set — validate serial coverage; low coverage inflates duplicates. Duplicate set reviewed and remediated.
  - [ ] **Orphan** rule = a Server with **no relationship to any Application / Business Service**, agreed with **Ray Reuter**. Score expected to improve as **Service Mapping (P1)** builds relationships *(lead currently vacant — see risks)*.
  - [ ] **Stale** rule — Server not seen by Discovery / SG-SCCM within **N days** *([confirm])* is flagged (reconciliation inherited from the Computer/Hardware hierarchy). Stale CIs feed lifecycle (HL-1).
  - [ ] Server Correctness score visible on the dashboard / baseline, scored vs target (85–90%, confirm). *(Distinct from the Server Compliance/Completeness audit-ready milestone.)*
  - [ ] PM (Sonika) accepts target; PO (Joe) sign-off; CCB informed; logged in quality register. Team [[definition-of-done]] met.
- **Notes:** Coordinate with the Servers audit spike ([[audit-dashboard-servers-spike]]). Orphan sub-metric is the one most affected by Service Mapping progress.

## CR-3 — Configure CMDB Health Correctness: Database Instance
- **Type:** Enabler – Configuration (NON-SOW) · **Priority:** P3 *(confirm)* · **Scope:** `cmdb_ci_database` — 3,113 active (child classes Oracle / MS SQL add engine-specific rules).
- **User Story:**
  - **As the** CMDB Configuration Management Process Owner,
  - **I want** the CMDB Health **Correctness** KPI (Duplicate · Orphan · Stale) configured and scored for the **Database Instance** class,
  - **So that** database data integrity is measurable against target and remediation is targeted.
- **Acceptance criteria:**
  - [ ] **Duplicate** sub-metric active and scored using the **Database instance rule** — `serial_number` (100) → `Edition` + `name` + TCP port(s) (200). **Note:** the rule is **Dependent** — identified in the context of its **host Server**, so duplicate detection is only as correct as host-server identity; validate `Edition`/`name`/TCP port populated (identifier attributes, not the governance managed attributes). Duplicate set reviewed and remediated.
  - [ ] **Orphan** rule = a Database Instance **not hosted on a Server** (`Runs on::Runs` absent), agreed with **Ray Reuter**. A hostless DB is both an identity and orphan problem; expect orphans where Discovery can't authenticate to the host (**Oracle-KY gap**, RAID).
  - [ ] **Stale** rule — Database not seen by ServiceNow **application probes** within **N days** *([confirm])* is flagged. **Dependency:** only as good as DB discovery coverage (credential risk 1444864; enhanced DB discovery D2.3; Oracle-KY gap). Stale CIs feed lifecycle (HL-3).
  - [ ] Database Correctness score visible on the dashboard / baseline, scored vs target (85–90%, confirm).
  - [ ] PM (Sonika) accepts target; PO (Joe) sign-off; CCB informed; logged in quality register. Team [[definition-of-done]] met.
- **Notes:** Coordinate with the Database audit spike ([[audit-dashboard-database-spike]]). Confirm whether Correctness is scored at the `cmdb_ci_database` parent or per child class (Oracle / MS SQL).

---

## Consistency check (across all 7)
- **CI counts** are the slide figures, used identically in both KPIs: Computer 19,901 · Server 3,917 · Database 3,113 · BA 2,148.
- **Field names** (per delivered dictionary): **all four classes** use `managed_by` / `managed_by_group` for CI Owner / Technical Owner Group; BA `owned_by` = Business Owner. Data Classification = `data_classification` (BA) vs `classification` (Server); Value Stream = `business_unit` (Server, BA).
- **Persona, target (85–90%), acceptance lane, parent feature** are defined once and apply to all 7.
- **BA appears in Completeness only** (CP-4); it is deliberately absent from Correctness (not discovery-based).
- **Correctness identifier attributes** (Computer `Name`+`serial_number`; Server `serial_number`→lookup→`name`; Database `serial_number`→`Edition`+`name`+TCP) match the CI Class Reference table above.

## To confirm before creating in ADO
- **Intent** — CR stories build the ServiceNow **Correctness KPI** (Duplicate/Orphan/Stale), not value-validation (which is Compliance). *(Joe / Sonika)*
- **Target** — 85–90% per class/KPI, or different; and recommended-attribute weighting in the deployed release. *(Sonika)*
- **Database attribute set (blocking, CP-3)** — reconcile the 5 slide attributes vs the 6 audit-dashboard audits (dashboard adds Value Stream / SOX Type / Approval Group; slide adds Technical Owner Group / Location). *(Ray Reuter)*
- **BA Recovery Tier (CP-4)** — does it join the BA completeness set? *(Todd Dierksheide)*
- **Field names** — resolved by the delivered dictionary (Server Value Stream = `business_unit`, Data Classification = `classification`, Environment = `environment`; `managed_by`/`managed_by_group` on all four classes). Still verify these technical field names in the live instance before configuring.
- **Staleness `N`** per class + **orphan rule** definitions (Computer over-flag risk); **Service Mapping lead reassignment** (orphan dependency).
- **Computer scope** — full population vs Physical/Virtual split.
- **Parent feature & Enabler type** — single *CMDB Health & Data Quality* parent; Enabler type vs User Story + tag.
- **Reconcile with HL-1/2/3/4** so their bundled "Completeness/Correctness KPI" ACs point to these stories rather than duplicating.

_When the real ADO items exist, add IDs / points / iteration to the Story index and reconcile against [[cmdb-health-lifecycle-validation-stories]]._
