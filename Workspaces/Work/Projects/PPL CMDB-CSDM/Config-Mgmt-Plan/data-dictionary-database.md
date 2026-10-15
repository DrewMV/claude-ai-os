---
workspace: Work
tags: [cmdb-csdm, servicenow, governance, ccb, data-definitions, database]
cmp-stage: 1
status: ccb-approved
parent: configuration-management-plan-stage1
updated: 2026-10-09
---

# CMDB Data Dictionary — Database Instance

> **Status: CCB-APPROVED** — managed attribute set approved by CCB. Class Manager: Ray Reuter. Source: CI Class Reference slide (CMP Stage 1), approved 2026-07-21.

> **Companion to** [[configuration-management-plan-stage1]]. Database Instance class definitions for CMP Stage 1.  
> **Scope:** Parent class `cmdb_ci_db_instance` and two in-scope subclasses: Oracle Instance, MS SQL Database.  
> **Active CIs:** 3,113 · **Audited (Proposed):** 2 of 5 (CI Owner, Location).  
> **Updated:** 2026-10-09.

---

## CLASS: Database Instance (parent) — `cmdb_ci_db_instance`

### 1. Class Identity & Scope

- **Class Display Name:** Database Instance
- **ServiceNow Table Name:** `cmdb_ci_db_instance`
- **CSDM Domain:** Service Delivery
- **Class Owner:** Ray Reuter (CCB Class Manager — Database CIs)
- **In Scope:** Oracle Instance (`cmdb_ci_db_ora_instance`) and MS SQL Database (`cmdb_ci_db_mssql_instance`). Both subclasses share the governing attribute set defined here.
- **Out of Scope:** Other database engine types not managed via ServiceNow App Probes; non-production instances excluded from certification scope unless explicitly confirmed by Class Manager.

### 2. Attribute-Level Data Dictionary

> **Field categories per CCB-approved CI Class Reference (CMP Stage 1):**
> - **Required** — must be populated for a CI record to be considered complete.
> - **Recommended (Discoverable)** — populated by ServiceNow App Probes; completeness validated via certification.
> - **Recommended (Non-Discoverable)** — populated manually via Data Certification workflow; governance-critical.
>
> **Audited = T** means the field is in scope for the certification campaign. 2 of 5 managed attributes are audited (CI Owner, Location).

**Data dictionary columns:** Attribute (Display Name) · Technical Name · Data Type · Category · Mandatory · Allowed Values / Reference · Source of Truth · Default Value · Audited · Certification Owner · Last Reviewed · Description & Governance

| Attribute (Display Name) | Technical Name | Data Type | Category | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **— REQUIRED —** | | | | | | | | | | | |
| Name | `name` | String (255) | Required | Y | Free text; unique within host context | ServiceNow App Probes (authoritative) | — | Y | Ray Reuter | 2026-10-09 | Primary CI identifier. IRE priority 200 key field (Edition + Name + TCP port). Identified dependently — always in context of host Server. |
| **— RECOMMENDED (DISCOVERABLE) —** | | | | | | | | | | | |
| Version | `version` | String | Rec-Discoverable | N | Discovery authoritative | ServiceNow App Probes | — | Y | Ray Reuter | 2026-10-09 | Active running version of the database engine. App Probes are authoritative; version is a reconciliation winning attribute. |
| TCP Port | `tcp_port` | String | Rec-Discoverable | N | Discovery authoritative | ServiceNow App Probes | — | Y | Ray Reuter | 2026-10-09 | Network port the database instance listens on. IRE priority 200 key field. App Probes authoritative. |
| **— RECOMMENDED (NON-DISCOVERABLE) —** | | | | | | | | | | | |
| CI Owner | `managed_by` | Reference (`sys_user`) | Rec-Non-Disc | N | Active sys_user record | Manual / Data Certification | — | T | Ray Reuter | 2026-10-09 | Individual accountable for the CI's lifecycle and accuracy. PPL label: "CI Owner." Populated via Data Certification workflow. Note: field is `managed_by` (not `owned_by`) per PPL CCB-approved class definition — see [[ownership-terminology-mapping]]. |
| Technical Owner Group | `managed_by_group` | Reference (`sys_user_group`) | Rec-Non-Disc | N | Active sys_user_group | Manual / Data Certification | — | F | Ray Reuter | 2026-10-09 | Group technically responsible for managing this database instance. Certification tasks route to this group. |
| Support Group | `support_group` | Reference (`sys_user_group`) | Rec-Non-Disc | N | Active sys_user_group | Manual / Data Certification | — | F | Ray Reuter | 2026-10-09 | ITSM group handling incidents for this database instance. Oracle DBA Team (Oracle) / SQL DBA Team (MS SQL) per CCB decision sheet. |
| Environment | `environment` | Choice | Rec-Non-Disc | N | Prod, QA, Dev, Test | Manual / Data Certification | — | F | Ray Reuter | 2026-10-09 | Deployment environment. Missing Environment gap: ~1,187 CIs (38%) as of PI-2 audit. See ADO 1504309 (Populate Environment Attribute). |
| Location | `location` | Reference (`cmn_location`) | Rec-Non-Disc | N | Active location record | Manual / Data Certification | — | T | Ray Reuter | 2026-10-09 | Physical location of the host Server. Populated via Data Certification workflow. |

### 3. Data Population & Identification

- **Primary Discovery Source:** ServiceNow Discovery Application Probes (Oracle probes / MS SQL probes). App Probes are authoritative for active running version and TCP port details.
- **Identification Rules (IRE):** Type: **Dependent (host Server)**
  - Priority 100: Serial Number — Standard
  - Priority 200: Edition + Name + TCP port(s) — Standard
- **IRE Note:** A Database Instance is identified dependently — always in the context of its host Server. First by Serial Number (Pri 100), then by Edition + Name + TCP port(s) (Pri 200). No reconciliation rules are captured on the parent class; child classes (Oracle, MS SQL) add engine-specific discovery and reconciliation.
- **Data Precedence / Reconciliation:** App Probes are authoritative for Version and TCP Port. Governance attributes (CI Owner, Technical Owner Group, Support Group, Environment, Location) are authoritative via Data Certification — probes cannot overwrite them.
- **Known Data Quality Risk:** Oracle / Kentucky visibility gap (ADO Issue 1520824, Active) and DB credential coverage risk (ADO 1444864) may produce stale or missing discovery data. Gaps caused by discovery holes are not owner-attributable in the certification campaign. See DEP-4 in [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]].

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Runs on → Server (`cmdb_ci_server`) — identification is dependent on host Server
- **Downstream Relationships:**
  - Used by → Application Services / Service Instances where the database backs an application

---

## SUBCLASSES IN SCOPE

> Each subclass extends `cmdb_ci_db_instance` and inherits all managed attributes defined above. Subclass-specific discoverable attributes are listed below per the CCB decision sheet (2026-07-21).

| Subclass Display Name | ServiceNow Table | Engine-Specific Attributes (Discoverable) |
|---|---|---|
| Oracle Instance | `cmdb_ci_db_ora_instance` | SID, Oracle Edition, Oracle Version — via Oracle App Probes |
| MS SQL Database | `cmdb_ci_db_mssql_database` | Instance Name, Clustered, SQL Edition, TCP Port — via Discovery / SCCM |

### Oracle Instance — `cmdb_ci_db_ora_instance`

**Certification display fields (read-only context in certification form):** Name, Host Name, Version, TCP Port, SID, Oracle Edition

| Attribute | Technical Name | Source of Truth | Audited | Notes |
|---|---|---|---|---|
| SID | `sid` | Oracle App Probes | [CCB confirm] | Oracle System Identifier — primary engine identity; IRE key field |
| Oracle Edition | `edition` | Oracle App Probes | [CCB confirm] | e.g., Enterprise, Standard |
| Oracle Version | `version` | Oracle App Probes | [CCB confirm] | Inherited from parent `version` field |
| Support Group | `support_group` | Manual / Data Certification | F | Oracle DBA Team (CCB decision #33) |

### MS SQL Database — `cmdb_ci_db_mssql_database`

**Certification display fields (read-only context in certification form):** Name, Host Name, Version, TCP Port, Instance Name, SQL Edition, Clustered

| Attribute | Technical Name | Source of Truth | Audited | Notes |
|---|---|---|---|---|
| Instance Name | `instance_name` | Discovery / SCCM | [CCB confirm] | SQL Server instance name; key identifying field |
| Clustered | `clustered` | Discovery | [CCB confirm] | True/False — whether the instance is part of a cluster |
| SQL Edition | `sql_edition` | SCCM (authoritative for edition/license) | [CCB confirm] | e.g., Enterprise, Standard, Express |
| TCP Port | `tcp_port` | Discovery (overrides SCCM) | [CCB confirm] | Inherited from parent `tcp_port` field |
| Support Group | `support_group` | Manual / Data Certification | F | SQL DBA Team (CCB decision #38) |

---

## OPEN QUESTIONS

1. **Audited scope for subclass-specific attributes** — CCB decision sheet marks SID, Oracle Edition, Oracle Version, Instance Name, Clustered, SQL Edition, TCP Port as "Audited? — align to Dec audit scope" but no ruling was captured. Confirm with Ray Reuter which subclass attributes join the 2-of-5 audited set. [Ray Reuter confirm]
2. **Operational Status values** — CCB decision sheet flagged value list for `operational_status` as open (#29). Confirm allowed values (Operational, Retired, …). [CCB confirm]
3. **Value Stream / Approval Group** — audit dashboard shows Missing Value Stream ~100% and Missing Approval Group ~99.9% on Database CIs. Neither field appears in the CCB-approved managed attribute set. Confirm whether these join the certified set or remain out of scope. See DEP-3 in [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]]. [Ray Reuter / CCB confirm]
4. **Kentucky / Oracle discovery gap** — ADO Issue 1520824 (Active). Resolution status affects certification scope validity. [Stan Tomberg]
