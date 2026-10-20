---
type: configuration-record
workspace: Work
project: CMDB-CSDM
status: draft
updated: 2026-10-20
tags: [work, cmdb-csdm, governance, data-definitions]
---

# Business Application — Data Certification Policy (Data Manager) · As-Configured

> **Scope:** Configuration tracking record for the **Data Certification for Business App** policy in ServiceNow Data Manager. Certification only — no validation/remediation policy is in scope here.
>
> **Source:** DEV instance screenshots, captured 2026-10-20 (Manuel). **PROD not verified** — the DEV build could not be compared against PROD directly. Every panel below carries a `PROD verified` column to close as confirmation arrives.
>
> **Related:** [[configuration-management-plan-stage1]] (BA attribute dictionary) · [[ownership-terminology-mapping]] (CI Owner / `managed_by` conflict) · [[Backlog/audit-dashboard-accuracy-spike]] (BA gap counts).

---

## Panel 1 — General information

| Setting | Value (DEV, 2026-10-20) | PROD verified |
|---|---|---|
| Name | Data Certification for Business App | ☐ |
| Description | Data Certification for Business App | ☐ |
| Policy type | Certification | ☐ |

## Panel 2 — Data Filter

| Setting | Value (DEV, 2026-10-20) | PROD verified |
|---|---|---|
| Table | Business Application (`cmdb_ci_business_app`) | ☐ |
| Filter | Operational status **!=** Retired **AND** Class **=** Business Application | ☐ |
| Included records | 2,254 | ☐ |

> **Scope note:** the governed "Active Business Application" population on the BA audit dashboard is **2,135**. The 119-record delta is unreconciled — part DEV clone drift, possibly part filter-definition difference. Do not use 2,254 for capacity planning.

## Panel 3 — Assignment

| Setting | Value (DEV, 2026-10-20) | PROD verified |
|---|---|---|
| Assignment type | User Field | ☐ |
| Task assignment | CI Owner (= `managed_by` at PPL) | ☐ |
| If task assignment field is empty | Create unassigned task | ☐ |

> **Routing note:** PPL labels `managed_by` as "CI Owner" on `cmdb_ci_business_app` (confirmed 2026-09-09). This is an open CCB item — see [[ownership-terminology-mapping]] O5. The Server certification build routes to **Technical Owner Group** (`managed_by_group`) instead, so BA and Server use different routing models.

## Panel 4 — Options

| Setting | Value (DEV, 2026-10-20) | PROD verified |
|---|---|---|
| Display fields (read-only context) | Name | ☐ |
| Certification fields (attested/editable) | Support group · Technical Owner Group · CI Owner · Approval group · Data Classification · Business Unit · App Code · Business owner | ☐ |
| Allow field updates | ✅ Enabled | ☐ |
| Allow empty field values | ☐ Disabled | ☐ |
| Days to complete | 21 | ☐ |
| Instructions | *"The purpose of this task is to review the associated Business Application records and verify that the supporting information is accurate. If the information is correct, select the Certify button. If updates are needed, supporting information can be corrected during this review. If the required information is not available, the record can be failed and returned at a later time."* | ☐ |

> **Instructions text:** as entered in DEV, the sentences run together without spaces after the periods ("accurate.If", "Certify button.If", "review.If"). Customer-facing in the task — fix before PROD.

### Certification fields — technical mapping and current gap volume

Field mapping is **assumed** from the audit dashboard labels; confirm technical names in the instance. Gap counts are from the BA audit dashboard against the 2,135 active BA population.

| Certification field | Technical name (assumed) | BAs missing | % of 2,135 |
|---|---|---|---|
| Data Classification | `classification` | 1,375 | 64% |
| Business Unit (Value Stream) | `business_unit` | 822 | 39% |
| Support group | `support_group` | 496 | 23% |
| Approval group | `u_approval_group` | 401 | 19% |
| Business owner | `business_owner` | 350 | 16% |
| Technical Owner Group | `u_technical_owner_group` *(TBC)* | 236 | 11% |
| App Code | App Code / Asset Tag | 208 | 10% |
| CI Owner | `managed_by` | 11 | <1% |

**~3,900 field gaps across 2,135 records.** With *Allow empty field values* disabled, a task cannot be certified until all eight fields are populated.

## Panel 5 — Schedule

| Setting | Value (DEV, 2026-10-20) | PROD verified |
|---|---|---|
| Schedule | On Demand | ☐ |
| Run policy scheduled job as | DataManager Job Runner | ☐ |

## Panel 6 — Review (policy impact)

| Metric | Value (DEV, 2026-10-20) | PROD verified |
|---|---|---|
| Records | 2,254 | ☐ |
| Tasks | 272 | ☐ |

> ≈ 8.3 records per task, i.e. ~272 distinct CI Owner values. The ~11 BAs with no CI Owner fall to unassigned task(s) — no catcher named yet.

---

## Open items to confirm before PROD

1. **Field set vs. governed dictionary** — the Stage 1 BA data dictionary lists Name, Application Category, Life Cycle Stage, IT Application Owner, Business Owner, Access Control Source System, Approval Group, Recovery Tier. The policy shares only **two** of those (Business Owner, Approval Group) and implements the audit dashboard's set instead. Confirm which set is authoritative.
2. **IT Application Owner absent** — the dictionary names Data Certification as its source of truth, yet it is not a certification field.
3. **Recovery Tier absent** — 1,820 missing (85%), the largest BA gap, and connected to the open DR field-alignment escalation (Criticality/RTO/RPO).
4. **Allow empty field values disabled** — confirm this is intentional (gap-fill) rather than attestation. As configured, ~2/3 of records are blocked on Data Classification alone within the 21-day window.
5. **CI Owner routing** — settled, or placeholder pending the CCB ruling on the `managed_by` label?
6. **Undefined fields** — Technical Owner Group and Approval Group remain open questions Q3/Q4 in [[ownership-terminology-mapping]] (field name and use case unconfirmed).
7. **Support group on BA** — the attribute schema scopes it as not applicable to non-operational Business Applications, which the filter admits.
8. **Scope filter** — reconcile `Operational status != Retired` against the dashboard's "Active" definition; in CSDM, BA retirement is carried on Life Cycle Stage.
9. **On Demand schedule** — no recurring cadence configured; the audit engagement will ask for one.
10. **BA enhancement pause (6/10)** — confirm this campaign clears it, given mass BA edits were to be logged as a story.

## How to verify against PROD

- **Provenance check (cheapest):** open the PROD policy record and read *Updated* / *Updated by*. If it was deployed by update set and untouched since, DEV and PROD match by construction.
- **Panel diff:** request the same six screenshots from PROD (platform team) and tick the `PROD verified` column above.
- **XML export diff:** export the policy record and its child field/filter records from both instances — produces an attachable artifact for audit.

## Change log

| Date | Change | Source |
|---|---|---|
| 2026-10-20 | Initial as-configured record captured from DEV screenshots | Manuel (DEV instance) |
