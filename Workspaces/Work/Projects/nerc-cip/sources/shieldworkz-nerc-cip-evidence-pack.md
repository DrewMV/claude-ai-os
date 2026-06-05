---
title: Shieldworkz — NERC CIP Evidence Pack for SCADA Change Management
category: references
workspace: Work
project: nerc-cip
tags: [nerc-cip, cip-010, change-management, cab, audit-evidence, scada]
sources:
  - "https://shieldworkz.com/blogs/nerc-cip-evidence-pack-how-to-document-scada-patch-change-management-for-audits"
source_url: "https://shieldworkz.com/blogs/nerc-cip-evidence-pack-how-to-document-scada-patch-change-management-for-audits"
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  Practical guide to NERC CIP audit evidence for SCADA change management. Defines 
  CAB structure, change request contents, required documentation, and audit trail requirements.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.80
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# Shieldworkz — NERC CIP Evidence Pack

**URL**: https://shieldworkz.com/blogs/nerc-cip-evidence-pack-how-to-document-scada-patch-change-management-for-audits

## What It Covers

Practical audit preparation guide for NERC CIP change management evidence. Most useful source found for the CAB/CCB governance body structure and what NERC auditors actually expect in documentation.

## Key Claims

**Change Advisory Board (CAB) structure:**
- "A cross-functional team including OT, IT, and security stakeholders"
- Reviews proposed changes, debates feasibility, formally authorizes modifications
- Produces "approval workflow records" with clear audit trails

**Required records for NERC CIP change management:**
1. Baseline configuration documents ("gold standard" configurations, version-controlled)
2. CMDB — centralized tracking of all CIs, attributes, and relationships
3. Change request forms — proposed change, justification, impact, rollback plan, implementation date, verification procedures
4. **CAB meeting minutes** — records of cross-functional reviews and decisions
5. Implementation plans — step-by-step execution instructions
6. Work orders/tickets — who performed work, when, any issues
7. System logs/audit trails — exact commands or changes made
8. Post-change verification reports
9. Configuration audit reports — comparisons to approved baselines

**Change request must document:**
- Proposed change details
- Justification
- Potential operational impact analysis
- Rollback/contingency plan
- Requested implementation date
- Pre-implementation checks
- Post-implementation verification procedures
- Issues encountered

**Auditable evidence must demonstrate:**
- All BES Cyber System configurations identified
- Approval mechanisms for all changes
- Complete documentation of each modification
- Verification that changes were authorized and properly implemented
- Detection capability for unauthorized changes

## Concepts Informed

- [[Configuration Control Board Charter]]
- [[Configuration Management Plan for NERC CIP]]
- [[CIP-010 Configuration Change Management]]
- [[CMDB as NERC CIP Asset Registry]]
