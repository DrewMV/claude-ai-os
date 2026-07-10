---
type: team-artifact
workspace: Work
project: CMDB-CSDM
updated: 2026-07-10
tags: [work, cmdb-csdm, backlog]
---

# Story B — Modify SR: SOX-Flagged CI Handling (Governed)

*Depends on [[service-instance-modify-storyA-core|Story A]]. Target: early PI-3 (8/5/2026).*

## User Story

**As a** SOX / Compliance stakeholder (with the Service/Application Owner submitting the change),
**I want** a governed path to modify SOX-flagged Service Instances / Application Services — and to set or change SOX classification — with the appropriate approval or notification applied,
**So that** changes to SOX-relevant services keep their audit and compliance integrity, and the SOX team has the appropriate control or visibility.

## Context — Relationship to Story A

[[service-instance-modify-storyA-core|Story A]] **blocks** modification of SOX-flagged CIs (guardrail, Option a) and keeps SOX Indicator/Type read-only, directing users here. **Story B is that flow** — it enables those modifications with SOX handling applied. What Story A blocks, Story B governs — no interim gap.

## Acceptance Criteria

### Enable Governed Modification of SOX-Flagged CIs
- Given a CI has SOX Indicator = Yes (blocked in Story A)
- When a user modifies it through this governed flow
- Then the modification is permitted and the SOX handling below is applied
- And the SOX Indicator / SOX Type fields become editable here (lifting Story A's read-only restriction), also subject to the SOX handling below

### When This Governed Flow Applies
- This flow governs a modification when either:
  - the target CI has **SOX Indicator = Yes**, or
  - the change **sets or alters SOX Indicator / SOX Type** (flagging a CI as SOX-relevant, or changing its SOX type)

### SOX Handling — Governance selects Option A or B (Decision #2)

**Option A — Requires Approval**
- Given a governed SOX modification is submitted
- When it reaches the SOX governance step
- Then the change is routed to the SOX team for approval before fulfillment
- And the change is not applied to the CI until approved (hard approval gate)
- And the SOX team may approve, reject, or request correction

**Option B — Notification Only**
- Given a governed SOX modification is submitted
- When the change is fulfilled
- Then the SOX team receives an informational notification only — no approval gate — and the change proceeds
- (Aligns with the meeting-notes direction: SOX = informational, not approval)

### SOX Payload (Both Options)
- Sent to the SOX team (Pepa, POC): CI Name, Business Unit / Value Stream, Owned By, CI Owner, Request Number, SOX Indicator, SOX Type (if applicable), Link to the CI record

## Decisions Needed (block this story)

| # | Decision | Owner |
|---|----------|-------|
| 2 | SOX handling: Option A (approval) vs Option B (notification-only) | Joe / Compliance |
| 3 | Governance scope: does *every* change to a SOX-flagged CI get the SOX handling, or only ownership + SOX-classification changes (other attributes flow through lighter)? | Joe / Pepa |

> **Note:** Choosing Story A / Option a (block) reframed Decision #3. It used to be "which ownership role change triggers the notification" — but since Story A now blocks all changes to SOX CIs and routes them here, the real question is how broadly Story B governs those changes.
>
> Option A also runs against the meeting-notes direction (which discussed *replacing* SOX approvals with notifications). Option B is the "as-discussed" path.

## Out of Scope

- Everything in [[service-instance-modify-storyA-core|Story A]] (core modify of non-SOX CIs)
- NERC CIP change handling → parked/deferred

## Dependencies

| # | Dependency | Owner | Status |
|---|-----------|-------|--------|
| 1 | Story A delivered | CMDB team | Sequential prerequisite |
| 2 | Decision #2 (Option A vs B) | Joe / Compliance | Pending |
| 3 | Decision #3 (governance scope) | Joe / Pepa | Pending |
| 4 | SOX team recipient / approver list | Pepa (POC) | Pending |

## Terminology Note (CSDM 5 / Yokohama)

**Application Service** was renamed to **Service Instance** (Application Service now a type of Service Instance). Confirm PPL's exact class/table with Stan Tomberg before build.

## Definition of Ready — Status

**Not Ready** — blocked on Decisions #2 & #3, the SOX recipient/approver list, and Story A delivery. Cannot be sized or tested until Option A/B and the governance scope are set.
