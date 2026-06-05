---
title: CMDB-CSDM Team Operating Model
type: concept
workspace: Work
project: ServiceNow
tags: [work, cmdb, safe, ceremonies, agile, team, operating-model]
created: 2026-06-05
updated: 2026-06-05
summary: "CMDB-CSDM team SAFe ceremony cadence, meeting-to-ceremony mapping, non-SAFe recurring meetings, and known structural gaps in the team's agile operating model."
base_confidence: 0.90
lifecycle: draft
lifecycle_changed: 2026-06-05
provenance: "Derived from calendar analysis June 2026. Mapped against SAFe team-level ceremonies."
---

# CMDB-CSDM Team Operating Model

**Team:** CMDB-CSDM
**Scrum Masters:** Manuel Vazquez, Alex Phan (co-SMs)
**Product Owner:** Joe Dames
**Sprint cadence:** 2 weeks

---

## SAFe Ceremony Cadence

### Daily

| Meeting | SAFe Ceremony | Organizer | Time |
|---------|--------------|-----------|------|
| CMDB DSU (Daily Stand-up) | **Daily Standup** | Phan, Alex | 8:30–9:00 AM |
| CMDB Service Mapping Stand-up | **Daily Standup** (SM sub-team) | Ortega, John B. T. | 11:30 AM–12:00 PM |

> Two standups reflect two active streams — core CMDB/CSDM and Service Mapping. Monitor for overlap/redundancy as team evolves.

---

### Sprint Start (Day 1–2)

| Meeting | SAFe Ceremony | Organizer | Cadence |
|---------|--------------|-----------|---------|
| Sprint Planning - CMDB/SM/CSDM | **Sprint Planning** | Phan, Alex | Sprint start |
| Backlog Refinement - CMDB/SM/CSDM | **Backlog Refinement** | Phan, Alex | Recurring (weekly or bi-weekly) |
| Stories Elicitation & Prioritization | **Backlog Refinement** | Rai, Anuradha | Recurring (daily 8:00–8:30 AM) |

> Stories Elicitation & Prioritization runs daily at 8:00 AM before the DSU — functions as a lightweight pre-refinement touchpoint.

---

### Sprint End

| Meeting | SAFe Ceremony | Organizer | Cadence |
|---------|--------------|-----------|---------|
| Weekly Showback (PO Acceptance) - CMDB/SM/CSDM | **Sprint Review** | Phan, Alex | Sprint end |
| CMDB/SM/CSDM Retrospective | **Sprint Retrospective** | Phan, Alex | Sprint end |

---

## Non-SAFe Recurring Meetings

These meetings do not map to a SAFe ceremony but serve important functions:

| Meeting | Purpose | Organizer |
|---------|---------|-----------|
| **Azure Airlift – Daily Dependency & Execution Touchbase** | Cross-team dependency and execution sync for the VMware-to-Azure migration. Runs daily during the migration period. Closest SAFe parallel: ART Sync / Scrum of Scrums, but project-specific. | Project Airlift |
| **CMDB Go Green Plan – Weekly** | PPL-specific operational meeting tracking CMDB health and quality improvement progress. Not a SAFe ceremony. | Das, Sonika |
| **Class Manager Touchpoint** | Technical SME engagement on ServiceNow Class Manager configuration. Functions as an enabler story or spike support session. | de Araujo, Anthony |
| **Cherwell CMDB Import File** | Operational meeting around legacy Cherwell data import into CMDB. One-time or episodic. | Uloma, Adelufosi |

---

## Known Structural Gaps

These SAFe ceremonies are not consistently scheduled or visible in the team calendar:

| Gap | Risk | Recommendation |
|-----|------|---------------|
| **Sprint Review not scheduled for Sprint 2.3 end** | PO acceptance may be missed at sprint close | Schedule Showback for June 23 |
| **Sprint Planning not scheduled for Sprint 2.4** | Team may enter next sprint without a committed plan | Schedule Sprint Planning for June 23–24 |
| **Retrospective not scheduled for Sprint 2.3 end** | Team has no structured reflection at sprint close | Schedule Retro for June 23 or 24 |
| **Backlog Refinement recurrence unclear** | Only one instance confirmed per sprint; may be insufficient for backlog depth | Confirm weekly recurrence; add second session if needed |
| **No System Demo visible** | ART-level demo cadence not reflected in team calendar | Confirm if System Demo is owned at ART level and whether team is expected to attend |

---

## Untracked Work — Shadow Activities (No Backlog Coverage)

These activities consumed team or SM capacity in Sprint 2.2 but have no corresponding story, spike, or backlog item. They represent invisible work that reduces delivery capacity without appearing on the board.

| Activity | Type | Risk | Recommended Action |
|---------|------|------|-------------------|
| **Access issues — ADO, Dev, SharePoint (Anuradha Rai)** | Onboarding/operational overhead | Blocks story execution if unresolved | Log as impediment; track to resolution |
| **Dashboard capability request (new demand)** | Unformalized demand | Becomes invisible expectation if not captured | Create story or formally park in backlog |
| **Change governance reinforcement (standard vs normal CR)** | Process gap / SM practice | Gap recurs if not addressed formally | Consider spike or enabler story to document and enforce the process |
| **Correctness metric data population** | Data dependency with no owner | Blocked Sprint 2.2 acceptance; no story owns it | Add as task under Story 1435307 or log as impediment |

> **SM principle:** If work is happening and consuming sprint capacity, it belongs on the board. Shadow work is a planning and forecasting risk.

---

## Impediment Tracking

Active impediments should be raised in the DSU and tracked visibly. As of Sprint 2.2 close:

| Impediment | Impact | Owner |
|-----------|--------|-------|
| Correctness metric data not populated | Blocks Sprint 2.2 PO acceptance | TBD |
| Anuradha Rai access issues (ADO/Dev/SharePoint) | Blocks story execution | TBD |

---

## Sprint Boundary Reference

| Sprint | Start | End | Key Ceremonies Due |
|--------|-------|-----|--------------------|
| 2.2 | May 27 | June 9 | Showback June 8–9, Planning June 9, Retro June 12 |
| 2.3 | June 10 | June 23 | Showback ~June 23, Planning ~June 23, Retro ~June 23–24 |
| 2.4 | June 24 | July 7 | Planning ~June 24 |

---

## Related Pages

- [[cmdb-governance-roadmap]] — overall CMDB governance and PI2 focus areas
- [[SAFe-planning-and-events]] — SAFe ceremony reference (PI Planning, iterations, all events)
- [[SAFe-roles]] — SAFe role definitions including SM and PO responsibilities
