---
source_url: https://framework.scaledagile.com/team-backlog
scraped: 2026-05-30
authenticated: true
---

Home » Team Backlog
Team Backlog

While building trust gives teams the ability to reconfigure and "do the right thing," it is also necessary to make sure that team members know what the right thing is. Team members must all work toward the same goal, and in volatile, complex environments that goal is changeable.

– General Stanley McChrystal, Team of Teams [1]

Definition: The Team Backlog is a Kanban system that is used to capture and manage the user stories and enablers intended to enhance the solution.

Summary

The team backlog is represented as a Kanban system that the Agile Team uses to capture stories and enablers needed to advance the product or solution they develop. This includes stories that come from features in the ART backlog as well as those from the team's local context. Each Agile Team maintains its backlog, which creates a shared, transparent view of all the known work to be completed by the team. This technique enables efficient planning, collaboration, and continuous improvement.

What is the team backlog?

The team backlog holds all the work a team might need to enhance the solution. It contains user stories, enablers, and work items, such as improvement stories that may have been identified during Retrospectives or Inspect and Adapt (I&A) events. This includes stories originating from features in the ART backlog and those from the team's local context.

The team backlog contains all the work the Agile Team needs to do to deliver on their goals and develop the area of the product or solution they are responsible for. It is a list of desired work items rather than commitments, and items can be estimated (which is preferred) or left unestimated. There are no specific deadlines for completion. This gives the team flexibility to decide what to implement and when. All team members are encouraged to contribute stories to the team backlog. The Product Owner (PO) is responsible for managing the backlog and assists the team in working with multiple stakeholders, each of whom may have different opinions on what is most important.

The PO prioritizes the backlog, balancing the needs of stakeholders. There are three primary inputs to the team backlog.

Figure 1. Input sources for a team backlog

ART backlog – The ART Backlog consists of the upcoming features to be delivered by an Agile Release Train. During PI Planning, teams split features into stories and plan them into future iterations. These new stories are maintained in the team backlog.
Team's local context – The team's local concerns (other new functionality, defects, refactors, technical debt, and maintenance) are also in the backlog. Since PI planning produces only a high-level plan, adjustments will occur during team planning events during the PI, and new work items will be identified.
Other stakeholders – Agile Teams on the ART are not islands, so their backlogs will contain some stories that support other dependencies and commitments on behalf of other teams. This may include the research spikes required to estimate future features, capabilities, and even epics.

Teams also receive continuous feedback from previous iterations and events such as the System Demo that may affect the backlog.

Nonfunctional requirements (NFRs) are persistent qualities that may affect the design, performance, or quality of the product or solution. Since they serve as constraints for all the team's backlog items they are shown underneath the team backlog. Due to their importance, teams often automate acceptance tests for NFRs and include them in their definition of done (DoD).

Read more about Agile Teams and Stories:

Agile Teams
Stories

How is the team backlog created and refined?

Agile Teams apply a continuous, flow-based approach to backlog readiness. So, the backlog always contains some stories ready to implement without significant risk or surprise. Like a neglected garden that grows wild when left unattended for too long, the team backlog becomes unmanageable without regular attention. Maintaining the team backlog includes the following activities:

The PO regularly collaborates with the team and stakeholders to prioritize the team backlog
Existing stories are refined or removed, and acceptance criteria are established
New stories, including enablers, are discovered and described
High-priority items are readied by defining acceptance criteria and sizing them to fit within small timeboxes
Stories that have aged or perhaps are no longer relevant are removed

Although the PO leads prioritization of the team backlog, refinement is a collaborative process. Refinement includes dialogue between the team, customers, and other stakeholders. This breaks down barriers between the business and the teams, eliminating waste, handoffs, and delays. Collaboratively creating acceptance criteria for a story helps clarify the requirements. It uses the team's knowledge and creativity and encourages everyone to take ownership.

There is no recommended pattern for refining the backlog. Some teams like to refine the backlog after their Team Sync. Others prefer weekly sessions or requirements specification workshops, applying behavior-driven development (BDD) techniques to help explain stories. Multiple teams often collaborate on feature development, so new issues, dependencies, and stories are likely to emerge. Backlog refinement also helps surface problems with the current plan, which may require discussion at team, PO, or Coach Syncs.

How is a Kanban system used to manage the team backlog?

In SAFe, Agile Teams manage their backlog using a Kanban system to facilitate alignment, visibility, and dependency management.

Figure 2. One Agile Team's initial Kanban board

This Kanban system visualizes all active and pending work, workflow states, and work-in-process (WIP) limits. The system is WIP-limited; a work item can be pulled into the next step only when the number of items is lower than the WIP limit. A few activities in the Kanban may not be WIP-limited (typically the beginning and the end). The team defines and adjusts WIP limits, allowing it to adapt quickly to the flow of complex system development variations.

Read more about Applying Kanban in SAFe:

Applying Kanban in SAFe

How does the team balance different types of work?

Every Agile Team must balance internally focused work (maintenance, refactors, and technical debt) with new user stories that deliver immediate business value. Focusing solely on business and customer-facing functionality may work well in the short term. However, this approach often leads to increased technical debt and a slower development velocity. Avoiding this requires continuous investment in evolving the product or solution architectural runway alongside making customers happy with enhancements, new functionality, and bug fixes. The right balance extends the system's life and defers technical obsolescence.

Prioritizing different types of work can be challenging. The PO must compare the value of dissimilar things: defects, refactors, redesigns, technology upgrades, and new user stories. The demand for any of these is not limited. The PO works with the team to allocate their capacity for these items.

During planning, the PO, team, and System Architect choose the highest-priority items for each slice of capacity allocation. Due to the origins of many stories from features, some priorities may already be set during the PI planning. However, the PO can determine work priorities based on the team's local context by value, size, and logical sequence. The PO can also change the percentage allocation for each type of work to balance long-term system health and value delivery. Teams can adjust the capacity allocation categories as needed, but it can help to keep these categories consistent across the teams in the ART.

Figure 3. Typical examples of capacity allocation categories (user stories, enablers, and maintenance in this case)

Read more about Enablers and User Stories:

Enablers
Stories

References

[1] McChrystal, General Stanley; Collins, Tantum; Silverman, David; Fussell, Chris. Team of Teams: New Rules of Engagement for a Complex World. Penguin Publishing Group, 2015.

Key Takeaways
The team backlog is represented as a Kanban system that tracks the user stories and enablers needed to advance the product and the related systems.
Keeping the backlog refined keeps Agile Teams focused and ready for every iteration.
Agile Teams balance both system health and product functionality when prioritizing the team backlog.

Last Update: 24 February 2025
