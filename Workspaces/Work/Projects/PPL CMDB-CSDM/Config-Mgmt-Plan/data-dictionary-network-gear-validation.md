---
workspace: Work
tags: [cmdb-csdm, governance, validation, network-gear]
status: draft
updated: 2026-08-24
---

# Network Gear Data Dictionary — Stakeholder Validation Sheet

> **Purpose.** Capture validation sign-off from three stakeholder groups on the proposed Network Gear data dictionary (see [[data-dictionary-network-gear]]).

> **Context.** The Corporate Audit Services CMDB Governance and Lifecycle Advisory Review (4/15–10/31/2026) is active; Work Review 1 is the week of 2026-08-24. Network Gear certification is a PI-3 deliverable — stakeholder sign-off on this field set gates the certification story scope. Note: ESS-02 was identified as a CO6 holdback risk — ESS-02 validation here is an opportunity to resolve that gap.

---

## How to use this sheet

Each stakeholder group reviews their section. For each open item, record one of:
- **Accept** — proposed approach is acceptable as-is
- **Amend** — acceptable with a stated change (note the change in the Notes column)
- **Defer** — decision needed by a specific date (note owner + deadline)
- **Reject** — proposed approach does not meet requirements (note reason + alternative)

---

## Proposed Field Set — Summary

| Field | Category | Mandatory (proposed) | Audited (proposed) |
|---|---|---|---|
| Name | Required | Y | Y |
| IP Address | Required | Y | Y |
| Manufacturer | Rec-Discoverable | N | TBD |
| Model ID | Rec-Discoverable | N | TBD |
| Asset | Rec-Discoverable | N | TBD |
| Serial Number | Rec-Discoverable | N | TBD |
| CI Owner | Rec-Non-Disc | TBD | TBD |
| Technical Owner Group | Rec-Non-Disc | TBD | TBD |
| Support Group | Rec-Non-Disc | TBD | TBD |
| Environment | Rec-Non-Disc | TBD | TBD |
| Location | Rec-Non-Disc | TBD | TBD |
| Value Stream (`business_unit`) | Rec-Non-Disc | TBD | TBD |

---

## 1. Network Core Team

**What you're being asked to validate:** Field coverage, discovery sources, IRE logic, device-type completeness, and ownership model alignment.

| # | Item | Proposed | Decision | Notes |
|---|------|----------|----------|-------|
| N1 | Field set completeness | 12 fields as listed above | | Are any fields missing for network operations? |
| N2 | Operational Status | **Not included.** All other governed classes include this. Recommend adding as Required. | | Accept add / Not needed / Defer |
| N3 | Firmware / OS Version | **Not included.** Discoverable via SSH probe if enabled. | | Add as Rec-Discoverable / Not needed / Defer |
| N4 | Management IP convention | `ip_address` captures management IP. For multi-interface devices, is this sufficient or is a dedicated management IP field needed? | | Sufficient / Need dedicated field |
| N5 | Discovery source | SNMP probe (primary), SSH probe (supplemental). Are these the correct sources for PPL's network environment? | | Correct / Amend: |
| N6 | Network Controller table | Confirm ServiceNow table name for Network Controller subclass. | | Table: |
| N7 | Subclass-specific fields | Any subclass (Firewall, Switch, LB, WAP, Controller, Router) requiring attributes beyond the parent set? | | Notes per subclass: |
| N8 | Ownership model | `owned_by` = individual CI Owner. `managed_by_group` = Technical Owner Group. Does this match Network Core's ownership model? | | Correct / Amend: |
| N9 | Mandatory designations | Of the non-discoverable fields, which should be Mandatory (not just Recommended) for Network Core operations? | | |

**Network Core sign-off:**

| Representative | Date | Status |
|---|---|---|
| | | ⬜ Pending |

---

## 2. ESS-02

**What you're being asked to validate:** Whether the proposed field set satisfies ESS-02 control requirements for network infrastructure CIs. Note: ESS-02 was flagged as a CO6 holdback risk — this is the validation that resolves it.

| # | Item | Proposed | Decision | Notes |
|---|------|----------|----------|-------|
| E1 | Required field sufficiency | Name + IP Address as Required. Does ESS-02 mandate any additional Required fields? | | Accept / Add: |
| E2 | Firewall security attributes | No Firewall-specific attributes currently proposed. Does ESS-02 require additional fields on the Firewall subclass (e.g., security zone, policy reference, compliance classification)? | | Not needed / Add: |
| E3 | GASCI / NERC TCA flags | Base class PPL custom attributes (GASCI, NERC TCA, SOX Indicator) are inherited by all Network Gear CIs. Does this satisfy ESS-02 requirements for network gear regulatory flagging? | | Sufficient / Amend: |
| E4 | Audit scope alignment | Which fields should be flagged as Audited = Y for ESS-02 purposes? (Proposed: Name, IP Address. Remaining fields TBD.) | | |
| E5 | Overall ESS-02 compliance | Does the proposed field set meet ESS-02 requirements as drafted? | | Accept / Amend / Reject |

**ESS-02 sign-off:**

| Representative | Date | Status |
|---|---|---|
| | | ⬜ Pending |

---

## 3. Audit — Corporate Audit Services

**What you're being asked to validate:** Whether the proposed field set meets the requirements of the CMDB Governance and Lifecycle Advisory Review (Objective 1: completeness and accuracy; Objective 2: governance process; Objective 3: OCM).

| # | Item | Proposed | Decision | Notes |
|---|------|----------|----------|-------|
| A1 | Required field audit coverage | Name + IP Address = Required + Audited. Is this sufficient for audit sampling of network gear CIs? | | Accept / Amend: |
| A2 | Governance field mandatory status | CI Owner, Technical Owner Group, Support Group are Recommended (not Mandatory). Should any be elevated to Mandatory for audit purposes? | | Accept / Elevate: |
| A3 | Environment field | Environment is Recommended (non-discoverable). Should it be Mandatory and Audited for audit scope? | | Accept / Mandatory |
| A4 | Certification Owner assignment | No Certification Owner is currently assigned for the Network Gear class. Who should own certification for network gear? | | Owner: |
| A5 | Operational Status | Not in the proposed field set. Should Operational Status be Required and Audited for network gear lifecycle evidence? | | Add / Not needed |
| A6 | Serial Number in audit scope | Serial Number is Recommended-Discoverable. Should it be Audited = Y for asset-to-CI reconciliation? | | Yes / No |
| A7 | Asset linkage in audit scope | Asset (`alm_asset` reference) is Recommended-Discoverable. Is asset linkage in scope for audit evidence? | | In scope / Out of scope |
| A8 | Overall field set adequacy | Does the proposed field set provide sufficient evidence for the Governance and Lifecycle Advisory Review? | | Accept / Amend: |

**Audit sign-off:**

| Representative | Date | Status |
|---|---|---|
| | | ⬜ Pending |

---

## Sign-Off Summary

| Stakeholder Group | Representative | Date | Status |
|---|---|---|---|
| Network Core Team | | | ⬜ Pending |
| ESS-02 | | | ⬜ Pending |
| Audit (Corp. Audit Services) | | | ⬜ Pending |

> **Once all three groups sign off,** update `status: validated` in [[data-dictionary-network-gear]] and submit to CCB for ratification.
