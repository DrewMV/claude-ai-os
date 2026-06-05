---
title: >-
  Research: ServiceNow CMDB/CSDM Governance and NERC CIP Compliance
category: synthesis
workspace: Work
project: nerc-cip
tags: [nerc-cip, cmdb, csdm, servicenow, configuration-management, compliance, ot-security]
sources:
  - "https://nercipedia.com/active-standards/cip-010-4-cyber-security-configuration-change-management-and-vulnerability-assessments/"
  - "https://frenos.io/nerc-cip/nerc-cip-requirements"
  - "https://shieldworkz.com/blogs/nerc-cip-evidence-pack-how-to-document-scada-patch-change-management-for-audits"
  - "https://www.servicenow.com/community/grc-blog/simplify-compliance-to-nerc-cip-with-servicenow/ba-p/2838673"
  - "https://dss.bg/news/csdm-5-0-explained-whats-new-how-it-works-why-it-matters"
  - "https://www.servicenow.com/docs/r/operational-technology/operational-technology-manager/ot-use-case.html"
  - "https://www.industrialdefender.com/blog/nerc-cip-checklist-identification-categorization-bes-cyber-assets"
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  3-round research on how ServiceNow CMDB/CSDM governance — Configuration Management Plan
  and CCB Charter — maps to NERC CIP-002, CIP-007, CIP-010, and CIP-011 requirements.
provenance:
  extracted: 0.70
  inferred: 0.25
  ambiguous: 0.05
base_confidence: 0.82
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# Research: ServiceNow CMDB/CSDM Governance and NERC CIP Compliance

## Overview

NERC CIP standards require electric utilities to maintain accurate, auditable records of BES Cyber Assets, enforce authorized change processes, and protect configuration data. ServiceNow's CMDB — governed by the CSDM framework — serves as the system of record that satisfies these requirements across CIP-002 (asset categorization), CIP-007 (system security baselines), CIP-010 (configuration change management), and CIP-011 (information protection). The Configuration Management Plan (CMP) and Configuration Control Board (CCB) Charter are the two governance artifacts that operationalize this: the CMP defines *what* is managed and *how*, while the CCB Charter defines *who* authorizes changes and under *what criteria*. Together they create the documented process evidence NERC auditors require.

## Key Findings

- **CIP-002 relies on CMDB as the authoritative asset inventory.** Static spreadsheets are explicitly flagged as non-viable; a dynamic CMDB with CSDM service mapping provides the defensible, maintainable inventory that ties BES Cyber Assets to BES functions needed for impact categorization (High/Medium/Low). Inventory must be reviewed every 15 months. [[CIP-002 BES Cyber System Categorization]]

- **CIP-010 is the standard most directly operationalized by CMDB governance.** R1 requires documented change management processes with baseline maintenance and authorization workflows. R2 requires configuration drift detection within 35 days. R3 requires periodic vulnerability assessments. All three map to CMDB capabilities: baselines as CI attributes, change tickets as authorization records, and automated drift detection or scheduled reviews. [[CIP-010 Configuration Change Management]]

- **The Configuration Management Plan (CMP) is the procedural backbone of CIP-010 compliance.** It defines baseline configuration components, the authorization chain for changes, documentation standards, monitoring cadence, evidence retention (3-year minimum), and vulnerability assessment schedule. Each CMP section can be annotated with a direct CIP requirement mapping. [[Configuration Management Plan for NERC CIP]]

- **The CCB Charter is the governance backbone of the CMP.** It defines the cross-functional body (OT + IT + Security) that authorizes changes, their meeting cadence, voting/approval thresholds, emergency change procedures, and documentation obligations. CCB meeting minutes are required NERC audit evidence. Without a charter, the authorization "process" lacks the organizational accountability NERC expects. [[Configuration Control Board Charter]]

- **CSDM 5.0 extends the ServiceNow data model explicitly into OT.** New CI classes for industrial equipment, OT System Services, and dependency mapping between physical assets and business services enable utilities to model BES Cyber Systems inside ServiceNow's CMDB, not just IT assets. This is the structural bridge between ServiceNow governance and NERC CIP applicability. [[CSDM OT Domain]]

- **CIP-011 means CMDB data itself may be BCSI.** Configuration records that could enable unauthorized access to BES Cyber Systems are classified as BES Cyber System Information (BCSI) and must be protected. Access controls on CMDB records — role-based access, audit logging of views/exports — are a CIP-011 control. [[CIP-011 Information Protection]]

- **ServiceNow GRC closes the loop by linking assets to controls.** ServiceNow's Integrated Risk Management tethers CMDB CIs to compliance controls, providing real-time compliance posture for CIP-003, CIP-007, CIP-010, and CIP-013. The CMDB is both the asset registry and the evidence substrate.

## CMP Sections → CIP Requirements Mapping

| CMP Section | CIP Requirement |
|---|---|
| Scope — which BES Cyber Systems are covered | CIP-002 (categorization scope) |
| Baseline configuration components | CIP-010 R1.1 (OS, firmware, software, ports, patches) |
| Change authorization process | CIP-010 R1.2 (authorized and documented changes) |
| Change documentation standards | CIP-010 R1.3 (change records, approvals, test evidence) |
| Post-change verification procedures | CIP-010 R1.4 (control impact verification) |
| Emergency change procedures | CIP-010 R1.5 |
| Configuration monitoring schedule (35-day cycle) | CIP-010 R2 |
| Vulnerability assessment schedule | CIP-010 R3 |
| Transient cyber asset procedures | CIP-010 R4 |
| BCSI identification and protection | CIP-011 R1 |
| Evidence retention policy (3-year minimum) | CIP-010 / CIP-011 evidence requirements |

## CCB Charter Elements → CIP Requirements Mapping

| CCB Charter Element | CIP Requirement |
|---|---|
| Membership (OT, IT, Security representation) | CIP-010 R1.4 (cross-domain impact analysis) |
| Change authorization criteria and thresholds | CIP-010 R1.2 (only authorized changes) |
| Baseline definition and approval authority | CIP-010 R1.1 |
| Change request documentation standards | CIP-010 R1.3 |
| Emergency change authorization procedure | CIP-010 R1.5 |
| Meeting cadence and minutes requirements | Audit evidence for CIP-010 |
| Scope — which systems require CCB approval | CIP-002 (High/Medium impact BCS) |
| ESP boundary change review requirement | CIP-005 (Electronic Security Perimeter) |
| Rollback/contingency plan requirement | CIP-010 R1.3 |

## Core Concepts

- [[CIP-002 BES Cyber System Categorization]] — The foundational inventory and impact-classification standard; CMDB is the required system of record
- [[CIP-010 Configuration Change Management]] — The change management and baseline standard most directly served by CMDB governance
- [[CIP-011 Information Protection]] — BCSI protection requirements that extend to CMDB records
- [[Configuration Management Plan for NERC CIP]] — Procedural document that maps governance processes to CIP requirements
- [[Configuration Control Board Charter]] — Governance document defining the authorization body for changes to BES Cyber Systems
- [[CSDM OT Domain]] — ServiceNow's data model layer enabling OT asset representation in CMDB
- [[CMDB as NERC CIP Asset Registry]] — How the CMDB specifically satisfies CIP-002 and CIP-010 asset inventory obligations

## Entities & Tools

- [[ServiceNow OT Manager]] — ServiceNow product providing OT CI classes, OT System Services, and dependency mapping for industrial environments
- [[ServiceNow Integrated Risk Management (IRM)]] — Links CMDB CIs to compliance controls; manages CIP-007 and CIP-010 posture

## Contradictions & Open Questions

- **CCB vs. CAB terminology**: NERC CIP literature uses "Change Advisory Board" (CAB) rather than "Configuration Control Board" (CCB). In practice, the two terms describe the same governance function. Some organizations use CCB specifically for configuration baseline approvals and CAB for routine IT changes. For NERC CIP, the body reviewing changes to BES Cyber Systems should cover both functions.
- **CSDM BES Cyber System as native class**: There is no native "BES Cyber Asset" or "BES Cyber System" CI class in ServiceNow out of the box. These are implemented as custom extensions on OT CI classes or as CMDB CI groups. Utilities need to design this mapping intentionally.
- **CIP-010 R2 automation**: The 35-day monitoring requirement can be met manually (scheduled review) or via automated drift detection tools (e.g., Tripwire, Industrial Defender feeding into ServiceNow). The CMP should specify which method is used and how alerts are triaged.
- **CIP-011 CMDB data protection**: Whether CMDB records constitute BCSI depends on the data they contain. Records with logical network topology, port configurations, and access paths likely qualify. This determination should be documented in the information protection program.

## Sources Consulted

- [[NERCipedia CIP-010-4]] — Full CIP-010-4 requirements, documentation obligations, evidence retention
- [[Frenos NERC CIP Requirements]] — CIP-002, CIP-007, CIP-010 practical breakdown with CMDB relevance notes
- [[Shieldworkz NERC CIP Evidence Pack]] — CAB structure, change request contents, audit evidence requirements
- [[ServiceNow Community NERC CIP]] — ServiceNow CMDB/GRC capabilities mapped to CIP-003, CIP-007, CIP-009, CIP-010, CIP-013
- [[CSDM 5.0 Explained]] — 7-domain CSDM structure, OT extension, governance and ownership features
- [[ServiceNow OT Manager Docs]] — OT CI classes, CSDM table usage, OT System Services
- [[Industrial Defender BES Cyber Asset Checklist]] — Asset categorization requirements and 15-month update cycle
