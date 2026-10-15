---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-4
status: draft
updated: 2026-10-14
tags: [work, cmdb-csdm, safe, pi-planning]
relationships:
  - target: "[[PI-4/pi-planning]]"
    type: derived_from
  - target: "[[PI-4/Memory]]"
    type: related_to
  - target: "[[PI-4/pi4-adoption-1639308-campaign-stories-dependencies]]"
    type: related_to
---

# PI-4 Implementation Plan — Appendix (Draft)

Source content for a **single appendix slide** behind slide 6 of `PI4-Objectives-Features-2026-10-14.pptx`. The main deck is unchanged.

**Why this exists:** project DL feedback on slides 4–6 — the sprint/commitment/program-board views show hard due dates but not the activities that have to happen to hit them. This adds phase timing, parallelism, and intermediate due dates.

---

## Phase model

Three duration bands, three point markers.

| Band | What it covers |
|------|----------------|
| **Requirements / Spike** | Discovery, spike work, requirements drafted and circulated |
| **Build & Test** | Development plus team testing — merged, because testing happens inside the sprint under the existing [[Backlog/definition-of-done]] |
| **Validate & Release** | PPL/customer validation, change request, PROD release, deliverable submission |

| Marker | Meaning |
|--------|---------|
| ◆ | Stakeholder requirements sign-off |
| ▲ | OCM sign-off |
| ⬥ | AP00288 contract gate |

**Why UAT is not inside Build & Test:** team testing is capacity we control; customer validation is elapsed time we don't. It is also where the AP00288 **three-business-day deemed-acceptance** clock runs. Merging the two would hide the dependency the DL is asking to see.

### Derivation rule

Phases are derived mechanically from the ADO sprint spans already on slide 3 — not estimated per feature.

| Phase | Rule |
|-------|------|
| Requirements / Spike | 1 sprint, **ending** where the current ADO build span starts |
| Build & Test | the ADO sprint span as shown on slide 3 |
| Validate & Release | 1 sprint following build end, landing before the gate |

Sprint 4.5 (Dec 23 – Jan 5) is treated as unavailable. Where the rule lands a phase there, it shifts to the adjacent sprint and is flagged.

---

## Sprint calendar

| Sprint | Dates |
|--------|-------|
| PI-3 IP | Oct 14 – Oct 27 |
| 4.1 | Oct 28 – Nov 10 |
| 4.2 | Nov 11 – Nov 24 |
| 4.3 | Nov 25 – Dec 8 |
| 4.4 | Dec 9 – Dec 22 |
| 4.5 | Dec 23 – Jan 5 — holiday, treated as unavailable |
| 4.6 | Jan 6 – Jan 19 |
| 4.7 IP | Jan 20 – Feb 2 |

---

## Phase timeline — 13 PI-4 features

| ADO | Feature | SOW | Requirements | Build & Test | Validate & Release | Gate | Margin |
|-----|---------|-----|--------------|--------------|--------------------|------|--------|
| 1646517 | 15 Priority Service Maps (1 of 3) | D3 | **PI-3 IP · Oct 14–27** ⚠ | 4.1 · Oct 28 – Nov 10 | 4.2 · Nov 11–24 | Nov 30 | **6 d** |
| 1639335 | CMDB Correctness Rules | D8 | **PI-3 IP · Oct 14–27** ⚠ | 4.1–4.2 · Oct 28 – Nov 24 | 4.3 · Nov 25 – Dec 8 | Dec 31 | 23 d |
| 1642237 | 15 Priority Service Maps (2 of 3) | D4 | 4.1 · Oct 28 – Nov 10 | 4.2 · Nov 11–24 | 4.3 · Nov 25 – Dec 8 | Dec 31 | 23 d |
| 1640795 | Non-Discoverable CI Attribute Interface | D9 | 4.1 · Oct 28 – Nov 10 | 4.2 · Nov 11–24 | 4.3 · Nov 25 – Dec 8 | Dec 31 | 23 d |
| 1642240 | Automated Stakeholder Notifications | D6 | 4.2 · Nov 11–24 | 4.3 · Nov 25 – Dec 8 | 4.4 · Dec 9–22 | Dec 31 | **9 d** ⚠ |
| 1639225 | Network Inventory — Cisco Catalyst | D2 | 4.2 · Nov 11–24 | 4.3–4.4 · Nov 25 – Dec 22 | 4.6 · Jan 6–19 ⚠ | Feb 2 | 14 d |
| 1640805 | Server Build Lifecycle Process Flow | D10 | 4.2 · Nov 11–24 | 4.3–4.4 · Nov 25 – Dec 22 | 4.6 · Jan 6–19 ⚠ | Feb 2 | 14 d |
| 1639308 | CMDB Adoption Campaign | D7 | 4.1 · Oct 28 – Nov 10 | 4.2–4.6 · Nov 11 – Jan 19 | **no window** ⚠ | Jan 30 | **0 d** ⚠ |
| 1640819 | Server Decommission Lifecycle Flow | D11 | 4.3 · Nov 25 – Dec 8 | 4.4–4.6 · Dec 9 – Jan 19 | 4.7 IP · Jan 20 – Feb 2 | Feb 2 | **0 d** ⚠ |
| 1642332 | 15 Priority Service Maps (3 of 3) | D5 | 4.4 · Dec 9–22 ⚠ | 4.6 · Jan 6–19 | 4.7 IP · Jan 20 – Feb 2 | Feb 2 | **0 d** ⚠ |
| 1640844 | Catalog Item — Service Map Updates | D12 | 4.4 · Dec 9–22 ⚠ | 4.6 · Jan 6–19 | 4.7 IP · Jan 20 – Feb 2 | Feb 2 | **0 d** ⚠ |
| 1639239 | Network Inventory POC — Qualys | TBC | 4.4 · Dec 9–22 ⚠ | 4.6–4.7 · Jan 6 – Feb 2 | **no window** ⚠ | Feb 2 | **0 d** ⚠ |
| TBD | Network Inventory — Tripwire | TBC | — | — | — | TBC | **unscheduled** ⚠ |

⚠ on a Requirements cell = phase shifted off its rule because it landed in PI-3 IP or holiday Sprint 4.5.

---

## What the derivation surfaces

**1. Two features need requirements work started now.** 1646517 (D3) and 1639335 (D8) both build in Sprint 4.1. Their requirements runway is **PI-3 IP, Oct 14–27** — this week, three weeks before PI Planning on Nov 4. D3 carries the $478,197 November invoice.

**2. Slide 5's margins shrink once release is a phase.** Slide 5 measures gate minus *build end*. Measured gate minus *release*, five features go to zero: D7, D11, D5, D12, and Qualys all finish on their gate date with no validation window. D3 drops from 20 days to 6.

**3. D7 does not fit.** The Adoption Campaign builds through Jan 19 against a **Jan 30** gate, with OCM sign-off still to obtain. There is no validate-and-release sprint available — 4.7 IP starts Jan 20 but the gate falls inside it. Either build ends earlier or validation runs concurrently with the 4.6 build. Consistent with Risk 8 in [[PI-4/pi-planning]] and the two-wave rollout in [[PI-4/pi4-adoption-1639308-campaign-stories-dependencies]].

**4. The Dec 31 gate cluster all releases in Dec 8–22.** D4, D6, D8, D9 — four deliverables releasing in the two weeks before the holiday shutdown. **If PPL runs a December change freeze, these move earlier and the margins above are wrong.** Unconfirmed — see Open Questions.

**5. Sprint 4.5 displaces work in both directions.** Three features (D5, D12, Qualys) would have had requirements in 4.5 and three (D2, D10, and the D5/D12/Qualys releases) would have released into or across it. All shifted.

**6. Qualys has no validation window at all** — it builds to Feb 2, the contract end date. It also still has no AP00288 deliverable number.

**7. Tripwire cannot be planned.** No ADO work item, no sprint, no dates. Show as an unscheduled lane rather than omitting it.

---

## Tracking companion

Four intermediate due dates per feature, carried as columns in the weekly status. This is the "more frequent due dates" half of the DL's ask, and it is cheaper to maintain than the slide.

| Column | Set at |
|--------|--------|
| Req sign-off | ◆ end of Requirements phase |
| Build complete | end of Build & Test |
| Validation exit | PPL acceptance received |
| Released | PROD + deliverable submitted |

---

## Open questions

| # | Question | Blocks |
|---|----------|--------|
| 1 | Does PPL run a December change freeze, and what are the dates? | Release dates for D4, D6, D8, D9 — and the slide-5 margin recalculation |
| 2 | Can D7 validation run concurrently with the 4.6 build, or does build end earlier? | The only zero-margin item with a January invoice attached ($493,794) |
| 3 | Who runs OCM for the 11 non-campaign features, and at what allocation? | The ▲ markers — Nora Lizenberg is OCM Support on the CCB, but there is no OCM capacity line in the plan |
| 4 | Is requirements work for 1646517 and 1639335 starting in PI-3 IP? | Both Sprint 4.1 builds; D3 carries the November invoice |
| 5 | Tripwire — create the ADO item, or show it as explicitly unscheduled? | Whether it gets a row |

---

## Next step

Build as one slide reusing slide 6's grid: same 7 sprint columns, same 12 rows, same objective colors, bars segmented into the 3 bands with the 3 markers. Standalone `.pptx` for the user to append — the main deck stays untouched.
