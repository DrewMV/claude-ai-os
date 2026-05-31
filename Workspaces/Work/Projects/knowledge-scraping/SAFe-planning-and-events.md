---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, planning, events, cadence]
updated: 2026-05-30
sources: [pi-planning, planning-interval, inspect-and-adapt, iteration-planning, iterations, innovation-and-planning-iteration, pi-objectives, wsjf, iteration-goals, reaching-the-tipping-point]
summary: SAFe planning cadence — PI Planning, iterations, Inspect & Adapt, PI Objectives, WSJF, and the full ART event cycle.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.88
  inferred: 0.09
  ambiguous: 0.03
---

# SAFe Planning and Events

SAFe operates on a structured cadence of events at two primary levels: the **Planning Interval (PI)** (8–12 weeks) and the **Iteration** (2 weeks). These events provide the rhythm for alignment, delivery, and improvement across the ART. Cadence and synchronization are [[SAFe-core-values-and-principles|SAFe Principle #7]] — they create predictability and limit variance accumulation.

## Planning Interval (PI)

The Planning Interval (PI) is the primary timebox for the ART — a fixed period during which the ART delivers continuous value and achieves PI Objectives.

A typical PI consists of:
- **4 development iterations** (2 weeks each)
- **1 Innovation and Planning (IP) Iteration** at the end

Total PI duration: typically 10 weeks (4×2 development + 1×2 IP).

Key PI activities:
- Starts with PI Planning
- Progresses through a series of System Demos each iteration
- Ends with the Inspect & Adapt (I&A) event in the IP Iteration

## PI Planning

**Definition:** A cadence-based event for the entire ART that aligns teams and stakeholders to a shared mission and vision.

PI Planning is the most powerful event in SAFe. It is held every 8–12 weeks, typically a 2-day event held at the start of the PI (within the IP Iteration). The people who do the work plan the work.

**Benefits:**
- Face-to-face communication among all ART members and stakeholders
- Alignment of development to business goals
- Identification of dependencies and cross-team collaboration opportunities
- Architecture and Lean UX guidance
- Matching demand to capacity; eliminating excess WIP
- Fast decision-making with all decision-makers present
- Holistic, transparent view of where and when value will be delivered

**Inputs:**
- Business context
- Vision and roadmap
- Highest-priority Features from the ART Backlog

**Outputs:**
- **Committed PI Objectives** — each team's set of business and technical goals for the PI; Business Owners assign business value to each objective
- **ART Planning Board** — matrix showing feature delivery dates, dependencies between teams, and milestones; dependency management throughout the PI

### PI Planning Preparation

Three readiness areas:
1. **Organizational readiness** — scope and context understood; Business Owner alignment; Agile Teams formed with PO and SM/TC
2. **Content readiness** — Executive briefing (business context), Product/Solution Vision briefing (top features), Architecture Vision briefing (enablers, NFRs)
3. **Logistics readiness** — Venue secured; technology/tools for distributed teams; communication channels

### PI Planning Agenda

**Day 1:**
1. Business context — Business Owners share portfolio vision and current business state
2. Product/solution vision — Product Management presents top features and changes from last PI
3. Architecture vision — System Architect presents enablers, current/future state architecture, NFRs
4. Planning context — RTE explains process and expected outcomes
5. Team breakouts #1 — Teams estimate capacity, identify features and stories, draft PI plans, identify risks and dependencies, add to ART Planning Board
6. Draft plan review — Teams present capacity, draft objectives, risks, and dependencies to all
7. Management review and problem-solving — Management negotiates scope, resolves constraints and dependencies

**Day 2:**
1. Planning adjustments — Management presents scope/resource changes
2. Team breakouts #2 — Teams finalize objectives; Business Owners assign business value
3. Final plan review — All teams present plans; state risks and impediments; Business Owners accept or request revisions
4. ART PI Risks (ROAM) — Risks categorized: Resolved, Owned, Accepted, Mitigated
5. Confidence vote (fist of five) — ART votes confidence; average ≥3 = accept; <3 = rework
6. Planning retrospective and next steps

### PI Objectives

PI Objectives summarize the specific business and technical goals each team and the ART intend to achieve in the upcoming PI. Characteristics:
- **Committed objectives** — goals the team commits to with high confidence
- **Uncommitted objectives** — goals built into the plan with too many unknowns to fully commit; provide capacity buffer and early warning to management
- Business Owners assign business value (1–10) to each team's PI objectives at PI Planning
- At I&A, actual business value achieved is compared to planned for predictability measurement

**SMART PI Objectives:** Specific, Measurable, Achievable, Realistic, Time-bound.

## Iterations

Iterations are fixed-duration timeboxes (typically 2 weeks) during which Agile Teams and ARTs deliver incremental customer value while working toward PI Objectives.

Each iteration is a complete **PDCA cycle** (Plan-Do-Check-Adjust):
- **Plan** — Iteration Planning; backlog refinement; planning for System Demo
- **Do** — Deliver stories and high-value increments; team sync; demo completed work immediately
- **Check** — Retrospective; review improvement stories; review demos with stakeholders
- **Adjust** — Improve team processes; refine backlog

**Nested PDCA cycles:** Iteration PDCA cycles nest within the PI PDCA cycle (PI Planning → Delivery → I&A), and within individual team sprints.

### Iteration Events (SAFe Scrum)

| Event | Frequency | Purpose |
|---|---|---|
| Iteration Planning | Start of each iteration | Team identifies iteration goals and commits to stories from backlog |
| Team Sync (formerly Daily Standup) | Daily (~15 min) | Inspect progress toward iteration goal; adjust plan |
| Backlog Refinement | Once or twice per iteration | Review, clarify, and estimate upcoming stories and enablers |
| Iteration Review | End of each iteration | Demo completed work; gather stakeholder feedback |
| Iteration Retrospective | End of each iteration | Reflect on practices; identify process improvements |

### Innovation and Planning (IP) Iteration

A special iteration at the end of each PI. It:
- Serves as an **estimating buffer** — no planned stories; scope buffer for meeting PI Objectives
- Provides dedicated time for **innovation** — hackathons, prototypes, exploratory work
- Hosts **PI Planning** for the next PI
- Hosts the **Inspect & Adapt** event for the current PI
- Supports **continuing education** — training, certifications, Communities of Practice

The IP Iteration is critical: without it, teams would sacrifice learning, planning, and improvement for delivery pressure.

## ART Events

### System Demo

The primary measure of ART progress — the integrated work of all teams for the iteration, demonstrated to stakeholders every 2 weeks. Key properties:
- Shows the fully integrated system (not just individual team work)
- Stakeholders provide feedback on business value and fitness for purpose
- At PI end, the PI System Demo is the formal demonstration of all features developed in the PI

### ART Sync

Combines Coach Sync and PO Sync into a single coordinating event:
- **Coach Sync** — RTEs and SM/TCs coordinate dependencies and impediments
- **PO Sync** — Product Management and POs review progress toward PI Objectives; adjust scope if needed

## Inspect and Adapt (I&A)

**Definition:** A significant event at the end of each PI where the current state of the Solution is demonstrated and evaluated, then teams reflect and identify improvement backlog items via a structured problem-solving workshop.

The I&A is the structural forcing function for relentless improvement — dedicated time every PI for the entire ART to improve, not just teams in isolation.

**Three parts:**

### Part 1: PI System Demo
- Showcases all features developed during the PI
- Business Owners and teams assess actual business value vs. planned for each PI objective
- Predictability measure: compare planned vs. actual business value; target 80–100% reliability range
- Uncommitted objectives excluded from plan scoring but included in actual achievements

### Part 2: Quantitative and Qualitative Measurement
- RTE presents performance metrics: ART predictability measure, flow metrics (velocity, flow time, flow load, distribution), value stream KPIs, eNPS
- Provides fact-based foundation for the problem-solving workshop

### Part 3: Problem-Solving Workshop
Structured root-cause analysis workshop:
1. **Agree on problems to solve** — brief retrospective surfaces key issues; cross-functional groups self-select
2. **Root cause analysis** — Fishbone (Ishikawa) diagram with 5 Whys: brainstorm causes across People, Process, Tools, Work, and Environment
3. **Identify biggest root cause** — Pareto analysis (80/20 rule); dot voting on main causes
4. **Restate the problem** — Clearly articulate the root cause as a problem statement
5. **Brainstorm solutions** — Generate many possible corrective actions
6. **Create improvement backlog items** — Vote on top 3 solutions; write as improvement backlog items for the ART Backlog

Improvements are planned into the upcoming PI with designated owners and a communication plan.

## WSJF: Weighted Shortest Job First

**Definition:** A prioritization model used to sequence work for maximum economic benefit. WSJF = Cost of Delay ÷ Job Duration.

WSJF is the primary backlog prioritization method in SAFe at ART and Portfolio levels. Key principles:
- "If you only quantify one thing, quantify the Cost of Delay." (Reinertsen)
- Job sequencing produces better results than theoretical ROI prioritization
- Automatically ignores sunk costs

**Cost of Delay components:**
- **User and business value** — Direct value to the customer or business
- **Time criticality** — Does value decay over time? Are there fixed deadlines?
- **Risk reduction / Opportunity enablement** — Does this item reduce risk or enable other value?

WSJF score = (User/Business Value + Time Criticality + Risk Reduction/OE) ÷ Job Size

All values are relative estimates (Fibonacci-like sequence). The highest WSJF items are pulled first from the backlog.

## Iteration Goals

Iteration Goals summarize the planned work for the iteration and are agreed upon by the team during Iteration Planning. They:
- Provide a shared team objective for the iteration
- Help manage dependencies with other teams
- Are tracked throughout the iteration (typically on a Kanban or planning board)
- Are evaluated at the Iteration Review to assess completion

## Related Pages

- [[SAFe-overview]] — ART and PI cadence in context
- [[SAFe-roles]] — Who participates in which events
- [[SAFe-backlogs-and-artifacts]] — What the backlog contains that gets planned
- [[SAFe-flow-and-delivery]] — Flow metrics measured at I&A
- [[SAFe-implementation-roadmap]] — How to launch the ART and prepare for first PI Planning
- [[SAFe-core-values-and-principles]] — Principles #7 (cadence) and #4 (incremental cycles) underpin all events
- [[SAFe-team-and-technical-agility]] — Team-level events (retrospectives, refinement, daily sync)
- [[SAFe-lean-portfolio-management]] — Portfolio Sync and Strategic Portfolio Review cadence
