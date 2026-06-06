---
type: ceremony
ceremony: backlog-refinement
meeting-name: Service Mapping / CSDM / CMDB Backlog Refinement
pi: PI-2
iteration: 2.1
iteration-start: 2026-05-13
iteration-end: 2026-05-26
date: 2026-05-20
status: completed
workspace: Work
project: CMDB-CSDM
attendees: [Joe Dames (PO), Alex Phan (SM), Anu, Bhushan Salsekar (TL), Tanzeel Rehman (TL), Stan Tomberg (TL), Dev Team]
tags: [work, agile, safe, backlog-refinement, cmdb-csdm]
---

# Service Mapping / CSDM / CMDB Backlog Refinement — Iteration 2.1

> **Status: COMPLETED** — Backfill notes if available.

## Stories Reviewed

| ADO Story ID | Title | PI Obj # | Points | DoR Met | Notes |
|-------------|-------|---------|--------|---------|-------|
| TBD | Azure Airlift — Pre-Migration CMDB Preparation | 6 | TBD | TBD | Sequenced: must complete before During |
| TBD | Azure Airlift — During Migration CMDB Tracking | 6 | TBD | TBD | Depends on Pre-Migration completion |
| TBD | Azure Airlift — Post-Migration CMDB Validation | 6 | TBD | TBD | Depends on During Migration completion |
| TBD | CI Attribute Auto-Population — CI Owner | 1 | TBD | TBD | |
| TBD | CI Attribute Auto-Population — Support Group | 1 | TBD | TBD | |
| TBD | CI Attribute Auto-Population — Technical Owner | 1 | TBD | TBD | |
| TBD | Custom Field Implementation — Asset Criticality, RPO, RTO, Recovery Tier | 1 | TBD | TBD | |
| TBD | SCCM Ingestion Validation | 1 | TBD | TBD | |
| TBD | IRE Behavior Validation Post-Upgrade | 1 | TBD | TBD | |

> **Note:** ADO Story IDs to be confirmed with Anu. AI-related stories noted as next wave — entering refinement in Iteration 2.2.

## Acceptance Criteria Discussion

- **Azure Airlift stories** must be reviewed for requirements and AC completeness before implementation. Three-story sequence (Pre/During/Post) must be dependency-mapped in ADO.
- **ServiceNow CI type distinction clarified** — see [[servicenow-ci-type-distinctions]]: Business Application ≠ Application Service (Service Instance) ≠ Application CI. Relevant to migration and service mapping stories.
- **Customization standard established** — evaluate OOTB suitability before any customization. Complex UI filters flagged as high-risk customization area. Decisions treated as product-level choices, not individual preferences.
- **Custom fields (Asset Criticality, RPO, RTO, Recovery Tier)** — confirm alignment with business requirements and data model before implementation.

## Stories Promoted to Ready

| ADO Story ID | Title | Points | Priority |
|-------------|-------|--------|---------|
| TBD | Azure Airlift — Pre-Migration CMDB Preparation | TBD | P1 |
| TBD | CI Attribute Auto-Population stories | TBD | TBD |

## Stories Needing More Work

| ADO Story ID | Title | Blocker | Owner |
|-------------|-------|---------|-------|
| TBD | Azure Airlift During/Post Migration | Dependency on Pre-Migration completion | Joe Dames |

## Story IDs to Share with Anu

_Confirm all IDs with Anuradha Rai once available from ADO._

- Azure Airlift Pre/During/Post Migration stories
- CI attribute auto-population stories
- Custom field implementation story
- SCCM ingestion validation
- IRE validation

## Next Iteration Preview

Stories entering refinement for Iteration 2.2:

| ADO Story ID | Title | Priority |
|-------------|-------|---------|
| TBD | NowAssist AI — CMDB Workflow stories | TBD |
| TBD | NowAssist AI — ITSM Workflow stories | TBD |
