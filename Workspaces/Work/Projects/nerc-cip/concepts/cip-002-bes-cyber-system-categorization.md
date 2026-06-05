---
title: CIP-002 BES Cyber System Categorization
category: concepts
workspace: Work
project: nerc-cip
tags: [nerc-cip, cip-002, asset-inventory, bes-cyber-system, categorization, cmdb]
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  CIP-002 requires identification and High/Medium/Low impact categorization of BES Cyber Systems
  and Assets, with a 15-month review cycle. CMDB is the natural system of record.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.88
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# CIP-002: BES Cyber System Categorization

## Purpose

CIP-002 is the foundational NERC CIP standard: before any security control can be applied, a utility must know *what* it has and *how important it is*. It requires identifying all BES Cyber Assets and grouping them into BES Cyber Systems, then categorizing each system by impact level.

## Key Definitions

**BES Cyber Asset**: A cyber asset that if rendered unavailable, degraded, or misused would, within **15 minutes** of its required operation, adversely impact the reliable operation of the Bulk Electric System.

**BES Cyber System**: One or more BES Cyber Assets logically grouped by a responsible entity to perform one or more reliability tasks.

**Supporting Systems** (also require inventory):
- **EACMS** — Electronic Access Control or Monitoring Systems (authentication/access control)
- **PACS** — Physical Access Control Systems (building/facility security)
- **PCA** — Protected Cyber Assets (ancillary equipment in the same security zone as BES Cyber Systems)

## Impact Categorization

| Level | Criteria |
|---|---|
| **High** | Control center systems overseeing energy balancing, transmission, or generation across multiple assets |
| **Medium** | Single facilities significantly affecting grid reliability; generation > 15,000 MW capacity |
| **Low** | All other BES Cyber Systems not meeting High/Medium thresholds |

Categorization follows "bright-line criteria" in CIP-002 Attachment 1. Low impact systems must still be identified but have significantly reduced control obligations.

## Inventory Maintenance Requirements

- The impact inventory and categorization must be **reviewed and updated every 15 months**
- Every categorization decision must be documented with justification
- Static spreadsheets are explicitly inadequate for audit purposes — a dynamic, maintainable registry is expected

## CMDB as the Authoritative Registry

The CMDB is the natural implementation for CIP-002 compliance:

- Each BES Cyber Asset is a CI with attributes for function, location, and connectivity
- BES Cyber Systems are CI groups or service mappings
- Impact category (High/Medium/Low) is a CI attribute
- EACMS, PACS, and PCA are separate CI classes linked by relationship to BES Cyber Systems
- 15-month review can be enforced via scheduled CMDB data certification policies

### CSDM Role

The [[CSDM OT Domain]] provides the service model layer that connects physical OT CIs to BES functions. By mapping OT System Services (e.g., energy management, SCADA control) to underlying CIs, CSDM enables defensible impact assessment: if this CI fails, which BES functions are affected within 15 minutes?

## Relationship to Other CIP Standards

CIP-002 scope defines which systems CIP-003 through CIP-015 apply to:
- High/Medium impact systems are subject to [[CIP-010 Configuration Change Management]] (R1–R4)
- High impact systems have additional obligations under CIP-006 (physical security) and CIP-008 (incident response)
- All BES Cyber System Information (BCSI) is subject to [[CIP-011 Information Protection]]

## Common Gaps

- Failing to identify EACMS and PACS that support BES Cyber Systems
- Not updating inventory when new assets are added between 15-month reviews
- Categorizing systems based on function alone without documenting the 15-minute impact rationale
- Treating the CMDB as supplemental rather than authoritative
