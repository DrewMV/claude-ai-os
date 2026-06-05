---
title: ServiceNow Upgrade Analysis — CMDB Impact
type: concept
workspace: Work
project: ServiceNow
tags: [work, cmdb, upgrade, ire, servicenow, risk, analysis]
created: 2026-06-05
updated: 2026-06-05
summary: "CMDB upgrade impact assessment framework covering IRE behavior, schema changes, discovery touchpoints, attribute precedence, governance controls, and remediation planning."
base_confidence: 0.90
lifecycle: draft
lifecycle_changed: 2026-06-05
provenance: "Derived from PI2 ADO backlog reviewed June 2026 (Feature 1355890, Sprint 2.3)."
---

# ServiceNow Upgrade Analysis — CMDB Impact

Feature 1355890 in PI2 tracks a structured CMDB impact assessment for the upcoming ServiceNow platform upgrade. All 11 spikes and stories are in Sprint 2.3 (June 10–23, 2026).

## Sandbox Upgrade Schedule (June 2026)

> **Status:** Sandbox upgrade confirmed as scheduled — specific version and dates communicated via email week of June 5, 2026.
> **Action required:** Capture exact version and sandbox dates here once confirmed. This directly gates Sprint 2.3 spike execution — analysis work cannot begin until the sandbox is available.

| Field | Status |
|-------|--------|
| Target version | TBD — confirm from upgrade email |
| Sandbox upgrade date | TBD — confirm from upgrade email |
| Sprint 2.3 impact | High — 11 spikes/stories depend on sandbox availability |

---

## Assessment Areas

### 1. IRE (Identification & Reconciliation Engine)
- Assess upgrade impact on IRE behavior (Spike 1403722)
- Review and validate CMDB Dynamic IRE behavior post-Australia upgrade (Story 1411237)
- Validate impact on authoritative sources, attribute precedence, and data "flapping" (Spike 1403723)

> IRE behavior changes are the highest-risk area — attribute precedence and authoritative source rules can silently change after an upgrade, causing CI data to revert or conflict.

### 2. Schema & Data Model
- Identify CMDB schema and data model changes introduced by the upgrade (Spike 1402543)
- Analyze impact on CI class hierarchy, customizations, and class manager behavior (Story 1403721)

### 3. Discovery & Integration Touchpoints
- Impact assessment of Discovery and integration touchpoints — mid-servers, schedules, sources (Spike 1403725)
- Identify deprecated plugins/features that could impact CMDB capabilities (Spike 1403733)

### 4. Governance Controls & KPIs
- Analyze impact on governance controls, KPIs, and CMDB operating model during upgrade (Story 1403731)
- Validate CMDB Health indicators and scorecards post-upgrade (3Cs + rules coverage) (Spike 1403726)

### 5. Remediation Planning
- Build remediation backlog and validation plan to prevent CMDB data integrity degradation (Story 1403737)
- Create Upgrade Impact Risk Register and dependency map specific to CMDB (Spike 1403736)

### 6. Team Enablement (Nice to Have)
- Establish CMDB upgrade readiness knowledge package for team enablement (Spike 1403738)

## Key Risks to Monitor

| Risk | Why It Matters |
|------|---------------|
| IRE attribute flapping post-upgrade | CI attributes can revert to lower-precedence sources silently |
| Deprecated plugins | Could disable discovery rules or integrations without warning |
| Class hierarchy changes | Custom CI classes may break or lose inheritance |
| CMDB Health score drift | Baseline established in NowAssist Phase 1 could shift post-upgrade |

## Outputs Expected from Sprint 2.3

- Upgrade Impact Risk Register (Spike 1403736)
- Remediation backlog (Story 1403737)
- Validated IRE behavior documentation (Spike 1403722, Story 1411237)
- CMDB Health scorecards validated post-upgrade (Spike 1403726)

## Authoritative Sources

> **NotebookLM — ServiceNow Australia AI Platform Capabilities**
> Query for CMDB/CSDM architecture changes, IRE behavior, schema updates, class hierarchy changes, and platform capability changes introduced in the Australia release.

> **NotebookLM — ServiceNow Australia IT Operations Management (ITOM)**
> Query for Discovery touchpoint changes, mid-server impacts, deprecated plugins, AIOps behavior, and Service Mapping changes in the Australia release.

> See [[notebooklm-library]] for full notebook registry.

## Related Pages

- [[cmdb-governance-roadmap]] — governance model that upgrade must preserve
- [[nowassist-for-cmdb]] — NowAssist health baseline established in Phase 1 must be re-validated post-upgrade
- [[notebooklm-library]] — full registry of connected ServiceNow Australia notebooks
