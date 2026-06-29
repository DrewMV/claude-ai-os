---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: reference-draft
scope: NON-SOW
updated: 2026-06-23
tags: [work, cmdb-csdm, backlog, quality-governance, spike]
---

# Audit Dashboard Accuracy & Gap Remediation Plan — Spike (Computer tab)

> **🟢 RECONCILED with ADO (6/29).** Created as Spike **1480114** — "Validate Computer Audit Dashboard Scope & Build a Compliance-Prioritized Gap Remediation Plan" · Owner **Anthony de Araujo** · Iteration **2.4** · State **Ready DoR**. This file remains the working reference; reconcile further changes back here. ADO is authoritative.
> **Built from** [[audit-dashboard-spike-template]] · sibling of [[audit-dashboard-accuracy-spike]] (BA), [[audit-dashboard-servers-spike]] (Servers), [[audit-dashboard-database-spike]] (Database).

---

## Title
[Spike] Validate Computer Audit Dashboard Scope & Build a Compliance-Prioritized Gap Remediation Plan

## Iteration / dates
PI-2 · Iteration 2.4 — Target completion 2026-06-30 (front-load at start of 2.4).

## Context / Problem statement
The Computer audit dashboard reads directly from CMDB production. The data quality of the active computer CI population (28,203) is in question, and — most importantly — there is no documented plan to close the gaps each audit surfaces. The numbers are already being used for governance reporting, with very high gap rates on several audits (Missing Approval Group ~100%, Missing IP Address ~79%, Location is Empty ~62%). We need to confirm the scope is accurate, then turn each audit into an owned, dated, costed remediation action.

## Spike statement (hypothesis to resolve)
As the CMDB Configuration Management Process Owner, I want the active-computer scope validated and a compliance-prioritized remediation plan — with owner, target completion date, and solution type (automated / manual / other) — built for every audit gap, so that computer data quality can be governed to target and the team has an actionable, time-bound plan instead of raw counts.

## Outcome / deliverable
A Gap Remediation Plan for the Computer tab:
1. Scope validation result for Active Computer CI's (28,203), plus the secondary scope figure Active Virtual Computer CI's (6,530).
2. One remediation row per audit, ordered by compliance priority, each with: what it measures · gap root cause · solution type (automated / manual / other) · owner · target completion date · draft story requirement.
3. Any safe quick fixes applied (within the change-control limits below).

## Audit boxes in scope (all 13 reviewed)
Two of the boxes are scope counts (total + virtual subset); the other eleven are the quality audits:
1. Active Computer CI's — 28,203 (the scope/denominator — validated first, not a gap audit)
2. Active Virtual Computer CI's — 6,530 (secondary scope — virtual subset; validate the split, not a gap audit)
3. Computer – Missing CI Owner — 17
4. Computer – Assigned To is Empty — 8,166
5. Computer – Missing Support Group — 14
6. Computers – Missing IP Address — 22,290
7. Computers – Missing SOX Type — 0
8. Computer CI's – Missing Serial Number — 0
9. Computer – Missing Approval Group — 28,203
10. Computer CI's – Manufacturer is Empty — 332
11. Computers – Location is Empty — 17,513
12. Computers – Missing Asset Tag — 8,275
13. Computer – Operating System is Empty — 957

> **Two scope boxes — validate the split first.** Active Computer CI's (28,203) is the denominator; Active Virtual Computer CI's (6,530) is a subset. Confirm whether the audits run against the full population or should be split Physical vs Virtual — Physical and Virtual have different stakeholder groups (6/08 decision), and offline physical devices may not update.

> **Validate the extreme results first** — most likely either a real, large gap *or* a query/scoping error:
> - **Missing Approval Group = 28,203 (100% of active)** — exact match to the scope count; confirm genuinely empty for all vs mis-scoped query.
> - **Missing SOX Type = 0** and **Missing Serial Number = 0** — confirm truly clean (SCCM-populated) and not a broken/empty query returning zero.

> **Change-control note:** computers are SCCM/Discovery-driven (ties SCCM precedence 1348712/716/717/715 and retired-computer handling 1402790), so many gaps may be closable via the source pipelines rather than manual entry. Confirm with Joe whether any freeze applies. "Safe quick fixes" are dashboard/query corrections and data fixes cleared with the PO + change control; mass record edits are logged as a story.
