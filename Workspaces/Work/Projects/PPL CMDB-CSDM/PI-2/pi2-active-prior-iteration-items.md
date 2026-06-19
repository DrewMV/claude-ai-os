---
type: team-artifact
workspace: Work
project: CMDB-CSDM
pi: PI-2
updated: 2026-06-17
tags: [work, cmdb-csdm, pi-planning, iteration-review]
---

# PI-2 — Active Work Items in Prior Iterations (2.1 / 2.2)

> **Also known as: the "clean-up list."**

**Purpose:** iteration-review hygiene — work items still in **Active** state that are parked in a *previous* iteration (2.1 or 2.2) rather than the current **2.3** (Jun 10–23). Each owner should confirm: close it, re-sprint to 2.3, or it's genuinely still in progress.

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

**Totals:** 6 tasks · 3 features · 1 spike · 3 dependencies = **13 confirmed** (objectives excluded — they carry no iteration).

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
