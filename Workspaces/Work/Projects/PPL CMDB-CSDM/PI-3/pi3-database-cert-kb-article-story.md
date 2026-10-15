---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1517037 — Certify Databases — CMDB Data Certification"
objective: CO6 Obj 3 — Expand CI Data Certification Across All Major Classes
status: draft
updated: 2026-10-12
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification]
relationships:
  - target: "[[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]]"
    type: derived_from
---

# Database Certification — KB Article Story (Draft)

**KB-article story for Feature 1517037 (Certify Databases) — how a Technical Owner Group member finds, reviews, and completes an MS SQL Database certification task**
Drafted 2026-10-12 · Modeled on **SV-9** ([[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]]), the Server KB story built off ADO 1603551 · Worked example is **ADO 1641258** · **Not yet in ADO**

> **⚠️ Key difference from SV-9.** 1603551 is **gap-triggered** (task fires when Location *or* IP Address is missing), so SV-9 needed an AC explaining the OR/AND distinction. 1641258 is a **governance review**: filtered only on Install Status = Installed, Operational Status = Operational, and Technical Owner Group not empty — so **every in-scope MS SQL instance receives a task whether or not anything is missing**. AC #3 below addresses the equivalent confusion for this policy ("why did I get a task when everything looks filled in?") rather than carrying SV-9's OR/AND text across.

---

## DB-6b · [User Story] KB article — complete an MS SQL Database certification task *(draft)*

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1517037 |
| Sprint | TBD |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | DB-1 (1560066), 1641258 |
| Tags | `Data-Certification` `Database` `MSSQL` `KB` `CO6-Obj3` |

**As** a Technical Owner Group member assigned an MS SQL Database certification task,
**I want** a step-by-step knowledge article that shows me how to find my assigned task, review the database instance it's asking about, and enter or correct the requested values,
**so that** I can complete certification correctly on my own, without opening a ticket to ask how the process works.

**Acceptance criteria:**

1. KB article published in PPL's ServiceNow Knowledge Base (confirm space/category) and targeted at the Technical Owner Group audience — the group that receives MS SQL Database certification tasks.

2. The worked example used throughout the article is **ADO 1641258** — *"CMDB: Certify SQL Database"* (policy name `CMDB Cert — MS SQL Database — Governance Review`) — MS SQL Database class only (`cmdb_ci_db_mssql_instance`), scoped to instances with Install Status = Installed, Operational Status = Operational, and Technical Owner Group populated, with **five certification fields** that must all show a value before the task can be certified.

3. Article explicitly explains that this is a **governance review, not a gap alert**, so owners aren't confused when a task arrives for a record that already looks complete: **every in-scope MS SQL instance is issued a task** — the point is to have the owner confirm the five fields are right, not just fill in blanks. Fields already correct need confirming; wrong values need correcting; blank values need entering. Certification cannot complete until all five show a value.

4. Article includes a field map so owners know what to touch in the UI vs. what is context only:

   | Certification field (editable, required) | UI label |
   |---|---|
   | `location` | Location |
   | `managed_by` | CI Owner |
   | `managed_by_group` | Technical Owner Group |
   | `support_group` | Support Group |
   | `environment` | Environment |

   | Display field (read-only context) |
   |---|
   | Name, Host Name, Version, TCP Port, Instance Name, SQL Edition, Clustered |

5. Article covers, in order:
   - Where the task notification arrives ("CMDB Data Manager task assigned to you") and what it links to.
   - How to find assigned tasks without the notification — the group's task list in CMDB Workspace / Service Graph Workspace — for members who missed or deleted the email.
   - How to open a task and identify the correct database instance using the read-only display fields (Name, Host Name, Version, TCP Port, Instance Name, SQL Edition, Clustered) — including how to distinguish multiple instances on the same host, which Name alone won't do.
   - How to tell which fields need action — the five certification fields are editable and required; everything else is read-only context.
   - How to enter or correct each of the five fields, and what happens if any is left blank (certification is blocked — "Allow empty field values" is disabled per 1641258 AC #7).
   - How to submit/certify the task once all five fields are populated.
   - What to do if you're not the right owner for a CI — reassign the task to the correct Technical Owner Group, per 1641258's instruction text (full wording on file, quoted below).
   - The 21-day completion window and what happens if it's missed (task auto-closes; OOB reminder behavior at 50/70/90% of days-to-complete, per the platform capability baseline already verified for Data Manager certification — confirm reminders fire the same way for Database policies).

6. Article does **not** state a recurring certification cadence. 1641258 AC #9 configures **On Demand** scheduling, so owners should be told tasks are issued when a cycle is launched, not on a fixed calendar.

7. Article explains the two group fields owners will have to tell apart — **Technical Owner Group** (`managed_by_group`, the group the task routes to, and itself a certification field the owner may correct) and **Support Group** (`support_group`) — including what happens when an owner changes Technical Owner Group on their own task.

8. All screenshots (task list view, task form, field layout, instructions text) are captured directly from the **live 1641258 policy** — confirm it's built and deployed to PROD before shooting screenshots, not a mockup.

9. The class targeted in the screenshots matches what 1641258 actually enforces — confirm `cmdb_ci_db_mssql_instance` vs. the `cmdb_ci_db_mssql_database` on file in the DB-2b draft before writing.

10. KB wording (roles, escalation, reassignment) matches DB-1's documented process flow (1560066).

11. Article is linked from the task assignment notification, same pattern as the Computer campaign's job aid ([[PI-3/pi3-physical-computer-data-validation-stories|PV-4]]).

12. Confirmed with DB-5's owner (1560071) whether this article fulfills DB-5's "quick-reference (job aid)" criterion, so the two stories don't duplicate the same deliverable.

**1641258 instruction text (quote verbatim in the article):**
> Please review the attributes for this MS SQL database and update any values that are missing or incorrect before the due date. If you are not the right owner for this CI, reassign the task to the correct Technical Owner Group.

**Dependencies:** DB-1 / 1560066 (process flow this KB must match), ADO 1641258 (the example policy — confirm deployed to PROD and class name resolved before final screenshots), DEP-3 (if the contested attribute set changes, the five certification fields in AC #4 change with it).

---

## Open items before ADO entry

| # | Item | Owner | Blocks |
|---|------|-------|--------|
| 1 | ~~Resolve MS SQL class name~~ — **settled 2026-10-12**: DEP-5 AC #3 in [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]] also names `cmdb_ci_db_mssql_instance`, so 1641258 is right and the `cmdb_ci_db_mssql_database` in the DB-2b draft is the stale value. Correct the DB-2b draft | Manuel Vazquez | — |
| 2 | Confirm 1641258 is the ADO ID the DB-2b build story was created under; update [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]] if so | Manuel Vazquez | DB-2b record |
| 3 | Confirm 1641258 is deployed to PROD — screenshots can't be shot otherwise | Bhushan Salsekar | AC #8 |
| 4 | Confirm KB space/category for CMDB certification articles | Manuel Vazquez | AC #1 |
| 5 | Confirm reminder behavior (50/70/90%) applies to Database policies, not just the verified Data Manager baseline | Bhushan Salsekar | AC #5 |
| 6 | De-dup against DB-5's job aid criterion | Joe Dames / Manuel Vazquez | AC #12 |
| 7 | CI Owner field conflict: 1641258 uses `managed_by`; the Network gear story uses `owned_by` for the same "CI Owner" label. Open CCB item — confirm which the article documents | Josh Sterling / CCB | AC #4 |

---

## Analogue reference

| Server KB story (SV-9, example ADO 1603551) | This story (DB-6b, example ADO 1641258) |
|---|---|
| Gap-triggered — task fires on Location **or** IP Address missing | Governance review — every in-scope instance gets a task |
| Needed an AC explaining the OR/AND distinction | Needs an AC explaining "why a task when nothing's missing" |
| 2 certification fields (Location, IP Address) | 5 certification fields (Location, CI Owner, Technical Owner Group, Support Group, Environment) |
| 7 display fields (Name, Serial Number, OS, Asset Tag, SOX Type, Data Classification, Environment) | 7 display fields (Name, Host Name, Version, TCP Port, Instance Name, SQL Edition, Clustered) |
| Instruction text truncated on file ("Please confirm and e...") — needed confirming | Instruction text complete on file — quote verbatim |
| Targets `cmdb_ci_win_server` | Targets `cmdb_ci_db_mssql_instance` — confirm |
| Assigned to Technical Owner Group · 21-day window | Assigned to Technical Owner Group · 21-day window |
| Scheduling not specified | On Demand scheduling — no cadence to document |
