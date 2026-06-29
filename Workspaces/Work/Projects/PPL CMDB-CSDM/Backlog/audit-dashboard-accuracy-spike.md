---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: reference-draft
scope: NON-SOW
updated: 2026-06-23
tags: [work, cmdb-csdm, backlog, quality-governance, spike]
---

# Audit Dashboard Accuracy & Gap Remediation Plan — Spike (Business Application tab)

> **🟢 RECONCILED with ADO (6/29).** Created as Spike **1480111** — "Validate Business Application Audit Dashboard Scope & Build a Compliance-Prioritized Gap Remediation Plan" · Owner **Joe Dames** · Iteration **2.4** · State **Ready DoR**. This file remains the working reference; reconcile further changes back here. ADO is authoritative.
> **Reusable approach** — see [[audit-dashboard-spike-template]] to apply this same structure to the next audit areas (Servers, Database, Computer, Groups).

---

## Title
[Spike] Validate Business Application Audit Dashboard Scope & Build a Compliance-Prioritized Gap Remediation Plan

## Iteration / dates
PI-2 · Iteration 2.4 — Target completion 2026-06-30 (front-load at start of 2.4).

## Context / Problem statement
The Business Application audit dashboard reads directly from CMDB production. The data quality of the active BA population (2,135) is in question, and — most importantly — there is no documented plan to close the gaps each audit surfaces. The numbers are already being used for governance reporting, with high gap rates on several audits (Missing Recovery Tier ~85%, Missing Classification ~64%, Missing Value Stream ~39%). We need to confirm the scope is accurate, then turn each audit into an owned, dated, costed remediation action.

## Spike statement (hypothesis to resolve)
As the CMDB Configuration Management Process Owner, I want the active-Business-Application scope validated and a compliance-prioritized remediation plan — with owner, target completion date, and solution type (automated / manual / other) — built for every audit gap, so that BA data quality can be governed to target and the team has an actionable, time-bound plan instead of raw counts.

## Outcome / deliverable
A Gap Remediation Plan for the BA tab:
1. Scope validation result for Active Business Application (2,135).
2. One remediation row per audit, ordered by compliance priority, each with: what it measures · gap root cause · solution type (automated / manual / other) · owner · target completion date · draft story requirement.
3. Any safe quick fixes applied (within the BA-pause limits below).

## Audit boxes in scope (all 11 reviewed)
Every box on the Business Application tab is reviewed — the first is the scope, the other ten are the quality audits:
1. Active Business Application — 2,135 (the scope/denominator — validated first, not a gap audit)
2. Business Application CIs – Missing CI Owner — 11
3. Business Application: Missing Business Owner — 350
4. Business Application – Missing App Code / Asset Tags — 208
5. Business Application: Missing Support Group — 496
6. Business Application – Missing Technical Owner Group — 236
7. Business Application: Missing Approval Group (Business Owner) — 401
8. Business Application – Missing Classification — 1,375
9. Business Application – SOX Indicator is True / SOX Type is Empty — 5
10. Business Application – Missing Value Stream (Business Unit) — 822
11. Business Application – Missing Recovery Tier — 1,820

> **BA enhancement pause (6/10 decision):** new Business Application enhancements are paused until the Application Services migration completes. "Safe quick fixes" are limited to dashboard/query corrections and any data fix explicitly cleared with Joe + change control. Mass BA-record edits are logged as a story, not done inline.
