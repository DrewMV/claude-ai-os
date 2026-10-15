---
workspace: Work
project: CMDB-CSDM
type: facilitation-worksheet
status: draft
updated: 2026-09-09
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
| O1 | IT Application Owner | IT Application Owner *(same — no relabel observed)* | `it_application_owner` | Reference (`sys_user`) | The strategic IT leader accountable for the platform's lifecycle, roadmap, and investment decisions. Not operational — this is the "product owner" of the application in the business portfolio sense. | Notification routing for lifecycle events; used in EA integrations (LeanIX). Does **not** drive ITSM ticket routing. | Business Application | _TBD — PPL calls this \_\_\_. Is it distinct from `managed_by` (labeled "CI Owner" — see O5 correction) and from `owned_by` ("Service Owner")? Is it a single named person, or can it be a role/group? Note: CCB has already voted this field Mandatory on Business Application (decision sheet, item 3), so this isn't hypothetical — it's populated today._ | _TBD_ | ❓ |
| O2 | Business Owner | Business Owner *(same — no relabel observed)* | `business_owner` | Reference (`sys_user`) | The business-side stakeholder who funds, sponsors, or is accountable for business outcomes of the application. Distinct from IT ownership. | Notification routing for certification campaigns and ownership-change alerts. Drives the Data Certification workflow (certification tasks assigned to this person). Does **not** route ITSM tickets. | Business Application | _TBD — PPL audit: 350 BAs missing. Is Business Owner the same person PPL thinks of as "the business contact"? VP / Director level, or the operational contact?_ | _TBD_ | ❓ |
| O3 | Owned By | **"Service Owner"** (Service Instance form, per Stage 1 Data Dictionary) · Business Application form label **not confirmed** — previously logged here as "CI Owner," but confirmed 2026-09-09 (Manuel, direct instance check) that "CI Owner" is actually PPL's label for `managed_by`, not `owned_by` — see O5 | `owned_by` | Reference (`sys_user`) | Operational owner responsible for the CI's availability and data accuracy. The person accountable if the CI goes down or its data is wrong. **Not** the end user, and **not** the IT Application Owner. | Used in CMDB Health dashboards, certification campaigns, and ownership-change notifications. Does **not** directly route incidents — that is `support_group`. | Server · Service Instance · Database · Business Application | _Corrected 2026-09-09: do not assume "CI Owner" for this field. Its actual label on the Business Application form is unconfirmed — leave blank rather than guess. PPL audit: 11 BAs missing._ | _TBD_ | ⚠️ Label previously misattributed — corrected; BA-form label still unconfirmed |
| O4 | Assigned To | Assigned To *(same — no relabel observed)* | `assigned_to` | Reference (`sys_user`) | The individual to whom a CI is physically or logically assigned — the end user who has the device. On task records (Incidents, Changes), this is the resolver assigned to work the ticket. | On Computer CIs: identifies which user "has" the device; used in asset accountability reporting. On task records: drives SLA assignment and escalation routing. **Not an ITSM routing field on CI records.** | Computer | _TBD — Does PPL use "Assigned To" on Servers or Databases, or only on end-user Computers? Is there confusion with "CI Owner" (`owned_by`) on infrastructure CIs?_ | _TBD_ | ❓ |
| O5 | Managed By | **"CI Owner"** — confirmed on `cmdb_ci_business_app` (2026-09-09, Manuel, direct instance check); believed applied platform-wide but not yet confirmed on other classes | `managed_by` | Reference (`sys_user`) | The person who manages the CI on a day-to-day operational basis — a team lead or manager, not the end user. Represents who is accountable for keeping the CI running day-to-day. | Referenced by some Discovery patterns and integrations to establish management hierarchy. Used in reporting; **not** a primary ITSM routing field. | Server · Computer · Database · Business Application | _**Governance conflict, not just a labeling gap:** CSDM 5.0 reserves owner-style accountability language for `owned_by`, not `managed_by`. Labeling `managed_by` as "CI Owner" invites the exact anti-pattern CSDM 5.0 is correcting — people populate this field with whoever they consider accountable for the CI, while `owned_by` (the field actually meant to carry that accountability) goes unpopulated or underused. Needs a CCB decision: relabel `managed_by` away from "CI Owner," or explicitly redefine what "CI Owner" means at PPL and reconcile it with `owned_by`'s intended role._ | _TBD_ | ⚠️ Conflicts with CSDM 5.0 — needs CCB decision, not just alignment |

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
| `owned_by` | `owned_by` | *(not confirmed — previously logged as "CI Owner" here in error; that label belongs to `managed_by`, see below)* | **"Service Owner"** | *(not prominently surfaced)* | "Owned By" | Confirm the actual Business Application label before deciding on standardization |
| `managed_by` | `managed_by` | **"CI Owner"** (confirmed 2026-09-09) | *(not confirmed)* | *(not confirmed)* | "Managed By" | **Conflicts with CSDM 5.0**, not just inconsistent — "CI Owner" implies accountability that belongs on `owned_by`. Needs a CCB decision on relabeling, not just standardization |
| `support_group` | `support_group` | "Support Group" | "ITSM Support Group" | **"ITSM Support Group"** | "Support Group" | Standardize to one label; "ITSM Support Group" is more descriptive — apply consistently |
| `change_control` | `change_control` | *(not observed on BA form)* | "Change Approval Group" | **"Change Approval Group"** | "Change Control" | "Change Approval Group" is clearer than OOB "Change Control" — confirm as standard label |

---

## Section 5 — Open Facilitation Questions

Answer these in the working session. Each question resolves one or more rows above.

| # | Question | Resolves | Bring To |
|---|---|---|---|
| Q1 | **Partially resolved 2026-09-09:** "CI Owner" is PPL's label for `managed_by` on `cmdb_ci_business_app` (confirmed), believed platform-wide but not yet confirmed on other classes. Remaining question: is this labeling intentional, and does it conflict with the CSDM 5.0 role split badly enough to warrant relabeling `managed_by` (or redefining "CI Owner")? | O5 | Josh Sterling (CCB Chair) · Class Managers |
| Q2 | Is "IT Application Owner" (`it_application_owner`) distinct from `managed_by` (the field actually labeled "CI Owner" — see O5) and from `owned_by` ("Service Owner")? Or does the same person end up entered in more than one of these three fields today? | O1, O3, O5 | Joe Dames · Todd Dierksheide |
| Q3 | What team or role does "Technical Owner Group" identify? Is it the dev/engineering team, the infra team? How does it differ from ITSM Support Group? What is the actual field name in SN? | S4 | Todd Dierksheide · platform team |
| Q4 | What does "Approval Group (Business Owner)" approve — catalog requests, change tickets, data certification tasks? What is the actual field name in SN? Is it wired into any workflow today? | S5 | Joe Dames · platform team |
| Q5 | **Partially answered 2026-09-10 (Manuel):** "Mostly the same group, although not always." Remaining question: quantify the diverging population and confirm which field should win for automation/certification purposes when they differ — see [[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies|DEP-8]], where this is now a tracked assumption (`managed_by_group` used for certification task assignment pending confirmation). | S1, S3 | All class managers |
| Q6 | Who is the "Business Owner" of a Business Application at PPL — a named individual, a role, a committee? At what organizational level (VP / Director / Manager)? | O2 | Joe Dames · Todd Dierksheide |
| Q7 | Should `owned_by` carry the label "CI Owner" or "Service Owner" — and should that label be consistent across all CI class forms, or intentionally different? | Section 4 | CCB / platform team |
| Q8 | Should "Support Group" or "ITSM Support Group" be the standard label? Apply consistently across all class forms. | Section 4 | CCB / platform team |

---

## Section 6 — PPL → ServiceNow Crosswalk (complete during session)

Fill this table at the end of the working session. It becomes the authoritative vocabulary reference — feed results back into the Stage 1 Data Dictionary and data dictionary CCB decision sheet.

| PPL Term | PPL Definition (in their words) | Maps To (SN Technical Field) | PPL Instance Label | Notes / Gaps |
|---|---|---|---|---|
| CI Owner | _TBD_ | `managed_by` | "CI Owner" | Confirmed 2026-09-09 on `cmdb_ci_business_app`; previously misattributed to `owned_by` in this worksheet — corrected. Conflicts with CSDM 5.0 (see O5). |
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
