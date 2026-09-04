---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1517029 — Certify Computers — CMDB Data Certification (proposed parent)"
objective: CO6 Obj 3 — Expand CI Data Certification Across All Major Classes
sprint: "3.3 (spike + build); 3.4 (pilot)"
co6-due: 2026-09-30
status: draft
updated: 2026-09-02
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification]
relationships:
  - target: "[[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]]"
    type: extends
  - target: "[[Config-Mgmt-Plan/configuration-management-plan-stage1]]"
    type: related_to
  - target: "[[Backlog/audit-dashboard-computer-spike]]"
    type: derived_from
  - target: "[[PI-3/pi3-objectives]]"
    type: related_to
---

# Physical Computer Data Validation — Stories & Dependencies

**End-user validation of Location and Asset Tag on physical `cmdb_ci_computer` CIs**
Proposed parent: Feature 1517029 · Sprint 3.3–3.4 · Owner: M. Vazquez

> **Status: DRAFT** — not created in ADO. ADO IDs are placeholders. Reconcile back to this file on creation, per [[Backlog/definition-of-ready]] (create stories from the Feature "+" link, never standalone).

> **Parentage is a reversible decision.** Proposed under **Feature 1517029 (Certify Computers)** because this delivers the Computer certification technical build that 1517029's CO6 acceptance criterion already calls for, and because **CC-2 currently claims overlapping scope** (see Reconciliation below). If the CCB or PO would rather isolate end-user-facing validation from owner certification, this lifts out to its own feature without changing any story content.

---

## What this delivers

Every PPL employee with a physical computer assigned to them receives a task asking them to confirm two attributes about their own device:

| Attribute | Field | Treatment |
|---|---|---|
| Location | `location` | **Editable** — dropdown of approved locations, pre-filled where populated |
| Asset Tag | `asset_tag` | **Editable** — pre-filled where populated |

Everything else is shown as read-only context so the employee can identify the device: Name, Serial Number, Model ID, Operating System, Assigned To, CI Owner, Technical Owner Group, Support Group.

**Why the end user.** The recorded root cause for Computer Location being 66% complete is HR system limitations (2026-07-16 audit status meeting). If HR data cannot establish where a laptop physically sits, the person holding it is the remaining authoritative source. This is a targeted answer to a documented audit gap, not a new lane of work.

**Gap being closed** (from spike 1480114): Location empty **17,513** · Missing Asset Tag **8,275**.

---

## Platform capability basis (verified against ServiceNow docs, 2026-09-02)

This is **OOB CMDB Data Manager**, honoring the standing *"Data Certification: stay OOTB"* decision. No custom form, no custom table, no modification of certification code. Verified against the Zurich documentation set:

| Capability | Confirmed |
|---|---|
| `Certification` is a CMDB Data Manager policy type | Yes — alongside Delete, Attestation, Archive, Retire, Delete CMDB Related Entry |
| **Display fields** — identifying context shown in task list views | Yes |
| **Certification fields** — the attributes requiring verification | Yes |
| Display and Certification fields **cannot overlap** | Yes — constrains field layout |
| **Allow field updates** — reviewer may correct values to certify | Yes — this is what makes Location/Asset Tag editable |
| **Allow empty field values** — whether a blank attribute can be certified | Yes — policy-level setting |
| Assignment to a **user field on the record** (e.g. `assigned_to`) | Yes — "User Field" assignment option |
| OOB notification **"CMDB Data Manager task assigned to you"**, includes task link | Yes — active by default |
| OOB reminders at 50% / 70% / 90% of `Days to complete`, plus past-due to user **and manager** | Yes — `sn_cmdb_ws.cmdb.dm.policy_types.due_date_notification` |
| Max **10,000 CIs per task**; excess auto-splits into additional tasks | Yes |
| Stale tasks auto-close after **90 days** | Yes |

**Known platform constraints carried into the stories below:**

1. **Reviewers work in CMDB Workspace / Service Graph Workspace**, documented roles `data_manager_user` + `sn_cmdb_editor`. Extending this to the full employee population is a role and licensing question, not a configuration question — **PV-1 exists to answer it and blocks everything else.**
2. **Notification setup is global**, on the CMDB Data Manager Settings page — not per-policy. Campaign-specific email copy means editing the underlying notification records.
3. **KB2701247** documents notifications not firing for CMDB Workspace data certification. Verify in-instance; do not assume.
4. **Field-level certification status is not readily reportable** — community guidance indicates the per-attribute status field needs unpacking via script to report on "which attribute was certified." Affects CC-3's dashboard.
5. **Legacy vs. Data Manager certification** are two different implementations with a documented conversion path. Which one PPL is on changes the build. Confirm first.

---

## Reconciliation with CC-1…CC-5 (read before creating anything in ADO)

Feature 1517029 already has five stories. These new stories are **additive and non-duplicative**, but three existing stories need amendment rather than duplication:

| Existing | Current scope | Action |
|---|---|---|
| **CC-1** (1535486) — process flow doc | Documents the Computer certification process | **Amend** — add the end-user validation path as a distinct actor/flow alongside owner attestation |
| **CC-2** (1535488) — build certification policies to PROD | *"Certification definition/filter created scoping the active `cmdb_ci_computer` population (≈19,901)"* + attestation rules for all 9 attributes | **⚠️ Direct overlap.** CC-2 was drafted before the Display/Certification-field and `assigned_to`-assignment capability was confirmed. Either narrow CC-2 to owner-attested governance attributes and let **PV-3** own the end-user policy, or absorb PV-3 into CC-2 and re-point it. **Decide at refinement — do not create PV-3 alongside an unamended CC-2.** |
| **CC-3** (1535489) — certification dashboard | Coverage, attestation status, gaps | **Amend** — add physical/virtual breakout and per-attribute status; carry constraint #4 above as a risk |
| **CC-4** (1535490) — run cycle + monitor | First certification cycle end-to-end | **Amend** — PV-5 pilot feeds this; CC-4 becomes the full-population cycle |
| **CC-5** (1535491) — training | Aimed at *CI owners / support groups* | **Amend** — an all-employee campaign needs different comms (see PV-4); CC-5's owner-facing training is not a substitute |

---

## Stories (5 + 1 deferred)

---

### PV-1 · [Spike] Confirm role, workspace-access, and licensing feasibility for end-user certification reviewers

| Field | Value |
|-------|-------|
| ADO ID | _(net-new — not yet created)_ |
| Type | Spike |
| Parent feature | 1517029 |
| Sprint | 3.3 |
| Owner | Manuel Vazquez (w/ Stan Tomberg, Sonika Das) |
| Points | 3 |
| State | Draft |
| Tags | `Data-Certification` `Computer` `Spike` `CO6-Obj3` |

**As** the CMDB Product Owner,
**I want** confirmation of what roles, workspace access, and licence entitlement a standard PPL employee needs to open and complete a CMDB Data Manager certification task,
**So that** we know whether end-user validation is deliverable on OOB Data Certification before any policy is built against that assumption.

**Acceptance criteria:**
- [ ] Documented role set required for a non-IT employee to complete a certification task in CMDB Workspace / Service Graph Workspace (baseline: `data_manager_user`, `sn_cmdb_editor` — confirm sufficiency and whether `itil` is additionally required)
- [ ] Licence impact confirmed **in writing** with the ServiceNow account team — does granting these roles to ~21,000 employees consume fulfiller licences?
- [ ] Tested end-to-end with **one** real non-IT test user in a sub-prod instance: receives notification, opens task, edits Location, certifies successfully
- [ ] Confirmed whether PPL is on **legacy Data Certification** or **Data Manager certification policies** (constraint #5) — determines the build target
- [ ] OOB notification delivery verified in-instance against **KB2701247** (constraint #3)
- [ ] Security review position obtained on granting CMDB editor roles broadly (Jason Dubreuil, CCB Cybersecurity consulting member)
- [ ] **Outcome recorded as a go / no-go**: if licensing or security blocks broad role grants, PV-3 is re-scoped to a Service Catalog record producer and this file is revised before build

**Dependencies:** DEP-1 (licensing answer), DEP-6 (legacy vs. Data Manager).

> **This spike gates PV-2 through PV-6.** It is the single highest-value item in the set — a no-go answer invalidates the OOB approach and changes the solution, not just the estimate. Front-load it in 3.3.

---

### PV-2 · [Enabler – Configuration] Curate the approved location list for end-user selection

| Field | Value |
|-------|-------|
| ADO ID | _(net-new — not yet created)_ |
| Type | Enabler – Configuration |
| Parent feature | 1517029 |
| Sprint | 3.3 |
| Owner | Stan Tomberg / Bhushan Salsekar (confirm) |
| Points | 3 |
| State | Draft |
| Tags | `Data-Certification` `Computer` `Configuration` `CO6-Obj3` |

**As** an employee validating my computer's location,
**I want** a short, recognizable list of approved locations to choose from,
**So that** I can pick the right answer quickly and the resulting data is reportable rather than free text.

**Context:** `cmdb_ci.location` is a **reference field to `cmn_location`** — free text is not possible, and is not wanted. Uncurated, the picker exposes every location record in the instance; 17,513 users each free-associating produces populated-but-unreportable data, which does not move the audit metric.

**Acceptance criteria:**
- [ ] Current `cmn_location` population reviewed for granularity — confirm whether records exist at the level an employee can actually recognize (site / building / floor) rather than only legal-entity or region level
- [ ] Approved, user-selectable location set agreed with the Computer Class Manager (Monica Green) and facilities/real-estate source of truth
- [ ] Selection constrained via reference qualifier or an equivalent flag on `cmn_location` (e.g. `u_user_selectable`) — the employee picker shows only the approved set, not the full table
- [ ] **Remote / home-office option present** — a materially large share of the population is not in a PPL facility; without this option remote workers will select a wrong site, which is worse than a blank
- [ ] Any location an employee needs but that does not exist is created, or an escape path is defined (comment field / "my location isn't listed")
- [ ] Approved list documented and referenced in PV-3's policy configuration
- [ ] Confirmed the qualifier does **not** break Location population on other CI classes or via Asset Management integrations

**Dependencies:** DEP-3 (`cmn_location` granularity), DEP-4 (Class Manager sign-off).

---

### PV-3 · [Enabler – Configuration] Build the physical-computer certification policy in CMDB Data Manager

| Field | Value |
|-------|-------|
| ADO ID | _(net-new — not yet created)_ |
| Type | Enabler – Configuration |
| Parent feature | 1517029 |
| Sprint | 3.3 → 3.4 |
| Owner | Bhushan Salsekar (confirm) |
| Points | 5 |
| State | Draft |
| Tags | `Data-Certification` `Computer` `Configuration` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** a CMDB Data Manager certification policy that targets physical `cmdb_ci_computer` CIs, assigns tasks to the user in `assigned_to`, and permits that user to correct Location and Asset Tag,
**So that** the two largest Computer attribute gaps are closed by the only population that reliably knows the answers.

**Acceptance criteria:**

*Scope*
- [ ] Policy targets the **Computer class** with a filter isolating **physical** devices only — virtual excluded
- [ ] Filter explicitly resolves whether scope is `cmdb_ci_computer` **exact class only** or **class and descendants** (e.g. `cmdb_ci_pc_hardware`); PPL's physical PCs may sit in a child class, in which case exact-class-only silently scopes to zero. Mirror the exact-class treatment used in [[PI-3/pi3-nd-1356646-stories-dependencies|CR-4]]
- [ ] Physical/virtual determination method agreed and documented (DEP-2) — reconciles to the audit dashboard's 28,203 total / 6,530 virtual split, and the divergence from the dictionary's 19,901 figure is explained, not ignored
- [ ] CIs with `assigned_to` **empty are excluded** from this policy and counted — they route to PV-6, not to a task with no recipient
- [ ] **Recency filter — include only CIs seen by an endpoint source within the last 45 days.** Rationale: 45 days absorbs vacation and short-term leave, while excluding devices no longer in use. Devices outside the window are excluded **and counted**, not silently dropped
- [ ] **Authoritative last-seen field confirmed (DEP-8)** — PPL Computers are sourced from SCCM/Intune Service Graph Connector, Jamf, and Agent Client Collector, **not** ServiceNow Discovery, so `last_discovered` may not be the field those connectors stamp. Confirm before building the filter. Same open question [[PI-3/pi3-nd-1356646-stories-dependencies|CR-6]] carries for network gear — resolve both consistently
- [ ] **`u_off_network` interaction assessed** — the PPL custom flag marks devices operating off-network. An off-network device will not report to SCCM and will fail a 45-day recency test while remaining a live, assigned asset. Decide whether `u_off_network = true` is an exception to the recency filter or is excluded with the rest
- [ ] Excluded-by-recency population quantified and routed to PV-6 / lifecycle review — these are retirement candidates, not validation candidates
- [ ] Recency evaluated at **policy execution time** — a device at day 44 on execution may be well past 45 days by the time the employee responds. Acceptable, but documented rather than discovered
- [ ] **Final campaign denominator stated as an explicit formula** — active physical Computer − no `assigned_to` − not seen in 45 days — and disclosed wherever coverage is reported, so the ≥90% figure is always read against a known population

*Field configuration*
- [ ] **Certification fields:** `location`, `asset_tag`
- [ ] **Display fields:** `name`, `serial_number`, `model_id`, `os`, `assigned_to`, CI Owner, `managed_by_group`, `support_group` — no overlap with Certification fields
- [ ] CI Owner field binding resolved — `owned_by` or `managed_by` (see Open Items); the dictionary and CC-1 must agree with what is configured
- [ ] **Allow field updates = enabled** — this is the setting that makes correction possible
- [ ] **Allow empty field values** decision made and recorded: disabled forces a value before certification (drives remediation, risks abandonment); enabled permits certify-with-blank (protects completion rate, weakens the outcome). Recommend **disabled**, since a blank Location is the gap being closed
- [ ] Pre-filled current values confirmed visible to the reviewer — an employee confirming an already-correct Location must be able to see it and certify without retyping

*Assignment, schedule, delivery*
- [ ] Assignment configured as **User Field → Assigned to**
- [ ] Confirmed behavior for a user with **multiple assigned devices** — expected to be one task listing all their CIs, not one task per device; verify before comms go out, as it changes email volume
- [ ] `Days to complete` set, with the resulting 50/70/90% reminder milestones documented and acceptable
- [ ] Schedule set (initial run window + recurrence); recurrence establishes the re-validation cadence that makes this a standing control rather than a one-off
- [ ] 10,000-CI-per-task cap and 90-day stale-task auto-close both confirmed as non-issues for the chosen assignment model, or handled

*Write-back integrity*
- [ ] **Asset Tag write-path resolved** — `asset_tag` exists on both the CI and the related `alm_hardware` asset record, kept aligned by CI–Asset sync. Confirm which is authoritative at PPL and that certifying on the CI does not leave Asset Management stale. Two systems disagreeing is worse than the original blank
- [ ] Field-level history confirmed captured in `sys_audit` for both certified attributes — this is the audit evidence
- [ ] A `last validated` timestamp is stamped per CI on successful certification (custom attribute if not OOB) so re-validation cadence and staleness are measurable
- [ ] Deployed to PROD via governed update set / change

**Dependencies:** PV-1 (go/no-go — hard gate), PV-2 (location list), DEP-2 (physical/virtual split), DEP-4 (Class Manager sign-off), DEP-5 (asset sync direction), DEP-8 (last-seen field).

---

### PV-4 · [Enabler – Configuration] Notifications and employee communications for the validation campaign

| Field | Value |
|-------|-------|
| ADO ID | _(net-new — not yet created)_ |
| Type | Enabler – Configuration |
| Parent feature | 1517029 |
| Sprint | 3.4 |
| Owner | Manuel Vazquez (w/ Nora Lizenberg, OCM) |
| Points | 3 |
| State | Draft |
| Tags | `Data-Certification` `Computer` `OCM` `CO6-Obj3` |

**As** an employee receiving a request to validate my computer,
**I want** a clear, plainly written email that tells me why I'm being asked and takes me straight to the task,
**So that** I complete it rather than ignore it or raise a ticket asking what it is.

**Context:** the OOB notification *"CMDB Data Manager task assigned to you"* is active by default and includes a task link. But notification setup is **global** (Data Manager Settings), not per-policy — campaign-specific copy means editing the notification records. Default platform wording is not appropriate for a company-wide employee audience.

**Acceptance criteria:**
- [ ] OOB assignment notification confirmed **firing in-instance** (explicitly tested against KB2701247 before relying on it)
- [ ] Notification body rewritten for a non-technical employee audience — what's being asked, why, how long it takes, who to contact; no CMDB jargon
- [ ] Task link verified to land the employee **on the task they can actually act on**, given the PV-1 role outcome
- [ ] Reminder cadence (50/70/90% + past-due) reviewed and confirmed appropriate; past-due notification copies the employee's **manager** — confirm this escalation is acceptable to HR/OCM **before** launch, as it is on by default
- [ ] Global notification changes assessed for impact on **other** Data Manager policies (Server, Database, Network certification) — this is shared configuration, not campaign-scoped
- [ ] Communications plan reviewed and approved by **OCM (Nora Lizenberg)** — a mass email to every PPL employee with a device is a company-wide communication, not a team artifact
- [ ] Service Desk pre-briefed with a response script; expected contact volume estimated
- [ ] Employee-facing FAQ / job aid published and linked from the notification

**Dependencies:** PV-1, PV-3, DEP-7 (OCM approval).

---

### PV-5 · [User Story] Run a bounded pilot cycle and validate the end-to-end experience

| Field | Value |
|-------|-------|
| ADO ID | _(net-new — not yet created)_ |
| Type | User Story |
| Parent feature | 1517029 |
| Sprint | 3.4 |
| Owner | Bhushan Salsekar / Manuel Vazquez |
| Points | 3 |
| State | Draft |
| Tags | `Data-Certification` `Computer` `Pilot` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the validation cycle proven on a bounded group of real employees before it goes to the full population,
**So that** a mistake reaches 50 people instead of 21,000.

**Acceptance criteria:**
- [ ] Pilot group agreed with Monica Green — a real cross-section including at least one remote worker and one user with multiple devices
- [ ] Pilot executes end to end: policy runs → task created → notification received → employee opens and edits → certification completes → CMDB updated
- [ ] Location and Asset Tag changes confirmed written to the CI **and** reconciled with Asset Management (PV-3 write-path criterion holds in practice)
- [ ] Completion rate, time-to-complete, and abandonment measured
- [ ] Employee feedback collected on clarity — specifically whether the location list contained their answer
- [ ] Service Desk contact volume from the pilot recorded and extrapolated
- [ ] Defects and copy fixes remediated before full launch
- [ ] Go / no-go for full-population launch recorded with PO (Joe Dames), feeding **CC-4** as the full cycle

**Dependencies:** PV-3, PV-4.

---

### PV-6 · [User Story] Remediation path for physical computers with no Assigned To *(candidate to defer)*

| Field | Value |
|-------|-------|
| ADO ID | _(net-new — not yet created)_ |
| Type | User Story |
| Parent feature | 1517029 |
| Sprint | 3.5 (candidate to defer to PI-4) |
| Owner | TBD |
| Points | 5 |
| State | Draft — recommend explicit defer decision |
| Tags | `Data-Certification` `Computer` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** a defined path for physical computers with no `assigned_to` value,
**So that** the ~29% of the population this campaign cannot reach is deliberately handled rather than silently excluded from the coverage denominator.

**Context:** 8,166 active Computer CIs have Assigned To empty (spike 1480114). No end-user validation is possible for these — there is no user to send to. Reporting campaign coverage without accounting for them overstates completeness.

**Second excluded population (added 2026-09-02):** PV-3's 45-day recency filter excludes physical computers not seen by an endpoint source inside the window. Both exclusions funnel here, and both are the same underlying question — *does this device still exist and is it still in use?* A device unseen for 45+ days **and** unassigned is a near-certain retirement candidate. Handle them as one population with one disposition path, not two.

**Acceptance criteria:**
- [ ] The no-`assigned_to` population quantified for physical computers specifically (the 8,166 figure spans the full Computer population)
- [ ] The **not-seen-in-45-days** population quantified for physical computers, and its overlap with the no-`assigned_to` set measured — the two are expected to overlap heavily; the union, not the sum, is the population to disposition
- [ ] Root cause categorized: genuinely unassigned / shared-use device / stale record that should be retired / SCCM data gap
- [ ] Records that should be **retired** routed to CMDB Data Manager lifecycle policies rather than validation — likely the largest sub-population
- [ ] Remaining records routed to Support Group or Technical Owner Group for owner assignment
- [ ] Population explicitly reported in the CC-3 dashboard as out-of-scope-for-end-user-validation, so coverage is not overstated
- [ ] Defer decision recorded if not taken this PI

**Dependencies:** PV-3 (exclusion list is its output).

---

## Dependencies (8)

**Work item type:** Dependency · **Linked to:** Feature 1517029 (Blocked By) · **Area path:** A-INFOPS\FY26\PI3

---

### DEP-1 · Licensing and role entitlement answer for broad certification-reviewer access

| Field | Value |
|-------|-------|
| Assigned To | Manuel Vazquez / Sonika Das |
| Priority | **1** |
| State | Open |
| Due Date | 2026-09-15 |

**Problem:** Certification reviewers work in CMDB Workspace with `data_manager_user` + `sn_cmdb_editor`. If granting those roles to ~21,000 employees consumes fulfiller licences or is refused on security grounds, the entire OOB approach is invalid and the solution becomes a Service Catalog record producer. Every other story in this set assumes the answer is yes.

**Acceptance criteria:**
- [ ] Written confirmation from the ServiceNow account team on licence consumption for these roles at employee scale
- [ ] Security position from Jason Dubreuil (CCB Cybersecurity) on broad CMDB editor role grants
- [ ] Decision recorded; if no-go, PV-3 re-scoped and this file revised before any build starts

---

### DEP-2 · Physical vs. virtual determination method for the Computer class

| Field | Value |
|-------|-------|
| Assigned To | Stan Tomberg / Anthony de Araujo |
| Priority | 1 |
| State | Open — carried from spike 1480114 |
| Due Date | 2026-09-15 |

**Problem:** PV-3's filter depends on a reliable physical/virtual split. Spike 1480114 flagged validating this split as an open item and it does not appear closed. Three population figures are in circulation — 28,203 active Computer, 6,530 active virtual, 19,901 per the delivered dictionary — and they do not reconcile. Building a policy on an unvalidated filter risks certifying the wrong population.

**Acceptance criteria:**
- [ ] Physical/virtual determination method documented (class-based, hardware attribute, or other)
- [ ] The three population figures reconciled or their differences explained
- [ ] Whether physical PCs sit in `cmdb_ci_computer` or a child class such as `cmdb_ci_pc_hardware` confirmed
- [ ] Resulting physical-only count agreed with Monica Green as the campaign denominator

---

### DEP-3 · `cmn_location` granularity sufficient for employee self-selection

| Field | Value |
|-------|-------|
| Assigned To | Stan Tomberg (w/ facilities contact TBD) |
| Priority | 2 |
| State | Open |
| Due Date | 2026-09-15 |

**Problem:** If `cmn_location` only holds site- or region-level records, employees cannot find a meaningful answer and will either abandon the task or pick something wrong. Response quality depends entirely on the picker containing recognizable options.

**Acceptance criteria:**
- [ ] Existing `cmn_location` records inventoried by granularity level
- [ ] Gap between available records and what an employee would recognize assessed
- [ ] Decision on creating additional location records, or accepting coarser granularity with a documented limitation

---

### DEP-4 · Computer Class Manager sign-off — scope, attribute set, and approved locations

| Field | Value |
|-------|-------|
| Assigned To | Manuel Vazquez → Monica Green |
| Priority | 2 |
| State | Open |
| Due Date | 2026-09-15 |

**Problem:** Monica Green is CCB Class Manager for Computers – Physical. The campaign population, the certified attribute set, and the approved location list all require her ratification. Without it, this is a team initiative rather than a governed control — which is precisely the distinction Corporate Audit Services will probe.

**Acceptance criteria:**
- [ ] Physical-computer population definition confirmed
- [ ] Location + Asset Tag confirmed as the end-user-certified attributes; confirmation that no additional attribute is expected of employees
- [ ] Approved location list ratified
- [ ] Her sign-off role on campaign results defined — employee submissions are evidence, Class Manager sign-off is the validation

---

### DEP-5 · Asset Tag authoritative source and CI–Asset sync direction

| Field | Value |
|-------|-------|
| Assigned To | Bhushan Salsekar |
| Priority | 2 |
| State | Open |
| Due Date | 2026-09-15 |

**Problem:** `asset_tag` exists on both the CI and the related asset record. If certification writes to the CI and the sync does not propagate — or propagates the wrong direction and overwrites — the CMDB and Asset Management will disagree. Two systems in conflict is a worse audit finding than the original blank field.

**Acceptance criteria:**
- [ ] Authoritative source for `asset_tag` at PPL confirmed
- [ ] CI–Asset sync direction and behavior on CI-side update confirmed by test
- [ ] Write path agreed and reflected in PV-3

---

### DEP-6 · Confirm legacy Data Certification vs. Data Manager certification policies

| Field | Value |
|-------|-------|
| Assigned To | Bhushan Salsekar / Stan Tomberg |
| Priority | 1 |
| State | Open |
| Due Date | 2026-09-08 |

**Problem:** Two different implementations exist with a documented conversion path. The Display fields / Certification fields / Allow field updates model verified above belongs to **Data Manager certification policies**. If PPL is on legacy certification schedules, the build differs and a conversion may be prerequisite. This is a one-hour check that de-risks PV-3 entirely.

**Acceptance criteria:**
- [ ] Which implementation is active in PPL PROD confirmed
- [ ] If legacy, conversion effort assessed and sequenced ahead of PV-3
- [ ] Instance release version recorded — capability verified against Zurich docs; confirm PPL's version exposes the same policy fields

---

### DEP-7 · OCM approval for company-wide employee communication

| Field | Value |
|-------|-------|
| Assigned To | Manuel Vazquez → Nora Lizenberg |
| Priority | 2 |
| State | Open |
| Due Date | 2026-09-22 |

**Problem:** This sends email to every PPL employee with an assigned computer, with automatic reminders and manager escalation on past-due. That is a company-wide communication with an HR-adjacent escalation path. It runs through OCM, not through the team.

**Acceptance criteria:**
- [ ] Communications plan and email copy approved by OCM
- [ ] Manager-escalation-on-past-due confirmed acceptable, or disabled
- [ ] Launch timing coordinated against other enterprise communications
- [ ] Service Desk briefed ahead of send

---

### DEP-8 · Authoritative "last seen" timestamp for SCCM/Intune-sourced Computer CIs

| Field | Value |
|-------|-------|
| Assigned To | Stan Tomberg / Bhushan Salsekar |
| Priority | 1 |
| State | Open |
| Due Date | 2026-09-15 |

**Problem:** PV-3's 45-day recency filter needs a reliable "last seen by an endpoint source" timestamp. Computers at PPL are populated by SCCM/Intune Service Graph Connector, Jamf, and Agent Client Collector — not ServiceNow Discovery — so the OOB `last_discovered` field may be empty, stale, or not maintained by those connectors. Filtering on the wrong field either scopes the campaign to zero or, worse, silently excludes live devices while including dead ones. `sys_updated_on` is **not** a substitute: any integration touch updates it, so it reports records as fresh that no endpoint has actually reported in.

**Acceptance criteria:**
- [ ] The field each endpoint source stamps on check-in identified (SCCM/Intune SGC, Jamf, ACC) — confirm whether they agree on one field or each write their own
- [ ] Behavior confirmed for a CI with multiple sources — which timestamp wins
- [ ] Field verified populated and current across a sample of known-live devices
- [ ] Interaction with `u_off_network` assessed — how off-network devices appear against the chosen field
- [ ] Chosen field documented and reused by [[PI-3/pi3-nd-1356646-stories-dependencies|CR-6]] so Computer and Network Gear apply the same definition of "recently confirmed"

---

## Sequence summary

```
DEP-6 (legacy vs Data Mgr, 9/8) ─┐
DEP-1 (licensing answer) ─────────┼─► PV-1 (SPIKE: go/no-go, 3.3) ── HARD GATE
                                   │            │
DEP-2 (phys/virtual split) ────────┘            ├─► PV-2 (location list, 3.3) ──┐
DEP-3 (cmn_location granularity) ───────────────┘                                │
DEP-4 (Class Mgr sign-off) ──────────────────────────────────────────────────────┼─► PV-3 (policy build, 3.3→3.4)
DEP-5 (asset sync) ──────────────────────────────────────────────────────────────┤        │
DEP-8 (last-seen field, 45-day filter) ─────────────────────────────────────────┘        │
                                                                                           ├─► PV-4 (notifications + OCM, 3.4) ◄── DEP-7
                                                                                           │        │
                                                                                           └────────┴─► PV-5 (pilot, 3.4)
                                                                                                            │
                                                                                        PV-6 (no-assigned-to, 3.5 / defer) ◄──┘
                                                                                                            │
                                                                                      → feeds CC-4 (full population cycle)
```

**Total points:** 3 + 3 + 5 + 3 + 3 = **17** (excluding PV-6 at 5, recommended defer).

---

## ⚠️ Gate reality check — raise at Sprint Planning

**CO6 Obj 3 due Sep 30** = end of Sprint 3.4. The CO6 acceptance criterion is *"process documented, technical build to PROD, dashboards live, training delivered"* — **all four are achievable** by Sep 30 on this plan.

**What is not achievable by Sep 30 is measured coverage.** A validation campaign to ~21,000 employees cannot be launched, completed, chased, and reported inside four weeks — starting from a spike that has not yet run and a licensing answer nobody has. If the Sep 30 gate is read as *"Location and Asset Tag are 90% populated,"* this plan does not meet it and no plan starting Sep 2 would.

**Recommendation:** confirm with Joe Dames and Sonika Das that the Sep 30 artifact is the **capability** (policy live in PROD, pilot proven, comms approved), with full-population coverage landing in **3.5/3.6 and into PI-4**. Get that in writing before committing. See DEP-2 on Feature 1517029 — the 90%-coverage acceptance story (G2) is still open and is the right place to pin the coverage target and its date.

---

## Open items

1. **CI Owner field binding** — this file follows the user's stated `managed_by`, but [[Config-Mgmt-Plan/ownership-terminology-mapping]] maps PPL "CI Owner" to **`owned_by`** (row O3) and treats `managed_by` as a separate person-level field (O5). CC-1's acceptance criteria currently says `managed_by`. Worksheet questions Q1/Q7 are unresolved. **A display field must bind to one field — resolve before PV-3.**
2. **OS and Serial Number categorization** — both were described as non-discoverable, but the ratified dictionary makes SCCM/Intune authoritative for `os` and Asset Mgmt/SCCM authoritative for `serial_number`. Read-only treatment is unaffected; the dictionary categorization should not be changed to match the form design.
3. **`Allow empty field values`** — recommended disabled (forces a value). Confirm with Monica Green; it trades completion rate against outcome quality.
4. **45-day recency threshold** — chosen to absorb vacation and short-term leave. It does **not** absorb extended leave (FMLA, sabbatical, military), long-term secondment, or seasonal staff, whose devices will fall out of the window while remaining legitimately assigned. Those records must land in the PV-6 review bucket rather than being retired on the strength of the filter alone. Confirm the threshold with Monica Green; 60 days is the obvious alternative if extended-leave exclusion proves material.
5. **Re-validation cadence** — the policy schedule sets it. An annual or semi-annual cycle is what converts this from remediation into a standing control, which is what the CMP should record.
5. **CMP update** — if end-user validation becomes the defined validation method for Location and Asset Tag on physical Computer, [[Config-Mgmt-Plan/configuration-management-plan-stage1]] should say so and the CCB should ratify it. Without that step this is a campaign, not a control.
6. **Audit acceptance** — whether Corporate Audit Services accepts end-user attestation as a validation control for a governed CI attribute is unconfirmed. Cheap to ask at the monthly CMDB Audit Sync; expensive to discover at sign-off.
