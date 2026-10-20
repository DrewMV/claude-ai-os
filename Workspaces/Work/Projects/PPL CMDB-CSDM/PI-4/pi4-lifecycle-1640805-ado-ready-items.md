---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-4
feature: "1640805 — Server Build Lifecycle Process Flow"
objective: "PI-4 Obj 4 (1639075) — Implement CMDB Lifecycle Management Process Flows"
sow: "AP00288 Deliverable 10"
gate: 2027-02-02
sprint: "4.3 → 4.4"
status: draft
updated: 2026-10-16
tags: [work, cmdb-csdm, safe, pi-planning, servicenow, governance]
relationships:
  - target: "[[PI-4/pi4-lifecycle-1640805-server-build-stories-dependencies]]"
    type: derived_from
  - target: "[[Backlog/feature-story-templates]]"
    type: derived_from
  - target: "[[Backlog/definition-of-ready]]"
    type: related_to
---

# Feature 1640805 — ADO-Ready Items (fitted to Sprints 4.3–4.4)

**Server Build Lifecycle Process Flow** · Objective **1639075** · AP00288 **D10** · Gate **Feb 2, 2027**

> **Status: DRAFT (2026-10-16).** Nothing created in ADO. Six items, fitted to the scheduled window of **Sprint 4.3 (Nov 25 – Dec 8)** and **Sprint 4.4 (Dec 9–22)**.

Reasoning, the full dependency table (DEP-1…DEP-11) and the risk register are in [[PI-4/pi4-lifecycle-1640805-server-build-stories-dependencies]]. The fuller eleven-item decomposition this was compressed from is mapped in the appendix.

---

## The schedule constraint

| | |
|---|---|
| Scheduled window | Sprint 4.3 (Nov 25 – Dec 8) + Sprint 4.4 (Dec 9 – Dec 22) |
| Working days | **≈ 18** — 4.3 opens on Thanksgiving (Nov 26) and loses two days; 4.4 has ten |
| Then | Sprint 4.5 (Dec 23 – Jan 5) is the holiday shutdown — no capacity |
| Contract gate | Feb 2, 2027, with delivery notification due **on or before Jan 27** |

**Everything the team controls has to land inside those 18 days.** What the team does not control — a Class Manager sign-off, a possible customization approval, a change window — has to run *alongside* the build rather than in front of it. That is what makes this window tight, not the number of stories.

This plan therefore makes two scope choices up front, both of which need PO confirmation. They are the reason it fits.

### Scope choice 1 — build to the AP00288 floor

AP00288 D10 requires only that *"a CMDB process flow is configured to manage the build lifecycle for the server CI class, enabling new servers to be accurately reflected in the CMDB upon provisioning"*, delivered as **XML**.

This plan builds to that, which means:

- **The three already-ratified mandatory attributes** — Name, Serial Number, Operational Status — plus ownership and support group where the assignment process already supports it.
- **OOB `Operational Status` values**, not a new ratified list.
- **No CMDB data-dictionary change**, so no CCB agenda slot on the critical path. The governance dependency reduces to a **Class Manager sign-off on the flow** (Ray Reuter), which can run in parallel.

**What this gives up:** the ADO acceptance criterion *"new server CIs created with mandatory attributes populated at build time"*, read as an extended attribute set. Under this plan the flow populates what is already mandatory and whatever ownership data the existing process can supply — not a newly mandated set.

**Recommendation:** confirm with Joe. If he wants the extended set, it is a CCB data-dictionary change on a monthly cadence and **this feature does not fit 4.3–4.4** — see Risk 1.

### Scope choice 2 — deploy inside Sprint 4.4

Production deployment is planned for **Sprint 4.4, before Dec 22**, rather than after the holiday.

**Why:** it fits the scheduled window, and it gives roughly five weeks of real build activity before the Jan 27 delivery notification instead of the six business days a January deploy would leave. The "live and in use" evidence problem largely solves itself.

**Risk:** a PPL December change freeze is **unconfirmed** and would block it. Confirm with Kostas before PI Planning. If a freeze applies, the deploy moves to Sprint 4.6 and A6 moves with it — see Risk 3.

---

## Before creating anything

- [ ] Confirm the parent objective is **1639075**. Create every item from the **Feature 1640805 "+" link** — never standalone ([[requirements-process#ADO Hierarchy Rule]]).
- [ ] **Get the two scope choices above confirmed by the PO before refinement.** Both change the shape of the work, not just its size.
- [ ] **Engage Ray Reuter in week 1 of 4.3, not at the end.** A2 runs in parallel with A1 or the window closes.
- [ ] A1 makes the configuration-vs-customization call. If anything is customization, the `Customization` tag, a linked RAID issue and Sonika Das's approval are needed **before implementation** ([[requirements-process#Customization Governance]]) — raise the RAID issue the day A1 closes.
- [ ] Assign **P1–P4** with numeric sub-ranking. Share IDs with Anu for Program Backlog Review.
- [ ] **Raise the external dependencies as RAID items, not as acceptance criteria.** Consolidating six items from eleven means blockers no longer have their own rows on the board.

**Suggested tags:** `CMDB-Lifecycle` `PI4-Obj4` `D10`, plus `governance` on A2 and A6.

---

## The list

| # | Type | Title | Sprint |
|---|------|-------|--------|
| A1 | Spike | Server build lifecycle — current state and target design | 4.3 (wk 1–2) |
| A2 | Enabler – Process | Class Manager sign-off on flow and state model | 4.3, parallel |
| A3 | Enabler – Configuration | Configure lifecycle states and build-process precedence | 4.3 (wk 2) → 4.4 |
| A4 | User Story | Create server CIs at provisioning and drive state transitions | 4.4 |
| A5 | User Story | Validate against real builds and deploy to production | 4.4 |
| A6 | Enabler – Process | Operations handover, evidence package and acceptance | 4.4 → Jan (calendar-bound) |

**Critical path:** A1 → A3 → A4 → A5. **A2 runs beside A1, never after it.**

---

### A1 · [Spike] Server build lifecycle — current state and target design

**Sprint 4.3, weeks 1–2** · **Timeboxed — hard stop at the end of 4.3**

> **Superseded.** A1 exists in ADO as **Spike 1656313**, with A2 folded into it as an exit gate. The current version — workshop-led, with the Thanksgiving calendar as an explicit constraint — is [[PI-4/pi4-lifecycle-1656313-server-build-spike-workshop]]. The criteria below are the pre-ADO draft; read them for the reasoning, not as the current acceptance criteria.

Establish how servers are provisioned today, and design the target flow, state model and Discovery coexistence well enough for build to start.

**Acceptance criteria**

1. **Build paths enumerated** — physical, virtual (vCenter), cloud — each with its trigger and the tooling that performs it. Paths that are **out of scope are named and excluded in writing**; this spike does not have the days to cover all three if they differ substantially.
2. **Scope boundary recorded against the sibling deliverables** — retirement is D11 (1640819), staleness and orphan monitoring is D8 (1639335), non-discoverable attribute change is D9 (1640795). Anything found that belongs to those is handed over, not absorbed.
3. **Target flow documented** as states, transitions, trigger per transition and owner per step, using **OOB `Operational Status` values** per scope choice 1. Produced with visibility to 1640819 so the same state set serves decommission (DEP-6).
4. **Build-time attribute list fixed** — the three ratified attributes plus a decision on CI Owner and Support Group: populated at provisioning if the existing assignment process supports it (DEP-1), otherwise explicitly out of scope with the reason recorded. **Any attribute requiring a data-dictionary change is logged and excluded from this feature.**
5. **Identification designed against the serial-number gap.** A build-time CI usually has no serial; the `PPL Server` rule matches Serial at 100, serial-lookup at 200, Name only at 300. States what identifies the CI before a serial exists and what happens when Discovery later supplies one — a named mechanism, not an assumption that IRE copes.
6. **Reconciliation precedence designed.** The Server class has no reconciliation rules of its own — all five derive from Computer/Hardware, SG-SCCM at 90/100, ServiceNow at 80/100/200. States whether the build process is registered as a discovery source, which attributes it is authoritative for, and which yield to Discovery. Reviewed with Stan Tomberg (DEP-2). **Also covers auditability** — how a build event is traced back to the process that created the record.
7. **Timeliness window defined as a number, anchored to provisioning** — the contract's own trigger word.
8. **Current build-to-CI lag recorded**, from existing data where a measurement would not fit the timebox. Estimated values are labelled as estimates. This is the baseline the benefit hypothesis is read against at A6.
9. **Build volume baselined** — servers provisioned per month, split by path. Determines what "in use" can evidence at A6.
10. **The teams that perform builds are named**, and identified as PPL staff or contract teams with MSA-mandated CMDB duties (Hands & Feet, DBA — Exhibits D/E/I/K). Decides how the change is communicated in A5.
11. **Configuration vs. customization determined**, with the RAID issue raised the same day if the answer is customization.
12. A3–A5 sized, each passing [[Backlog/definition-of-ready]] gates 1–4.

> **Timebox discipline:** this spike merges what were two spikes. If it is still open at the end of 4.3, escalate rather than extend — A3 cannot start without #3, #5 and #6, and there is no slack behind it.

---

### A2 · [Enabler – Process] Class Manager sign-off on flow and state model

**Sprint 4.3 — runs in parallel with A1, not after it** · Depends on DEP-1

**As** the CMDB governance team, **we need** the lifecycle flow and state model signed off by the Class Manager, **so that** the flow is built against something the governance owner has agreed to.

**Acceptance criteria**

1. **Ray Reuter (Class Manager — Servers and Storage CIs) engaged in week 1 of 4.3**, before the design is finished, so review happens alongside the work rather than after it.
2. **Written sign-off on the target flow and state model.** Verbal agreement does not close this.
3. **Ownership model agreed** — how CI Owner and Support Group are determined for a newly provisioned server, naming the source or the responsible party, not a placeholder group.
4. **Status transition rules agreed** — which transitions are automatic, which require approval, who owns each.
5. **Confirmation in writing that no CMDB data-dictionary change is required** for the scope as built. If Ray or the CCB says otherwise, **this is a stop-and-escalate point**, not an acceptance criterion to work around — see Risk 1.
6. Outcome recorded against [[Config-Mgmt-Plan/data-dictionary-ccb-decision-sheet]], noting that `Operational Status` allowed values (row 13) remain an open CCB item being worked around with OOB values rather than resolved.

> **Why this stays a separate item at six.** It is the only external approval on the critical path and the thing most likely to consume the window silently. Folded into an acceptance criterion reading "approved", it would be invisible on the board. If it is merged anyway, carry it as a RAID item.

---

### A3 · [Enabler – Configuration] Configure lifecycle states and build-process precedence

**Sprint 4.3 week 2 → 4.4** · Depends on A1, A2, DEP-2

**As** a CMDB administrator, **I need** the lifecycle states configured and the build process given a defined precedence standing, **so that** server records reflect their operational state and build-time data is not overwritten on the next sync.

**Acceptance criteria**

1. `Operational Status` values configured on the Server class per A1 #3, with a Build state available to the flow.
2. Field configuration and validation rules implemented — a record cannot be saved into a state its transition rules do not permit.
3. **The build process has a defined precedence standing** per A1 #6 — discovery source and/or reconciliation rule created, with the attributes it is authoritative for stated explicitly.
4. **For each build-time attribute, either the build process wins or Discovery wins, and which is recorded.** No attribute left to the derived Computer/Hardware rules by default.
5. **Identification verified against the serial-number gap:** a CI created without a serial, then matched when Discovery supplies one, resolves to **one record**. Verified in a sub-production environment before A4 builds on it.
6. Existing SCCM server precedence (**1356826 / 1403759–1403763**) extended, not contradicted — confirmed with Stan Tomberg.
7. Configuration promoted to test, and documented so the precedence model is readable by someone who did not build it.

---

### A4 · [User Story] Create server CIs at provisioning and drive state transitions

**Sprint 4.4** · Depends on A3, DEP-1

**As** a server build engineer, **I want** a server CI created with its required attributes when the server is provisioned, and its state kept current automatically, **so that** the record is complete and accurate when the server goes live instead of being corrected weeks later.

**Acceptance criteria**

1. A server CI is created at provisioning with **every attribute on the A1 #4 list** populated — the list, not a subset.
2. **Ownership and support group populated through the agreed process** (A2 #3) where in scope, not left blank and not defaulted to a placeholder group.
3. **Required fields enforced at creation, not requested.** A build cannot complete its CMDB step with a required attribute empty.
4. **No duplicate CI is created** where the build path and Discovery/SCCM overlap — verified behaviour, resting on A3 #5.
5. **CI creation occurs within the defined Timeliness window** (A1 #7), measurable from the record.
6. **The record is traceable to the process that created it** — discovery source or request reference visible on the CI.
7. Entry point matches what A1 found: integrated into existing build tooling where a trigger exists, only built as a new catalog item where none does. **No second creation path** alongside existing server onboarding.
8. Each transition in the state model fires on its defined trigger. No transition depends on someone remembering to set a field.
9. **Handoff to Discovery is explicit** — when Discovery first finds the host, the CI moves from Build to Operational, and build-time attributes are retained per the A3 precedence model.
10. **A cancelled or abandoned build leaves the CI in a defined state** — not stranded in Build, which would seed the stale-CI problem D8 (1639335) is separately solving.
11. **Assigned support group notified on assignment**, with content stating what the recipient must do. Whether this uses the D6 framework (**1642240**) or its own mechanism is settled here, not assumed (DEP-7).
12. Tested per [[Backlog/definition-of-done]]; staging deploy and PO demo.

> **Sizing warning.** This merges creation and transitions into one story to fit the window. It is the largest item in the plan and the one most likely to breach DoR gate 5 ("fits within one iteration"). If the team sizes it over one sprint at refinement, split creation from transitions and move the split back into 4.3 — do not let it run across the holiday.

---

### A5 · [User Story] Validate against real builds and deploy to production

**Sprint 4.4** · Depends on A4, DEP-8, DEP-10

**As** a CMDB data consumer, **I want** the flow validated against real builds and deployed to production, **so that** lifecycle management is operational and generating evidence before the holiday.

**Acceptance criteria**

1. **Validated against at least one real build per in-scope path**, not a walkthrough of screenshots, with the build teams named in A1 #10 and the Class Manager present.
2. **Duplicate regression executed and evidenced:** CI created at provisioning without a serial, Discovery later supplies the serial → exactly one CI.
3. **Overwrite regression executed and evidenced:** build-time attribute values survive a full Discovery and SCCM sync cycle.
4. **Timeliness measured** on the test builds against the A1 #7 window and compared with the A1 #8 baseline.
5. Feedback logged with each item either implemented or explicitly deferred with a reason. **Deferrals recorded rather than left open**, so the item can close.
6. **Change communications delivered to every team identified in A1 #10 before the deploy.** Where those are contract teams with MSA-mandated CMDB duties, the communication references the contractual duty, not only the new process. Coordinated with the D7 adoption campaign (**1639308**) so build teams are not messaged twice by two workstreams. At least one asynchronous route; distribution evidenced per team.
7. **December change freeze confirmed or ruled out** before the window is assumed (DEP-10). If a freeze applies, this item stops at validation and the deploy moves — see Risk 3.
8. Change request approved, production migration completed, **with the A3 precedence configuration verified in production, not inferred from staging**.
9. Smoke test: the first real build through the flow produces exactly one complete CI within the Timeliness window.
10. **No Sev 1 or Sev 2 defects open** at close. Rollback position stated.
11. Monitoring established, naming the condition watched — at minimum CIs stuck in Build, and build-path creations that produced no CI.

> **Why validation and deploy are one item.** The window does not allow a validate-then-deploy handoff across a sprint boundary. The cost is that this item cannot be partially done — if the change window slips, the whole item carries, which is why #7 is an early criterion rather than a late one.

---

### A6 · [Enabler – Process] Operations handover, evidence package and acceptance

**Sprint 4.4 for the handover and package; submission is calendar-bound to January** · Depends on A5, DEP-11

**As** the CMDB Product Owner, **I want** the capability owned by an operations team and D10 submitted as an evidenced package, **so that** it has an owner after the contract ends and the three-business-day acceptance clock closes before Feb 2.

**Acceptance criteria — in Sprint 4.4**

1. Support documentation published to an agreed, versioned location with a named content owner.
2. Operational procedures documented for the failure modes that actually occur: a CI stuck in Build, a build that produced no CI, a duplicate that slipped through, an attribute overwritten by Discovery.
3. Knowledge transfer completed and recorded.
4. **Ownership formally accepted by a named team with a named individual accountable** — not "operations" as an abstraction. **AP00288 ends Feb 2, 2027; anything unaccepted before then has no owner afterwards.**
5. **Monitoring from A5 #11 has an owner who will act on it**, identified by name. Escalation path documented.
6. **Evidence package assembled** — the **XML export** of the configured flow as the primary contractual artifact, plus Class Manager sign-off (A2), configuration and precedence documentation (A3), validation and regression evidence (A5), communications evidence (A5 #6), production change record, and the operations acceptance above.

**Acceptance criteria — calendar-bound, January**

7. **"Live and in use" evidenced with actual records** — servers provisioned after go-live that went through the flow, counted against the A1 #9 volume baseline. A December deploy should produce roughly five weeks of this.
8. **Before-and-after stated against the benefit hypothesis** — the A1 #8 build-to-CI lag versus the post-go-live measurement. If the baseline was an estimate, say so.
9. **Written delivery notification issued on or before Jan 27, 2027**, so the three-business-day window closes before Feb 2. PPL reviewer availability confirmed in advance (DEP-11).
10. Submission date, recipient and response logged. Any rejection has a named remediation owner and a date inside the remaining window.

> **This item deliberately spans the window.** Criteria 1–6 are sprint work and close in 4.4. Criteria 7–10 are fixed to the contract calendar and cannot be pulled into December — the evidence does not exist yet and the notification is dated. Track them as a carry item through Sprint 4.5 and 4.6 rather than forcing a close in 4.4.

---

## Risks and recommendation

| # | Risk | Impact | Response |
|---|------|--------|----------|
| 1 | **If the PO wants the extended mandatory-attribute set, this does not fit 4.3–4.4.** That is a CMDB data-dictionary change on a monthly CCB cadence, and the ruling would land mid-build at the earliest. | **High** | Confirm scope choice 1 with Joe **before PI Planning**. If he wants the extension, either the feature starts in 4.2 or the attribute work splits out and ships behind the flow |
| 2 | **A1 is a merged spike with 8 working days and a Thanksgiving start.** It carries what were two spikes, and A3 cannot start without three of its outputs. | **High** | Hard timebox with escalation, not extension. Cut build paths early (A1 #1) rather than covering all three shallowly. Engage Stan Tomberg in week 1 for #6 |
| 3 | **A December change freeze would block the 4.4 deploy**, pushing A5 and A6 into Sprint 4.6 and restoring the six-business-day evidence window. Currently unconfirmed. | **High** | Confirm with Kostas before PI Planning. A5 #7 makes it an early exit rather than a late surprise |
| 4 | **A4 is likely oversized.** Creation plus transitions in one story, in a ten-day sprint, before a holiday. | Medium | Size it honestly at refinement. If it exceeds one iteration, split it and pull the first half into 4.3 |
| 5 | **Consolidation hides blockers.** Six items instead of eleven means the CCB sign-off, the change window and the customization approval no longer have their own board rows. | Medium | Raise all three as RAID items at the start of 4.3 |
| 6 | **Customization approval discovered at A1 close.** If the flow is customization, Sonika's approval is a prerequisite to A3, and the RAID path has lead time the window does not hold. | Medium | A1 #11 makes the call and raises the RAID issue the same day. Flag at Sprint 4.3 planning as a known possible stop |
| 7 | **No slack behind anything.** Sprint 4.5 is the holiday shutdown; the next working window after Dec 22 is Jan 6. Any item that carries out of 4.4 carries two weeks. | Medium | Treat Dec 22 as the real deadline for A1–A5, not Feb 2 |
| 8 | **Nothing covers relationship modelling** — what a new server CI relates to at provisioning (host, database, Service Instance). Dropped to fit the window. | Low | Discovery establishes relationships post-provisioning as it does today. Record as a known limitation at A6, not a defect |

### Recommendation

**The plan above fits 4.3–4.4, but only because of the two scope choices.** Both need Joe's confirmation before PI Planning on Nov 4, and the second needs Kostas to confirm the freeze position.

If either confirmation goes the other way — the extended attribute set, or a December freeze — **the honest answer is that this feature needs Sprint 4.2 for requirements and Sprint 4.6 for release**, which is what [[PI-4/pi4-implementation-plan-appendix]] already assumes and what the eleven-item decomposition in the appendix below is scoped for. That is a schedule conversation to have at PI Planning rather than a problem to absorb inside the sprints.

The single highest-value adjustment available, if any room exists at all, is **pulling A1 into Sprint 4.2**. Sprint 4.2 carries only two feature starts, A1 needs no build capacity, and it would convert the tightest part of this plan into comfortable work without changing the 4.3–4.4 commitment for everything else.

---

## Appendix — mapping from the eleven-item decomposition

The fuller set was built for a 4.2 → 4.6 window. Nothing below was dropped on quality grounds; items were merged to fit the schedule.

| Fitted item | Absorbed | Note |
|---|---|---|
| **A1** | S1 (current state) + S2 (modeling approach) | Two spikes into one timeboxed spike. Relationship modelling (old S2 #8) dropped — see Risk 8 |
| **A2** | S3 (CCB ratification), reduced | Now a Class Manager sign-off, not a CCB data-dictionary ruling. Possible only under scope choice 1 |
| **A3** | S4 | Unchanged |
| **A4** | S5 (CI creation) + S6 (provisioning integration) | Merged; see the sizing warning |
| **A5** | S7 (validation) + S8 (communications) + S9 (deploy) | Communications become an acceptance criterion rather than a story, since D10 carries no contractual rollout obligation |
| **A6** | S10 (operations transition) + S11 (evidence and acceptance) | Split internally into sprint work and calendar-bound work |

The eleven-item version, with full acceptance criteria, is in this file's git history at commit `bd3bedd`.
