---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, teams, technical-agility]
updated: 2026-05-30
sources: [team-and-technical-agility-discipline, team-and-technical-agility, team-and-technical-agility-discipline_creating-great-agile-teams-competency, team-and-technical-agility-discipline_developing-quality-software-competency, team-and-technical-agility-discipline_launching-agile-business-teams-and-trains-competency, team-and-technical-agility-discipline_continuously-delivering-value-competency, team-and-technical-agility-discipline_marketing-with-agility-competency, team-and-technical-agility-discipline_implementing-the-architectural-runway-competency, built-in-quality, safe-scrum, safe-team-kanban, architectural-runway]
summary: Team and Technical Agility — Agile Team structure, ART operations, Built-in Quality, Continuous Delivery, and technical engineering practices.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.86
  inferred: 0.11
  ambiguous: 0.03
---

# SAFe Team and Technical Agility

Team and Technical Agility (TTA) describes the critical skills, roles, and practices that high-performing Agile Teams and Agile Release Trains (ARTs) use to create high-quality solutions for customers. TTA is one of SAFe's seven core competencies for Business Agility. An organization's ability to thrive in the digital age is entirely dependent on its teams' ability to deliver solutions that reliably meet customer needs.

TTA has three dimensions:
1. **Agile Teams** — High-performing, cross-functional teams anchoring the competency through effective Agile principles and practices
2. **Teams of Agile Teams** — ARTs provide shared vision, direction, and solution delivery at scale
3. **Built-In Quality** — All Agile teams apply defined practices to create high-quality, well-designed solutions

## Agile Teams

An Agile Team is a cross-functional group of **ten or fewer** individuals who can define, build, test, and deploy an increment of value in a short timebox. They are self-organizing and self-managing. Team members are dedicated full-time to the team, creating shared purpose and enhancing flow.

**Team roles:**
- **Product Owner (PO)** — Content authority for the team backlog; defines stories and prioritizes backlog; ensures alignment with customer needs and maximum business value
- **Scrum Master / Team Coach (SM/TC)** — Servant leader and Agile team coach; facilitates events; removes impediments; fosters high-performing team environment

**Team methods:**
- **SAFe Scrum** — Lightweight process for continuous value delivery; replaces ScrumXP from SAFe 5.1; regular schedule of events (iteration planning, review, retrospective, backlog refinement, team sync)
- **SAFe Team Kanban** — Lean-Agile method for teams with unpredictable workloads; visualize workflow, establish WIP limits, measure throughput, continually improve

Most teams use SAFe Scrum; Kanban is preferred when work is highly variable and iteration planning is less effective. Both approaches emphasize continuous delivery and ongoing process improvement.

## Agile Release Train (ART)

When a product is too large for a single Agile Team, multiple teams form an ART. ARTs are:
- Long-lived, virtual teams of 5–15 Agile Teams (typically 50–125 people)
- Cross-functional with all capabilities needed to define, build, validate, release, and operate solutions
- Organized around one or more value streams, aligned to a shared business and technology mission
- Plan together, commit together, execute together, and improve together

**ART roles:**
- **Product Management** — Defines desirable, feasible, viable, and sustainable products over the product-market lifecycle
- **System Architect** — Defines overall architecture; identifies NFRs; designs interfaces and collaborations between subsystems
- **Release Train Engineer (RTE)** — Servant leader and chief Scrum Master for the ART; facilitates ART events and artifacts; optimizes flow; coaches teams
- **Business Owners** — Primary stakeholders; responsible for fitness for use, governance, and ROI for the solution

**ART events:**
- **PI Planning** — Cadence-based face-to-face event; aligns all teams to shared mission; creates committed PI Objectives
- **System Demo** — Integrated view of new features after each iteration; objective evidence of ART progress
- **Inspect & Adapt (I&A)** — PI-end reflection and problem-solving workshop; identifies improvements for next PI
- **ART Sync** — Combines Coach Sync and PO Sync; coordinates dependencies and provides visibility into progress
- **IP Iteration** — Innovation and Planning iteration; exploration, learning, planning, and estimating buffer

## Built-In Quality

Built-In Quality (BiQ) is a set of practices to ensure Agile team outputs meet appropriate quality standards throughout value creation — not just before release.

Key insight: "Inspection does not improve quality. Quality cannot be inspected into a product or service; it must be built into it." (Deming)

**Why Built-In Quality matters:**
- Accelerates learning by shifting problem discovery left on the timeline
- Reduces the cost of fixing defects (exponentially more expensive later)
- Supports faster and more predictable flow (linked to Principle #6)
- Enables compliance, scalability, and innovation

SAFe applies Built-In Quality across five key domains:
1. **Flow** — WIP limits, small batches, fast feedback, stop-the-line quality
2. **Architecture and design quality** — Agile Architecture, design simplicity, emergent and intentional design
3. **Code quality** — Test-Driven Development (TDD), pair programming, collective code ownership, continuous integration, refactoring
4. **System quality** — Behavior-Driven Development (BDD), automated testing, system demos, NFR management
5. **Release quality** — Continuous Delivery Pipeline, definition of done, release on demand

## Architectural Runway

The Architectural Runway consists of existing code, components, and technical infrastructure needed to implement near-term features with minimal redesign and delay.

**Why it matters:** Emergent design alone cannot handle complexity at scale. Without adequate runway:
- Lack of standards increases delivery costs and delays
- One-off solutions become difficult to change and maintain
- Systems become vulnerable to security and stability issues
- Components have poor interoperability and reusability

**Intentional vs. emergent architecture:** The runway is built by balancing:
- **Emergent design** — architecture defined and extended only as necessary for the next increment
- **Intentional architecture** — centralized planning and cross-team coordination for foundational elements

Both are implemented via Enabler Features and Enabler Stories. Enabler epics/features support the architectural runway to provide future business functionality, including exploration, architecture, infrastructure, and compliance work.

## Continuous Delivery Pipeline (CDP)

Each ART either builds or shares a CDP that enables delivery of new functionality as needed — daily, weekly, or monthly depending on market demands. The CDP has four aspects:

| Aspect | Purpose |
|---|---|
| Continuous Exploration (CE) | Understand customer needs; define hypothesis and MMF |
| Continuous Integration (CI) | Integrate and test frequently; discover defects early |
| Continuous Deployment (CD) | Automate deployment to staging/production environments |
| Release on Demand | Release to customers when business needs it |

The CDP supports DevOps — a mindset of communication, integration, automation, and collaboration among everyone involved in planning, developing, testing, deploying, releasing, and maintaining a system.

## Technical Agility Practices

### Software Engineering
- Cloud-native development with microservices, Docker, Kubernetes, serverless
- Test-Driven Development (TDD) and Behavior-Driven Development (BDD)
- Continuous integration and automated regression testing
- Refactoring to extend the useful life of software assets
- Security-by-design and privacy-preserving techniques

### Hardware Engineering
Agile hardware engineering requires:
- **Rapid prototyping and testing** — build and test physical prototypes quickly to gather real-world data
- **Modular design** — components evolve independently through managed interfaces
- **Cross-functional collaboration** — break down hardware engineering knowledge silos
- **Vertical integration** — greater control over the development process, faster iteration

Hardware differs from software in tangibility, development cycles, flexibility, testing complexity, and cost of change. These differences require adaptations in how Agile principles are applied — longer iterations, more upfront planning, minimizing costly physical modifications.

## TTA Competencies

| Competency | Business Problem Addressed |
|---|---|
| Creating Great Agile Teams | Teams applying agile practices but slow to deliver and low on engagement |
| Developing Quality Software | Technical bottlenecks and frequent post-release defects with high maintenance costs |
| Launching Agile Business Teams | Not adapting to changing customer and market needs in operational departments |
| Continuously Delivering Value | No visibility into end-to-end delivery; slow, error-prone, inefficient |
| Implementing the Architectural Runway | Architecture defined up-front with minimal collaboration; hard to respond to change |
| Marketing with Agility | Marketing can't keep pace with emerging requirements and changing priorities |

## Measuring TTA

Key measurement tools:
- **Iteration Goals and PI Objectives** — measure whether committed outcomes are achieved
- **Employee Engagement** — higher engagement = higher productivity, efficiency, and innovation
- **Six Flow Metrics** — Flow Distribution, Velocity, Time, Load, Efficiency, Predictability — identify inefficiencies and guide application of flow accelerators

Improvement cycle:
1. Run routine retrospectives (team-level every iteration; ART-level I&A every PI)
2. Address impediments immediately
3. Share learnings across Agile teams (transparency, learning culture)

## Related Pages

- [[SAFe-overview]] — ART structure in the SAFe Big Picture
- [[SAFe-roles]] — Detailed role descriptions for PO, SM/TC, RTE, System Architect
- [[SAFe-planning-and-events]] — PI Planning, System Demo, Inspect & Adapt
- [[SAFe-devops-and-technical-practices]] — DevOps, CI/CD, TDD, BDD, and engineering practices
- [[SAFe-flow-and-delivery]] — Flow accelerators and the Continuous Delivery Pipeline
- [[SAFe-backlogs-and-artifacts]] — Team backlog, stories, enablers, NFRs
