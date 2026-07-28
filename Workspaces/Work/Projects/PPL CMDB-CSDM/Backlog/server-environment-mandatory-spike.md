---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: reference-draft
scope: NON-SOW
updated: 2026-07-28
tags: [work, cmdb-csdm, backlog, quality-governance, spike, enabler, data-dictionary]
---

# Enabler (Spike) — Validate Server `environment` Integration Source Behind the Mandatory Designation

> **Status: CREATED IN ADO (PI2.6, 2026-07-28).** Now exists as **Spike 1526856** "CMDB SPIKE: Validate Server environment Integration Source Behind the Mandatory Designation" — State **New**, parent **"Governance Validation & Acceptance"**. This file remains the working reference (ADO authoritative); reconcile points/iteration/findings back here. Feeds [[cmdb-health-completeness-correctness-stories|CP-2]] and is DEP-7 of Servers certification [[pi3-cert-1517032-certify-servers-stories-dependencies]].
> **Scope:** the **`environment` attribute on the Server class (`cmdb_ci_server`) only.** Not the Service Instance class, not other Server attributes.

---

## SAFe Enabler summary

| Field | Value |
|---|---|
| **Enabler Type** | Exploration (Spike) |
| **Parent Feature** | **Governance Validation & Acceptance** (per ADO Spike 1526856) — was drafted under the CMDB Health & Data Quality KPI feature; ADO placed it here |
| **Team** | CMDB-CSDM |
| **Iteration** | PI-2 · Iter 2.6 *(confirm; may slip to early PI-3)* |
| **Timebox** | Small — [confirm] pts *(hard timebox; investigation only — no configuration changes made)* |
| **Owner** | Stan Tomberg (technical trace) w/ Ray Reuter (requestor) *(confirm)* |
| **Priority / WSJF** | Behind P0/P1 (Airlift, Service Mapping) |
| **Tags** | `Enabler` `Spike` `Quality-Governance` `NON-SOW` |

## Spike statement (the research goal)
**As** the CMDB Configuration Management Process Owner,
**I want** to determine whether the Server class attribute `environment` (`cmdb_ci_server.environment`) is populated by an existing integration (SCCM or other) — and if so, its coverage and forward reliability —
**So that** the CCB's Mandatory ruling on Server `environment` is either substantiated (integration-fed and enforceable) or revisited (manual / non-discoverable → Recommended).

## Context / problem
The delivered CMDB Data Dictionary (CCB, 2026-07-21) records `environment` as the **only Mandatory** managed attribute on `cmdb_ci_server` — all nine other Server managed attributes are Recommended. Ray Reuter (CCB Class Manager, Servers) drove the designation, believing the value arrives via an existing integration (he suspects **SCCM**).

Three facts about the Server attribute need reconciling with that belief before it is enforced:
- **`environment` is normally non-discoverable** — a business/governance attribute describing *how a server is used*, not something a hardware-inventory tool measures. On its face a weak Mandatory candidate.
- **The delivered Server slide names no source** — `environment` is marked Mandatory, Audit = F, but (unlike IP/OS/hardware attributes) no source of truth is cited for it; SG-SCCM and ServiceNow Discovery are cited only for hardware, asset, ownership, IP, MAC and OS.
- **Coverage is low** — the Servers audit dashboard reports **Missing Environment = 11,665**. A reliable integration source would not leave that many blank.

## Hypotheses under test
- **H1 (Ray's):** `cmdb_ci_server.environment` is populated by an existing integration → Mandatory is substantiated.
- **H0 (null):** it is manually / certification-populated (non-discoverable) → current coverage is manual, and Mandatory-as-enforced would break inserts or block CI creation.

## "Mandatory" — resolve first (Task 1)
The delivered "Requirement" column uses Required / Recommended / **Mandatory** as governance designations (feeding completeness scoring). Whether the CCB also intends to **enforce** `environment` as a save-time constraint is a separate, higher-risk question:

| Interpretation | Mechanism | Effect | Risk |
|---|---|---|---|
| **(a) Requirement designation** | Dictionary "Mandatory" flag → CMDB Health completeness weighting | Scoring only — counts against the Server score if blank | Low / non-breaking |
| **(b) Enforced field constraint** | `mandatory=true` dictionary attr, UI policy, or data policy on `cmdb_ci_server` | Server record **cannot be saved** without a value | **Can fail integration/Discovery inserts and block manual server creation** |

## Investigation tasks (Server `environment` only)
1. **Clarify the "Mandatory" definition** with Ray / CCB (table above) — designation vs enforced constraint. Frames everything below.
2. **Baseline population.** Query active `cmdb_ci_server`: count `environment` populated vs empty; report %. **Reconcile the active-server count** — delivered dictionary shows **3,917**, the audit dashboard scopes **15,218** (Missing Environment 11,665); establish which `install_status` / `operational_status` filter each uses (Stan / Ray) so the baseline is unambiguous.
3. **Value quality.** Group populated Server records by `environment` value; validate against the allowed choice list (Prod / QA / Dev / Test); flag free-text drift or invalid values.
4. **Lineage trace (core task).** For a representative sample of populated servers, determine *how the value got there*:
   - `sys_audit` history on `cmdb_ci_server.environment` — set by a person, a system/integration account, or Discovery?
   - `sys_created_by` / `sys_updated_by`; whether the record arrived via an **import set** (`sys_import_set_row` / data source) or **ServiceNow Discovery** (identification/reconciliation).
   - Search **transform maps / robust transforms / IntegrationHub flows** for any field mapping targeting `cmdb_ci_server.environment`.
5. **Confirm/deny the SCCM hypothesis.** Does the SG-SCCM connector carry an environment-like attribute (e.g. a device-collection → environment mapping) that writes `cmdb_ci_server.environment`? If yes, document the mapping; if no, state SCCM is not the source.
6. **Coverage & forward reliability.** If an integration writes it: all in-scope servers or a subset (e.g. only SCCM-managed Windows, not Linux / vCenter-only)? Does it populate on **new** server inserts and on updates, and on what cadence? Determines whether ~100% coverage is achievable going forward.
7. **Enforcement-impact analysis** (only if interpretation (b) is intended): would enforced-Mandatory fail integration/Discovery inserts that omit `environment` (check data-policy "apply to import" behavior) and block manual server creation? Size the legacy blank backlog needing backfill.

## Acceptance criteria
- [ ] **"Mandatory" interpretation (a vs b)** confirmed with Ray / CCB.
- [ ] **Baseline population %** established against a reconciled active-server count (3,917 vs 15,218 explained).
- [ ] **Source of `cmdb_ci_server.environment` identified with evidence** (audit records, transform-map name, or "manual / not integration-sourced"); **SCCM hypothesis explicitly confirmed or denied**.
- [ ] **Coverage documented** — all servers vs subset; new-insert behavior.
- [ ] **Value validity** checked against the Prod/QA/Dev/Test choice list.
- [ ] **Enforcement impact assessed** (if (b)) — insert/creation breakage and backfill sized.
- [ ] **Recommendation delivered to CCB** — one of the outcomes below; delivered dictionary and [[cmdb-health-completeness-correctness-stories|CP-2]] updated to match.
- [ ] PM (Sonika) / PO (Joe) informed; CCB decision recorded. Team [[definition-of-done]] met.

## Possible outcomes / recommendation
- **A — Integration reliably supplies ~100% (incl. new inserts):** Mandatory substantiated. Backfill legacy blanks; confirm enforcement mode won't break the pipeline.
- **B — Integration supplies only a subset / unreliably, or not integration-sourced:** downgrade to **Recommended**, **or** enforce Mandatory **on manual create only** (UI policy, exempt imports), **or** conditional-Mandatory by sub-class where a source exists.

## Outcome / deliverable
A short findings write-up stating: (1) the confirmed **source** of `cmdb_ci_server.environment` with evidence; (2) **coverage** now and for new inserts against the reconciled baseline; (3) a **recommendation** (A / B) including the intended **enforcement mode** and any backfill; (4) reconciliation back to the delivered dictionary and CP-2.

## Dependencies / who
- **Ray Reuter** — requestor & CCB Class Manager (Servers); owns the Mandatory ruling and the "integration source" belief.
- **Stan Tomberg** — CMDB Discovery / integration SME; natural technical owner for the lineage trace **[confirm owner]**.
- **Delivered CCB dictionary** (Slide 7, Server) and [[cmdb-health-completeness-correctness-stories|CP-2]] — the artifacts this spike validates.
- **Audit-dashboard reconciliation** — Missing Environment 11,665 vs the completeness baseline; coordinate with [[audit-dashboard-servers-spike]].

## To confirm before creating in ADO
- **"Mandatory" definition** — designation vs enforced constraint (drives everything).
- **Owner** — Stan (technical) with Ray (requestor) input; or Tony, consistent with the audit spikes.
- **Iteration / points** — Iter 2.6 vs early PI-3; timebox size.
- **Parent Feature** — CMDB Data Dictionary / CMP governance feature, or the [[cmdb-health-completeness-correctness-stories|CMDB Health & Data Quality]] parent.
