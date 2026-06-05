---
title: ServiceNow OT Manager
category: entities
workspace: Work
project: nerc-cip
tags: [servicenow, ot-security, cmdb, csdm, operational-technology]
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  ServiceNow product providing OT CI classes, OT System Services, dependency mapping,
  and data certification for industrial environments. The CSDM implementation layer for OT.
provenance:
  extracted: 0.80
  inferred: 0.15
  ambiguous: 0.05
base_confidence: 0.78
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# ServiceNow OT Manager

**Type**: Software Product / ServiceNow Application  
**Vendor**: ServiceNow  
**Category**: Operational Technology Management

## What It Is

ServiceNow OT Manager is the ServiceNow product that extends the CMDB and CSDM into operational technology environments. It provides specialized CI classes for industrial equipment, OT System Services for modeling OT functions, and dependency mapping between physical assets and business services.

## Key Capabilities

| Capability | NERC CIP Relevance |
|---|---|
| **OT Configuration Item Extension Classes** | Stores OT-specific attributes (firmware, protocol, zone) on BES Cyber Asset CIs |
| **CMDB CI Classes for OT** | Purpose-built classes for PLCs, RTUs, HMIs, historians, protective relays |
| **OT System Services** | Models BES Cyber Systems as service entities with dependencies mapped to CIs |
| **Dependency Map** | Visualizes which CIs support each OT function — supports CIP-002 impact analysis |
| **CMDB OT Data Certification Policy** | Scheduled data quality reviews — supports 15-month CIP-002 review requirement |
| **Change and Incident Management Integration** | Links change tickets to OT CIs — creates the CIP-010 audit trail |
| **OT Vulnerability Response** | Ingests vulnerability data from Dragos, Forescout, Tenable — supports CIP-010 R3 |

## Integration Partners

OT asset data typically flows into ServiceNow OT Manager from:
- **Dragos** — OT threat detection and asset visibility
- **Forescout** — OT device discovery and classification
- **Tenable** — Vulnerability scanning for OT environments

## Limitations

- Does not ship with native "BES Cyber System" or "BES Cyber Asset" CI classes; utilities must implement as custom extensions
- Asset data quality depends on integration with OT discovery tools — ServiceNow alone cannot discover OT assets
- NERC CIP-specific compliance workflows (CCB approval gates, CIP categorization attributes) require configuration, not out-of-the-box setup

## Related Concepts

- [[CSDM OT Domain]] — The data model OT Manager implements
- [[CMDB as NERC CIP Asset Registry]] — How OT Manager CIs satisfy NERC CIP inventory requirements
- [[CIP-002 BES Cyber System Categorization]] — The standard OT System Services are designed to support
- [[CIP-010 Configuration Change Management]] — Dependency maps support R1.4; CI records store baselines for R1.1
