---
workspace: Work
tags: [cmdb-csdm, servicenow, governance, ccb, data-definitions, network-gear]
cmp-stage: 1
status: draft
parent: configuration-management-plan-stage1
updated: 2026-09-02
---

# CMDB Data Dictionary — Network Gear

> **Status: DRAFT** — pending validation from Network Core team, ESS-02, and Audit. See [[data-dictionary-network-gear-validation]] for open validation items.

> **Companion to** [[configuration-management-plan-stage1]]. Network Gear class definitions for CMP Stage 1.  
> **Scope:** Parent class `cmdb_ci_netgear` and six in-scope subclasses: Firewall, Switch, Load Balancer, WAP (Wireless Access Point), Network Controller, Router.  
> **Updated:** 2026-09-02.

---

## CLASS: Network Gear (parent) — `cmdb_ci_netgear`

### 1. Class Identity & Scope

- **Class Display Name:** Network Gear
- **ServiceNow Table Name:** `cmdb_ci_netgear`
- **CSDM Domain:** Technology Management
- **In Scope:** Active network infrastructure devices managed by Network Operations: Firewall, Switch, Load Balancer, Wireless Access Point (WAP), Network Controller, Router. All six subclasses share the governing attribute set defined here.
- **Out of Scope:** End-user devices (Computers), Servers, storage arrays, IoT/OT assets not managed by network operations.

### 2. Attribute-Level Data Dictionary

> **Field categories defined by the delivery team — pending stakeholder validation (see [[data-dictionary-network-gear-validation]]):**
> - **Required** — must be populated for a CI record to be considered complete.
> - **Recommended (Discoverable)** — populated by ServiceNow Discovery / SNMP probes; completeness validated via certification.
> - **Recommended (Non-Discoverable)** — populated manually via Data Certification workflow; governance-critical.
>
> Cells marked `[Network Core confirm]`, `[ESS-02 confirm]`, or `[Audit confirm]` are open validation items.

**Data dictionary columns:** Attribute (Display Name) · Technical Name · Data Type · Category · Mandatory · Allowed Values / Reference · Source of Truth · Default Value · Audited · Certification Owner · Last Reviewed · Description & Governance

| Attribute (Display Name) | Technical Name | Data Type | Category | Mandatory | Allowed Values / Reference | Source of Truth | Default Value | Audited | Certification Owner | Last Reviewed | Description & Governance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **— REQUIRED —** | | | | | | | | | | | |
| Name | `name` | String (255) | Required | Y | Free text; must be unique | ServiceNow Discovery / Manual | — | Y | [Network Core confirm] | 2026-08-24 | Primary CI identifier. IRE priority 1 key field. |
| IP Address | `ip_address` | String | Required | Y | Valid IPv4/IPv6 | ServiceNow Discovery (SNMP probe, authoritative) | — | Y | [Network Core confirm] | 2026-08-24 | Management IP address. IRE priority 2 key field. For devices with multiple interfaces, this field captures the management interface IP. [Network Core confirm — convention sufficient, or dedicated mgmt IP field needed?] |
| **— RECOMMENDED (DISCOVERABLE) —** | | | | | | | | | | | |
| Manufacturer | `manufacturer` | Reference (`core_company`) | Rec-Discoverable | N | Active company record | ServiceNow Discovery (SNMP sysObjectID, authoritative) | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | Hardware manufacturer; sourced from SNMP sysObjectID data. |
| Model ID | `model_id` | Reference (`cmdb_model`) | Rec-Discoverable | N | Active CMDB model record | ServiceNow Discovery (SNMP, authoritative) | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | Device model; links to hardware model catalog. |
| Asset | `asset` | Reference (`alm_asset`) | Rec-Discoverable | N | Active asset record | Asset Management / Discovery (auto-created on CI creation) | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | Financial asset record associated with this CI. |
| Serial Number | `serial_number` | String | Rec-Discoverable | N | Hardware serial | ServiceNow Discovery (SNMP) / Asset Mgmt | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | Hardware serial for asset tracking. IRE priority 3 component where discoverable. |
| **— RECOMMENDED (NON-DISCOVERABLE) —** | | | | | | | | | | | |
| CI Owner | `owned_by` | Reference (`sys_user`) | Rec-Non-Disc | [Network Core confirm] | Active sys_user record | Manual / Data Certification | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | Individual accountable for the CI's lifecycle and accuracy. Populated via Data Certification workflow. |
| Technical Owner Group | `managed_by_group` | Reference (`sys_user_group`) | Rec-Non-Disc | [Network Core confirm] | Active sys_user_group | Manual / Data Certification | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | Group technically responsible for managing this device (e.g., Network Operations). Maps to OOB `managed_by_group`. |
| Support Group | `support_group` | Reference (`sys_user_group`) | Rec-Non-Disc | [Network Core confirm] | Active sys_user_group | Manual / Data Certification | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | ITSM group handling incidents for this device. |
| Environment | `environment` | Choice | Rec-Non-Disc | [Network Core confirm] | Prod, QA, Dev, Test | Manual / Data Certification | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | Deployment environment. See [[server-environment-mandatory-spike]] for cross-class environment placement discussion. |
| Location | `location` | Reference (`cmn_location`) | Rec-Non-Disc | [Network Core confirm] | Active location record | Asset Mgmt / Manual | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | Physical location (data center, building, rack). |
| Value Stream | `business_unit` | Reference (`business_unit`) | Rec-Non-Disc | [Network Core confirm] | Active business_unit record | Manual / Data Certification | — | [Audit confirm] | [Network Core confirm] | 2026-08-24 | Business unit / value stream this device supports. Populated via Data Certification workflow. |
| Operational Status | `operational_status` | Choice | Rec-Non-Disc | [Network Core confirm] | Build, Operational, Non-Operational, Retired [CCB confirm] | Manual / Data Certification | — | [Audit confirm] | [Network Core confirm] | 2026-09-02 | Lifecycle state of the device. Added 2026-09-02 to close Open Question 1. Note: diverges from other governed CI classes, where this field is Required with a hybrid Discovery/Manual source — see [[data-dictionary-network-gear-validation]] N2, A5. |
| Install Status | `install_status` | Choice | Rec-Non-Disc | [Network Core confirm] | Installed, On Order, In Maintenance, Retired [CCB confirm] | Manual / Data Certification | — | [Audit confirm] | [Network Core confirm] | 2026-09-02 | Installation/lifecycle status, distinct from Operational Status. Net-new field, not previously tracked in this dictionary. Added 2026-09-02. |

> **PPL Custom Base-Class Attributes** — all 7 inherited from `cmdb_ci` (SOX Indicator, SOX Type, GASCI, GASCI Type, Special Handling NERC TCA, Computer Type, Metal Tier) apply to Network Gear per the base class definition. No additional class-level PPL custom attributes are proposed at this time. See [[configuration-management-plan-stage1]] § BASE CLASS.

### 3. Data Population & Identification

- **Primary Discovery Source(s):** ServiceNow Network Discovery (SNMP probes). SSH-based probes may supplement for firmware/OS version if enabled.
- **Identification Rules (IRE):** Name (priority 1), IP Address (priority 2), Serial Number (priority 3 — where discoverable via SNMP).
- **Data Precedence / Reconciliation Rules:** ServiceNow Discovery is authoritative for all Discoverable attributes (IP Address, Manufacturer, Model ID, Serial Number). Governance attributes (CI Owner, Technical Owner Group, Support Group, Environment, Location, Value Stream) are authoritative via Data Certification — Discovery cannot overwrite them.

### 4. Relationship Architecture (CSDM Mapping)

- **Upstream Relationships:**
  - Managed by / Used by → Service Instance (Application Service)
- **Downstream Relationships:**
  - Depends on → Physical infrastructure CIs (power, rack, location) where applicable

---

## SUBCLASSES IN SCOPE

> Each subclass extends `cmdb_ci_netgear` and inherits all attributes defined above. No subclass-specific additional attributes are proposed at this draft stage — pending Network Core team confirmation that the parent attribute set is sufficient for each device type.

| Subclass Display Name | ServiceNow Table | Open Item |
|---|---|---|
| Firewall | `cmdb_ci_ip_firewall` | [ESS-02 confirm] — may require additional security-specific attributes (e.g., security zone, policy reference) |
| Switch | `cmdb_ci_ip_switch` | — |
| Load Balancer | `cmdb_ci_lb` | — |
| Wireless Access Point | `cmdb_ci_wap` | [Network Core confirm] — may need SSID / Controller reference |
| Network Controller | `cmdb_ci_network_controller` | **RESOLVED 2026-09-02** — table name confirmed |
| Router | `cmdb_ci_ip_router` | — |

---

## OPEN QUESTIONS

1. **Operational Status & Install Status — RESOLVED 2026-09-02.** Both added to § 2 above as Recommended (Non-Discoverable). Note: this diverges from other governed CI classes, where `operational_status` is Required with a hybrid Discovery/Manual source — Network Core and Audit should confirm whether Network Gear should follow the same pattern, or whether Rec-Non-Disc stands. `install_status` is net-new to this dictionary; no equivalent existed in the prior field set. See [[data-dictionary-network-gear-validation]] N2, N10, A5.
2. **Firmware / OS Version** — network devices carry a firmware/OS version (e.g., Cisco IOS). Discoverable via SSH probe if enabled. [Network Core confirm — add as Rec-Discoverable?]
3. **Management IP convention** — `ip_address` captures one IP. For multi-interface devices, is the management IP convention sufficient or is a dedicated management IP field needed? [Network Core confirm]
4. **Network Controller table name — RESOLVED 2026-09-02.** Confirmed as `cmdb_ci_network_controller`. See [[data-dictionary-network-gear-validation]] N6.
5. **Value Stream (business_unit) values** — confirm the active `business_unit` records that should be selectable for network gear. [CCB confirm]
6. **Firewall security attributes** — ESS-02 may require additional security-relevant fields on the Firewall subclass. [ESS-02 confirm]
