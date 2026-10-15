---
workspace: Work
project: CMDB-CSDM
type: reference
status: active
source: servicenow_cmdb_csdm_attribute_schema-v2.docx
authoritative: true
updated: 2026-09-16
tags: [work, cmdb-csdm, governance, data-definitions, reference]
---

# ServiceNow CMDB & CSDM Attribute Schema & Governance Guide (v2.0)

> **Authoritative.** Source: `servicenow_cmdb_csdm_attribute_schema-v2.docx` (v2.0). Ingested 2026-09-16.
> CSDM alignment: CSDM v5 / Australia release.
> Cross-reference: [[Config-Mgmt-Plan/cmdb-ownership-scoping-matrix]] (class scoping matrix) · [[Config-Mgmt-Plan/ownership-terminology-mapping]] (PPL facilitation worksheet)

---

## Core Governance Principles

- **Individual Accountability vs. Group Governance:** Named individuals (sys_user) hold strategic data accountability (`owned_by`) and business vision (`business_owner`, `it_application_owner`). Operational squads (sys_user_group) execute daily technical workflows and automated data quality policies (`managed_by_group`, `support_group`, `change_control`).
- **Scoped Class Applicability:** Strategic business attributes (`business_owner`, `it_application_owner`) are scoped strictly to conceptual software entities (Business Applications) and Service Offerings. Hardware CIs use `owned_by` for named SME custodian accountability; `managed_by_group` handles technical data accuracy.
- **Static CI Pointers vs. Dynamic Task Inheritance:** CIs store static, foundational governance pointers. Downstream ITSM tasks dynamically inherit these onto the Task record's `assignment_group`.
- **Elimination of SPOF:** Legacy individual fields like `managed_by` are deprecated from active task routing to prevent operational bottlenecks when employees change roles or depart.

---

## Attribute Definitions

### CI Owner (`owned_by`)

| Property | Value |
|---|---|
| Database Field | `owned_by` |
| Field Type | sys_user (Reference) |
| CSDM Domain | Cross-Domain (All CIs) |
| Class Scope | Required: Business Applications, Application Services, Hardware CIs |

**What it represents:** The specific named individual (SME) held ultimately accountable for the CI's data record accuracy, completeness, and business alignment.

**Key question answered:** *"Who is the named individual accountable for ensuring this CI record is accurate, trustworthy, and validated?"*

On Hardware CIs: `owned_by` provides a human point of contact for ownership without forcing the individual to execute manual daily data maintenance (that is delegated to `managed_by_group`).

**Platform functionality:** CMDB Data Manager (Attestation policy target), CMDB Health Dashboard (Services with Owners KPI), CMDB Workspace (Data Owner Home).

---

### Managed By Group (`managed_by_group`)

| Property | Value |
|---|---|
| Database Field | `managed_by_group` |
| Field Type | sys_user_group (Reference) |
| CSDM Domain | Service Delivery / Infrastructure |
| Class Scope | Required: Hardware CIs, Application Services |

**What it represents:** The designated technical squad accountable for maintaining overall record quality, physical/operational configuration accuracy, and administrative lifecycle governance.

**Key question answered:** *"Which technical team is accountable for validating that this asset exists, is complete and correct, and receives automated lifecycle governance tasks?"*

**Platform functionality:** CMDB Data Manager (routes Attestation, Retirement, Archival, and Deletion policy tasks directly to the group), CI Class Manager sync, Now Assist AI Data Governance Agent.

---

### Support Group (`support_group`)

| Property | Value |
|---|---|
| Database Field | `support_group` |
| Field Type | sys_user_group (Reference) |
| CSDM Domain | Service Delivery (Operational) |
| Class Scope | Required: Application Services, Hardware CIs. Not applicable to non-operational Business Applications. |

**What it represents:** The primary operational engineering team paged to receive, investigate, and resolve operational incidents, system alerts, and outages.

**Key question answered:** *"Which active operational squad gets paged at 2:00 AM if this specific component breaks or triggers an alert?"*

Must reference an active functional group with 24/7 rotational coverage — not individual users.

**Platform functionality:** Incident & Problem Management (auto-populates Incident `assignment_group`), ITOM Event Management & Alert Routing, Major Incident war room assembly.

---

### Approval Group / Change Control (`change_control`)

| Property | Value |
|---|---|
| Database Field | `change_control` |
| Field Type | sys_user_group (Reference) |
| CSDM Domain | Service Delivery (Governance) |
| Class Scope | Required: Application Services, Hardware CIs. Separates approval authority from physical change execution. |

**What it represents:** The technical governance body or Change Advisory Board (CAB) authorized to review, evaluate, and approve proposed modifications or maintenance.

**Key question answered:** *"Which leadership body or technical squad must evaluate and sign off before changes, upgrades, or maintenance are executed?"*

**Platform functionality:** Change Management Approval Engine (auto-routes CAB approvals), Change Risk & Impact Analysis, DevOps Change Policy Engine.

---

### Business Owner (`business_owner`)

| Property | Value |
|---|---|
| Database Field | `business_owner` |
| Field Type | sys_user / sys_user_group (Reference) |
| CSDM Domain | Design & Planning / Service Consumption |
| Class Scope | Required: Business Applications, Service Offerings. **NOT APPLICABLE on Hardware CIs.** Hardware CIs inherit business context upstream via Service Instances. |

**What it represents:** The business executive or sponsor who funds the application/service, determines its business value, and aligns it with business capabilities.

**Key question answered:** *"Which business sponsor holds financial accountability and determines the strategic utility of this application?"*

Never added directly to low-level hardware or infrastructure CIs.

**Platform functionality:** APM Application Portfolio Rationalization, CSDM Manage Portfolio Domain, Service Catalog publishing, Business Capability scoring.

---

### IT Application Owner (`it_application_owner`)

| Property | Value |
|---|---|
| Database Field | `it_application_owner` |
| Field Type | sys_user (Reference) |
| CSDM Domain | Design & Planning |
| Class Scope | Required: Business Applications. **NOT APPLICABLE on Hardware CIs or infrastructure.** |

**What it represents:** The technology executive or lead architect responsible for long-term platform architecture, vendor roadmaps, and software license compliance.

**Key question answered:** *"Who is the technology executive responsible for the architectural health and vendor relationship of this application?"*

Distinguishes long-term architectural stewardship from daily infrastructure operation.

**Platform functionality:** Application Portfolio Management (APM tech debt scoring & software EOL), Software Asset Management (SAM compliance).

---

### Managed By — Legacy (`managed_by`)

| Property | Value |
|---|---|
| Database Field | `managed_by` |
| Field Type | sys_user (Reference) |
| CSDM Domain | Infrastructure (Legacy) |
| Class Scope | Legacy field on Hardware CIs. **Discouraged for active task routing.** |

**What it represents:** A legacy attribute referencing a single user record responsible for hands-on physical or technical configuration of a specific device.

**Key question answered:** *"Who is the primary individual contact focal point for maintaining this physical device?"*

Treated purely as read-only contact metadata. Active governance is routed to `managed_by_group`.

**Platform functionality:** Historical contact lookup, legacy form views, metadata displays.

---

### Assignment Group (`assignment_group`) — Derived Task Attribute

| Property | Value |
|---|---|
| Database Field | `assignment_group` |
| Field Type | sys_user_group (Task Level) |
| CSDM Domain | ITSM Operational Workflows |
| Class Scope | Present on Task tables (incident, change_request). **NOT present natively on cmdb_ci.** Inherited dynamically from CI `support_group` or `change_control`. |

**What it represents:** The active technical group assigned to work on and complete a specific operational record or workflow task.

**Key question answered:** *"Which specific team is currently assigned to work on and resolve this active ticket?"*

Never create custom `assignment_group` fields on `cmdb_ci`. Rely on task inheritance.

**Platform functionality:** Task Engine Routing, Visual Task Boards (VTBs), SLA countdown timers, MTTR analytics.

---

## Scoped Class Ownership Summary

| Attribute Name | Backend Field | Business Applications | Application Services | Hardware Classes |
|---|---|---|---|---|
| Business Owner | `business_owner` | Primary (Required) | Inherited / Optional | N/A |
| IT Application Owner | `it_application_owner` | Primary (Required) | N/A | N/A |
| CI Owner | `owned_by` | Required (SME) | Required (SME) | Required (Business SME) |
| Managed by Group | `managed_by_group` | N/A | Required (Primary) | Primary (Data Maintenance) |
| Support Group | `support_group` | N/A | Primary (Operational) | Primary (Operational) |
| Approval Group | `change_control` | N/A | Primary (Required) | Primary (Required) |
| Managed by | `managed_by` | N/A | N/A | Legacy (Discouraged) |
| Assignment Group | `assignment_group` | N/A | Inherited on Task | Inherited on Task |
| Assigned To | `assigned_to` | N/A | N/A | End-User Devices Only |
