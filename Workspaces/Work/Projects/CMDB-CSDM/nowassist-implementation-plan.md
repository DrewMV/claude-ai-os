---
type: reference
workspace: Work
project: CMDB-CSDM
updated: 2026-06-01
tags: [work, cmdb-csdm, nowassist, ai, roadmap]
---

# PPL NowAssist for CMDB — Implementation Plan

5-phase roadmap for embedding ServiceNow NowAssist AI into CMDB workflows.
Source: PPL NowAssist for CMDB PI Objectives spreadsheet (ART Path: A-INFOPS\CMDB-CSDM\Governance).

## Phase Summary

| Phase | Focus | Program Weeks | Approx PI |
|-------|-------|--------------|-----------|
| 2 | Duplicate CI Elimination | 3–8 | PI-2 |
| 3 | Natural Language CMDB Search | 6–10 | PI-2 |
| 4 | Guided CI Creation | 8–14 | PI-2 / PI-3 |
| 5 | Governance Advice Agentic Workflow | 12–20 | PI-3 |
| Ongoing | Custom Skills (NASK) | Post Week 20 | Post PI-3 |

> Phase 1 (baseline establishment) is referenced as a dependency throughout but is not shown in this document.

---

## Phase 2 — Duplicate CI Elimination (Weeks 3–8)

### OBJ-2.1 — Manage Duplicate CIs Skill Activation

**Objective:** Activate the Manage Duplicate CIs skill and complete an AI-guided review of the existing duplicate CI backlog, prioritizing CI classes most critical to live business services.

**Business Value:** Duplicate CIs corrupt service maps, break change routing, and inflate CMDB Health scores — this is the highest-ROI data quality intervention available.

**Success Criteria:**
- Manage Duplicate CIs skill activated
- Duplicate CI landscape assessed by class and volume
- Top-priority duplicate clusters reviewed and actioned
- Duplicate CI count reduced by ≥25% within 4 weeks of activation

**Dependencies:** OBJ-1.1 complete; CMDB Health correctness job confirmed active; IRE identification rules in place for primary CI classes

---

### OBJ-2.2 — Root Cause Analysis & IRE Rule Improvement

**Objective:** Document the root causes of duplication identified by the AI (overlapping discovery sources, naming conflicts, manual entry collisions) and feed findings into IRE rule improvement.

**Business Value:** Eliminates the systemic causes of duplication rather than only treating the backlog — preventing re-accumulation.

**Success Criteria:**
- Root cause analysis completed for top 3 duplication sources
- At least one IRE identification rule improvement submitted to Technical Governance Board
- Monthly duplicate CI review process established in CMDB Manager calendar

**Dependencies:** OBJ-2.1 in progress; Technical Governance Board engagement for IRE rule changes

---

## Phase 3 — Natural Language CMDB Search (Weeks 6–10)

### OBJ-3.1 — Search CMDB Workflow Activation & Validation

**Objective:** Activate the Search CMDB agentic workflow and validate it against PPL's top 10–15 common CMDB query use cases (incident triage, change impact, compliance review, security).

**Business Value:** Removes the specialist knowledge barrier to CMDB data — enabling incident managers, change managers, and security teams to self-serve CI queries instead of routing requests through the CMDB team.

**Success Criteria:**
- Search CMDB workflow activated and tested
- 10–15 PPL-specific test queries validated for accuracy
- Role-based access controls confirmed (search respects user permissions)
- Quick reference guide produced for PPL query patterns

**Dependencies:** OBJ-1.1 complete; CI data quality sufficient for search results to be reliable (Phase 1 baseline established)

---

### OBJ-3.2 — Secondary User Group Rollout

**Objective:** Roll out natural language CMDB search to secondary user groups (incident managers, change managers, security, compliance) and measure reduction in ad-hoc CMDB data requests to the CMDB team.

**Business Value:** Scales AI value beyond the CMDB team; quantifies time savings from self-service queries.

**Success Criteria:**
- Secondary user groups onboarded with 30-minute orientation session
- ≥80% positive satisfaction from secondary user survey
- Measurable reduction in CMDB team time spent on ad-hoc CI data requests

**Dependencies:** OBJ-3.1 complete; User groups identified and available for onboarding

---

## Phase 4 — Guided CI Creation (Weeks 8–14)

### OBJ-4.1 — Create Configuration Item Guided Workflow

**Objective:** Activate the Create Configuration Item guided workflow and validate it against PPL's top 5 CI classes, confirming that AI guidance enforces correct class selection, mandatory attributes, and relationship creation.

**Business Value:** New CI records created without guidance are a primary source of data quality debt — fixing problems at point of entry is far cheaper than remediation.

**Success Criteria:**
- Guided CI Creation skill activated
- Validated for top 5 CI classes (Servers, Business Applications, Network Devices, Databases, Cloud VMs)
- Completeness scores for guided-created CIs measurably higher than baseline
- Guidance aligned to PPL naming standards and mandatory attribute requirements

**Dependencies:** OBJ-1.2 baseline complete (needed as comparison); PPL CI naming standards and mandatory attribute definitions documented

---

### OBJ-4.2 — Integrate into CI Onboarding Process

**Objective:** Integrate guided CI creation into PPL's standard onboarding process for new CI classes and technology domains (including OT/ICS assets and cloud resources as they are added to CMDB scope).

**Business Value:** Prevents new-domain data quality debt before it accumulates, especially important as PPL expands CMDB scope.

**Success Criteria:**
- Guided CI creation included in PPL CMDB onboarding documentation
- Process communicated to all teams responsible for CI record creation
- Used for at least one new CI class onboarding event within the phase window

**Dependencies:** OBJ-4.1 complete; CMDB onboarding documentation updated

---

## Phase 5 — Governance Advice Agentic Workflow (Weeks 12–20)

### OBJ-5.1 — Governance Advice Workflow — First Full Session

**Objective:** Activate the Provide Advice on CMDB Governance agentic workflow and complete the first end-to-end governance advice session, covering data health, ownership gaps, staleness, and policy violations.

**Business Value:** Transforms the governance workflow from manual report-reading into an AI-guided triage and action process — directly accelerating the work of the CMDB Manager and governance board.

**Success Criteria:**
- Governance Advice workflow activated
- First full governance advice session completed with CMDB Manager
- AI-generated recommendations reviewed and accepted/rejected by Technical Governance Board
- Quarterly governance advice cadence established

**Dependencies:** OBJ-1.2 baseline in place; CI ownership policy defined; Staleness definition agreed by CI class; CMDB Health KPI targets set

---

### OBJ-5.2 — Quarterly Governance Review Cycle

**Objective:** Establish a recurring quarterly NowAssist governance review cycle, using AI-generated CMDB health narratives as the input to governance board reporting, replacing manual dashboard interpretation.

**Business Value:** Reduces the effort of governance board preparation; ensures AI insights drive board decisions rather than being siloed in the CMDB team.

**Success Criteria:**
- Quarterly governance review cycle documented and calendared
- AI-generated health narrative template reviewed and approved by governance board
- First narrative-driven governance board briefing completed
- CMDB health trend (baseline vs. current) quantified

**Dependencies:** OBJ-5.1 complete; Governance board cadence established

---

## Ongoing — Custom Skills / NASK (Post Week 20)

### OBJ-6.1 — NASK Use Case Identification & Prioritization

**Objective:** Identify and prioritize candidate use cases for custom NowAssist skills using the Now Assist Skill Kit (NASK), based on observed gaps from Phases 1–5 and PPL-specific governance requirements.

**Business Value:** Enables PPL to extend AI value beyond OOTB skills into PPL-specific workflows (e.g., CIP asset classification guidance, regulatory compliance checks, PPL naming standard enforcement).

**Success Criteria:**
- Custom skill candidate list produced and prioritized
- Top 1–2 candidates approved by Demand Board for development
- NASK development roadmap documented
- Assists consumption baseline established for budget planning

**Dependencies:** Phases 1–5 operational experience complete; NASK capability available on instance; Demand Board approval process in place
