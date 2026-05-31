---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, flow, delivery, metrics, okrs]
updated: 2026-05-30
sources: [accelerating-flow-with-safe, continuous-delivery-pipeline, art-flow, team-flow, solution-train-flow, portfolio-flow, value-stream-management, value-stream-coordination, value-stream-kpis, measure-and-grow, implementation-roadmap, coaching-flow, okrs]
summary: SAFe flow and delivery — Continuous Delivery Pipeline, flow accelerators at all levels, Measure and Grow metrics (outcomes/flow/competency), and OKRs.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.87
  inferred: 0.10
  ambiguous: 0.03
---

# SAFe Flow and Delivery

SAFe is fundamentally a flow-based system. The goal is to deliver a continuous flow of value to customers in the "shortest sustainable lead time." This page covers the Continuous Delivery Pipeline, flow at each SAFe level, flow accelerators, measurement, and OKRs.

## The Continuous Delivery Pipeline (CDP)

**Definition:** The workflows, activities, and automation needed to guide new functionality from ideation to on-demand release of value.

Each ART builds, manages, or shares a CDP. It enables ARTs to deliver new functionality as needed — from daily to monthly releases depending on market context.

### Four Aspects of the CDP

| Aspect | Purpose | Key Activities |
|---|---|---|
| **Continuous Exploration (CE)** | Understand what to build | Customer research, design thinking, hypothesis formation, feature definition and prioritization |
| **Continuous Integration (CI)** | Build and verify frequently | Code implementation, automated testing, build, end-to-end integration, staging validation |
| **Continuous Deployment (CD)** | Deploy to production safely | Deploy changes to production; verify and monitor; business decides release timing |
| **Release on Demand (RoD)** | Release at business timing | Release to customers when timing is optimal; control risk; maintain post-release stability |

The CDP is not strictly linear — it's a learning cycle. During every PI and iteration, ARTs simultaneously: explore user value, integrate and demo value, continuously deploy to production, and release value whenever the business needs it.

**Decoupling deployment from release** is a critical enabler of Release on Demand. Some CDP components (web services) may release daily; others (hardware) only at major cycles. Decoupling allows each component to release at its own cadence without creating monolithic releases.

### Mapping and Improving the CDP

To improve the existing pipeline:
1. **Value stream mapping** — Document every step from idea to production release
2. **Measure key metrics** — Active time, wait time, %C&A (percent complete and accurate)
3. **Identify improvement targets** — Eliminate wait states (often the biggest problem), address low %C&A steps that cause rework
4. **Reduce batch sizes** — Smaller batches flow faster, accumulate less variability, provide faster feedback

DevOps teams that successfully adopt CDP practices deploy 208× more frequently, 106× faster, experience 7× fewer failures, and recover from incidents 2,604× faster than low-performing teams.

## CALMR: SAFe's Approach to DevOps

The CDP is enabled by a DevOps mindset guided by CALMR:
- **Culture** — Collaboration across dev, QA, IT Ops, infosec; break down organizational silos
- **Automation** — Automated testing, builds, deployments, and compliance checks
- **Lean Flow** — WIP limits, small batches, fast feedback, stop-the-line quality
- **Measurement** — Metrics to track and improve CDP performance (DORA metrics: deployment frequency, lead time for changes, time to restore, change failure rate)
- **Recovery** — Ability to roll back, fix forward, and restore service rapidly

## Flow at Each SAFe Level

### Team Flow

A state where Agile Teams deliver a continuous flow of value to the customer. Teams achieve flow by:
- Maintaining a continuously refined team backlog
- Working in short iterations with minimal WIP
- Establishing a team Kanban board with WIP limits
- Applying Built-in Quality practices
- Using team retrospectives to identify and eliminate flow impediments

### ART Flow

A state where the ART delivers a continuous flow of value to the customer. ART-level flow is enabled by:
- PI Planning creating aligned, coordinated plans
- Regular System Demos demonstrating integrated, working software
- ART Kanban managing feature flow through the CDP
- ART Sync events monitoring and adjusting during the PI
- Inspect & Adapt driving systematic improvement

### Solution Train Flow

Flow at the Solution Train level coordinates multiple ARTs and suppliers. Key mechanisms:
- Pre-Plan aligning ARTs before PI Planning
- Coordinate and Deliver aggregating PI plans and resolving cross-ART dependencies
- Solution Demo providing integrated view of all ARTs' work
- Solution Train Kanban managing capability flow

### Portfolio Flow

Portfolio flow manages the flow of epics through the portfolio Kanban. Key elements:
- Portfolio Kanban with WIP limits at each state
- Strategic Portfolio Reviews and Portfolio Syncs managing flow
- LPM adjusting budgets and priorities based on portfolio flow data
- Value Stream Management providing visibility across all value streams

## Value Stream Management (VSM)

**Definition:** A leadership and technical discipline that enables the maximum flow of business value through end-to-end solution delivery.

VSM provides portfolio-level visibility into value flow across the enterprise. Key practices:
- Value stream mapping to visualize end-to-end flow
- Identifying and eliminating bottlenecks across the full delivery pipeline
- Measuring value stream KPIs to evaluate business outcomes
- Coordinating dependencies between value streams

**Value Stream Coordination** — Managing dependencies and exploiting opportunities between value streams within a portfolio. Value streams operating in isolation miss opportunities for differentiated, portfolio-level capabilities that competitors cannot match.

## Measure and Grow

**Definition:** An approach SAFe enterprises use to evaluate progress towards Business Agility and determine improvement actions.

SAFe measures business agility across three domains, applied at every level (team, ART, Solution Train, portfolio):

### Domain 1: Outcomes

Do solutions meet the needs of customers and the business?

| Metric | Description |
|---|---|
| **KPIs** | Specific, quantifiable measures of results for value streams; ongoing health metrics |
| **OKRs** | Aspirational goals describing specific outcomes the portfolio aims to achieve; measured quarterly |
| **Iteration Goals / PI Objectives** | Measure whether teams are achieving committed outcomes each iteration and PI |
| **Employee Engagement (eNPS)** | Motivation and engagement level; predicts productivity, quality, and retention |

### Domain 2: Flow

How efficient is the organization at delivering value?

| Metric | What It Measures | Why It Matters |
|---|---|---|
| **Flow Distribution** | Proportion of work by type (features, enablers, defects, risks) | Ensure healthy balance between new value and technical investment |
| **Flow Velocity** | Number of backlog items completed per timeframe (throughput) | Higher = more output; drops signal problems needing investigation |
| **Flow Time** | Total time from ideation to production for a work item | Shorter = faster customer value delivery; lower Cost of Delay |
| **Flow Load** | Number of items currently in the system (WIP) | High load → long wait times; limiting WIP accelerates flow |
| **Flow Efficiency** | Active time ÷ total flow time (expressed as percentage) | Typically low (<10%) in unoptimized systems; indicates bottleneck severity |
| **Flow Predictability** | Actual business value delivered ÷ planned business value per PI | Target 80–100%; reflects planning reliability and ART performance |

**DORA Metrics** (DevOps performance): Deployment frequency (flow velocity), lead time for changes (flow time), time to restore service (flow time for incidents), change failure rate.

### Domain 3: Competency

How proficient is the organization in the practices that enable agility?

- One assessment per SAFe Discipline and core competency
- Business Agility assessment for portfolio/enterprise level
- DevOps Health Radar for CDP maturity (four aspects × four activities)
- Process: Run assessment → analyze results → take action → celebrate successes

**Critical success factors for effective measurement:**
1. Use metrics alongside direct observation (Gemba) — numbers alone are incomplete
2. Apply metrics only where they improve decision-making — avoid over-measuring
3. Understand behavioral effects — metrics tied to compensation create gaming; emphasize transparency over individual accountability
4. Interpret carefully — metrics without context are misleading; understand what's actually flowing

## OKRs (Objectives and Key Results)

**Definition:** A collaborative framework for establishing clear goals and measurable outcomes.

OKRs in SAFe are optional (except for portfolio Strategic Themes). Three recommended use cases:

### Use Case 1: Enhancing Strategic Alignment (Portfolio)

Strategic themes are strongly recommended to be defined as OKRs. This provides:
- Clear, measurable outcomes connecting enterprise strategy to portfolio execution
- Cascading OKRs from portfolio → value stream → ART
- Direct line-of-sight from team work to business outcomes

OKRs inform value stream and solution KPIs — the key results define the specific outcomes that KPIs must track.

### Use Case 2: Defining Epic Outcomes (Portfolio Kanban)

Apply OKRs to define business outcomes in epic hypothesis statements and lean business cases:
- Objective: The expected outcome if the epic hypothesis is correct
- Key Results: Measurable conditions that prove/disprove the hypothesis
- Used to define MVP scope and measure pivot-or-persevere decisions

### Use Case 3: SAFe Transformation Goals

Apply OKRs to measure the outcomes of the SAFe transformation itself — improvements in quality, time-to-market, and predictability.

**Caution: Do NOT use OKRs for PI Objectives.** PI Objectives work best as SMART statements (clear, immediately actionable). OKRs with 3–5 key results take too long to write during PI Planning and their lagging indicators are rarely achievable within a single PI timebox.

**Writing good OKRs:**
- **Objectives:** Inspirational, clear and memorable, committed or aspirational (mark which), doing work or improving work
- **Key Results:** Value-based (outcomes not outputs), measurable with a target number, gradable (increase from X to Y; stay above/below Y)

Measure progress quarterly (at Strategic Portfolio Reviews); build solution telemetry into the CDP to enable continuous measurement.

## Related Pages

- [[SAFe-core-values-and-principles]] — Principle #6 (Make value flow) and eight flow accelerators
- [[SAFe-team-and-technical-agility]] — Team Flow and Built-in Quality
- [[SAFe-lean-portfolio-management]] — Portfolio Flow and LPM events
- [[SAFe-devops-and-technical-practices]] — CALMR, CDP practices, DevOps technical domains
- [[SAFe-planning-and-events]] — Inspect & Adapt metrics, PI predictability
- [[SAFe-backlogs-and-artifacts]] — Backlog artifacts that flow through the CDP
