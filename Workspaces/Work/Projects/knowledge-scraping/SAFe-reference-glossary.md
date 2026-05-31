---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, reference, glossary]
updated: 2026-05-30
sources: [wsjf, spikes, roadmap, solution-vision, solution-demo, coordinate-and-deliver, pre-plan, business-owners, portfolio-leadership, planning-interval, pi-objectives, iteration-goals, value-stream-kpis, agile-release-train]
summary: Quick-reference definitions for key SAFe terms, metrics, events, and concepts — a concise glossary for practitioners.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
---

# SAFe Reference Glossary

A quick-reference guide to key SAFe terms, acronyms, and concepts. For full explanations, see the linked wiki pages.

## Core Terms

| Term | Definition |
|---|---|
| **ART** | Agile Release Train — a long-lived team of 5–15 Agile teams (50–125 people) that incrementally develops, delivers, and operates one or more solutions |
| **CDP** | Continuous Delivery Pipeline — workflows, activities, and automation from ideation to release: CE → CI → CD → RoD |
| **CE** | Continuous Exploration — aligning what to build through customer research, hypothesis formation, and backlog prioritization |
| **CI** | Continuous Integration — frequent integration and automated testing of code to detect defects early |
| **CD** | Continuous Deployment — automated deployment of code to production environments |
| **CoD** | Cost of Delay — the economic impact of delaying a feature; drives WSJF prioritization |
| **CoP** | Community of Practice — group of practitioners with shared domain interest who collaborate to improve skills |
| **DevSecOps** | Development, Security, and Operations combined — mindset and practices for integrating security throughout the CDP |
| **DoD** | Definition of Done — agreed-upon criteria that a work item must meet to be accepted |
| **DVS** | Development Value Stream — sequence of activities to convert a business hypothesis into a digitally-enabled solution |
| **eNPS** | Employee Net Promoter Score — measures employee engagement and likelihood to recommend the organization as a workplace |
| **I&A** | Inspect and Adapt — significant ART event at PI end: System Demo, measurement review, problem-solving workshop |
| **IP Iteration** | Innovation and Planning Iteration — special iteration at PI end for planning, innovation, and I&A |
| **KPI** | Key Performance Indicator — specific, quantifiable measure of ongoing business or value stream performance |
| **LACE** | Lean-Agile Center of Excellence — small dedicated team driving SAFe transformation across the enterprise |
| **LPM** | Lean Portfolio Management — aligning strategy and execution via Lean funding, governance, and operations |
| **MMF** | Minimum Marketable Feature — smallest feature that provides customer value and tests a benefit hypothesis |
| **MTTR** | Mean Time to Recover — how long it takes to restore service after a failure |
| **MVP** | Minimum Viable Product — smallest product increment that tests an epic or product hypothesis |
| **NFR** | Nonfunctional Requirement — system quality constraint (performance, security, scalability, maintainability) |
| **OKR** | Objectives and Key Results — framework for ambitious goals (objective) with measurable outcomes (key results) |
| **OVS** | Operational Value Stream — sequence of activities that delivers a product or service to a customer |
| **PDCA** | Plan-Do-Check-Adjust — iterative learning cycle applied at team, ART, and PI level |
| **PI** | Planning Interval — fixed timebox (8–12 weeks) during which the ART delivers continuous value |
| **PMO** | Project/Program Management Office — traditional project oversight function; replaced/transformed by VMO in SAFe |
| **PO** | Product Owner — team member responsible for the team backlog and maximizing team value |
| **RoD** | Release on Demand — ability to release value to customers at business-optimal timing |
| **RTE** | Release Train Engineer — servant leader and ART coach who facilitates ART events and optimizes flow |
| **SBD** | Set-Based Design — Lean practice of maintaining multiple design options, eliminating weaker ones as knowledge grows |
| **SM/TC** | Scrum Master/Team Coach — servant leader who coaches the Agile team, facilitates events, and improves flow |
| **SPC** | SAFe Practice Consultant — trained change agent who implements and sustains SAFe (formerly SAFe Program Consultant) |
| **STE** | Solution Train Engineer — coach for the Solution Train; coordinates across ARTs and suppliers |
| **TDD** | Test-Driven Development — writing tests before code to ensure behavior meets requirements |
| **VMO** | Value Management Office — evolved PMO focused on enabling LPM processes and measuring value flow |
| **V&V** | Verification and Validation — verification = system works as designed; validation = system meets intended purpose |
| **WIP** | Work in Process — work items currently active in the system; limiting WIP accelerates flow |
| **WSJF** | Weighted Shortest Job First — prioritization model: CoD ÷ Job Duration; maximizes economic throughput |

## Key Metrics

### Flow Metrics

| Metric | What It Measures |
|---|---|
| **Flow Distribution** | Proportion of work by type (features, enablers, defects, risks) |
| **Flow Velocity** | Number of items completed per timeframe (throughput) |
| **Flow Time** | Total time from idea to production release |
| **Flow Load** | Number of items currently in the system (WIP) |
| **Flow Efficiency** | Active time ÷ Flow Time (often <10% in unoptimized systems) |
| **Flow Predictability** | Actual business value ÷ planned business value per PI (target: 80–100%) |

### DORA Metrics (DevOps)

| Metric | Maps To |
|---|---|
| Deployment frequency | Flow Velocity |
| Lead time for changes | Flow Time |
| Time to restore service | Flow Time (incident recovery) |
| Change failure rate | Quality (% changes requiring remediation) |

## Key Events

| Event | Frequency | Scope | Purpose |
|---|---|---|---|
| Iteration Planning | Start of each iteration | Team | Plan work for the iteration |
| Team Sync | Daily | Team | Inspect progress; adjust plan |
| Backlog Refinement | 1–2x per iteration | Team | Clarify and estimate upcoming stories |
| Iteration Review | End of iteration | Team | Demo completed work; gather feedback |
| Iteration Retrospective | End of iteration | Team | Reflect; improve process |
| PO Sync | Weekly | ART | PM/POs review ART progress |
| Coach Sync | Weekly | ART | RTEs/SM/TCs coordinate |
| System Demo | End of each iteration | ART | Integrated view of all teams' work |
| PI Planning | Start of each PI | ART | Align teams to shared mission; create PI plans |
| Inspect & Adapt | End of each PI | ART | Demo, measure, and improve |
| Strategic Portfolio Review | Quarterly | Portfolio | Strategy, investment, and budget alignment |
| Portfolio Sync | Monthly | Portfolio | Portfolio progress, epic status, dependencies |
| Pre-Plan | Before PI Planning | Solution Train | Align multiple ARTs for PI Planning |
| Coordinate and Deliver | After PI Planning | Solution Train | Aggregate ART plans; resolve cross-ART issues |
| Solution Demo | End of each PI | Solution Train | Integrated view across all ARTs |

## WSJF: Weighted Shortest Job First

WSJF = Cost of Delay ÷ Job Duration (size)

**Cost of Delay components (relative estimates):**
- User/Business Value
- Time Criticality
- Risk Reduction / Opportunity Enablement

**How to apply:**
1. Estimate each factor on a relative Fibonacci scale (1, 2, 3, 5, 8, 13, 20)
2. Sum the three CoD components
3. Divide by relative job size
4. Rank backlog from highest to lowest WSJF
5. Pull highest WSJF items first

**Why:** Sequencing by WSJF delivers more total economic value than sequencing by ROI or business value alone. It automatically accounts for sunk costs (which are ignored).

## PI Planning Artifacts

| Artifact | Description |
|---|---|
| **PI Objectives** | Team's committed and uncommitted goals for the PI; Business Owners assign business value |
| **ART Planning Board** | Matrix showing features by team × iteration; highlights dependencies and milestones |
| **Team PI Plan** | Iteration-by-iteration plan for each team; stories by iteration |
| **ART PI Risks (ROAM)** | Resolved, Owned, Accepted, Mitigated risks identified during PI Planning |

## Backlog Hierarchy

| Level | Work Item | Managed By | Sized For |
|---|---|---|---|
| Portfolio | Epic | Portfolio Kanban | Multiple PIs |
| Solution Train | Capability | Solution Train Backlog | Single PI |
| ART | Feature | ART Backlog | Single PI |
| Team | Story / Spike | Team Backlog | Single iteration |

## Eight Flow Accelerators (Principle #6)

1. Visualize and Limit WIP
2. Address Bottlenecks
3. Minimize Handoffs and Dependencies
4. Get Faster Feedback
5. Work in Smaller Batches
6. Reduce Queue Length
7. Optimize Time 'In the Zone'
8. Remediate Legacy Policies and Practices

## Ten SAFe Principles

1. Take an economic view
2. Apply systems thinking
3. Assume variability; preserve options
4. Build incrementally with fast, integrated learning cycles
5. Base milestones on objective evaluation of working systems
6. Make value flow without interruptions
7. Apply cadence, synchronize with cross-domain planning
8. Unlock the intrinsic motivation of knowledge workers
9. Decentralize decision-making
10. Organize around value

## Four SAFe Core Values

1. Alignment
2. Transparency
3. Respect for People
4. Relentless Improvement

## SAFe Configurations

| Configuration | Includes |
|---|---|
| Essential SAFe | Teams + ART; simplest starting point |
| Large Solution SAFe | Essential + Solution Train |
| Portfolio SAFe | Essential + Lean Portfolio Management |
| Full SAFe | All levels: Teams, ART, Solution Train, Portfolio |

## Pre-Plan vs. Coordinate and Deliver (SAFe 6.0 Replacements)

| SAFe 5.x Term | SAFe 6.0 Term | Purpose |
|---|---|---|
| Pre-PI Planning | Pre-Plan | Align multiple ARTs before PI Planning |
| Post-PI Planning | Coordinate and Deliver | Aggregate ART plans; resolve cross-ART issues |

## Key Acronym Changes (SAFe 6.0)

| Old Term | New Term |
|---|---|
| Program Increment | Planning Interval (PI) |
| SAFe Program Consultant | SAFe Practice Consultant (SPC) |
| Program Backlog | ART Backlog |
| Daily Standup | Team Sync |
| ScrumXP | SAFe Scrum |
| APMO | Value Management Office (VMO) |
| Metrics | Measure and Grow |

## Related Pages

- [[SAFe-overview]] — Big Picture and configurations
- [[SAFe-core-values-and-principles]] — All 10 principles in detail
- [[SAFe-planning-and-events]] — PI Planning, iterations, I&A detail
- [[SAFe-backlogs-and-artifacts]] — Backlog hierarchy and artifact definitions
- [[SAFe-flow-and-delivery]] — Flow metrics, CDP, and OKRs
- [[SAFe-roles]] — All SAFe roles and responsibilities
- [[SAFe-lean-portfolio-management]] — Portfolio-level terms and governance
- [[SAFe-team-and-technical-agility]] — Team and ART practices
- [[SAFe-devops-and-technical-practices]] — DevOps and engineering terminology
- [[SAFe-implementation-roadmap]] — Transformation terminology and steps
