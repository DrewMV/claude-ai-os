---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, roles, responsibilities]
updated: 2026-05-30
sources: [agile-release-train, agile-teams, product-owner, product-management, release-train-engineer, scrum-master-team-coach, system-architect, business-owners, portfolio-leadership, enterprise-architect, epic-owner, solution-train-engineer, shared-services, system-team, lace]
summary: All SAFe roles — definitions, responsibilities, and key relationships at team, ART, Solution Train, and portfolio levels.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.88
  inferred: 0.09
  ambiguous: 0.03
---

# SAFe Roles

SAFe defines roles at every level — Agile Team, Agile Release Train (ART), Solution Train, and Portfolio. Each role has clear content authority, technical authority, or value delivery responsibilities. This page synthesizes all major SAFe roles, their definitions, key responsibilities, and relationships.

## Agile Team Roles

### Product Owner (PO)

**Definition:** The Agile team member primarily responsible for maximizing the value delivered by the team by ensuring the team backlog is aligned with customer and stakeholder needs.

The PO is the "voice of the customer" on the Agile Team — the primary advocate for customer needs and business strategy. This is a full-time role for each Agile team.

**Five areas of responsibility:**
1. **Connecting with the customer** — Develop whole-product solutions; know the customer; know the stakeholders; identify problems worth solving
2. **Contributing to the vision and roadmap** — Understand market forces; represent the end user; assist with ART backlog prioritization; educate the ART during PI Planning
3. **Managing and prioritizing the team backlog** — Guide story creation; prioritize by Cost of Delay; accept stories against Definition of Done; support architectural runway
4. **Supporting the Agile Team** — Balance stakeholder perspectives; elaborate stories; foster built-in quality; participate in team and ART events
5. **Getting and applying feedback** — Test benefit assumptions; obtain feedback from customers and stakeholders; share feedback with the ART; evolve solution design

**Key relationships:** Bridges Product Management (strategy) and the Agile Team (execution). Partners closely with SM/TC, Product Management, System Architect, and other POs (via PO Sync).

### Scrum Master / Team Coach (SM/TC)

**Definition:** A servant leader and coach for an Agile Team who facilitates team events and processes, and supports teams and ARTs in delivering value.

Organizations may choose either name — Scrum Master or Team Coach. SM/TCs may be full-time or part-time depending on team size and context.

**Key attributes:** Empathy, conflict navigation, servant leadership, mentoring, transparency, coaching beyond Scrum.

**Five areas of responsibility:**
1. **Facilitating PI Planning** — Prepare teams; draft PI plans; coordinate with other teams; create PI objectives; review business value assignments
2. **Supporting iteration execution** — Facilitate team events (planning, sync, review, retrospective, refinement); work within ART cadence; collaborate with PO
3. **Improving flow** — Establish team Kanban board; measure and optimize with flow metrics; build quality in
4. **Building high-performing teams** — Foster Agile team attributes; encourage high-performing dynamics; develop T-shaped skills; resolve conflicts; coach with powerful questions
5. **Improving ART performance** — Facilitate cross-team collaboration; build trust with stakeholders; coach IP Iteration; facilitate I&A problem-solving workshop

**Key relationships:** Partners with RTE for ART-level coordination; represents team in Coach Sync, PO Sync, and ART Sync; participates in SM/TC Community of Practice.

## ART Roles

### Product Management

**Definition:** The function responsible for defining desirable, viable, feasible, and sustainable solutions that meet customer needs and supporting development across the product life cycle.

One or more Product Managers may serve an ART (especially for complex systems or multiple products). They bridge business strategy, customer needs, and Agile Team capability.

**Five areas of responsibility:**
1. **Exploring markets and users** — Primary/secondary research; market segmentation; identify market rhythms and events; understand user needs
2. **Connecting with the customer** — Customer-centric mindset; empathy interviews; design thinking; continuous customer involvement in PI Planning and System Demos
3. **Defining product strategy, vision, and roadmaps** — Encourage innovation; align strategy to business objectives; establish value exchange models; communicate compelling vision; manage flexible roadmaps
4. **Managing and prioritizing the ART backlog** — Guide feature creation; prioritize features with WSJF and CoD; accept features; support Architectural Runway
5. **Delivering value** — Release on demand; ensure product completeness; enable operations (marketing, sales, compliance); measure business value

**Key relationships:** Co-leads the ART with System Architect, RTE, and Business Owners. Informs POs about market trends and features. When serving as Epic Owner, creates Lean Business Cases.

### System Architect

**Definition:** Responsible for defining and communicating a shared technical and architectural vision for the solutions developed by an ART.

An ART may have multiple System Architects, each focusing on a specific domain (security, cloud, data, UI). They work with Enterprise and Solution Architects for cross-ART alignment.

**Five areas of responsibility:**
1. **Aligning architecture with business priorities** — Define enablers and architectural runway; participate in solution definition; define system NFRs; ensure capacity for enablement work
2. **Defining and communicating architecture vision** — Present architectural vision at PI Planning; provide guidance during execution; architect for agility and change using abstraction and set-based design
3. **Evolving system design with teams** — Support architectural experiments and spikes; collaborate on optimal design; align architectural intent with implementation reality
4. **Fostering built-in quality and NFRs** — Promote architectures that shift learning left; maintain NFR standards and definition of done
5. **Supporting DevOps and CDP** — Participate in release governance; support CDP design including cloud infrastructure; enable metrics instrumentation for Lean UX

**Key relationships:** Part of ART leadership alongside Product Management, RTE, and Business Owners. Works with Enterprise Architects for portfolio alignment. Pairs with Agile Teams on technical decisions.

### Release Train Engineer (RTE)

**Definition:** A servant leader and ART coach who facilitates ART events and processes, and supports teams in delivering value.

The RTE is the chief Scrum Master/Team Coach for the ART — a servant leader role, not a traditional manager. The critical shift is from telling people what to do to helping them discover what to do themselves.

**Five areas of responsibility:**
1. **Facilitating PI Planning** — Help ART prepare (backlog, vision, logistics); facilitate the two-day event (agenda, Coach Sync, risk management, confidence vote)
2. **Supporting PI execution** — Maintain progress visibility; facilitate ART events (ART Sync, System Demo, I&A); support ART backlog refinement; promote DevOps; coordinate with other ARTs
3. **Coaching the ART** — Coach with powerful questions; coach ART event facilitation; coach ART roles (Business Owners, System Architects, Product Managers)
4. **Optimizing flow** — Establish ART Kanban; measure flow metrics (predictability, flow time, etc.); apply flow accelerators; facilitate value stream mapping; reduce/eliminate cross-team dependencies
5. **Improving relentlessly** — Drive relentless improvement via I&A; leverage SAFe assessments; collaborate with VMO and LACE on transformation strategy

**Key relationships:** Partners with SM/TCs and Product Managers for ART execution. Coordinates with STEs in Solution Train context. Provides input to VMO and LACE for portfolio-level improvements.

### Business Owners

**Definition:** A small group of key stakeholders with primary business and technical responsibility for governance, compliance, and return on investment (ROI) for solutions developed by the ART.

Business Owners are not a role held by one person but a small group. They are the primary stakeholders in the ART.

**Key responsibilities:**
- Participate in pre-PI Planning to review priorities and capacity allocations
- Present business context at PI Planning; assign business value to team PI objectives; approve final plans
- Provide feedback during System Demos and Solution Demos
- Participate in I&A workshops; evaluate actual value versus plan
- Provide ongoing governance and compliance oversight

**Key relationships:** Work with Portfolio Leadership on strategy; partner with Product Management and System Architects to ensure investment targets the right things.

## Portfolio Roles

### Portfolio Leadership

A team of business, technology, and finance leaders responsible for modernizing portfolio management and enabling strategy agility. Typically the executive team (for a single portfolio) or senior leaders accountable for each portfolio (in multi-portfolio enterprises).

**Key responsibilities:**
- Formulate and communicate portfolio strategy aligned with enterprise strategy
- Maintain portfolio vision and roadmap
- Facilitate Strategic Investment Planning (formerly Participatory Budgeting)
- Establish and adjust Lean Budgets and Guardrails
- Manage the Portfolio Kanban (with VMO support)
- Conduct Strategic Portfolio Reviews and Portfolio Syncs
- Measure portfolio performance with OKRs and KPIs

### Enterprise Architect

Works within the Portfolio Leadership team to establish the portfolio's technology vision, strategy, and roadmap. Promotes adaptive design and engineering practices. Typically serves as Epic Owner for Enabler Epics (those that advance the architectural runway).

**Key responsibilities:**
- Guide enabler epics through the portfolio Kanban
- Promote architecture governance across the portfolio
- Balance intentional and emergent design to maintain a healthy Architectural Runway
- Support the technical feasibility evaluation of business epics

### Epic Owner

**Definition:** Responsible for coordinating epics through the portfolio Kanban system.

Epic Owners shepherd epics from the funnel through reviewing, analyzing, and into implementation. They:
- Collaborate with stakeholders to define the epic, Lean business case, and MVP definition
- Coordinate the epic through the portfolio Kanban; bring insights to LPM for Go/No-go decisions
- Coordinate implementation across multiple ARTs once approved
- Work with Agile Teams on MVP development and evaluation

Product Managers often serve as Epic Owners for business epics. Enterprise Architects serve as Epic Owners for enabler epics.

## Solution Train Roles

### Solution Management

Defines and supports building desirable, feasible, viable, and sustainable large-scale business solutions. Represents customers and business needs to the ARTs. Content authority for the Solution Train.

### Solution Architect

Defines and communicates a shared technical and architectural vision across the Solution Train. Works with ART System Architects to guide their portion of the solution's design. Technical authority for the Solution Train.

### Solution Train Engineer (STE)

The coach for the Solution Train — the "RTE of the Solution Train." Facilitates and guides all ARTs and suppliers; coordinates Pre-Plan and Coordinate and Deliver activities; works with RTEs on ART execution.

## Supporting Roles

### Shared Services

Specialists who cannot be dedicated full-time to a single ART or Solution Train. Examples: data security, legal/compliance specialists, site reliability engineering (SRE), UX specialists. Support multiple ARTs/trains as needed.

### System Team

A specialized Agile Team that assists in building and using the continuous delivery pipeline infrastructure and, where necessary, validating full end-to-end system performance. May exist at ART level, Solution Train level, or both.

### SAFe Practice Consultants (SPCs)

Trained change agents who implement and sustain SAFe across the enterprise. Facilitate SAFe training courses, coach transformations, and participate in the LACE and guiding coalition. Formerly called SAFe Program Consultants.

### LACE (Lean-Agile Center of Excellence)

See [[SAFe-lean-portfolio-management]] for full LACE description. A small dedicated Agile team (4–6 people for ~100s of practitioners) that drives the day-to-day SAFe transformation across the enterprise.

## Role Summary Table

| Role | Level | Responsibility Type |
|---|---|---|
| Product Owner | Team | Content authority (team backlog) |
| Scrum Master/Team Coach | Team | Value delivery (facilitation, coaching) |
| Product Management | ART | Content authority (ART backlog/vision) |
| System Architect | ART | Technical authority |
| Release Train Engineer | ART | Value delivery (coaching, facilitation) |
| Business Owners | ART/Portfolio | Governance, ROI |
| Epic Owner | Portfolio | Epic coordination |
| Enterprise Architect | Portfolio | Technical authority (portfolio) |
| Portfolio Leadership | Portfolio | Strategy, investment, governance |
| Solution Management | Solution Train | Content authority |
| Solution Architect | Solution Train | Technical authority |
| Solution Train Engineer | Solution Train | Value delivery |
| SPC | Enterprise | Transformation coaching |
| LACE | Enterprise | Transformation coordination |

## Related Pages

- [[SAFe-overview]] — ART and Solution Train structures
- [[SAFe-planning-and-events]] — How roles participate in PI Planning and other events
- [[SAFe-lean-portfolio-management]] — Portfolio Leadership, Epic Owner, VMO, LACE roles in detail
- [[SAFe-backlogs-and-artifacts]] — Which roles own and manage each backlog level
- [[SAFe-team-and-technical-agility]] — Team-level roles (PO, SM/TC) in ART and technical context
- [[SAFe-implementation-roadmap]] — Roles involved in the SAFe transformation journey
- [[SAFe-large-solution-delivery]] — Solution Management, STE, Solution Architect roles
- [[SAFe-lean-portfolio-management]] — Portfolio Leadership, VMO, and LACE
- [[SAFe-large-solution-delivery]] — Solution Train roles in detail
- [[SAFe-backlogs-and-artifacts]] — What each role owns and manages
