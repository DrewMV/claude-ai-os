---
title: Configuration Management Plan for NERC CIP
category: concepts
workspace: Work
project: nerc-cip
tags: [nerc-cip, cip-010, configuration-management, governance, compliance, documentation]
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  A CMP for NERC CIP is the procedural document that defines how CIP-010 obligations are
  met: baselines, authorization chain, monitoring cadence, and evidence retention.
provenance:
  extracted: 0.70
  inferred: 0.28
  ambiguous: 0.02
base_confidence: 0.78
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# Configuration Management Plan for NERC CIP

## What It Is

A Configuration Management Plan (CMP) is the organizational procedure document that defines how configuration management is performed for BES Cyber Systems. It is the primary implementation evidence for [[CIP-010 Configuration Change Management]] R1 and R2, and it scopes which systems and assets are governed.

NERC does not prescribe a specific CMP format — it requires "documented processes" that collectively satisfy each requirement part. A CMP consolidates those processes into a single auditable artifact.

## Why It Matters for NERC CIP

Without a CMP, an organization has isolated procedures but no unified governance framework. Auditors want to see:
1. That a defined process exists *before* changes are made
2. That the process is followed consistently (evidence)
3. That the process covers all applicable BES Cyber Systems

A well-structured CMP also enables the [[Configuration Control Board Charter]] to function: it defines what the CCB is authorizing changes *against* (the baseline) and what documentation the CCB must produce.

## Recommended CMP Sections and CIP Mappings

| CMP Section | Content | CIP Requirement |
|---|---|---|
| **1. Purpose and Scope** | Which BES Cyber Systems are covered (High/Medium/Low); reference to CIP-002 asset inventory | CIP-002 |
| **2. Roles and Responsibilities** | Who owns configuration records, who can request changes, who approves, who implements | CIP-010 R1.2 |
| **3. Baseline Configuration** | What constitutes a baseline (OS, firmware, software, ports, patches); how baselines are established and approved | CIP-010 R1.1 |
| **4. Change Authorization Process** | How a change request is submitted, reviewed, and approved; required fields; approval thresholds by change risk; emergency change path | CIP-010 R1.2, R1.5 |
| **5. Change Documentation Standards** | What records must be created for each change: request, approvals, implementation steps, verification results, rollback plan | CIP-010 R1.3 |
| **6. Control Impact Assessment** | Which CIP-005 and CIP-007 controls must be verified for each change type; who performs verification | CIP-010 R1.4 |
| **7. Post-Change Verification** | How to confirm change was implemented correctly; who signs off; what records are produced | CIP-010 R1.3 |
| **8. Configuration Monitoring** | Method used (automated vs. manual); 35-day cycle; how deviations are alerted and investigated; responsible party | CIP-010 R2 |
| **9. Vulnerability Assessment** | Schedule, scope, methodology, who performs, how findings are tracked and remediated | CIP-010 R3 |
| **10. Transient Cyber Assets** | Authorization, software validation, malicious code procedures | CIP-010 R4 |
| **11. BES Cyber System Information Protection** | How configuration records are classified as BCSI; access controls; disposal procedures | CIP-011 R1 |
| **12. Evidence Retention** | Retention period (3-year minimum); storage location; access controls on records | CIP-010 / CIP-011 |
| **13. Document Control** | Version history; review and approval cycle; owner | All requirements |

## ServiceNow/CMDB Implementation Notes

The CMP should explicitly reference the CMDB as the system of record for:
- Baseline configuration data (CI attribute fields)
- Change request and approval records (Change Management module)
- Configuration monitoring results (Scheduled Jobs or Certification Policies)
- Asset inventory scope (linked to CIP-002 CI classification)

The [[CSDM OT Domain]] enables the CMP's scope section to reference specific OT CI classes (OT System Services, OT Configuration Item Extension Classes) rather than generic "cyber assets."

## Governance Relationship

The CMP is operationalized by the [[Configuration Control Board Charter]], which defines the specific body that executes the authorization process in Section 4. The two documents should be cross-referenced:
- CMP Section 4 references the CCB Charter for approval authorities and thresholds
- CCB Charter references the CMP for the baseline definition and documentation standards

## Common Deficiencies in NERC Audits

- CMP exists but is not updated when the BES Cyber System inventory changes
- Emergency change process defined but not consistently followed (no after-the-fact documentation)
- Baseline records in CMDB not tied to the CMP's baseline definition (different fields used)
- No explicit documentation that control impact assessment (R1.4) was performed
- Monitoring process defined but 35-day cycle not met in practice
