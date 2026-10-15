---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "TBD — parent feature not yet confirmed"
sprint: "TBD"
status: draft
updated: 2026-09-25
tags: [work, cmdb-csdm, safe, pi-planning, service-catalog]
relationships:
  - target: "[[Config-Mgmt-Plan/cmdb-csdm-attribute-schema]]"
    type: related_to
  - target: "[[Config-Mgmt-Plan/ownership-terminology-mapping]]"
    type: related_to
---

# Business Application Modification Request — Service Catalog Story

**Requester-facing Service Catalog item to propose field changes to an existing `cmdb_ci_business_app`, with fulfiller review/approval and stakeholder notifications**
Sprint: TBD · Owner: M. Vazquez (confirm build owner)

> **Status: DRAFT** — not created in ADO. Parent feature, sprint, and points are placeholders pending refinement.

---

## Story

| Field | Value |
|-------|-------|
| ADO ID | _(net-new — not yet created)_ |
| Type | Enabler – Configuration |
| Parent feature | _(TBD — confirm at refinement)_ |
| Sprint | _(TBD)_ |
| Owner | Manuel Vazquez (confirm build owner) |
| Points | _(TBD — confirm at refinement)_ |
| State | Draft |
| Tags | `Service-Catalog` `Business-Application` `CMDB` `CI-Modification` |

**As** a requester needing to change data on an existing Business Application,
**I want** a Service Catalog item that lets me look up the application, see its current field values, submit only the changes I make, and have a fulfiller review/approve those changes before they're applied — with the right people notified along the way,
**So that** modification requests are captured accurately, governed fields like SOX classification aren't bypassed, and everyone responsible for the CI (old and new) stays informed.

**Acceptance criteria:**

*Initial state*
- [ ] Catalog item's only visible field on load is **Name** (Lookup Select Box against `cmdb_ci_business_app`)
- [ ] Name's reference qualifier excludes CIs in **Retired** operational status
- [ ] Typing letters into Name filters/searches via typeahead (native Lookup Select Box behavior)

*Reveal on selection (Catalog UI Policy 1)*
- [ ] Selecting a Business Application in Name reveals all 18 remaining fields (table below); clearing Name hides them again
- [ ] On selection, Lookup Select Box native auto-population pre-fills each revealed field with the CI's current value

*Field configuration*

| Field Label | ServiceNow field | Type | Qualifier |
|---|---|---|---|
| CI Owner | `managed_by` | Lookup Select Box (sys_user) | `active=true` |
| Business Owner | `owned_by` | Lookup Select Box (sys_user) | `active=true` |
| Metal Tier | `u_metal_tier` | Select Box (Choice) | — |
| Business Unit | `business_unit` | Lookup Select Box (business_unit) | — |
| Data Classification | `data_classification` | Select Box (Choice) | — |
| SOX Indicator | `u_sox_indicator` | Checkbox (True/False) | — |
| SOX Type | `u_sox_type` | Select Box (Choice) | conditional, see below |
| Category | `category` | Select Box (Choice) | — |
| Operational Status | `operational_status` | Select Box (Choice) | — |
| Status | `install_status` | Select Box (Choice) | — |
| Technical Owner Group | `managed_by_group` | Lookup Select Box (sys_user_group) | `active=true` |
| Approval Group | `approval_group` | Lookup Select Box (sys_user_group) | `active=true` |
| Support Group | `support_group` | Lookup Select Box (sys_user_group) | `active=true` |
| Access Control Source System | `u_access_control_source_system` | Select Box (Choice) | — |
| Recovery Tier | `u_recovery_tier` | Select Box (Choice) | — |
| Environment | `environment` | Select Box (Choice) | — |
| Asset Criticality | `u_asset_criticality` | Select Box (Choice) | — |
| RPO | `u_recovery_point_objective_rpo` | Select Box (Choice) | — |
| RTO | `u_recovery_time_objective_rto` | Select Box (Choice) | — |

*SOX conditional (Catalog UI Policy 2)*
- [ ] `sox_indicator` = true → `sox_type` becomes **visible and mandatory**
- [ ] `sox_indicator` = false → `sox_type` is hidden, cleared, and not mandatory
- [ ] Submit is blocked by native form validation if SOX Indicator is true and SOX Type is empty

*Change detection*
- [ ] On RITM creation, a server-side script (Business Rule or Flow Action) retrieves the CI record referenced by `name`
- [ ] Script compares each of the 18 submitted field values against that CI's current live values
- [ ] Only differing fields are written to a read-only summary variable (`requested_changes`), formatted as `Field: old value → new value`, displayed in the RITM's Notes section
- [ ] Unchanged fields are excluded from the summary entirely

*Fulfiller review and approval*
- [ ] Fulfiller reviews `requested_changes` in the RITM Notes section
- [ ] Fulfiller can revert any individual field's requested value back to the CI's current value before closing
- [ ] Fulfiller saves the RITM and sets **State to Closed Complete**
- [ ] A Business Rule on that state transition (state → Closed Complete) writes the accepted field values to the CI record
- [ ] Reverted fields are not written to the CI — only values still standing as "requested" at close time are applied

*Notifications*
- [ ] On RITM Closed Complete, the **requester** is notified of which changes were implemented (from the `requested_changes` summary, minus any fields the fulfiller reverted)
- [ ] On any CI field change, the CI's **pre-change** `managed_by` (CI Owner), `managed_by_group` (Technical Owner Group), and `owned_by` (Business Owner) are notified that changes were made to their CI
- [ ] If `managed_by`, `managed_by_group`, or `owned_by` is itself among the changed fields, the **new** value(s) — the incoming CI Owner, Technical Owner Group, and/or Business Owner — are notified that they are now responsible for this CI

---

## Known caveat

CI Owner (`managed_by`) / Business Owner (`owned_by`) reflects PPL's current, confirmed-as-used mapping, which is the reverse of the CSDM-standard mapping documented in [[Config-Mgmt-Plan/cmdb-csdm-attribute-schema]]. This is an open CCB item independent of this build — flag as a dependency, not a blocker.
