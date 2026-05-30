---
source_url: https://framework.scaledagile.com/guardrails
scraped: 2026-05-30
authenticated: true
---

SAFe Knowledge Base » Lean Budget Guardrails

Lean Budget Guardrails

We are all familiar with guardrails on highways. They are put there to keep a simple mishap from turning into a full-blown catastrophe. If you go a little off course, the rails help you regain the path towards your destination.

—Anonymous

Definition: Lean Budget Guardrails describe the policies and practices for budgeting, spending, and governance for a specific portfolio.

SAFe provides Lean budgeting strategies that eliminate traditional project-based funding and cost accounting overhead. In this model, LPM maintains appropriate levels of oversight through allocating value stream budgets and applying Lean budget guardrails. This way, enterprises can have the best of both worlds: a development process far more responsive to market needs and professional and accountable spending management.

Details

Every SAFe portfolio operates within an approved budget for developing and deploying systems and Solutions that the Enterprise needs to meet its strategic objectives. As described in the Lean Budgets article, the portfolio's total budget is allocated to individual value streams by Lean Portfolio Management (LPM) and portfolio stakeholders. The value stream's budget funds the people and resources to help achieve the current Portfolio Vision and Roadmap.

Establishing guardrails helps ensure that the mix of investments addresses both near-term opportunities and long-term strategy, that investments in technology, infrastructure, and maintenance aren't routinely ignored, and that significant investments are approved appropriately. Figure 1 illustrates four Lean budget guardrails:

Guiding investments by horizon
Applying capacity allocation to optimize value and solution integrity
Approving significant initiatives
Continuous Business Owner engagement

Figure 1. SAFe Lean budget guardrails

The first two guardrails are quantitative, guiding the allocation of investments within the approved budgets. The last two are process-related and are mainly qualitative, establishing how the budgets are governed. These guardrails are described in the sections that follow.

Guardrail 1: Guiding Investments by Horizon

As described in Lean Budgets, portfolio investments are organized by investment horizons that reflect four-time horizons. The amount of budget a given value stream allocates to solutions in these horizons determines the near- and long-term health of both the value streams and portfolio.

For example, a value stream solely focused on a Horizon 1 solution may be under-investing in future solution innovations, creating long-term risk. This may be balanced by the portfolio's intention to move the solution into Horizon 0 for subsequent decommissioning to enable the value stream to focus on other, more promising solutions. Accordingly, LPM establishes portfolio-level guidance for investments to optimize the whole while promoting decentralization so that individual value streams can optimize their solutions, as Figure 2 illustrates.

Figure 2. Investment horizon budget guardrail

Figure 2 shows that LPM has established different allocations for investments in solutions for each investment horizon. While this may be a healthy mix for a technology business, every portfolio and value stream has to consider its current context in determining its investment allocations for each horizon. A newly created value stream might allocate significantly more of its budget to Horizon 2 because it simply doesn't have any solutions in Horizon 1. An established value stream retiring legacy solutions with substantial technical obsolescence might allocate more budget to Horizon 0.

Guardrail 2: Apply Capacity Allocation

Lean Budgeting enables decentralized decision-making and more efficient execution. However, every train is challenged with balancing the backlog of new business Features with investment in the Architectural Runway continuously—for example, maintaining current systems, avoiding velocity reduction, and the need for wholesale replacement of components or solutions due to obsolete technology.

Balancing business features and enablers complicates prioritizing work since different forces can pull the teams in different directions, as Figure 3 shows.

Figure 3. Balancing business features and enablers

One solution to this challenge is that value streams (and ARTs) apply capacity allocation as a quantitative guardrail to determine how much of the total effort can be allocated for each type of activity for an upcoming PI, as shown in Figure 4. Each value stream should adapt the capacity allocation categories or add new ones as needed.

Figure 4. Balancing the forces on the ART backlog

Capacity Allocation Example Policies

Each value stream should develop explicit policies for managing capacity allocation. Following are example policy statements that many ARTs and Solution Trains have found helpful:

At each PI boundary, we agree on the percentage of capacity devoted to new features (or capabilities) versus enablers and tech debt and maintenance. Other capacity types may also apply, such as the percentage of capacity allocated to a specific epic.
We agree that Product and Solution Management have the authority to prioritize ART and Solution Train backlog items.
We agree to prioritize the business and enabler features and capabilities based on economics and in collaboration with architects.
We agree to collaborate on sequencing work in a way that maximizes customer value and minimizes technical debt.

While the agreed-to policies can persist for some time, the amount of capacity allocated will change periodically based on the context. In an ART context, the capacity allocation decision can be revisited as part of backlog refinement in preparation for PI planning.

Guardrail 3: Approving Significant Initiatives

While each value stream is funded to promote empowerment and local decision-making authority, it is reasonable to ensure that significant investments are governed responsibly.

Figure 5. Epics that exceed the portfolio threshold require LPM approval

Figure 5 shows that a significant initiative has been identified. It then goes through a decision filter to determine whether or not it exceeds the portfolio epic threshold, which LPM establishes.

Below threshold: If the epic estimate is below the portfolio epic threshold, approval is managed through the ART or Solution Train Kanban systems.
Above threshold: If the epic estimate exceeds the portfolio epic threshold, it requires review and approval through the Portfolio Kanban system, regardless of which level the initiative originates. LPM defines the Portfolio Epic threshold to determine which Epics are a portfolio concern.

Guardrail 4: Continuous Business Owner Engagement

Business Owners are uniquely qualified to ensure that the funding allocated to value streams is going toward the right things. Therefore, they serve as a critical guardrail that ensures that the priorities of the ARTs and Solution Trains are in alignment with LPM, customers, and Product and Solution Management, as illustrated in Figure 6.

Figure 6. Continuous Business Owner engagement

Figure 6 shows the minimum activities Business Owners should actively participate in before, during, and after PI execution:

Preparing for the upcoming PI – Business Owners ensure that ARTs and Solution Trains are allocating sufficient capacity for features, enablers, and technical debt and maintenance, as well as providing input on prioritization of Features and Capabilities using Weighted Shortest Job First (WSJF). Business Owners also collaborate with Product and Solution Management to ensure that the work planned for the PI contains the right mix of investments.

PI Planning – During PI planning Business Owners actively participate in key activities, including the presentation of the vision, draft plan review, assigning business value to team PI objectives, and approving final plans.

Inspect and Adapt (I&A) Workshop – During the I&A workshop, Business Owners provide feedback on the solution's fitness for purpose during the System Demo (or Solution Demo). The Business Owner's feedback is critical, as only they can give the guidance the train needs to stay on course or take corrective action. Additionally, they help assess actual value achieved versus plan and participate in the upcoming problem-solving workshop.

Learn More

[1] Nagji, Bansi, and Geoff Tuff. Managing Your Innovation Portfolio. Harvard Business Review, May 2012.

Ries, Eric. The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses. Crown Business, 2017.

Last update: 13 October 2023
