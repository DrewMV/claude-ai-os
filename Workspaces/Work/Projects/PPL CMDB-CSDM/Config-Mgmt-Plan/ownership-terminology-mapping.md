---
workspace: Work
project: CMDB-CSDM
type: facilitation-worksheet
status: draft
updated: 2026-07-15
tags: [cmdb-csdm, governance, data-definitions, facilitation, ccb]
---

# CMDB Ownership & Assignment — Terminology Mapping Worksheet

> **Purpose:** ServiceNow uses specific field names and definitions for ownership, stewardship, and assignment. PPL interprets these terms differently, and several PPL concepts have no direct ServiceNow equivalent (or the wrong one is being used). This worksheet maps the two vocabularies so the team can align on what each field *means*, how ServiceNow *uses it in automation*, and what PPL *calls it and expects from it*.
>
> **How to use:** Pre-populated columns (SN side) are from the ServiceNow platform standard and the Stage 1 Data Dictionary. **PPL columns are the facilitation output** — fill these in during the working session with class managers and/or CCB. Resolve each row to a `Status` of ✅ Aligned, ⚠️ Gap, or ❓ Needs Discussion.
>
> **Label note:** "SN OOB Label" is what vanilla ServiceNow displays on the form. "PPL Instance Label" is what PPL has relabeled it to in their instance (from the Stage 1 Data Dictionary and audit dashboard). Where PPL has relabeled a field, the same underlying field may carry *different labels on different CI class forms* — these are called out explicitly.
>
> **Sources:** Stage 1 Data Dictionary (CMP Stage 1) · BA Audit Dashboard Spike (1480111) · ADO stories 1475582 / 1475584 / 1475585 / 1509863.

---

## Section 1 — Ownership Fields (person-level)

These fields identify a named individual as responsible for a CI in some capacity.

| # | SN OOB Label | PPL Instance Label | Technical Field | Data Type | SN Standard Definition | SN Platform Usage (automation / workflow) | Applies To (Class) | PPL Interpretation / Actual Usage | PPL Preferred Term | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| O1 | IT Application Owner | IT Application Owner *(same — no relabel observed)* | `it_application_owner` | Reference (`sys_user`) | The strategic IT leader accountable for the platform's lifecycle, roadmap, and investment decisions. Not operational — this is the "product owner" of the application in the business portfolio sense. | Notification routing for lifecycle events; used in EA integrations (LeanIX). Does **not** drive ITSM ticket routing. | Business Application | _TBD — PPL calls this \_\_\_. Is it the same concept as "CI Owner"? Is it a single named person, or can it be a role/group?_ | _TBD_ | ❓ |
| O2 | Business Owner | Business Owner *(same — no relabel observed)* | `business_owner` | Reference (`sys_user`) | The business-side stakeholder who funds, sponsors, or is accountable for business outcomes of the application. Distinct from IT ownership. | Notification routing for certification campaigns and ownership-change alerts. Drives the Data Certification workflow (certification tasks assigned to this person). Does **not** route ITSM tickets. | Business Application | _TBD — PPL audit: 350 BAs missing. Is Business Owner the same person PPL thinks of as "the business contact"? VP / Director level, or the operational contact?_ | _TBD_ | ❓ |
| O3 | Owned By | **"Service Owner"** (Service Instance form) · **"CI Owner"** (Business Application form per audit dashboard) | `owned_by` | Reference (`sys_user`) | Operational owner responsible for the CI's availability and data accuracy. The person accountable if the CI goes down or its data is wrong. **Not** the end user, and **not** the IT Application Owner. | Used in CMDB Health dashboards, certification campaigns, and ownership-change notifications. Does **not** directly route incidents — that is `support_group`. | Server · Service Instance · Database · Business Application | _TBD — Same field, two different PPL labels. Does PPL expect the same person/role in this field for a Business Application as for a Server? PPL audit: 11 BAs missing._ | _TBD_ | ⚠️ Same field, two labels — align intent |
| O4 | Assigned To | Assigned To *(same — no relabel observed)* | `assigned_to` | Reference (`sys_user`) | The individual to whom a CI is physically or logically assigned — the end user who has the device. On task records (Incidents, Changes), this is the resolver assigned to work the ticket. | On Computer CIs: identifies which user "has" the device; used in asset accountability reporting. On task records: drives SLA assignment and escalation routing. **Not an ITSM routing field on CI records.** | Computer | _TBD — Does PPL use "Assigned To" on Servers or Databases, or only on end-user Computers? Is there confusion with "CI Owner" (`owned_by`) on infrastructure CIs?_ | _TBD_ | ❓ |
| O5 | Managed By | Managed By *(same — no relabel observed; not prominently surfaced in PPL forms)* | `managed_by` | Reference (`sys_user`) | The person who manages the CI on a day-to-day operational basis — a team lead or manager, not the end user. Represents who is accountable for keeping the CI running day-to-day. | Referenced by some Discovery patterns and integrations to establish management hierarchy. Used in reporting; **not** a primary ITSM routing field. | Server · Computer · Database | _TBD — Is "Managed By" (a person) distinct in PPL's model from "Managed By Group" (the group equivalent below)? Is this field currently populated at PPL?_ | _TBD_ | ❓ |

---

## Section 2 — Stewardship Fields (group-level)

These fields identify a *team or group* collectively responsible for a CI. These drive most ServiceNow automation — routing incidents, changes, and approvals.

| # | SN OOB Label | PPL Instance Label | Technical Field | Data Type | SN Standard Definition | SN Platform Usage (automation / workflow) | Applies To (Class) | PPL Interpretation / Actual Usage | PPL Preferred Term | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | Support Group | **"ITSM Support Group"** (relabeled on Server and Service Instance forms per data dictionary) | `support_group` | Reference (`sys_user_group`) | The ITSM team responsible for handling incidents and service requests raised against this CI. This is the **primary routing field** in ServiceNow. | **Incident auto-assignment routing** — when an incident is raised against a CI, `support_group` becomes the Assignment Group on the incident. Also drives Problem Management routing, Event Management alert correlation, and ITOM. **If empty, incident routing fails or falls to a default queue.** | Server · Computer · Database · Business Application · Service Instance | _TBD — PPL audit: 496 BAs missing. Does PPL distinguish between the "ITSM Support Group" label on Servers and the "Support Group" label elsewhere, or is that a form-label inconsistency to fix?_ | _TBD_ | ⚠️ Label inconsistency across classes |
| S2 | Change Control | **"Change Approval Group"** (relabeled on Server and Service Instance forms per data dictionary) | `change_control` | Reference (`sys_user_group`) | The CAB (Change Advisory Board) or approver group responsible for authorizing changes to this CI. When a Change Request targets a CI, this group is pulled in as approvers. | **Change request approval routing** — Change Approval Group is auto-populated as approvers on Change tickets raised against the CI. **If empty, change governance is bypassed or falls to a global default CAB.** | Windows Server · Linux Server · Database · Service Instance | _TBD — Does PPL have class-specific CABs (Wintel CAB, Linux CAB, DBA CAB) or a single enterprise CAB? Is the OOB label "Change Control" what PPL teams recognize, or is "Change Approval Group" a clearer term for them?_ | _TBD_ | ❓ |
| S3 | Managed By Group | Managed By Group *(same — no relabel observed; not prominently surfaced in PPL forms)* | `managed_by_group` | Reference (`sys_user_group`) | The group operationally managing the CI — accountable for day-to-day health. Distinct from Support Group (incident response) and Change Approval Group (change governance). | Used in reporting and some Discovery integrations for management hierarchy. Less automation-critical than `support_group`; primarily a governance and reporting field. **Low functional impact if empty (OOB).** | Server · Computer · Database | _TBD — Does PPL distinguish between the team that "manages" a CI (Managed By Group) and the team that handles incidents on it (Support Group / ITSM Support Group)? Are these the same group at PPL?_ | _TBD_ | ❓ |
| S4 | *(no OOB equivalent)* | **"Technical Owner Group"** (PPL-observed on Business Application audit dashboard — 236 missing) | `u_technical_owner_group` *(likely — confirm in SN)* | Reference (`sys_user_group`) | **Not a standard OOB ServiceNow field.** No direct equivalent in the OOB CMDB schema. Closest OOB candidates: `managed_by_group` (Managed By Group) or a custom field introduced by PPL or a prior implementation team. | **Unknown — depends on whether this field is wired into any workflow.** If it is a custom field with no script/rule referencing it, it has no automation impact today. Its functional role at PPL needs to be defined before it can be governed. | Business Application | _TBD — What team does this field identify? Is it the dev/engineering team? The infra team? How does it differ from Support Group? Who populates it, and what happens when it's populated (is it referenced anywhere)?_ | _TBD_ | ⚠️ No OOB equivalent — confirm field name and use case |
| S5 | *(no OOB equivalent)* | **"Approval Group (Business Owner)"** (PPL-observed on Business Application audit dashboard — 401 missing) | *(field name TBD — confirm in SN)* | Reference (`sys_user_group`) | **Not a standard OOB ServiceNow field.** Possibly a custom field for routing business-side approvals on Service Catalog requests (e.g., "Request a new Business Application") or change workflows targeting Business Application CIs. | **Unknown — depends on wiring.** If this group is referenced in a Catalog workflow or Change approval rule, empty records break that approval chain. If not wired, it is a data gap with no current functional impact. | Business Application | _TBD — What does this group approve? Catalog requests? Change tickets? Data Certification sign-offs? This needs a concrete use-case definition before the gap can be prioritized._ | _TBD_ | ⚠️ No OOB equivalent — define use case first |

---

## Section 3 — Automation Impact by Field (cross-reference)

Which fields ServiceNow uses to route work — and what breaks at PPL when they are empty.

| Field | Technical Name | Incident Routing | Change Routing | Catalog Approval | Data Certification | Health Audit | Notification | Functional Impact if Empty |
|---|---|---|---|---|---|---|---|---|
| ITSM Support Group | `support_group` | **PRIMARY** | — | — | — | Audited | Yes | **Incident falls to default queue or unassigned** |
| Change Approval Group | `change_control` | — | **PRIMARY** | — | — | — | Yes | **Change approval bypassed or falls to global CAB** |
| Business Owner | `business_owner` | — | — | — | **PRIMARY** | Audited (350 gap) | Yes | Certification task has no assignee; floats unowned |
| IT Application Owner | `it_application_owner` | — | — | — | Referenced | — | Yes | Lifecycle notifications go nowhere |
| CI Owner / Service Owner | `owned_by` | — | — | — | Referenced | Audited (11 gap) | Yes | CI accountability unclear; certification orphaned |
| Managed By Group | `managed_by_group` | — | — | — | — | — | — | Reporting gap only; no OOB functional impact |
| Assigned To | `assigned_to` | — | — | — | — | — | — | Asset accountability gap; no ITSM routing impact on CI |
| Technical Owner Group | `u_technical_owner_group` *(TBC)* | — | — | ❓ | — | Audited (236 gap) | — | **Unknown — depends on custom wiring** |
| Approval Group (BO) | *(TBD)* | — | — | ❓ | — | Audited (401 gap) | — | **Unknown — depends on custom wiring** |

---

## Section 4 — Label Inconsistencies Observed (action items)

Fields where PPL's instance uses **different labels on different CI class forms** for the same underlying field. These create confusion because users see a different name depending on which form they are on.

| Field | Technical Name | Label on Business Application | Label on Service Instance | Label on Server | OOB Label | Recommended Action |
|---|---|---|---|---|---|---|
| `owned_by` | `owned_by` | **"CI Owner"** | **"Service Owner"** | *(not prominently surfaced)* | "Owned By" | Align on a single label across all classes, or document the intentional distinction |
| `support_group` | `support_group` | "Support Group" | "ITSM Support Group" | **"ITSM Support Group"** | "Support Group" | Standardize to one label; "ITSM Support Group" is more descriptive — apply consistently |
| `change_control` | `change_control` | *(not observed on BA form)* | "Change Approval Group" | **"Change Approval Group"** | "Change Control" | "Change Approval Group" is clearer than OOB "Change Control" — confirm as standard label |

---

## Section 5 — Open Facilitation Questions

Answer these in the working session. Each question resolves one or more rows above.

| # | Question | Resolves | Bring To |
|---|---|---|---|
| Q1 | What does PPL mean by "CI Owner"? Is it a person or a group? Is it the same concept on a Business Application as on a Server? | O3 | Class Managers (Todd, Ray) |
| Q2 | Is "IT Application Owner" (`it_application_owner`) a distinct role from "CI Owner" (`owned_by`) in PPL's model — or are these the same person in two fields? | O1, O3 | Joe Dames · Todd Dierksheide |
| Q3 | What team or role does "Technical Owner Group" identify? Is it the dev/engineering team, the infra team? How does it differ from ITSM Support Group? What is the actual field name in SN? | S4 | Todd Dierksheide · platform team |
| Q4 | What does "Approval Group (Business Owner)" approve — catalog requests, change tickets, data certification tasks? What is the actual field name in SN? Is it wired into any workflow today? | S5 | Joe Dames · platform team |
| Q5 | Does PPL distinguish between "the group that manages a CI" (Managed By Group) and "the group that handles incidents on it" (ITSM Support Group)? Or are these the same group in practice? | S1, S3 | All class managers |
| Q6 | Who is the "Business Owner" of a Business Application at PPL — a named individual, a role, a committee? At what organizational level (VP / Director / Manager)? | O2 | Joe Dames · Todd Dierksheide |
| Q7 | Should `owned_by` carry the label "CI Owner" or "Service Owner" — and should that label be consistent across all CI class forms, or intentionally different? | Section 4 | CCB / platform team |
| Q8 | Should "Support Group" or "ITSM Support Group" be the standard label? Apply consistently across all class forms. | Section 4 | CCB / platform team |

---

## Section 6 — PPL → ServiceNow Crosswalk (complete during session)

Fill this table at the end of the working session. It becomes the authoritative vocabulary reference — feed results back into the Stage 1 Data Dictionary and data dictionary CCB decision sheet.

| PPL Term | PPL Definition (in their words) | Maps To (SN Technical Field) | PPL Instance Label | Notes / Gaps |
|---|---|---|---|---|
| CI Owner | _TBD_ | _TBD_ | _TBD_ | Observed on BA audit dashboard; `owned_by` is the likely field |
| Service Owner | _TBD_ | _TBD_ | _TBD_ | Same field (`owned_by`) — different form label on Service Instance |
| Business Owner | _TBD_ | `business_owner` | "Business Owner" | 350 BAs missing |
| IT Application Owner | _TBD_ | `it_application_owner` | "IT Application Owner" | |
| ITSM Support Group | _TBD_ | `support_group` | "ITSM Support Group" / "Support Group" | Label inconsistent across forms |
| Change Approval Group | _TBD_ | `change_control` | "Change Approval Group" | OOB label is "Change Control" |
| Technical Owner Group | _TBD_ | _TBD — confirm field name_ | "Technical Owner Group" | 236 BAs missing; likely custom field |
| Approval Group (BO) | _TBD_ | _TBD — confirm field name_ | "Approval Group (Business Owner)" | 401 BAs missing; use case TBD |
| Managed By | _TBD_ | `managed_by` | "Managed By" | Person-level; low automation impact |
| Managed By Group | _TBD_ | `managed_by_group` | "Managed By Group" | Group-level; low automation impact |
| Assigned To | _TBD_ | `assigned_to` | "Assigned To" | End-user device assignment (Computer) |
