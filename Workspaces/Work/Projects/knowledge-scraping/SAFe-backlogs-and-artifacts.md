---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, backlog, artifacts, requirements]
updated: 2026-05-30
sources: [portfolio-backlog, art-and-solution-train-backlogs, team-backlog, story, enablers, safe-requirements-model, solution-vision, solution-intent, solution-context, solution-demo, solution-management, solution-architect, nonfunctional-requirements, spikes]
summary: SAFe backlogs and artifacts — the four-tier requirements model, all backlog levels, story types, and key artifacts from epic to story.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.87
  inferred: 0.10
  ambiguous: 0.03
---

# SAFe Backlogs and Artifacts

SAFe uses a hierarchical requirements model that spans four levels — Portfolio, Solution Train, ART, and Team — with each level managing a Kanban backlog. The model scales from strategic epics down to team-level user stories, providing a coherent way to express system behavior across the entire enterprise.

## The SAFe Requirements Hierarchy

| Level | Work Item Type | Managed In |
|---|---|---|
| Portfolio | Epic (Business & Enabler) | Portfolio Backlog / Portfolio Kanban |
| Solution Train | Capability (Business & Enabler) | Solution Train Backlog |
| ART | Feature (Business & Enabler) | ART Backlog |
| Team | Story (User & Enabler), Spikes | Team Backlog |

**Cross-cutting:** Nonfunctional Requirements (NFRs) constrain all levels.

## Epics

Epics are the largest SAFe work items — large, typically cross-cutting initiatives that span multiple ARTs and often multiple PIs. They are managed in the Portfolio Backlog via the Portfolio Kanban.

**Two types:**
- **Business Epics** — Directly deliver business value to customers or stakeholders
- **Enabler Epics** — Advance the Architectural Runway to support upcoming business or technical needs

**Epic lifecycle:** Funnel → Reviewing → Analyzing → Ready → Implementing (MVP → Persevere) → Done

Key epic artifacts:
- **Epic Hypothesis Statement** — Describes the epic's intent and the value it expects to deliver
- **Lean Business Case** — Created during Analyzing phase; defines MVP, cost estimates, and business value
- **Minimum Viable Product (MVP)** — Smallest version of the epic that can test the hypothesis

Epics are done when: the hypothesis is proven, sufficient value is delivered, or Portfolio Leadership removes them from the Kanban.

## Capabilities

Capabilities are Solution Train-level work items describing the solution behaviors that span multiple ARTs. They are sized to fit within a single PI. Capabilities are split into Features for ART-level implementation.

## Features

Features are ART-level work items that fulfill stakeholder needs. Each feature includes:
- **Name** — Short phrase giving context
- **Benefit hypothesis** — The proposed measurable benefit to the end user or business
- **Acceptance criteria** — Conditions that must be met for the feature to be accepted

Features must be sized to fit within one PI. Features come from: local ART context, Epic decomposition, and portfolio-level strategic initiatives.

**Business Features** vs. **Enabler Features:**
- Business features deliver direct customer value
- Enabler features support the architectural runway (exploration, architecture, infrastructure, compliance)

## Stories

**Definition:** Short descriptions of a small piece of desired functionality written from the user's perspective.

Stories are the primary tool Agile Teams use to describe system behavior — a small, vertical slice of intended functionality that can be completed within a single iteration.

### User Stories

Format: "As a [user role], I want to [activity] so that [business value]"

This format guides teams to understand who uses the system, what they do with it, and why. Personas can replace generic user roles (e.g., "As Jane, I want...").

**3Cs of a good story:**
1. **Card** — Statement of intent on a card/sticky; limited size prevents premature specificity
2. **Conversation** — Promise of a conversation between team, customer/proxy, PO, and stakeholders; just-in-time discussions create shared understanding
3. **Confirmation** — Acceptance criteria that confirm correct implementation; automated tests where possible

**INVEST criteria for good stories:**
- **I**ndependent — not dependent on other stories for delivery
- **N**egotiable — a flexible statement of intent, not a contract
- **V**aluable — provides value to the customer
- **E**stimatable — small and understood enough to estimate
- **S**mall — fits within one iteration
- **T**estable — known enough to define tests

**Story estimation:** Teams use story points (relative sizing) and planning poker. Fibonacci sequence (1, 2, 3, 5, 8, 13, 20, 40, 100) reflects inherent uncertainty. Story velocity (completed points per iteration) becomes reliable for planning over time.

### Enabler Stories

Support exploration, architecture, infrastructure, or compliance work — not directly customer-visible but essential for future value delivery. Written in technical language; acceptance criteria still apply.

Common types: refactoring, spikes, build/deploy infrastructure improvements, performance testing, product configurations, compliance documentation.

### Spikes

Spikes are a type of enabler story used for exploration and research — time-boxed investigations to reduce uncertainty or validate technical assumptions. Spikes demonstrate knowledge gained or artifacts produced, not working functionality.

## Enablers (All Levels)

Enablers extend the Architectural Runway or improve the development value stream. They exist at every level:

| Level | Enabler Type |
|---|---|
| Portfolio | Enabler Epics (architectural, technical strategy) |
| Solution Train | Enabler Capabilities |
| ART | Enabler Features |
| Team | Enabler Stories, Spikes |

**Four categories of enablers:**
1. **Exploration** — Research, prototyping, validating customer needs and solution alternatives
2. **Architecture** — Build the Architectural Runway; enable smooth and fast delivery through the CDP
3. **Infrastructure** — Development and runtime environments; CI/CD infrastructure; cloud services
4. **Compliance** — Verification and validation (V&V), audits, policy automation, regulatory documentation

Enablers are prioritized like business items — they warrant capacity allocation and portfolio attention because they enable future value. Implement incrementally to avoid blocking delivery.

## Nonfunctional Requirements (NFRs)

**Definition:** System qualities that guide the design of the solution and often serve as constraints across the relevant backlogs.

NFRs specify how well the system performs, not what it does. Examples:
- **Performance** — Response time, throughput
- **Scalability** — Handling increased users or workload
- **Security** — Protection against unauthorized access and data breaches
- **Usability** — Ease of use
- **Maintainability** — Ease of updates and modifications
- Safety, reliability, compliance with regulatory standards

NFRs are persistent constraints — revisited as part of the Definition of Done (DoD) for each iteration, PI, or release. System Architects define NFRs and guide teams in addressing them. Over-specified NFRs make the solution too costly; under-specified NFRs make it inadequate or non-compliant.

## Team Backlog

The team backlog consists of user and enabler stories (and spikes). Most are identified during PI Planning and backlog refinement. The PO maintains and prioritizes it, ensuring it always contains work ready for the team.

Key practices:
- Continuously refined with new stories, reprioritized using Cost of Delay
- Managed as a Kanban with WIP limits
- Contains both PI-planned stories and locally generated stories from team context

## ART Backlog

The ART Backlog contains Features intended to address user needs and deliver business benefits for a single ART. Managed by Product Management with input from POs, System Architects, and Business Owners.

Key properties:
- Prioritized using WSJF (Weighted Shortest Job First)
- Contains business and enabler features; capacity allocation guardrails ensure a healthy mix
- Visualized in the ART Kanban system

## Solution Train Backlog

Contains Capabilities for the Solution Train to implement. Managed by Solution Management and prioritized using WSJF. Capabilities are split into Features for individual ART backlogs.

## Solution-Level Artifacts

### Solution Vision

Describes the future state of the solution — what it will do, the customers it will serve, and the problems it will solve. Aligns all ARTs and suppliers to a shared purpose. Maintained by Solution Management and Solution Architects; communicated at Pre-Plan and PI Planning.

### Solution Intent

The repository for storing, managing, and communicating the knowledge of current and intended solution behavior and design. Contains:
- **Fixed requirements** — Non-negotiable; must be met
- **Variable requirements** — Open for exploration; resolved as facts emerge
- Applicable standards, system models, functional and nonfunctional tests
- Traceability between requirements, design, and tests

Solution intent evolves alongside the solution — specifications are never complete up-front but grow incrementally as teams validate assumptions.

### Solution Context

Describes how the system will interface with, and be packaged and deployed in, its operating environment. Critical for large cyber-physical systems where the operating environment significantly impacts design decisions, development priorities, testing, and release governance.

### Solution Demo

Held at the end of each PI, the Solution Demo provides an integrated view of the complete solution — all ARTs' work integrated and demonstrated to stakeholders. Similar in purpose to the System Demo at ART level but spanning the entire Solution Train.

## PI Artifacts

### PI Objectives

Sets of business and technical goals each team and the ART commit to for the upcoming PI. Include committed objectives (high confidence) and uncommitted objectives (valuable but uncertain — provide capacity buffer and management visibility).

### ART Planning Board

Matrix created during PI Planning showing: features (by iteration and team), dependencies (cross-team work relationships), and milestones. Maintained throughout the PI for dependency management.

## Roadmap

The Roadmap communicates planned ART and value stream deliverables and milestones over a timeline. Types:
- **PI Roadmap** — Near-term delivery within the current and next PI
- **Product/Solution Roadmap** — Medium-term planned features and milestones
- **Portfolio Roadmap** — Multi-year strategic initiatives and investment horizons

Roadmaps are flexible rolling-wave planning tools, not fixed commitments. Every long-term commitment reduces agility.

## Related Pages

- [[SAFe-overview]] — Big Picture showing all backlog levels
- [[SAFe-roles]] — Who manages each backlog and artifact
- [[SAFe-planning-and-events]] — When backlogs are refined and planned
- [[SAFe-lean-portfolio-management]] — Portfolio Backlog and Kanban in detail
- [[SAFe-devops-and-technical-practices]] — How enablers enable the CDP and architectural runway
- [[SAFe-reference-glossary]] — Quick definitions for all key terms
