---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-4
feature: "1640805 — Server Build Lifecycle Process Flow"
objective: "PI-4 Obj 4 (1639075) — Implement CMDB Lifecycle Management Process Flows"
sow: "AP00288 Deliverable 10"
gate: 2027-02-02
sprint: "4.2 (requirements) → 4.6 (release)"
status: draft
updated: 2026-10-16
tags: [work, cmdb-csdm, safe, pi-planning, servicenow, governance]
relationships:
  - target: "[[PI-4/pi-planning]]"
    type: derived_from
  - target: "[[PI-4/pi4-implementation-plan-appendix]]"
    type: derived_from
  - target: "[[Backlog/feature-story-templates]]"
    type: derived_from
  - target: "[[Backlog/feature-implementation-structure]]"
    type: related_to
  - target: "[[Config-Mgmt-Plan/ci-class-ire-reconciliation-config]]"
    type: related_to
  - target: "[[Config-Mgmt-Plan/data-dictionary-ccb-decision-sheet]]"
    type: related_to
  - target: "[[PI-4/pi4-adoption-1639308-campaign-stories-dependencies]]"
    type: related_to
  - target: "[[PI-4/Memory]]"
    type: related_to
---

# Feature 1640805 — Stories & Dependencies (Draft)

**Server Build Lifecycle Process Flow**
Objective 4 (**1639075**) · AP00288 **D10** · Requirements Sprint 4.2 (Nov 11) → Release 4.6 · Gate **Feb 2, 2027** · Owner: M. Vazquez

> **Status: DRAFT (2026-10-16)** — no stories exist in ADO yet. Per [[Backlog/definition-of-ready]], create every item from the Feature "+" link, never standalone.

> **Use [[PI-4/pi4-lifecycle-1640805-ado-ready-items]] as the creation list.** That file merges this draft with the team's own decomposition into 11 ADO-ready items (S1–S11) and supersedes the SB-numbered items below for the purpose of raising work in ADO. **This file remains the reasoning record** — the contract reconciliation, the dependency table (DEP-1…DEP-11) and the risk register are here and are referenced from there by number.

> **Objective ID note:** the parent objective was given as "16390" — the full ADO ID per the Oct 8 official list is **1639075** (*Implement CMDB Lifecycle Management Process Flows*, AP00288 §3.4). Confirm before creating items, since the "+" link has to come off the right parent.

Applies **Template B — Lifecycle process flow** from [[Backlog/feature-story-templates]] (3 requirements items · 5 build · 3 promote), adapted to what this feature actually runs into.

---

## What AP00288 actually requires for D10

Verbatim from the SOW (unsigned draft, Table 2 — Deliverables, p. 9–10):

> **10. CMDB Lifecycle Management — Server Build Lifecycle Process Flow**
> *"A CMDB process flow is configured to manage the build lifecycle for the server CI class, enabling new servers to be accurately reflected in the CMDB upon provisioning"*
> **Format:** XML · **Targeted Completion Date:** February 2, 2027

Scope section §3.4 adds only: *"Leverage CMDB process flows to manage lifecycle events and enable updates to the CMDB."* There is no further D10 detail in the contract.

**The ADO feature's acceptance criteria are stricter than the contract in three places.** This is not a defect — a higher internal bar is defensible — but it should be a deliberate PO choice, because all three sit on the critical path:

| # | ADO acceptance criterion | AP00288 D10 | Effect |
|---|---|---|---|
| 1 | "New server CIs created with **mandatory attributes populated** at build time" | "new servers **accurately reflected** in the CMDB upon provisioning" | The contract does not require an extended mandatory-attribute set. A correct CI with the three CCB-mandatory attributes and the right state plausibly satisfies "accurately reflected." |
| 2 | "Process flow **documented and approved**" | Deliverable **Format: XML** | The contractual artifact is a configuration export (update set), not an approved process document. The documented-and-approved flow is an internal bar. |
| 3 | "**Live and in use** by Feb 2, 2027" | "A CMDB process flow **is configured**" | The contract bar is *configured*, evidenced by the XML. "In use" requires adoption evidence the contract does not ask for. |

**What this changes:** the CCB data-dictionary extension (below) is required to satisfy the **ADO acceptance criteria as written**, not to satisfy AP00288. That gives the PO a legitimate fallback if the CCB defers — align the ADO AC to the contract language rather than slip the gate. It also materially lowers the exposure on the short "in use" evidence window (Risk 5).

Note also that D10, unlike D7, **carries no contractual rollout or training obligation**. SB-9 remains the right thing to do under Template B and is needed for "in use", but it is not gate-blocking for the contract.

**Role note:** AP00288 §12 makes the **Business Process Consultant** responsible for leading current-state process assessment, defining process control points, and translating process requirements into ServiceNow user stories. That is the named contractual home for SB-1 and SB-2 — useful when filling the Owner fields below.

---

## Four things to settle at the feature level first

**1. "Mandatory attributes populated at build time" is not defined, and the obvious reading contradicts the CCB data dictionary.**

The CCB ratified the Server data dictionary on **July 21, 2026**. It makes exactly three attributes mandatory on `cmdb_ci_server` — **Name, Serial Number, Operational Status** — and names **ServiceNow Discovery** as the source for all three ([[Config-Mgmt-Plan/data-dictionary-ccb-decision-sheet]]). Discovery cannot run before the server exists. So the feature's benefit hypothesis resolves one of two ways:

| Reading | Consequence |
|---|---|
| Build-time population means the existing three mandatory attributes | Discovery already supplies them once the host is up. The flow delivers process, not data completeness — the benefit hypothesis is not met. |
| Build-time population means **more** than the three | The additional attributes have to be added to the mandatory set, which is a **CCB data-dictionary change** with CCB lead time — not something a process flow story can decide. |

The feature's own dependency list points at the second reading: *"confirmed ownership/support-group assignment process for new servers."* **CI Owner (`managed_by`) and Support Group are not mandatory on `cmdb_ci_server` today.** SB-2 names the attribute list; SB-3 takes it to the CCB. Treat this as the feature's defining scope question, not a detail.

**The contract gives this a floor.** AP00288 asks only that new servers be *"accurately reflected in the CMDB upon provisioning"* — it does not name an attribute set. So the second reading is an **ADO-AC obligation, not a contract obligation**. If the CCB defers the data-dictionary change, D10 can still be delivered against the contract language; what gets renegotiated is the ADO acceptance criterion, not the Feb 2 gate. SB-3 #4 is where that call gets made and recorded.

**2. The build process is not a registered discovery source, so anything it writes can be silently overwritten.**

Per [[Config-Mgmt-Plan/ci-class-ire-reconciliation-config]], the Server class has **zero reconciliation rules created directly on it** — all five are *derived* from the Computer/Hardware hierarchy, including **SG-SCCM at priority 90 and 100** and **ServiceNow at 80, 100 and 200**. A record created by a new build flow has no precedence standing at all. On the next Discovery or SCCM sync, build-time values are liable to be overwritten by a source that ranks above a process that has no rank.

This is the "attribute flapping" theme already recorded in [[Workspaces/Work/Memory]] under *Authoritative source conflicts*. It is a design input to SB-4, not a defect to find in test.

**3. Duplicate-CI risk has a specific mechanism, and the acceptance criteria depend on closing it.**

The `PPL Server` identification rule is Independent with three identifier entries: **Serial number (100) · Serial number via lookup (200) · Name (300)**. A server CI created at build time typically has **no serial number yet** — the hardware is not racked, or the VM has no serial assigned. It therefore matches on Name at priority 300, or not at all. When Discovery later arrives carrying the serial, IRE can reasonably create a second record. AC #3 ("no duplicate CI creation where discovery and the build process overlap") is a function of this, and it is answered in SB-2/SB-4 or it is not answered.

Existing precedent to build on, not duplicate: **Feature 1356826 / stories 1403759, 1403760, 1403762, 1403763** (SCCM Server Class precedence, in Validation, Sonika's approval gate cleared).

**4. The state model belongs to this feature *and* to 1640819 — define it once, here.**

`Operational Status` allowed values are an **open CCB decision** (decision sheet row 13: *Build / Operational / Non-Operational / Retired — confirm full list vs OOB choices*). No "Build" state is ratified. 1640805 needs the front of that lifecycle; **1640819 Server Decommission (D11)** needs the back of it, and starts one sprint later with **0 days of gate margin** ([[PI-4/pi4-implementation-plan-appendix]]). If each feature defines states independently, the second one reopens the first one's ruling. SB-2 and SB-3 cover the **whole** server lifecycle state set, and 1640819 consumes that output rather than re-deciding it.

---

## Phasing

| Phase | Sprint | Items | Why here |
|-------|--------|-------|----------|
| Requirements | 4.2 (Nov 11–24) | SB-1, SB-2, SB-3 | Nothing can be built until the attribute set, the state model, and the Discovery coexistence design are settled — and SB-3 has CCB lead time |
| Build & test | 4.3–4.4 (Nov 25 – Dec 22) | SB-4, SB-5, SB-6, SB-7, SB-8 | The whole build window; Sprint 4.5 is holiday dead time |
| Promote | 4.6 (Jan 6–19) | SB-9, SB-10, SB-11 | PROD early in 4.6 so "in use" evidence can accumulate before the Feb 2 gate |

**Critical path:** SB-2 → SB-3 → SB-4 → SB-5 → SB-10 → SB-11. **SB-3 is the long pole** — it is CCB calendar time, not team capacity.

**Sprint 4.5 (Dec 23 – Jan 5) carries no work by design.** Build closes Dec 22; validation resumes Jan 6. Do not plan a release into it.

> ⚠ **Sprint discrepancy to resolve before PI Planning.** [[PI-4/pi-planning]] shows 1640805 starting in **Sprint 4.3 (Nov 25)**; the newer [[PI-4/pi4-implementation-plan-appendix]] (Oct 14) puts requirements in **4.2 (Nov 11–24)** after Sprint 4.5 displacement. This draft follows the appendix. If 4.3 is correct, the requirements phase lands inside the build window and SB-3's CCB lead time has nowhere to go. **Note that 4.2 contains Thanksgiving week** — a two-week requirements window is effectively shorter.

---

## Stories (11)

---

### SB-1 · [Spike] Current-state server build process and CMDB touchpoints

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Spike |
| Parent feature | 1640805 |
| Sprint | 4.2 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | DEP-1, DEP-8 |
| Tags | `CMDB-Lifecycle` `PI4-Obj4` `D10` |

**As** the CMDB Product Owner,
**I want** the server build process as it runs today mapped end to end, with every point the CMDB is touched (or isn't) identified by name,
**so that** the target flow attaches to the process PPL actually runs rather than replacing a process nobody has written down.

**Acceptance criteria:**

1. Build paths enumerated and mapped **separately where they differ** — physical server, virtual (vCenter), and cloud/Azure — with the trigger that starts each one named.
2. For each path: who requests, who approves, who executes, what tooling performs the build, and what record (if any) is created in ServiceNow, at what point.
3. **The teams that actually perform builds are named**, including whether they are PPL staff or contract teams with MSA-mandated CMDB duties (Hands & Feet, DBA — Exhibits D/E/I/K). This determines whether SB-9 is training or contract-duty enforcement.
4. Current CMDB entry point for a new server is stated factually: today a server CI appears when **Discovery or SCCM finds it**, not when it is built. The lag between physical build and CI appearance is **measured, not estimated** — this is the baseline for the Timeliness NFR and for the benefit hypothesis.
5. **Build volume baselined** — servers built per month over a recent representative period, split by path. Feeds the "in use" evidence question in SB-11 (see Risk 5).
6. Existing adjacent work identified so it is reused, not rebuilt: SCCM/Discovery server precedence (**1356826 / 1403759–1403763**), credential work (**1444864**), and server support-group assignment (Ray Reuter — DEP-1).
7. Output is a single referenceable artifact in the vault, cited by SB-2.

**Dependencies:** DEP-1 (Ray Reuter), DEP-8 (build team identification).

---

### SB-2 · [Spike] Target-state flow, CI state model, build-time attribute set, and Discovery coexistence

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Spike |
| Parent feature | 1640805 |
| Sprint | 4.2 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | SB-1, DEP-2, DEP-3, DEP-6 |
| Tags | `CMDB-Lifecycle` `PI4-Obj4` `D10` |

**As** the CMDB Product Owner,
**I want** the target build flow designed as a state model plus a named attribute set plus an explicit answer on how it coexists with Discovery and SCCM,
**so that** build stories can be written against a design that will survive contact with the identification and reconciliation engine.

**Acceptance criteria:**

1. **Target flow documented** as states, transitions, trigger per transition, and owner per step — covering every build path SB-1 found, or stating which paths are out of scope and why.
   **Class scope stated explicitly.** AP00288 says *"the server CI class"*; the CCB data dictionary covers the **parent `cmdb_ci_server` class only** — Windows/Linux child classes and the Hardware Type custom attribute were out of scope on July 21. State whether the flow applies at parent or child level, and whether Azure/cloud server CIs are in scope given they sit under a different Class Manager (Mark Smith).
2. **Lifecycle state set proposed for the full server lifecycle, not just build.** Covers `Operational Status` allowed values (decision-sheet row 13 — *Build / Operational / Non-Operational / Retired* vs OOB choices) and the relationship to `install_status` / Life Cycle Stage where PPL uses both. **Produced jointly with 1640819 (D11)** so one model serves build and decommission (DEP-6).
3. **Build-time mandatory attribute list named explicitly**, each entry marked:
   - *already CCB-mandatory* (Name, Serial Number, Operational Status), or
   - *proposed addition* — with the source that can populate it at build time and the named party accountable for it.
   Candidates to assess and explicitly include or exclude with a reason: **CI Owner (`managed_by`) · Support Group · Technical Owner Group (`managed_by_group`) · Location · Environment · Operational Status**.
4. **Any proposed addition is flagged as a CCB data-dictionary change** and routed to SB-3. Terminology follows [[Config-Mgmt-Plan/cmdb-csdm-attribute-schema]] and the PPL UI labels, noting that *"CI Owner" = `managed_by`* and *"Technical Owner Group" = `managed_by_group`* remains an **open CCB item** (DEP-3).
5. **Serial-number gap addressed for identification.** States what identifies a build-time CI before a serial exists, and what happens when Discovery later arrives with the serial — against the live `PPL Server` rule (Serial 100 · Serial lookup 200 · Name 300). A stated mechanism for preventing a second record, not an assumption that IRE handles it.
6. **Reconciliation precedence designed.** States how build-time values survive the derived SG-SCCM (90, 100) and ServiceNow (80, 100, 200) rules: whether the build process is registered as a discovery source, which attributes it is authoritative for, and which it must yield to Discovery. Reviewed with **Stan Tomberg** (DEP-2).
7. **Timeliness window defined as a number**, anchored to **provisioning** — the contract's own trigger word is *"accurately reflected in the CMDB upon provisioning"*, so the window is measured from the provisioning event, not from a request or a rack date. States the maximum compliant interval (NFR: *"CI creation within a defined window"*) and is measurable against SB-1 #4.
8. **Auditability mechanism named** — how a build event is traced to the process that created the record (discovery source value, audit history, request reference), so the NFR is testable.
9. **Configuration vs. customization determined** per [[requirements-process#Customization Governance]]. A flow with triggers and automation is very likely customization: if so, the **"Customization" tag, a linked RAID issue, and Sonika Das's approval start now, in 4.2** — not at build (DEP-5).
10. Build stories listed and sized, each passing [[Backlog/definition-of-ready]] gates 1–4.

**Dependencies:** SB-1, DEP-2 (Stan Tomberg / Discovery), DEP-3 (CI Owner label ruling), DEP-6 (joint state model with 1640819).

---

### SB-3 · [Enabler – Process] CCB ratification — server lifecycle states and build-time mandatory attributes

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Enabler – Process |
| Parent feature | 1640805 |
| Sprint | 4.2 |
| Owner | M. Vazquez |
| Points | TBD |
| State | Draft |
| Depends on | SB-2, DEP-1, DEP-4 |
| Tags | `CMDB-Lifecycle` `governance` `PI4-Obj4` `D10` |

**As** the CMDB Product Owner,
**I want** the state model and any mandatory-attribute additions ratified by the Class Manager and the CCB before build starts,
**so that** the flow is not built against values and obligations the governance body has not agreed to.

**Acceptance criteria:**

1. **Ray Reuter (Class Manager — Servers and Storage CIs) signs off the target flow and state model in writing** — not verbally. This is Template B's long pole and an external dependency, not team capacity.
2. **`Operational Status` allowed values ruled on by the CCB** and recorded against decision-sheet row 13, which is currently open. A "Build" (or equivalent) state must exist in the ratified list, or SB-4 has no state to configure.
3. **Any attribute proposed for addition to the mandatory set is submitted as an explicit data-dictionary change** with the CCB ruling recorded (Accept / Amend / Defer) — chaired by **Josh Sterling** (DEP-4).
4. **A deferral or rejection is treated as a scope answer, not a blocker.** If the CCB declines to extend the mandatory set, the feature's acceptance criteria are renegotiated with the PO *in 4.2* against what the flow can actually deliver (see Feature-level item 1), and the change is recorded against the ADO AC.
5. Ruling is reflected back into [[Config-Mgmt-Plan/data-dictionary-ccb-decision-sheet]] and the Configuration Management Plan.
6. CCB meeting date confirmed and the submission lodged against it — the cadence is monthly, so a missed agenda costs a sprint.

**Dependencies:** SB-2 (nothing to ratify without it), DEP-1 (Ray Reuter), DEP-4 (CCB agenda slot).

---

### SB-4 · [Enabler – Configuration] Lifecycle states, discovery source registration, and reconciliation precedence

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Enabler – Configuration |
| Parent feature | 1640805 |
| Sprint | 4.3 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | SB-3, DEP-2 |
| Tags | `CMDB-Lifecycle` `PI4-Obj4` `D10` |

**As** a CMDB administrator,
**I want** the ratified lifecycle states configured and the build process given a defined precedence standing against Discovery and SCCM,
**so that** build-time data is not overwritten on the next sync and no second CI is created when Discovery finds the host.

**Acceptance criteria:**

1. Ratified `Operational Status` values (SB-3 #2) configured on the Server class, with the "Build" state available for the flow.
2. **Build process registered so its writes have a defined precedence** per the SB-2 #6 design — discovery source and/or reconciliation rule created, with the attributes the build process is authoritative for stated explicitly.
3. **Server-class reconciliation is no longer purely derived for the attributes in scope** — the gap identified in Feature-level item 2 is closed for the build-time attribute set, or an explicit decision is recorded that a given attribute yields to Discovery.
4. **Identification behaviour verified against the serial-number gap** — a CI created without a serial, then matched when Discovery supplies one, resolves to **one record**. Verified in a sub-production environment before SB-5 builds on it.
5. Existing SCCM server precedence configuration (**1356826 / 1403759–1403763**) is **extended, not contradicted** — confirmed with Stan Tomberg (DEP-2).
6. Configuration documented so the precedence model is readable by someone who did not build it.
7. Customization governance applied where configuration crosses into custom logic (DEP-5).

**Dependencies:** SB-3 (ratified states), DEP-2 (Discovery owner review).

---

### SB-5 · [User Story] Build-time CI creation with mandatory attributes populated

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1640805 |
| Sprint | 4.3 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | SB-4, DEP-1 |
| Tags | `CMDB-Lifecycle` `PI4-Obj4` `D10` |

**As** a server build engineer,
**I want** a server CI created with its required attributes at the point I build the server,
**so that** the record is complete when the server goes live instead of being corrected weeks later by a data-quality cleanup.

**Acceptance criteria:**

1. A server CI is created at build time with **every attribute on the SB-3-ratified build-time mandatory list** populated — the list, not a subset.
2. **Ownership and support-group assignment is populated through the agreed process**, not left blank or defaulted to a placeholder group (Ray Reuter — DEP-1). A blank owner at build time reproduces the gap this feature exists to close.
3. The entry point matches what SB-1 found: **integrated into the existing build tooling/trigger where one exists**, and only built as a new catalog item or interface where it does not. Aligns with existing server onboarding rather than creating a second creation path (NFR: Integration).
4. **No duplicate CI is created** where the build path and Discovery/SCCM overlap — verified behaviour, resting on SB-4 #4.
5. **CI creation occurs within the defined Timeliness window** (SB-2 #7), measurable from the record.
6. **The created record is traceable to the build process** that created it (SB-2 #8) — discovery source or request reference visible on the CI (NFR: Auditability).
7. Required fields are enforced at creation rather than requested — a build cannot complete its CMDB step with a mandatory attribute empty.
8. Tested per [[Backlog/definition-of-done]]; staging deploy plus PO demo.

**Dependencies:** SB-4, DEP-1 (support-group assignment process).

---

### SB-6 · [User Story] State transitions and handoff from build to operational

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1640805 |
| Sprint | 4.4 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | SB-5 |
| Tags | `CMDB-Lifecycle` `PI4-Obj4` `D10` |

**As** a server build engineer,
**I want** the CI to move through its lifecycle states automatically as the build progresses and completes,
**so that** the CMDB reflects where the server actually is without anyone maintaining status by hand.

**Acceptance criteria:**

1. Each transition in the SB-3 state model fires on its defined trigger; no transition depends on a human remembering to set a field.
2. **Handoff to Discovery is explicit** — when Discovery first finds the host, the CI moves from the build state to operational per the agreed rule, and build-time attributes are retained per the SB-4 precedence model.
3. A build that is cancelled or abandoned leaves the CI in a defined state — not stranded in "Build" indefinitely, which would seed the stale-CI problem the retirement monitoring work (**1639335 / D8**) is separately trying to solve.
4. Transition history is auditable on the record.
5. Tested against each build path in scope from SB-1.
6. Tested per [[Backlog/definition-of-done]]; staging deploy plus PO demo.

**Dependencies:** SB-5.

---

### SB-7 · [User Story] Notifications and approvals for the build flow

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1640805 |
| Sprint | 4.4 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | SB-6, DEP-7 |
| Tags | `CMDB-Lifecycle` `PI4-Obj4` `D10` |

**As** a server support group owner,
**I want** to be notified when a server is assigned to my group and to approve where the process requires it,
**so that** ownership is accepted by a real person rather than assigned to a group that does not know it owns the CI.

**Acceptance criteria:**

1. Notification recipients and triggers defined per the SB-2 flow — at minimum the assigned support group and CI Owner on assignment.
2. Approval steps configured only where the SB-2 flow requires them. **Approvals are not added speculatively** — each one is a delay in a flow whose Timeliness NFR is a defined window.
3. **Overlap with 1642240 (Automated Stakeholder Notifications, D6, gate Dec 31) resolved explicitly** — this story either consumes D6's notification framework or states why it needs its own (DEP-7). Two notification mechanisms for CMDB events is a defect, not a feature.
4. Notification content states what the recipient must do, not just that something happened.
5. Tested per [[Backlog/definition-of-done]]; staging deploy plus PO demo.

**Dependencies:** SB-6, DEP-7 (D6 notification framework).

---

### SB-8 · [Enabler – Test] Validate against representative server builds, including duplicate and overwrite regression

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Enabler – Test |
| Parent feature | 1640805 |
| Sprint | 4.4 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | SB-5, SB-6, SB-7 |
| Tags | `CMDB-Lifecycle` `PI4-Obj4` `D10` |

**As** the CMDB Product Owner,
**I want** the flow validated against real representative builds before it goes near PROD,
**so that** the duplicate-CI and attribute-overwrite failure modes are proven closed rather than assumed closed.

**Acceptance criteria:**

1. Validated against **at least one real build per in-scope path** from SB-1 (physical, virtual, cloud as applicable) — not a single synthetic record.
2. **Duplicate regression test:** CI created at build time without a serial, Discovery subsequently supplies the serial → exactly one CI. Executed, evidenced.
3. **Overwrite regression test:** build-time attribute values survive a full Discovery and SCCM sync cycle, per the SB-4 precedence model. Executed, evidenced.
4. **Timeliness measured** against the SB-2 #7 window on the test builds, and compared against the SB-1 #4 baseline.
5. Mandatory-attribute completeness verified on every test record — the acceptance criterion is *populated*, not *prompted for*.
6. Evidence captured in a form that goes straight into the SB-11 package. Testing sits inside the stories per [[Backlog/feature-implementation-structure]]; this item exists for the cross-path regression work that no single build story owns.

**Dependencies:** SB-5, SB-6, SB-7.

---

### SB-9 · [User Story] OCM — communications and training for the teams that build servers

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | User Story |
| Parent feature | 1640805 |
| Sprint | 4.6 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | SB-8, DEP-8, DEP-9 |
| Tags | `CMDB-Lifecycle` `OCM` `PI4-Obj4` `D10` |

**As** a server build engineer,
**I want** to be told what the new CMDB step in my build process is and how to do it, before it becomes mandatory,
**so that** I follow the new flow rather than working around it.

**Acceptance criteria:**

1. Materials produced for **every team SB-1 #3 identified as performing builds**, including contract teams where applicable.
2. **Where build teams are contract teams with MSA-mandated CMDB duties, the communication references the contractual duty**, not just the new process. Training alone does not change contractor behaviour; the obligation does (DEP-8, Risk 8).
3. **Coordinated with the D7 adoption campaign (1639308)** so server build teams do not receive two different CMDB messages from two workstreams in the same window — D7's Wave 2 sends in the same Sprint 4.6 ([[PI-4/pi4-adoption-1639308-campaign-stories-dependencies]], DEP-9).
4. OCM reviewed and signed off (Nora Lizenberg), recorded in writing.
5. Delivered **before or with the PROD deploy (SB-10)**, not after — the flow becomes mandatory at deploy.
6. At least one asynchronous route (KB article or written walkthrough) so no team depends on attending a live session.
7. Distribution evidenced per team — supporting evidence for the ADO "in use" criterion.

> **Not contract-gating.** Unlike D7, AP00288 D10 carries no rollout or training obligation — the deliverable is a configured flow exported as XML. This story exists because Template B requires it and because the ADO AC says "in use", which adoption underwrites. If the schedule compresses, this is the item to descope in conversation with the PO — ahead of SB-8 or SB-10.

**Dependencies:** SB-8, DEP-8 (build teams named), DEP-9 (OCM + D7 coordination).

---

### SB-10 · [Enabler – Process] Change request and PROD deploy

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Enabler – Process |
| Parent feature | 1640805 |
| Sprint | 4.6 |
| Owner | TBD |
| Points | TBD |
| State | Draft |
| Depends on | SB-8, SB-9, DEP-10 |
| Tags | `CMDB-Lifecycle` `PI4-Obj4` `D10` |

**As** the CMDB Product Owner,
**I want** the flow deployed to PROD early in Sprint 4.6,
**so that** real server builds run through it for long enough to evidence "live and in use" before the Feb 2 gate.

**Acceptance criteria:**

1. Change request raised and scheduled into a change window (DEP-10).
2. **Deploy targeted early in 4.6 (week of Jan 6), not at sprint close.** A Jan 19 deploy leaves almost no in-use window before the delivery notification is due (Risk 5).
3. **Any PPL December/January change freeze confirmed** before the window is assumed — flagged as unconfirmed in [[PI-4/pi4-implementation-plan-appendix]] (DEP-10).
4. Deployed to PROD with the SB-4 precedence configuration intact — verified in PROD, not inferred from staging.
5. Post-deploy verification that the first real build through the flow produces one complete CI.
6. Rollback position stated.

**Dependencies:** SB-8, SB-9, DEP-10 (change window / freeze).

---

### SB-11 · [Enabler – Process] D10 evidence package, "in use" evidence, and acceptance

| Field | Value |
|-------|-------|
| ADO ID | *(not yet created)* |
| Type | Enabler – Process |
| Parent feature | 1640805 |
| Sprint | 4.6 → 4.7 IP |
| Owner | M. Vazquez |
| Points | TBD |
| State | Draft |
| Depends on | SB-10, DEP-11 |
| Tags | `CMDB-Lifecycle` `governance` `PI4-Obj4` `D10` |

**As** the CMDB Product Owner,
**I want** D10 submitted as a single evidenced package with written delivery notification,
**so that** the three-business-day deemed-acceptance clock starts on a known date and closes before the Feb 2 contract end.

**Acceptance criteria:**

1. **The contractual artifact is the XML export.** AP00288 lists D10's Format as **XML** — the configured process flow exported as an update set / configuration export. This is the primary submission; everything below supports it.
2. Supporting evidence set assembled: approved process flow and CCB sign-off (SB-3), CCB ruling on states and attributes (SB-3), configuration and precedence documentation (SB-4), regression evidence for duplicates and overwrites (SB-8), OCM materials and distribution evidence (SB-9), PROD change record (SB-10).
3. **"Live and in use" evidenced with actual records** — servers built after go-live that went through the flow, with their mandatory attributes populated at creation, reported as a count against the SB-1 #5 volume baseline. *This is the ADO acceptance criterion, not the contract's: AP00288 requires the flow to be* configured*.*
4. **If build volume in the window is too low to be meaningful, that is stated honestly** rather than padded: the evidence becomes "every server built after go-live followed the flow, n = x", with the small n disclosed. Do not overclaim adoption on a six-business-day window.
5. **Written delivery notification issued on or before Jan 27, 2027** so the three-business-day acceptance window closes before Feb 2. PPL reviewer availability confirmed in advance for that window.
6. Submission date, recipient, and response logged.
7. Any PPL comment or rejection has a named remediation owner and a date inside the remaining window.
8. **Before-and-after stated against the benefit hypothesis:** the SB-1 #4 build-to-CI lag baseline versus the post-go-live measurement. This is the only evidence that the hypothesis was tested rather than asserted.

**Dependencies:** SB-10, DEP-11 (PPL reviewer availability).

---

## Dependencies

| # | Description | Depends on | Needed by | Status |
|---|-------------|-----------|-----------|--------|
| DEP-1 | **Server support-group and ownership assignment process** — Ray Reuter is both the Class Manager (Servers and Storage CIs) and the standing contact for server support-group assignments, with a prior P1 story on the topic. The flow cannot populate an owner it has no process to derive. | Ray Reuter | SB-1, SB-3, SB-5 | Open |
| DEP-2 | **Discovery and reconciliation design review** — the build process needs a precedence standing against derived SG-SCCM and ServiceNow rules. Must not contradict the existing SCCM server precedence work (1356826 / 1403759–1403763). | Stan Tomberg | SB-2 (4.2), SB-4 | Open |
| DEP-3 | **CI Owner / `managed_by` label ruling** — PPL labels `managed_by` as "CI Owner", conflicting with CSDM 5.0's `owned_by`/`managed_by` split. Open CCB item. Building a flow that writes a contested field means rework if the ruling moves. | CCB | SB-2 (4.2) | **Open — flagged** |
| DEP-4 | **CCB agenda slot and ruling** on `Operational Status` allowed values (decision-sheet row 13) plus any mandatory-attribute additions. Monthly cadence — a missed agenda costs a sprint, and the whole build phase sits behind it. | Josh Sterling (Chair) / CCB | SB-3 (4.2) | **Open — critical path** |
| DEP-5 | **Customization approval** — a flow with triggers and automation is almost certainly customization, requiring the "Customization" tag, a linked RAID issue, and Sonika Das's approval **before implementation**. Lead time must start in 4.2. | Sonika Das / RAID log | SB-2 call, before SB-4 build | Open |
| DEP-6 | **Joint state model with 1640819 (Server Decommission, D11)** — D11 starts one sprint later with **0 days of gate margin**. One lifecycle state model must serve both; if D11 re-decides states, D10's CCB ruling reopens. | Feature 1640819 / PO | SB-2, SB-3 (4.2) | **Open — sequencing decision** |
| DEP-7 | **1642240 (Automated Stakeholder Notifications, D6, gate Dec 31)** — decide whether this flow consumes D6's notification framework or builds its own. | Feature 1642240 / PO | SB-7 (4.4) | Open |
| DEP-8 | **Identification of the teams that actually build servers**, and whether they are PPL staff or contract teams with MSA-mandated CMDB duties (Exhibits D/E/I/K). Determines whether SB-9 is training or contract-duty enforcement. | SB-1 / PO | SB-1 (4.2), SB-9 | Open |
| DEP-9 | **OCM capacity and D7 coordination** — Nora Lizenberg is OCM Support; the D7 adoption campaign (1639308) sends its Wave 2 in the same Sprint 4.6 to overlapping audiences. | Nora Lizenberg / 1639308 owner | SB-9 (4.6) | Open |
| DEP-10 | **Change window, and confirmation of any PPL December/January change freeze.** A freeze is flagged as unconfirmed in the implementation-plan appendix and would move the deploy — and with it the entire in-use evidence window. | Change management (Kostas) / CAB | SB-10 (4.6) | **Open — unconfirmed** |
| DEP-11 | **PPL reviewer availability for the Jan 27 – Feb 2 acceptance window**, which runs into the contract end date. | PPL / PO | SB-11 | Open |

---

## Risks specific to this feature

| # | Risk | Impact | Mitigation |
|---|------|--------|------------|
| 1 | **The benefit hypothesis may be unachievable as written.** The three CCB-mandatory server attributes are all Discovery-sourced; populating them "at build time" either adds nothing or requires a CCB data-dictionary change. **Scoped to the ADO AC, not the contract** — AP00288 asks only for servers "accurately reflected upon provisioning". | Medium | SB-2 #3 names the attribute list; SB-3 #4 renegotiates the ADO acceptance criteria in 4.2 if the CCB declines, with the contract language as the floor |
| 2 | **Build-time data gets overwritten by Discovery/SCCM.** The Server class has no reconciliation rules of its own — all five are derived from Computer/Hardware, with SG-SCCM at 90/100. A process with no precedence loses. | **High** | SB-2 #6 designs it, SB-4 #2 configures it, SB-8 #3 proves it with a regression test |
| 3 | **Duplicate CIs at serial-number arrival.** A build-time CI has no serial; the `PPL Server` rule matches serial at 100/200 and name only at 300. Discovery arriving with a serial can create a second record — which is explicitly an acceptance criterion. | **High** | SB-2 #5, SB-4 #4, SB-8 #2 |
| 4 | **CCB lead time sits on the critical path.** `Operational Status` values are unratified, the CCB meets monthly, and the entire build phase depends on the ruling. | **High** | SB-3 submitted against a confirmed agenda date in 4.2; DEP-4 tracked as critical path |
| 5 | **"In use" has roughly six business days of evidence window.** PROD in 4.6 (closes Jan 19), delivery notification due ~Jan 27 for the three-business-day clock to close before Feb 2. Few builds may occur in that window. **Contract exposure is limited** — AP00288 requires the flow to be *configured* and submitted as XML, so this threatens the ADO acceptance criterion rather than the gate. | Medium | SB-1 #5 baselines build volume; SB-10 #2 deploys early in 4.6; SB-11 #4 reports small n honestly rather than overclaiming |
| 6 | **1640819 rework.** If D11 defines its own states in 4.3/4.4, D10's ratified model reopens — and D11 has 0 days of margin to absorb it. | Medium | DEP-6 — one joint state model produced in SB-2, ratified once in SB-3 |
| 7 | **Customization/RAID lead time discovered at build.** Flow automation is customization; approval is a prerequisite to implementation, not a parallel task. | Medium | SB-2 #9 makes the call in 4.2 and starts the RAID path immediately |
| 8 | **Build teams may be contractors, so training does not enforce.** If builds are performed by Hands & Feet or DBA teams under MSA Exhibits D/E/I/K, behaviour change runs through contractual duty, not a KB article. | Medium | SB-1 #3 identifies them; SB-9 #2 references the contractual duty |
| 9 | **Sprint 4.5 (Dec 23 – Jan 5) splits build from validation.** Build closes Dec 22; nothing resumes until Jan 6. Context and momentum are lost across the holiday, and any build defect found in 4.6 has no slack behind it. | Medium | Phasing puts all build in 4.3–4.4 with SB-8 regression inside 4.4, not deferred into 4.6 |
| 10 | **A December/January change freeze would move the PROD deploy** and compress or eliminate the in-use window. Currently unconfirmed. | Medium | DEP-10 — confirm the freeze before committing the 4.6 release at PI Planning |
| 11 | **Requirements window ambiguity.** pi-planning says 4.3; the appendix says 4.2. If 4.3 is right, SB-3's CCB lead time has nowhere to sit. 4.2 also contains Thanksgiving week. | Medium | Resolve before PI Planning (Nov 4); see the phasing note |

---

## Open questions for refinement

1. **Which reading of "mandatory attributes populated at build time" does the PO intend** — the existing three CCB-mandatory attributes, or an extended set? Everything downstream scales off this answer, and it is the one question that cannot be deferred past Sprint 4.2.
2. **Does the team keep the stricter ADO acceptance criteria, or align them to AP00288?** The contract asks for a flow *configured* and delivered as XML, with servers *"accurately reflected upon provisioning"*. The ADO AC adds a documented-and-approved flow, a populated mandatory-attribute set, and "live and in use". Keeping the higher bar is defensible and has audit value; it should be an explicit PO decision rather than an inherited assumption, because all three additions sit on the critical path.
3. **A mandatory-attribute extension is outside D10's contract scope** — confirmed against the SOW. Does it therefore run on the CMP/CCB governance track with its own timeline, and if so, does D10 ship without it?
4. **DEP-6** — are the D10 and D11 state models being produced jointly? If not, who owns the single server lifecycle state model, and when is it ratified?
5. **DEP-7** — does the build flow consume D6's notification framework (1642240) or build its own?
6. **Who performs server builds today**, and are any of them contract teams with MSA-mandated CMDB duties? This is the difference between an OCM story and a contract-compliance conversation.
7. **Is there a December/January change freeze?** Still unconfirmed and it governs the release window for this feature and four others.
8. **Does the team have the Discovery/IRE capability available in 4.2** for the SB-2 precedence design, given Stan Tomberg's load across Network Gear and Service Mapping?
9. **Template gap:** [[Backlog/feature-story-templates]] Template B has no reconciliation/precedence item, while Template A does (A-S3). This feature writes to a class Discovery owns, so it needs one. Should Template B inherit A-S3 for any flow that creates or updates discoverable CIs — which includes 1640819?
10. **Structure inconsistency:** [[Backlog/feature-implementation-structure]] says *"exactly one spike per feature"*; Template B lists three requirements-stage items, and the D7 precedent ([[PI-4/pi4-adoption-1639308-campaign-stories-dependencies]]) uses two spikes plus an enabler. This draft follows Template B. Worth settling before the convention is adopted at PI Planning.
