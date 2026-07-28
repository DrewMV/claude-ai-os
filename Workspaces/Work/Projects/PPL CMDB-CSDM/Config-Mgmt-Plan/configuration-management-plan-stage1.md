---
workspace: Work
tags: [cmdb-csdm, servicenow, governance, ccb, data-definitions]
cmp-stage: 1
status: draft
parent: configuration-management-plan
updated: 2026-07-20
---

# Configuration Management Plan — Stage 1: Class & Attribute Data Definitions

> **⚠️ RECONCILIATION (2026-07-27) — delivered dictionary is authoritative for the governance view.** The version delivered to PPL — *CMDB-Data-Dictionary-CCB-2026 (July 21 2026) - DELIVERED to PPL.pptx* — is the **ratified CMP Stage 1** for the **governance managed-attribute view** (per-class Managed Attributes with Required / Recommended / Mandatory designations; mirrored 1:1 in [[cmdb-health-completeness-correctness-stories]]). **This document is the fuller technical-dictionary draft** (base-class custom attributes, child classes, IRE, per-attribute source-of-truth, relationships) and is **retained for that detail** — but where the two differ on governed attributes, the delivered deck governs.
> **Known divergence (left open, per decision 2026-07-27):** the delivered deck lists `environment` as a **Mandatory** attribute on **Server**, whereas this narrative models `environment` on **Service Instance** (see § Service Instance) and scopes it *out* of Server. That placement and the Mandatory ruling are **under validation** — see [[server-environment-mandatory-spike]]. Not changed here pending the spike.

> **Part of:** [[configuration-management-plan]] — the **CMP umbrella**. This file is the **Stage 1** deliverable; the umbrella holds the full deliverable roadmap, governance, and CO5 linkage.
> **Sync:** this doc owns Stage 1 *content*; the umbrella owns the *roadmap status*. If this stage's status changes, update **both** this file's `status` frontmatter **and** the Stage 1 row in the umbrella roadmap.
>
> **Audience:** CMDB Change Control Board (CCB). **Status:** DRAFT for CCB review. **Updated:** 2026-06-29.
>
> This stage defines the Data Definitions for key CSDM and CMDB classes: an attribute-level data dictionary, explicit Data Precedence / Reconciliation Rules, and CSDM relationship mappings establishing the source of truth for each attribute across discovery sources.
>
> **Cells marked `[CCB confirm]`** are PPL-specific governance decisions (mandatory rules, audit inclusion, certification ownership) that require CCB ratification — they are intentionally not assumed. **Certification Owner** is pre-populated from the CCB Class Manager roster where a class mapping exists.

**Data dictionary columns:** Attribute (Display Name) · Technical Name · Data Type · Mandatory · Allowed Values / Reference · Source of Truth · Default Value · Audited · Certification Owner · Last Reviewed · Description & Governance

---

## BASE CLASS: Configuration Item (`cmdb_ci`)

> All CI classes in the instance extend `cmdb_ci` and inherit its attributes. The PPL custom attributes defined here apply **universally** across every CI class.

### PPL Custom Attributes (Inherited by All CI Classes)

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| SOX Type | `u_sox_type` | Choice | N | [CCB confirm — choice values TBD] | Manual / Data Certification | — | [CCB confirm] | [CCB confirm] | 2026-07-20 | SOX compliance type classification. Applied across all CI classes. Used alongside SOX Indicator to determine SOX-scoped CIs. Per Story A design, read-only in modification workflows for SOX-flagged CIs. |
| GASCI | `u_gasci` | True/False | N | true / false | Manual / Data Certification | — | [CCB confirm] | [CCB confirm] | 2026-07-20 | Government and Security Critical Infrastructure flag. Marks CIs subject to GASCI controls. |
| GASCI Type | `u_gasci_type` | Choice | N | [CCB confirm — choice values TBD] | Manual / Data Certification | — | [CCB confirm] | [CCB confirm] | 2026-07-20 | Type of GASCI classification for the CI. |
| Special Handling (NERC TCA) | `u_nerctca` | True/False | N | true / false | Manual / Data Certification | — | [CCB confirm] | [CCB confirm] | 2026-07-20 | NERC CIP Transient Cyber Asset flag. Marks CIs requiring NERC CIP special handling. Technical name reflects the regulatory program. |
| Computer Type | `u_computer_type` | Choice | N | [CCB confirm — choice values TBD] | Manual / Discovery | — | [CCB confirm] | [CCB confirm] | 2026-07-20 | Hardware/computer type classification at the base CI level. |
| SOX Indicator | `u_sox_indicator` | True/False | N | true / false | Manual / Data Certification | false | [CCB confirm] | [CCB confirm] | 2026-07-20 | Boolean SOX flag. Default: false. Used alongside SOX Type to identify SOX-scoped CIs. Read-only in Story A modification workflow — SOX-flagged CIs are blocked from modification until Story B (governed path) is implemented. |
| Metal Tier | `u_business_priority` | Choice | N | [CCB confirm — e.g., Gold / Silver / Bronze] | Manual / Data Certification | — | [CCB confirm] | [CCB confirm] | 2026-07-20 | Business priority tier. Technical name (`u_business_priority`) differs from display label ("Metal Tier"). |

> **As configured in CI Class Manager, 2026-07-20.** Total of 7 PPL-added custom attributes at the base class level (all with `Added: true`). Choice list values for SOX Type, GASCI Type, Computer Type, and Metal Tier require CCB confirmation.

---

## CLASS: Business Application

### 1. Class Identity & Scope

- **Class Display Name:** Business Application
- **ServiceNow Table Name:** `cmdb_ci_business_app`
- **CSDM Domain:** Design & Planning
- **In Scope:** The strategic software model — the abstract concept of the application used for tracking costs, lifecycle, and business value (e.g., "ServiceNow HRSD"). Represents *what* functionality is provided.
- **Out of Scope:** Operational, deployed environments (these belong to Service Instances). Underlying physical servers or databases.

### 2. Attribute-Level Data Dictionary

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| Name | `name` | String (255) | Y | Free text; must be unique | EA integration (LeanIX) / Manual | — | Y | Todd Dierksheide (Class Mgr – Business Application) | 2026-06-24 (draft) | Primary CI identifier; IRE match key. |
| Application Category | `category` | Choice | [CCB confirm] | HR, Finance, IT, … (choice list) | EA integration (authoritative) | — | Y | Todd Dierksheide (Class Mgr – Business Application) | 2026-06-24 (draft) | High-level grouping. EA integration is authoritative for category. |
| Life Cycle Stage | `life_cycle_stage` | Choice | [CCB confirm] | CSDM lifecycle stages | EA integration (authoritative) | — | Y | Todd Dierksheide (Class Mgr – Business Application) | 2026-06-24 (draft) | Lifecycle metric sourced from Enterprise Architecture. |
| IT Application Owner | `it_application_owner` | Reference (sys_user) | [CCB confirm] | Active sys_user record | Manual / Data Certification | — | Y | CI Data Manager (Data Certification) | 2026-06-24 (draft) | Strategic IT leader responsible for the platform lifecycle. Manual updates via Data Certification workflow. |
| Business Owner | `business_owner` | Reference (sys_user) | [CCB confirm] | Active sys_user record | Manual / Data Certification | — | Y | CI Data Manager (Data Certification) | 2026-06-24 (draft) | Business stakeholder funding/sponsoring the application. |
| Access Control Source System | `u_access_control_source_system` | Choice (PPL custom) | N | [CCB confirm — choice values TBD] | Manual | — | [CCB confirm] | Todd Dierksheide (Class Mgr – Business Application) | 2026-07-20 | PPL-added custom attribute. Source system used for access control data. |
| Approval Group | `u_approval_group` | Reference (Group) (PPL custom) | N | Active sys_user_group | Manual | — | [CCB confirm] | Todd Dierksheide (Class Mgr – Business Application) | 2026-07-20 | PPL-added custom attribute. Approval group associated with this Business Application. |
| Recovery Tier | `u_recovery_tier` | String (PPL custom) | N | Free text | Manual | — | [CCB confirm] | Todd Dierksheide (Class Mgr – Business Application) | 2026-07-20 | PPL-added custom attribute. Recovery priority tier classification for the application. |

### 3. Data Population & Identification

- **Primary Discovery Source(s):** Manual entry via Catalog Request, or integration with Enterprise Architecture tools (e.g., LeanIX).
- **Identification Rules (IRE):** Name.
- **Data Precedence / Reconciliation Rules:** Enterprise Architecture integration (if present) is authoritative for Category and Lifecycle metrics. Manual updates are permitted for Ownership fields via Data Certification workflows.

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Provided by → Business Capability
- **Downstream Relationships:**
  - Consumes :: Consumed By → Service Instance

---

## CLASS: Service Instance

### 1. Class Identity & Scope

- **Class Display Name:** Service Instance / Application Service
- **ServiceNow Table Name:** `cmdb_ci_service_auto (and subclasses, e.g., cmdb_ci_service_discovered)`
- **CSDM Domain:** Service Delivery
- **In Scope:** The operational, deployed environment — the actual running stack (e.g., "ServiceNow HRSD - PROD"). Represents *where* the functionality is running.
- **Out of Scope:** The abstract software portfolio (Business Application) or individual hardware components.

### 2. Attribute-Level Data Dictionary

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| Name | `name` | String (255) | Y | Free text; must be unique | Service Mapping / Manual | — | Y | [CCB confirm] — no dedicated CCB Class Manager mapped | 2026-06-24 (draft) | Primary CI identifier. |
| Environment | `environment` | Choice | Y | Prod, QA, Dev, Test | Service Mapping / Manual | — | Y | [CCB confirm] — no dedicated CCB Class Manager mapped | 2026-06-24 (draft) | Deployment environment of the running stack. **⚠️ Divergence:** the delivered dictionary (2026-07-21) instead places a **Mandatory** `environment` on **Server**, not here — placement under validation via [[server-environment-mandatory-spike]]. |
| Service Owner | `owned_by` | Reference (sys_user) | [CCB confirm] | Active sys_user record | Manual / Data Manager | — | Y | CI Data Manager | 2026-06-24 (draft) | Operational manager responsible for uptime. |
| ITSM Support Group | `support_group` | Reference (sys_user_group) | [CCB confirm] | Active sys_user_group | Manual / Data Manager | — | Y | CI Data Manager | 2026-06-24 (draft) | Team that handles incidents for this environment. |
| Change Approval Group | `change_control` | Reference (sys_user_group) | [CCB confirm] | Active sys_user_group | Manual / Data Manager | — | Y | CI Data Manager | 2026-06-24 (draft) | CAB for this environment. |

### 3. Data Population & Identification

- **Primary Discovery Source(s):** ServiceNow Service Mapping (Top-Down), Tag-Based Mapping, or Manual mapping via APIs.
- **Identification Rules (IRE):** Inherited / Service Mapping identity (no standalone IRE defined at Stage 1).
- **Data Precedence / Reconciliation Rules:** ServiceNow Service Mapping is authoritative for dependency structure. ITSM User / Data Manager is authoritative for Governance attributes (Support Group, Change Control, Service Owner).

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Consumed by :: Consumes → Business Application
  - Used by :: Depends on → Business Service Offering
- **Downstream Relationships:**
  - Depends on :: Used by → Infrastructure CIs (Servers, Databases)
  - Contained by :: Contains → Technology Management Offering

---

## CLASS: Computer

### 1. Class Identity & Scope

- **Class Display Name:** Computer
- **ServiceNow Table Name:** `cmdb_ci_computer`
- **CSDM Domain:** Service Delivery
- **In Scope:** End-user computing devices such as laptops, desktops, and workstations.
- **Out of Scope:** Servers, Network Gear, Mobile Devices, or IoT devices.

### 2. Attribute-Level Data Dictionary

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| Name | `name` | String (255) | Y | Free text | SCCM/Intune SGC / ACC | — | Y | Monica Green (Physical) / Paul Becker (Virtual) | 2026-06-24 (draft) | CI identifier; IRE priority 3. |
| Assigned To | `assigned_to` | Reference (sys_user) | [CCB confirm] | Active sys_user record | Asset Mgmt / Manual | — | Y | CI Data Manager | 2026-06-24 (draft) | End-user to whom the device is deployed. |
| Operating System | `os` | String | N | e.g., Windows 11, macOS | SCCM/Intune SGC (authoritative) | — | [CCB confirm] | Monica Green (Physical) / Paul Becker (Virtual) | 2026-06-24 (draft) | OS sourced from endpoint management connector. |
| MAC Address | `mac_address` | String | N | Valid MAC format | Endpoint connector / Discovery | — | [CCB confirm] | Monica Green (Physical) / Paul Becker (Virtual) | 2026-06-24 (draft) | Network identifier; IRE priority 2. |
| Serial Number | `serial_number` | String | Y | Hardware serial | Asset Mgmt / SCCM (authoritative) | — | Y | Monica Green (Physical) / Paul Becker (Virtual) | 2026-06-24 (draft) | Hardware serial for asset tracking; IRE priority 1. |
| Requested Item | `u_request` | Reference (Requested Item) (PPL custom) | N | sc_request record | Service Catalog / Manual | — | N | Monica Green (Physical) / Paul Becker (Virtual) | 2026-07-20 | PPL-added custom attribute. Links the CI to the originating Service Catalog request. Max length: 32. |
| Off Network | `u_off_network` | True/False (PPL custom) | N | true / false | Manual | — | N | Monica Green (Physical) / Paul Becker (Virtual) | 2026-07-20 | PPL-added custom attribute. Flags whether the device is operating off-network. Max length: 40. |

### 3. Data Population & Identification

- **Primary Discovery Source(s):** Endpoint Management Connectors (Microsoft SCCM/Intune Service Graph Connector, Jamf), ServiceNow Agent Client Collector.
- **Identification Rules (IRE):** Rule name: **PPL Computers** (Independent; description: *Duplicate Workstation*). Single identifier entry: Standard, Active, Priority 100, criteria: **Name + Serial number**. _(As configured in CI Class Manager, 2026-07-20. Note: earlier CMP draft listed MAC Address as a separate priority level — not reflected in current system configuration. See [[ci-class-ire-reconciliation-config]] for full reconciliation rule detail.)_
- **Data Precedence / Reconciliation Rules:** SCCM/Intune Service Graph Connector is authoritative for OS, OS Version, and Hardware specifications. Asset Management / Procurement integrations override for Financial fields (Cost Center, PO Number). Four created reconciliation rules with source priorities ranging from ServiceNow[80] to ServiceNow[300] — see [[ci-class-ire-reconciliation-config]].

### 4. Relationship Architecture (CSDM Mapping)

- Typically lacks standard CSDM dependency relationships; usually tied directly to User / Asset records.

---

## PARENT CLASS: Server

### 1. Class Identity & Scope

- **Class Display Name:** Server
- **ServiceNow Table Name:** `cmdb_ci_server`
- **CSDM Domain:** Service Delivery
- **In Scope:** Any active physical or virtual instance providing compute resources (regardless of OS).
- **Out of Scope:** Network appliances, storage arrays, decommissioned hardware, and end-user workstations (laptops/desktops).

### 2. Attribute-Level Data Dictionary

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| Name | `name` | String (255) | Y | Free text | ServiceNow Discovery | — | Y | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | CI identifier; IRE component. |
| Operational Status | `operational_status` | Choice | Y | Build, Operational, Non-Operational, Retired [CCB confirm] | ServiceNow Discovery / Manual | Operational | Y | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | Lifecycle state. Confirm full allowed-value list against OOB choices. |
| IP Address | `ip_address` | String | N | Valid IPv4/IPv6 | ServiceNow Discovery (authoritative) | — | [CCB confirm] | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | Primary network interface. |
| MAC Address | `mac_address` | String | N | Valid MAC format | ServiceNow Discovery (authoritative) | — | [CCB confirm] | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | Primary network interface; IRE component. |
| CPU Count | `cpu_count` | Integer | N | Numeric | vCenter override (else Discovery) | — | [CCB confirm] | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | vCenter overrides Discovery for CPU allocation only. |
| RAM (MB) | `ram` | Integer | N | Numeric (MB) | vCenter override (else Discovery) | — | [CCB confirm] | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | vCenter overrides Discovery for RAM allocation only. |
| Serial Number | `serial_number` | String | Y | Hardware serial | ServiceNow Discovery | — | Y | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | IRE component (Serial + Type). |
| Hardware Type | `u_hardware_type` | String (Full UTF-8) (PPL custom) | N | Free text | Manual | — | N | Ray Reuter (Class Mgr – Servers & Storage) | 2026-07-20 | PPL-added custom attribute. Additional hardware categorization supplementing the standard class hierarchy. Max length: 255. |

### 3. Data Population & Identification

- **Primary Discovery Source(s):** ServiceNow Discovery, VMware vCenter, Cloud Discovery (AWS/Azure).
- **Identification Rules (IRE):** Rule name: **PPL Server** (Independent; 3 entries). Entry 1: Standard, Active, Priority 100, criterion: **Serial number**. Entry 2: Lookup, Active, Priority 200, criterion: **Serial number via lookup table**. Entry 3: Standard, Active, Priority 300, criterion: **Name**. _(As configured in CI Class Manager, 2026-07-20. Note: earlier CMP draft listed MAC Address + Name as Priority 2 — actual system uses a Lookup entry at that priority. See [[ci-class-ire-reconciliation-config]] for full reconciliation rule detail.)_
- **Data Precedence / Reconciliation Rules:** ServiceNow Discovery is authoritative for Hardware and Network attributes (ip_address, mac_address). VMware vCenter integration overrides Discovery ONLY for CPU and RAM allocation attributes. Server has no Created reconciliation rules — all 5 reconciliation rules are Derived from the parent Computer/Hardware class hierarchy; see [[ci-class-ire-reconciliation-config]].

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Used by :: Depends on → Application Service
- **Downstream Relationships:**
  - Runs on :: Hosts → Virtual Machine Instance (if virtual) OR Hardware CI (if physical)

---

## CHILD CLASS: Windows Server
*Child of parent class **Server**.*

### 1. Class Identity & Scope

- **Class Display Name:** Windows Server
- **ServiceNow Table Name:** `cmdb_ci_win_server`
- **CSDM Domain:** Service Delivery (inherited from Server)
- **In Scope:** Compute instances running Microsoft Windows Server OS (e.g., 2016, 2019, 2022).
- **Out of Scope:** Non-Windows compute instances.

### 2. Attribute-Level Data Dictionary

> Inherits all attributes, IRE, and relationships from parent class Server (cmdb_ci_server). Only attributes unique to or overridden by this child class are listed below.

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| OS Version | `os_version` | String | N | e.g., Windows Server 2019 | SCCM SGC (overrides Discovery) | — | [CCB confirm] | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | SCCM overrides ServiceNow Discovery for OS attributes. |
| OS Domain | `os_domain` | String | N | AD domain | SCCM SGC (overrides Discovery) | — | [CCB confirm] | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | SCCM overrides Discovery. |
| OS Service Pack | `os_service_pack` | String | N | Free text | SCCM SGC (overrides Discovery) | — | [CCB confirm] | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | SCCM overrides Discovery. |
| ITSM Support Group | `support_group` | Reference (sys_user_group) | [CCB confirm] | Wintel Infrastructure Ops | Manual / CI Data Manager | — | Y | CI Data Manager | 2026-06-24 (draft) | Governance attribute — NOT writable by automated tooling. |
| Change Approval Group | `change_control` | Reference (sys_user_group) | [CCB confirm] | Wintel CAB | Manual / CI Data Manager | — | Y | CI Data Manager | 2026-06-24 (draft) | Governance attribute — NOT writable by automated tooling. |

### 3. Data Population & Identification

- **Primary Discovery Source(s):** Microsoft SCCM Service Graph Connector, ServiceNow Discovery (WMI).
- **Identification Rules (IRE):** Inherited from Server.
- **Data Precedence / Reconciliation Rules:** SCCM overrides ServiceNow Discovery for Operating System attributes (os_version, os_service_pack, os_domain). Neither automated tool may overwrite Governance attributes (support_group, change_control) — strictly manual / CI Data Manager.

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Inherited from Server
- **Downstream Relationships:**
  - Inherited from Server

---

## CHILD CLASS: Linux Server
*Child of parent class **Server**.*

### 1. Class Identity & Scope

- **Class Display Name:** Linux Server
- **ServiceNow Table Name:** `cmdb_ci_linux_server`
- **CSDM Domain:** Service Delivery (inherited from Server)
- **In Scope:** Compute instances running a Linux kernel (e.g., RHEL, Ubuntu, CentOS, SUSE).
- **Out of Scope:** Non-Linux compute instances.

### 2. Attribute-Level Data Dictionary

> Inherits all attributes, IRE, and relationships from parent class Server (cmdb_ci_server). Only attributes unique to or overridden by this child class are listed below.

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| OS Architecture | `os_architecture` | String | N | e.g., x86_64 | ServiceNow Discovery (SSH, authoritative) | — | [CCB confirm] | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | Discovery via SSH is authoritative for OS/Hardware. |
| Kernel Release | `kernel_release` | String | N | Free text | ServiceNow Discovery (SSH, authoritative) | — | [CCB confirm] | Ray Reuter (Class Mgr – Servers & Storage) | 2026-06-24 (draft) | Discovery via SSH is authoritative. |
| ITSM Support Group | `support_group` | Reference (sys_user_group) | [CCB confirm] | Unix/Linux Administration Team | Manual / CI Data Manager | — | Y | CI Data Manager | 2026-06-24 (draft) | Governance attribute — manual / Data Manager control. |
| Change Approval Group | `change_control` | Reference (sys_user_group) | [CCB confirm] | Linux CAB | Manual / CI Data Manager | — | Y | CI Data Manager | 2026-06-24 (draft) | Governance attribute — manual / Data Manager control. |

### 3. Data Population & Identification

- **Primary Discovery Source(s):** ServiceNow Discovery (SSH).
- **Identification Rules (IRE):** Inherited from Server.
- **Data Precedence / Reconciliation Rules:** ServiceNow Discovery via SSH is strictly authoritative for all OS and Hardware attributes. Governance attributes (support_group, change_control) remain under manual / Data Manager control.

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Inherited from Server
- **Downstream Relationships:**
  - Inherited from Server

---

## PARENT CLASS: Database

### 1. Class Identity & Scope

- **Class Display Name:** Database Instance
- **ServiceNow Table Name:** `cmdb_ci_database`
- **CSDM Domain:** Service Delivery
- **In Scope:** Logical database instances providing data storage and retrieval capabilities.
- **Out of Scope:** The underlying host server OS, or the underlying physical storage / disks.

### 2. Attribute-Level Data Dictionary

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| Name | `name` | String (255) | Y | Free text | ServiceNow Discovery (App Probes) | — | Y | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | CI identifier. |
| Version | `version` | String | N | Engine version string | ServiceNow Discovery (authoritative) | — | [CCB confirm] | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | Active running version of the DB engine. |
| TCP Port | `tcp_port` | Integer | N | Numeric port | ServiceNow Discovery (authoritative) | — | [CCB confirm] | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | Listening port; IRE component. |
| Operational Status | `operational_status` | Choice | Y | Operational, Retired, … [CCB confirm] | ServiceNow Discovery / Manual | Operational | Y | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | Lifecycle state. |

### 3. Data Population & Identification

- **Primary Discovery Source(s):** ServiceNow Discovery (Application Probes), Database Management integrations.
- **Identification Rules (IRE):** Rule name: **Database instance rule** (Dependent — identified in context of its host Server). Entry 1: Standard, Active, Priority 100, criterion: **Serial number**. Entry 2: Standard, Active, Priority 200, criteria: **Edition + Name + TCP port(s)**. _(As configured in CI Class Manager, 2026-07-20.)_
- **Data Precedence / Reconciliation Rules:** ServiceNow Discovery Application Probes are authoritative for active running version and port details.

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Used by :: Depends on → Application Service / Service Instance
- **Downstream Relationships:**
  - Runs on :: Hosts → Server (Windows or Linux)

---

## CHILD CLASS: Oracle Database
*Child of parent class **Database**.*

### 1. Class Identity & Scope

- **Class Display Name:** Oracle Instance
- **ServiceNow Table Name:** `cmdb_ci_db_ora_instance`
- **CSDM Domain:** Service Delivery (inherited from Database)
- **In Scope:** Logical instances running the Oracle RDBMS engine.
- **Out of Scope:** Other database engines.

### 2. Attribute-Level Data Dictionary

> Inherits all attributes, IRE, and relationships from parent class Database (cmdb_ci_database). Only attributes unique to this child class are listed below.

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| SID | `sid` | String | Y | Oracle SID | ServiceNow Discovery (Oracle probes) | — | [CCB confirm] | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | System identifier for the Oracle instance. |
| Oracle Edition | `edition` | String | N | e.g., Enterprise, Standard | ServiceNow Discovery (Oracle probes) | — | [CCB confirm] | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | Oracle edition. |
| Oracle Version | `version` | String | N | Version string | ServiceNow Discovery (Oracle probes) | — | [CCB confirm] | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | Oracle engine version. |
| Support Group | `support_group` | Reference (sys_user_group) | [CCB confirm] | Oracle DBA Team | Manual / CI Data Manager | — | Y | CI Data Manager | 2026-06-24 (draft) | Governance attribute. |

### 3. Data Population & Identification

- **Primary Discovery Source(s):** ServiceNow Discovery via Oracle-specific probes / patterns.
- **Identification Rules (IRE):** Inherited from Database.
- **Data Precedence / Reconciliation Rules:** Oracle DB-specific patterns override basic TCP-port discovery mapping for deeper instance metrics.

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Inherited from Database
- **Downstream Relationships:**
  - Contains :: Contained By → Oracle Catalogs (cmdb_ci_db_ora_catalog)

---

## CHILD CLASS: MSFT SQL Database
*Child of parent class **Database**.*

### 1. Class Identity & Scope

- **Class Display Name:** MSFT SQL Instance
- **ServiceNow Table Name:** `cmdb_ci_db_mssql_instance`
- **CSDM Domain:** Service Delivery (inherited from Database)
- **In Scope:** Logical instances running Microsoft SQL Server.
- **Out of Scope:** Other database engines.

### 2. Attribute-Level Data Dictionary

> Inherits all attributes, IRE, and relationships from parent class Database (cmdb_ci_database). Only attributes unique to this child class are listed below.

| Attribute (Display Name) | Technical Name | Data Type | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|
| Instance Name | `instance_name` | String | Y | Free text | ServiceNow Discovery / SCCM SGC | — | [CCB confirm] | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | SQL instance name. |
| Clustered | `clustered` | True/False | N | true / false | ServiceNow Discovery (authoritative for clustering) | false | [CCB confirm] | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | Whether the instance is clustered. |
| SQL Edition | `edition` | String | N | e.g., Enterprise, Standard | SCCM SGC (authoritative for edition/license) | — | [CCB confirm] | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | SCCM is authoritative for Edition and License parameters. |
| TCP Port | `tcp_port` | Integer | N | Numeric port | ServiceNow Discovery (overrides SCCM) | — | [CCB confirm] | Ray Reuter (Class Mgr – Database CIs) | 2026-06-24 (draft) | Discovery overrides SCCM for active running Port and clustering metrics. |
| Support Group | `support_group` | Reference (sys_user_group) | [CCB confirm] | SQL DBA Team | Manual / CI Data Manager | — | Y | CI Data Manager | 2026-06-24 (draft) | Governance attribute. |

### 3. Data Population & Identification

- **Primary Discovery Source(s):** ServiceNow Discovery (WMI/PowerShell), SCCM Service Graph Connector.
- **Identification Rules (IRE):** Inherited from Database.
- **Data Precedence / Reconciliation Rules:** SCCM Service Graph Connector is authoritative for SQL Server Edition and License parameters. ServiceNow Discovery overrides SCCM for active running Port and clustering metrics. Reconciliation Rules (as configured in CI Class Manager, 2026-07-20): 2 Created rules, both covering Attributes: All — one sourced from ServiceWatch[9999], one from ServiceNow[9999]. (Priority 9999 = lowest precedence, allow-all fallback rules for this class.)

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Inherited from Database
- **Downstream Relationships:**
  - Contains :: Contained By → MSFT SQL Databases (cmdb_ci_db_mssql_database)

---
