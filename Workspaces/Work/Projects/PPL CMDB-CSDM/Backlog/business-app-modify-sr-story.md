---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: draft
updated: 2026-09-28
tags: [work, cmdb-csdm, backlog, safe, service-catalog]
---

# Modify SR — Business Application

> **Status: DRAFT** — not created in ADO. Create from the Feature "+" link, never standalone.

## Story

| Field | Value |
|-------|-------|
| ADO ID | _(net-new)_ |
| Type | Story |
| Parent feature | _(TBD)_ |
| Sprint | _(TBD)_ |
| Owner | _(TBD)_ |
| Points | _(TBD)_ |
| Tags | `Service-Catalog` `Business-Application` `CMDB` `Customization` |

**As a** business user,
**I want** the ability to request changes to existing Business Applications,
**So that** correct data is quickly updated and available in the CMDB.

## Acceptance criteria

- [ ] The requester selects the Business Application to change — only applications whose operational status is **not** Retired **and** whose Technical Owner Group (`managed_by_group`) is populated are available to choose
- [ ] Current values are displayed for each field in scope, and the requester can edit any of them **except** App Code (`asset_tag`) and Metal Tier (`u_business_priority`), which are display-only
- [ ] On submit, a request item is created and assigned to the application's owning group (`managed_by_group`)
- [ ] The request notes list only the fields the requester changed, each showing its current value and the requested value
- [ ] The fulfiller can reset any field back to its original value
- [ ] The fulfiller can Save, Close Complete, or Close Incomplete
- [ ] On Close Complete, the accepted values are written to the Business Application record
- [ ] SOX Type is hidden and cleared when SOX Indicator is false; visible and mandatory when true
- [ ] On Close Complete, the requester is notified that the request has been processed, listing the changes actually applied
- [ ] On Close Complete, the CI's **pre-change** `owned_by`, `managed_by`, and `managed_by_group` are notified of the changes applied — **except** where Description is the only field changed, in which case only the requester is notified
- [ ] Where `owned_by`, `managed_by`, or `managed_by_group` is itself among the applied changes, the **new** value of that field is notified that it is now responsible for the CI
- [ ] On Close Incomplete, the requester is notified that the request was closed without changes being applied

## Before refinement

1. **Field list — mostly resolved (2026-09-28).** The authoritative source is now the catalog requirements workbook `Documents/Catalog Item - Request Template Business Application.xlsx`, Questions tab: **22 fields**, not the 19 in `Config-Mgmt-Plan/cmdb-attribute-change-catalog-fields.xlsx`. App Code (`asset_tag`) and Description (`description`) were added; the analysis spreadsheet is stale and also still carries the wrong `u_technical_owner_group` (it is `managed_by_group`). Field names confirmed 2026-09-28: `u_business_priority` (Metal Tier, not `u_metal_tier`), `u_access_control_source_system`, `u_recovery_tier`. **Still unverified:** `u_sox_indicator`, `u_sox_type`, `data_classification`.
2. **Customization approval.** This is custom work, so per [[definition-of-ready]] Gate 2 it needs the `Customization` tag, a linked RAID/Decision issue, and Sonica Das approval **before sprint entry**.
3. **Sizing.** Likely too large for one iteration. If the team won't commit it, split on the AC lines above.

## Out of scope

No approval workflow — fulfiller review only, confirmed 2026-09-28. No SOX-specific approval or routing: the SOX Indicator / SOX Type conditional behaviour in the acceptance criteria **is** in scope, but a SOX change gets no additional governance step beyond fulfiller review.

Notifications are **no longer out of scope** — see the acceptance criteria above (superseded 2026-09-28).
