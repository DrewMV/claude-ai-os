---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1517032 — Certify Servers — CMDB Data Certification"
objective: CO6 Obj 3 — Expand CI Data Certification Across All Major Classes
sprint: "3.2 (build start); process-flow doc 3.1"
co6-due: 2026-09-30
status: reconciled
updated: 2026-08-05
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification]
relationships:
  - target: "[[PI-3/pi3-data-certification-feature-breakdown]]"
    type: derived_from
  - target: "[[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-cmdb-csdm-ado-tracking]]"
    type: related_to
  - target: "[[PI-3/pi3-objectives]]"
    type: related_to
  - target: "[[cmdb-health-completeness-correctness-stories]]"
    type: related_to
  - target: "[[server-environment-mandatory-spike]]"
    type: related_to
  - target: "[[PI-3/pi3-physical-computer-data-validation-stories]]"
    type: related_to
---

# Feature 1517032 — Stories & Dependencies

**Certify Servers — CMDB Data Certification**
Sprint 3.2 (build) · process-flow doc starts 3.1 · CO6 due Sep 30 · Owner: M. Vazquez

> **Status: RECONCILED (2026-07-31)** — all 5 stories created in ADO under Feature 1517032; IDs below, and unlike the Computers feature, all 5 landed in the sprints originally planned. Per [[definition-of-ready]], create stories from the Feature "+" link, never standalone.
> Parallel to [[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]] (Computers). Both certify a CI class off the PI-2 BA pilot pattern to the same Sep 30 gate. See [[PI-3/pi3-data-certification-feature-breakdown]] for the full feature-level breakdown.
> **Update (2026-08-05 — full ADO board export):** sprint placement unchanged and confirmed; states and remaining points added below. SV-1 (1535496) shows ADO Work Item Type **Spike**, not User Story as drafted — naming drift only.
> **Update (2026-09-11):** SV-6, SV-7, SV-8 added below as **draft, targeted remediation stories** for Server CIs missing Location and/or IP Address — not yet in ADO. SV-6 targets both fields empty together; SV-7 and SV-8 split out Location-only and IP Address-only.
> **Update (2026-09-28):** SV-9 added below as a **draft KB-article story** for the Technical Owner Group — how to find, review, and complete/correct a Server certification task — using **ADO 1603551** (*"CMDB: Certify Windows Servers with missing Location OR IP Address"*) as its worked example; not yet in ADO. 1603551 is a real, already-created ADO story that overlaps with SV-6 (Windows-only scope, OR trigger vs. SV-6's AND) — see the reconciliation flag on SV-6 below.

---

## Sprint reconciliation note (raise at Sprint Planning)

ADO records Feature 1517032's start as **Sprint 3.2 (Aug 19)**; the [[PI-3/pi3-data-certification-feature-breakdown]] shapes it **3.1 → 3.4**. The reconciliation: the **test code freeze runs through Aug 15** (mid-3.1), so no PROD deployment is possible early — the feature's *build* work correctly starts in 3.2. The only 3.1 work is **doc-only process-flow definition (SV-1)** off the 1480112 gap plan, which needs no deployment.

---

## Server starting position vs Computers (why this feature is not a straight clone)

Servers run in parallel with Computers, but the class is in a **stronger and messier** position:

- **Ahead on remediation:** recent work took Server **Location 44%→100%** and **IP 43%→91%** — the ownership/location gaps that dominate Computers are largely closed on Servers.
- **One Mandatory attribute — `environment`:** per the delivered Data Dictionary, Server is the only class with a **Mandatory** managed attribute. Its designation is **unresolved** — an open spike ([[server-environment-mandatory-spike]]) questions whether it is integration-fed (audit shows Missing Environment ≈11,665) and whether "Mandatory" means *scoring weight* or an *enforced save-time constraint*. This directly affects what the certification attests to → **DEP-7**.
- **Disputed active count:** dictionary shows **3,917** active servers; the audit dashboard scopes **15,218**. The certification scope must land on one reconciled number → **DEP-5**.

---

## CO6 Acceptance Criteria this feature delivers (Sep 30)

From [[PI-3/pi3-objectives]] — Obj 3 (CO6 §4), Sep 30 gate:

> *Data certification process for **Servers**: end-to-end process documented, technical build to PROD, dashboards live, training delivered.*

"Certified" = all four artifacts present for the Server class:

| Artifact | Delivered by |
|----------|--------------|
| Documented process flow | SV-1 |
| Technical build in PROD | SV-2 |
| Tracking dashboard live | SV-3 |
| Certification cycle executed + monitored | SV-4 |
| Training delivered | SV-5 |

---

## ADO item reconciliation note

Clones the **PI-2 Business-Application certification pilot pattern**; no net-new *process* is invented. Reusable story shapes (from the feature breakdown):

| PI-2 pilot item | Shape it provides | Clones to |
|-----------------|-------------------|-----------|
| 1480112 | Servers audit-dashboard scope + gap-remediation plan (**anchor**) | Input to SV-1 (see DEP-1) |
| 1402962 | Kick-off / training | SV-5 |
| 1402976 | Execute certification policies | SV-2 / SV-4 |
| 1402980 | Monitor completeness | SV-4 |
| 1402984 | Office hours | SV-5 |
| 1402985 | Process feedback | optional SV-6 |
| 1402727 | Dashboard | SV-3 |

Stories SV-1 through SV-5 are **net-new** for the Server class — the pilot shapes re-scoped from Business Application to `cmdb_ci_server` (Windows + Linux inherit additively from the parent class).

---

## Stories (5 + 3 draft)

---

### SV-1 · [User Story] Document the Server Data Certification process flow

| Field | Value |
|-------|-------|
| ADO ID | **1535496** |
| Type | User Story (shows as **Spike** in ADO — naming drift only) |
| Parent feature | 1517032 |
| Sprint | 3.1 (doc-only — no PROD dependency) — as planned |
| Owner | Bhushan Salsekar (confirm) |
| Points | 2 |
| State | Ready DoR (confirmed 2026-08-05) |
| ADO note | Created in ADO as 1535496 — clones the BA pilot process definition, re-scoped to Server |
| Depends on | DEP-1 (1480112 gap plan), DEP-5 (Class Manager), DEP-7 (Environment ruling) |
| Tags | `Data-Certification` `Server` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the end-to-end Server data-certification process documented — trigger, attestation steps, roles, escalation, and remediation path — built off the 1480112 gap-remediation plan,
**So that** the certification campaign for the Server class runs on an agreed, repeatable workflow before any PROD configuration is built.

**Acceptance criteria:**
- [ ] Process flow diagram covers the full cycle: campaign trigger → owner attestation → gap identification → remediation → re-attestation → sign-off
- [ ] Roles defined at each step (CI Owner, Technical Owner Group, Support Group, Process Owner) using the delivered Data Dictionary field mappings (`managed_by`, `managed_by_group`, `support_group`)
- [ ] Attested attribute set for Server confirmed against the delivered dictionary (10 managed attributes) and the 1480112 gap plan — no attribute drift
- [ ] **`environment` handling explicitly stated** — whether it is attested as Mandatory or Recommended, per the DEP-7 ruling; if unresolved, the process documents both branches
- [ ] Escalation and non-response handling defined
- [ ] Process documented in the agreed location and reviewed with the Server CCB Class Manager, Ray Reuter (DEP-5)
- [ ] Doc-only — no PROD change; demonstrable during the Aug 5–15 test freeze

**Dependencies:** DEP-1 (audit spike 1480112 gap plan), DEP-5 (Class Manager confirmation), DEP-7 (Environment Mandatory ruling).

---

### SV-2 · [Enabler – Configuration] Build Server certification policies/rules to PROD

| Field | Value |
|-------|-------|
| ADO ID | **1535499** |
| Type | Enabler – Configuration |
| Parent feature | 1517032 |
| Sprint | 3.2 — as planned |
| Owner | Bhushan Salsekar (confirm) |
| Points | 2 |
| State | Ready DoR (confirmed 2026-08-05) |
| ADO note | Created in ADO as 1535499 — clones pilot 1402976 (execute policies), re-scoped to Server |
| Depends on | SV-1, DEP-3 (Data Dictionary CCB), DEP-4 (test freeze lifts), DEP-7 (Environment ruling) |
| Tags | `Data-Certification` `Server` `Configuration` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the ServiceNow data-certification campaign, filters, and attestation rules for `cmdb_ci_server` configured and deployed to PROD,
**So that** Server CI owners can be issued attestation tasks against the agreed attribute set on a defined schedule.

**Acceptance criteria:**
- [ ] Certification definition/filter created scoping the reconciled active `cmdb_ci_server` population (DEP-5 resolves 3,917 vs 15,218); Windows + Linux inherit the parent-class attribute set additively
- [ ] Attestation rules configured for the Server managed attribute set per SV-1: CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Asset Tag (`asset_tag`), Value Stream (`business_unit`), SOX Type (`u_sox_type`), Data Classification (`classification`), Location (`location`), IP Address (`ip_address`), Environment (`environment`)
- [ ] **`environment` configured per the DEP-7 ruling** — as a scored Mandatory attribute, or Recommended, or Mandatory-on-manual-create-only — not enforced in a way that breaks Discovery/integration inserts
- [ ] Certification schedule configured (frequency + first run window) and documented
- [ ] Configuration migrated to PROD via a governed update set / change (post-freeze, on/after Aug 15 — DEP-4)
- [ ] Task routing verified — attestation tasks land with the correct owner group (`managed_by_group` / `support_group`)
- [ ] Dry-run on a bounded owner group confirms tasks generate and complete without error before full launch

**Dependencies:** SV-1, DEP-3 (attribute set locked by CCB), DEP-4 (test freeze), DEP-5 (active population), DEP-7 (Environment ruling).

---

### SV-3 · [Enabler – Configuration] Stand up the Server certification tracking dashboard

| Field | Value |
|-------|-------|
| ADO ID | **1535500** |
| Type | Enabler – Configuration |
| Parent feature | 1517032 |
| Sprint | 3.2 (created here, not 3.2→3.3 as planned) |
| Owner | Kiran (confirm) |
| Points | 1 (confirmed 2026-08-05) |
| State | Ready DoR (confirmed 2026-08-05) |
| ADO note | Created in ADO as 1535500 — clones pilot 1402727 (dashboard), re-scoped to Server |
| Depends on | SV-2 |
| Tags | `Data-Certification` `Server` `Dashboard` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** a live tracking dashboard for the Server certification cycle — coverage, attestation status, and outstanding gaps,
**So that** certification progress against the Sep 30 gate is visible to the team and stakeholders without manual reporting.

**Acceptance criteria:**
- [ ] Dashboard shows Server certification coverage: % attested, pending, and overdue against the scoped active population
- [ ] Outstanding-gap view surfaces the attributes driving non-certification (cross-checks the 1480112 audit gaps so remediation is not double-counted — DEP-1); reflects the closed Location/IP gaps and highlights Environment
- [ ] Dashboard reads from the live certification records created by SV-2 (not a static export)
- [ ] Coordinated with the CMDB Health Completeness (Server) config so the two do not build overlapping scoring — see [[cmdb-health-completeness-correctness-stories|CP-2]] (DEP-6)
- [ ] Dashboard reviewed with PO (Joe Dames) and confirmed as the reporting source for the Sep 30 gate
- [ ] Refresh cadence confirmed — scores update on schedule, not stale

**Dependencies:** SV-2 (records must exist to report on), DEP-1 (audit-gap alignment), DEP-6 (CP-2 coordination).

---

### SV-4 · [User Story] Run the Server certification cycle and monitor completeness

| Field | Value |
|-------|-------|
| ADO ID | **1535502** |
| Type | User Story |
| Parent feature | 1517032 |
| Sprint | 3.3 — as planned |
| Owner | Bhushan Salsekar (confirm) |
| Points | 1 (confirmed 2026-08-05) |
| State | New (confirmed 2026-08-05) |
| ADO note | Created in ADO as 1535502 — clones pilot 1402980 (monitor completeness), re-scoped to Server |
| Depends on | SV-2, SV-3 |
| Tags | `Data-Certification` `Server` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the first Server certification cycle executed end-to-end with completeness monitored on the dashboard,
**So that** attestation is actively driven to the target coverage and the process is proven before the Sep 30 gate.

**Acceptance criteria:**
- [ ] First certification cycle launched to Server CI owners via the SV-2 configuration
- [ ] Attestation progress tracked on the SV-3 dashboard through the cycle
- [ ] Gaps surfaced during attestation routed to remediation per the SV-1 process; Environment gaps handled per the DEP-7 ruling
- [ ] Coverage reaches the agreed acceptance target for Servers (ties the 90%-coverage acceptance G3 — DEP-2); shortfall documented with cause if target not met
- [ ] Non-responding owners escalated per the SV-1 escalation path
- [ ] Cycle outcome (coverage %, gaps closed, gaps outstanding) recorded and reviewed at Sprint Review

**Dependencies:** SV-2 (PROD build), SV-3 (dashboard), DEP-2 (90%-coverage acceptance G3).

---

### SV-5 · [User Story] Deliver Server certification training to CI owners

| Field | Value |
|-------|-------|
| ADO ID | **1535504** |
| Type | User Story |
| Parent feature | 1517032 |
| Sprint | 3.4 — as planned |
| Owner | Joe Dames (PO) / Manuel Vazquez |
| Points | 3 |
| State | New (confirmed 2026-08-05) |
| ADO note | Created in ADO as 1535504 — clones pilot 1402962 (kick-off/training) + 1402984 (office hours), re-scoped to Server |
| Depends on | SV-2, SV-4 |
| Tags | `Data-Certification` `Server` `Training` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** Server CI owners trained on the certification process — how to attest, correct gaps, and use office hours,
**So that** owners can sustain certification independently and the CO6 "training delivered" artifact is satisfied for the Server class.

**Acceptance criteria:**
- [ ] Training material produced covering the Server certification workflow (attest, remediate, re-attest) per SV-1, including how `environment` is to be attested
- [ ] Training delivered to the Server CI owner / support-group audience; attendance or distribution recorded
- [ ] Office-hours / support channel established and communicated for attestation questions
- [ ] Quick-reference (job aid) distributed to owners
- [ ] Training completion evidenced for the Sep 30 gate (session recording, deck, or sign-off log)
- [ ] PO (Joe Dames) confirms the training artifact satisfies the CO6 Server certification acceptance criterion

**Gate note:** CO6 due Sep 30 lands on the 3.4/3.5 boundary → this story is the tight item; it must be **done by end of Sprint 3.4 (Sep 29)**.

---

### SV-6 · [User Story] Certify Servers with missing Location and IP Address *(draft)*

> **⚠️ Reconciliation flag (2026-09-28):** ADO **1603551** — *"CMDB: Certify Windows Servers with missing Location OR IP Address"* — already exists and covers overlapping ground: Windows-only scope, Technical Owner Group routing, both fields as certification fields, both required to complete. It differs from this draft in two ways: (1) **scope is Windows-only** (`cmdb_ci_win_server`), no Linux; (2) the **trigger is OR, not AND** — a server missing *either* field qualifies, not only servers missing both. Before building SV-6/7/8 as drafted, confirm with the PO whether 1603551 already supersedes this three-way split (at least for Windows) or whether a Linux equivalent and/or the narrower single-field policies (SV-7/SV-8) are still wanted alongside it. See SV-9 below, which documents 1603551 directly.

| Field | Value |
|-------|-------|
| ADO ID | _(not yet created)_ |
| Type | User Story |
| Parent feature | 1517032 |
| Sprint | TBD |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Tags | `Data-Certification` `Server` `CO6-Obj3` |

**As** a Configuration Manager,
**I want** a certification policy that asks the Technical Owner Group to confirm Location and IP Address on their active servers missing both,
**so that** those attributes stay accurate without manual audit.

**Acceptance criteria:**
1. Policy targets `cmdb_ci_win_server` and `cmdb_ci_linux_server` only — no other `cmdb_ci_server` child classes are in scope. Filtered to Install Status = Installed, Operational Status = Operational, Technical Owner Group is not empty, and Location and IP Address are both empty.
2. Certification fields are Location and IP Address only.
3. Display fields show Name, Serial Number, Operating System, Asset Tag, SOX Type, Data Classification, and Environment as read-only context.
4. Tasks route to the Technical Owner Group (`managed_by_group`).
5. Days to complete is set to 21. Instructions below.
6. Allow field updates is enabled, permitting the assigned group to correct values before certifying.
7. Allow empty field values is disabled, so certification cannot complete until Location and IP Address are entered.
8. The "CMDB Data Manager task assigned to you" notification reaches the assigned group.
9. The policy is named CMDB Cert — Servers — Location and IP Address, configured with On Demand scheduling, with its scheduled job discoverable by policy name.

**Instructions:**
> This server is missing its Location and IP Address in the CMDB. Please confirm and enter both values before the due date. If you are not the right owner for this CI, reassign the task to the correct Technical Owner Group.

---

### SV-7 · [User Story] Certify Servers with missing Location *(draft)*

| Field | Value |
|-------|-------|
| ADO ID | _(not yet created)_ |
| Type | User Story |
| Parent feature | 1517032 |
| Sprint | TBD |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Tags | `Data-Certification` `Server` `CO6-Obj3` |

**As** a Configuration Manager,
**I want** a certification policy that asks the Technical Owner Group to confirm Location on their active servers where it is missing,
**so that** Location stays accurate without manual audit.

**Acceptance criteria:**
1. Policy targets `cmdb_ci_win_server` and `cmdb_ci_linux_server` only — no other `cmdb_ci_server` child classes are in scope. Filtered to Install Status = Installed, Operational Status = Operational, Technical Owner Group is not empty, and Location is empty.
2. Certification field is Location only.
3. Display fields show Name, Serial Number, Operating System, Asset Tag, SOX Type, Data Classification, and Environment as read-only context.
4. Tasks route to the Technical Owner Group (`managed_by_group`).
5. Days to complete is set to 21. Instructions below.
6. Allow field updates is enabled, permitting the assigned group to correct values before certifying.
7. Allow empty field values is disabled, so certification cannot complete until Location is entered.
8. The "CMDB Data Manager task assigned to you" notification reaches the assigned group.
9. The policy is named CMDB Cert — Servers — Location, configured with On Demand scheduling, with its scheduled job discoverable by policy name.

**Instructions:**
> This server is missing its Location in the CMDB. Please confirm and enter the value before the due date. If you are not the right owner for this CI, reassign the task to the correct Technical Owner Group.

---

### SV-8 · [User Story] Certify Servers with missing IP Address *(draft)*

| Field | Value |
|-------|-------|
| ADO ID | _(not yet created)_ |
| Type | User Story |
| Parent feature | 1517032 |
| Sprint | TBD |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Tags | `Data-Certification` `Server` `CO6-Obj3` |

**As** a Configuration Manager,
**I want** a certification policy that asks the Technical Owner Group to confirm IP Address on their active servers where it is missing,
**so that** IP Address stays accurate without manual audit.

**Acceptance criteria:**
1. Policy targets `cmdb_ci_win_server` and `cmdb_ci_linux_server` only — no other `cmdb_ci_server` child classes are in scope. Filtered to Install Status = Installed, Operational Status = Operational, Technical Owner Group is not empty, and IP Address is empty.
2. Certification field is IP Address only.
3. Display fields show Name, Serial Number, Operating System, Asset Tag, SOX Type, Data Classification, and Environment as read-only context.
4. Tasks route to the Technical Owner Group (`managed_by_group`).
5. Days to complete is set to 21. Instructions below.
6. Allow field updates is enabled, permitting the assigned group to correct values before certifying.
7. Allow empty field values is disabled, so certification cannot complete until IP Address is entered.
8. The "CMDB Data Manager task assigned to you" notification reaches the assigned group.
9. The policy is named CMDB Cert — Servers — IP Address, configured with On Demand scheduling, with its scheduled job discoverable by policy name.

**Instructions:**
> This server is missing its IP Address in the CMDB. Please confirm and enter the value before the due date. If you are not the right owner for this CI, reassign the task to the correct Technical Owner Group.

---

### SV-9 · [User Story] Publish a Technical Owner Group KB article for completing Server certification tasks *(draft)*

| Field | Value |
|-------|-------|
| ADO ID | _(not yet created)_ |
| Type | User Story |
| Parent feature | 1517032 |
| Sprint | TBD |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Tags | `Data-Certification` `Server` `KB` `CO6-Obj3` |

**As** a Technical Owner Group member assigned a Server certification task,
**I want** a step-by-step knowledge article that shows me how to find my assigned task, review the server it's asking about, and enter or correct the requested values,
**so that** I can complete certification correctly on my own, without opening a ticket to ask how the process works.

**Acceptance criteria:**
1. KB article published in PPL's ServiceNow Knowledge Base (confirm space/category) and targeted at the Technical Owner Group audience — the group that receives Server certification tasks.
2. The worked example used throughout the article is **ADO 1603551** — *"CMDB: Certify Windows Servers with missing Location OR IP Address"* (policy name `CMDB Cert — Windows Servers — Location or IP Address`) — **Windows servers only** (`cmdb_ci_win_server`), where the task fires on Location **or** IP Address missing (either field alone qualifies), and both fields must be populated to complete certification.
3. Article explicitly explains the OR/AND distinction so owners aren't confused when a task shows a field that was already populated: **a server qualifies for the task if either Location or IP Address is missing**, but **both fields must show a value before the task can be certified** — the one already correct just needs confirming, the missing one needs to be entered.
4. Article covers, in order:
   - Where the task notification arrives ("CMDB Data Manager task assigned to you") and what it links to.
   - How to find assigned tasks without the notification — the group's task list in CMDB Workspace / Service Graph Workspace — for members who missed or deleted the email.
   - How to open a task and identify the correct server using the read-only display fields (Name, Serial Number, Operating System, Asset Tag, SOX Type, Data Classification, Environment).
   - How to tell which fields need action — Location and IP Address are editable and required; everything else is read-only context.
   - How to enter or correct Location and/or IP Address, and what happens if either is left blank (certification is blocked — "Allow empty field values" is disabled per 1603551 AC #7).
   - How to submit/certify the task once both fields are populated.
   - What to do if you're not the right owner for a CI — reassign the task to the correct Technical Owner Group, per 1603551's instruction text (confirm full wording — text supplied to date is truncated after "Please confirm and e...").
   - The 21-day completion window and what happens if it's missed (task auto-closes; OOB reminder behavior at 50/70/90% of days-to-complete, per the platform capability baseline already verified for Data Manager certification — confirm reminders fire the same way for Server policies).
5. All screenshots (task list view, task form, field layout, instructions text) are captured directly from the **live 1603551 policy** — confirm it's built and deployed before shooting screenshots, not a mockup.
6. Filter logic shown in the screenshots is verified against what 1603551 actually enforces, since its AC #1 doesn't explicitly state the Location/IP-Address-empty condition.
7. KB wording (roles, escalation, reassignment) matches SV-1's documented process flow.
8. Article is linked from the task assignment notification, same pattern as the Computer campaign's job aid ([[PI-3/pi3-physical-computer-data-validation-stories|PV-4]]).
9. Confirmed with SV-5's owner whether this article fulfills SV-5's "quick-reference job aid" criterion, so the two stories don't duplicate the same deliverable.

**Dependencies:** SV-1 (process flow this KB must match), ADO 1603551 (the example policy — confirm current state and that AC #6's filter gap is resolved before final screenshots), DEP-8 (if `managed_by_group` turns out not to be the correct assignment field, "Technical Owner Group" language throughout the article needs to change).

---

## Dependencies (8)

**Work item type:** Dependency · **Linked to:** Feature 1517032 (Blocked By) · **Area path:** A-INFOPS\FY26\PI3

Each dependency is stated as **Problem** (why it blocks) + **Acceptance criteria** (what "resolved" looks like), per SAFe.

---

### DEP-1 · Server audit-dashboard scope + gap-remediation spike (1480112) closed

| Field | Value |
|-------|-------|
| Title | [Dependency] Close Server audit spike 1480112 — Feature 1517032 |
| Assigned To | Anthony (Tony) (confirm) |
| Priority | 1 |
| State | ✅ **CLOSED** — 1480112 completed (ADO PI2.6, confirmed 2026-07-28) |
| Due Date | 2026-08-05 (met early) |

**RESOLVED (2026-07-28):** Spike 1480112 is closed (ADO PI2.6 board, parent "Data Certification Rollout (PI2)"). SV-1 (process-flow doc) is **no longer blocked by this dependency** — the Server gap-remediation plan is available to anchor it. Confirm the "reviewed with Class Manager" sub-criterion below was satisfied inside 1480112; if not, it rolls into DEP-5.

**Problem:** SV-1 documents the certification process *off the 1480112 gap-remediation plan*, and SV-3's dashboard cross-checks the same audit gaps. If 1480112 has not closed, the Server attribute gap picture is undefined and SV-1 cannot anchor to it — blocking the feature at story 1.

**Acceptance criteria:**
- [ ] Spike 1480112 completed and its Server gap-remediation plan published
- [ ] Server attribute gaps quantified (reflecting closed Location/IP gaps and the outstanding Environment gap) and available as SV-1/SV-3 input
- [ ] Gap plan reviewed with the Server CCB Class Manager, Ray Reuter (links DEP-5)

---

### DEP-2 · Servers 90%-coverage acceptance story (G3) created and accepted

| Field | Value |
|-------|-------|
| Title | [Dependency] Create + accept Servers 90%-coverage story (G3) — Feature 1517032 |
| Assigned To | Manuel Vazquez |
| Priority | 1 |
| State | Open (net-new — no formal story exists) |
| Due Date | 2026-08-19 |

**Problem:** The CO6 Server certification acceptance is evidenced by a 90%-coverage acceptance story (gate G3). No formal ADO story exists yet. Without an agreed coverage target and acceptance vehicle, SV-4's completeness cycle has no defined "done" and the feature cannot be signed off at the Sep 30 gate.

**Acceptance criteria:**
- [ ] 90%-coverage acceptance story for Servers (G3) created in ADO and linked to Feature 1517032
- [ ] Coverage target and measurement basis (which attributes — and whether Environment is included — which active population) agreed with PO (Joe Dames) and PM (Sonika Das)
- [ ] Story referenced as the acceptance target in SV-4
- [ ] Accepted at the appropriate Sprint Review as the Server certification evidence

---

### DEP-3 · Data Dictionary CCB approval — Server attribute set

| Field | Value |
|-------|-------|
| Title | [Dependency] Data Dictionary CCB approval covering Server attributes — Feature 1517032 |
| Assigned To | Manuel Vazquez / Josh Sterling (CCB Chair) |
| Priority | 1 |
| State | Open (delivered to PPL 2026-07-21; CCB vote pending) |
| Due Date | 2026-08-19 |

**Problem:** SV-2 configures attestation rules against the Server managed-attribute set. If the Data Dictionary is not CCB-approved, the certified attribute list — including the contested Environment designation — can still change under the team, forcing rework of the PROD build and invalidating early attestations.

**Acceptance criteria:**
- [ ] Data Dictionary CCB approval recorded covering the 10 Server managed attributes and their field mappings (`managed_by`, `managed_by_group`, `support_group`, `business_unit`, `classification`, `environment`, etc.)
- [ ] Environment's requirement designation resolved in the approved dictionary (coordinated with DEP-7)
- [ ] Approved attribute set matches the set configured in SV-2 — no drift
- [ ] Approval date and CCB decision referenced in SV-1 / SV-2

---

### DEP-4 · Test code freeze lifts (no PROD deploy before Aug 15)

| Field | Value |
|-------|-------|
| Title | [Dependency] Test code freeze through Aug 15 — Feature 1517032 |
| Assigned To | Manuel Vazquez |
| Priority | 2 |
| State | Open |
| Due Date | 2026-08-15 |

**Problem:** SV-2 requires a governed PROD deployment of the certification configuration. The test code freeze (PI-3 Risk #1, CHG70100865) runs through Aug 15 — the first 10 days of PI-3 — so no deployment can occur in early Sprint 3.1. This is why the feature's build start is Sprint 3.2, not 3.1.

**Acceptance criteria:**
- [ ] Freeze end date (Aug 15) confirmed unchanged; if extended, SV-2 sprint placement re-planned
- [ ] Deployment window for the certification update set secured on/after Aug 15
- [ ] SV-1 (doc-only) confirmed as the only 1517032 work scheduled during the freeze

---

### DEP-5 · Class Manager confirms attribute set + reconciled active-population count

| Field | Value |
|-------|-------|
| Title | [Dependency] Ray Reuter sign-off — Server attribute set + active scope (3,917 vs 15,218) — Feature 1517032 |
| Assigned To | Manuel Vazquez |
| Priority | 2 |
| State | Open |
| Due Date | 2026-08-19 |

**Problem:** SV-2's scoped population must be ratified by the Server CCB Class Manager (Ray Reuter). The active-server count is **disputed** — the delivered dictionary shows 3,917 while the audit dashboard scopes 15,218 (Missing Environment 11,665 is measured against the larger set). Certifying against the wrong population invalidates the coverage %.

**Acceptance criteria:**
- [ ] Ray Reuter confirms the Server managed-attribute set to be certified
- [ ] The 3,917 vs 15,218 discrepancy explained — exact `install_status` / `operational_status` filter behind each figure agreed with Ray / Stan, and one scored population fixed for certification
- [ ] Any attribute an owner cannot reasonably attest to flagged and dispositioned before SV-2 build

---

### DEP-6 · Coordinate with CMDB Health Completeness (Server) config — CP-2

| Field | Value |
|-------|-------|
| Title | [Dependency] Align cert dashboard with CMDB Health Completeness CP-2 — Feature 1517032 |
| Assigned To | Manuel Vazquez |
| Priority | 3 |
| State | Open — CP-2 exists in ADO as **US 1520424** (Validation) |
| Due Date | 2026-08-19 |

**Problem:** The CMDB Health **Completeness (Server)** KPI ([[cmdb-health-completeness-correctness-stories|CP-2]] = ADO **1520424**, parent "Governance Validation & Acceptance"; and the linked `environment` Spike **1526856**) scores the same Server attribute population that SV-3's certification dashboard reports on. Building the two independently risks overlapping/contradictory scoring of the same gaps.

**Acceptance criteria:**
- [ ] SV-3 and CP-2 owners agree which artifact is authoritative for "attribute populated" scoring vs "owner attested"
- [ ] No double-counting of the same Server gap across the certification dashboard and the CMDB Health completeness score
- [ ] Coordination decision recorded (ADO comment) and reflected in SV-3 acceptance

---

### DEP-7 · Resolve the Server `environment` Mandatory designation (spike)

| Field | Value |
|-------|-------|
| Title | [Dependency] Resolve Server `environment` Mandatory ruling — Feature 1517032 |
| Assigned To | Stan Tomberg (technical) w/ Ray Reuter (requestor) (confirm) |
| Priority | 2 |
| State | Open — created in ADO as **Spike 1526856** (New; parent "Governance Validation & Acceptance") — [[server-environment-mandatory-spike]] |
| Due Date | 2026-08-19 |

**Problem:** `environment` is the only Mandatory Server managed attribute, but its designation is unresolved: (a) it is normally non-discoverable, (b) the delivered slide names no source, (c) audit shows ≈11,665 missing — inconsistent with a reliable integration feed. Two open questions block the build: *what is the source* (integration vs manual), and *does "Mandatory" mean scored-weight or an enforced save-time constraint*. If SV-2 configures Environment as enforced-Mandatory and it is not integration-fed, it can break Discovery/integration inserts and block server creation; if it is attested but unpopulated, it drags Server coverage below the DEP-2 target for reasons owners cannot fix.

**Acceptance criteria:**
- [ ] Spike [[server-environment-mandatory-spike]] completed: source of `cmdb_ci_server.environment` identified with evidence; SCCM hypothesis confirmed or denied
- [ ] "Mandatory" interpretation confirmed with Ray / CCB — scoring designation vs enforced field constraint
- [ ] Enforcement mode decided (scored-only, Recommended, or Mandatory-on-manual-create-only) so SV-2 can configure without breaking inserts
- [ ] Decision fed into DEP-3 (dictionary) and SV-1/SV-2/SV-4; [[cmdb-health-completeness-correctness-stories|CP-2]] updated to match

---

### DEP-8 · Confirm `managed_by_group` vs `support_group` for certification task assignment

| Field | Value |
|-------|-------|
| Title | [Dependency] Confirm assignment group field (`managed_by_group` vs `support_group`) — Feature 1517032 |
| Assigned To | Manuel Vazquez |
| Priority | 3 |
| State | Open — **working assumption in use: `managed_by_group`, not yet confirmed** |
| Due Date | TBD |

**Problem:** SV-2's certification tasks need a group-field assignment to spread attestation load beyond a single named CI Owner (e.g., Ray individually owns 2,510 Windows servers). `managed_by_group` (Technical Owner Group) and `support_group` (ITSM Support Group) are confirmed to be **"mostly the same group, although not always"** (2026-09-10, per Q5 on [[Config-Mgmt-Plan/ownership-terminology-mapping]]). For the servers where they diverge, `support_group` is the field that drives real operational routing (incidents, etc.); `managed_by_group` is documented elsewhere as a lower-impact governance/reporting field. Assigning on the wrong one in the divergent slice risks routing certification to a group not actually engaged with the CI. Proceeding on `managed_by_group` as a working assumption for now — not yet verified as correct, and the divergent population has not been quantified.

**Acceptance criteria:**
- [ ] Quantify the Server population where `managed_by_group` and `support_group` diverge
- [ ] Confirm with Ray Reuter / class managers which field should drive certification task assignment
- [ ] Confirm how CMDB Data Manager technically handles assignment to a group field (shared task any member can complete vs. fan-out) before relying on it to "share the burden"
- [ ] SV-2 updated if the working assumption (`managed_by_group`) turns out to be wrong

---

## Sequence summary

```
DEP-1 (Aug 5, 1480112 gap plan) ─┐
DEP-5 (Ray — attr set + count) ──┤
DEP-7 (Environment ruling) ──────┼─► SV-1 (process flow, 3.1 doc-only)
DEP-3 (Data Dictionary CCB) ──────┤        │
DEP-4 (freeze lifts Aug 15) ──────┴────────┼─► SV-2 (PROD build, 3.2)
                                            │        │
                                            │        ├─► SV-3 (dashboard, 3.2→3.3) ◄── DEP-6 (CP-2 align)
                                            │        │        │
DEP-2 (90% acceptance G3) ──────────────────┘        └────────┼─► SV-4 (run cycle + monitor, 3.3)
                                                              │        │
                                                              └────────┴─► SV-5 (training, 3.4) ── done by Sep 29
```

**Freeze-window rule:** only SV-1 (doc-only) runs during the Aug 5–15 test freeze. All PROD work (SV-2 onward) starts Sprint 3.2.
**Gate:** CO6 Sep 30 lands on the 3.4/3.5 boundary → the feature must be **done by end of Sprint 3.4 (Sep 29)**; SV-5 training is the tight item.
**Server-specific critical path:** DEP-7 (Environment ruling) gates SV-1 *and* SV-2 — if the spike is not resolved by ~Aug 19, the build either stalls or proceeds on an assumption that may force rework. Raise DEP-1/DEP-2/DEP-3/DEP-7 (all PI-2 carryover or open spikes) at PI Planning (IP Iteration, Jul 22–Aug 4).
