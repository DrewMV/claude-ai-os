---
source_url: https://framework.scaledagile.com/art-and-solution-train-backlogs
scraped: 2026-05-30
authenticated: true
---

Home » ART and Solution Train Backlogs
ART and Solution Train Backlogs

The emphasis should be on why we do a job.

—W. Edwards Deming, Paraphrased from The New Economics for Industry, Government, Education [1]

Definition: The ART backlog is a Kanban system used to capture and manage the features and enablers that enhance the solution and extend its Architectural Runway.

Definition: The Solution Train backlog is a Kanban system used to capture and manage the capabilities and enablers intended to enhance the large solution and extend its Architectural Runway.

Summary

The Agile Release Train (ART) and Solution Train backlogs capture the upcoming features, capabilities, and nonfunctional requirements (NFRs). Product Management is responsible for the ART backlog, while Solution Management is responsible for the Solution Train backlog. Kanban systems help manage and visualize each backlog. The backlogs are regularly refined and prioritized to deliver customers the most valuable features and capabilities.

What are the ART & Solution Train backlogs?

The ART and Solution Train backlogs are Kanban systems that help track and manage features and improvements. The backlogs support and expand the products being developed by the ART or Solution Train. Product Management and Solution Management develop, maintain, and prioritize the ART and Solution Train backlogs. They collaborate with stakeholders, including customers, Business Owners, Product Owners (POs), System and Solution Architects, and others to discover features and capabilities and advance the solution.

Figure 1 illustrates the primary inputs to the ART and Solution Train backlogs:

Portfolio epics split into features or capabilities
Capabilities and enablers arising from the Solution Train's local context
Solution Train capabilities split into features and enablers
Features and enablers created from the ART's local context

Figure 1. Input sources for the ART and Solution Train backlogs

An effective Solution has to meet all its functional and nonfunctional requirements (NFRs). The NFRs shown at the bottom of the backlogs in Figure 1 are the constraints or restrictions across the backlog that affect the solution's design and performance. They are typically captured in acceptance criteria or as part of the definition of done (DoD). NFRs are persistent qualities, and ARTs often revisit them as part of the DoD.

How are these backlogs built and refined?

Product and Solution Management refine the backlogs with a continuous, flow-based approach. This ensures that features and capabilities are ready to be implemented with the right balance of discovery and risk. This often involves the following activities:

Discovering new features and capabilities
Reviewing and updating backlog item definitions, including developing acceptance criteria and benefit hypothesis
Identifying the enablers required to support new features and capabilities
Applying behavior-driven development (BDD) techniques to clarify features and capabilities or holding specification workshops
Prioritizing the backlogs using Weighted Shortest Job First (WSJF) in collaboration with Business Owners, System Architects, POs, and other stakeholders, such as RTEs/STEs
Briefing Agile Teams and stakeholders about upcoming features and capabilities for PI Planning
Removing backlog items that are no longer relevant

Refinement activities often occur during the PO Sync. A well-maintained backlog is essential for a successful PI Planning event.

Read more about Product and Solution Management:

Product Management
Solution Management

How are these backlogs managed within a Kanban system?

The ART and Solution Train Kanban system helps manage the flow of features and capabilities through the Continuous Delivery Pipeline (CDP). Figure 2 shows a typical ART or Solution Train Kanban with examples of the rules and work-in-progress (WIP) limits for each stage. While this provides a good foundation, the system should be tailored to meet the specific needs of the train. That requires setting WIP limits and defining the activities for each stage.

Figure 2. A typical ART or Solution Train Kanban system

The following describes the flow of the ART and Solution Train Kanbans.

Funnel – All big ideas are captured here and typically expressed as features or capabilities. They may indicate the need for new functionality, enhancement of existing system functions, or enablers.

Analyzing – Agile Teams explore these big ideas when they have available capacity. Analyzing includes continuous exploration activities (e.g., customer centricity, design thinking) and collaboration to create one or more well-formed features (see backlog refinement above). The WIP limit for this state considers the availability of Product or Solution Management, architects, the capacity of teams, and subject matter experts.

Ready – Product Management or Solution Management approves and prioritizes features and capabilities. These move to the ready state, where they wait to be implemented. WSJF is then applied to create a priority across the entire backlog.

Implementing – Features and capabilities are pulled into the Implementing state as teams begin to work on them throughout the PI.

Validating on staging – The validating on staging step has two sub-states, In progress and Ready:

In progress – Teams pull implemented and ready features into this state. They integrate and test them with the rest of the system in a staging environment and present them for approval.
Ready – Approved features and capabilities move to the 'ready' buffer, where they await deployment. This state is WIP-limited to avoid building up deployed but not yet released work.

Deploying to production – The deploying to production step also has two sub-states, In progress and Ready:

In progress – Features are moved to production immediately in an automated continuous delivery environment or to the in-progress state for manual deployment when capacity exists.
Ready – ARTs that separate deployment from release move the item to the ready buffer for deployment to production to await release. In other cases, features are automatically released, and users can access them immediately. This state is WIP-limited to avoid the buildup of deployed but unreleased features.

Releasing – When there is enough value and opportunity, the team releases features to some or all customers to evaluate the benefits.

Done – After a feature has been released and evaluated, it moves to the done state. However, new work items may be created based on customer feedback.

Read more about WSJF as a method of prioritization:

WSJF

How does capacity allocation help balance the backlog?

The backlog of business features or capabilities is balanced with investment in enablers. Enablers build and maintain the architectural runway, avoiding velocity reduction and technology obsolescence. Further, enablers support exploring requirements and applying design thinking for future PIs. This helps create prototypes and models and enhances visibility into opportunities and problem areas.

Collaborating during WSJF prioritization often serves to communicate concerns and arrive at a good balance of work. If that fails, Product and Solution Management may work with Architects to apply capacity allocation and determine the total effort the ART will reserve for each type of work in the coming PI. Figure 3 illustrates an example of capacity allocation in a PI.

Figure 3. Example capacity allocation for a PI

While the agreed-to capacity allocation can persist for several PIs, teams should periodically review and adjust it during backlog refinement in preparation for PI planning.

Read more about architectural runway and enablers:

Architectural Runway
Enablers

References

[1] Deming, W. Edwards. The New Economics for Industry, Government, Education. The MIT Press.

Key Takeaways
Agile Release Trains (ARTs) and Solution Trains use backlogs to capture the Solution's upcoming Features, Capabilities, and nonfunctional requirements.
Product and Solution Management refine the backlogs continuously.
The ART and Solution Train Kanban system helps manage the flow of Features and Capabilities through the continuous delivery pipeline.
Balancing business features and technical enablers is crucial for maintaining architectural runway and customer needs.

Last Update: 21 January 2025
