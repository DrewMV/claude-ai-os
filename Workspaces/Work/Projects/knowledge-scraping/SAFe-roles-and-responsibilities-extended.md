---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, value-streams, customers, community, workspace]
updated: 2026-05-30
sources: [operational-value-streams, development-value-streams, business-value, customer-centricity, communities-of-practice, agile-workspaces, supplier, release-on-demand, portfolio-strategy]
summary: Value streams, customer-centricity, communities of practice, agile workspaces, suppliers, and release on demand — the extended operational context of SAFe.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.86
  inferred: 0.11
  ambiguous: 0.03
---

# SAFe Roles and Responsibilities Extended

This page covers key supporting concepts in SAFe beyond the primary roles and events: the two types of value streams, customer centricity, communities of practice, suppliers, agile workspaces, and release on demand.

## Two Types of Value Streams

Value streams are the most fundamental construct of Lean thinking in SAFe. Every enterprise has value streams — the sequences of steps used to deliver value to customers. SAFe identifies two types:

### Operational Value Streams (OVS)

**Definition:** The sequence of activities needed to deliver a product or service to a customer.

Examples: manufacturing a product, fulfilling an order, admitting and treating a patient, providing a loan, delivering a professional service.

OVS represent the primary work of most enterprise employees — those who directly serve customers in marketing, sales, order processing, manufacturing, and customer support. These are the value streams that Development Value Streams exist to support.

**Structure of an OVS:**
- **Trigger** — A customer request initiates the flow
- **Steps** — Activities that process the request
- **Flow Time** — Sum of all processing times plus delays between steps
- **Customers** — External (buyers/users) and internal (departments that use the output)

**Four common OVS types:**
1. **Fulfillment** — Processing a customer order for a digitally-enabled product or service (insurance, banking, eCommerce)
2. **Manufacturing** — Converting raw materials into products (medical devices, consumer goods, cyber-physical systems)
3. **Software Products** — Developing and supporting software applications for sale (SaaS, ERP, mobile apps)
4. **Supporting** — Internal, repetitive workflows (hiring, audits, supplier contracting, sales cycles)

**Key insight:** In most unoptimized value streams, wait time between steps consumes 89%+ of total flow time. Active value-added work is only 11% or less of flow time. This reveals the largest opportunity for improvement.

### Development Value Streams (DVS)

**Definition:** The sequence of activities needed to convert a business hypothesis into a digitally-enabled solution that delivers customer value.

DVS represent the work of developers, product managers, engineers, scientists, and IT practitioners. Each DVS is composed of one or more Agile Release Trains (ARTs).

**Structure of a DVS:**
- **Trigger** — A new feature request
- **Steps** — Define, build, validate, release
- **Output** — New increment of the product or solution
- **Customers** — Both internal (OVS users) and external (end users)

**Why DVS organization matters:**
- Enables long-lived, stable teams focused on delivering value
- Reveals delays, bottlenecks, and handoffs
- Supports smaller batches of work
- Enables value stream funding (Lean Budgets)
- Allows continuous learning about a specific domain

**DVS patterns matching OVS types:**
1. Fulfillment DVS (e.g., consumer loan origination systems)
2. Manufacturing DVS (e.g., automotive design tools and specifications)
3. Software Products DVS (e.g., ISV development and support)
4. Supporting DVS (e.g., ERP system development and maintenance)

**Value stream mapping applied to DVS:** In a typical example, only 5% of flow time is value-added work; 95% is waiting. Only 35% of features flow through without rework. This empirical data drives improvement focus.

**The relationship:** "The aim of development is, in fact, the creation of profitable operational value streams." (Allen Ward) — DVS exist to make OVS more efficient and effective, not as ends in themselves.

## Customer Centricity

**Definition:** A mindset that focuses on creating positive experiences for the customer through the full set of products and services that the enterprise offers.

Customer-centric organizations place customer needs at the center of every decision. Rather than just responding to feature requests, they invest in understanding deeper, ongoing customer needs.

### Two Types of SAFe Customers

- **Internal customers** — Part of the company; use solutions in operational value streams (e.g., bank underwriters using a credit scoring system built by the IT DVS)
- **External customers** — Outside the company; purchase, license, or use products and solutions (B2B, B2C, B2P)

Customers also exist within DVS chains — Product Managers consuming platform services are customers of the platform DVS, even though they're not end users.

### Whole Product Thinking

Customer-centricity requires considering the entire product, not just a set of features:

| Level | Description |
|---|---|
| MVP | Minimum Viable Product — proves/disproves the hypothesis |
| Core Product | Addresses basic functional needs minimally |
| Expected Product | What buyers typically expect (help, documentation, support) |
| Augmented Product | Features that delight and differentiate from competitors |
| Potential Product | Future features that sustain long-term customer interest |

Customers are satisfied only when actual value meets or exceeds perceived value.

### Research Methods for Customer Centricity

- **Empathy interviews** — Deep, one-on-one conversations to understand customer context and pain points
- **Gemba walks** — Observe customers in their actual work environment
- **Personas** — Representative user archetypes that guide design decisions
- **Customer journey maps** — Visualize the full customer experience across all touchpoints with the OVS
- **User research** — Drives product design; understands how users actually work
- **Market research** — Drives strategy; identifies market segments and competitive positioning
- **Usage analytics / telemetry** — Continuous measurement of actual customer behavior with the deployed solution

### Market Rhythms and Events

Customer-centric organizations leverage market timing:
- **Market rhythms** — Predictable, recurring patterns (holiday shopping, quarterly cycles) that inform release timing
- **Market events** — One-time significant events (competitor launches, regulatory changes, technology shifts) that may require adaptive releases

## Communities of Practice (CoPs)

**Definition:** Organized groups of people with a common interest in a specific technical or business domain who regularly collaborate to share information, improve skills, and advance their knowledge.

CoPs provide the cross-team, cross-ART knowledge sharing that complements the value stream-aligned team structure. While ARTs organize around delivering value, CoPs organize around building expertise.

### Three CoP Characteristics (Wenger)

1. **Domain** — An area of shared interest (e.g., DevOps, testing, product ownership)
2. **Practice** — A shared body of knowledge, experiences, and techniques
3. **Community** — Self-selected individuals who participate in regular interactions

### Why CoPs Matter in SAFe

Cross-functional teams optimize value flow but can create knowledge silos: software engineers need to talk to other software engineers; data scientists need peer conversations; Product Owners need to exchange practices. CoPs fill this gap.

**Benefits:**
- Rapid problem-solving through shared expertise
- Improved quality and craftsmanship
- Cooperation across functional and organizational boundaries
- Increased retention of top talent
- Autonomous, mastery, and purpose beyond daily ART tasks (satisfying Principle #8)

### Common CoP Types

**Role-based CoPs:**
- Scrum Master/Team Coach CoP — exchange practices for building high-performing teams
- Product Owner CoP — better feature writing, backlog management, customer engagement
- RTE CoP — ART coordination patterns, PI Planning facilitation

**Topic-based CoPs:**
- DevOps CoP — broad participation across roles
- Architecture CoP — design standards and emerging patterns
- Security CoP — security practices in the CD pipeline
- Value Stream Management CoP — flow metrics and DVS optimization

### CoP Participation Levels

- **Core team** — Organizes, charters, markets, and operates the community
- **Active** — Helps shape community vision and direction
- **Occasional** — Participates when specific topics are of interest
- **Peripheral** — Limited engagement; newcomers or observers
- **Transactional** — Access resources or provide specific services

CoPs are self-organizing; participation levels shift naturally. IP Iterations are an excellent time for CoP activities (learning sessions, coding dojos, coaching clinics).

### CoP Lifecycle

Conceptualize → Coalesce → Commit → Active → Retire. Healthy retirement spawns 3–5 new communities. Core team maintains health through simplicity, trust, rapid communication, and growing the shared knowledge base.

## Suppliers

Suppliers are internal or external organizations that develop and deliver components, subsystems, or services that help ARTs and Solution Trains deliver solutions.

Large-scale solution development almost always requires suppliers. SAFe principles for supplier relationships:
- **Long-term partnerships** over transactional, lowest-bid relationships
- **Win-win contracts** that create mutual benefit and accountability
- **Collaboration in SAFe events** — strategic suppliers participate in PI Planning, System Demos, and I&A
- **Trust-based relationships** — treat suppliers with the same respect as customers
- **Agile contracts** — outcome-based, scope-flexible agreements that support iterative development

## Release on Demand

**Definition:** The ability to release value to customers in one event or in waves based on market and business needs.

Release on Demand is the final aspect of the CDP. Key characteristics:
- Decouples deployment from release — code is deployed to production but released to customers at business timing
- Enables release timing aligned to market rhythms and events
- Uses feature flags, canary releases, A/B testing, and phased rollouts to control risk
- Maintains post-release activities that preserve solution stability and value

Different components release at different cadences — web services may release daily; hardware components only at major milestones. Decoupling eliminates the need for monolithic releases.

## Agile Workspaces

Agile workspaces are physical or virtual environments designed to enable the Lean-Agile ways of working:

- **Physical colocation** — Preferred for PI Planning when possible; enables richer collaboration and faster decisions
- **Visual management** — ART boards, team boards, PI Objective walls, risk boards — all work made visible
- **Collaboration tools** — Digital equivalents of physical boards (Jira, Miro, Rally, Azure DevOps)
- **Open, flexible spaces** — Reduce barriers between team members; enable cross-team coordination
- **Distributed team support** — Video conferencing, shared digital boards, asynchronous collaboration for distributed ARTs

Workspace design reflects the SAFe Core Value of transparency — making all work visible to all stakeholders.

## Portfolio Strategy

Portfolio strategy connects enterprise direction to portfolio execution:

- **Strategic Themes** — Differentiating business objectives that reflect the current enterprise strategy; express as OKRs
- **Portfolio Vision** — Desired future state of the portfolio's value streams and solutions
- **Portfolio Roadmap** — Long-horizon view integrating ART roadmaps into a comprehensive plan
- **Value Stream Alignment** — Organizing ARTs around value streams that deliver the strategic intent

Effective portfolio strategy requires "one portfolio" mindset — all value streams working toward shared goals, not locally optimizing against each other.

## Related Pages

- [[SAFe-lean-portfolio-management]] — Portfolio strategy, LPM, and value stream funding
- [[SAFe-roles]] — All roles including suppliers, customers, shared services
- [[SAFe-product-development-flow]] — Customer-centricity in product design
- [[SAFe-devops-and-technical-practices]] — Release on Demand and the CDP
- [[SAFe-leadership-and-culture]] — Communities of Practice and continuous learning culture
