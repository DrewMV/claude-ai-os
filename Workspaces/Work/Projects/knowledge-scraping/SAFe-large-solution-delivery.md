---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, large-solution, systems-engineering]
updated: 2026-05-30
sources: [large-solution-integration-and-delivery-discipline, enterprise-solution-delivery, large-solution-integration-and-delivery-discipline_coordinating-large-solution-delivery-competency, large-solution-integration-and-delivery-discipline_lean-systems-engineering-competency, large-solution-integration-and-delivery-discipline_large-solution-roadmapping-competency, large-solution-integration-and-delivery-discipline_organizing-around-value-for-large-solutions-competency, solution-train, coordinate-and-deliver, pre-plan, solution-intent]
summary: Large Solution Integration and Delivery — how SAFe coordinates multiple ARTs and suppliers to build complex cyber-physical and enterprise systems.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.86
  inferred: 0.11
  ambiguous: 0.03
---

# SAFe Large Solution Delivery

The Large Solution Integration and Delivery (LSID) Discipline describes how to apply SAFe principles and practices to the specification, development, operation, and evolution of the world's largest and most sophisticated software, hardware, and cyber-physical systems. This includes defense systems, satellites, autonomous vehicles, large enterprise software platforms — any solution requiring the coordination of 6 to 60+ ARTs.

Traditional approaches to large systems — detailed upfront specifications, fixed schedules, big-batch handoffs — create false positive feasibility, constrain innovation, and prevent adjustment based on learning. LSID applies Lean-Agile methods at scale to solve these challenges.

## When Large Solution is Needed

Large Solution SAFe applies when:
- Solutions require multiple ARTs and suppliers to coordinate delivery
- A single ART cannot deliver the complete solution within a reasonable timeframe
- Solutions have an unacceptable social or economic cost for failure
- Solutions are subject to industry and regulatory standards requiring objective evidence of compliance
- Solutions are part of a larger "system-of-systems" with an extended supply chain

## Value Stream Structures at Scale

Large solutions are built by large value streams composed of multiple Solution Trains, ARTs, teams, and suppliers. Two key structures:

- **Nested value streams** — multiple development value streams that must collaborate to deliver a single integrated solution (e.g., multiple ARTs contributing subsystems to one product)
- **Networked value streams** — multiple development value streams maintaining alignment to deliver various related solutions

Key principle: "There is more value created with overall alignment than with local excellence." (Reinertsen)

All value streams operate on the **same cadence**, enabling synchronized planning, alignment, review, and improvement events.

## The Solution Train

The Solution Train is the organizational construct used to build large solutions requiring coordination of multiple ARTs and suppliers.

### ART Topologies within a Solution Train

| ART Type | Purpose |
|---|---|
| Stream-Aligned ART | Has all skills and authority to deliver a full product, service, or major component |
| Complicated Subsystem ART | Manages a unique, specialized subsystem; reduces cognitive load on stream-aligned ARTs |
| Platform ART | Provides services and infrastructure that stream-aligned ARTs extend and build on |
| Enabling ART | Provides specialty tools, services, or expertise to other ARTs |

### Solution Train Roles

- **Solution Management** — Defines desirable, feasible, viable, and sustainable large-scale solutions; represents customers and business to the ARTs
- **Solution Architect** — Defines and communicates shared technical and architectural vision across the Solution Train; works with System Architects to guide solution design
- **Solution Train Engineer (STE)** — Coach for the Solution Train; facilitates and guides all ARTs and suppliers; works with RTEs to coordinate delivery
- **Suppliers** — Internal or external organizations developing components, subsystems, or services
- **Business Owners** — Key stakeholders with final responsibility for business outcomes; may also serve as Business Owners for individual ARTs
- **Customers** — Work closely with Solution Management to define and adjust vision, intent, and delivery roadmap
- **System Team** — Formed at the Solution Train level to address integration issues across ARTs
- **Shared Services** — Specialty roles and services required for Solution Train success but not dedicated full-time

### Solution Train Responsibilities

1. **Connecting with the customer** — Feedback is critical; Solution Train leadership actively works to bridge the organizational gap between builders and those who can provide the best input
2. **Planning and roadmapping** — Pre-Plan activities align ARTs before PI Planning; rolling-wave roadmaps maintain alignment across ARTs and suppliers
3. **Building solution capabilities** — Capabilities describe higher-level solution behaviors that span multiple ARTs; sized to fit within a PI; split into Features for ART-level implementation
4. **Coordinating ARTs and suppliers** — Common cadence, Solution Train Syncs, Solution Demos; strategic suppliers participate in planning events
5. **Releasing and release governance** — Release management function with authority to foster and approve releases; automated testing in CDP addresses quality; additional governance for high-stakes systems

## Key Artifacts

### Solution Intent

Solution Intent is the repository for storing, managing, and communicating the knowledge of current and intended solution behavior and design. It includes:
- Fixed requirements — non-negotiable; must be met
- Variable requirements — subject to further exploration as facts surface; allowing variability to proceed (even late) is vital to agility in large solutions
- Applicable standards and references
- System models, functional and nonfunctional tests
- Traceability between requirements, design, and tests

Solution intent evolves alongside the solution. Early specifications are written in the language of **intent** — describing the future state without overly constraining how it is delivered. Each PI increment validates assumptions, producing a new vertical slice of requirements, designs, implementations, and tests.

### Solution Vision and Roadmap

Vision provides a clear and motivating description of the future to inspire and align all solution builders across many value streams. Roadmaps at multiple levels (ART, Solution Train, Portfolio) connect to:
- Communicate what each value stream plans to deliver
- Illustrate dependencies between value streams
- Ensure capacity alignment for local and large-solution customers
- Facilitate trade-off decisions to maximize cross-value stream value

### Solution Demo

Each PI, the Solution Train conducts a Solution Demo — an integrated view of all ARTs' work for the PI, demonstrated to key stakeholders. This provides the objective evidence of progress needed for governance and decision-making.

## Pre-Plan (formerly Pre-PI Planning)

Pre-Plan describes activities that align and prepare ARTs within a Solution Train for PI Planning. Goals:
- Ensure all ARTs enter PI Planning aligned on shared vision, goals, and objectives
- Identify Solution Train Capabilities and cross-ART dependencies to address during individual ART PI Planning events
- Align Strategic Suppliers on their role in the upcoming PI

## Coordinate and Deliver (formerly Post-PI Planning)

After ARTs complete PI Planning, Coordinate and Deliver aligns the Solution Train on the combined PI plan:
- Aggregates individual ART PI objectives into a coherent Solution Train plan
- Identifies and resolves cross-ART dependencies and risks
- Establishes the Solution Demo plan for the PI
- Aligns suppliers on their integration milestones

## Architecture for Change

Large solutions must be architected for continuous evolution, not one-time delivery. Key architectural principles:
- **Decouple components** — components interact through managed interfaces; can evolve independently
- **Modular design** — reduces dependencies between value streams; simplifies management
- **Solution Context** — understand the operating environment; it impacts solution intent, design, development priorities, testing, and release governance
- **Agile Architecture** — balance emergent and intentional design; Architectural Runway supports rapid feature delivery

## LSID Competencies

| Competency | Business Problem Addressed |
|---|---|
| Coordinating Large Solution Delivery | Struggle to coordinate value delivery across multiple teams, specialists, and suppliers |
| Organizing Around Value for Large Solutions | Larger projects and more systems = slower delivery and more missed deadlines |
| Lean Systems Engineering | Engineering practices haven't kept pace with technological advancement |
| Large Solution Roadmapping | Large solution planning is fragmented and misaligned |
| Large Solution Vision | Lack of unified understanding leads to fragmented solutions and misaligned ARTs |
| Supplier Collaboration | Suppliers not effectively integrated into the innovation and delivery process |

## Mindset Shifts for Large Solutions

| Traditional | LSID Approach |
|---|---|
| Driven by outputs (deliver a feature list) | Driven by outcomes (change user behavior) |
| Fix schedule early; strive to meet it | Forecast delivery with roadmaps; adjust based on learning |
| Commit early to detailed specifications | Specify the solution incrementally with clear intent |
| Communicate via initial documentation | Communicate via cadence-based events and evolving specification |
| Regulatory/quality testing at end | Continually address quality based on frequent system integration |
| Deliver once; modernize later | Deliver early; evolve live solutions continuously |

## Related Pages

- [[SAFe-overview]] — Large Solution and Full SAFe configurations
- [[SAFe-roles]] — Solution Management, Solution Architect, STE, Solution Train Engineer
- [[SAFe-planning-and-events]] — PI Planning, Pre-Plan, Coordinate and Deliver, Solution Demo
- [[SAFe-backlogs-and-artifacts]] — Capabilities, solution vision, solution intent, solution context
- [[SAFe-team-and-technical-agility]] — ART structure and practices that scale up to large solutions
- [[SAFe-devops-and-technical-practices]] — Set-Based Design, architecture for large systems
