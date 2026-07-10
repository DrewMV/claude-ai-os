---
type: team-artifact
workspace: Work
project: CMDB-CSDM
updated: 2026-07-10
tags: [work, cmdb-csdm, backlog]
---

# Story A — Modify SR: Core (Attributes + Ownership Integrity)

*Foundation story for the Service Instance / Application Service modification flow. SOX handling is carved into [[service-instance-modify-storyB-sox|Story B]]. Target: end of PI-2 (8/4/2026).*

## User Story

**As a** Service or Application Owner,
**I want** to submit a Service Request to modify an existing Service Instance / Application Service CI (excluding SOX classification changes),
**So that** CMDB records stay accurate as ownership and attributes change over time — preserving data quality, audit readiness, reporting, lifecycle management, and reliable ownership data for downstream integrations, including future SailPoint / IAM access-approval processes.

## Acceptance Criteria

### Modification Service Request Exists
- Given an authorized user needs to change an existing Service Instance / Application Service
- When they access the Service Catalog / Employee Center
- Then a request item titled "Modify a Service Instance / Application Service" is available and can be submitted

### Select the CI to Modify
- Given a user opens the modification request
- When they identify the target
- Then they can search for and select an existing CI, and its current attribute values are pre-populated for editing

### Blank Ownership Prevented (Five Ownership Roles)
- Given a user is modifying the CI
- When they attempt to submit with any required ownership field cleared/blank
- Then submission is blocked with a clear inline validation message identifying the field(s)
- Required ownership fields (may be reassigned but not emptied): Owned By (Business Manager), CI Owner (IT Manager), Support Group, Technical Owner Group, Approval Group

### Owners Must Be Active Users or Groups
- Given ownership information is changed
- When the request is submitted
- Then the system validates: Owned By (active user), CI Owner (active user), Support Group / Technical Owner Group / Approval Group (exist and active)
- And inactive or invalid selections are rejected

### Editable Attributes Defined
- Given a user is modifying the CI
- When editing
- Then the request exposes the editable attributes below, required fields unable to be emptied:
  - Name (unique within the population)
  - Owned By, CI Owner, Support Group, Technical Owner Group, Approval Group
  - Business Unit / Value Stream, Metal Tier
  - Data Classification
  - Recovery Tier, Asset Criticality, RTO, RPO
  - SOX Indicator, SOX Type — **read-only in this story** (editing handled in Story B)
- Validation: Name uniqueness preserved on rename; required fields must remain populated; field validation messages displayed.

### SOX-Flagged CI Guardrail
- Given a selected CI has SOX Indicator = Yes
- When the user attempts to modify it
- Then the request is blocked with a message "Unable to modify the SOX Applications"

> **Note for later:** once [[service-instance-modify-storyB-sox|Story B]] ships, update this block message to direct the user to the governed SOX modification request.

### Baseline Approval Workflow — PENDING INPUT FROM JOE DAMES
- Baseline approval only (who approves, sequence, escalation). SOX-specific approval is out of scope here.
- Candidate approvers for Joe's consideration: Business Owner, CI Owner, Approval Group, CMDB Governance Team.

### CI Updated and Traceable on Fulfillment
- Given the request has completed its baseline approval
- When it is fulfilled
- Then the CI is updated with approved values, traceable to the originating request
- And ownership, support, classification, and resiliency information is retained
- And the CI remains available for reporting, certification, governance, audit, and downstream integrations

### Submitter Notified of Outcome
- Given a request has been fulfilled or rejected
- When processing is complete
- Then the submitter receives an automated notification including: Request Number, Request Status, Approval/Rejection Outcome, Updated CI Number, Link to the CI record

## Out of Scope

- SOX change handling and editing of SOX classification → [[service-instance-modify-storyB-sox|Story B]]
- Automated offboarding reassignment (separate story — confirm with JP)
- C-level / VIP hierarchy stop-level → separate SNOW Enhancements story
- Creation and Retirement / Decommission SRs → separate stories
- Bulk / discovery-driven updates
- NERC CIP change handling → parked/deferred

## Terminology Note (CSDM 5 / Yokohama)

Per the CSDM 5 white paper, **Application Service** was renamed to **Service Instance** (Application Service is now a type of Service Instance). This story uses "Service Instance / Application Service" until the exact class/table in PPL's instance is confirmed. Verify with Stan Tomberg against PPL's CSDM version before build.

## Relationship to Story B

Story A keeps SOX Indicator/Type **read-only** (Editable Attributes) and **blocks** modification of SOX-flagged CIs (SOX-Flagged CI Guardrail, Option a). [[service-instance-modify-storyB-sox|Story B]] is the governed path that enables exactly those modifications, applying either an approval or an informational notification (pending governance decision). What Story A blocks, Story B governs — no interim gap.
