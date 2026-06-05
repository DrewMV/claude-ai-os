---
title: Data Certification Program
type: concept
workspace: Work
project: ServiceNow
tags: [work, cmdb, data-quality, governance, certification, process]
created: 2026-06-05
updated: 2026-06-05
summary: "CI Data Certification pilot program at PPL — structure, pilot group approach, implementation planning, and support model for ongoing CI owner certification."
base_confidence: 0.90
lifecycle: draft
lifecycle_changed: 2026-06-05
provenance: "Derived from PI2 ADO backlog reviewed June 2026 (Objective 1420082)."
---

# CI Data Certification Program

**Priority 1 objective in PI2.** Goal: establish a repeatable process by which CI owners certify their configuration items are accurate, complete, and up to date.

## Program Structure

### Feature 1: Functionality (Feature 1247179)
Core certification functionality built and piloted in Sprint 2.2.
- Story 1435307: CMDB Data Certification Pilot changes — Active in Sprint 2.2

### Feature 2: Implementation Planning (Feature 1402958)
- Story 1402976: Execute Initial Data Certification Policies — **no iteration assigned; needs scheduling**
- Story 1402962: Facilitate Kick-Off/Training Meeting with pilot group of CI Owners — Sprint 2.3

### Feature 3: Implementation Support (Feature 1402979)
All three support stories assigned to Sprint 2.3 but missing start/end dates:
- Story 1402984: Hold Office Hours to support questions/address issues
- Story 1402980: Monitor Data Certification Completeness Progress
- Story 1402985: Process Feedback

## Pilot Approach

- A defined pilot group of CI Owners is onboarded first before broader rollout
- Kick-off/training meeting (Story 1402962) triggers active certification window
- Office hours model provides direct support during the pilot period
- Progress monitoring and feedback loop built into the support phase

## Open Planning Gaps

| Gap | Risk |
|-----|------|
| Story 1402976 has no iteration | Initial policies may not be defined before training begins |
| Support stories (2.3) have no dates | Capacity unclear; may conflict with heavy NowAssist sprint load |
| Pilot group confirmation not documented | Training meeting cannot be scheduled without a confirmed attendee list |

## Governance Connection

CI certification policies directly support:
- CMDB Health Score (linked to [[nowassist-for-cmdb]] Phase 1 baseline)
- NERC-CIP 15-month asset review cadence (see [[CMDB as NERC CIP Asset Registry]])
- SOX team notification workflow (Story 1455827, Feature 1371672 — currently unplanned)

## Related Pages

- [[cmdb-governance-roadmap]] — overall governance roadmap this program supports
- [[nowassist-for-cmdb]] — NowAssist governance advice features that build on certification data
