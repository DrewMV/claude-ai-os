---
type: ceremony
ceremony: pi-planning
pi: PI-4
date: TBD
status: future
workspace: Work
project: CMDB-CSDM
attendees: [Joe Dames (PO), Alex Phan (SM), Bhushan Salsekar (TL), Tanzeel Rehman (TL), Stan Tomberg (TL), Dev Team, Sonika Das (PM), Nolan LeBlanc (RTE), Joe Dunn (Systems Architect), Business Owners]
tags: [work, safe, pi-planning, cmdb-csdm]
---

# PI Planning — PI 4

PI 4 covers Oct 28, 2026 – Feb 2, 2027 (6 iterations + IP).
PI Planning occurs during PI 3 IP Iteration (Oct 14 – Oct 27, 2026).

## PI Objectives — CMDB-CSDM

_Candidates pre-populated from CO7 (AP00105-5 v3). ADO IDs and owners from the official ADO list as of 2026-10-08. Confirm commitments at PI Planning._

| # | ADO ID | Objective | Owner | Business Value | Committed |
|---|--------|-----------|-------|---------------|-----------|
| 1 | 1639022 | Network Gear Inventory — POC 1 integration by Dec 31; POC 2 integrations by Feb 2 | M. Vazquez | CMDB as authoritative source for non-NERC CIP network gear | TBD |
| 2 | 1639027 | Service Mapping — 30 app maps + automated notifications by Dec 31; 15 more by Feb 2 | A. Griffis | End-to-end visibility of business services and infrastructure dependencies | TBD |
| 3 | 1639072 | CMDB Adoption — campaign content developed and rolled out by Feb 2 | M. Vazquez | PPL users understand and use the CMDB effectively | TBD |
| 4 | 1639075 | CMDB Lifecycle Management — retirement rules + catalog items by Dec 31; server lifecycle flows by Feb 2 | M. Vazquez | Automated, accurate CI lifecycle management reduces data debt | TBD |

## Features Committed This PI

From the official ADO list as of 2026-10-08, with gates realigned to **SOW AP00288** (2026-10-12). Sprint assignments derived from ADO Start Date on each feature.

| ADO ID | Feature | Obj | Owner | Sprint | Start | SOW | AP00288 gate |
|--------|---------|-----|-------|--------|-------|-----|--------------|
| 1639206 | Network Inventory Integration POC — SolarWinds | 1 | A. Griffis | 4.1 | Oct 28 | D1 | Dec 31, 2026 |
| 1639225 | Network Inventory Integration POC — Cisco Catalyst | 1 | A. Griffis | 4.3 | Nov 25 | D2 | Feb 2, 2027 |
| 1639239 | Network Inventory Integration POC — Qualys | 1 | A. Griffis | 4.4 | Dec 9 | **none** | ⚠ no contract deliverable |
| 1642237 | 30 Priority Business App Service Maps — Built & Validated | 2 | A. Griffis | 4.1 | Oct 28 | **D3 + D4** | ⚠ **Nov 30** + Dec 31, 2026 |
| 1642240 | Automated CI-Impact Notifications (Incidents & Change Requests) | 2 | A. Griffis | 4.3 | Nov 25 | D6 | Dec 31, 2026 |
| 1642332 | 15 Additional Priority App Service Maps | 2 | A. Griffis | 4.4 | Dec 9 | D5 | Feb 2, 2027 |
| 1639308 | CMDB Adoption Campaign — Content, Training & Communications | 3 | M. Vazquez | 4.2 | Nov 11 | D7 | ⚠ **Jan 30, 2027** |
| 1639335 | CI Retirement Monitoring Rules (Staleness, Orphans, Duplication) | 4 | M. Vazquez | 4.1 | Oct 28 | D8 | Dec 31, 2026 |
| 1640795 | Catalog Item — Non-Discoverable CI Attribute Updates | 4 | M. Vazquez | 4.2 | Nov 11 | D9 | Dec 31, 2026 |
| 1640805 | Server Build Lifecycle Process Flow | 4 | M. Vazquez | 4.3 | Nov 25 | D10 | Feb 2, 2027 |
| 1640819 | Server Decommission Lifecycle Process Flow | 4 | M. Vazquez | 4.4 | Dec 9 | D11 | Feb 2, 2027 |
| 1640844 | Catalog Item — Service Map Update Requests | 4 | M. Vazquez | 4.6 | Jan 6 | D12 | Feb 2, 2027 |

Sprint load: 4.1 = 3, 4.2 = 2, 4.3 = 3, 4.4 = 3, 4.5 = 0 (holiday), 4.6 = 1, 4.7 IP = 0.

Owner load: A. Griffis 6, M. Vazquez 6. A. Griffis is 50% allocated.

**Three ADO items need action before PI Planning:**
1. **1642237 must split** — AP00288 D3 (15 maps, Nov 30) and D4 (15 maps, Dec 31) are separate deliverables. One 30-map ADO feature cannot evidence both.
2. **1639308 gate moved** — Feb 2, 2027 → Jan 30, 2027.
3. **1639239 has no contract home** — AP00288 requires 2 of 3 integrations; this is a third.

Changed from the Oct 5 backlog view: 1639308 moved Dec 9 → Nov 11 (Sprint 4.4 → 4.2), and 1517655 dropped off the list entirely.

## AP00288 invoicing against deliverables

| Invoice month | Deliverables | Fee |
|---|---|---|
| Nov 2026 | D3 | $478,197 |
| Dec 2026 | D1, D4, D6, D8, D9 | $505,885 |
| Jan 2027 | D7 | $493,794 |
| Feb 2027 | D2, D5, D10, D11, D12 | $47,950 |
| **Total** | | **$1,525,826** |

Revenue is heavily front-loaded — February covers five deliverables for 3% of the fee. The Nov 30 gate alone carries 31% of contract value.

## Risks Identified

| # | Risk | Likelihood | Impact | Mitigation | Owner |
|---|------|-----------|--------|-----------|-------|
| 1 | Holiday capacity (4.5: Dec 23–Jan 5) | High | Medium | Reduced sprint commitment; no ceremonies Dec 25 / Jan 1 | Alex Phan |
| 2 | A. Griffis owns 6 of 12 features at 50% allocation | Medium | High | Confirm capacity at PI Planning; consider reassignment or deferral | M. Vazquez |
| 3 | Objective 1639022 owned by M. Vazquez, all 3 features owned by A. Griffis | Low | Medium | Clarify delivery accountability for the objective at PI Planning | M. Vazquez |
| ~~4~~ | ~~Nov 30 gate not separately evidenced in ADO~~ | — | — | ✅ Closed 2026-10-12 — split done, 1646517 created for D3 | M. Vazquez |
| ~~5~~ | ~~1639239 (Qualys) outside AP00288 scope~~ | — | — | ✅ Closed 2026-10-12 — deferred to PI-1 2027 | M. Vazquez |
| 7 | Qualys has no contract vehicle — PI-1 2027 starts after AP00288 expires (Feb 2, 2027), and a third integration was never contracted | Medium | Medium | Include in the follow-on SOW scope discussion, or it goes unfunded | M. Vazquez |
| 8 | D7 (Adoption Campaign, 1639308) runs Nov 11 – Jan 19 through the holiday sprint, 11-day buffer to its Jan 30 gate, carries the $493,794 January invoice | Medium | High | Tightest margin in the PI — track weekly from Sprint 4.4 onward | M. Vazquez |
| 6 | Three-business-day deemed acceptance on all deliverables | Low | Medium | Track delivery notifications; confirm PPL reviewer availability per gate | M. Vazquez |

## Dependencies Identified

| # | Description | Depends On | Iteration Needed | Status |
|---|-------------|-----------|-----------------|--------|
| | | | | |

## Vision / Context from Business Owners

_Fill in at PI Planning._

## ART PI Objectives (CMDB-CSDM contribution)

_Fill in at PI Planning._
