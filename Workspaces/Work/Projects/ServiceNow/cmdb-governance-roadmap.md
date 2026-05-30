---
type: project-note
workspace: Work
project: ServiceNow
tags: [work, operations, strategy, process]
updated: 2026-05-30
summary: "CMDB governance and operations roadmap covering standards, discovery rules, CI lifecycle, archival policies, and CMDB health dashboards."
base_confidence: 0.80
lifecycle: draft
lifecycle_changed: 2026-05-30
provenance: "Distilled from one Claude conversation (May 2026) in which a CMDB roadmap proposal was drafted from screenshot findings. Extracted from actual proposal content."
---

# CMDB Governance Roadmap

A governance and operations roadmap for the ServiceNow CMDB, derived from a review of current state findings.

## Key Themes

- **Standards and SOPs** — defining what goes in the CMDB and under what rules
- **Principal classes** — which CI (Configuration Item) types are in scope
- **Discovery rules** — automated discovery configuration and validation
- **IRE (IT Resource Explorer)** — managing the IRE integration for CMDB population
- **Archival and staleness policies** — when to retire/archive CIs that are no longer active
- **CMDB health dashboards** — ongoing visibility into data quality

## Governance Structure

Proposed governance involves:

- **CMB (Change Management Board)** — approval gate for changes affecting CMDB schema or principal classes
- **TRB (Technology Review Board)** — technical oversight for discovery rule changes
- **RACI framework** ^[inferred] — ownership clarification between IT Ops, platform team, and business owners

## CI Lifecycle Management

Key stages in a CI's lifecycle within the CMDB:

1. **Discovery / Onboarding** — automated (via discovery rules) or manual entry
2. **Active management** — ongoing updates, relationships, ownership
3. **Staleness detection** — rules to flag CIs not seen by discovery in N days
4. **Archival** — move stale CIs to archived state (not deleted; retained for audit)

## Related Pages

- [[servicenow-analytics]] — analytics and reporting work on the same platform
