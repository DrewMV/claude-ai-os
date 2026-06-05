---
title: Configuration Control Board Charter
category: concepts
workspace: Work
project: nerc-cip
tags: [nerc-cip, cip-010, change-management, governance, ccb, cab, authorization]
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  The CCB Charter defines the cross-functional body (OT+IT+Security) that authorizes changes
  to BES Cyber Systems. Its meeting minutes are required NERC CIP audit evidence.
provenance:
  extracted: 0.65
  inferred: 0.30
  ambiguous: 0.05
base_confidence: 0.75
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# Configuration Control Board Charter

## What It Is

A Configuration Control Board (CCB) Charter — also called a Change Advisory Board (CAB) Charter — is the governance document that establishes the body responsible for reviewing and authorizing changes to BES Cyber Systems. It defines membership, authority, process, and documentation requirements.

For NERC CIP purposes, the CCB is the organizational mechanism that satisfies [[CIP-010 Configuration Change Management]] R1.2: "authorize and document changes that deviate from the existing baseline configuration."

> **Terminology note**: NERC CIP literature uses "Change Advisory Board" (CAB); ITSM tradition uses "Change Advisory Board" for IT and "Configuration Control Board" for configuration baselines. For utilities, these functions are often combined. The charter should name the body and define its scope unambiguously.

## Why a Charter Is Required

NERC auditors do not just want to see that changes were documented — they want evidence of a *repeatable, organizational process* with accountable humans. A charter provides:
- Named individuals (or roles) with defined approval authority
- Criteria that determine when CCB review is required
- A record of deliberation (meeting minutes) showing the process was followed
- An emergency path that does not bypass accountability

Without a charter, the "authorization process" is informal and cannot be consistently demonstrated across audit cycles.

## Required Charter Elements

### 1. Purpose and Authority
- What the CCB is authorized to do (approve, reject, defer changes to BES Cyber Systems)
- Which systems are in scope (reference [[CIP-002 BES Cyber System Categorization]] inventory)
- Relationship to the [[Configuration Management Plan for NERC CIP]] (the CMP defines the baseline; the CCB authorizes deviations)

### 2. Membership
Cross-functional composition required by CIP-010 R1.4 (control impact analysis requires multiple domain perspectives):
- **OT Engineering** — owns BES Cyber System operational context
- **IT/Cybersecurity** — assesses CIP-005 and CIP-007 control impacts
- **Compliance** — ensures CIP documentation requirements are met
- **Operations** — assesses reliability impact of proposed changes
- **Executive Sponsor** — escalation path for high-risk or contested changes

Quorum requirements and decision-making rules should be defined.

### 3. Change Authorization Criteria

| Change Category | CCB Requirement |
|---|---|
| **High-risk** (affects ESP boundary, OS upgrade, major software change) | Full CCB review and vote required before implementation |
| **Medium-risk** (patch application, port changes, config parameter change) | Abbreviated review; 2+ CCB members must approve |
| **Low-risk** (pre-approved change type with no baseline impact) | Expedited approval; post-implementation CCB notification |
| **Emergency change** (immediate threat to BES reliability or security) | Verbal/email approval from designated CCB authority; full documentation within 7 days |

### 4. Change Request Requirements

Each change request submitted to the CCB must include:
- Description of proposed change and affected BES Cyber Systems
- Justification (operational, security, or compliance driver)
- Impact analysis: which CIP-005 and CIP-007 controls are affected
- Implementation plan with rollback/contingency
- Proposed implementation window
- Testing and verification approach
- Requester identity and authorization level

### 5. Meeting Cadence and Minutes Requirements

- Regular CCB meeting cadence (e.g., weekly or bi-weekly for normal changes)
- Emergency sessions as needed
- **Minutes must capture**: attendees, changes reviewed, decisions (approved/rejected/deferred), rationale, and dissenting views
- Minutes are retained as NERC CIP audit evidence for minimum 3 years

### 6. Post-Implementation Review
- Confirmation that approved change was implemented as documented
- Verification that affected controls still function as required
- CMDB baseline updated to reflect the new authorized configuration

### 7. Document Control
- Charter owner (typically Compliance Manager or CISO)
- Annual review cycle
- Version history

## CIP Requirement Traceability

| Charter Element | CIP-010 Requirement |
|---|---|
| Change authorization criteria | R1.2 — only authorized changes |
| Baseline definition reference | R1.1 — maintains current baseline |
| Documentation standards | R1.3 — change records |
| Membership (OT+IT+Security) | R1.4 — control impact analysis |
| Emergency change procedure | R1.5 |
| Meeting minutes retention | Evidence requirements |
| Scope (High/Medium BCS) | CIP-002 categorization |
| ESP boundary review | CIP-005 (EACMS in scope) |

## ServiceNow Integration

The CCB process can be implemented natively in ServiceNow:
- **Change Requests** in the Change Management module serve as change tickets with approval workflows
- **Approval groups** map to CCB membership; approval rules enforce quorum requirements
- **Change Advisory Board Workbench** (ServiceNow feature) surfaces pending changes for CCB review
- **CAB meeting records** in ServiceNow document the deliberation and decision
- All records are linked to the relevant CMDB CIs, creating an end-to-end audit trail from baseline → change request → CCB approval → implementation → updated baseline

## Relationship to CMP

The [[Configuration Management Plan for NERC CIP]] defines the what (baseline components, documentation standards, monitoring cadence). The CCB Charter defines the *who* and *how* of authorization. They are companion documents that should cross-reference each other.
