---
title: NowAssist for CMDB
type: concept
workspace: Work
project: ServiceNow
tags: [work, cmdb, nowassist, ai, servicenow, strategy]
created: 2026-06-05
updated: 2026-06-05
summary: "Phased NowAssist AI activation roadmap for CMDB at PPL — 5 features across CI summarization, form help, natural language search, guided CI creation, custom skills, and governance advice."
base_confidence: 0.90
lifecycle: draft
lifecycle_changed: 2026-06-05
provenance: "Derived from PI2 ADO backlog reviewed June 2026 (Objective 1408764)."
---

# NowAssist for CMDB

Objective: embed ServiceNow's NowAssist AI capabilities across CMDB workflows to improve data quality, reduce manual effort, and support governance at scale.

## Activation Phases

### Phase 1 — Foundation & Readiness (Feature 1436574)
*Sprint 2.3 | Prerequisite for all other phases*

- Confirm platform prerequisites for NowAssist activation (Story 1436576) — **gate story; must complete first**
- Activate Now Assist for CMDB Plugin (Story 1436579)
- Activate CI Summarization Skill and onboard pilot group (Story 1436592)
- Activate Contextual CI Form Help Skill (Story 1436593)
- Establish CMDB Health Baseline Score (Story 1436581)

> Story 1436576 is the dependency gate. No other NowAssist activation should proceed until prerequisites are confirmed.

### Phase 3 — Natural Language CMDB Search (Feature 1451935)
*Sprint 2.3 (planned)*

- Activate and validate Search CMDB Agentic Workflow (Story 1455811)
- Roll out natural language search to secondary user groups (Story 1455812)

### Phase 4 — Guided CI Creation (Feature 1451936)
*Sprint 2.3 (planned)*

- Activate and validate Guided CI Creation Workflow (Story 1451947)
- Integrate Guided CI Creation into PPL CMDB onboarding process (Story 1451948)

### Phase 5 — Custom Skills & Governance Advice (Features 1451937, 1451938)
*Sprint 2.3 (planned — at risk of deferral)*

- Activate "Provide Advice on CMDB Governance" Agentic Workflow (Story 1451949)
- Establish quarterly governance review cycle using AI-generated health narratives (Story 1451950)
- Identify and prioritize Custom NASK Skill candidates (Story 1451955)

## Sprint 2.3 Risk

All 13 NowAssist stories are scheduled in a single 2-week sprint. Recommended approach:
1. Complete Phase 1 fully before activating any other phase
2. If capacity is tight, defer Phases 4–5 to Sprint 2.4
3. Phase 3 (Natural Language Search) can run in parallel with Phase 1 once prerequisites are confirmed

## Key Dependencies

- NowAssist plugin must be activated before any skill can be enabled
- CMDB Health Baseline (Phase 1) provides the measurement anchor for governance advice (Phase 5)
- Platform admin access required for plugin activation — confirm availability before sprint start

## Authoritative Source

> **NotebookLM — ServiceNow Australia AI Platform Capabilities**
> Query this notebook for official documentation on NowAssist plugin activation, CI summarization skills, form help, natural language search, guided CI creation, and NASK custom skills.
> See [[notebooklm-library]] for full notebook registry.

## Related Pages

- [[cmdb-governance-roadmap]] — overall CMDB governance and operations roadmap
- [[data-certification-program]] — Data Certification pilot, which NowAssist governance advice can support
- [[notebooklm-library]] — full registry of connected ServiceNow Australia notebooks
