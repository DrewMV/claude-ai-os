---
level: pi
workspace: Work
project: CMDB-CSDM
pi: PI-3
status: future
start: 2026-08-05
end: 2026-10-27
updated: 2026-06-01
tags: [work, safe, pi-planning, cmdb-csdm]
---

## PI Objectives

_PI Planning occurs during PI2 IP Iteration (Jul 22 – Aug 4, 2026). Fill in after PI Planning._

- **CO6 contract objectives (7):** [[PI-3/pi3-objectives]] — governing scope, does not change
- **CMDB/CSDM team ADO objectives (4) + features (11):** [[PI-3/pi3-cmdb-csdm-ado-tracking]] — subset of CO6; this team's tracked/reported scope

### Feature story breakdowns (SAFe stories + dependencies)

Per-feature drafts: SAFe user stories (description + acceptance criteria) and dependencies (problem + acceptance criteria). REFERENCE/DRAFT — ADO authoritative.

- **1517029 — Certify Computers** (Obj 3): [[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]] — 5 stories (CC-1…CC-5) + 6 dependencies
- **1517032 — Certify Servers** (Obj 3): [[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]] — 5 stories (SV-1…SV-5) + 7 dependencies (incl. the `environment` Mandatory ruling, DEP-7)
- **1517037 — Certify Databases** (Obj 3): [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]] — 5 stories (DB-1…DB-5) + 6 dependencies (blocking: CP-3 attribute reconciliation DEP-3; Oracle-KY data quality DEP-4); Oct 30 gate
- **1517040 — Certify Network Devices** (Obj 3): [[PI-3/pi3-cert-1517040-certify-network-devices-stories-dependencies]] — 6 stories (NW-1…NW-6, incl. net-new audit spike) + 5 dependencies; **highest-risk cert feature** — depends on Obj 4 attribute population (1517005, Sep 30), no audit spike or Class Manager yet; Oct 30 gate
- **1516993 — Network Discovery** (Obj 4): [[PI-3/pi3-nd-1516993-stories-dependencies]] — existing precedent for this artifact type

## Iterations

| Iteration | Start | End | Status |
|-----------|-------|-----|--------|
| 3.1 | 2026-08-05 | 2026-08-18 | Future |
| 3.2 | 2026-08-19 | 2026-09-01 | Future |
| 3.3 | 2026-09-02 | 2026-09-15 | Future |
| 3.4 | 2026-09-16 | 2026-09-29 | Future |
| 3.5 | 2026-09-30 | 2026-10-13 | Future |
| 3.6 (IP) | 2026-10-14 | 2026-10-27 | IP Iteration |

## Planning Readiness Milestones (Runway to Ready)

| Iteration | Due | Owner | Gate |
|-----------|-----|-------|------|
| Iter 2 | **Jun 9** | Joe (PO) | PI-3 Epics identified; tied to OKRs; on ADO roadmap |
| Iter 3 | Jun 23 | Joe (PO) | Candidate Features created; ~5/team; on ADO roadmap |
| Iter 4 | Jul 7 | Joe (PO) | Preliminary PI Objectives drafted in ADO; dependencies identified |
| Iter 5 | Jul 21 | Joe (PO), Alex (SM), Teams | Features decomposed to Stories; DoR met; estimates in; ADO current |
| Iter 6 / IP | **Aug 4** | Alex (SM) | Miro boards ready; matches ADO; capacity finalized |

See [[PI-3/pi3-planning-readiness]] for full checklist.

## Team Capacity

_Fill in at PI Planning._

## Risks and Dependencies

| # | Risk | Severity | Status | Notes |
|---|------|---------|--------|-------|
| 1 | **Test code freeze extends to Aug 15** — pplwebtest frozen through first 10 days of PI-3 (Iter 3.1: Aug 5–18); no test deployments until Aug 15; Iter 3.1 sprint planning must account for reduced test capacity | High | Open | See [[Dependencies/external]] — CHG70100865 |
| 2 | **Prod upgrade Aug 15 (Australia)** — pplweb (Prod) upgrades mid-Iter 3.1; NowAssist PI-3 objectives (OBJ-4.x, OBJ-5.x) depend on OBJ-1.1/1.2 baselines that may require Australia features; confirm NowAssist capability availability pre/post upgrade | High | Open | See [[Dependencies/external]] — CHG70121033 |
| 3 | **Post-clone validation — dev (June 19) and test (July 10)** — both clone events during PI-2 will require post-clone data integrity checks; pattern from prior clone (Risk #2 in PI-2) should inform validation checklist | Medium | Open | Carried pattern from PI-2 |

## Key Decisions This PI

_No decisions recorded yet._

## Open Questions

_No open questions yet._
