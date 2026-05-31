---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, devops, technical, tdd, bdd, architecture]
updated: 2026-05-30
sources: [devops, devops-practice-domains, calmr, continuous-exploration, continuous-deployment, continuous-integration, agile-testing, agile-architecture, behavior-driven-development, test-driven-development, domain-modeling, set-based-design, agile-contracts]
summary: SAFe DevOps and technical practices — CALMR, CDP practices, TDD, BDD, Agile Architecture, Set-Based Design, and engineering excellence.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.87
  inferred: 0.10
  ambiguous: 0.03
---

# SAFe DevOps and Technical Practices

DevOps is a mindset, culture, and set of technical practices that support the integration, automation, and collaboration needed to effectively develop and operate a solution. It is a key component of the Agile Product Delivery competency and the foundation for the Continuous Delivery Pipeline (CDP).

Without DevOps, there is significant tension between those who build solutions and those who support and maintain them. DevOps breaks down those silos and creates a high-performance innovation engine capable of delivering market-leading solutions at the speed of business.

**DevOps performance impact (Google DORA research):** Teams that successfully adopt DevOps deploy 208× more frequently, 106× faster, experience 7× fewer failures, and recover from incidents 2,604× faster than low-performing teams.

## CALMR: SAFe's DevOps Mindset

CALMR provides the shared mindset and values for successful DevOps adoption in SAFe (SAFe's adaptation of the community's CALMS, replacing "Sharing" with "Recovery"):

### Culture
- Break down organizational silos between development, QA, IT operations, infosec, and the business
- Foster shared responsibility for the full lifecycle: plan, develop, test, deploy, release, maintain
- "Imagine a world where product owners, Development, QA, IT Operations, and Infosec work together... to enable the fast flow of planned work into production, while achieving world-class stability, reliability, availability, and security." (DevOps Handbook)
- Psychological safety to experiment, learn from failures, and improve continuously

### Automation
- Automate as much of the build, test, and deployment pipeline as possible
- Infrastructure as Code (IaC) — treat infrastructure provisioning like software
- Automated regression testing — every code change triggers tests
- Automated deployment — changes flow through environments without manual intervention
- Eliminate manual, error-prone handoffs that introduce delays and defects

### Lean Flow
- Apply flow accelerators from Principle #6 to the CDP
- Limit WIP; work in small batches; reduce queue length
- Eliminate bottlenecks in the pipeline
- Fast feedback loops at every stage

### Measurement
- Instrument the system to provide telemetry and operational feedback
- DORA metrics: Deployment frequency, Lead time for changes, Time to restore service, Change failure rate
- Flow metrics applied to the pipeline: active time, wait time, %C&A (percent complete and accurate)
- Use metrics to drive improvement, not blame

### Recovery
- Design for failure: assume systems will fail and optimize MTTR (Mean Time to Recover)
- Feature flags / feature toggles enable targeted releases and quick rollback
- Blue/green deployments, canary releases, and A/B testing
- Automated rollback capabilities
- Chaos engineering to proactively discover failure modes

## Agile Testing

Agile Testing develops and tests systems in small increments, often writing tests before code (test-first). Key principles:
- Quality is built-in from the beginning, not inspected in at the end
- All team members share responsibility for testing
- Tests help elaborate and define system behavior before implementation
- Automated tests wherever possible — they become the definitive statement of as-built behavior

**Test types in the Agile testing pyramid:**
1. Unit tests (bottom, most numerous) — fast, automated, developer-written
2. Component tests — test larger architectural subsystems
3. Integration tests — verify components work together
4. End-to-end / acceptance tests (top, fewest) — test full system behavior from user perspective

## Test-Driven Development (TDD)

**Definition:** A philosophy and practice involving building and executing tests before implementing the code.

TDD is a core Built-In Quality practice. The cycle:
1. **Write the test first** — Ensure the developer understands required behavior
2. **Run the test (watch it fail)** — Verifies the test works and shows how the system fails without code
3. **Write the minimum code to pass the test** — Iteratively until the test passes
4. **Continue until all tests pass** — Confidence that changes meet requirements and don't break existing behavior
5. **Refactor** — Continuously improve design to support changing requirements (enables emergent design)

**Unit tests** from TDD give developers confidence to refactor without introducing regressions. They also allow QA/test personnel to focus on more complex behaviors and interactions rather than code-level bugs.

**Test doubles** (mocks, stubs, fakes) accelerate testing by substituting slow, unavailable, or expensive components with faster proxies.

## Behavior-Driven Development (BDD)

**Definition:** A test-first, Agile Testing practice that defines tests before or as part of specifying system behavior. BDD creates a shared understanding of requirements between business and Agile teams.

BDD tests are business-facing scenarios describing system behavior from a user's perspective — not internal implementation details. When automated, they ensure the system continuously meets specified behavior as it evolves (enabling Release on Demand).

**The BDD Triad:** Three cognitive perspectives needed to define behavior clearly:
- Customer-centric stakeholders — desirability and viability
- Development-centric stakeholders — feasibility
- Test-centric stakeholders — exceptions, edge cases, boundary conditions

**The BDD process:**
1. **Discovery** — PO/PM creates acceptance criteria; team collaborates to discover additional criteria
2. **Formulation** — As backlog item approaches implementation, formalize acceptance criteria into detailed acceptance tests using Given-When-Then (GWT) format
3. **Automation** — Automate acceptance tests using frameworks (Cucumber, FIT); run continuously for regression protection

**GWT example:**
```
Given: speed limit is 50 mph
When: the car drives
Then: its speed is between 49 and 50 mph
```

BDD acceptance tests replace traditional requirement specifications — they are simultaneously a requirement and a test.

## Agile Architecture

**Definition:** A set of values, practices, and collaborations that support a system's active, evolutionary design and architecture.

Agile Architecture avoids Big Design Up Front (BDUF) while providing enough intentional structure to support large-scale solution delivery. Key properties:
- **Collaboration** — architects work with teams, not in silos
- **Design simplicity** — simplest architecture that meets current and near-term needs
- **Balance of intentional and emergent design** — some centralized planning for foundational elements; teams own local design decisions
- **Design for testability, deployability, and releaseability** — architecture enables the CDP

**Architectural Runway** is maintained through a balance of intentional architecture (cross-team coordination for foundational elements) and emergent design (teams evolve architecture as they learn). Both implemented via Enabler Epics, Features, and Stories.

Agile architects support business alignment by:
- Identifying and eliminating architectural bottlenecks to value flow
- Communicating technical objectives in clear business terms
- Leading legacy modernization initiatives incrementally
- Maintaining just enough Architectural Runway to support evolving business needs

## Set-Based Design (SBD)

**Definition:** A Lean development practice that keeps requirements and design options flexible for as long as possible during the development process.

SBD applies SAFe Principle #3 — Assume variability; preserve options. Instead of committing to a single point-based solution early (in the "cone of uncertainty"), teams explore multiple options simultaneously and eliminate weaker choices based on validated learning.

**SBD vs. Point-Based Design:**
- **Point-based:** Commit early to one set of requirements and one design → high risk if assumptions are wrong → late discovery → emergency rework
- **Set-based:** Maintain multiple design options → explore and validate → converge as knowledge grows → better technical and economic outcomes

**Key SBD practices:**
1. **Increase interface flexibility** — System engineers specify ranges for requirements at intersection points; interfaces remain negotiable longer
2. **Leverage modeling, simulation, and prototyping** — Digital twins, CAD, design thinking, UX prototypes to learn cheaply before committing
3. **Collapse options with frequent integration points** — System Demos (each iteration) and Solution Demos (each PI) provide experiential learning that narrows design alternatives
4. **Take a systems view** — Technology decisions must consider future capabilities, not just current initiative
5. **Make decisions based on economic trade-offs** — Balance development expense, lead time, product cost, value, and risk across design options

**When SBD is most valuable:** High degree of technological innovation, variability in market/customer conditions, or fixed delivery deadlines where wrong early choices are expensive to correct.

## Continuous Integration (CI)

Continuous Integration requires teams to integrate their code frequently (at least daily) into a shared repository where automated builds and tests are triggered. Benefits:
- Defects discovered immediately when code is integrated, not weeks or months later
- Forces small batch sizes — teams integrate small changes, not large batches
- Provides rapid feedback on whether new code meets quality standards
- Enables the "system always runs" goal of Agile development

CI pipeline components: version control, automated build, automated unit tests, automated component tests, staging environment integration.

## Continuous Deployment (CD)

Continuous Deployment takes changes from the staging environment and deploys them to production automatically (or with minimal manual approval). Benefits:
- Eliminates manual, error-prone deployment processes
- Enables deployment at any time without scheduled maintenance windows
- Allows feature flags and partial rollouts for risk control
- Decouples deployment from release (can deploy without releasing to users)

## Continuous Exploration (CE)

Continuous Exploration ensures ARTs continuously understand what to build next. Activities:
- Customer research and market analysis
- Design thinking workshops (empathy maps, journey maps, personas)
- Hypothesis formation and Lean UX experiments
- Feature definition with benefit hypothesis and acceptance criteria
- ART backlog prioritization using WSJF

## DevOps Practice Domains

SAFe organizes DevOps technical practices into four practice domains aligned with the CDP:
1. **Continuous Exploration** — customer and market research, design, requirements
2. **Continuous Integration** — build, test, integrate automation
3. **Continuous Deployment** — deployment automation, environment management
4. **Release on Demand** — feature flags, release governance, monitoring, operational readiness

## Domain Modeling

Domain modeling creates a shared understanding of the problem domain between technical and business stakeholders. It uses language from the customer's domain to express system behavior, reducing translation errors between business requirements and technical implementation. Enables Ubiquitous Language — the same terms used in code, tests, and conversations.

## Agile Contracts

Agile contracts reflect the Lean-Agile approach to supplier and customer agreements. Key principles:
- Favor outcome-based contracts over specification-based (fixed scope) contracts
- Build in mechanisms for scope flexibility and learning
- Establish long-term partnership relationships over transactional, lowest-bid approaches
- Align supplier incentives with customer outcomes

## Related Pages

- [[SAFe-flow-and-delivery]] — CDP, flow metrics, and Measure and Grow
- [[SAFe-team-and-technical-agility]] — Built-in Quality, architectural runway, and team practices
- [[SAFe-backlogs-and-artifacts]] — Enablers for exploration, architecture, and infrastructure
- [[SAFe-large-solution-delivery]] — Set-Based Design in large solution context
- [[SAFe-governance-and-compliance]] — Compliance enablers and agile contracts
