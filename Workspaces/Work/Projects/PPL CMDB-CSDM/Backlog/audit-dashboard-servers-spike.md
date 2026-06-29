---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: reference-draft
scope: NON-SOW
updated: 2026-06-23
tags: [work, cmdb-csdm, backlog, quality-governance, spike]
---

# Audit Dashboard Accuracy & Gap Remediation Plan — Spike (Servers tab)

> **🟢 RECONCILED with ADO (6/29).** Created as Spike **1480112** — "Validate Servers Audit Dashboard Scope & Build a Compliance-Prioritized Gap Remediation Plan" · Owner **Anthony de Araujo** · Iteration **2.4** · State **Ready DoR**. This file remains the working reference; reconcile further changes back here. ADO is authoritative.
> **Built from** [[audit-dashboard-spike-template]] · sibling of [[audit-dashboard-accuracy-spike]] (Business Application tab).

---

## Title
[Spike] Validate Servers Audit Dashboard Scope & Build a Compliance-Prioritized Gap Remediation Plan

## Iteration / dates
PI-2 · Iteration 2.4 — Target completion 2026-06-30 (front-load at start of 2.4).

## Context / Problem statement
The Servers audit dashboard reads directly from CMDB production. The data quality of the active server population (15,218) is in question, and — most importantly — there is no documented plan to close the gaps each audit surfaces. The numbers are already being used for governance reporting, with very high gap rates on several audits (Missing Value Stream ~100%, Missing Environment ~77%, Missing IP Address ~57%, Missing Location ~56%). We need to confirm the scope is accurate, then turn each audit into an owned, dated, costed remediation action.

## Spike statement (hypothesis to resolve)
As the CMDB Configuration Management Process Owner, I want the active-server scope validated and a compliance-prioritized remediation plan — with owner, target completion date, and solution type (automated / manual / other) — built for every audit gap, so that server data quality can be governed to target and the team has an actionable, time-bound plan instead of raw counts.

## Outcome / deliverable
A Gap Remediation Plan for the Servers tab:
1. Scope validation result for Active Servers Count (15,218).
2. One remediation row per audit, ordered by compliance priority, each with: what it measures · gap root cause · solution type (automated / manual / other) · owner · target completion date · draft story requirement.
3. Any safe quick fixes applied (within the change-control limits below).

## Audit boxes in scope (all 12 reviewed)
Every box on the Servers tab is reviewed — the first is the scope, the other eleven are the quality audits:
1. Active Servers Count — 15,218 (the scope/denominator — validated first, not a gap audit)
2. Server – Missing CI Owner — 0
3. Servers – Missing Support Group — 97
4. Servers – Missing IP Address — 8,643
5. Server – Missing Serial Numbers — 6,020
6. Servers – Missing SOX Type — 42
7. Servers – Missing Technical Owner Group — 0
8. Servers – Missing Location — 8,587
9. Server – Classification is Empty — 379
10. Servers – Missing Value Stream (Business Unit) — 15,218
11. Servers – Missing Asset Tag — 3,351
12. Server – Missing Environment — 11,665

> **Validate the extreme results first** — they are the most likely to be either a real, large gap *or* a query/scoping error:
> - **Missing Value Stream = 15,218 (100% of active)** — equals the scope count exactly; confirm whether Value Stream is genuinely unpopulated for all servers or the audit is counting the whole class (mis-scoped).
> - **Missing CI Owner = 0** and **Missing Technical Owner Group = 0** — confirm these are truly clean (auto-populated by Discovery/SCCM) and not a broken/empty query returning zero.

> **Change-control note:** unlike Business Applications, servers are Discovery/SCCM-driven, so many gaps may be closable via the existing source pipelines (precedence rules 1348712/716/717, credential work 1444864, server support-group assignment work with Ray Reuter). Confirm with Joe whether any freeze applies before any quick fix. "Safe quick fixes" are dashboard/query corrections and data fixes cleared with the PO + change control; mass record edits are logged as a story.
