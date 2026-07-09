---
workspace: Work
tags: [cmdb-csdm, servicenow, governance, ccb, template]
type: template
status: template
updated: 2026-07-01
---

# Configuration Management Plan — Reusable Template

> **What this is:** a reusable skeleton + table of contents for a ServiceNow Configuration Management Plan (CMP), aligned to the **CSDM 5** framework and CMDB governance best practices. Structure validated against official ServiceNow sources (CSDM 5 white paper, CMDB Data Manager, CMDB Health docs).
>
> **Pattern:** **class-centric (Option A)** — all per-class detail lives in §8; §9–§11 hold *cross-class policy/rules only* and must never restate per-class values. This matches how [[configuration-management-plan-stage1]] is already built.
>
> **Conventions:** `[CCB confirm]` marks a PPL governance decision requiring CCB ratification. `<angle brackets>` mark fill-ins.
>
> **Parent:** [[configuration-management-plan]] (the CMP umbrella).

---

## Document Frontmatter (copy into each real CMP doc)

```yaml
title: Configuration Management Plan
owner: <Configuration Management Process Owner>
approver: <CCB Chairperson>
version: 0.1 (DRAFT)
status: draft
updated: <YYYY-MM-DD>
```

## Table of Contents

1. Document Control
2. Introduction & Purpose
3. Scope
4. Objectives & Success Criteria
5. References & Related Documents
6. Roles & Responsibilities
7. CMDB / CSDM Architecture
8. Data Definitions (Class & Attribute Dictionary) — *class-centric, self-contained*
9. Data Sourcing & Reconciliation — Policy — *rules only, no per-class values*
10. CI Lifecycle Management — Policy — *rules only*
11. Relationship & Dependency Standard — *rules only*
12. Data Quality & CMDB Health
13. Data Certification & Attestation
14. Governance & Change Control (CCB Operating Model)
15. Security & Compliance Alignment
16. Metrics, Reporting & Dashboards
17. Maintenance & Continual Improvement
18. Glossary
19. Appendices

---

## 1. Document Control

Version history (version · date · author · summary of change) · approvers / sign-off (CCB Chair, Process Owner, Architecture) · distribution list · review cycle (e.g., reviewed quarterly by the CCB).

## 2. Introduction & Purpose

Why the plan exists and what "good" looks like for the CMDB · relationship to ITIL Service Configuration Management and to the CSDM framework · intended audience (CCB, CI Class Owners, Discovery/integration teams).

## 3. Scope

- **In scope** — CI classes governed by this plan: `<list>`
- **Out of scope** — `<list>`
- **CSDM 5 domains in scope** — Foundation · Ideation & Strategy · Design & Planning · Build & Integration · Service Delivery · Service Consumption · Manage Portfolio
- Environments / business units / data sources covered.

## 4. Objectives & Success Criteria

Measurable objectives, each tied to a verifiable KPI in §12/§16. Example: audit coverage ≥ 90% `[CCB confirm]`.

## 5. References & Related Documents

CSDM white paper `<confirm version>` · ServiceNow CMDB docs · contract deliverables · related governance policies · the data-dictionary doc(s).

## 6. Roles & Responsibilities

- **Configuration Management Process Owner** — overall CMDB health & policy
- **CMDB Manager / CI Data Manager** — day-to-day data quality, certification
- **CI Class Owners / Class Managers** — accountable per class `<roster>`
- **Data Stewards** — attribute-level stewardship
- **Discovery / Integration owners** — authoritative source feeds
- **CCB (Change Control Board)** — ratifies definitions, policy, precedence rules
- **RACI matrix** — roles × key activities

## 7. CMDB / CSDM Architecture

The seven CSDM 5 domains and what lives in each · CI class hierarchy in scope (parent/child) · how classes map to CSDM 5 domains · service types (Business / Technical / Application service).

## 8. Data Definitions (Class & Attribute Dictionary) — CLASS-CENTRIC

> Authoritative home for all per-class detail. §9–§11 state *rules*; this section states the *values*. Each class is a self-contained unit. Link to [[configuration-management-plan-stage1]] — do not duplicate.

For each class:

1. **Class Identity & Scope**
2. **Attribute-Level Data Dictionary** (incl. Source of Truth, Mandatory, Audited, Certification Owner)
3. **Data Population & Identification** (this class's IRE identifiers + precedence)
4. **Relationship Architecture** (this class's CSDM mappings)

## 9. Data Sourcing & Reconciliation — Policy *(RULES ONLY)*

The IRE philosophy · connector / discovery inventory · how precedence conflicts are adjudicated in general. **Never restate per-class source-of-truth values — those live in §8.**

## 10. CI Lifecycle Management — Policy *(RULES ONLY)*

What each lifecycle stage / operational status *means* · transition triggers · staleness, retirement, and archival rules (ref: CMDB Data Manager). **No per-class value lists.**

## 11. Relationship & Dependency Standard *(RULES ONLY)*

Approved relationship types · top-down vs tag-based vs manual Service Mapping · mapping ownership and refresh cadence.

## 12. Data Quality & CMDB Health

The three metrics — **Completeness · Compliance · Correctness** · targets/thresholds per class `[CCB confirm]` · remediation workflow for failing CIs.

## 13. Data Certification & Attestation

Certification cadence · intake · ownership · attestation flow · OOTB vs custom decision `[CCB confirm]` · evidence retention for audit.

## 14. Governance & Change Control (CCB Operating Model)

CCB charter, membership, chairperson, quorum · meeting cadence and decision process · change control for data definitions, classes, and precedence rules · exception / waiver process.

## 15. Security & Compliance Alignment

SOX scoping · regulatory drivers (e.g., NERC-CIP) · security standards · audit inclusion rules per class/attribute `[CCB confirm]` · access control & data classification.

## 16. Metrics, Reporting & Dashboards

KPI catalog (health scores, certification %, audit coverage) · dashboards · report cadence and audience per report.

## 17. Maintenance & Continual Improvement

Review/update cadence for this plan · how findings feed back into objectives and the CCB backlog.

## 18. Glossary

CI · CSDM · IRE · CCB · SGC · Service Mapping · and other key terms.

## 19. Appendices

- **A** — RACI matrix
- **B** — CI class → CSDM domain map
- **C** — Authoritative-source matrix
- **D** — KPI definitions
- **E** — Change / version log detail
