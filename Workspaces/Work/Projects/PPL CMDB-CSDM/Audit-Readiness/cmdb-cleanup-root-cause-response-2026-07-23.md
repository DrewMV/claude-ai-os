---
workspace: Work
tags: [work, cmdb-csdm, servicenow]
updated: 2026-07-23
status: draft
---

> **DRAFT, for review before sending.** Audience: Sonika first, then broader key stakeholders. Purpose: a root-cause and remediation summary for leadership, and a response to the concerns raised in Sonika's email thread ("RE: Issues...SNOW CMDB").
>
> **Open items before sending:**
> - Record count: currently stated as "all qualifying records." Insert the actual count from the query result if you want it shown.
> - Remediation (Concerns #6/#8): now framed as a governed CMDB Health and retirement lifecycle policy (see Governance & Go-Forward Controls). Requirements still need to be defined with stakeholders and approved by the CCB before development.

# ServiceNow CMDB: Computer & Server Record Cleanup
### Root Cause, Impact, and Response to Concerns Raised

## Executive Summary

We ran a one-time cleanup to retire Computer and Server records that were loaded into the CMDB from legacy sources as an initial starting point, before ServiceNow Discovery scope was finalized. Concerns were then raised that active operational assets may have been caught in that cleanup, with risk to data integrity, operations, governance, and compliance.

The main cause is a gap between what the CMDB actually covers today and how broadly its coverage is understood. Discovery is intentionally limited to specific subnets. Many subnets, including those hosting OT, SCADA, and NERC-related devices, are out of scope and are not discovered or maintained in the CMDB. The cleanup removed unvalidated pre-scope import records, not live discovered assets.

Every retirement is **fully reversible**. Retired records are not deleted, so any record later confirmed as a legitimate in-scope asset can be restored immediately with no data loss. Going forward, a governed CMDB Health and lifecycle policy, defined with stakeholder input and approved by the CCB, will gate all future retirements (see Governance & Go-Forward Controls). The current focus is a stable, in-scope CMDB baseline.

## What Occurred

- A single, one-time query identified and retired the qualifying records. This was **not an automated or recurring process** writing to the CMDB on a schedule.
- The criteria: records not already Retired whose Discovery Source was a legacy or manual origin (ImportSet, iTeam, Manual Entry, CherWell KY, CherWell PA, or empty).
- All records meeting the criteria were retired, across both the Computer and Server classes.
- The action was **reviewed with key stakeholders in advance**. The CMDB team did not do this unilaterally.

## Root Cause

The initial CMDB loads were bulk collections of records from existing sources, imported as a starting point before Discovery scope was finalized. Because scope was not yet defined, these records were **never validated for scope** when they entered the CMDB. They are not maintained by any authoritative discovery source, and many sit outside the subnets the CMDB is scoped to manage.

The concern that active operational assets were retired comes largely from that same scope gap. The CMDB covers a narrower slice of the environment today than most people assume.

## Scope Clarification

- ServiceNow Discovery is scoped to specific, prescribed subnets.
- Multiple subnets are **intentionally out of scope**, including subnets that host OT, SCADA, and NERC-related devices. By design, those assets are not discovered and not maintained in the CMDB.
- Retirement logic based on the absence of active discovery does not act on those out-of-scope operational assets, because they are not in the discovered inventory in the first place.
- **NERC CIP is currently out of scope** for this CMDB effort. A separate, parallel initiative is evaluating NERC-specific solutions.

## Response to the Concerns Raised

| # | Concern | Response |
|---|---------|----------|
| 1 | Active CIs automatically retired | Done by a **one-time script**, not an automated or recurring rule. Reviewed with key stakeholders beforehand, not unilaterally. |
| 2 | Potential widespread / undiscovered impact | Retired records were unvalidated pre-scope imports, not authoritatively discovered assets. No affected record has been identified as a legitimate in-scope asset. Any that turns out to be one is **restored immediately**, since retirement is reversible. |
| 3 | Communication / stakeholder awareness | The cleanup was reviewed with key stakeholders. Communication is deliberately staged: key stakeholders now to stabilize the baseline, then operational teams as the baseline is confirmed. |
| 4 | Operational risk (monitoring alerts) | Where a retired record was still referenced downstream, discrepancies could surface. Restoring the record resolves them, and **over 40 records found this way have already been restored**. These cases also help confirm which records belong in the validated baseline. |
| 5 | OT / SCADA / CIP assets are different | Agreed, and this is central. Those assets sit on **out-of-scope subnets**, are not discovered, and are not maintained in the CMDB. The cleanup targeted pre-scope import records, not live OT assets. OT and CIP are handled by a parallel effort. |
| 6 | Insufficient retirement controls | Agreed. We are establishing a governed **CMDB Health and lifecycle policy**: staleness-based candidate identification, automated stakeholder notification, an explicit approval step, and advance notice before implementation (see Governance & Go-Forward Controls). Requirements will be defined with stakeholder input and **approved by the CCB** before any development. |
| 7 | Compliance / NERC CIP | **NERC CIP is out of scope today**, and the CMDB is not its system of record. A parallel initiative owns NERC-specific solutions and will define governance for any future regulated data. |
| 8 | Root cause & remediation | Root cause: unvalidated pre-scope legacy imports, plus a CMDB scope narrower than people assumed. Remediation: the governed CMDB Health retirement policy (see Governance & Go-Forward Controls). In the meantime, **full reversibility** (40+ already restored) and staged communication protect the move toward a validated baseline. |

## Safeguards & Reversibility

- Retired does not mean deleted. Every retired record is **fully recoverable**, and any legitimate in-scope asset can be restored on request. We have already done this in practice: **over 40 records restored to date**.
- The cleanup was a one-time baseline action, not a standing automated rule.
- Future retirements will run through the governed CMDB Health and lifecycle policy below, not ad-hoc scripts.

## Governance & Go-Forward Controls

So this stays a one-time event and not a recurring risk, we are establishing a governed **CMDB Health and lifecycle policy** for identifying and retiring CIs. It puts every future retirement through a controlled, approval-gated workflow that leaves an audit trail:

1. **Candidate identification (CMDB Health).** Retirement candidates come from defined CMDB Health criteria, mainly staleness (CIs not updated or confirmed by an authoritative source within a set threshold) and related data-quality checks. The criteria will explicitly account for legitimately non-discoverable in-scope assets such as OT and SCADA, so that lack of discovery alone never triggers retirement.
2. **Automated stakeholder notification.** When a CI meets the criteria, an automated workflow notifies the affected stakeholders and owners. No silent state changes.
3. **Explicit approval step.** Retirement does not proceed without explicit approval from the responsible stakeholders and SMEs, keeping them in the lifecycle decision.
4. **Advance notice before implementation.** Once approved, advance notice goes out before the change is made, giving downstream and operational teams time to complete their own decommissioning steps and avoid monitoring surprises.

**Governance authority:** These policy requirements will be defined with stakeholder input and formally approved by the Change Control Board (CCB) before any development or implementation.

**Process compliance:** The policy will comply with all existing change, configuration management, and governance processes.

> **Lifecycle at a glance:** Identify (CMDB Health criteria) → Notify (automated) → Approve (explicit) → Advance notice → Implement.

## Next Steps

1. Define the CMDB Health and retirement lifecycle policy with stakeholder input (staleness criteria, automated notification, explicit approval, advance notice) and **submit it to the CCB for approval before development**.
2. Keep restoring any record identified as a legitimate in-scope asset (40+ done so far).
3. Keep stabilizing the in-scope CMDB baseline, and widen communication as it firms up.
