---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1517040 — Certify Network Devices — CMDB Data Certification"
objective: CO6 Obj 3 — Expand CI Data Certification Across All Major Classes
status: draft
updated: 2026-10-07
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification, network-gear]
relationships:
  - target: "[[PI-3/pi3-cert-1517040-certify-network-devices-stories-dependencies]]"
    type: related_to
  - target: "[[Config-Mgmt-Plan/data-dictionary-network-gear]]"
    type: derived_from
  - target: "[[Config-Mgmt-Plan/data-dictionary-network-gear-validation]]"
    type: related_to
---

# Network Gear — Governance Review Certification Story (Draft)

**Reference story for Feature 1517040 (Certify Network Devices) — general governance attribute review across all active network gear CIs**
Drafted 2026-10-07 · Modeled on ADO 1603551 ("CMDB: Certify Windows Servers with missing Location OR IP Address") · **Not yet in ADO**

> **⚠️ Pre-ADO gate:** Certification fields and filter must be reconciled against the **NW-1 audit baseline (ADO 1560087)** before this story is created in ADO. Field selection below reflects the network gear data dictionary non-discoverable set plus ESS-02 requirements; confirm all fields exist on the live `cmdb_ci_netgear` class and its subclasses before build.

---

## NW-R1 · [User Story] Certify Network Gear — Governance Attribute Review *(draft)*

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1517040 |
| Sprint | TBD |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Tags | `Data-Certification` `Network` `CO6-Obj3` |

**As** a Configuration Manager,
**I want** a certification policy that asks the Technical Owner Group to review and confirm the governance attributes on their active network gear CIs,
**so that** network device records are accurate and complete across all six device classes without manual audit.

**Acceptance criteria:**

1. Policy targets all six in-scope network gear subclasses: `cmdb_ci_ip_firewall`, `cmdb_ci_ip_switch`, `cmdb_ci_lb`, `cmdb_ci_wap`, `cmdb_ci_network_controller`, `cmdb_ci_ip_router`. Filtered to Install Status = Installed, Operational Status = Operational, and Technical Owner Group is not empty.

2. Certification fields are: Location (`location`), CI Owner (`owned_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Environment (`environment`), Value Stream (`business_unit`), and Data Classification (`classification`).

3. Display fields show Name, IP Address, Manufacturer, Model ID, and Serial Number as read-only context.

4. Tasks route to the Technical Owner Group (`managed_by_group`). *(Confirm this is the correct assignment field — no group-field assignment decision on file for Network; confirm with Network CCB Class Manager Adam Gross before build.)*

5. Days to complete is set to 21. Instructions below.

6. Allow field updates is enabled, permitting the assigned group to review and correct values before certifying.

7. Allow empty field values is disabled, so certification cannot complete until all certification fields have a value entered.

8. The "CMDB Data Manager task assigned to you" notification reaches the assigned group.

9. The policy is named **CMDB Cert — Network Gear — Governance Review**, configured with On Demand scheduling, with its scheduled job discoverable by policy name.

**Instructions:**
> Please review the attributes for this network device and update any values that are missing or incorrect before the due date. If you are not the right owner for this CI, reassign the task to the correct Technical Owner Group.

---

## Open items before ADO entry

| # | Item | Owner | Blocks |
|---|------|-------|--------|
| 1 | Reconcile certification fields against NW-1 audit baseline (ADO 1560087) — confirm all 7 fields are appropriate for this policy | Manuel Vazquez | AC #2 |
| 2 | Confirm Install Status and Operational Status allowed values for network gear with Adam Gross (Network CCB Class Manager) — values in AC #1 are borrowed from the Server story | Adam Gross | AC #1 |
| 3 | Confirm task assignment field: `managed_by_group` vs. `support_group` — no decision on file for Network | Manuel Vazquez / Adam Gross | AC #4 |
| 4 | Confirm all six subclass `sys_class_name` values against the live instance — table names are provisional per [[Config-Mgmt-Plan/data-dictionary-network-gear]] | Stan Tomberg | AC #1 |
| 5 | Confirm Data Classification (`classification`) field exists and is editable on `cmdb_ci_netgear` records in the live instance — it is a base class inherited field but populate-ability should be verified | Stan Tomberg | AC #2 |
| 6 | Confirm Network CCB Class Manager (Adam Gross) sign-off on certification field set — required before NW-3 build | Manuel Vazquez | AC #2, #4 |

---

## ESS-02 alignment

Certification fields mapped against ESS-02 Section 5 minimum asset requirements:

| ESS-02 Requirement | Certification Field | Status |
|---|---|---|
| Asset Owner | CI Owner (`owned_by`) | ✓ Included |
| Operational support contact group | Technical Owner Group (`managed_by_group`), Support Group (`support_group`) | ✓ Included |
| IP / network address | IP Address — display field only | Discovery-authoritative via SNMP; not owner-attestable |
| Physical location | Location (`location`) | ✓ Included |
| Information classification | Data Classification (`classification`) | ✓ Included |
| OS / apps / versions | Firmware version — not in dictionary | Missing field — needs Network Core + CCB decision before it can be certified |
| Criticality / prioritization | — | Missing field — needs stakeholder decision |
| Recoverability (RPO / RTO) | — | Missing field — needs stakeholder decision |

---

## Analogue reference

| Server story (ADO 1603551) | This story |
|---|---|
| "CMDB: Certify Windows Servers with missing Location OR IP Address" | "CMDB: Certify Network Gear — Governance Review" |
| Triggered by specific empty fields | General review of all active network gear CIs |
| Targets `cmdb_ci_win_server` | Targets all six network subclasses |
| 2 certification fields | 7 certification fields |
| Assigned to Technical Owner Group | Assigned to Technical Owner Group — confirm |
| 21-day completion window | 21-day completion window |
