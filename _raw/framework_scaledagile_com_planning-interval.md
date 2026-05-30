---
source_url: https://framework.scaledagile.com/planning-interval
scraped: 2026-05-30
authenticated: true
---

Home » Planning Interval (PI)
Planning Interval (PI)

Unless commitment is made, there are only promises and hopes; but no plans.

– Peter F. Drucker

Definition: A Planning Interval (PI) is a cadence-based timebox in which Agile Release Trains deliver continuous value to customers in alignment with PI Objectives.

Summary

A Planning Interval (PI) is a timebox of 8-12 weeks, during which the Agile Teams on an ART deliver the work needed to meet their PI Objectives. The most common PI structure includes four or five development iterations and one Innovation and Planning (IP) iteration. Applying a PI adds cadence to Agile Release Trains (ARTs) in the same way an iteration does to Agile Teams. The PI facilitates planning, building, validating, delivering value, and obtaining quick feedback within a fixed timeframe.

What is a PI?

A PI is an 8 to 12-week timebox consisting of four or five development iterations, followed by an Innovation and Planning (IP) iteration. This structured approach promotes effective planning and encourages rapid validation and value delivery, allowing teams to gather quick feedback and continuously improve.

During the PI, Agile Teams apply cadence and synchronization to collaborate effectively and release multiple increments of value. Individual teams may also release value independently, depending on context. The cadence and synchronization of the PI enables the ART to:

Plan the ART's next increment of work
Limit work in process (WIP)
Demonstrate progress and gather feedback
Collectively address systemic problems

The PI is divided into a series of iterations. Figure 1 shows how a PI begins with a PI Planning event, followed by four development iterations, and ends with one IP (innovation and planning) iteration.

Figure 1. Typical PI timebox

This pattern is a suggestion rather than a strict rule, and there isn't a set number of iterations for a PI. However, experience shows that a PI lasting between 8 and 12 weeks is a good starting point, with shorter durations preferred. Organizations using Lean Portfolio Management (LPM) often find aligning the Strategy Portfolio Review and Participatory Budgeting events to this cadence to be helpful. This ensures that plans align closely with strategy.

Iterations

All Agile Teams work in iterations. However, the planning and execution during the iteration may differ based on whether the team works in Scrum or Kanban. Since Agile Teams operate as part of an ART, cooperation is critical to meet their Team and ART PI Objectives. To accomplish this, teams must align to the same iteration cadence and duration.

Develop on Cadence, Release on Demand

'Develop on cadence' describes a coordinated set of events that happen on an iteration or PI cadence to support product and solution development across the teams on the ART. Whereas development happens on a cadence, releases happen on demand. Some companies release often during the PI, while others may release less frequently due to compliance rules, supplier needs, or other factors. Market demands and company norms determine the timing of product releases.

Release on Demand lets businesses provide value to customers all at once or gradually, depending on what the market needs. This reduces the risks associated with large, infrequent releases and allows the organization to deliver value to customers at any time during the PI.

Read more about Iterations and Release on Demand:

Iterations
Release on Demand

How do PI events support ART execution?

When it comes to execution for a single ART, a dual Plan-Do-Check-Adjust (PDCA) sequence of events creates a closed-loop system to keep the train on the tracks, as illustrated in Figure 2. The outer loop represents the ART's PDCA cycle for the PI, while the inner circle represents an Agile Team's PDCA cycle for an iteration. In this example, the team is using Scrum for the inner loop. The diagonal line (PI Start) shows that after ART completes PI Planning, the teams on the train start the inner PDCA loop.

Figure 2. ART and team events drive successful execution

The following sections describe the ART events. The SAFe Scrum article offers guidance for the iteration events shown in Figure 2, and the SAFe Team Kanban article describes the events when using this method.

PI Planning

Each ART begins its PI with PI Planning. During this event, the teams estimate what they will deliver and then highlight their dependencies with other Agile Teams and trains. One outcome of PI planning is a set of PI objectives for each team detailing what the ART should deliver by the end of the PI. Agile Teams continuously integrate their work throughout the PI and demo progress towards their PI objectives during the Iteration Reviews and System Demo.

PI Planning follows a standard agenda that includes a presentation of the business context and vision. Then comes planning breakouts, where each team creates its high-level Iteration plans and objectives for the upcoming PI. The Release Train Engineer (RTE) facilitates PI planning, and it includes all ART members. The event takes place within the Innovation and Planning (IP) Iteration.

System Demos

The system demo tests and evaluates the product or solution under development in a production-like environment (often staging) to gather feedback from stakeholders. That includes Business Owners, executive sponsors, other Agile Teams, development management, and customers (or their proxies). Their feedback is critical to evaluate effectiveness and usability and provide the guidance the ART needs to stay on course or adjust. This event occurs at the end of every Iteration, providing a comprehensive view of the new features delivered by the ART.

Inspect and Adapt

The PI ends with an Inspect and Adapt (I&A) event to reflect, apply problem-solving techniques, and identify improvements. The goal is to increase the next PI's velocity, quality, and reliability. During the I&A, Product Management or other team members showcase the finished features in a final PI system demo. Quantitative and qualitative measurements and a problem-solving workshop follow the demo. This results in improvement features or stories that the RTE or teams can add to the backlog for the upcoming PI. So, every ART improves every PI, including course corrections to the product or solution itself.

Read more about Inspect and Adapt and System Demos:

Inspect and Adapt
System Demo

How are products and solutions built during the PI?

Building and maintaining a Continuous Delivery Pipeline (CDP) enables each ART to define, develop, validate, and release new functionality quickly. This allows them to deliver value to customers and stakeholders iteratively and continuously. Multiple Agile Teams on the ART may share a CDP. Each part of the CDP is described below:

Continuous Exploration (CE)

Continuous Exploration focuses on creating alignment on what needs to be built. In CE, design thinking practices ensure that the ART understands the market problem, customer needs, and the product or solution required to meet that need. It starts with an idea or a hypothesis of something that will provide value to customers, typically in response to customer feedback or market research. The concept is further analyzed and researched to understand the requirements for a Minimum Marketable Feature (MMF) or Minimum Viable Product (MVP). Finally, convergence occurs by understanding which features will likely meet customer and market needs.

Continuous Integration (CI)

Continuous Integration focuses on taking features from the ART backlog and improving them with design thinking tools. Teams conduct user research and gather feedback to ensure they understand what's needed. Then, Agile Teams start to work on the features. After completing the work, they put it into version control, build it, and integrate it into the product or solution. Finally, they test everything from start to finish before validating it in a staging environment.

Continuous Deployment (CD)

Continuous Deployment takes changes from the staging environment and deploys them into production. Then, teams verify and monitor them to ensure they are working correctly. This step makes the features available to the business, which determines the appropriate time to release them to customers. This allows the organization to respond, rollback, or fix forward.

Read more about the Continuous Delivery Pipeline:

Continuous Delivery Pipeline

How are flow, scope, risk, and dependencies managed in a PI?

The ART Backlog and Kanban system may be the most vital tools of the ART. Stakeholders use them to visualize and track the ongoing work, even when a part of the pipeline is automated. The ART needs to establish WIP limits to improve throughput and address bottlenecks. That's the role of the ART Kanban. In addition, sync events help manage flow, scope, risk, and dependencies, as described in the following sections.

Visualize and Limit WIP with the ART Kanban

The RTE, Product Management and others use the ART Kanban to visualize, track, and manage the flow of features. They begin in ideation and then move to analysis, implementation, and release through the CDP. Figure 3 illustrates a typical ART Kanban with example rules guiding how features enter and exit each state. This helps the ART improve flow, matching demand to capacity, applying WIP limits, visualizing bottlenecks, and highlighting relentless improvement opportunities. Product Management reviews the Kanban and pulls in more work, respecting WIP limits and collaborating with Product Owners.

This Kanban also helps review and prioritize new features. It continuously explores ideas and provides the information needed to make decisions about deployments and releases.

Sync on Scope, Progress, Risks and Dependencies

Sync events help keep the ART on track. The Coach Sync focuses on identifying risks, managing dependencies, tracking progress, and solving problems for the current PI. The PO Sync manages the scope of the PI, checks progress, adjusts priorities, and gets ready for the following PI. Since Product Owners and Scrum Masters/Team Coaches often deal with similar issues and need to work together, combining the Coach Sync and PO Sync into one event called the ART Sync can be helpful. The ART Sync usually replaces the Coach Sync and PO Sync for a specific iteration to reduce overhead.

The ROAM board created during PI planning is visible during ART Sync to ensure that team members recognize who's responsible for owning or mitigating the risk and then follow through. The ART may also record any new items that arise after planning and add them to the ROAM board.

Note: ROAM is an acronym for Resolve, Own, Accept, and Mitigate. It summarizes the four actions needed to prevent a potential risk.

During sync events, the RTE, Product Management, Scrum Masters/Team Coaches, and other stakeholders use and update the ART Planning Board, which was initially created during the PI Planning event. This helps track and manage dependencies and ensures they do not block other teams.

Read more about the ART Backlog and ART Planning Board:

ART and Solution Train Backlog
PI Planning

Key Takeaways
A Planning Interval is typically an 8 to 12-week timebox.
Agile Teams on an ART collaborate during a PI to deliver their PI Objectives.
A series of ART events, including PI Planning and Inspect and Adapt, ensures successful PI execution.

Last Update: 25 February 2025
