---
type: reference
workspace: Work
project: CMDB-CSDM
updated: 2026-06-01
tags: [work, cmdb-csdm, process, requirements]
---

# Requirements Process — CMDB-CSDM

Reference document for how requirements flow from stakeholder request to Sprint Planning. See [[Backlog/definition-of-ready]] for story readiness gates and [[Team/working-agreements]] for team contacts and roles.

## Process Flow

```
Stakeholder (PPL / Accenture)
    OR
Employee Center request → Uloma (PPL BA)
    ↓
PO (Joe Dames) meets with stakeholders to gather and confirm requirements
    ↓
Anu + Uloma + Alex Phan refine the story
    OR advise Anu when the story is ready to create
    ↓
Story created in ADO
  - Must be created under correct Epic > Feature using "+" icon
  - PO owns Epic and Feature levels
  - Priority assigned: P1–P4
  - Story ID shared with Anu
    ↓
Service Mapping / CSDM / CMDB Backlog Refinement (team-level)
  - Dev team sizes the story
  - BPC, Tester, Developers discuss requirement and technical solution
    ↓
SERVNW Program Backlog Refinement & Prioritization (Wednesday, program-level)
  - Cross-team review and prioritization
    ↓
Sprint Planning — Dev team picks up work
  - PO sub-ranks multiple P1 stories numerically (1, 2, 3...) for execution order
```

## Key People

| Name | Role | Responsibility in Process |
|------|------|--------------------------|
| Joe Dames | Solution Architect / PO | Requirements confirmation, Epic/Feature ownership, priority ranking |
| Anuradha Rai (Anu) | Functional Designer | Story creation in ADO, Program Backlog Review ownership |
| Uloma Adelufosi | Product Analyst | Employee Center request intake, story refinement with PO |
| Alex Phan | Scrum Master | Story refinement, Sprint Planning facilitation |

## ADO Hierarchy Rule

All items must follow: **Epics > Features > Stories**

- Always create new stories from Epic/Feature links using the "+" icon
- Never create standalone stories — linkage is required for tracking and reporting
- PO must own Epic and Feature levels

## Priority Model

| Priority | Meaning |
|---------|---------|
| P1 | Must Have |
| P2 | Should Have |
| P3 | Could Have |
| P4 | Nice to Have |

When multiple P1 stories exist, PO provides numeric sub-ranking (1–10) so the team knows execution order during Sprint Planning.

## Recurring Meetings in This Process

| Meeting | Cadence | Level | Purpose |
|---------|---------|-------|---------|
| Service Mapping / CSDM / CMDB Backlog Refinement | Per iteration | Team | Story sizing + technical discussion |
| SERVNW Program Backlog Refinement & Prioritization | Weekly, Wednesday | Program | Cross-team review and prioritization |
| ServiceMapping / CSDM / CMDB — Sprint Planning | Per iteration | Team | Dev team commits to stories |

## OCM Coordination

Organizational Change Management (OCM) is involved for communications and training when stories have significant user or process impact. Engage OCM early when:

- A story changes a user-facing workflow
- New fields or UI changes affect end users
- A policy or governance decision requires training
- Communications to stakeholders are needed before or after release

## Customization Governance

Established 2026-06-08 (communicated by Alex Phan to Manuel Vazquez and team).

**Definition:**

| Type | Examples | Requires governance? |
|------|----------|----------------------|
| Configuration | Adding fields, forms, basic updates | No |
| Customization | Custom logic, scripts, workflows, anything deviating from OOTB | **Yes** |

**Process for Customization Stories:**

1. Apply **"Customization" tag** to the story in ADO
2. Log a **Decision/RAID issue** in ADO (Josh or Alex Phan can log — SM coordinates, does not need to log directly)
3. **Link the RAID issue** to the story in ADO
4. Submit for **Sonica Das approval** — story cannot be implemented until approved
5. RAID issue reviewed at **RAID log meeting**
6. Story tracked in **monthly ADO customization report** (query maintained by program team)

**SM Role:** Identification and coordination. The cleanest enforcement point is the Definition of Ready — a story with custom logic and no linked RAID issue does not enter the sprint.

ADO report reference: https://dev.azure.com/PPLElectric/A-INFOPS/_queries/query/?tempQueryId=e45abffd-39bc-471e-b435-90cc0d392b92
