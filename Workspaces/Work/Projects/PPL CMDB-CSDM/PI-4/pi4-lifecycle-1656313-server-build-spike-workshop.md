---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-4
ado: "1656313 — Server Build Lifecycle: Current State, Target Design and Class Manager Sign-off"
feature: "1640805 — Server Build Lifecycle Process Flow"
objective: "PI-4 Obj 4 (1639075) — Implement CMDB Lifecycle Management Process Flows"
sow: "AP00288 Deliverable 10"
gate: 2027-02-02
sprint: "4.2 (workshop) → 4.3 (hard stop Dec 8)"
status: draft
updated: 2026-10-20
tags: [work, cmdb-csdm, safe, pi-planning, servicenow, governance]
relationships:
  - target: "[[PI-4/pi4-lifecycle-1640805-ado-ready-items]]"
    type: derived_from
  - target: "[[PI-4/pi4-lifecycle-1640805-server-build-stories-dependencies]]"
    type: derived_from
  - target: "[[Backlog/definition-of-ready]]"
    type: related_to
---

# Spike 1656313 — Workshop-Led Rewrite

**Server Build Lifecycle: Current State, Target Design and Class Manager Sign-off**
Feature **1640805** · Objective **1639075** · AP00288 **D10** · 8 points

> **Status: DRAFT (2026-10-20).** Not yet applied to ADO. This rewrites the existing spike description and acceptance criteria to run the elicitation half as a single facilitated workshop, and to make the Thanksgiving calendar an explicit constraint rather than an assumption.
>
> The paste-ready text is in **§1**. What changed and why is in **§2**. The calendar analysis behind the dates is in **§3** — that section is for the PO and SM, not for ADO.

---

## §1 — Paste-ready ADO text

### Description

**PURPOSE**

Establish how servers are provisioned today, design the target flow, state model and Discovery coexistence, and obtain Class Manager sign-off — all inside one timebox, so that build can start in Sprint 4.4 with no governance debt behind it.

**QUESTIONS TO ANSWER**

1. How are servers provisioned today, by which teams and tooling, and at what point (if any) does a CMDB record appear?
2. What is the target flow and lifecycle state model, using out-of-the-box Operational Status values?
3. Which attributes can be populated at provisioning, and from what source?
4. How does build-time CI creation coexist with Discovery and SCCM without creating duplicates or having its values overwritten?
5. Is the solution configuration or customization?

**HOW THIS RUNS — THREE PHASES, ONE WORKSHOP**

The answers to questions 1–3 live in separate teams — physical build, vCenter, cloud, Hands & Feet, DBA — plus Discovery and the Class Manager. Elicited one conversation at a time, that is six to eight meeting requests with scheduling latency between each and contradictions resolved by email. The timebox does not hold that. It is therefore run as **one facilitated session against a straw-man design**, with analysis before and after it:

- **Phase 0 — Pre-work (Sprint 4.2).** Current ServiceNow configuration pulled, attendees confirmed, straw-man flow circulated. This phase gates the workshop; without it the session produces a transcript instead of decisions.
- **Phase 1 — Workshop (one session, ≤3 hours).** Build paths, target flow, attribute sources, timeliness window and build teams settled in the room, by the people with standing to settle them.
- **Phase 2 — Analysis (Sprint 4.3).** The work that cannot be done in a room: configuration-vs-customization, identification and reconciliation design, sizing of the downstream items.

The session is framed to PPL as a **design review of a proposed flow**, not a discovery session.

**TIMEBOX AND CALENDAR**

HARD STOP at the end of **Sprint 4.3 (Dec 8, 2026)**. If open at that point, escalate — do not extend.

Sprint 4.3 contains **8 working days**, and **week 1 contains exactly one** (Wed Nov 25; Nov 26–27 are the Thanksgiving holiday). No criterion in this spike may be scheduled to complete between **Nov 25 and Nov 27**.

The workshop is therefore held in **Sprint 4.2, on Nov 17 or Nov 18**, with **Nov 30 / Dec 1** as the fallback. Invitations must be issued by **Nov 6** — the day after PI Planning — for a cross-team session of this size to be seated.

**GOVERNANCE RUNS ALONGSIDE, NOT AFTER**

Ray Reuter attends the workshop as a **co-author of the state model**, not as a week-2 reviewer. Sign-off then confirms a design he helped produce rather than reviewing one handed to him. The sign-off criteria remain the exit gate, and they have a different owner from the analysis criteria. Raise the Class Manager dependency as a RAID item with a dated commitment **before** Sprint 4.3 opens — this spike no longer carries a separate board row for it.

**SCOPE NOTE**

Build lifecycle only.

**OUTPUT**

Current-State Assessment and Target Design Recommendation, signed off in writing by the Class Manager.

---

### Acceptance Criteria

**PHASE 0 — PRE-WORK (Sprint 4.2; gates the workshop)**

1. **Workshop seated by role, not by invitation list.** Each in-scope build path is represented by someone who performs it, plus Discovery (Stan Tomberg) and the Class Manager (Ray Reuter). A build path with no confirmed attendee by the invite deadline is **named and excluded in writing before the session**, not discovered as a hole during it.
2. **Current configuration pulled and circulated** — the `PPL Server` identification rule precedence, the reconciliation rules the Server class derives from Computer/Hardware with their SG-SCCM and ServiceNow priorities, and the OOB `Operational Status` values available on the class.
3. **Straw-man target flow circulated at least two business days before the session** — states, transitions, owner per step. The workshop reacts to a draft; it does not start from a blank page.

**PHASE 1 — WORKSHOP (one session, ≤3 hours)**

4. **Build paths enumerated** — physical, virtual (vCenter), cloud — each with its trigger and the tooling that performs it. Paths out of scope are **excluded by decision in the room**, by attendees with standing to exclude them, and recorded in writing.
5. **Target flow agreed** as states, transitions, trigger per transition and owner per step, using OOB `Operational Status` values, including which transitions are automatic, which require approval, and who owns each. Produced with visibility to Feature 1640819 so one state set serves decommission.
6. **Build-time attribute list fixed** — the three CCB-ratified attributes (Name, Serial Number, Operational Status) plus a decision on CI Owner and Support Group: how each is determined at provisioning, naming the source or responsible party rather than a placeholder group, or explicitly out of scope with the reason recorded. Any attribute requiring a data-dictionary change is logged and excluded from this feature.
7. **Timeliness window defined as a number**, anchored to provisioning.
8. **Teams performing builds named**, and identified as PPL staff or contract teams with MSA-mandated CMDB duties (Hands & Feet, DBA — Exhibits D/E/I/K).
9. **Decision log published within one business day.** Every question that leaves the room unanswered carries a named owner and a due date **on or before Dec 4** — inside the timebox, not at its edge. Without this the workshop converts into a second round of follow-up meetings and the timebox is lost anyway.

**PHASE 2 — ANALYSIS (Sprint 4.3; cannot be done in the room)**

10. **Configuration vs. customization determined.** If customization, the RAID issue is raised the same day and Sonika Das approval initiated.
11. **Identification designed against the serial-number gap.** A build-time CI usually has no serial. States what identifies the CI before a serial exists, and what happens when Discovery later supplies one — a named mechanism, not an assumption that IRE copes.
12. **Reconciliation precedence designed.** States whether the build process is registered as a discovery source, which attributes it is authoritative for, and which yield to Discovery. Reviewed with Stan Tomberg. Covers auditability — how a build event is traced back to the process that created the record.
13. **Downstream items sized** — configuration, CI creation and validation/deploy — each passing Definition of Ready gates 1–4, ready for Sprint 4.4 planning.

**EXIT GATE — CLASS MANAGER SIGN-OFF** *(owner: M. Vazquez)*

14. **Ray Reuter (CCB Class Manager, Servers and Storage CIs) participates in the workshop** as co-author of the state model, before the design is finished.
15. **Written sign-off dated on or before Dec 8**, covering the target flow, state model, transition rules and ownership model, **and confirming that no CMDB data-dictionary change is required for the scope as built**. Verbal agreement does not close this. If Ray or the CCB indicates a dictionary change *is* required, this is a **stop-and-escalate point**, not a criterion to work around.

---

## §2 — What changed, and why

| # | Change | Why |
|---|---|---|
| Structure | Flat 8-criterion list → four phases (Pre-work / Workshop / Analysis / Exit gate) | Makes visible which criteria depend on getting people in a room and which do not. The old list hid that distinction, so the scheduling risk had nowhere to show up |
| AC 1 | **New** — attendance by role, with a pre-session exclusion rule | A workshop missing a path owner produces a design hole that surfaces at CI-creation build time, when it is expensive. Forcing the exclusion *before* the session converts a hidden gap into a recorded scope decision |
| AC 2–3 | **New** — config pull and straw-man circulated ≥2 business days ahead | A blank-page session with nine attendees produces a transcript. This is the single highest-leverage change in the rewrite |
| AC 4 | Reworded — out-of-scope paths now **excluded by decision in the room** | Previously "named and excluded in writing" with no named decider. The people with standing to exclude a path are the ones attending |
| AC 5–8 | Substantively unchanged, relocated into the workshop phase | These are the elicitation criteria. Content is the same; the delivery mechanism is now stated |
| AC 9 | **New** — decision log with named owners and dates ≤ Dec 4 | The main failure mode of a workshop is that it spawns follow-ups. This closes it |
| AC 10 | Unchanged | — |
| AC 11–12 | **RESTORED** from the original A1 plan (identification / reconciliation precedence) | These are the two outputs the downstream configuration item cannot start without. See the note below |
| AC 13 | **RESTORED** — sizing of downstream items against Definition of Ready | A spike whose output does not let the next sprint plan has not met its purpose |
| AC 14 | Rewritten — "engaged in WEEK 1" → "participates in the workshop as co-author" | Week 1 of Sprint 4.3 is a single working day (Nov 25). The old criterion was not satisfiable as written. Co-authorship is also the stronger governance position |
| AC 15 | Merged — sign-off and the no-dictionary-change confirmation into one dated artifact; **stop-and-escalate language restored** | They are one written document. The escalation clause was in the original A2 plan and was lost when A2 folded into this spike |

**PO decision required on AC 11, 12 and 13.** The spike as it currently stands in ADO carries 8 criteria; the original A1 plan carried 12. The dropped ones were identification against the serial-number gap, reconciliation precedence, the build-to-CI lag baseline, and the build volume baseline. If the highlighted **"Build lifecycle only"** scope note was meant to exclude them, delete AC 11–13 and the rewrite still stands. **But the configuration item downstream cannot start without AC 11 and 12** — it has to know which attributes the build process is authoritative for and what identifies a CI with no serial. Dropping them does not remove the work; it moves it into the build sprint, unanalysed, with no slack behind it.

**Not restored:** the build-to-CI lag baseline and the build volume baseline. Both feed the "live and in use" evidence due in January rather than anything downstream in the build, and both can be gathered later without blocking. They should be picked up by the evidence/handover item instead — flagging so they are not simply lost.

---

## §3 — The Thanksgiving problem *(for the PO and SM — not for ADO)*

### What the calendar actually gives you

Sprint 4.3 runs Nov 25 – Dec 8, 2026.

| | |
|---|---|
| Wed **Nov 25** | Working day. Also the day Sprint 4.3 planning is scheduled. In practice a travel day — attendance at its lowest of the year |
| Thu **Nov 26** | Thanksgiving |
| Fri **Nov 27** | Company holiday |
| Mon Nov 30 – Fri Dec 4 | 5 working days |
| Mon Dec 7 – Tue Dec 8 | 2 working days |
| **Total** | **8 working days — and week 1 contains exactly one** |

Two consequences the current item does not account for:

**"Ray Reuter engaged in WEEK 1" means engaged on Nov 25.** One day, the worst attendance day of the year, which is also consumed by sprint planning. The criterion cannot be met as written. Anything deferred to "raise at Sprint 4.3 planning" lands on Nov 25 and then sits untouched until Nov 30.

**If the spike runs its full box, the configuration item does not start in Sprint 4.3 at all.** The plan assumed configuration begins in 4.3 week 2 and runs into 4.4. With Thanksgiving, week 2 is Nov 30 – Dec 4 and the spike is still open. Configuration therefore starts Dec 9 at the earliest, which pushes configuration, CI creation *and* validation-plus-deploy into the ten working days of Sprint 4.4, before a holiday shutdown with no slack behind it.

That second point is the real argument for the workshop, and for holding it early.

### Recommended dates

**Primary — workshop Tue Nov 17 or Wed Nov 18 (Sprint 4.2).** Clean week, no holiday, ahead of the travel week. This gives Ray roughly three weeks to produce written sign-off, landing comfortably inside the box, and it frees all 8 of Sprint 4.3's working days for Phase 2 analysis — which is where they are actually needed. The spike can then close around Dec 1–2 and configuration can start Dec 7, recovering most of what Thanksgiving takes away.

This requires the spike to **start in Sprint 4.2** rather than 4.3, with the hard stop still Dec 8. The spike needs no build capacity, and Sprint 4.2 carries only two feature starts. This is the same adjustment already recommended in [[PI-4/pi4-lifecycle-1640805-ado-ready-items]], now with a concrete date attached.

*Unverified:* whether PPL observes Veterans Day (Wed Nov 11). It does not affect Nov 17–18, but it does affect how much pre-work time Phase 0 really has. Worth confirming at PI Planning.

**Fallback — workshop Mon Nov 30 or Tue Dec 1.** Spike stays in Sprint 4.3. Cost: six working days remain after a Dec 1 session (Dec 1, 2, 3, 4, 7, 8) to produce the decision log, the customization determination, the identification and reconciliation designs with Stan, the sizing, *and* Ray's written sign-off. Sign-off alone typically does not turn around in six days. If this is the path, Ray's dated commitment must be secured **before Sprint 4.3 opens**, not requested during it.

### Decision ladder

| When | Check | Action |
|---|---|---|
| **Nov 4** (PI Planning) | Attendee list agreed and straw-man owner named | Both must be settled here. Issuing invites later than Nov 6 makes the primary date unreachable |
| **Nov 6** | Invitations issued for Nov 17–18 | — |
| **Nov 13** | Are the invitations accepted, with every build path covered? | If no — **switch to the fallback that day.** Do not wait to see whether acceptances arrive late |
| **Nov 25** (Sprint 4.3 planning) | Fallback session seated for Nov 30 / Dec 1, Ray's sign-off commitment dated | Raise the Class Manager dependency as a RAID item here with its date |
| **Dec 1** | Has the workshop happened? | If not, **escalate**. Do not extend the timebox — the downstream items have no slack and Sprint 4.5 is the holiday shutdown |

### Risk, stated for the register

**If the workshop cannot be seated before Dec 1, this spike cannot close inside its timebox, and the three downstream items compress into the ten working days of Sprint 4.4 ahead of a holiday shutdown.** Probability depends entirely on calendar lead time, which is controllable now and not controllable in three weeks. Response: settle the attendee list at PI Planning on Nov 4, issue invitations by Nov 6, and treat Nov 13 as a hard decision point rather than a status check.

The secondary risk is that moving the session into Sprint 4.2 is read as the spike starting early without a commitment. It is cleaner to move the spike's start to 4.2 explicitly at PI Planning than to run unaccounted pre-work against a 4.3 item.
