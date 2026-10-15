---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-4
feature: "1639308 — CMDB Adoption Campaign — Content, Training & Communications"
objective: "PI-4 Obj 3 (1639072) — Drive CMDB Adoption Across PPL User Groups"
sow: "AP00288 Deliverable 7"
gate: 2027-01-30
sprint: "4.2 (start) → 4.6"
status: draft
updated: 2026-10-14
tags: [work, cmdb-csdm, safe, pi-planning, communication]
relationships:
  - target: "[[PI-4/pi-planning]]"
    type: derived_from
  - target: "[[PI-4/Memory]]"
    type: related_to
  - target: "[[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-database-cert-kb-article-story]]"
    type: related_to
  - target: "[[Config-Mgmt-Plan/ownership-terminology-mapping]]"
    type: related_to
  - target: "[[csdm5-terminology]]"
    type: related_to
---

# Feature 1639308 — Stories & Dependencies (Draft)

**CMDB Adoption Campaign — Content, Training & Communications**
Objective 3 (1639072) · AP00288 **D7** · Sprint 4.2 (Nov 11) → 4.6 · Gate **Jan 30, 2027** · Owner: M. Vazquez

> **Status: DRAFT (2026-10-14)** — no stories exist in ADO yet. Per [[definition-of-ready]], create stories from the Feature "+" link, never standalone.

---

## Three things to fix at the feature level first

1. **The feature's acceptance criteria still say "rolled out … by Feb 2, 2027."** AP00288 D7 moved the gate to **Jan 30, 2027** (see [[PI-4/Memory]]). Correct the ADO AC before refinement, or the team plans to the wrong date. *(The SOW itself prints "January 30, **2026**" — a drafting defect already logged for pre-signature correction; the intended year is 2027.)*

2. **This feature carries the whole objective and the whole January invoice.** 1639308 is the only feature under 1639072, and D7 is the only deliverable invoiced in January ($493,794). There is no second item to evidence against. That is the reason for AC-10 below — a packaged acceptance submission, not just "campaign done."

3. **Rollout cannot be one event in 4.6.** Risk 8 in [[PI-4/pi-planning]] gives an 11-day buffer between Sprint 4.6 close (Jan 19) and the Jan 30 gate — with OCM sign-off still to obtain and Sprint 4.5 lost to holidays. The breakdown therefore splits rollout into **two waves**: Wave 1 (purpose + ownership) in 4.4, Wave 2 (request process) in 4.6, so a failed Wave 2 does not mean zero rollout evidence.

---

## Phasing

| Phase | Sprint | Items | Why here |
|-------|--------|-------|----------|
| Define | 4.2 (Nov 11–24) | AC-1, AC-2, AC-3 | Nothing can be written until audiences, reusable assets, and the OCM review path are known |
| Build | 4.3–4.4 (Nov 25–Dec 22) | AC-4, AC-5, AC-6, AC-7 | Content + its versioned home + the measurement mechanism |
| Roll out | 4.4 / 4.6 | AC-8 (Wave 1), AC-9 (Wave 2) | Wave 1 before the holiday sprint; Wave 2 after D9 catalog lands |
| Evidence | 4.6 (Jan 6–19) | AC-10 | Submit with buffer before the Jan 30 gate |

**Sprint 4.5 (Dec 23 – Jan 5) carries no campaign work by design** — it is the OCM review window and holiday buffer. Do not schedule a push into it; audience availability is at its lowest point of the PI.

**Critical path:** AC-1 → AC-4 → AC-8 → AC-9 → AC-10. AC-3 (OCM path) is the item most likely to silently consume the buffer.

---

## Stories (10)

---

### AC-1 · [Spike] Define and confirm the campaign's target audiences and personas

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Spike |
| Parent feature | 1639308 |
| Sprint | 4.2 |
| Owner | M. Vazquez |
| Points | TBD |
| State | Draft |
| Depends on | DEP-2, DEP-10 |
| Tags | `CMDB-Adoption` `OCM` `PI4-Obj3` |

**As** the CMDB Product Owner,
**I want** the campaign's target audiences defined as named, sized groups with their specific CMDB responsibilities — not "PPL users",
**so that** content can be written to what each audience actually has to do, and rollout can be evidenced per audience against the D7 gate.

**Acceptance criteria:**

1. Audience list is **named groups, not role abstractions** — each entry identifies the actual ServiceNow group / distribution list / organizational unit and an approximate population count.
2. Candidate audiences assessed and explicitly included or excluded with a reason: Technical Owner Groups (`managed_by_group`), CI Owners (`managed_by`), Support Groups (`support_group`), Business Application owners, requesters / Service Desk, CCB members and Class Managers, and the **contract teams with MSA-mandated CMDB duties** (DBA, Network Admin, Voice Management, Hands & Feet — Exhibits D/E/I/K) — see DEP-10.
3. Each audience has: the CMDB actions it is expected to perform, the systems/screens it touches, its current known pain points, and its reachable channel(s).
4. Audience list reviewed with OCM (Nora Lizenberg) and **signed off by the Process Owner / CCB Chair (Josh Sterling)** — recorded in writing, not verbal.
5. Output is a single referenceable artifact in the vault + the agreed PPL location, cited by every downstream story.

**Dependencies:** DEP-2 (PO/Process Owner sign-off), DEP-10 (contract-team audience decision).

---

### AC-2 · [Spike] Inventory existing CMDB content and agree a reuse / no-duplicate map

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Spike |
| Parent feature | 1639308 |
| Sprint | 4.2 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | AC-1, DEP-7 |
| Tags | `CMDB-Adoption` `knowledge` `PI4-Obj3` |

**As** the CMDB Product Owner,
**I want** an inventory of CMDB training and communication material that already exists, mapped against the AC-1 audiences,
**so that** the campaign reuses what is already published and no audience receives two different explanations of the same process from two different workstreams.

**Acceptance criteria:**

1. Inventory covers at minimum: the CI-certification training stories and KB articles (Server SV-5/SV-9 off 1603551, Database DB-6b off 1641258, Computers, Network Gear), the temporary application **intake template**, CCB/governance documentation, and the Configuration Management Plan material.
2. Each asset is classified **reuse as-is / update / supersede / out of scope**, with the owning workstream named.
3. **Overlap with the certification workstream is resolved explicitly** — certification KB articles already target Technical Owner Groups, which is also a campaign audience. States which workstream owns which message to that group.
4. Produces the campaign **content backlog**: the list of net-new assets AC-4 and AC-6 must write, with nothing on it that duplicates an inventoried asset.
5. Gaps where no asset exists for an AC-1 audience are called out as content backlog items, not silently dropped.

**Dependencies:** AC-1 (audiences), DEP-7 (certification workstream coordination).

---

### AC-3 · [Enabler – Process] Agree the OCM review, sign-off, and distribution path

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Enabler – Process |
| Parent feature | 1639308 |
| Sprint | 4.2 |
| Owner | M. Vazquez |
| Points | TBD |
| State | Draft |
| Depends on | DEP-1, DEP-9 |
| Tags | `CMDB-Adoption` `OCM` `governance` `PI4-Obj3` |

**As** the CMDB Product Owner,
**I want** the OCM review and approval path for campaign content agreed and dated before any content is drafted,
**so that** review turnaround is a planned input to the schedule rather than the thing that consumes the 11-day buffer before the Jan 30 gate.

**Acceptance criteria:**

1. OCM reviewer(s) named and **resourcing confirmed** for the Nov–Jan window, including the holiday period (Nora Lizenberg / OCM Support — DEP-1).
2. **Review turnaround expectation agreed in writing** (e.g. 5 business days per submission) and mapped backwards from Jan 30 to produce content-freeze dates for AC-4 and AC-6.
3. Approval record format agreed — what constitutes OCM sign-off and where it is stored, since it is a D7 acceptance artifact.
4. Approved distribution channels confirmed per AC-1 audience, with the distribution lists verified to reach **offshore and contractor audiences** and not just onshore PPL staff (DEP-9).
5. Campaign calendar published: submission dates, review windows, Wave 1 and Wave 2 send dates, with **no send scheduled Dec 23 – Jan 5**.
6. Precedent followed: OCM communications were required before the Business App enhancement pause rollout (2026-06-10) — same gate applies here.

**Dependencies:** DEP-1 (OCM resourcing), DEP-9 (channels and lists).

---

### AC-4 · [User Story] Core content set — CMDB purpose and ownership responsibilities

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1639308 |
| Sprint | 4.3 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | AC-1, AC-2, AC-3, DEP-3, DEP-4 |
| Tags | `CMDB-Adoption` `knowledge` `PI4-Obj3` |

**As** a PPL user who owns or supports CIs,
**I want** material that tells me what the CMDB is for and exactly which ownership fields I am responsible for keeping right,
**so that** I know what is expected of me without having to ask someone on the CMDB team.

**Acceptance criteria:**

1. Content covers **CMDB purpose** (why it exists, what consumes it — incident, change, service mapping, audit, security) in terms of the audience's own work, not platform terminology.
2. Content covers **ownership responsibilities** per audience, using the authoritative attribute definitions from [[Config-Mgmt-Plan/cmdb-ownership-scoping-matrix]] and [[Config-Mgmt-Plan/cmdb-csdm-attribute-schema]].
3. **Field labels match what the audience actually sees in the PPL instance.** PPL labels `managed_by` as "CI Owner" and `managed_by_group` as "Technical Owner Group" — which conflicts with CSDM 5.0's `owned_by`/`managed_by` split and is an **open CCB item** (DEP-3). Content uses the PPL UI label with the CSDM term noted, and is re-checked against the CCB ruling before Wave 1 send.
4. **CSDM 5.0 terminology applied** — Service Instance / Application Service handled per [[csdm5-terminology]], with PPL's actual instance version confirmed (DEP-4). Where the UI still shows the old term, content shows both.
5. Variants produced per AC-1 audience from a single source — no audience-specific rewrite that can drift from the others.
6. Content is **self-serve and asynchronous** (readable/viewable without attending a live session) so distributed onshore/offshore/contractor audiences are not timezone-dependent.
7. Submitted to OCM per the AC-3 calendar; review comments incorporated; sign-off recorded.

**Dependencies:** AC-1, AC-2 (content backlog), AC-3 (review path), DEP-3 (CI Owner label ruling), DEP-4 (CSDM version).

---

### AC-5 · [Enabler – Configuration] Stand up the versioned, accessible content home

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Enabler – Configuration |
| Parent feature | 1639308 |
| Sprint | 4.3 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | AC-3 |
| Tags | `CMDB-Adoption` `knowledge` `PI4-Obj3` |

**As** the CMDB Product Owner,
**I want** one published, versioned home for all campaign content with a named owner for updates,
**so that** the material does not go stale as CMDB processes change, and users have a single place to come back to after the campaign ends.

**Acceptance criteria:**

1. Location agreed and created (ServiceNow Knowledge Base space/category confirmed, consistent with where the certification KB articles live — AC-2).
2. Every asset carries a **version, last-reviewed date, and named content owner**.
3. A **review trigger** is documented: content is re-reviewed when CMDB terminology or process changes (named examples — CSDM naming, intake/catalog changes, ownership attribute rulings), not on an arbitrary calendar alone.
4. Access verified for all AC-1 audiences, **including contractors and offshore staff** — no asset behind a permission that an audience member does not hold.
5. Links are stable and citable so communications point at the home rather than carrying attachments.

**Dependencies:** AC-3 (channel/location approvals).

---

### AC-6 · [User Story] Process content — how to request a CMDB change or update

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1639308 |
| Sprint | 4.4 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | AC-4, AC-5, DEP-5, DEP-6 |
| Tags | `CMDB-Adoption` `knowledge` `PI4-Obj3` |

**As** a PPL user who needs a CI record changed,
**I want** step-by-step material showing the correct channel to request it,
**so that** I stop using ad-hoc channels and the change goes through a governed path.

**Acceptance criteria:**

1. Content documents the **request/update path that is actually live at time of publication** — the temporary intake template, the non-discoverable CI attribute update catalog item (**1640795 / D9, due Dec 31**), and the Business Application modify path.
2. **Content is written against what is in PROD, not what is planned.** Publication is held until 1640795 is in PROD (DEP-5), or the asset ships with that section marked "available from <date>".
3. **Service Map Update Requests (1640844 / D12) are addressed explicitly** — that catalog item is not due until **Feb 2, 2027, after the campaign's Jan 30 gate** (DEP-6). Content either excludes it with a stated reason or describes it as forthcoming with no live link. This is a decision for the PO, recorded in the story.
4. Content states what users should **stop** doing (direct edits, informal requests) and what happens if they do — the behavioural change the benefit hypothesis depends on.
5. Includes the escalation/help path for requests that do not fit a catalog item.
6. Submitted to OCM per the AC-3 calendar; sign-off recorded.

**Dependencies:** AC-4 (shared source + tone), AC-5 (home), DEP-5 (D9 in PROD), DEP-6 (D12 lands after the gate).

---

### AC-7 · [Enabler – Process] Feedback mechanism and pre-rollout measurement baseline

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Enabler – Process |
| Parent feature | 1639308 |
| Sprint | 4.3 (baseline) → 4.4 (mechanism live) |
| Owner | M. Vazquez |
| Points | TBD |
| State | Draft |
| Depends on | AC-1, DEP-8 |
| Tags | `CMDB-Adoption` `PI4-Obj3` |

**As** the CMDB Product Owner,
**I want** a feedback mechanism and a measured pre-campaign baseline,
**so that** the benefit hypothesis ("measurable drop in data-quality tickets attributable to user error") can actually be evidenced instead of asserted.

**Acceptance criteria:**

1. **"Data-quality ticket attributable to user error/misunderstanding" is defined as a query** — specific tables, categories, and filters. If no such category exists today, the story records that and defines the closest measurable proxy (DEP-8).
2. **Baseline captured and dated before Wave 1 sends** (AC-8). A baseline taken after rollout begins is worthless.
3. Feedback mechanism is two-way and low-friction — survey or equivalent that asks whether the audience knows what it is responsible for and how to request a change, with a free-text route for questions.
4. Mechanism is reachable by every AC-1 audience through its approved channel, including offshore/contractor audiences.
5. Responses are attributable to audience (not necessarily to individual) so effectiveness can be read per group.
6. Reporting view agreed with the PO for how results will be presented at the gate.

**Dependencies:** AC-1 (audiences), DEP-8 (ticket-category baseline definition).

---

### AC-8 · [User Story] Wave 1 rollout — purpose and ownership responsibilities

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1639308 |
| Sprint | 4.4 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | AC-4, AC-5, AC-7 |
| Tags | `CMDB-Adoption` `communication` `PI4-Obj3` |

**As** a targeted PPL audience member,
**I want** to receive the CMDB purpose and ownership material through a channel I actually read,
**so that** I understand my CMDB responsibilities before the January process rollout lands.

**Acceptance criteria:**

1. AC-4 content distributed to **every AC-1 audience** through its approved channel, per the AC-3 calendar — **completed before Dec 23**.
2. OCM sign-off obtained **before** the send, evidenced.
3. At least one **asynchronous** consumption route per audience (recording, KB article, or written walkthrough) so no audience depends on attending a live session.
4. Any live session is scheduled to cover distributed timezones, recorded, and the recording published to the AC-5 home.
5. **Distribution is evidenced per audience** — what was sent, to which list, on what date, with reach/open data where the channel provides it. This is a D7 acceptance artifact.
6. AC-7 feedback mechanism is live and referenced in the communication.
7. Questions received are logged — they are the input to the Wave 2 content check and to office hours.

**Dependencies:** AC-4, AC-5, AC-7 (baseline must already be captured).

---

### AC-9 · [User Story] Wave 2 rollout — request process + post-rollout feedback read

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1639308 |
| Sprint | 4.6 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | AC-6, AC-7, AC-8, DEP-5 |
| Tags | `CMDB-Adoption` `communication` `PI4-Obj3` |

**As** a targeted PPL audience member,
**I want** to be shown the live request/update process once it is actually available,
**so that** I submit CMDB changes through the proper channel from the point it exists.

**Acceptance criteria:**

1. AC-6 content distributed to all AC-1 audiences, with OCM sign-off evidenced, **completed by Jan 19 (Sprint 4.6 close)** to leave buffer before the Jan 30 gate.
2. Content re-verified against the live state at send time — 1640795 in PROD, terminology current (AC-4 #3/#4), no link to anything not yet available.
3. Office hours or an equivalent Q&A route offered at least once, scheduled for distributed audiences and recorded.
4. **Post-rollout feedback read taken** against the AC-7 mechanism: positive confirmation from targeted audiences that they know how to interact with the CMDB, reported per audience.
5. Baseline comparison started — ticket-metric read taken and recorded, with the caveat that behaviour change will not be fully visible by Jan 30 stated honestly rather than overclaimed.
6. Gaps (audiences with low reach or low confirmation) identified with a named follow-up action, carried into PI-5.

**Dependencies:** AC-6, AC-7, AC-8, DEP-5.

---

### AC-10 · [Enabler – Process] D7 acceptance package and delivery notification

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Enabler – Process |
| Parent feature | 1639308 |
| Sprint | 4.6 |
| Owner | M. Vazquez |
| Points | TBD |
| State | Draft |
| Depends on | AC-8, AC-9 |
| Tags | `CMDB-Adoption` `governance` `PI4-Obj3` |

**As** the CMDB Product Owner,
**I want** D7 submitted as a single evidenced package with written delivery notification,
**so that** the three-business-day deemed-acceptance clock starts on a known date and the $493,794 January invoice is not exposed.

**Acceptance criteria:**

1. Package assembles the D7 evidence set: audience definition + sign-off (AC-1), content assets with versions (AC-4, AC-6), OCM sign-off records (AC-3), distribution evidence per audience (AC-8, AC-9), feedback mechanism and results (AC-7, AC-9).
2. **Written delivery notification issued on or before Jan 22, 2027** — not Jan 29 — so the three-business-day acceptance window closes before the Jan 30 gate.
3. PPL reviewer availability confirmed in advance for that window (Risk 6 in [[PI-4/pi-planning]]).
4. Submission date, recipient, and response logged.
5. Any PPL rejection or comment has a named remediation owner and a date inside the remaining window.

**Dependencies:** AC-8, AC-9 (nothing to submit without both waves).

---

## Dependencies

| # | Description | Depends on | Needed by | Status |
|---|-------------|-----------|-----------|--------|
| DEP-1 | **OCM review capacity and turnaround** for Nov–Jan, including the holiday period. OCM is a dependency, not a team member — an unquantified review time is the single largest threat to the Jan 30 gate. | Nora Lizenberg / OCM Support | AC-3 (Sprint 4.2) | Open |
| DEP-2 | **Audience/persona sign-off** — written confirmation that the defined audiences are the right ones. | Josh Sterling (Process Owner / CCB Chair), PO | AC-1 (Sprint 4.2) | Open |
| DEP-3 | **CI Owner / `managed_by` label ruling** — PPL labels `managed_by` as "CI Owner", conflicting with CSDM 5.0's `owned_by`/`managed_by` split. Open CCB item. Teaching the wrong label to the whole user base is harder to undo than to delay. | CCB | AC-4 content freeze | Open |
| DEP-4 | **CSDM 5.0 terminology state on PPL's instance** — Application Service → Service Instance. | Stan Tomberg | AC-4 (Sprint 4.3) | Open |
| DEP-5 | **1640795 (Catalog Item — Non-Discoverable CI Attribute Updates, D9) in PROD** — due Dec 31. Process content cannot describe a catalog item that is not live. | Feature 1640795 | AC-6 publication, AC-9 send | Scheduled Dec 31 |
| DEP-6 | **1640844 (Catalog Item — Service Map Update Requests, D12) is due Feb 2, 2027 — after this feature's Jan 30 gate.** The campaign cannot train users on a request path that does not exist yet. Needs an explicit in/out decision. | PO decision | AC-6 (Sprint 4.4) | **Open — flagged** |
| DEP-7 | **Certification workstream coordination** — certification training/KB assets already target Technical Owner Groups (SV-5, SV-9/1603551, DB-6b/1641258). Avoid two workstreams messaging the same group. | Certification feature owners | AC-2 (Sprint 4.2) | Open |
| DEP-8 | **Baseline ticket definition** — "data-quality tickets attributable to user error" may not exist as a reportable category today. Without it the benefit hypothesis is unmeasurable. | Reporting / PO | AC-7 baseline, before AC-8 | Open |
| DEP-9 | **Approved channels + distribution lists** that verifiably reach offshore and contractor audiences, not just onshore PPL staff. | OCM / comms | AC-3 (Sprint 4.2) | Open |
| DEP-10 | **Contract-team audience decision** — DBA, Network Admin, Voice Management, and Hands & Feet teams carry MSA-mandated CMDB duties (Exhibits D/E/I/K). In or out of campaign scope? | PO decision | AC-1 (Sprint 4.2) | **Open — decision needed** |

---

## Risks specific to this feature

| # | Risk | Impact | Mitigation |
|---|------|--------|------------|
| 1 | **OCM review time is unknown and unresourced.** If review is two weeks per submission, AC-6 content must be final by early January — inside the holiday sprint. | High | AC-3 fixes turnaround in writing in Sprint 4.2 and back-schedules content freezes from Jan 30 |
| 2 | **Single-feature objective, single-deliverable invoice.** No partial credit; nothing else evidences 1639072. | High | Two-wave rollout (AC-8/AC-9) so Wave 1 evidence exists by Dec 23 |
| 3 | **Sprint 4.5 (Dec 23 – Jan 5) is dead time** — lowest audience availability of the PI sits between content completion and Wave 2. | Medium | No sends scheduled in 4.5; it is the OCM review window and buffer |
| 4 | **Teaching contested terminology.** DEP-3 is open at CCB; retraining a whole user base on a corrected ownership label costs more than the delay. | Medium | AC-4 #3 — use PPL UI labels, note CSDM terms, re-verify before Wave 1 send |
| 5 | **Benefit hypothesis may be unmeasurable.** If the ticket category does not exist, "measurable drop" cannot be shown at the gate. | Medium | DEP-8 + AC-7 define the query or an agreed proxy before Wave 1 |
| 6 | **Behaviour change will not be visible by Jan 30.** Even a successful campaign will not have moved ticket volumes in 11 days. | Medium | AC-9 #5 — report confirmation-of-understanding at the gate and ticket trend as a PI-5 follow-on; do not overclaim |
| 7 | **Content describes a process still being built.** D9 lands Dec 31, D12 after the gate. | Medium | AC-6 #2/#3 — publish against PROD state only |

---

## Open questions for refinement

1. Does the ADO feature AC get corrected to **Jan 30, 2027** before or at PI Planning (Nov 4)?
2. Is OCM a named, allocated resource for this feature, or a best-effort dependency? If best-effort, does the Jan 30 commitment hold?
3. **DEP-10** — are the MSA contract teams a campaign audience? They have contractual CMDB duties, which makes them the highest-leverage audience and also the one most likely to be assumed out of scope.
4. **DEP-6** — does campaign content mention Service Map Update Requests at all, given the catalog item lands after the gate?
5. Who writes the content? None of AC-4/AC-6 has a named owner — the team is configuration-heavy, and content authoring is not an obvious fit for current capacity.
6. Is "training delivered" at the certification level (SV-5 pattern) being counted toward this campaign, or kept separate? Affects both AC-2 and what D7 claims.
