---
title: CMDB as NERC CIP Asset Registry
category: concepts
workspace: Work
project: nerc-cip
tags: [nerc-cip, cmdb, asset-inventory, cip-002, cip-010, servicenow, compliance]
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  The CMDB serves as the auditable, dynamic asset registry required by CIP-002 and CIP-010,
  replacing static spreadsheets with a system that links assets to services, baselines, and change records.
provenance:
  extracted: 0.75
  inferred: 0.22
  ambiguous: 0.03
base_confidence: 0.80
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# CMDB as NERC CIP Asset Registry

## Why CMDB, Not Spreadsheets

NERC CIP requires asset inventories to be:
- **Accurate** — reflect actual deployed configuration
- **Maintainable** — linkable to change management processes
- **Reviewable** — updated every 15 months with documented rationale
- **Auditable** — evidence of who updated what and when

Static spreadsheets fail all four criteria over time. A CMDB backed by the [[CSDM OT Domain]] provides a living registry that automatically links to change requests, configuration baselines, and ownership records.

## CMDB CI Structure for NERC CIP

Each BES Cyber Asset is represented as a CI with the following key attributes:

| CI Attribute | NERC CIP Use |
|---|---|
| Asset name and type | Identification (CIP-002) |
| Location (Electronic Security Perimeter) | Scoping for CIP-005/CIP-010 |
| BES function supported | 15-minute impact analysis (CIP-002) |
| Impact category (High/Medium/Low) | Applicability determination |
| OS / Firmware name and version | Baseline (CIP-010 R1.1) |
| Software installed (name/version) | Baseline (CIP-010 R1.1) |
| Logical ports (protocol/purpose) | Baseline (CIP-010 R1.1) |
| Security patches applied | Baseline (CIP-010 R1.1) |
| Baseline last reviewed | Monitoring cadence (CIP-010 R2) |
| Owner / Responsible team | Accountability |
| Classification (BCSI / non-BCSI) | Information protection (CIP-011) |

## CMDB CI Groupings

| NERC CIP Entity | CMDB Representation |
|---|---|
| BES Cyber System | OT System Service (CSDM) or CI Group |
| BES Cyber Asset | Individual CI (OT CI Extension class) |
| EACMS | CI class linked to BES Cyber System |
| PACS | CI class linked to facility |
| PCA | CI class in same security zone |

## Change Management Integration

CMDB CIs are linked directly to change requests in the Change Management module:
- Every approved change ticket references the CI(s) being modified
- Post-implementation, the CI baseline attributes are updated to reflect the new authorized configuration
- Change history on the CI record constitutes audit evidence for CIP-010 R1.3

The [[Configuration Control Board Charter]] approval workflow in ServiceNow creates the authorization record that must precede any CI baseline update.

## Configuration Monitoring (CIP-010 R2)

CMDB supports the 35-day drift detection requirement via:
- **Scheduled CI certification policies** — periodic review prompts assigned owners to certify CI attributes are current
- **Reconciliation tasks** — compare CI records against discovery scan data (from Dragos, Forescout, Tenable)
- **Automated alerts** — ServiceNow can alert when a CI attribute changes without an associated approved change ticket

## BCSI Considerations

CMDB records containing logical network topology, port configurations, and access paths likely qualify as BES Cyber System Information (BCSI) under [[CIP-011 Information Protection]]. Access controls on CMDB CI records should:
- Restrict read access to personnel with a demonstrated need
- Log all exports of CI data to external formats
- Apply data disposal procedures when CIs are retired

## Relationship to Governance Artifacts

- The [[Configuration Management Plan for NERC CIP]] defines which CI attributes constitute the baseline (CMP Section 3)
- The [[Configuration Control Board Charter]] defines who can authorize changes to CI baseline attributes (Charter Section 3)
- CSDM provides the structural framework that makes CI relationships meaningful for compliance analysis

## PI2 Status (as of June 2026)

Spike 1402602 — "Define CMDB requirement based on NERC CIP solutioning for ServiceNow" — is the active work item connecting this concept to implementation. As of Sprint 2.3 planning it has **no iteration assigned** and is **blocked pending PO (Joe Dames) availability**. This spike is the prerequisite for any concrete NERC-CIP CI structure work in ServiceNow.

See [[cmdb-governance-roadmap]] for broader PI2 context.
