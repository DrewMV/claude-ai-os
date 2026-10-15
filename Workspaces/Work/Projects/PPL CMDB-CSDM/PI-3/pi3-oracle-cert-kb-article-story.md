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
  - target: "[[PI-3/pi3-database-cert-kb-article-story]]"
    type: related_to
  - target: "[[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]]"
    type: derived_from
---

# Oracle Certification — KB Article Story (Draft)

**KB-article story for Feature 1517037 (Certify Databases) — how a Technical Owner Group member finds, reviews, and completes an Oracle Instance certification task**
Drafted 2026-10-12 · Modeled on **SV-9** ([[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]]), the Server KB story built off ADO 1603551 · Worked example is **ADO 1642236** · **Not yet in ADO**
Engine-parallel to [[PI-3/pi3-database-cert-kb-article-story|DB-6b]] (MS SQL, example ADO 1641258), mirroring the DB-2a / DB-2b build split.

> **⚠️ Key difference from SV-9.** 1603551 is **gap-triggered** (task fires when Location *or* IP Address is missing), so SV-9 needed an AC explaining the OR/AND distinction. 1642236 is a **governance review**: filtered only on Install Status = Installed, Operational Status = Operational, and Technical Owner Group not empty — so **every in-scope Oracle instance receives a task whether or not anything is missing**. AC #3 below addresses the equivalent confusion for this policy.
>
> **⚠️ Oracle-specific risk the MS SQL article doesn't carry.** DEP-4 (Oracle / Kentucky discovery-authentication gap, ADO Issue **1520824** Active; MID Server disruption **1520799**; DB app-probe credential coverage **1444864**) means Oracle owners can be issued tasks whose **read-only display fields are stale or wrong** — and read-only fields can't be corrected in the task. AC #8 covers that path.

---

## DB-6a · [User Story] KB article — complete an Oracle Instance certification task *(draft)*

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1517037 |
| Sprint | TBD |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | DB-1 (1560066), 1642236, DEP-4 |
| Tags | `Data-Certification` `Database` `Oracle` `KB` `CO6-Obj3` |

**As** a Technical Owner Group member assigned an Oracle Instance certification task,
**I want** a step-by-step knowledge article that shows me how to find my assigned task, review the Oracle instance it's asking about, and enter or correct the requested values,
**so that** I can complete certification correctly on my own, without opening a ticket to ask how the process works.

**Acceptance criteria:**

1. KB article published in PPL's ServiceNow Knowledge Base (confirm space/category) and targeted at the Technical Owner Group audience — the group that receives Oracle Instance certification tasks.

2. The worked example used throughout the article is **ADO 1642236** — *"CMDB: Certify Oracle Database"* (policy name `CMDB Cert — Oracle Instance — Governance Review`) — Oracle Instance class (`cmdb_ci_db_ora_instance`), scoped to instances with Install Status = Installed, Operational Status = Operational, and Technical Owner Group populated, with **five certification fields** that must all show a value before the task can be certified.

3. Article explicitly explains that this is a **governance review, not a gap alert**, so owners aren't confused when a task arrives for a record that already looks complete: **every in-scope Oracle instance is issued a task** — the point is to have the owner confirm the five fields are right, not just fill in blanks. Fields already correct need confirming; wrong values need correcting; blank values need entering. Certification cannot complete until all five show a value.

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
   | Name, Host Name, Version, TCP Port, SID, Oracle Edition |

5. Article covers, in order:
   - Where the task notification arrives ("CMDB Data Manager task assigned to you") and what it links to.
   - How to find assigned tasks without the notification — the group's task list in CMDB Workspace / Service Graph Workspace — for members who missed or deleted the email.
   - How to open a task and identify the correct Oracle instance using the read-only display fields (Name, Host Name, Version, TCP Port, SID, Oracle Edition) — explicitly **Host Name + SID** as the disambiguator, since Name alone won't separate multiple instances on one host and the Oracle display set has no cluster field.
   - How to tell which fields need action — the five certification fields are editable and required; everything else is read-only context.
   - How to enter or correct each of the five fields, and what happens if any is left blank (certification is blocked — "Allow empty field values" is disabled per 1642236 AC #7).
   - How to submit/certify the task once all five fields are populated.
   - What to do if you're not the right owner for a CI — reassign the task to the correct Technical Owner Group, per 1642236's instruction text (full wording on file, quoted below).
   - The 21-day completion window and what happens if it's missed (task auto-closes; OOB reminder behavior at 50/70/90% of days-to-complete, per the platform capability baseline already verified for Data Manager certification — confirm reminders fire the same way for Database policies).

6. Article does **not** state a recurring certification cadence. 1642236 AC #9 configures **On Demand** scheduling, so owners should be told tasks are issued when a cycle is launched, not on a fixed calendar.

7. Article explains the two group fields owners will have to tell apart — **Technical Owner Group** (`managed_by_group`, the group the task routes to, and itself a certification field the owner may correct) and **Support Group** (`support_group`) — including what happens when an owner changes Technical Owner Group on their own task.

8. Article tells the owner what to do when the **read-only display fields are wrong, stale, or describe an instance they don't recognize** — they cannot be corrected in the task, and for Oracle this is a live risk per DEP-4 (Issue 1520824 Oracle-KY discovery gap, Active; 1520799 MID Server disruption; 1444864 credential coverage). The article gives a named route to raise it (per DB-1's escalation path) and states whether the owner should certify the five fields anyway or hold — **confirm the intended answer with the process owner; do not guess it in the article.**

9. All screenshots (task list view, task form, field layout, instructions text) are captured directly from the **live 1642236 policy** — confirm it's built and deployed to PROD before shooting screenshots, not a mockup.

10. Article's class scope matches what 1642236 actually enforces. 1642236 AC #1 names only `cmdb_ci_db_ora_instance`; the DB-2a build story on file also includes **Oracle DB Service (`cmdb_ci_db_ora_service`)**. Confirm whether DB Service is in scope — if it is, the article needs its own identification guidance for that record type, since Oracle DB Service does not carry SID.

11. KB wording (roles, escalation, reassignment) matches DB-1's documented process flow (1560066).

12. Article is linked from the task assignment notification, same pattern as the Computer campaign's job aid ([[PI-3/pi3-physical-computer-data-validation-stories|PV-4]]).

13. Confirmed with DB-5's owner (1560071) whether this article fulfills DB-5's "quick-reference (job aid)" criterion, so the two stories don't duplicate the same deliverable.

14. Article and the MS SQL article ([[PI-3/pi3-database-cert-kb-article-story|DB-6b]]) use identical wording for everything common to both engines — notification, task list navigation, the five certification fields, the 21-day window, reassignment — so owners who hold both engines aren't reading two different procedures. Confirm whether these publish as two KB articles or one with engine-specific sections.

**1642236 instruction text (quote verbatim in the article):**
> Please review the attributes for this Oracle database instance and update any values that are missing or incorrect before the due date. If you are not the right owner for this CI, reassign the task to the correct Technical Owner Group.

**Dependencies:** DB-1 / 1560066 (process flow this KB must match), ADO 1642236 (the example policy — confirm deployed to PROD and class scope resolved before final screenshots), DEP-4 (AC #8's guidance depends on how the Oracle-KY gap is resolved or scoped out), DEP-3 (if the contested attribute set changes, the five certification fields in AC #4 change with it).

---

## Open items before ADO entry

| # | Item | Owner | Blocks |
|---|------|-------|--------|
| 1 | Confirm Oracle class scope: 1642236 names only `cmdb_ci_db_ora_instance`; DB-2a on file also includes `cmdb_ci_db_ora_service`. Was DB Service dropped deliberately or is it a separate policy? | Manuel Vazquez | AC #2, #10 |
| 2 | Confirm 1642236 is the ADO ID the DB-2a build story (1560067) was created or recreated under; update [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]] if so | Manuel Vazquez | DB-2a record |
| 3 | **Decide the AC #8 answer:** when Oracle display data is stale per DEP-4, does the owner certify the five fields anyway or hold the task? The article can't be written without this | Manuel Vazquez / Josh Sterling | AC #8 |
| 4 | Confirm DEP-4 resolution — remediated, or Oracle-KY population explicitly scoped out of the first cycle. If scoped out, the article should say so rather than imply full Oracle coverage | Stan Tomberg | AC #8 |
| 5 | Confirm 1642236 is deployed to PROD — screenshots can't be shot otherwise | Bhushan Salsekar | AC #9 |
| 6 | Confirm whether Oracle RAC members need a cluster/Clustered display field for owners to identify the right instance — the MS SQL policy has `Clustered`, this one does not | Bhushan Salsekar / Ray Reuter | AC #5 |
| 7 | Confirm KB space/category for CMDB certification articles | Manuel Vazquez | AC #1 |
| 8 | Confirm reminder behavior (50/70/90%) applies to Database policies, not just the verified Data Manager baseline | Bhushan Salsekar | AC #5 |
| 9 | De-dup against DB-5's job aid criterion, and decide one-article-vs-two with the MS SQL KB story | Joe Dames / Manuel Vazquez | AC #13, #14 |
| 10 | CI Owner field conflict: 1642236 uses `managed_by`; the Network gear story uses `owned_by` for the same "CI Owner" label. Open CCB item — confirm which the article documents | Josh Sterling / CCB | AC #4 |

---

## Analogue reference

| MS SQL KB story (DB-6b, example ADO 1641258) | This story (DB-6a, example ADO 1642236) |
|---|---|
| Targets `cmdb_ci_db_mssql_instance` | Targets `cmdb_ci_db_ora_instance` — confirm whether `cmdb_ci_db_ora_service` is also in scope |
| 7 display fields incl. Instance Name and Clustered | 6 display fields — SID replaces Instance Name; **no Clustered field** |
| Disambiguate by Host Name + Instance Name | Disambiguate by Host Name + SID; no cluster context available |
| Discovery data quality not called out | DEP-4 Oracle-KY gap is Active — needs AC #8 stale-data path |
| Same 5 certification fields · 21-day window · On Demand · Technical Owner Group routing | Identical — AC #14 requires the shared wording stay identical |
