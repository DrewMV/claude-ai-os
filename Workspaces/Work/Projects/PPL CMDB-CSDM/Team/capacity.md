---
type: team-artifact
workspace: Work
project: CMDB-CSDM
updated: 2026-06-01
tags: [work, cmdb-csdm, team, capacity]
---

# CMDB-CSDM Capacity Tracker

Team size: 10 members + PO (Joe Dames) + SM (Alex Phan)

## Team Members

| Name | Title | Location |
|------|-------|---------|
| Stan Tomberg | CMDB Discovery / Senior IS (Architect) | Onshore |
| Tanzeel Rehman | Team Lead Service Mapping | Onshore |
| Bhushan Salsekar | Implementation Specialist | Offshore |
| Kiran Dhobale | Implementation Specialist | Offshore |
| Vinay Geddannavar | Implementation Specialist | Offshore |
| Tony De Araujo | Developer | Onshore |
| Venkateswarlu Manikanta | QA Tester | Offshore |
| Ruchita Rohini | Project Manager | Offshore |
| Anuradha Rai (Anu) | Functional Designer | Offshore |
| Uloma Adelufosi | Product Analyst | Onshore |

## PI-2

| Iteration | Start | End | Available Days | Committed Points | Actual Points | Velocity |
|-----------|-------|-----|---------------|-----------------|---------------|---------|
| 2.1 | 2026-05-13 | 2026-05-26 | | | | |
| 2.2 | 2026-05-27 | 2026-06-09 | | | | |
| 2.3 | 2026-06-10 | 2026-06-23 | | | | |
| 2.4 | 2026-06-24 | 2026-07-07 | | | | |
| 2.5 | 2026-07-08 | 2026-07-21 | | | | |
| 2.6 (IP) | 2026-07-22 | 2026-08-04 | — | — | — | — |

## PI-3 Developer Capacity

**Developers:** 3 in India (offshore) · 5 in US (onshore) · 8 developers total
**Target capacity:** 8 days/sprint per developer (baseline, before holiday deduction)

| | 3.1 | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 (IP) |
|---|---|---|---|---|---|---|
| **Start** | 2026-08-05 | 2026-08-19 | 2026-09-02 | 2026-09-16 | 2026-09-30 | 2026-10-14 |
| **End** | 2026-08-18 | 2026-09-01 | 2026-09-15 | 2026-09-29 | 2026-10-13 | 2026-10-27 |
| **Total Dev-Days** | **64** | **64** | **53** | **64** | **64** | **61** |
| **Holiday Impact** | Independence Day (India) Sat Aug 15 — weekend, no impact | Raksha Bandhan Fri Aug 28 — likely no impact (Maharashtra) | India: Janmashtami Sep 4 + Ganesh Chaturthi Sep 14 (−2) · US: Labor Day Sep 7 (−1) | None identified | Columbus Day (US) Oct 12 — not universally observed; confirm | Dussehra Oct 20 (India, −1) · IP sprint, reference only |

**Sprint 3.3 is the lowest-capacity sprint of PI-3** (53 dev-days vs. the 64 baseline) — both India (Janmashtami + Ganesh Chaturthi) and US (Labor Day) lose capacity in the same 2-week window. Flag at sprint planning; consider reducing commitment for 3.3 accordingly.

## PI-3 Days-Off Request — Developer Sign-off

Send to each developer to confirm planned days off (PTO, holidays observed, other absences) per sprint. Blank = to be filled in by the developer.

| Developer | Location | 3.1 | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 (IP) | Total Days Off |
|-----------|----------|-----|-----|-----|-----|-----|----------|-----------------|
| Vinay | India | | | | | | | |
| Kiran | India | | | | | | | |
| Bhushan | India | | | | | | | |
| Stan | US | | | | | | | |
| Tony | US | | | | | | | |
| Mike | US | | | | | | | |
| Josh | US | | | | | | | |
| Jeff | US | | | | | | | |
| Alex | US | | | | | | | |
| Laurent | US | | | | | | | |
| Adam | US | | | | | | | |

**Sprint dates for reference:** 3.1 (Aug 5–18) · 3.2 (Aug 19–Sep 1) · 3.3 (Sep 2–15) · 3.4 (Sep 16–29) · 3.5 (Sep 30–Oct 13) · 3.6 IP (Oct 14–27)

> **Open item:** this developer list (11: 3 India / 8 US, three of whom — Alex, Laurent, Adam — are 50% allocated) doesn't match the 8-developer / 8-days-per-sprint split used in the capacity chart above, and Mike/Josh/Jeff/Alex/Laurent/Adam aren't on [[Team/team-roster]] as direct CMDB delivery team members — Laurent in particular is tracked elsewhere as cross-team (Airlift), and Adam Griffis is the Service Mapping feature owner (1516955), not previously listed as a developer. Reconcile the capacity chart (target days/sprint should be halved to ~4 for the 50%-allocated developers) once this list is settled.

## Notes

- **8 days/sprint/developer** is the target baseline (already assumed to account for standard ceremonies/overhead); each confirmed holiday that lands on a weekday subtracts 1 day per affected developer for that sprint.
- India developers assumed Pune/Maharashtra-based per [[Team/team-roster]] — Maharashtra state holidays (Ganesh Chaturthi, Dussehra) are high-confidence impacts; other regional festivals (Onam, Raksha Bandhan, Durga Puja) are lower-confidence unless a specific developer is based elsewhere — confirm actual PTO/regional calendar per person closer to each sprint.
- Janmashtami date conflict in sources: some list Aug 19, others (Panchang-based) list Sep 4, 2026 — used Sep 4 as the primary tithi date; verify against the actual company holiday calendar.
- Columbus Day (Oct 12, Sprint 3.5) is a US federal holiday but not universally observed by private employers/contractors — confirm whether it's on PPL's or Accenture's holiday calendar before deducting a day.
- 3.6 is the IP (Innovation & Planning) iteration — dev-days shown for reference, but this sprint isn't planned/measured the same way as a delivery sprint (PI planning, innovation work, no committed story points).
- Track PTO and known individual absences per iteration here as they're confirmed — the table above only reflects public/company holidays, not vacation.
