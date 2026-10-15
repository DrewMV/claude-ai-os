---
workspace: Work
project: CMDB-CSDM
type: reference
status: active
source: cmdb_ownership_attributes_scoping_matrix-v2.xlsx
authoritative: true
updated: 2026-09-16
tags: [work, cmdb-csdm, governance, data-definitions, reference]
---

# CMDB Ownership Attributes Scoping Matrix (v2.0)

> **Authoritative.** Source: `cmdb_ownership_attributes_scoping_matrix-v2.xlsx` (v2.0). Ingested 2026-09-16.
> Cross-reference: [[Config-Mgmt-Plan/cmdb-csdm-attribute-schema]] (detailed per-attribute narrative) · [[Config-Mgmt-Plan/ownership-terminology-mapping]] (PPL facilitation worksheet)

---

## Scoped Attribute Matrix

| Attribute Name | Backend Field | Reference Type | CSDM Domain | Business Applications (`cmdb_ci_business_app`) | Application Services (`cmdb_ci_service_auto`) | Hardware Classes (`cmdb_ci_hardware` / server) |
|---|---|---|---|---|---|---|
| Business Owner | `business_owner` | sys_user / sys_user_group | Design & Planning | **Primary (Required)** | Inherited / Optional | N/A (Upstream on Apps) |
| IT Application Owner | `it_application_owner` | sys_user | Design & Planning | **Primary (Required)** | N/A | N/A |
| CI Owner | `owned_by` | sys_user | Cross-Domain (All CIs) | Required (SME) | Required (SME) | Required (Business SME) |
| Managed by Group | `managed_by_group` | sys_user_group | Service Delivery | N/A | **Required (Primary)** | Primary (Data Maintenance) |
| Support Group | `support_group` | sys_user_group | Service Delivery | N/A | Primary (Operational) | Primary (Operational) |
| Approval Group / Change Control | `change_control` | sys_user_group | Service Delivery | N/A | **Primary (Required)** | Primary (Required) |
| Managed by | `managed_by` | sys_user (Legacy) | Infrastructure | N/A | N/A | Legacy (Discouraged) |
| Assignment Group | `assignment_group` | sys_user_group (Task level) | ITSM Workflows | N/A | Inherited on Task | Inherited on Task |
| Assigned To | `assigned_to` | sys_user | End-User Assets | N/A | N/A | End-User Devices Only |

### Governance Role & Platform Triggers (per attribute)

| Attribute | Primary Governance Role | Automated Platform Triggers & Workflows |
|---|---|---|
| Business Owner | Financial executive sponsor accountable for strategic application utility & capabilities | APM Portfolio Rationalization, Service Catalog publishing, Business Capability scoring |
| IT Application Owner | Technology executive responsible for application architecture, licensing, and EOL roadmap | APM Tech Stack risk scoring, Software Asset Management (SAM) compliance, tech debt roadmap |
| CI Owner | Named individual accountable for record data accuracy, completeness, and periodic attestation. On hardware, acts as business/department SME custodian | CMDB Data Manager Attestation campaigns, CMDB Health Ownership KPI, Workspace Data Owner Home |
| Managed by Group | Technical squad accountable for record quality, operational config accuracy, and lifecycle tasks. On hardware, primary operational data steward | CMDB Data Manager Policies (Retirement / Archival / Deletion), CI Class Manager sync, Now Assist AI |
| Support Group | Operational engineering squad designated to receive, investigate, and resolve incident alerts | Incident auto-routing, ITOM Alert Management, Major Incident war-room alerts |
| Approval Group / Change Control | Technical governance body authorized to review, evaluate, and sign off on changes | Change Management Approval Engine, CAB routing, DevOps policy auto-approvals |
| Managed by | Legacy single user contact; deprecated from active task routing to prevent SPOF risks | Read-only contact lookup, legacy workspace views |
| Assignment Group | Active technical squad assigned to work on and resolve a specific task or ticket | Task queues, SLA response/resolution timers, MTTR analytics |
| Assigned To | Individual employee assigned physical custody of an end-user device | Asset Management (HAM), physical custody tracking, offboarding reclamation |

---

## CSDM Governance Axioms (v2.0)

**Axiom 1 — Individual Accountability vs. Group Operational Governance**
Strategic data accountability (`owned_by`) and business ownership (`business_owner`, `it_application_owner`) are assigned to named individuals (sys_user). Daily operational maintenance, incident resolution, change approval, and lifecycle task execution belong strictly to squads/groups (`managed_by_group`, `support_group`, `change_control`) to prevent SPOF risks.

**Axiom 2 — Class Scoping & Upstream Business Context**
Strategic business attributes (`business_owner`, `it_application_owner`) are scoped strictly to Business Applications and Service Offerings. Hardware CIs DO NOT track `business_owner` directly. On hardware CIs, `owned_by` represents individual business/department SME accountability, while `managed_by_group` acts as the technical data steward.

**Axiom 3 — Static CI Pointers vs. Dynamic Task Inheritance**
CIs store static governance pointers. Downstream ITSM tasks (Incidents, Changes, Problems) dynamically inherit these pointers onto the Task record's `assignment_group` depending on the nature of the operational work being performed.

**Axiom 4 — Automated CMDB Data Manager Alignment**
All automated Data Manager policy workflows (Attestation, Retirement, Archival, Deletion) route directly to `managed_by_group`. Ensuring `managed_by_group` is populated across hardware classes eliminates administrative bottlenecks.

> **Note:** Axiom 4 applies to Hardware and Application Services where `managed_by_group` is required. For Business Applications (`managed_by_group` = N/A in this matrix), attestation routing target should be confirmed separately — likely `owned_by` (CI Owner).
