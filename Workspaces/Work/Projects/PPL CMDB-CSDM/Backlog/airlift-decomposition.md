---
type: team-artifact
workspace: Work
project: CMDB-CSDM
pi: PI-2
updated: 2026-07-08
tags: [work, cmdb-csdm, pi-planning, backlog]
---

# Airlift to Azure — Story Decomposition Tracker

**Live worksheet.** Record child stories here **as the decomposition takes place**, then reconcile back to ADO. Parent traceability lives in [[pi2-objectives-features-stories]] (Feature 1420613, 7/8 note); stranded-item flag in [[pi2-active-prior-iteration-items]].

## What we're doing

Three phase-sliced stories under Feature **1420613 — CMDB Support for Air Lift** (PI Obj 0, BV 10, **P0**) are stranded in **2.3** with no visible progress. We are breaking each into smaller vertical stories that **document the actual CMDB migration work of the last 4 weeks**, placing each child in the sprint where the work happened, at its true state.

**Rules (all must hold before an original is closed):**
1. Each child = **one concrete activity** with an acceptance criterion.
2. Each child sits in the sprint where the work **actually occurred** — 2.3 / 2.4 / 2.5 — at its **true state**.
3. Child points **sum exactly to the parent budget**: Pre = **10**, During = **8**, Post = **12** (30 total).
4. Once children carry the scope, **close the original** (or convert it to a feature) so points aren't double-counted.
5. Feature 1420613 advances out of **Defining** once its children carry the state.

**Sprints:** 2.3 = Jun 10–23 (closed) · 2.4 = Jun 24–Jul 7 (closed) · 2.5 = Jul 8–21 (current)
**States:** ⚪ New · 🔵 Active · 🟣 Validation · ✅ Done/Closed

**Row format (example — delete when filling):**
`| 1 | Tag in-scope VMware CIs for airlift | 2.3 | ✅ Done | 3 | Alex Lim | 14xxxxx | Query returns agreed server set; each flagged airlift-scope |`

---

## Reconciliation summary

| Parent | ADO ID | Budget | Allocated | # Children | Reconciles? | Original closed/converted? |
|--------|--------|--------|-----------|-----------|-------------|----------------------------|
| Pre-Migration | 1418610 | 10 | 0 | 0 | ☐ | ☐ |
| During Migration | 1418618 | 8 | 0 | 0 | ☐ | ☐ |
| Post-Migration | 1418621 | 12 | 0 | 0 | ☐ | ☐ |
| **Total** | — | **30** | **0** | **0** | ☐ | — |

---

## Pre-Migration — parent 1418610 · budget 10 pts · owners Laurent / Alex Lim

| # | Child story (activity) | Sprint | State | Pts | Owner | ADO ID | Acceptance criterion |
|---|------------------------|--------|-------|-----|-------|--------|----------------------|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |

**Allocated: 0 / 10**

## During Migration — parent 1418618 · budget 8 pts · owner Alex Lim

| # | Child story (activity) | Sprint | State | Pts | Owner | ADO ID | Acceptance criterion |
|---|------------------------|--------|-------|-----|-------|--------|----------------------|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |

**Allocated: 0 / 8**

## Post-Migration — parent 1418621 · budget 12 pts · owners Laurent / Alex Lim

| # | Child story (activity) | Sprint | State | Pts | Owner | ADO ID | Acceptance criterion |
|---|------------------------|--------|-------|-----|-------|--------|----------------------|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |

**Allocated: 0 / 12**

---

## Decomposition log

Record refinement/creation events here as they happen (date — what changed — by whom).

- **7/8** — Tracker created. Points confirmed Pre 10 / During 8 / Post 12. Refinement to be scheduled with Laurent / Alex Lim + Joe (PO) + Stan (Discovery). No child stories created yet.
- **7/8** — Evidence sources identified from this week's Airlift comms (see [[weekly-activity-reference-2026-07-08]]): **Airlift_VS_CriticalApplicationRequirements** (Joe, Excel), **Airlift Application Owners & CMDB** (email + Teams), **Daily Dependency & Execution Touchbase** (daily), **Airlift Plan Sync** (Jordan Yung). Sprint-placement context: Airlift **ran in 2.3, paused in 2.4** (CO5 reprioritization — [[pi2-iteration-activity]], 6/29), **resuming in 2.5**. Draw child activities from these artifacts, then confirm actual work + sprint with Laurent / Alex Lim.
- **7/8** — ⚠️ **Possible-postponement flag.** The 7/7 Go Green deck lists Airlift as "temporary pause (6/24)" with **"Possible Postponement."** Confirm with Joe / Jordan / Sonika whether Airlift continues in PI-2 or shifts to **PI-3 / CO6**. Impact: this changes sprint placement for any **future** child stories only — documenting the **last 4 weeks of already-completed work** (in 2.3 / 2.4) stands regardless. See [[weekly-activity-reference-2026-07-08]] §1.
