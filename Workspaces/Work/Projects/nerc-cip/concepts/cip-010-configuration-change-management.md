---
title: CIP-010 Configuration Change Management
category: concepts
workspace: Work
project: nerc-cip
tags: [nerc-cip, cip-010, configuration-management, change-management, baseline, compliance]
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  CIP-010 requires documented baseline configurations, authorized change processes, 35-day drift
  monitoring, and periodic vulnerability assessments for BES Cyber Systems.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.90
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# CIP-010: Configuration Change Management and Vulnerability Assessments

## Purpose

CIP-010 exists to "prevent and detect unauthorized changes to BES Cyber Systems." It operationalizes configuration governance by requiring documented baselines, formal change authorization, drift monitoring, and vulnerability assessments.

## Applicability

Applies to High and Medium impact BES Cyber Systems, Electronic Access Control or Monitoring Systems (EACMS), Physical Access Control Systems (PACS), and Protected Cyber Assets (PCA). Low impact systems have reduced obligations.

## Four Core Requirements

### R1: Configuration Change Management

Each responsible entity must implement documented processes covering:

1. **Baseline establishment (R1.1)**: Maintain a current baseline configuration for each BES Cyber System. A baseline must include:
   - Operating system or firmware (name and version)
   - Commercially available or open-source software (name, version)
   - Custom software
   - Logical network accessible ports (protocol, purpose)
   - Security patches applied

2. **Authorization process (R1.2)**: Authorize and document any change that deviates from the baseline *before* implementation. Each change record must capture: description, justification, impact analysis, rollback plan, requested date, and approvals.

3. **Documentation (R1.3)**: Maintain change request records, approval workflow, implementation evidence, and post-change verification results.

4. **Control impact verification (R1.4)**: For any baseline change, identify and verify which CIP-005 (network access) and CIP-007 (system security) controls could be impacted. Only verify controls actually relevant to the change type.

5. **Emergency change procedures (R1.5)**: Document and implement a process for emergency changes that may bypass normal approval timelines but still require after-the-fact documentation and authorization.

### R2: Configuration Monitoring

- Monitor configurations for unauthorized modifications
- Must detect deviations within **35 days** of the change
- Generate alerts and investigate detected changes
- Document all monitoring activities and findings

This can be met via:
- Automated drift detection tools (Tripwire, Industrial Defender, Tenable)
- Scheduled manual review with documented results
- ServiceNow CMDB reconciliation processes

### R3: Vulnerability Assessments

- Conduct periodic vulnerability assessments at each High/Medium impact BES Cyber System
- Document identified vulnerabilities and remediation tracking
- Evidence retention: 3 calendar years

### R4: Transient Cyber Assets and Removable Media

- Authorize users, locations, and permitted uses
- Verify software vulnerability mitigation before connection
- Malicious code detection on removable media before use

## Documentation Required for Audit Evidence

| Document | Purpose |
|---|---|
| Baseline configuration records | Proves R1.1 — establishes what was authorized |
| Change request forms | Proves R1.2 — shows authorization before change |
| CAB/CCB meeting minutes | Proves R1.2 — organizational authorization trail |
| Post-change verification reports | Proves R1.3-R1.4 — controls verified after change |
| Configuration monitoring logs | Proves R2 — 35-day detection cycle met |
| Vulnerability assessment reports | Proves R3 |
| Remediation tracking records | Proves R3 follow-through |

**Evidence retention minimum: 3 calendar years.**

## CMDB/CSDM Support

The CMDB serves as the system of record for all five baseline components. Key CMDB capabilities that support CIP-010:

- **CI attribute records** store OS, firmware, software, port, and patch baseline data
- **Change management module** creates the authorization trail (R1.2–R1.3)
- **Reconciliation/certification** processes can detect drift (R2)
- **Relationship mapping** (via CSDM service model) supports control impact analysis (R1.4)

## Relationship to Governance Artifacts

- **[[Configuration Management Plan for NERC CIP]]** is the procedural document that defines *how* R1–R4 are implemented organizationally
- **[[Configuration Control Board Charter]]** defines the authorization body and approval criteria required by R1.2

## Related Standards

- [[CIP-002 BES Cyber System Categorization]] — defines which systems CIP-010 applies to
- [[CIP-005]] — Electronic Security Perimeter; changes affecting perimeter require control verification under R1.4
- [[CIP-007]] — System Security Management; patches and ports in CIP-010 baseline are managed here
- [[CIP-011 Information Protection]] — baseline configuration data may be BCSI
