---
type: leadership-brief
workspace: Work
project: PPL CMDB-CSDM
pi: PI-2
updated: 2026-06-23
tags: [work, cmdb-csdm, leadership-status, co5, scope]
---

# PI-2 Status Update — CO5 Alignment & Deliverable Health

**To:** CMDB-CSDM Leadership · **From:** Manuel Vazquez (SM / PO Support)
**As of:** Jun 23, 2026 — Iteration 2.3 close · ADO pull 6/23

---

## Bottom Line

- **About a third of the delivery effort we've spent through Sprint 2.3 went to work that isn't in CO5.** That holds up whichever way I measure it: ~**30% by story/spike count**, ~**33% by points**. Airlift by itself is two people for the whole sprint on work that needs a change order.
- **Point tracking this PI is uneven** — only ~74% of user stories are pointed, and the tasks that make up most of Service Mapping aren't pointed at all. So I'm leading with a count of stories and spikes and using points only as a cross-check. The headline doesn't rest on the points either way.
- **All three CO5 deliverables are due June 30, a week out.** Four hard gaps are still open, and the **$533,775 holdback** depends on accepting them.
- The added work, Airlift and NowAssist, has been absorbed into the team's capacity **with no change order**. CO5 Article 2 says scope changes have to be in writing.

---

## 1. PI-2 effort out of scope for CO5 — through Sprint 2.3

> **Why I'm counting items, not just points:** point tracking this PI is uneven. Only **29 of 39 user stories (74%)** carry points, and **tasks** — the biggest category of work, and nearly all of Service Mapping — don't carry points at all by design. Measure by points alone and you miss most of what the team actually worked. So the main view below counts stories and spikes; points are there to back it up. This is Iterations 2.1–2.3 only, since 2.4–2.6 haven't run yet.

**Both ways of counting land in the same place: about 30–33% out of scope.**

| Measure (through Sprint 2.3) | Out of scope for CO5 |
|---|---|
| **By story / spike count** | ~15 of ~51 ≈ **30%** |
| **By story points** | 24 of 72 ≈ **33%** |

### Primary view — by story / spike count

| Category | Stories + Spikes | Share |
|---|---|---|
| In-scope — CO5 deliverables (18 stories + 6 spikes) | 24 | |
| In-scope — Service Mapping (8 + 1) | 9 | |
| **In-scope subtotal** | **33** | **~65%** |
| Out — **Airlift** (4)¹ · **NowAssist** (5) · **Qualys build** (2) · **Network Gear** (2) · Sailpoint / Moveworks (2) | **15** | **~30%** |
| Borderline — Operational Monitoring (2 + 1) | 3 | ~6% |
| **Total** | **~51** | |

¹ *Airlift's 4 stories sit past the export slice but are counted per the flagged 2-resource Sprint-2.3 effort.*

### Corroborating view — by story points

| Out-of-scope stream | Pts | Items | Status |
|---|---|---|---|
| **Airlift / VMware→Azure** (P0 · Feat 1420613) | **16** | 1418610 / 18 / 21 + 1416384 *(unpointed; 16 = 2 resources × S2.3)* | 3 Validation · 1 Active |
| **NowAssist AI** (P5 · Feat 1436574) | **6** | 1436576, 1436579, 1436592, 1436593 + 1470837 health spike | Mostly Resolved / Validation |
| **Qualys *build*** (P4 · beyond CO5 requirements) | **2** | 1428703, 1428704 | **BLOCKED** — vendor plugin (Issue 1465952) |
| **Out-of-scope subtotal** | **24** | vs **48** in-scope (CO5 35 + Service Mapping 13) | |

> **Both numbers are floors.** Network Gear (CO6), NERC-CIP, and Upgrade Analysis are out of scope too, but they're mostly unpointed, so they barely show up in the points column. The in-scope side is undercounted as well: a few pointed 2.3 stories (SCCM Server precedence, 1454371, 1387236, ~7 pts) landed after my export slice. Add those and in-scope rises, which pushes out-of-scope a bit under 30%.

---

## 2. CO5 deliverable status — all due June 30, 2026

Accepting these three deliverables is what releases the **$533,775 holdback**.

| Deliverable | Sub-item | Due | RAG | Status / evidence |
|---|---|---|---|---|
| **1. Governance** | 1.1 Data Dictionary — Servers | Jun 30 | 🟡 | Feat 1354797 Ready; 1421790 Validation; 1454371 Active |
| | 1.1 — Computers | Jun 30 | 🟡 | 1313400 Resolved; 1399547 / 1455858 Validation |
| | 1.1 — Business Apps | Jun 30 | 🟡 | 1475584/585/582, 1478286, 1474892 — New / Refinement (early) |
| | 1.1 — **Databases [G1]** | Jun 30 | 🔴 | **HARD GAP** — no dedicated DB data-dictionary story |
| | 1.2 Data Certification | Jun 30 | 🟢 | Dashboard 1402727 UAT signed (6/10), PROD 6/23; 1435307 Resolved |
| | 1.3 ESS-02 Alignment | Jun 30 | 🟡 | Spike 1420244 Active — analysis only; parent feature 1406668 Removed |
| | 1.4 SOX BA review *(SOX only, not NERC/CIP)* | Jun 30 | 🟡 | Issue 1438967 Closed/approved; notification 1455827 in **Iter 2.5 (post-deadline)** |
| | 1.5 Monthly CCB + future backlog | Jun 30 | 🔴 | Cadence running (CCB 6/16) but stories 1406672/683/687 sit under **Removed** feature 1406668 |
| **2. Automated Data Ingestion** | 2.1 Computers — SCCM/Discovery precedence | Jun 30 | 🟢 | 1348712/716/717 Resolved; 1348715 Validation |
| | 2.1 Computers — **90% coverage [G2]** | Jun 30 | 🔴 | **HARD GAP** — no coverage-measurement story |
| | 2.1 Computers — bulk Lifecycle | Jun 30 | 🟢 | 1402790 Closed |
| | 2.2 Servers — SCCM/Discovery precedence | Jun 30 | 🟢 | 1403759/760/762/763 Validation |
| | 2.2 Servers — credentials enabling discovery | Jun 30 | 🟡 | 1444864 Validation; child tasks still Active |
| | 2.2 Servers — **90% non-NERC-CIP coverage [G3]** | Jun 30 | 🔴 | **HARD GAP** — no coverage-measurement story |
| | 2.2 / 2.3 Servers & DB SOX indicators | Jun 30 | ⚪ n/a | **Manual per CO5** — excluded from automation |
| | 2.3 Databases — enhanced MS-SQL/Oracle Discovery | Jun 30 | 🟡 | Task-level only (creds under 1444864); no standalone deliverable story |
| **3. Other Enhancement** | Evaluate 1 integration (Qualys) | Jun 30 | 🟡 | Requirements 1234585 Ready; **build BLOCKED** (1428703/704, Issue 1465952) |

**Scorecard:** 4 🟢 · 8 🟡 · 4 🔴 · 1 n/a. The four reds are where acceptance is at risk: the **Databases data dictionary (G1)**, **90% coverage measurement for Computers and Servers (G2/G3)**, and **CCB evidence sitting under a feature marked Removed (1.5)**.

> **Also in scope, but not a holdback-gated CO5 deliverable: Service Mapping.** It's contracted under a prior CO and shows up in CO5 only in the PO role description on p.4, not the deliverables table. 🟡 Maps are moving (~13 pts pointed through 2.3), but about 36 map tasks are stranded in 2.1/2.2 carryover and Waves 20–21 are empty.

---

## What we need from leadership

1. **A change-order decision on the added work.** Airlift (P0) and NowAssist are ~22 of the 24 out-of-scope points already spent through Sprint 2.3. CO5 Article 2 requires a **written change order** for scope changes, and right now this is being absorbed into a back half (Sprints 4–5) that's already at 100% capacity.
2. **Sign CO6 before July 1.** CO6 re-baselines the at-risk CO5 items — **Databases, 90% coverage, Qualys** — to Jul 31 / Oct 30. If it isn't signed, the **June 30 deadline and the $533,775 holdback stand with no relief**.
3. **Close or re-home the three hard gaps:** G1 (DB data dictionary) and G2 / G3 (coverage measurement). Either deliver them by 6/30 or move them into CO6.
4. **Fix CCB feature 1406668** — un-Remove it or re-parent the stories — so the Deliverable 1.5 evidence isn't filed under a dead feature.
5. **A ruling on SOX story 1455827.** It's in Iteration 2.5 right now, which falls after the 6/30 deadline.

---

### Data provenance & caveats

- **Basis:** the 6/23 ADO export, Iterations 2.1–2.3 only (2.4–2.6 haven't run). Story/spike count is the primary measure; points corroborate.
- **Inconsistent point tracking (the key limitation):** 29 of 39 user stories (74%) are pointed, spikes are tracked well, and tasks and features carry no points by design. Tasks are the largest category of work and nearly all of Service Mapping. That's why count, not points, is the primary basis.
- **Airlift** isn't pointed in ADO. Its 16 pts / 4 stories reflect the 2-resource Sprint-2.3 effort, not ADO values.
- **These are floors, not ceilings.** Out-of-scope leaves out the largely-unpointed Network Gear, NERC-CIP, and Upgrade Analysis; in-scope leaves out ~7 pts of 2.3 stories past the export slice. The real out-of-scope share is probably **a little under 30%**.
- **Operational Monitoring** (3 items / 3 pts) is flagged pending a ruling. If it's ruled out of scope, out-of-scope rises to ~35% by count / 36% by points.
- **Service Mapping** counts as in-scope committed work per your direction, but it's **not** one of CO5's three holdback-gated deliverables.
