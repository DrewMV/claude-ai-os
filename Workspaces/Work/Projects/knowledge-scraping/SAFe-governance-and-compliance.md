---
workspace: Work
project: knowledge-scraping
category: SAFe Framework
tags: [work, agile, safe, framework, governance, compliance, risk, government]
updated: 2026-05-30
sources: [lean-governance, compliance, agile-risk-management, agile-hr, agile-contracts, capex-and-opex, guardrails, government]
summary: SAFe governance and compliance — Lean Governance, compliance in Agile, risk management, CapEx/OpEx, agile contracts, HR, and SAFe for Government.
base_confidence: 0.9
lifecycle: draft
tier: supporting
provenance:
  extracted: 0.87
  inferred: 0.10
  ambiguous: 0.03
---

# SAFe Governance and Compliance

SAFe provides a comprehensive approach to governance and compliance that is compatible with Lean-Agile development. Rather than deferring compliance to the end or treating governance as a separate, waterfall-style process, SAFe integrates compliance into the development workflow — making quality and compliance everyone's job, not just the regulatory team's.

## Lean Governance

**Definition:** Lean governance provides oversight of spending, audit, security, compliance, expenditure, measurement, and reporting in a SAFe portfolio.

Lean governance is a critical aspect of [[SAFe-lean-portfolio-management]]. It enables enterprise leaders to maintain appropriate oversight while supporting the decentralized decision-making that enables business agility.

### Key Lean Governance Activities

**Dynamic forecasting and budgeting:**
- Value stream budgets adjusted on a regular cadence (typically at PI boundaries or significant events)
- Historical and forecasted future costs inform budget decisions
- Guardrails guide the mix of investments across horizons
- Real-time visibility via PI System Demos and VMO data

**Continuous measurement:**
- Regular portfolio performance assessment across Outcomes, Flow, and Competency
- Early identification of underperforming areas and bottlenecks
- Data-driven decisions rather than opinion-driven governance

**Collaboration and transparency:**
- Close collaboration between Portfolio Leadership, VMO, Business Owners, and Enterprise Architects
- Shared understanding of strategic objectives and resource allocation priorities
- Participatory budgeting (Strategic Investment Planning) for collaborative funding decisions

**Adjusting value stream budgets:**
- Dynamic reallocation as market conditions shift and priorities evolve
- Resources directed to areas of highest value and impact
- Lean budgets prevent the rigid annual cycles that impede agility

**Compliance automation:**
- "Organizations need an automated way to track governance throughout the entire software delivery process so they can attest to the integrity of all assets and the security of all running applications." (Investments Unlimited)
- Automated governance, risk, and compliance (GRC) enables organizational goals faster while improving flow

## Compliance in Agile Development

**Definition:** Compliance refers to the strategy, activities, and artifacts that allow teams to apply Lean-Agile development methods while ensuring they meet regulatory, industry, and other relevant standards.

High-assurance systems built by SAFe organizations include: medical devices, automobiles, avionics, banking and financial services, aerospace, and defense. These face extensive regulatory oversight and rigorous compliance requirements.

### The Problem with Traditional Compliance

Traditional QMS (Quality Management Systems) are based on phase-gated waterfall methods:
- All specifications defined up-front before any system behavior is known
- Large batches of compliance activities deferred to the end
- Late discovery of compliance issues → expensive rework
- Compliance becomes a bottleneck before release, not a quality-building process throughout

**Deming's insight:** "Inspection is too late. The quality, good or bad, is already in the product."

### Five SAFe Practices for Compliance

**1. Build the Solution and Compliance Incrementally**
- Each PI increment assesses viability AND compliance progress
- Specifications evolve in small batches with faster feedback
- PDCA cycles (Plan-Do-Check-Adjust) provide rapid learning on both functionality and compliance
- Early feedback on fitness for use; avoid large compliance events at the end

**2. Organize for Value and Compliance**
- ARTs include all skills needed for compliance: QA, security, testing, V&V specialists
- Cross-functional teams with embedded compliance competency
- Solution and Product Management ensure Solution Intent and backlog reflect compliance requirements
- Communities of Practice keep compliance specialists connected to regulatory changes

**3. Build In Quality and Compliance**
- Built-In Quality is the mechanism for compliance — quality is a culture, not a job title
- Compliance activities automated wherever possible
- Manual compliance activities (FMEA, audits) planned as stories in the team backlog
- Definition of Done includes compliance checkpoints — making final approval a quick, boring "non-event"
- PIs and retrospectives provide feedback loops for compliance activities

**4. Continuously Verify and Validate (V&V)**
- Verification: the system works as designed
- Validation: the system meets the intent of its purpose and functions
- Solution Intent provides the repository for requirements, designs, and traceability
- Each increment yields new tests; automation prevents testing from becoming a bottleneck
- All material requirements (features, stories, NFRs) have test cases created at the same time as functionality

**5. Make V&V and Compliance Part of Flow**
- V&V performed in small batches as part of each work item
- Definition of Done includes reviews, audits, and sign-offs for compliance items
- System Demo evaluates compliance progress alongside functionality
- Release on Demand includes validation testing, regulatory approvals where required

### Compliance in Regulated Environments

Final release may require additional compliance activities beyond sprint/PI-level work:
- Validation testing of the final release candidate (medical trials, flight tests)
- Review of objective evidence for production approval
- Customer/user acceptance tests and regulatory submissions

These are planned as part of the development process — not an afterthought.

## Agile Risk Management

Agile risk management embeds risk identification and mitigation into the development process rather than treating it as a separate, sequential activity.

Key practices:
- **Risk identification in PI Planning** — Teams identify risks to their PI Objectives; ROAM technique (Resolved, Owned, Accepted, Mitigated) addresses risks transparently
- **Risk as backlog items** — Risk mitigations converted to Agile stories; managed in the backlog with priority based on CoD
- **Continuous risk assessment** — Risk is re-evaluated at each iteration as new functionality introduces new combinations that may create new risks
- **Cross-functional risk teams** — Risk experts embedded in ARTs and Solution Trains; Communities of Practice maintain regulatory expertise

**Collaborative risk mitigation:** Risk management sessions held with the full solution team — product management, engineering, quality, regulatory, operations — to think through all possible failure modes and design mitigations before they occur.

**Risk Masters (medical device example):** Organizations have created hybrid roles combining Scrum Master facilitation skills with risk management expertise. Risk managers shadow Scrum Masters; regulatory specialists embed in Agile teams; nurses rotate through teams to maintain clinical context.

## CapEx and OpEx in Lean-Agile

See [[SAFe-lean-portfolio-management]] for full CapEx/OpEx guidance. Summary:

**Operating Expenses (OpEx):** Ongoing costs of running the business — salaries, administrative costs, training, supplies, rent. Recorded in the period they occur.

**Capital Expenses (CapEx):** May include some software development labor when developing intangible assets (software, IP, patents). Requirements:
- Technical feasibility established
- Management has committed to fund and execute the development

**Agile CapEx tracking approaches:**
- By story hours (most granular)
- By story points (most common; low overhead)
- By story count (simple proxy)

Feature-level work (implementing new software functionality) is the primary candidate for CapEx treatment. Exploration, refactoring, infrastructure maintenance, and defect fixes are typically expensed (OpEx).

## Agile Contracts

Traditional contracts create adversarial supplier relationships based on fixed scope, lowest-bid competition, and penalty clauses for changes. Agile contracts apply the same Lean-Agile principles as product development:

**Key principles:**
- **Outcome-based** rather than specification-based — define what value must be delivered, not how
- **Scope flexibility** — build in mechanisms for learning and changing direction as facts emerge
- **Long-term partnerships** over transactional relationships — "end the practice of awarding business on the basis of price tag" (Deming)
- **Win-win** — supplier incentives aligned with customer outcomes; mutual benefit over adversarial negotiation
- **Agile contract formats** — shorter, more frequent contracts; iterative delivery with milestones; shared risk/reward models

## Agile HR

Traditional HR practices — annual performance reviews, forced stack rankings, individual incentive compensation — conflict with Lean-Agile principles and undermine the collaborative, team-based culture SAFe requires.

Agile HR principles:
- **Continuous feedback** over annual reviews — frequent check-ins; coaching conversations
- **Team-based incentives** over individual competition — reward collective outcomes, not individual metrics
- **Purpose and mastery** over bonus-chasing — connect compensation to collective purpose
- **Growth and development** as a continuous practice — learning plans, coaching, cross-functional skill development
- **Flexible workforce** — T-shaped skills, Communities of Practice, cross-team mobility

## SAFe for Government

SAFe for Government applies Lean-Agile values, mindset, principles, and practices to public sector organizations with specific adaptations for government context.

### Why Government is Different

Governments face unique challenges:
- Mission agility (not profit-driven; success = mission value delivered to citizens)
- Limited and rigid funding mechanisms (multi-year appropriations, non-reallocation rules)
- Acquisition and procurement regulations
- Complex contractor/government team relationships
- Political and oversight environments
- Technical debt and legacy system modernization
- Regulatory compliance for defense, healthcare, and financial systems

### Nine Government-Specific SAFe Topics

1. Building on a solid foundation of Lean-Agile values, principles, and practices
2. Creating high-performing teams of government and contractor personnel
3. Aligning technology investments with agency strategy
4. Transitioning from projects to a lean flow of epics
5. Adopting Lean budgeting aligned to development value streams
6. Applying Lean estimating and forecasting in cadence
7. Modifying acquisition practices to enable Lean-Agile development and operations
8. Building in quality and compliance
9. Adapting governance practices to support agility and lean flow of value

### Common Government Adaptations

- **Language changes:** "Business Value" → "Mission Value"; "Customer" → "Citizen" or "Public Servant"
- **Acquisition patterns:** Modular contracting; multiple award task orders; performance-based contracting
- **Budget alignment:** Working within annual appropriations cycles while implementing value stream funding within those constraints
- **Compliance integration:** DevSecOps with automated compliance in the pipeline; FedRAMP, NIST, DoD CMMC compliance built into Definition of Done
- **Security:** Continuous security validation in the CD pipeline

**Current adoption:** 80%+ of U.S. government programs use some form of Agile or iterative development. However, Agile practices are often limited to development teams. SAFe addresses program and portfolio challenges: strategy alignment, budgeting, planning, acquisitions, governance, and compliance.

## Related Pages

- [[SAFe-lean-portfolio-management]] — Lean Budgets, Guardrails, CapEx/OpEx, and LPM governance
- [[SAFe-core-values-and-principles]] — Principle #1 (economic view) and transparency as a core value
- [[SAFe-devops-and-technical-practices]] — DevSecOps, compliance automation, and agile contracts
- [[SAFe-ai-and-emerging-topics]] — Responsible AI governance and Big Data governance
- [[SAFe-backlogs-and-artifacts]] — Compliance enablers in the backlog
