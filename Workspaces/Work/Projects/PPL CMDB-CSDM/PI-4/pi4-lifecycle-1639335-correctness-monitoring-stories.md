---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-4
feature: "1639335 — CMDB Correctness (Staleness, Orphans, Duplication)"
objective: "PI-4 Obj 4 (1639075) — Implement CMDB Lifecycle Management Process Flows"
sow: "AP00288 Deliverable 8"
gate: 2026-12-31
sprint: "4.1 → 4.3"
status: draft
updated: 2026-10-20
tags: [work, cmdb-csdm, safe, pi-planning, servicenow, governance, cmdb-health]
relationships:
  - target: "[[PI-4/pi4-lifecycle-1640805-ado-ready-items]]"
    type: derived_from
  - target: "[[Backlog/cmdb-health-completeness-correctness-stories]]"
    type: derived_from
  - target: "[[Backlog/cmdb-health-lifecycle-validation-stories]]"
    type: related_to
  - target: "[[Backlog/feature-implementation-structure]]"
    type: derived_from
  - target: "[[Backlog/definition-of-ready]]"
    type: related_to
---

# Feature 1639335 — Spikes & Stories (Sprints 4.1–4.3)

**CMDB Correctness (Staleness, Orphans, Duplication)** · Objective **1639075** · AP00288 **D8** · Gate **Dec 31, 2026**

> **Status: DRAFT (2026-10-19).** Nothing created in ADO. Seven items — **2 spikes, 4 build, 1 implement** — fitted to **Sprint 4.1 (Oct 28 – Nov 10)**, **4.2 (Nov 11–24)** and **4.3 (Nov 25 – Dec 8)**, with evidence and submission in **4.4**.

---

## The deliverable, verbatim

AP00288 **Deliverable 8 — "CMDB Lifecycle Management – CI Retirement Data Monitoring Rules"**:

> *"Implement rules for CMDB data monitoring related to CI retirement, such as staleness, orphans, and duplication."*

**Format: XML.** **Due: December 31, 2026.** Invoiced in the December cycle alongside D1, D4, D6 and D9 ($505,885 combined).

The SOW defines two of the three terms and leaves the third open:

| Term | AP00288 definition |
|---|---|
| **Orphan** | *"A Configuration Item in the CMDB that has no valid relationship to another Configuration Item."* |
| **Staleness** | *"The condition of a Configuration Item record that has not been updated by a Discovery Source within a defined period."* |
| **Duplication** | **not defined** — the team sets the basis (see C2) |

### The SOW title is imprecise — the ADO title is the one that matches the work

| Source | Title |
|---|---|
| AP00288 D8 | CMDB Lifecycle Management – CI Retirement Data Monitoring Rules |
| ADO 1639335 (Oct 8 official list) | CI Retirement Monitoring Rules (Staleness, Orphans, Duplication) |
| PI-4 deck (Oct 12 / Oct 16) | ✅ **CMDB Correctness (Staleness, Orphans, Duplication)** — **use this** |

**Confirmed by the PO, 2026-10-19: this feature is the configuration of staleness, orphan and duplication settings to manage CMDB correctness.** It is not retirement plumbing. "Correctness" is a ServiceNow CMDB Health KPI whose three sub-metrics are exactly Duplicate, Orphan and Stale, so the deck title names the work precisely and the ADO title should stay as it is.

The SOW's *"related to CI retirement"* framing is a **drafting imprecision in AP00288**, not a scope statement. Log it alongside the four already tracked in [[PI-4/Memory]] — the "three (3) integrations" that names four, the duplicated D1/D2 text, the Deliverable 7 date of "January 30, **2026**", and the Dierkshiede/Dierksheide spelling split.

**Do not rename the ADO item to match the SOW.** Two consequences follow instead:

1. **The evidence package must bridge the vocabulary gap itself.** The submission is made against a deliverable called "CI Retirement Data Monitoring Rules" while the artifacts say "Correctness." C7 #11 carries this — state in the submission that the configured staleness, orphan and duplication rules *are* the D8 monitoring rules, so a reviewer matching titles does not read a gap.
2. **The contract text still bounds what is owed.** D8 asks that the rules be implemented, delivered as XML. The Correctness KPI scoring added at C6 is how PPL reads the rules, and is the right thing to build — but it is PPL's management instrument, not an additional contractual obligation. Keep that distinction visible at submission (C6 #9).

---

## Two scope choices, both confirmed 2026-10-19

### Scope choice 1 — detect, score and report; do not act

The rules **flag** stale, orphan and duplicate CIs, and the Correctness KPI **scores** the result per class against a target (C6). What happens to a flagged CI afterwards — notification, remediation task, state change, retirement — is **out of scope for D8**.

> **Revised 2026-10-19.** This originally read "detect and report" with scoring explicitly excluded. On PO direction the KPI scoring is in scope: managing correctness, not merely detecting it, is what the feature is for. The boundary that did **not** move is action on a flagged CI.

**Why:** the deliverable says *"implement rules for CMDB data monitoring"*, delivered as XML. A detection rule set is what an XML export can evidence. Adding an automated retirement workflow would almost certainly trip the [[requirements-process#Customization Governance|Customization]] gate and would collide with **Sonika's open CI auto-retirement item** (CMDB Go Green weekly), which is being worked on a different track.

**What this gives up:** any reading of *"related to CI retirement"* that expects CIs to actually get retired. If the PO wants that, it is a separate feature behind this one — not an acceptance criterion inside it.

### Scope choice 2 — three CI classes: Computer, Server, Database Instance

| Class | Table | Active CIs | CCB Class Manager |
|---|---|---|---|
| Computer | `cmdb_ci_computer` | 19,901 | Monica Green / Paul Becker |
| Server | `cmdb_ci_server` | 3,917 | Ray Reuter |
| Database Instance | `cmdb_ci_db_instance` | 3,113 | Ray Reuter |

**Business Application is excluded.** A BA is not discovered — it is identified by Name with no CI-Class-Manager identification rule — so the SOW's own staleness definition (*"not been updated by a Discovery Source"*) cannot apply to it. BA freshness is certification-based and lives in [[Backlog/cmdb-health-lifecycle-validation-stories|HL-4]]. **Network gear classes are excluded** — the D1/D2 integrations that populate them do not land until Dec 31 and Feb 2, so rules written now would score an empty population.

Counts and class facts are from the **CMDB Data Dictionary — CCB Review & Approval, delivered to PPL 2026-07-21**, via [[Backlog/cmdb-health-completeness-correctness-stories]].

---

## What already exists in the vault

This feature does **not** start from zero. Two prior drafts cover most of the design thinking, both tagged **NON-SOW**:

| Existing draft | Covers | Status |
|---|---|---|
| [[Backlog/cmdb-health-completeness-correctness-stories]] **CR-1 / CR-2 / CR-3** | Correctness (Duplicate · Orphan · Stale) per class, with identification rules, discovery sources, orphan bases and the **85–90% target model** | Draft — **never created in ADO.** Now **absorbed into C6** |
| [[Backlog/cmdb-health-completeness-correctness-stories]] **CP-0** | Dashboard scoping via one base-level `cmdb_ci` inclusion rule filtered on `sys_class_name`, plus the active-records lifecycle filter | Reconciled in ADO as **1526841**. **Reused by C6 #2** |
| [[Backlog/cmdb-health-lifecycle-validation-stories]] **HL-1 / HL-2 / HL-3** | Discovery-based staleness policy and lifecycle transitions per class | Draft |

**D8 gives them a contract home, and that changes their acceptance lane.** CR-1/2/3 were drafted as team-added quality governance: PM accepts, PO signs off, CCB informed, *"not linked to a deliverable number."* Under D8 the same work is contractual, submitted to PPL, and subject to the **three-business-day deemed-acceptance** clock. Carry the content forward; do not carry the NON-SOW framing forward.

**C6 now absorbs CR-1/CR-2/CR-3 outright**, since it scores the same KPI across the same three classes. That makes the reconciliation below mandatory rather than tidy-up: two live drafts for one piece of work, one contractual and one not, is how a team ends up configuring the same KPI twice to two different targets.

**Reconcile on creation:** once these items exist in ADO, mark CR-1/CR-2/CR-3 in the Backlog file as superseded by 1639335 C6 and point to this file. Leave CP-0 (1526841) alone — it is a live item C6 builds on, not a duplicate.

---

## Schedule

| Phase | Sprint | Dates |
|---|---|---|
| Spikes | **4.1** | Oct 28 – Nov 10 |
| Build & test | **4.2** | Nov 11 – Nov 24 |
| Validate & release | **4.3** | Nov 25 – Dec 8 |
| Evidence & submission | **4.4** | Dec 9 – Dec 22 |
| Contract gate | — | **Dec 31, 2026** |

**This deviates from [[PI-4/pi4-implementation-plan-appendix]], deliberately.** The appendix's derivation rule puts requirements for 1639335 in **PI-3 IP (Oct 14–27)** — this fortnight, before PI Planning on Nov 4, with the backlog not yet committed. That is not a real runway. Moving the spikes into 4.1 honours the ADO start date (Oct 28), still releases Dec 8, and leaves **23 days of margin** to the gate. It is the healthiest schedule of any PI-4 feature.

**Delivery notification is the real deadline, not Dec 31.** Sprint 4.5 (Dec 23 – Jan 5) is the holiday shutdown. Three business days before Dec 31 (a Thursday) run back into the shutdown, so **issue the notification on or before Friday Dec 18** — the last working day before the break — giving Dec 21–23 as the acceptance window.

**The December change freeze question barely touches this feature.** Open Question 1 in [[PI-4/pi4-implementation-plan-appendix]] flags an unconfirmed PPL December freeze. D8 releases **Dec 8**, ahead of where a freeze would normally start. Confirm with Kostas anyway, but this is the one Dec-31 deliverable that is not exposed to it.

---

## Before creating anything

- [ ] Confirm the parent objective is **1639075**. Create every item from the **Feature 1639335 "+" link** — never standalone ([[requirements-process#ADO Hierarchy Rule]]).
- [ ] **Read the ADO acceptance criteria on 1639335 against the D8 text above.** On D10 the ADO criteria were found to be materially stricter than the contract (see Risk 8 in [[PI-4/Memory]]); 1639335 has not been checked. If ADO adds obligations the SOW does not carry, that is a PO decision to make knowingly, not a surprise to absorb in Sprint 4.2.
- [ ] **Decide the title.** Align ADO to the SOW wording, or accept the deck/contract vocabulary split in writing.
- [ ] Get **both scope choices** confirmed by the PO before refinement.
- [ ] **Get the C1 workshop into Ray Reuter's and Monica Green / Paul Becker's calendars for week 1 of 4.1**, and issue the chair ruling on the sign-off path (C1 #3) before the invite goes out. They are the only external approvers C1 has, and they gate two of the three rule families.
- [ ] **Decide whether child Tasks are a C1-only device or an ART convention.** Neither [[requirements-process]] nor [[Backlog/definition-of-done]] mentions the Task level — the documented process stops at Story and Spike. C1 introduces three tasks; that is fine, but it is a new convention landing in the same PI as the structure proposal.
- [ ] **Raise the Class Manager written confirmations (C1 #7) as a RAID item** the day the workshop closes. Both [[Backlog/feature-story-templates]] (B-S3) and the Server Build plan (A2) carry this as its own work item; C1 merges it into a criterion, so the RAID entry is what keeps it visible on the board.
- [ ] C1 and C2 make the configuration-vs-customization call. OOTB CMDB Health rule configuration is expected, so **no `Customization` tag anticipated** — but if either spike finds scripted logic is needed, the tag, a linked RAID issue and Sonika Das's approval are required **before** C3/C4/C5 start ([[requirements-process#Customization Governance]]).
- [ ] Assign **P1–P4** with numeric sub-ranking. Share IDs with Anu for Program Backlog Review.
- [ ] Mark **CR-1/CR-2/CR-3** in [[Backlog/cmdb-health-completeness-correctness-stories]] as superseded once the ADO IDs exist.

**Suggested tags:** `CMDB-Lifecycle` `PI4-Obj4` `D8`, plus `governance` on C1 and C7.

---

## The list

| # | Type | Title | Sprint |
|---|------|-------|--------|
| C1 | Spike | Staleness and orphan rule design — analyze, decide, confirm | 4.1 |
| C2 | Spike | Duplicate detection readiness — identification rules and identifier coverage | 4.1, parallel |
| C3 | Enabler – Configuration | Staleness rules — Computer, Server, Database Instance | 4.2 |
| C4 | Enabler – Configuration | Orphan rules — Computer, Server, Database Instance | 4.2 |
| C5 | Enabler – Configuration | Duplicate detection — Computer, Server, Database Instance | 4.2 |
| C6 | Enabler – Configuration | Correctness KPI — score per class against target, and publish | 4.2 → 4.3 |
| C7 | Story | Implement — release, evidence package and acceptance | 4.3 → 4.4 |

**Critical path:** C1 → C3 / C4 → C6 → C7. **C2 runs beside C1; C5 depends only on C2.**

### Why two spikes and not one

[[Backlog/feature-implementation-structure]] says *exactly one spike per feature*. This plan runs two, on purpose:

- **Different stakeholders.** C1 is a governance conversation with CCB Class Managers about thresholds and what counts as an orphan. C2 is a technical investigation with Adam Griffis and Jeff Schwartzkopf into IRE behaviour and identifier coverage. Neither blocks the other.
- **Different failure modes.** C1 fails if a Class Manager will not commit to a number. C2 fails if serial coverage turns out to be too thin for duplicate detection to mean anything. Merged, the second failure hides behind the first.
- **The 1640805 lesson.** A1 on the Server Build feature merged two spikes into one timeboxed item and that merge is Risk 2 on the plan. This window is comfortable enough not to repeat it.

If the team prefers the single-spike convention, merge C1 and C2 into one timeboxed spike for Sprint 4.1 and carry the identifier-coverage finding as an explicit exit criterion — but expect the same sizing pressure A1 carries.

---

### C1 · [Spike] Staleness and orphan rule design

**Sprint 4.1** · **Timeboxed — hard stop at the end of 4.1**

Set the thresholds and definitions the staleness and orphan rules will be built from. The three numbers and three definitions belong to **Class Managers outside the team**, so the spike is shaped around getting them decided and recorded, not researched.

| Phase | Purpose | Produces |
|---|---|---|
| **1 — Analyze** | Turn open questions into choices | The data pack, and a ruling on who signs off |
| **2 — Decide** | Get the choices owned, in one room, by the people who own the classes | Three thresholds, three orphan bases |
| **3 — Confirm** | Turn agreement into evidence that outlives the meeting | Written confirmations, and the baseline |

**In ADO each phase is a child task** under this spike — Analyze, Workshop, Confirm — so the phases are individually assignable and visible on the board while the decisions and their written record stay in one work item. Task definitions and done-conditions are in the appendix.

#### Phase 1 — Analyze
*So the session chooses between prepared options instead of answering open questions. This is query work against the CMDB, not write-up — size it accordingly.*

1. **Data pack built, per class** — Discovery scan interval; active CIs that would flag stale at **30 / 45 / 60 / 90 days**; candidate orphan count. Coverage distortions marked on the figures: offline Computers, and the **Oracle-KY gap** plus issue **1520824** on Database.
2. **Scored population defined** — active, non-retired only. `install_status` / `operational_status` values agreed with Ray Reuter, Adam Griffis and Jeff Schwartzkopf; counts reconcile to **19,901 / 3,917 / 3,113**.
3. **Chair ruling logged, before the invitation goes out** — Class Manager sign-off is sufficient; thresholds are not a data-dictionary change. A dated CCB entry, not a wait.

#### Phase 2 — Decide · ~2 hours
*So each decision has a named owner who chose it, rather than a default nobody owns.*

**In the room:** Ray Reuter (Server, Database Instance) · Monica Green and Paul Becker (Computer) · Adam Griffis and Jeff Schwartzkopf (Discovery / CMDB integration) · M. Vazquez (PO, CCB Chair, facilitator).

4. **Staleness threshold per class** — one number, not a range, chosen against the criterion 1 distributions. Computer: Monica Green / Paul Becker. Server and Database Instance: Ray Reuter.
5. **Orphan basis per class** — Server: no relationship to any Application or Business Service. Database Instance: no `Runs on::Runs` host. **Computer: a defined non-orphan condition, or a documented exemption** — end-user devices are relationship-light and a naive rule over-flags. Leaving Computer open is not an outcome.
6. **Detect-and-score boundary minuted**, and the recipient and cadence named for the flagged population. Acting on a flagged CI stays out of scope.

#### Phase 3 — Confirm
*So the decisions survive as evidence, not as recollection.*

7. **Written confirmation from each Class Manager, by a named date** — individually attributed. **The only independent approvals behind D8**, since criteria 3 and 6 are self-decided. Carried as a RAID item.
8. **Baseline recorded** — stale and orphan counts per class at the agreed thresholds, captured before any rule exists. Calibrates the C6 target (DEP-14).
9. **Customization call made** — RAID issue the same day if it is customization — and **C3, C4 and C6 sized** to [[Backlog/definition-of-ready]] gates 1–4.

**Notes**

- **Timing.** Phase 1 in PI-3 IP where the process allows it, Phase 2 in week 1. If the IP start is not permitted, Phase 1 runs in week 1 and Phase 2 moves to week 2. **The hard stop does not move either way.**
- **The analysis is the agenda.** Asking Ray *"what should N be for Server?"* cold gets "it depends," and the one convening is spent. Without criterion 1 there is no workshop, only a meeting.
- **Criterion 7 gets a RAID item the day Phase 2 closes.** [[Backlog/feature-story-templates]] makes Class Manager confirmation its own spike (**B-S3**, *"the long pole — an external dependency, not team capacity"*) and 1640805 does the same at **A2**, with the fallback *"if it is merged anyway, carry it as a RAID item."* C1 merges it, so take the fallback — three outstanding replies are invisible inside a criterion reading "confirmed," and they are the likeliest reason C1 misses its hard stop.
- **If Phase 2 slips its week**, run per-class conversations and take **Ray first** — two of the three classes.
- **Hand over, don't absorb.** Anything belonging to D10 (1640805), D11 (1640819), D9 (1640795) or D6 (1642240) goes to that feature. CR-1/CR-2/CR-3 in [[Backlog/cmdb-health-completeness-correctness-stories]] are the starting point; Phase 1 confirms them live. C2's findings are welcome in the session but are not a prerequisite.

---

### C2 · [Spike] Duplicate detection readiness — identification rules and identifier coverage

**Sprint 4.1 — runs in parallel with C1** · **Timeboxed**

Establish whether duplicate detection will produce a meaningful result on each class before a rule is configured against it.

**Acceptance criteria**

1. **The identification rule behind each class's duplicate basis is confirmed in the live instance:**
   - **Computer** — PPL Computers (Independent): `Name` + `serial_number` at priority 100.
   - **Server** — PPL Server (Independent): `serial_number` (100) → serial lookup (200) → `name` (300).
   - **Database Instance** — Database instance rule (**Dependent**, on host Server): `serial_number` (100) → `Edition` + `name` + TCP port (200).
2. **Identifier coverage measured per class, as a percentage.** This is the finding that decides whether the rule is worth configuring. Note that **`serial_number` is the Server class's primary identifier but is not in the Server managed-attribute set** — low coverage inflates the duplicate count with false positives.
3. **The Database dependency is tested, not assumed.** The DB rule identifies instances *in the context of their host Server*, so duplicate detection on Database Instance is only as correct as Server identity. State what happens to DB duplicate detection where the host Server is itself duplicated or missing.
4. **A duplicate sample is pulled and manually inspected per class** — enough records to say whether the matches are real duplicates, identifier gaps, or legitimate distinct CIs. A count with no inspection behind it is not a finding.
5. **"Duplication" is defined for D8 and written down**, since AP00288 does not define it. Recommended: *two or more active CIs in the same class resolving to the same identity under the class's identification rule.* Agreed with Adam Griffis and Jeff Schwartzkopf, and the relevant Class Manager.
6. **Interaction with the D10 server-build flow recorded** — 1640805 creates server CIs at provisioning before a serial exists, which is a known duplicate-generation path. State whether the duplicate rule will flag those CIs during their build window, and if so how that is suppressed or accepted.
7. **Baseline duplicate count captured per class** before any configuration, for the same reason as C1 #8.
8. **Configuration vs. customization determined** for the duplicate surface; RAID issue raised the same day if needed.
9. C5 sized, passing [[Backlog/definition-of-ready]] gates 1–4.

> **This spike can return "don't build it yet."** If identifier coverage on a class is too thin for duplicate detection to be meaningful, the honest outcome is a documented exclusion for that class with the coverage number attached — not a rule that produces noise. D8 names duplication as an example (*"such as"*), not as a mandatory per-class obligation. Confirm that reading with the PO before relying on it.

---

### C3 · [Enabler – Configuration] Staleness rules — Computer, Server, Database Instance

**Sprint 4.2** · Depends on C1

**As** the CMDB Configuration Management Process Owner, **I want** staleness rules configured for the three managed classes, **so that** CIs no longer being updated by their Discovery Source are identified instead of quietly aging in the CMDB.

**Acceptance criteria**

1. A staleness rule is configured per class at the agreed `N` from C1 #4, anchored on **last update by a Discovery Source** — matching the AP00288 definition, not on `sys_updated_on`, which a manual edit would reset.
2. The rule evaluates **active, non-retired CIs only**, per the C1 #2 population definition, and the evaluated counts reconcile to the dictionary figures.
3. Configured at the parent class so child classes inherit — `cmdb_ci_computer`, `cmdb_ci_server` (Windows / Linux inherit), `cmdb_ci_db_instance` (Oracle / MS SQL inherit). No per-child duplication of the same rule.
4. **The rule runs on a schedule and completes without error**, and the flagged population refreshes on cadence rather than going stale itself.
5. **Flagged counts compared against the C1 #8 baseline** and the difference explained. A large divergence means the rule is not implementing the agreed threshold.
6. **Known distortions annotated on the output, not silently included** — offline physical Computers, and Database instances inside the Oracle-KY authentication gap. A reader must be able to tell a genuinely stale CI from one Discovery cannot reach.
7. Rule exported as **XML** and the export verified to re-import cleanly — this is the contractual artifact format, so it is proven here rather than discovered at C7.
8. Tested per [[Backlog/definition-of-done]]; staging deploy and PO demo.

---

### C4 · [Enabler – Configuration] Orphan rules — Computer, Server, Database Instance

**Sprint 4.2** · Depends on C1

**As** the CMDB Configuration Management Process Owner, **I want** orphan rules configured for the in-scope classes, **so that** CIs with no valid relationship to anything else are identified as candidates for retirement or relationship remediation.

**Acceptance criteria**

1. An orphan rule is configured **per class per the C1 #5 basis** — Server (no relationship to any Application / Business Service) and Database Instance (`Runs on::Runs` absent) at minimum.
2. **Computer is handled per the C1 #5 outcome** — either a defined non-orphan condition, or an explicit documented exemption. **A Computer orphan rule is not configured by default.**
3. Each rule is **signed off by its CCB Class Manager** before it is enabled — Ray Reuter for Server and Database, Monica Green / Paul Becker for Computer if in scope. Written, not verbal.
4. Flagged counts compared against the C1 #8 baseline and the difference explained.
5. **The Service Mapping dependency is stated on the output.** Orphan counts on Server fall as Service Mapping builds relationships under D3/D4/D5, so a point-in-time orphan count is a measure of mapping coverage as much as of data quality. Confirm the current Service Mapping owner — [[Backlog/cmdb-health-completeness-correctness-stories]] records the lead as vacant as of July 2026 and that may no longer hold.
6. **Over-flagging is checked before enablement**, not after: a sample of flagged CIs per class is inspected and confirmed to be genuinely relationship-less rather than caught by a rule that is too broad.
7. Rules exported as **XML**, verified to re-import cleanly.
8. Tested per [[Backlog/definition-of-done]]; staging deploy and PO demo.

---

### C5 · [Enabler – Configuration] Duplicate detection — Computer, Server, Database Instance

**Sprint 4.2** · Depends on C2

**As** the CMDB Configuration Management Process Owner, **I want** duplicate detection active for the classes where it will produce a meaningful result, **so that** CIs resolving to the same identity are surfaced rather than silently double-counted.

**Acceptance criteria**

1. Duplicate detection is active per class using the identification rule confirmed at C2 #1, scored over active CIs only.
2. **Any class excluded at C2 is excluded here in writing, with its coverage number attached** — not quietly dropped.
3. The flagged duplicate set is **reviewed against the C2 #4 sample behaviour** — the rule in production finds the same kind of matches the spike found by hand.
4. **Build-window CIs from the D10 server flow are handled per the C2 #6 decision** — suppressed, excluded, or accepted with the reason recorded. The two features must not fight each other in production.
5. **Remediation is explicitly out of scope and stated as such on the output.** The duplicate set is surfaced and routed; merging or retiring duplicates is not part of D8 (scope choice 1).
6. Flagged counts compared against the C2 #7 baseline.
7. Configuration exported as **XML**, verified to re-import cleanly.
8. Tested per [[Backlog/definition-of-done]]; staging deploy and PO demo.

---

### C6 · [Enabler – Configuration] Correctness KPI — score per class against target, and publish

**Sprint 4.2 → 4.3** · Depends on C3, C4, C5 · **Absorbs CR-1 / CR-2 / CR-3 from** [[Backlog/cmdb-health-completeness-correctness-stories]]

**As** the CMDB Configuration Management Process Owner, **I want** the CMDB Health **Correctness** KPI configured and scored per class against an agreed target, **so that** data integrity is measurable and remediation is targeted, rather than a raw count of flags nobody can read against anything.

**What Correctness is, and is not.** The ServiceNow Correctness KPI is an aggregate of three per-CI data-integrity sub-metrics — **Duplicate** (configured via Identification Rules), **Orphan** (via orphan rules, manual, one per class, none in base) and **Stale** (via staleness rules). It is **not** "are the attribute values accurate" — that is Compliance, and it is out of scope. C3, C4 and C5 configure the three rule sets; this story turns them into a scored KPI.

**Acceptance criteria**

1. **The Correctness KPI is configured and scored per class** — Computer, Server, Database Instance — aggregating the Duplicate, Orphan and Stale sub-metrics from C3/C4/C5. Validate the KPI mechanics against the **deployed release** with Adam Griffis and Jeff Schwartzkopf before building; sub-metric configuration and orphan-rule limits differ between versions.
2. **The scored population is scoped by one base-level inclusion rule**, anchored on `cmdb_ci` and filtered by `sys_class_name` to the managed leaf classes, carrying the C1 #2 lifecycle filter so only active, non-retired CIs score. This reuses the CP-0 approach already drafted in the Backlog rather than inventing a second scoping mechanism. **Expect the scored counts to be narrower than the parent-class dictionary totals** (19,901 / 3,917 / 3,113), because scoping is by exact class — reconcile the difference explicitly so the numbers are explainable.
3. **Whether Database Instance scores at the parent or per child class** (`cmdb_ci_db_ora_instance`, `cmdb_ci_db_mssql_instance`) is decided and recorded, with the exact child-class names confirmed in the live instance. CR-3 left this open.
4. **A target is agreed and recorded per class**, starting from the **85–90%** working figure in CR-1/2/3, confirmed with Sonika Das as PM and ratified by the PO. **Whether the target differs per class is decided, not assumed** — Computer, Server and Database have materially different Discovery coverage, so one number may not fit all three.
5. **Partial-coverage classes score honestly, not silently.** Where Computer is exempted from the orphan rule (C1 #5) or a class is excluded from duplicate detection (C5 #2), its Correctness score aggregates fewer than three sub-metrics. **State for each class which sub-metrics its score covers**, on the dashboard itself. An aggregate that quietly averages two sub-metrics where another class averages three is not comparable, and will be compared anyway.
6. **Scores and the flagged populations are readable in one view**, by CI class, with counts, the score against target, and drill-through to the underlying CIs. Built on the **OOB CMDB Health surface** wherever it will carry this — not a custom dashboard build.
7. **Baselines shown alongside current scores** — the C1 #8 and C2 #7 figures — so the view reads as a trend from a known starting point rather than an unanchored number. Ties to the existing CMDB Health baseline spikes **1436581 / 1470837**.
8. **Coverage caveats are visible on the view itself** — offline Computers, the Oracle-KY gap and credential issue 1520824, plus every exclusion from #5. A number without its caveat gets quoted without its caveat.
9. **The target is recorded as a management target, not a contractual acceptance threshold**, and that distinction is stated where the score is published. **D8 obliges PPL to implement the rules, not to reach a score.** A Correctness figure below 85% in December is a remediation backlog, not a failed deliverable — but only if nobody has implied otherwise first.
10. **A named recipient and cadence are agreed** for the flagged population and the score — who reads this, how often, and where it goes next (Sonika's CI auto-retirement track per C1 #6). Agreed, not assumed.
11. **Do not disable the platform-wide Correctness scheduled jobs** when scoping — other classes and teams depend on them. Scope by inclusion rule, not by switching the engine off.
12. Tested per [[Backlog/definition-of-done]]; staging deploy and PO demo.

> **This is the heaviest build item, and it grew on purpose.** It was drafted as a thin view over the three rule sets; scoring the KPI against a target was added on PO direction (2026-10-19) because managing correctness, not just detecting it, is what the feature is for. **Size it honestly at refinement** — if it exceeds one iteration, split the KPI configuration and scoring (#1–#5) from the dashboard view and publication (#6–#11), and keep the first half in 4.2. See Risk 10.

> **CR-1 / CR-2 / CR-3 are this story's source material.** They carry the per-class identification rules, discovery sources, orphan bases and the 85–90% target model. Mark them superseded by 1639335 once the ADO items exist — the acceptance lane changes from team-added quality governance (PM accepts, CCB informed) to a contractual deliverable submitted to PPL.

---

### C7 · [Story] Implement — release, evidence package and acceptance

**Sprint 4.3 for release; evidence and submission in 4.4** · Depends on C6

**As** the CMDB Product Owner, **I want** the rules in production and D8 submitted as an evidenced package, **so that** the deliverable is accepted inside the December invoice cycle and before the holiday shutdown.

**Acceptance criteria — Sprint 4.3**

1. Change request raised, approved, and the rules deployed to **production**, with the rule configuration verified in production rather than inferred from staging.
2. **December change freeze position confirmed** with Kostas before the window is assumed. A Dec 8 release should sit ahead of any freeze, but it is confirmed rather than assumed.
3. **First production run completed** and the flagged populations compared against the staging results — a material divergence is investigated before the item closes.
4. No Sev 1 or Sev 2 defects open at close. Rollback position stated.
5. **Operational ownership accepted by a named individual**, not "operations" as an abstraction, covering: who reviews the flagged populations and scores on the C6 #10 cadence, who maintains the thresholds and targets when Discovery cadence changes, and who is called when a rule stops running. **AP00288 ends Feb 2, 2027 — anything unaccepted before then has no owner afterwards.**
6. Rule documentation published to an agreed, versioned location with a named content owner, covering each threshold and its C1 #4 justification so a successor can tell a deliberate number from an arbitrary one.

**Acceptance criteria — Sprint 4.4, calendar-bound**

7. **Evidence package assembled** — the **XML export** of the configured rules as the primary contractual artifact, plus Class Manager sign-offs (C4 #3), the written threshold confirmations (C1 #7), baseline-versus-post-implementation counts (C1 #8, C2 #7), the per-class Correctness scores against target with their sub-metric-coverage disclosures (C6 #4, #5), the production change record, and the operational acceptance above.
8. **Before-and-after stated against the benefit hypothesis** — baseline stale / orphan / duplicate counts versus the first production run. Where a baseline was an estimate, it is labelled as an estimate.
9. **Written delivery notification issued on or before Friday, December 18, 2026**, so the three-business-day deemed-acceptance window closes before the Dec 23 holiday shutdown and well clear of the Dec 31 gate. PPL reviewer availability confirmed in advance.
10. Submission date, recipient and response logged. Any rejection has a named remediation owner and a date inside the remaining window.
11. **Exclusions and framing restated in the submission, not buried** — Business Application, network gear classes, any class excluded from duplicate detection, Computer orphan if exempted, and the detect-only boundary. Two additions now that C6 scores a KPI:
    - **State that the configured staleness, orphan and duplication rules *are* the D8 "CI Retirement Data Monitoring Rules."** The artifacts say "Correctness"; the deliverable is titled differently. Bridge it explicitly so a reviewer matching titles does not read a gap.
    - **State that the Correctness target is a management target, not an acceptance threshold** (C6 #9). D8 obliges implementation of the rules, not attainment of a score.

    A deliverable accepted on an unstated assumption is a dispute waiting for February.

> **Why Dec 18 and not Dec 31.** Three business days before Dec 31 fall inside the holiday shutdown, when PPL reviewers are unlikely to be available and a deemed acceptance would be hollow even if it technically ran. Dec 18 is the last working day that produces a real review.

---

## Dependencies

| # | Dependency | Owner | Needed by | Note |
|---|---|---|---|---|
| DEP-1 | Staleness threshold `N` agreed per class | Ray Reuter · Monica Green / Paul Becker | C1 workshop, wk 1 of 4.1 | On the critical path. Invite out during PI-3 IP |
| DEP-2 | Orphan basis agreed, incl. the Computer decision | Ray Reuter · Monica Green / Paul Becker | C1 workshop, wk 1 of 4.1 | Computer is the hard one — exemption is an acceptable answer |
| DEP-16 | **Written Class Manager confirmations returned** (distinct from DEP-1/DEP-2 — the agreement is made in the room, this is the follow-through) | Ray Reuter · Monica Green / Paul Becker | C1 #7, wk 2 of 4.1 | ⚠ **Carry as a RAID item**, per the B-S3 / A2 precedent. The likeliest cause of C1 missing its hard stop: people agree in a session and then do not answer the follow-up. Only independent approvals behind D8 |
| DEP-3 | IRE behaviour and identifier coverage confirmed in the live instance | Adam Griffis · Jeff Schwartzkopf | C2, Sprint 4.1 | Decides whether C5 is worth building per class. ⚠ See DEP-12 |
| DEP-4 | Active-CI population definition (`install_status` / `operational_status`) | Ray Reuter · Adam Griffis · Jeff Schwartzkopf | C1 #2, before the workshop | Every number shown in the session rests on it |
| DEP-5 | Oracle-KY authentication gap / credential issue **1520824** | DB / Discovery team | C3, C4 | Bounds Database staleness and orphan validity; annotate rather than block |
| DEP-6 | Service Mapping relationship coverage | Service Mapping lead — **confirm current owner** | C4 | Orphan counts on Server move with D3/D4/D5 progress |
| DEP-7 | D10 (1640805) server-build CI creation behaviour | M. Vazquez (same owner) | C2 #6, C5 #4 | Build-window CIs without serials are a duplicate-generation path |
| DEP-8 | Sonika's CI auto-retirement track | Sonika Das | C1 #6, C6 #10 | Receives the flagged population; D8 stops at detection and scoring |
| DEP-10 | December change freeze position | Kostas | C7 #2 | Low exposure at a Dec 8 release, but confirm |
| DEP-11 | PPL reviewer availability for the Dec 18 notification | PO / PPL | C7 #9 | Three-business-day clock must close before the shutdown |
| DEP-12 | **Adam Griffis's availability** | Nolan LeBlanc (RTE) / PO | C1 Phase 1, C2 | ⚠ He is taking over as Accenture CMDB **senior architect** (Joe Dames's role) while owning **6 of 12 PI-4 features at 50% allocation** (Risk 2 in [[PI-4/pi-planning]]), and C1's Phase 1 analysis, C2 and C6 all route through him. Confirm the draw on him at PI Planning, or route what Jeff Schwartzkopf can cover alone to Jeff |
| ~~DEP-13~~ | ~~Governance contacts after Josh Sterling's departure~~ | — | — | ✅ **Resolved 2026-10-19** — M. Vazquez holds both PO and CCB Chair. C1 #3 is a ruling to record, not a dependency to chase. **Residual:** he is also facilitator, so the Class Manager confirmations at C1 #7 and C4 #3 are the only independent approvals in the chain — see Risk 5 |
| DEP-14 | **Correctness target agreed per class** (85–90% starting point) | Sonika Das (PM) · M. Vazquez (PO) | C6 #4, Sprint 4.2 | Set it **after** the C1 #8 baseline exists, or the number is aspirational. Decide explicitly whether the target differs per class |
| DEP-15 | **Deployed-release Correctness KPI mechanics** — sub-metric configuration, orphan-rule limits, whether the OOB dashboard supports per-KPI scoping | Adam Griffis · Jeff Schwartzkopf | C6 #1, C6 #2 | CR-1/2/3 flagged this as a version caveat and it was never closed. Decides how much of C6 is configuration versus build |

---

## Risks

| # | Risk | Impact | Response |
|---|------|--------|----------|
| 1 | **A Class Manager will not commit to a threshold.** The whole feature rests on three numbers that someone has to own, and "it depends" is the likely first answer. | **High** | The C1 workshop is the mitigation — all three Class Managers in one room against prepared distributions (C1 #1), choosing between four numbers rather than answering an open question. C1 #7 requires it in writing; escalate inside 4.1 rather than configuring against a guess |
| 2 | **Computer orphan over-flagging.** A naive rule flags a large share of 19,901 end-user devices, the output becomes noise, and the rule is quietly ignored. | **High** | C1 #1 puts the real count in front of the room and C1 #5 forces an explicit decision on it; exemption with a written reason is a valid and probably correct outcome |
| 3 | **ADO acceptance criteria stricter than the SOW.** On D10 the ADO criteria carried three obligations the contract did not. 1639335 has not been checked. | **High** | Read them before PI Planning. If they add scope, that is a PO decision taken knowingly |
| 4 | **The workshop does not convene inside week 1**, or a Class Manager sends nobody. Concentrating the plan's front end into one session makes it efficient when it happens and expensive when it slips — and three of the attendees are outside the team. | **High** | Invite out during PI-3 IP with the Phase 1 data attached so the session has visible value before anyone has to clear a calendar. Fall back to per-class sessions, **Ray first** (two of three classes). C1's hard timebox makes a slip visible rather than silent |
| 5 | **Approval independence.** M. Vazquez is PO, CCB Chair and workshop facilitator, so the sign-off path (C1 #3) and the scope boundary (C1 #6) are self-decided. Legitimate and fast, but it leaves the Class Manager confirmations as the only external approval behind a contractual deliverable — and **CMDB governance is one of the three objectives of the Corporate Audit Services review**. | Medium | Record C1 #3 as a dated chair ruling in the CCB log rather than leaving it implicit. Hold C1 #7 and C4 #3 to written, individually attributed confirmations. Where a reviewer could read self-approval, show the decision and its reasoning rather than only the outcome |
| 6 | **Serial coverage too thin for duplicate detection**, particularly on Server where `serial_number` is the primary identifier but is not a managed attribute. | Medium | C2 measures it before C5 is built. A documented per-class exclusion with the number attached is a defensible outcome under *"such as"* |
| 7 | **Discovery coverage gaps masquerade as staleness.** Oracle-KY and offline Computers make rules measure reachability rather than data decay. | Medium | C1 #1 quantifies, C3 #6 annotates the output. Do not try to fix Discovery inside this feature |
| 8 | **"Related to CI retirement" is read as "retires CIs."** PPL accepts a detection-only deliverable believing it automates retirement, and the gap surfaces at submission. | Medium | Scope choice 1 confirmed with the PO at C1 #6; C7 #11 restates it in the submission rather than burying it |
| 9 | **The published target becomes a de facto acceptance threshold.** C6 now scores Correctness against 85–90%. If the December score lands below it, a reviewer can read a contractual deliverable as failed — when D8 only obliges PPL to *implement the rules*, not to reach a number. The risk is created by publishing the target, not by missing it. | **High** | C6 #9 states the distinction wherever the score is published, and C7 #11 restates it in the submission. Set the target **after** the C1 #8 baseline is known, so it is calibrated rather than aspirational |
| 10 | **C6 is oversized.** Scoring the KPI per class, scoping the population, agreeing targets and building the view is now the heaviest item in the plan, landing in Sprint 4.2 behind three rule-configuration stories. | **High** | Size it honestly at refinement. Split KPI configuration and scoring from dashboard publication if it exceeds one iteration, keeping the first half in 4.2 |
| 11 | **Partial sub-metric coverage makes scores incomparable.** If Computer is exempted from orphan and a class is excluded from duplicate detection, their Correctness scores aggregate different numbers of sub-metrics — and will be compared anyway. | Medium | C6 #5 requires per-class disclosure of which sub-metrics each score covers, on the dashboard itself |
| 12 | **The two story sets drift.** CR-1/2/3 stay in the Backlog as live NON-SOW drafts while 1639335 builds the same rules contractually — now more acute, since C6 absorbs them outright. | Medium | Mark them superseded the day the ADO items are created |
| 13 | **Collision with D10 in production.** The server-build flow creates serial-less CIs that the duplicate rule may flag during the build window. | Low | Same feature owner on both. C2 #6 decides the behaviour before either ships |

---

## Recommendation

**This plan still fits 4.1–4.3**, but with less room than before C6 took on KPI scoring. The schedule was never the binding constraint here — what binds is that three external numbers (the staleness thresholds) and one hard definitional call (Computer orphan) sit at the front of the work and are owned by people outside the team. **That is why C1 runs as a workshop** rather than a research spike: extracting owned decisions goes badly over email and well in a room with the numbers on screen.

**What C6's expansion changed.** Scoring the Correctness KPI per class against a target is the right build — detection alone would have left PPL with flag counts and no way to manage against them. It costs two things. Sprint 4.2 now carries the heaviest item in the plan behind three rule-configuration stories (Risk 10), and publishing a target inside a contractual deliverable creates a number the deliverable can be read as failing (Risk 9). Both are manageable, neither is free.

**Do five things before PI Planning on Nov 4:**

1. **Read the ADO acceptance criteria on 1639335 against the D8 text.** This is the one unknown that could change the plan's shape, and it is a ten-minute check.
2. **Name the handoff to Sonika's auto-retirement track.** The detect-and-score boundary is settled; what is not settled is who receives the flagged population afterwards and on what cadence.
3. **Issue the chair ruling on the sign-off path** (C1 #3) — Class Manager sign-off, not CCB ratification. You hold the chair, so this costs a written entry in the CCB log rather than a wait. Do it before the workshop invitation goes out, so the session's output is known to be sufficient on the day it is produced.
4. **Get the C1 workshop invited and the Phase 1 analysis started now**, during PI-3 IP. It needs no committed backlog, and the invite lands better with the distributions attached than as an open-ended ask.
5. **Decide how the Correctness target will be framed before anyone sees a score** (C6 #9, DEP-14). Set it after the C1 #8 baseline exists so it is calibrated, and state in writing that it is a management target rather than an acceptance threshold. This is cheap now and expensive to retrofit once PPL has seen a number.

The single highest-value adjustment, if there is any IP capacity at all, is **pulling C1's Phase 1 analysis into PI-3 IP** — not the spike itself, just the cadence figures and the last-updated distributions. That is what turns the workshop from a discussion into a decision, and it is also what makes the C6 target calibrated rather than aspirational. Everything else can wait for Oct 28.

---

# Appendix — C1 as an ADO work item (paste-ready)

Everything below is written to stand alone inside ADO: no wikilinks, no C1/C2 shorthand, no references to this file. Create it from the **Feature 1639335 "+" link**, never standalone.

## Fields

| Field | Value |
|---|---|
| **Work Item Type** | Spike |
| **Title** | Spike: Define staleness thresholds and orphan bases for Computer, Server and Database Instance |
| **Parent** | Feature 1639335 — CMDB Correctness (Staleness, Orphans, Duplication) |
| **Area Path** | *(team default — confirm)* |
| **Iteration Path** | A-INFOPS\FY26\PI4\Sprint 4.1 *(confirm exact node name)* |
| **State** | New |
| **Assigned To** | M. Vazquez *(PO, CCB Chair, workshop facilitator)* |
| **Priority** | P1 — Must Have *(numeric sub-rank set by M. Vazquez as PO)* |
| **Story Points** | *set at refinement* |
| **Tags** | `CMDB-Lifecycle`; `PI4-Obj4`; `D8`; `governance`; `Workshop` |
| **Customization tag** | Not applied — OOTB CMDB Health rule configuration expected. If criterion 15 finds otherwise, apply `Customization`, log a linked RAID issue and obtain Sonika Das's approval before any build story starts |

## Description

AP00288 Deliverable 8 requires PPL to implement rules for CMDB data monitoring covering staleness, orphans and duplication, delivered as XML by **December 31, 2026**. This spike fixes the numbers and definitions those rules will be built from, for three CI classes: Computer (`cmdb_ci_computer`, 19,901 active), Server (`cmdb_ci_server`, 3,917 active) and Database Instance (`cmdb_ci_db_instance`, 3,113 active). Business Application is out of scope — it is not discovered, so the contract's staleness definition cannot apply to it.

AP00288 defines two of the three terms: an **Orphan** is "a Configuration Item in the CMDB that has no valid relationship to another Configuration Item," and **Staleness** is "the condition of a Configuration Item record that has not been updated by a Discovery Source within a defined period." Duplication is not defined in the contract and is handled by the sibling duplicate-detection spike.

**This spike is run as a facilitated workshop with data prepared in advance.** Its output is not research — it is three staleness thresholds and three orphan definitions that have to be owned by CCB Class Managers outside the delivery team. Pursued by email those decisions arrive one at a time over several weeks and Sprint 4.1 is consumed. The work is therefore structured in three phases, each with a distinct purpose:

| Phase | Purpose | Produces |
|---|---|---|
| 1 — Analyze | Turn open questions into choices | The data pack, and a ruling on who signs off |
| 2 — Decide | Get the choices owned, in one room, by the people who own the classes | Three thresholds, three orphan bases |
| 3 — Confirm | Turn agreement into evidence that outlives the meeting | Written confirmations, and the baseline |

Phase 1 is query work against the CMDB, not documentation — it produces figures that do not exist yet, and it is the longest of the three phases. Size it as analysis.

**Timing and timebox:** hard stop at the end of Sprint 4.1. Phase 1 runs in PI-3 IP where the process permits work against an uncommitted backlog, with the workshop in week 1 of Sprint 4.1; otherwise Phase 1 runs in week 1 and the workshop moves to week 2. The hard stop does not move either way. If the decisions are not closed by then, escalate rather than extend — the build stories for the staleness and orphan rules cannot start without criteria 4 and 5, and there is no slack behind them.

**Out of scope for this spike and for Deliverable 8 overall:** acting on a flagged CI. These rules detect, and the Correctness KPI scores the result. Notification, remediation, merging duplicates and automated retirement are not part of this deliverable and are tracked separately under the CI auto-retirement work.

**Workshop participants:** Ray Reuter (Class Manager — Server, Database Instance), Monica Green and Paul Becker (Class Managers — Computer), Adam Griffis (Accenture CMDB senior architect) and Jeff Schwartzkopf (Discovery / CMDB integration), and M. Vazquez, who holds the Product Owner and CCB Chairperson roles and facilitates the session.

**Note on approval independence:** because the Product Owner, CCB Chairperson and facilitator roles are held by one person, criteria 3 and 6 below are decided internally. The written Class Manager confirmations at criterion 7 are therefore the only independent approvals supporting this deliverable's governance evidence, and must be individually attributed and dated.

## Acceptance Criteria

**Phase 1 — Analyze** · *so the session chooses between prepared options instead of answering open questions*

1. **Data pack built, per class**, covering: the Discovery scan interval (Computer via SG-SCCM / ServiceNow Discovery, Server via Discovery / SG-SCCM, Database Instance via ServiceNow application probes); how many active CIs would be flagged stale at 30, 45, 60 and 90 days; and the candidate orphan count against the criterion 5 bases, in particular the Computer count. Known coverage distortions are marked on the figures — offline physical Computers, and the Oracle-KY authentication gap (RAID) plus credential issue 1520824 on Database — so the session knows which numbers are suspect before reading them. A threshold shorter than a class's scan interval would flag healthy CIs, so the intervals bound the decision before it is made.
2. **Scored population defined** — active, non-retired CIs only — with the exact `install_status` and `operational_status` values agreed with Ray Reuter, Adam Griffis and Jeff Schwartzkopf, so counts reconcile to the CCB data dictionary figures of 19,901 / 3,917 / 3,113.
3. **Sign-off path ruled and logged before the workshop invitation is sent:** that Class Manager sign-off is sufficient and that staleness thresholds are not a data-dictionary change requiring CCB ratification. This is a CCB Chairperson ruling, recorded as a dated entry in the CCB record so the evidence package shows a decision rather than a gap. If the ruling goes the other way, the CCB's monthly cadence lands mid-build and the schedule must be replanned.

**Phase 2 — Decide** · *so each decision has a named owner who chose it, rather than a default nobody owns*

4. **Staleness threshold agreed per class** — a single number, not a range, selected against the criterion 1 distributions and justified against that class's scan interval. Computer is Monica Green and Paul Becker's decision; Server and Database Instance are Ray Reuter's.
5. **Orphan basis agreed per class**, starting from the AP00288 definition:
    - Server — no relationship to any Application or Business Service.
    - Database Instance — not hosted on a Server (`Runs on::Runs` relationship absent).
    - Computer — either a defined non-orphan condition, or a documented exemption of Computer from the orphan rule with the reason recorded. End-user devices are legitimately relationship-light, so a naive rule over-flags. Both outcomes are acceptable; leaving it undecided is not.
6. **Detect-and-score boundary stated by the Product Owner in session and minuted**, and the handoff of the flagged population to the CI auto-retirement track named — who receives it and on what cadence. Acting on a flagged CI remains outside this deliverable.

**Phase 3 — Confirm** · *so the decisions survive as evidence, not as recollection*

7. **Written confirmation obtained from each Class Manager, by a named date**, of the thresholds and orphan bases attributed to them. Verbal agreement does not satisfy this criterion. These confirmations are the only independent approvals supporting the deliverable's governance evidence and form part of the Deliverable 8 evidence package. **A RAID item is raised for these confirmations on the day the workshop closes**, with the named date as its due date, so three outstanding replies remain visible on the board rather than hidden inside this criterion.
8. **Baseline recorded before any rule is configured:** flagged stale and orphan counts per class at the agreed thresholds. This is the comparison point for the benefit hypothesis at deliverable submission, it cannot be reconstructed afterwards, and it calibrates the Correctness KPI target set in the downstream scoring item.
9. **Configuration versus customization determined** for the staleness and orphan rule surface — if any part requires custom logic, the `Customization` tag is applied, a RAID issue is raised and linked the same day, and Sonika Das's approval is obtained before implementation begins — **and the three downstream build items sized** (staleness rules, orphan rules, Correctness KPI scoring and dashboard), each passing Definition of Ready gates 1 through 4. The KPI item is the largest and may need to split.

## Child tasks

One task per phase, created under this Spike. They give per-phase visibility and individual assignment without splitting the spike — the decisions and their written record stay in one work item.

### Task 1 — Analyze: build the correctness data pack (Computer, Server, Database Instance)

| | |
|---|---|
| **Assigned To** | Jeff Schwartzkopf *(with Adam Griffis on coverage distortions; M. Vazquez on the chair ruling)* |
| **Covers** | Acceptance criteria 1–3 |
| **Timing** | PI-3 IP where permitted, otherwise week 1 of Sprint 4.1 |

**Purpose — find out what's actually in the CMDB today.**

You can't pick a staleness threshold without seeing the data first. This task answers three plain questions, for Computer, Server and Database Instance:

- How often does Discovery actually run against this class?
- How many CIs would be flagged stale at 30, 45, 60 and 90 days?
- How many CIs have no relationships?

Two supporting pieces go with it: agree which CIs count (active, not retired), and confirm the thresholds can be signed off by the CCB Chair rather than needing to go to CCB.

The point is that the workshop picks from real numbers instead of guessing. Where a number is unreliable — offline Computers, databases Discovery can't authenticate to — say so on the figure, so the room knows which ones to trust.

*Duplicates are not in this task. They are measured in the sibling spike, because they depend on identification rules and serial coverage rather than Discovery timing.*

**Done when:** Discovery scan intervals, the 30 / 45 / 60 / 90-day staleness distributions and the candidate orphan counts exist for all three classes; coverage distortions are marked on the figures; the scored population is defined and its counts reconcile to 19,901 / 3,917 / 3,113; and the CCB chair ruling on the sign-off path is logged with a date.

> This task has three different people doing different pulls and an ADO task takes one assignee. Split it by owner at Iteration Planning if the work genuinely parallelises; otherwise assign to Jeff with the others as contributors.

### Task 2 — Workshop: agree staleness thresholds and orphan bases (decision)

| | |
|---|---|
| **Assigned To** | M. Vazquez *(facilitator)* |
| **Covers** | Acceptance criteria 4–6 |
| **Timing** | ~2 hours, week 1 of Sprint 4.1 (week 2 if Task 1 could not start in IP) |
| **Attendees** | Ray Reuter · Monica Green · Paul Becker · Adam Griffis · Jeff Schwartzkopf · M. Vazquez |

**Purpose — get the decisions made, by the people who own the classes.**

Three thresholds and three orphan definitions, decided in one sitting with Task 1's numbers on screen.

A meeting rather than email, for two reasons. The three choices only make sense next to each other — 45 days on Server is hard to defend beside 90 on Computer unless the Discovery cadences differ. And the Computer orphan question is an argument, not a question: seeing how many of the 19,901 end-user devices a given basis would flag settles it in minutes, where a thread about it runs for weeks.

Every decision gets a name against it. A threshold nobody chose becomes whatever the person configuring the rule picked, and there is nobody to point to when it is questioned in December.

Say out loud here that the rules only detect and score — they do not retire anything — so the flagged list is not mistaken for a retirement queue later.

**Done when:** a staleness threshold is chosen per class with the deciding Class Manager named; an orphan basis is agreed per class, including an explicit in-or-out call on Computer; and the detect-and-score boundary plus the handoff recipient and cadence are minuted.

> **This task is not done because the session took place.** Its done-condition is that the decisions exist and each has a named owner. A session that ends in "let me think about it" leaves this task open and triggers the per-class fallback — Ray Reuter first, since he covers two of the three classes.

### Task 3 — Confirm: Class Manager confirmations, baseline and downstream sizing

| | |
|---|---|
| **Assigned To** | M. Vazquez *(confirmations); team (baseline and sizing)* |
| **Covers** | Acceptance criteria 7–9 |
| **Timing** | Week 2 of Sprint 4.1 |

**Purpose — write it down while it is still true.**

A decision made in a meeting exists only as memory until someone records it and the person who made it confirms it. Three things happen here:

- **Get it in writing from each Class Manager.** These are the only approvals on this deliverable that do not come from you, so they are what a reviewer will actually look at. Named and dated — not "the Class Managers agreed."
- **Record the before-numbers.** Once the rules are switched on and cleanup starts, you cannot go back and measure what it looked like beforehand.
- **Size the next three stories.** Sprint 4.2 cannot be planned until they are ready, which is the reason this spike sits in 4.1.

**Done when:** written confirmation has been received from each Class Manager, individually attributed and dated; the pre-configuration baseline is recorded; the configuration-versus-customization call is made; and the staleness rule, orphan rule and Correctness KPI scoring stories pass Definition of Ready gates 1–4.

> Raise the RAID item for the Class Manager confirmations on the day Task 2 closes, with this task's named date as its due date.

## Notes for refinement

- **An unprepared session fails.** Criterion 1 is the agenda. Asking a Class Manager for a threshold without the distribution in front of them returns "it depends" and spends the one convening.
- **Fallback if the session cannot be convened in its week:** run per-class conversations and take Ray Reuter first — he covers two of the three classes, so one conversation unblocks two thirds of the downstream rule configuration. Do not let the workshop format become the blocker.
- **Hand over, don't absorb:** anything surfacing that belongs to server build lifecycle (Feature 1640805), server decommission lifecycle (Feature 1640819), non-discoverable CI attribute change (Feature 1640795) or automated CI-impact notifications (Feature 1642240) goes to that feature.
- **Dependency to watch:** Adam Griffis is taking over as Accenture CMDB senior architect while already owning six PI-4 features at 50% allocation. Where Jeff Schwartzkopf can answer alone, route to Jeff.
- Prior design work exists in the vault as draft correctness stories CR-1, CR-2 and CR-3, covering per-class identification rules, discovery sources and orphan bases. Phase 1 confirms those against the live instance and supplies the numbers they left open. Findings from the sibling duplicate-detection spike are welcome in the session but are not a prerequisite for it.
