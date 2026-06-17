---
type: team-artifact
workspace: Work
project: CMDB-CSDM
pi: PI-2
updated: 2026-06-12
tags: [work, cmdb-csdm, backlog, board-snapshot]
---

# PI-2 Board Snapshot — 2026-06-11

Source: ADO board (current view), provided 2026-06-11. **Stage is factual (board truth).**
Objective grouping in brackets is **inferred from titles** — verify before using in leadership reporting.

> ⚠️ Not yet reflected in the leadership deck. Held pending resolution of the gaps in "Open Questions" below.

> 🕒 **Superseded by the 6/12 12:00pm story pull on these items:** 1407572 is **Validation** (not Done) → this snapshot's "Done/Closed (2)" is unreliable, and 1413033's Done is unconfirmed (absent 6/12); Qualys 1428703 & 1428704 are **Active + Blocked** (vendor approval, Issue 1465952), not Validation; SCCM 1403762/1403763/1403760 advanced to Validation. See the traceability doc's "6/12 12:00pm story pull" notes for the authoritative set.

## Items by Stage (31 total)

### 🔵 New / Defining (1)
- 1402559 — Compare CI Class sources  _[P1 Discovery]_

### 🟡 Ready (2)
- 1403725 — Impact assessment of Discovery & integration touchpoints (mid-servers, schedules, sources)  _[P1]_
- 1411237 — Review & Validate CMDB Dynamic IRE Behaviour Post-Australia Upgrade  _[P1]_ ← was worksheet "IRE Validation"

### 🟠 Ready DoR (11)
- 1339116 — Define process to monitor/update CI owners who have left PPL  _[P1 — data quality/ownership]_
- 1470837 — Analyze CMDB health indicators for 35 principal classes  _[P2 Data Cert? inferred]_
- 1402555 — Identify CI classes for group 1  _[P1]_
- 1403733 — Identify deprecated plugins/features impacting CMDB  _[P1]_
- 1234585 — Qualys: Define & Configure Data Scope and Import Views (bidirectional)  _[P4 Qualys]_
- 1436576 — NowAssist: Confirm Platform Prerequisites (Part 1)  _[P5]_
- 1436579 — NowAssist: Activate Now Assist for CMDB Plugin  _[P5]_
- 1436592 — NowAssist: Activate CI Summarization Skill  _[P5]_
- 1436593 — NowAssist: Activate Contextual CI Form Help Skill  _[P5]_
- 1454371 — Extract servers without Support Groups and validate routing  _[P1]_
- 1435307 — Data Certification Pilot changes  _[P2 Data Cert]_

### 🔥 Active (8)
- 1420244 — ESS-02 Policy and CMDB Alignment  _[P4 NERC-CIP/ESS]_
- 1421790 — Gap analysis for Servers (Linux & Windows)  _[P1]_
- 1403763 — SCCM Server Hardware & Software Attribute Data Precedence  _[P1]_
- 1403762 — SCCM Servers – Last Time Seen Timestamp Alignment  _[P1]_ ← was "blocked", now Active
- 1403760 — SCCM Servers – Domain & Network Attribute Data Precedence  _[P1]_
- 1387236 — Discovery: Install AIM API on PROD MID Servers  _[P1]_
- 1444864 — Fix credentials for Servers, Databases and Network  _[P1]_
- 1455858 — Computers – Virtual – Location Management Solution  _[P1]_

### 🟣 Validation (7)
- 1428704 — Configure Qualys integration for CMDB to Qualys (Part 2)  _[P4 Qualys]_
- 1428703 — Install Qualys plugin on dev/test/prod (Part 1)  _[P4 Qualys]_
- 1355167 — Define solution for migrating Business App to Service Instance  _[P3 Service Mapping]_
- 1418610 — Airlift to Azure Pre-Migration  _[P0]_
- 1418618 — Airlift to Azure During Migration  _[P0]_
- 1418621 — Airlift to Azure Post-Migration  _[P0]_
- 1403759 — SCCM Servers – Remove SCCM Attributes  _[P1]_ ← was "on hold", now Validation

### ⚪ Done / Closed (2)
- 1413033 — Import user location values in sys_user  _[P1]_
- 1407572 — Auto Populate CI Owner/Support Group/Technical Owner Group for Virtual Computers  _[P1]_

## Reconciliation by Objective (inferred mapping)

| Objective | Total | Done | Validation | Active | Queued |
|-----------|-------|------|-----------|--------|--------|
| P0 Airlift | 3 | 0 | 3 | 0 | 0 |
| P1 Discovery / SCCM | 17 | 2 | 1 | 7 | 7 |
| P2 Data Certification | 2 | 0 | 0 | 0 | 2 |
| P3 Service Mapping | 1 | 0 | 1 | 0 | 0 |
| P4 Regulatory / Qualys / ESS | 4 | 0 | 2 | 1 | 1 |
| P5 NowAssist | 4 | 0 | 0 | 0 | 4 |
| **Portfolio** | **31** | **2** | **7** | **8** | **14** |

## Changes vs. prior provisional assumptions
- 1403762 (SCCM timestamp): blocked → **Active** (approval gate cleared)
- 1403759 (SCCM remove attrs): on hold → **Validation**
- NowAssist (1436576/79/92/93): blocked/Karen → **Ready for Dev** (unblocked)
- **2 stories Done:** 1413033 (user location), 1407572 (auto-populate CI owner — virtual)

## Validation worksheet — IDs now resolved
- "IRE Behavior Validation Post-Upgrade" → **1411237** (Ready)
- "CI Auto-Population (virtual)" → **1407572** (Done)
- "User location import / LDAP fix" → **1413033** (Done)

## Addendum — items from 6/11 11:30am type-grouped view (not in original 31-item board pull)

These surfaced in a work-item-type-grouped ADO view and were not in the stage pull above. Listed separately so the 31-item counts stay board-true.

- **1465952** — Issue: Qualys Plugin Replacement Awaiting Vendor Approval — 🔥 Active — Rich Santillo  _[P4 Qualys]_ — **risk; may gate 1428703 install**
- **1436581** — Spike: NowAssist Establish CMDB Health Baseline Score (Last Part) — 🟠 Ready DoR — 2 pts — parent **1436574**  _[P5]_
- **1451930** — Feature: Now Assist Duplicate CI Elimination (Phase 2) — 🔵 New  _[P5 / PI-3]_
- **1383493** — Dependency: Date Mapping from App PoC – EndPoint (Credentials Support) — 🔵 New — John Benedict Ortega  _[P3 Service Mapping]_
- **1383515** — Dependency: Cyber Security Team Coordination – NERC CIP — 🔵 New — Sonika Das  _[P4 NERC-CIP]_

**Feature ID resolved:** "Update Operational Monitoring Activities P2" = **1355888** (was unconfirmed).
**Feature ID confirmed:** NowAssist parent = **1436574** (Foundation & Readiness…), owner Joe Dames, Ready.

## Open Questions (block leadership-deck refresh)
1. **Service Mapping wave stories** (1380747 MV90, 1281161 WATT, 1380757 RIE, 1400703 Vault, spikes 1420634/1326754) are **not on this board**. Separate board/area path, closed, or out of filter?
2. **Data Cert dashboard 1402727** ("UAT signed off, PROD Jun 23") not on this board — closed or tracked elsewhere?
3. **Airlift server-class auto-populate 1416384** not listed (only virtual version 1407572, now Done) — superseded?
4. Confirm inferred objective mapping for: 1339116, 1470837, 1444864, 1355167.
