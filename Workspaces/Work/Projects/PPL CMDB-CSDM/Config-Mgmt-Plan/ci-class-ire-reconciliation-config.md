---
workspace: Work
tags: [cmdb-csdm, servicenow, governance, ire, reconciliation, data-definitions]
type: reference
status: current
parent: configuration-management-plan-stage1
updated: 2026-07-20
---

# CI Class IRE & Reconciliation Rule Configuration

> **Source:** Screenshots captured from ServiceNow CI Class Manager, 2026-07-20.
> **Part of:** [[configuration-management-plan-stage1]] — Stage 1 companion reference.
> This file records the **as-built** identification and reconciliation rule configuration as observed in the system. It is a factual snapshot, not a governance decision document. Governance authority remains with the CCB per [[configuration-management-plan]].

---

## Computer (`cmdb_ci_computer`)

### Identification Rule

| Field | Value |
|---|---|
| Rule name | PPL Computers |
| Type | Independent |
| Applies to | Computer |
| Description | Duplicate Workstation |

**Identifier Entries (1):**

| # | Type | Status | Priority | Search on table | Criterion attributes |
|---|---|---|---|---|---|
| 1 | Standard | Active | 100 | Computer | Name, Serial number |

> Note: The CMP Stage 1 draft originally listed MAC Address as a separate priority level. The actual system configuration uses a single entry combining Name + Serial number at Priority 100.

### Reconciliation Rules

**Created (4):**

| Priority | Discovery Source | Attributes | Applies to |
|---|---|---|---|
| 80 | ServiceNow | IP Address, MAC Address, OS Version (3 attributes) | Computer |
| 90 | SG-SCCM | CPU count, Disk space GB, Manufacturer, + additional (~7 total) | Computer |
| 100 | SG-SCCM | Approval group, Asset, Assigned, Attestation status + additional (~98 total) | Computer |
| 300 | ServiceNow | Approval group, Asset, Asset tag, Assigned + additional (~100 total) | Computer |

**Derived (1) — inherited from Hardware parent class:**

| Priority | Discovery Source | Attributes | Applies to |
|---|---|---|---|
| 100 | ServiceNow | All | Hardware |

---

## Server (`cmdb_ci_server`)

### Identification Rule

| Field | Value |
|---|---|
| Rule name | PPL Server |
| Type | Independent |
| Applies to | Server |

**Identifier Entries (3):**

| # | Type | Status | Priority | Search on table | Criterion attributes |
|---|---|---|---|---|---|
| 1 | Standard | Active | 100 | Server | Serial number |
| 2 | Lookup | Active | 200 | Server | Serial number (via lookup table) |
| 3 | Standard | Active | 300 | Server | Name |

> Note: The CMP Stage 1 draft listed MAC Address + Name as a priority level. The actual system uses a Lookup entry at Priority 200 (serial number via lookup table), not a MAC-based match.

### Reconciliation Rules

**Created (0):** No rules created directly on this class.

**Derived (5) — all inherited from parent class hierarchy:**

| Priority | Discovery Source | Attributes | Applies to (source class) |
|---|---|---|---|
| 80 | ServiceNow | IP Address, MAC Address, OS Version | Computer |
| 90 | SG-SCCM | CPU count, Disk space GB, Manufacturer, + additional | Computer |
| 100 | ServiceNow | All | Hardware |
| 100 | SG-SCCM | Approval group, Asset, Assigned, Attestation + additional | Computer |
| 200 | ServiceNow | Approval group, Asset, Asset tag, Assigned + additional | Computer |

> Server inherits all reconciliation rules from the Computer/Hardware class hierarchy — none are defined directly on the Server class.

---

## Database Instance (`cmdb_ci_database`)

### Identification Rule

| Field | Value |
|---|---|
| Rule name | Database instance rule |
| Type | **Dependent** — identified in context of its host Server |
| Applies to | Database Instance |

**Identifier Entries (2):**

| # | Type | Status | Priority | Search on table | Criterion attributes |
|---|---|---|---|---|---|
| 1 | Standard | Active | 100 | Database Instance | Serial number |
| 2 | Standard | Active | 200 | Database Instance | Edition, Name, TCP port(s) |

> Rule type is Dependent, reflecting that a Database Instance is always identified relative to the Server it runs on.

---

## MS SQL Database (`cmdb_ci_db_mssql_database`)

### Reconciliation Rules

**Created (2):**

| Priority | Discovery Source | Attributes | Applies to |
|---|---|---|---|
| 9999 | ServiceWatch | All | MS SQL Database |
| 9999 | ServiceNow | All | MS SQL Database |

> Priority 9999 = lowest possible precedence. These are allow-all fallback rules — any source can populate any attribute, with no override precedence between sources. No Identification Rule screenshot was captured for this class.

---

## Business Application (`cmdb_ci_business_app`)

> No IRE or reconciliation rule screenshots were captured for this class. Custom attributes (u_access_control_source_system, u_approval_group, u_recovery_tier) are documented in [[configuration-management-plan-stage1]].
