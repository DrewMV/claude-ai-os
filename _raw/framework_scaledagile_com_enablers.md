---
source_url: https://framework.scaledagile.com/enablers
scraped: 2026-05-30
authenticated: true
---

Home » Enablers
Enablers

Luck is what happens when preparation meets opportunity.

– Widely attributed to Seneca, Roman philosopher and playwright

Definition: Enablers are backlog items that extend the architectural runway of the solution under development or improve the performance of the development value stream.

Summary

Enablers are used to describe the work needed to support research, evolve architecture and infrastructure, refine code and essential infrastructure, and ensure regulatory compliance. They are managed in the appropriate backlog as epics, capabilities, features, or stories. While enablers have a distinct classification, they are treated and managed similarly to customer-facing backlog items.

What is an enabler?

Enablers define the work needed to develop and deliver future business requirements. Teams use them to explore ideas, improve architecture, strengthen infrastructure, and manage compliance. Because enablers produce tangible outputs, they must be visible and treated like other backlog items. They generally fall into one of four categories:

Exploration – supports research, prototyping, and other actions needed to understand customer needs, including exploring possible solutions and evaluating alternatives

Architecture – used to build the Architectural Runway, allowing smoother and faster development through the Continuous Delivery Pipeline (CDP)

Infrastructure – helps create and improve the development and runtime environments that underpin the systems used to build, test, deploy, and manage solutions

Compliance – facilitates managing specific compliance activities, including verification and validation (V&V), audits and approvals, and policy automation

More details on each of these types and how they are used are included below.

How are enablers identified and defined?

Enablers are common in SAFe. They are written and prioritized according to the same rules as epics, features, capabilities, and stories.

Enabler epics are similar to business epics and are written using the 'epic hypothesis statement' format. They can span multiple Agile Release Trains (ARTs) and PIs. They are managed via the Portfolio Backlog and associated Kanban system.
Enabler features and capabilities are defined by ARTs and Solution Trains and include a short phrase, benefit hypothesis, and acceptance criteria. They must be sized to fit within a single PI.
Enabler stories must fit within Iterations like any story. Although they may not require the user voice format, their acceptance criteria clarify the requirements and support testing.

Architects often define and guide enabler epics, features, and capabilities. They might be Enterprise Architects supporting the portfolio, System Architects supporting ARTs, or Solution Architects supporting Solution Trains. They steer enablers through the appropriate Kanban system and backlog, guiding implementation from concept to delivery. Agile Teams also use enablers; enabler stories emerge locally from their needs and are managed in the team backlog.

Read more about features and epics:

Features and Capabilities
Epics

Exploration Enablers

Exploration enablers are used for requirements discovery activities and exploring design options. The nature of product and solution development is that many requirements begin with variable intent. Teams know little about what the customer needs or how to implement it at the beginning of development. And customers themselves often don't understand precisely what they need. Through continuous exploration, teams progressively learn which aspects of the product or solution intent should move from variable to fixed.

There are usually several technical options to satisfy a business need or opportunity, and it's essential to analyze them. Common evaluation methods include modeling, prototyping, set-based design, or applying the lean startup cycle. Exploration enablers can help to manage and sequence these activities. They visualize the work and ensure that the outcomes of the exploration align with the needs of customers and stakeholders.

Architecture Enablers

The architectural runway consists of the existing code, components, and infrastructure needed to implement near-term features with minimal redesign and delay. It ensures that Agile Teams and ARTs can deliver products and solutions quickly with minimal delay. However, new epics, features, capabilities, and stories continually consume the runway. Architectural enablers help extend the runway to be ready for new functionality.

Architecture enablers can also address problems with the resiliency of deployed solutions. After implementation, they often reflect nonfunctional requirements (NFRs) that constrain future backlog items. NFRs frequently begin as architectural enablers and grow over time.

Figure 1. Many NFRs appear over time as a result of enablers

Read more about NFRs:

Nonfunctional Requirements (NFRs)

Infrastructure Enablers

Agile development requires frequent integration. Agile teams integrate their work and showcase the working increment at the System Demo. Similarly, ARTs in a solution train integrate their work as frequently as possible during the PI in preparation for Solution Demos. Infrastructure enablers provide continuous integration and deployment technology to support these regular integration points.

The System Team is integral in defining and building the infrastructure enablers that enhance the development environment and streamline the CDP. Shared Services, operations teams, and Site Reliability Engineering (SRE) use infrastructure tools to provide cloud services. These help speed up development and make it easier to scale.

Read more about the System Team:

System Team

Compliance Enablers

By building the necessary artifacts of the solution intent over a series of PIs, SAFe supports continuous verification and validation (V&V). These activities are part of the development workflow and are often enforced in the definition of done (DoD). Their artifacts are developed throughout the development lifecycle, ensuring they meet the evidence requirements by the end of the development process. Validation occurs when Product Owners, customers, and end-users are involved in PI Planning and System Demos to approve the fitness for purpose. Enablers support these activities.

Consider a regulation that requires design reviews and documenting the actions that these reviews set into motion. A 'design review enabler' backlog item would offer evidence of the review. Its definition of done (DoD) would ensure that actions were recorded and resolved according to the lean quality management system (QMS). If needed, the activities could be tracked as enabler stories.

Read more about Solution Intent:

Solution Intent

How are enablers implemented incrementally?

Enablers provide the essential foundation for effective product and solution development. Thus, they warrant portfolio attention regarding budgeting and capacity allocation. However, since their value is linked to future business objectives, it is crucial to implement them quickly and iteratively. If not, the delivery of customer value may be delayed, undermining the purpose of the enabler.

Enablers improve economics by creating technology platforms that deliver optimal business functionality. However, innovative product development cannot occur without risk-taking. Therefore, initial technology decisions cannot always be correct. This is why Lean-Agile organizations must be willing to change course occasionally. In these cases, the principle of sunk costs [2] is valuable: Do not consider money already spent. Implementing incrementally allows adjustments before the investment grows too large.

Enablers of all types should be implemented incrementally. However, as architectural and infrastructure enablers may influence the delivery and operation of mission-critical solutions, they warrant additional guidance.

The size and demands of architectural and infrastructure enabler work can be overwhelming. So, it's important to remember to split them into features and stories to be delivered incrementally. However, This can be difficult as architectural and infrastructure changes can keep the existing system from working until the changes are in place.

The work must be sequenced to ensure the system can continue operating in the current environment while enablers are implemented. That way, teams can continue to work, integrate, demo, and even release new functionality.

There are three approaches: [1]

Case A – The enabler is big, but implementation is incremental. The system always runs (operates).
Case B – The enabler is big but can't be implemented incrementally. The system will need to take an occasional break.
Case C – The enabler is huge and can't be implemented incrementally. The system runs when needed.

Enabler epics and capabilities can cut across multiple value streams or ARTs. During the analysis stage of the appropriate Kanban system, it is important to determine whether to implement the enabler across all ARTs simultaneously or incrementally.

In scenario A, the enabler is implemented first in ART 1 and then by the other ARTs in subsequent PIs. This may lessen the impact of the change across the portfolio, but it can delay all the benefits of a fully implemented enabler. By contrast, scenario B calls for all ARTs to implement the enabler at the same time. If the cost of delaying the implementation is unacceptable, this is preferable.

References

[1] Leffingwell, Dean. Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise. Addison-Wesley Professional, 2010.

[2] Reinertsen, Donald G. The Principles of Product Development Flow: Second Generation Lean Product Development. Celeritas Publishing, 2009.

[3] Fowler, Martin. Strangler Fig Application. MartinFowler.com, June 29, 2004.

Key Takeaways
Enablers extend the architectural runway of the product or solution under development.
Enablers typically fall into one of four categories: exploration, architecture, infrastructure, or compliance.
Defining and managing enablers follows the same rules as epics, features, capabilities, and stories.

Last Update: 25 February 2025
