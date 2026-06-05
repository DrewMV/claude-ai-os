---
title: DSS.bg — CSDM 5.0 Explained
category: references
workspace: Work
project: nerc-cip
tags: [csdm, servicenow, cmdb, ot-security, governance]
sources:
  - "https://dss.bg/news/csdm-5-0-explained-whats-new-how-it-works-why-it-matters"
source_url: "https://dss.bg/news/csdm-5-0-explained-whats-new-how-it-works-why-it-matters"
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  Independent analysis of CSDM 5.0. Documents the 7-domain structure, new OT CI classes,
  Teams capability for ownership tracking, and SBOM support for compliance.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.80
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# DSS.bg — CSDM 5.0 Explained

**URL**: https://dss.bg/news/csdm-5-0-explained-whats-new-how-it-works-why-it-matters

## What It Covers

Third-party explanation of CSDM 5.0, covering the new 7-domain structure, OT additions, and compliance-relevant features. Good for understanding what changed from CSDM 4.x.

## Key Claims

**Domain expansion (5 → 7 domains):**
1. Foundation
2. Ideation & Strategy (new)
3. Design & Planning
4. Build & Integration
5. Service Delivery (renamed from Manage Technical Services)
6. Service Consumption
7. Manage Portfolio (new)

**OT support:**
- "New classes added to support industrial environments and physical processes"
- Extends model from IT to manufacturing and utility sectors

**Compliance features:**
- **SBOM** (Software Bill of Materials): "detailed inventory of software components, critical for security operations and vulnerability tracking" — maps directly to CIP-010 R1.1 software baseline requirement
- **Information Objects** (Design & Planning domain): supports data governance and regulatory requirements — relevant for CIP-011 BCSI identification
- **Teams** capability: flexible tracking of user groups per CI, supporting clear ownership accountability

**Governance language:**
- "Different roles and teams speak a common language" — reduces ambiguity in configuration management
- Enables "accurate impact assessment across ITSM processes"

## Concepts Informed

- [[CSDM OT Domain]]
- [[CMDB as NERC CIP Asset Registry]]
- [[CIP-010 Configuration Change Management]]
- [[CIP-011 Information Protection]]
