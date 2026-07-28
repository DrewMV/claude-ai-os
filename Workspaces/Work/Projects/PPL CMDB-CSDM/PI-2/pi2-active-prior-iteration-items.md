---
type: team-artifact
workspace: Work
project: CMDB-CSDM
pi: PI-2
updated: 2026-07-21
tags: [work, cmdb-csdm, pi-planning, iteration-review]
---

# PI-2 — Active Work Items in Prior Iterations (2.1 / 2.2)

> **Also known as: the "clean-up list."**

**Purpose:** iteration-review hygiene — work items still in **Active** (or non-closed) state that are parked in a *previous* iteration rather than the current active sprint.

> 🔄 **Transition: 2.4 → 2.5 (7/7).** Iteration 2.4 closes today (Jul 7). Iteration 2.5 opens Jul 8. Final ADO closeout grid expected today/tomorrow — this file will be updated with any 2.4 items that did not close and are not yet re-sprinted into 2.5. Prior-iteration frame now spans **2.1 / 2.2 / 2.3 / 2.4**. Each owner should confirm: close it, re-sprint to 2.3, or it's genuinely still in progress.

> **Living document.** Kept in sync with [[pi2-objectives-features-stories]] — update whenever work items are reconciled against ADO. Source: ADO grids reviewed as of the `updated` date; may not reflect query pages not yet seen.

---

## Inventory

### Tasks (6) — all parent 1444864 "Fix Credentials for Servers, Databases and Network", Iter 2.2
| ID | Title | Owner |
|----|-------|-------|
| 1445257 | Configure CSDISCOVERY credential (Linux) | Stan |
| 1445274 | Test Linux Server discovery w/ CSDISCOVERY | Stan |
| 1445306 | Configure GWIZ_MON_ORACLE_DB_PA credential | Stan |
| 1445202 | Configure MID servers (`mid.dns.resolver`) | Stan |
| 1445239 | Test Discovery after MID reconfig | Stan |
| 1445339 | Test PA Oracle DB discovery | Anthony |

> ⚠️ Parent story 1444864 is marked **Validation**, but still has these 6 Active child tasks open in 2.2. Confirm true status — gates discovery for P1/P3 and Service Mapping.

### Features (3)
| ID | Title | Iter | Owner |
|----|-------|------|-------|
| 1247179 | Data Certification Pilot - Functionality | 2.1 | Anuradha Rai |
| 1354794 | Computer Class Data & Form Improvements | 2.1 | — |
| 1356826 | SCCM Server Class Precedence Updates | 2.2 | — |

### Spikes (1)
| ID | Title | Iter | Owner |
|----|-------|------|-------|
| 1326754 | Evaluate Automated Service Mapping via Endpoint-Based Discovery | 2.2 | Tanzeel |

### Dependencies (3)
| ID | Title | Iter | Owner |
|----|-------|------|-------|
| 1420565 | End User Location Mapping for Physical Computer CIs | 2.1 | Sonika Das |
| 1383519 | Qualys Development / Support Team | 2.2 | Rich Santillo |
| 1416953 | Cloud Migration Impact to CMDB Data Accuracy & Change Coordination | *(Active, no iteration set)* | Alex Phan |

### Stories — confirmed clear ✅
Reviewed the ADO Iteration 2.3 story grid on 6/17: all 19 stories are in **2.3** (current), so **no Active story is stranded in 2.1/2.2**. Re-check when a fresh story grid is pulled.

> **6/30 sync:** Iteration **2.3 closed (6/23); 2.4 is now active** (Jun 24 – Jul 7). The 6/30 ADO pull was a **2.4-only board grid** — it surfaced **no new 2.1/2.2 stranded items**, so the inventory below stands. Note the "prior iteration" frame now spans **2.1/2.2/2.3**; a 2.1–2.3-inclusive grid is still needed to re-confirm carryover. 2.4 story/spike states reconciled into [[pi2-objectives-features-stories]].
>
> **6/23 re-check:** A full grid pull (Iter 2.3→2.6) on the last day of 2.3 did **not** surface any 2.1/2.2 items in the visible rows — so the 13 prior-iteration items above were **not re-confirmed against this pull** (the pull was forward-looking, sorted 2.3↑). Their status stands from 6/17 until a 2.1/2.2-inclusive grid is pulled. No *story* appeared stranded in 2.1/2.2 in the 6/23 view. Note: parent story **1444864** still shows **Validation** in 2.3 while its 6 Active credential tasks remain in 2.2 (the core flag above is unchanged).

> **7/8 — stranded-story case (Airlift, P0) — supersedes the "confirmed clear ✅" note above.** Three stories are stranded in **2.3** (closed 6/23): **1418610** Airlift Pre-Migration (10 pts), **1418618** During (8 pts), **1418621** Post (12 pts) — all under Feature **1420613 CMDB Support for Air Lift** (P0, BV 10), owners Laurent / Alex Lim. Being **decomposed** into smaller vertical stories that document the last 4 weeks of work, re-placed into the sprint where the work happened (2.3 / 2.4 / 2.5) at true state (Done/Closed vs Active), with child points summing to 10 / 8 / 12; the three originals then closed or converted to features. Full record + plan in [[pi2-objectives-features-stories]] (Feature 1420613, 7/8 note); live child-story tracking in [[airlift-decomposition]].

> **7/15 — 2.4 closeout review.** Iteration 2.4 closed Jul 7; 2.5 is now current. ADO grid reviewed 7/15. Prior-iteration frame now spans **2.1 / 2.2 / 2.3 / 2.4**. Two items are **Active** in 2.4 (true stranded — both owned by Anthony/de Araujo): **1480112** (Spike — Validate Servers Audit Dashboard Scope & Build Compliance) and **1487872** (Story — Validate Staged Retirement Candidates). Also flagged: **1403731** (Story — Analyze impact on governance controls, Stan) is still **New** in 2.4 — never started. Multiple items remain in **Validation** in 2.4 (see 2.4 Stranded section below) — these are likely pending stakeholder sign-off, but should be confirmed closed or re-sprinted.

> **7/21 — Iteration 2.5 board reviewed (full story grid).** ADO 2.5 board pulled 7/21. Prior-iteration frame now spans **2.1 / 2.2 / 2.3 / 2.4 / 2.5**. None of the 2.4 stranded items (1480112, 1487872, 1403731, or the Validation group) appear in the 2.5 grid — confirm whether they were closed, re-sprinted into 2.5 off-screen, or still sitting in 2.4. See 2.5 Story Status section below for the full 2.5 board state.

**Totals (2.1–2.3 legacy items):** 6 tasks · 3 features · 1 spike · 3 dependencies = **13 confirmed** (objectives excluded — they carry no iteration).

---

## 2.4 Stranded Items (as of 7/15)

### Active (true stranded — action required)
| ID | Type | Title | Owner | Feature |
|----|------|-------|-------|---------|
| 1480112 | Spike | Validate Servers Audit Dashboard Scope & Build a Compliance... | Anthony (de Araujo) | Data Certification Rollout (PI2) |
| 1487872 | Story | Validate Staged Retirement Candidates | Anthony (de Araujo) | — |

### New (never started in 2.4 — re-sprint or close)
| ID | Type | Title | Owner | Feature |
|----|------|-------|-------|---------|
| 1403731 | Story | Analyze impact on governance controls, KPIs, and CMDB oper... | Stan (Tomberg) | Support ServiceNow Upgrade Analysis (PI2) |

### Validation (pending stakeholder sign-off — confirm closed or carry to 2.5)
| ID | Type | Title | Owner | Feature |
|----|------|-------|-------|---------|
| 1455832 | Spike | Servers: Recommendation on tracking environment field | Vinay | Server Class Data & Form Updates (PI2) |
| 1480111 | Spike | Validate Business Application Audit Dashboard Scope & Build... | Joe Dames | Data Certification Rollout (PI2) |
| 1480088 | Story | Data Dictionary: Servers (Windows/Linux) | Vinay | Governance Validation & Acceptance |
| 1480090 | Story | Data Dictionary: Computers (Physical/Virtual) | Bhushan | Governance Validation & Acceptance |
| 1487867 | Story | Import PA VMware Inventory into ServiceNow | Vinay | — |
| 1487868 | Story | Import KY VMware Inventory into ServiceNow | Vinay | — |
| 1487869 | Story | Import PA Physical Inventory into ServiceNow | Vinay | — |
| 1487897 | Story | Drop Custom Inventory and Staging Tables | Kiran | — |
| 1490398 | Story | Retired Servers from the Server Table | Bhushan | — |

---

## Iteration 2.5 — Full Story Status (as of 7/21)

> Source: ADO Iteration 2.5 board grid, pulled 2026-07-21.

### Features
| ID | Title | Owner | State |
|----|-------|-------|-------|
| 1354794 | Computer Class Data & Form Improvements (PI2) | — | Active _(was stranded in 2.1 — now progressing)_ |
| 1388523 | Unplanned Backlog - CMDB Workstream (PI2) | Josh Sterling | New |

### Spikes
| ID | Title | Owner | State | Points |
|----|-------|-------|-------|--------|
| 1402452 | Advanced Shipping Notification (ASN) File for Workstations from WWT – RITM0054309 | Uloma | Defining | 0 |
| 1403721 | CMDB: Analyze impact on CI class hierarchy, customizations, and class manager behavior | Stan | Refinement Ready | 3 |
| 1403723 | CMDB: Validate impact on authoritative sources, attribute precedence, and data "flapping" | Stan | Refinement Ready | 2 |

### Closed ✅
| ID | Title | Owner |
|----|-------|-------|
| 1378017 | CMDB: Populate Missing Business Owners for Business Applications | Bhushan |
| 1454371 | CMDB: Extract servers without Support Groups and validate routing | Bhushan |
| 1475582 | CMDB: Identify and Populate Missing Support Groups in Business Application CIs (496 records) | Kiran |
| 1478403 | Align the available Value Streams in ServiceNow CMDB to official value stream taxonomy (RITM0059921) | Bhushan |
| 1504305 | CMDB: Rebuild Database Audit Dashboard around Database Instances | Bhushan |
| 1506217 | CMDB: Computers Clean up and Retiring CIs | Bhushan |
| 1509864 | CMDB: Populate Value Stream values for Business app | Kiran |

### Resolved (confirm closed)
| ID | Title | Owner |
|----|-------|-------|
| 1480107 | CMDB: Monthly CCB cadence operating + future-PI backlog | Manuel |
| 1483886 | CMDB: Enforce SOX Field Dependencies on Mapped Application Services | Bhushan |

### Validation (pending sign-off)
| ID | Title | Owner |
|----|-------|-------|
| 1483893 | CMDB: Provide Form Help Text and Guidance for SOX Type Selection | Kiran |
| 1504526 | CMDB: Add new values for data classification on Business App | Kiran |
| 1506125 | CMDB: Missing IP address validation for 849 servers in Dashboard | Vinay |
| 1509863 | CMDB: Populate CI Owner for Business App | Vinay |

### Active (in progress)
| ID | Title | Owner |
|----|-------|-------|
| 1428703 | CMDB: Install x_qual5_itam_nwapp plugin on dev, test and Prod (Part 1) | Stan |
| 1480099 | CMDB: Data Certification process defined & Business App pilot validated | Joe Dames |
| 1480102 | CMDB: CMDB Alignment to ESS-02 confirmed | Manuel |
| 1512084 | CMDB: Populate Assigned to field in Computer Class | Kiran |

### Ready DoR (groomed, not yet started)
| ID | Title | Owner |
|----|-------|-------|
| 1478286 | CMDB: Business App: Populate Classification field values (approx 938 records) | Tony |
| 1504309 | CMDB: Database: Populate Environment Attribute | Stan |
| 1504314 | CMDB: Populate CI Owner | Kiran |
| 1504316 | CMDB: Database: Populate Support Group | Stan |
| 1504318 | CMDB: Database: Populate SOX Indicator | Stan |
| 1504320 | CMDB: Database Clean up: IP address and Location | Stan |
| 1508982 | CMDB: Service Catalog for New Business Application/Update Business Application | Joe Dames |
| 1511122 | CMDB: Upgrade Testing Checklist | Joe Dames |

### Refinement Ready (needs grooming)
| ID | Title | Owner |
|----|-------|-------|
| 1475584 | CMDB: Identify and Populate Missing Technical Owner Group in Business Application CIs | — |
| 1475585 | CMDB: Identify and Populate Missing Approval Groups in Business Application CI | Manuel |
| 1483891 | CMDB: Top Down SOX Compliance Data from Application Services to Infrastructure CIs | — |
| 1504299 | CMDB: ENH: Removal of field value during data certification | — |
| 1504301 | CMDB: ENH: Unassigned Tasks to Platform team | — |
| 1504302 | CMDB: ENH: Data Certification – Notification Branding and CMDB Workspace Links | — |

### New (not started)
| ID | Title | Owner |
|----|-------|-------|
| 1513103 | Additional Fields to Weekly Imports – Memory and Model ID | — |
| 1513944 | CMDB: Modify SR: SOX-Flagged CI Handling (Governed) | Joe Dames |

### Removed
| ID | Title | Owner |
|----|-------|-------|
| 1487874 | CMDB: Obtain Change Approval for CI Retirement | Manuel |

---

## Email draft (copy to share)

**Subject: PI-2 — Active work items still sitting in Iterations 2.1 / 2.2**

Hi team,

Ahead of iteration review, I pulled together the work items still in **Active** state that are parked in a previous iteration (2.1 or 2.2) rather than the current 2.3. I'd like each owner to confirm whether these should be closed, re-sprinted into 2.3, or are genuinely still in progress.

**Tasks — all under story 1444864 "Fix Credentials for Servers, Databases and Network" (Iteration 2.2):**
- 1445257 — Configure CSDISCOVERY credential (Linux) — Stan
- 1445274 — Test Linux Server discovery w/ CSDISCOVERY — Stan
- 1445306 — Configure GWIZ_MON_ORACLE_DB_PA credential — Stan
- 1445202 — Configure MID servers (mid.dns.resolver) — Stan
- 1445239 — Test Discovery after MID reconfig — Stan
- 1445339 — Test PA Oracle DB discovery — Anthony

A flag on these: the parent story 1444864 is marked Validation, but it still has six Active child tasks open in 2.2. Stan / Anthony — can you confirm the real status? This work gates discovery for the network/server classes and Service Mapping.

**Features:**
- 1247179 — Data Certification Pilot - Functionality (Iter 2.1) — Anuradha
- 1354794 — Computer Class Data & Form Improvements (Iter 2.1)
- 1356826 — SCCM Server Class Precedence Updates (Iter 2.2)

**Spike:**
- 1326754 — Evaluate Automated Service Mapping via Endpoint-Based Discovery (Iter 2.2) — Tanzeel

**Dependencies:**
- 1420565 — End User Location Mapping for Physical Computer CIs (Iter 2.1) — Sonika
- 1383519 — Qualys Development / Support Team (Iter 2.2) — Rich
- 1416953 — Cloud Migration Impact to CMDB Data Accuracy & Change Coordination (Active, no iteration set) — Alex

**One ask:** if your item above is done, please close it; if it's continuing, move it to 2.3 so the board reflects reality. I'll review the rest at our next sync.

Thanks,
Manuel
