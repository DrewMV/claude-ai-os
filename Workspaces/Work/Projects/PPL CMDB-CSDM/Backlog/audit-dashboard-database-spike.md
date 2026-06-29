---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: reference-draft
scope: NON-SOW
updated: 2026-06-23
tags: [work, cmdb-csdm, backlog, quality-governance, spike]
---

# Audit Dashboard Accuracy & Gap Remediation Plan — Spike (Database tab)

> **🟢 RECONCILED with ADO (6/29).** Created as Spike **1480113** — "Validate Database Audit Dashboard Scope & Build a Compliance-Prioritized Gap Remediation Plan" · Owner **Stan Tomberg** · Iteration **2.4** · State **Ready DoR**. This file remains the working reference; reconcile further changes back here. ADO is authoritative.
> **Built from** [[audit-dashboard-spike-template]] · sibling of [[audit-dashboard-accuracy-spike]] (BA) and [[audit-dashboard-servers-spike]] (Servers).

---

## Title
[Spike] Validate Database Audit Dashboard Scope & Build a Compliance-Prioritized Gap Remediation Plan

## Iteration / dates
PI-2 · Iteration 2.4 — Target completion 2026-06-30 (front-load at start of 2.4).

## Context / Problem statement
The Database audit dashboard reads directly from CMDB production. The data quality of the active database CI population (3,113) is in question, and — most importantly — there is no documented plan to close the gaps each audit surfaces. The numbers are already being used for governance reporting, with very high gap rates on several audits (Missing Value Stream ~100%, Missing Approval Group ~99.9%, Missing Environment ~38%). We need to confirm the scope is accurate, then turn each audit into an owned, dated, costed remediation action.

## Spike statement (hypothesis to resolve)
As the CMDB Configuration Management Process Owner, I want the active-database scope validated and a compliance-prioritized remediation plan — with owner, target completion date, and solution type (automated / manual / other) — built for every audit gap, so that database data quality can be governed to target and the team has an actionable, time-bound plan instead of raw counts.

## Outcome / deliverable
A Gap Remediation Plan for the Database tab:
1. Scope validation result for Active Database CI Count (3,113).
2. One remediation row per audit, ordered by compliance priority, each with: what it measures · gap root cause · solution type (automated / manual / other) · owner · target completion date · draft story requirement.
3. Any safe quick fixes applied (within the change-control limits below).

## Audit boxes in scope (all 7 reviewed)
Every box on the Database tab is reviewed — the first is the scope, the other six are the quality audits:
1. Active Database CI Count — 3,113 (the scope/denominator — validated first, not a gap audit)
2. Database – Missing CI Owner — 10
3. Database – Missing Value Stream (Business Unit) — 3,113
4. Database – Missing Support Group — 15
5. Database – Missing Environment — 1,187
6. Database – SOX Type is Empty — 75
7. Database – Missing Approval Group — 3,110

> **Validate the extreme results first** — most likely either a real, large gap *or* a query/scoping error:
> - **Missing Value Stream = 3,113 (100% of active)** — exact match to the scope count; confirm whether Value Stream is genuinely empty on every DB CI or the audit is counting the whole class (mis-scoped).
> - **Missing Approval Group = 3,110 (~99.9%)** — near-total; same validation as above.

> **Change-control note:** databases are Discovery-driven (MS-SQL / Oracle), so some gaps may be closable via the discovery pipeline (ties enhanced DB Discovery D2.3 and credential work 1444864) — staleness/coverage is only as good as DB discovery. Confirm with Joe whether any freeze applies. "Safe quick fixes" are dashboard/query corrections and data fixes cleared with the PO + change control; mass record edits are logged as a story.
