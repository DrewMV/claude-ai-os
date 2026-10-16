---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-4
feature: "1640805 — Server Build Lifecycle Process Flow"
objective: "PI-4 Obj 4 (1639075) — Implement CMDB Lifecycle Management Process Flows"
sow: "AP00288 Deliverable 10"
gate: 2027-02-02
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

# Feature 1640805 — ADO-Ready Items

**Server Build Lifecycle Process Flow** · Objective **1639075** · AP00288 **D10** · Gate **Feb 2, 2027**

This is the **creation list** — 11 items to raise in ADO, each with acceptance criteria written to be failed by a tester rather than ticked by an author.

The reasoning behind them — the contract reconciliation, the full dependency table (DEP-1…DEP-11) and the risk register — lives in [[PI-4/pi4-lifecycle-1640805-server-build-stories-dependencies]]. This file does not repeat it; dependencies below are referenced by their DEP number.

**Merged from two drafts.** The shape, the production-deployment story and the operations-transition story come from the team set; the contract grounding, attribute/identification work, CCB item and acceptance item come from the vault draft. Where the two overlapped — "define data standards" versus "evaluate modeling approach" — the definition work folds into S2 (propose) and S3 (ratify) rather than running as a third item.

---

## Before creating anything

- [ ] Confirm the parent objective is **1639075**. Create every item from the **Feature 1640805 "+" link** — never standalone ([[requirements-process#ADO Hierarchy Rule]]).
- [ ] **Resolve the sprint ambiguity.** [[PI-4/pi-planning]] starts this feature in 4.3; [[PI-4/pi4-implementation-plan-appendix]] puts requirements in 4.2. The sprints below follow the appendix. If 4.3 is correct, S3's CCB lead time has nowhere to sit.
- [ ] Assign **P1–P4** per item, with numeric sub-ranking if several are P1.
- [ ] **S2 makes the configuration-vs-customization call.** If any item is customization, it needs the `Customization` tag, a linked RAID issue, and Sonika Das's approval **before implementation** ([[requirements-process#Customization Governance]]).
- [ ] Share the item IDs with Anu for Program Backlog Review tracking.

**Suggested tags:** `CMDB-Lifecycle` `PI4-Obj4` `D10`, plus `governance` on S3/S11 and `OCM` on S8.

---

## The list

| # | Type | Title | Sprint |
|---|------|-------|--------|
| S1 | Spike | Investigate current-state server build lifecycle | 4.2 |
| S2 | Spike | Evaluate CMDB modeling approach for server lifecycle | 4.2 |
| S3 | Enabler – Process | Ratify server lifecycle data standards at the CCB | 4.2 |
| S4 | Enabler – Configuration | Configure lifecycle support and build-process precedence | 4.3 |
| S5 | User Story | Create server CIs at provisioning with required attributes | 4.3 |
| S6 | User Story | Integrate provisioning events with the CMDB | 4.4 |
| S7 | User Story | Validate the server lifecycle process with stakeholders | 4.4 |
| S8 | User Story | Prepare and deliver change communications for build teams | 4.6 |
| S9 | User Story | Deploy server lifecycle capability to production | 4.6 |
| S10 | User Story | Transition lifecycle capability to operations | 4.6 |
| S11 | Enabler – Process | Package D10 evidence and obtain acceptance | 4.6 → 4.7 IP |

**Critical path:** S2 → S3 → S4 → S5 → S9 → S11. **S3 is the long pole** — monthly CCB cadence, not team capacity.

---

### S1 · [Spike] Investigate current-state server build lifecycle

**Sprint 4.2** · Depends on DEP-1, DEP-8

Research how servers are requested, provisioned and brought into service today, and identify every system that contributes lifecycle information to the CMDB.

**Acceptance criteria**

1. Build paths enumerated and mapped **separately where they differ** — physical, virtual (vCenter), cloud — each with the event that triggers it and the tooling that performs it named.
2. For each path: who requests, who approves, who executes, and what record appears in ServiceNow at what point.
3. **Current build-to-CI lag measured, not estimated** — today a server CI appears when Discovery or SCCM finds it, not when it is provisioned. The measured lag is the baseline for the Timeliness NFR and for the benefit hypothesis at S11.
4. **Build volume baselined** — servers provisioned per month over a recent representative period, split by path. Determines whether "in use" can be evidenced in the window available (see S11).
5. **The teams that perform builds are named**, and identified as PPL staff or contract teams carrying MSA-mandated CMDB duties (Hands & Feet, DBA — Exhibits D/E/I/K). This decides whether S8 is training or contract-duty enforcement.
6. Existing adjacent work identified so it is extended rather than rebuilt: SCCM/Discovery server precedence (**1356826 / 1403759–1403763**), credential work (**1444864**), server support-group assignment (Ray Reuter).
7. **Scope boundary stated against the sibling deliverables** — retirement is D11 (1640819), staleness/orphan monitoring is D8 (1639335), non-discoverable attribute change is D9 (1640795). If this spike deliberately covers the retire path as well, it is recorded as **shared with 1640819** so D11's spike does not repeat it.
8. Findings reviewed with stakeholders and published as a single referenceable artifact, cited by S2.

> **Expected output:** Current-State Assessment document.

---

### S2 · [Spike] Evaluate CMDB modeling approach for server lifecycle

**Sprint 4.2** · Depends on S1, DEP-2, DEP-3, DEP-6

Determine how server lifecycle states are represented in the CMDB, which attributes must be populated at provisioning, and how the build process coexists with Discovery and SCCM.

**Acceptance criteria**

1. **Target flow documented** as states, transitions, trigger per transition and owner per step, covering every in-scope path from S1 and naming the paths excluded.
2. **Class scope stated.** AP00288 says *"the server CI class"*; the CCB dictionary covers parent `cmdb_ci_server` only — Windows/Linux child classes were out of scope on July 21. State whether the flow applies at parent or child level, and whether Azure CIs are included given they sit under a different Class Manager.
3. **Lifecycle state set proposed for the full server lifecycle, not just build** — `Operational Status` allowed values (decision-sheet row 13: *Build / Operational / Non-Operational / Retired* vs OOB choices) and the relationship to `install_status` / Life Cycle Stage where PPL uses both. **Produced jointly with 1640819** so one model serves build and decommission (DEP-6).
4. **Build-time attribute list named explicitly**, each entry marked *already CCB-mandatory* (Name, Serial Number, Operational Status) or *proposed addition*, with the source that can populate it at provisioning and the party accountable. Candidates to include or exclude with a reason: **CI Owner (`managed_by`) · Support Group · Technical Owner Group (`managed_by_group`) · Location · Environment**.
5. **Every proposed addition is flagged as a CCB data-dictionary change** and routed to S3. Terminology follows [[Config-Mgmt-Plan/cmdb-csdm-attribute-schema]] and PPL UI labels, noting that *"CI Owner" = `managed_by`* remains an open CCB item (DEP-3).
6. **Identification designed against the serial-number gap.** A build-time CI usually has no serial; the `PPL Server` rule matches Serial at 100, serial-lookup at 200, Name only at 300. States what identifies the CI before a serial exists and what happens when Discovery later supplies one — a named mechanism, not an assumption that IRE copes.
7. **Reconciliation precedence designed.** The Server class has no reconciliation rules of its own — all five derive from Computer/Hardware, with SG-SCCM at 90/100 and ServiceNow at 80/100/200. States whether the build process is registered as a discovery source, which attributes it is authoritative for, and which yield to Discovery. Reviewed with Stan Tomberg (DEP-2).
8. **Relationship impacts assessed** — what the new CI relates to at provisioning (host, database, Service Instance) and what is deferred to Discovery. Uses CSDM 5 terminology per [[csdm5-terminology]].
9. **Timeliness window defined as a number, anchored to provisioning** — the contract's own trigger word. States the maximum compliant interval, measurable against S1 #3.
10. **Auditability mechanism named** — how a build event is traced to the process that created the record (discovery source, audit history, request reference), so the NFR is testable.
11. **Configuration vs. customization determined.** If any part is customization, the `Customization` tag, RAID issue and Sonika Das approval path **start in 4.2**, not at build.
12. Build items listed and sized, each passing [[Backlog/definition-of-ready]] gates 1–4.

> **Expected output:** CMDB Lifecycle Design Recommendation.

---

### S3 · [Enabler – Process] Ratify server lifecycle data standards at the CCB

**Sprint 4.2** · Depends on S2, DEP-1, DEP-4

**As** the CMDB governance team, **we need** the lifecycle states, ownership rules and required attributes ratified by the Class Manager and the CCB, **so that** the flow is built against standards the governance body has agreed to rather than ones the team assumed.

**Acceptance criteria**

1. **Ray Reuter (Class Manager — Servers and Storage CIs) signs off the target flow and state model in writing.** Verbal agreement does not close this.
2. **`Operational Status` allowed values ruled on by the CCB** and recorded against decision-sheet row 13, which is open today. A Build state (or equivalent) exists in the ratified list, or S4 has nothing to configure.
3. **Status transition rules approved** — which transitions are automatic, which require approval, and who owns each.
4. **Ownership model approved** — how CI Owner and Support Group are determined for a newly provisioned server, naming the source or the responsible party, not a placeholder group.
5. **Any attribute proposed for the mandatory set is submitted as an explicit data-dictionary change** with the ruling recorded (Accept / Amend / Defer), chaired by Josh Sterling.
6. **A deferral is a scope answer, not a blocker.** If the CCB declines to extend the mandatory set, the ADO acceptance criteria are renegotiated with the PO **in 4.2** against the AP00288 language — *"accurately reflected in the CMDB upon provisioning"* — and the change is recorded on the feature.
7. Ruling written back into [[Config-Mgmt-Plan/data-dictionary-ccb-decision-sheet]] and the Configuration Management Plan.
8. CCB agenda slot confirmed and the submission lodged against it. The cadence is monthly; a missed agenda costs a sprint on the critical path.

---

### S4 · [Enabler – Configuration] Configure lifecycle support and build-process precedence

**Sprint 4.3** · Depends on S3, DEP-2

**As** a CMDB administrator, **I need** the ratified lifecycle states configured and the build process given a defined precedence standing, **so that** server records reflect their operational state and build-time data is not overwritten on the next sync.

**Acceptance criteria**

1. Ratified `Operational Status` values configured on the Server class, with the Build state available to the flow.
2. Field configuration and validation rules implemented per the S2 design — a record cannot be saved in a state its transition rules do not permit.
3. **The build process has a defined precedence standing** per S2 #7 — discovery source and/or reconciliation rule created, with the attributes it is authoritative for stated explicitly.
4. **For each build-time attribute, either the build process wins or Discovery wins, and which is recorded.** No attribute is left to the derived Computer/Hardware rules by default.
5. **Identification verified against the serial-number gap:** a CI created without a serial, then matched when Discovery supplies one, resolves to **one record**. Verified in a sub-production environment before S5 builds on it.
6. Existing SCCM server precedence (**1356826 / 1403759–1403763**) is extended, not contradicted — confirmed with Stan Tomberg.
7. Configuration promoted to the test environment and documented so the precedence model is readable by someone who did not build it.

---

### S5 · [User Story] Create server CIs at provisioning with required attributes

**Sprint 4.3** · Depends on S4, DEP-1

**As** a server build engineer, **I want** a server CI created with its required attributes at the point the server is provisioned, **so that** the record is complete when the server goes live instead of being corrected weeks later by a data-quality cleanup.

**Acceptance criteria**

1. A server CI is created at provisioning with **every attribute on the S3-ratified list** populated — the list, not a subset.
2. **Ownership and support group are populated through the agreed process** (S3 #4), not left blank and not defaulted to a placeholder group. A blank owner at provisioning reproduces the gap this feature exists to close.
3. **Required fields are enforced at creation, not requested.** A build cannot complete its CMDB step with a required attribute empty.
4. **No duplicate CI is created** where the build path and Discovery/SCCM overlap — verified behaviour, resting on S4 #5.
5. **CI creation occurs within the defined Timeliness window** (S2 #9), measurable from the record.
6. **The record is traceable to the process that created it** (S2 #10) — discovery source or request reference visible on the CI.
7. The entry point matches what S1 found: integrated into existing build tooling where a trigger exists, and only built as a new catalog item or interface where none does. No second creation path alongside existing server onboarding.
8. **Assigned support group is notified on assignment**, with content stating what the recipient must do. Whether this uses the D6 framework (**1642240**) or its own mechanism is settled here, not assumed (DEP-7).
9. Tested per [[Backlog/definition-of-done]]; staging deploy and PO demo.

---

### S6 · [User Story] Integrate provisioning events with the CMDB

**Sprint 4.4** · Depends on S5

**As** a CMDB data consumer, **I want** server lifecycle updates synchronised automatically, **so that** the CMDB reflects current server status without manual intervention.

**Acceptance criteria**

1. Integration logic implemented and **mapping rules documented per source system** identified in S1.
2. Each transition in the S3 state model fires on its defined trigger. No transition depends on someone remembering to set a field.
3. **Handoff to Discovery is explicit** — when Discovery first finds the host, the CI moves from Build to Operational per the agreed rule, and build-time attributes are retained per the S4 precedence model.
4. **A cancelled or abandoned build leaves the CI in a defined state** — not stranded in Build indefinitely, which would seed the stale-CI problem D8 (**1639335**) is separately solving.
5. Test records processed successfully across **every in-scope build path**, not a single synthetic record.
6. **Reconciliation verified as a named test:** build-time values survive a full Discovery and SCCM sync cycle. Executed and evidenced, not asserted.
7. Transition history auditable on the record.
8. Tested per [[Backlog/definition-of-done]]; staging deploy and PO demo.

---

### S7 · [User Story] Validate the server lifecycle process with stakeholders

**Sprint 4.4** · Depends on S5, S6

**As** a server lifecycle stakeholder, **I want** to review and validate the process against real builds, **so that** it meets operational and governance requirements before it reaches production.

**Acceptance criteria**

1. Validation workshop held with the build teams named in S1 #5, the Class Manager, and the PO.
2. **Validated against at least one real build per in-scope path**, not a walkthrough of screenshots.
3. **Duplicate regression executed and evidenced:** CI created at provisioning without a serial, Discovery later supplies the serial → exactly one CI.
4. **Overwrite regression executed and evidenced:** build-time attribute values survive a full Discovery and SCCM sync cycle.
5. **Timeliness measured** on the test builds against the S2 #9 window and compared with the S1 #3 baseline.
6. Required-attribute completeness verified on every test record — populated, not prompted for.
7. Feedback logged with each item either implemented or explicitly deferred with a reason. **Deferrals are recorded rather than left open**, so this item can close.
8. Approval received from the Class Manager and the PO.
9. Evidence captured in the form S11 will submit.

---

### S8 · [User Story] Prepare and deliver change communications for build teams

**Sprint 4.6** · Depends on S7, DEP-8, DEP-9

**As** a server build engineer, **I want** to be told what the new CMDB step in my build process is and how to do it before it becomes mandatory, **so that** I follow the new flow rather than working around it.

**Acceptance criteria**

1. Materials produced for **every team identified in S1 #5**.
2. **Where build teams are contract teams with MSA-mandated CMDB duties, the communication references the contractual duty**, not only the new process. Training alone does not change contractor behaviour.
3. **Coordinated with the D7 adoption campaign (1639308)**, whose Wave 2 sends in the same Sprint 4.6, so build teams do not receive two different CMDB messages from two workstreams.
4. OCM reviewed and signed off (Nora Lizenberg), recorded in writing.
5. **Delivered before or with the production deploy (S9)** — the flow becomes mandatory at deploy.
6. At least one asynchronous route (KB article or written walkthrough), so no team depends on attending a live session.
7. Distribution evidenced per team.

> **Not contract-gating.** Unlike D7, AP00288 D10 carries no rollout or training obligation — the deliverable is a configured flow exported as XML. This item underwrites the ADO "in use" criterion. If the schedule compresses, descope this in conversation with the PO ahead of S7 or S9.

---

### S9 · [User Story] Deploy server lifecycle capability to production

**Sprint 4.6** · Depends on S7, S8, DEP-10

**As** a CMDB data consumer, **I want** the approved lifecycle capability deployed to production, **so that** lifecycle management can be used operationally.

**Acceptance criteria**

1. Deployment plan approved and change request raised into a scheduled change window.
2. **Any PPL December/January change freeze confirmed before the window is assumed** — currently unconfirmed and it governs this release and four others (DEP-10).
3. **Deploy targeted early in 4.6 (week of Jan 6), not at sprint close.** A Jan 19 deploy leaves almost no in-use window before the S11 delivery notification is due.
4. Production migration completed with the S4 precedence configuration intact — **verified in production, not inferred from staging**.
5. Smoke testing successful: the first real build through the flow produces exactly one complete CI, within the Timeliness window.
6. **No Sev 1 or Sev 2 defects open** at close.
7. Monitoring established, with the specific condition being watched named — at minimum CIs stuck in the Build state and build-path creations that produced no CI.
8. Rollback position stated.

---

### S10 · [User Story] Transition lifecycle capability to operations

**Sprint 4.6** · Depends on S9

**As** an operations team member, **I need** documentation and support procedures, **so that** the lifecycle capability can be managed after the implementation team has rolled off.

**Acceptance criteria**

1. Support documentation published to an agreed, versioned location with a named content owner.
2. Operational procedures documented for the failure modes that actually occur: a CI stuck in Build, a build that produced no CI, a duplicate that slipped through, an attribute being overwritten by Discovery.
3. Knowledge transfer session completed and recorded.
4. **Ownership formally accepted by a named team with a named individual accountable** — not "operations" as an abstraction.
5. **Run-state monitoring from S9 #7 has an owner who will act on it**, identified by name.
6. Escalation path documented for issues the accepting team cannot resolve.

> **Why this matters here:** AP00288 ends **Feb 2, 2027**. Anything not formally accepted by an operating team before then has no owner afterwards.

---

### S11 · [Enabler – Process] Package D10 evidence and obtain acceptance

**Sprint 4.6 → 4.7 IP** · Depends on S9, S10, DEP-11

**As** the CMDB Product Owner, **I want** D10 submitted as a single evidenced package with written delivery notification, **so that** the three-business-day deemed-acceptance clock starts on a known date and closes before the Feb 2 contract end.

**Acceptance criteria**

1. **The contractual artifact is the XML export.** AP00288 lists D10's Format as XML — the configured process flow as an update set / configuration export. This is the primary submission.
2. Supporting evidence assembled: approved process flow and CCB sign-off (S3), configuration and precedence documentation (S4), validation and regression evidence (S7), communications and distribution evidence (S8), production change record (S9), operations acceptance (S10).
3. **"Live and in use" evidenced with actual records** — servers provisioned after go-live that went through the flow, with required attributes populated at creation, counted against the S1 #4 volume baseline. *This is the ADO acceptance criterion; AP00288 requires only that the flow be* configured*.*
4. **If volume in the window is too low to be meaningful, say so rather than pad it:** "every server provisioned after go-live followed the flow, n = x", with the small n disclosed.
5. **Written delivery notification issued on or before Jan 27, 2027**, so the three-business-day window closes before Feb 2. PPL reviewer availability confirmed in advance (DEP-11).
6. Submission date, recipient and response logged.
7. Any rejection or comment has a named remediation owner and a date inside the remaining window.
8. **Before-and-after stated against the benefit hypothesis:** the S1 #3 build-to-CI lag baseline versus the post-go-live measurement. This is the only evidence that the hypothesis was tested rather than asserted.

---

## What changed from the team set, and why

| Change | Reason |
|---|---|
| Added **S3** (CCB ratification) | `Operational Status` values are an open CCB decision and Ray Reuter must sign off the model. Monthly cadence on the critical path — invisible if folded into an AC reading "approved" |
| Added **S5** (create CI with attributes) | The original set identified and configured attributes but never populated one. This is the feature's central acceptance criterion |
| Added **S8** (build-team communications) | Story 6 handed over to *operations*; the people who must change how they work are the *build teams*. Different audience, different artifact |
| Added **S11** (evidence and acceptance) | Nothing in the original set submitted the deliverable. D10 is an XML export on a three-business-day deemed-acceptance clock |
| Folded **"Define Data Standards"** into S2 and S3 | It duplicated the modeling spike. S2 proposes, S3 ratifies and records |
| Folded **notifications** into S5 #8 | A full story would overlap D6 (1642240). As an AC with the overlap flagged, it stays visible without claiming scope |
| Kept **Story 6 → S10** | The strongest item in the original set and absent from the vault draft. The contract ends Feb 2; unaccepted capability has no owner after that |
| Kept **Story 4 → S7**, bounded | "Required adjustments implemented" was unbounded. Now deferrals are recorded, so the item can close |
| Rewrote every AC | The originals asserted an artifact existed. These name the condition that makes it correct, so DoR Gate 3 can be met |
| Scoped **S1** to the build path | The original covered retirement and maintenance, which are D11, D8 and D9. Shared coverage is allowed, but declared |
