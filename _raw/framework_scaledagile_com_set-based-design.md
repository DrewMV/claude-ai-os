---
source_url: https://framework.scaledagile.com/set-based-design
scraped: 2026-05-30
authenticated: true
---

SAFe Knowledge Base » Set-Based Design

Set-Based Design

Assume variability; preserve options.

—SAFe Lean-Agile Principle #3

Definition: Set-Based Design (SBD) is a Lean development practice that keeps requirements and design options flexible for as long as possible during the development process.

Instead of choosing a single-point solution upfront, teams use SBD to explore multiple options simultaneously, eliminating poorer choices over time. This approach enhances flexibility and design outcomes by committing to technical solutions only after validating assumptions.

Details

System development involves continuously converting uncertainty into knowledge. With SBD, teams make design decisions only after they have gained sufficient knowledge and data. They maintain multiple requirements and design options open for a longer time in the development cycle. As the timeline advances, they use experiential data to narrow the focus on the final design option. Through this approach, they embrace Principle #3 – Assume variability; preserve options for as long as possible, providing maximum flexibility.

Set-based design is different than a traditional 'point-based' approach. A point-based design approach commits to a set of requirements and a single design strategy too early in the 'cone of uncertainty' (Figure 1). It often leads to incorrect assumptions and late discoveries that require significant rework. As the facts become known and the deadline approaches, teams must often rush to solve problems. This emergency work can result in shortcuts, stress, quality compromises, and missed commitments and deadlines.

Figure 1. A point-based design forces decisions too early in the cone of uncertainty

In a Set-Based Design approach (Figure 2), developers initially consider multiple design choices. Teams begin researching, developing, and evaluating various designs, exploring technical and economic trade-offs. Based on their work, objective evidence is available at integration-based learning points. Then, as Figure 2 illustrates, teams eliminate the weaker options over time and ultimately converge on a final design.

Figure 2. Set-based design converges towards the best solution as uncertainty decreases

As described further in references [1] and [2], SBD is essential to achieve economic efficiency in Lean product development. Figure 3 summarizes the conceptual difference between set- and point-based design approaches.

Figure 3. Comparing point-based and set-based design approaches

Set-Based Design Increases Economic Efficiency

Teams use SBD along with a hypothesis-driven Minimum Viable Product (MVP) approach and gain fast feedback on their choices through their Continuous Delivery Pipeline. Design alternatives include the hypothesis and a set of assumptions. Teams also define experiments to gain the knowledge needed to validate or invalidate those hypotheses, eliminate poor choices, and arrive at the optimal design.

Figure 4 illustrates an example in which an autonomous vehicle's designers must select a technology to prevent forward collisions before a significant milestone.

Figure 4. Exploring alternatives for a new forward collision prevention vehicle subsystem

With their corresponding hypothesis statement, teams create Enablers that explore cost trade-offs—for example, providing support for environmental and weather conditions, vehicle design impact on manufacturing, obstacle detection quality, Nonfunctional Requirements (NFRs), and more. Based on validated learning, teams select the best design and record the results in the Solution Intent repository.

Of course, exploring multiple design choices comes at a cost, even if the designs are primarily model-based or paper-prototypes. (Note: Reinertsen points out that maintaining various design options is a type of u-curve optimization, and sometimes the optimum number of choices is one. [3])

However, a set-based design is more cost-efficient overall if there's a high degree of technological innovation, variability in market or customer conditions, or fixed deadlines. In this case, SBD design efficiency depends on several factors:

Flexibility – Preserving a broad set of design options for as long as possible
Cost – Minimizing the cost of multiple options through modeling, simulation, and prototyping
Speed – Facilitating fast earning through early and frequent validation of design alternatives

The following sections provide recommended practices for achieving efficiency with SBD.

Increase Flexibility in Interfaces and Design

Teams build and integrate complex systems from subsystems and components to produce the desired system behavior. To support SBD, subsystem interfaces must be flexible at the intersection points. System engineers may specify ranges for requirements and designs for these intersection points, which they can discuss with Product Management as more validated learning occurs. For example, how would the overall system value improve if a system engineer allocated more space, weight, and power to one component instead of another?

This more experimental approach allows system designers to manage the system-level allocations, creating a collaborative environment for system-level learning, negotiation, and making sound economic choices.

Leverage Modeling, Simulation, and Prototyping

Modeling, simulation, and prototyping provide the initial learning points that help eliminate some design alternatives and confirm others. As described in the MBSE article, modeling uses a broad set of specific techniques, including digital twins, CAD, design thinking, and user-experience design options. Teams should use various SBD approaches to the parts of the system where the risk is highest, optimizing the overall cost of maintaining design alternatives.

Collapse Design Options with Frequent Integration Points

When teams explore new designs during development, uncertainty abounds, and validated learning is scarce. The best way to resolve this variability is to test design alternatives through early and frequent system integration. In part, integration points are driven by regular System Demos, which occur each iteration, and Solution Demos, which happen on the PI cadence. (See 'Frequently Integrate the System' in Enterprise Solution Delivery.)

These frequent integration points support experiential learning, providing new insights and reducing options as the system evolves (Figure 5).

Figure 5. Frequent integration provides critical learning points that narrow design alternatives

Take a Systems View

Significant design decisions often span parallel development initiatives and require some consideration for the future and the present. For example, the operational data store (ODS) technology decision for the autonomous vehicle should consider more than the current initiative to avoid front collisions. Figure 6 illustrates how architects guide the teams' understanding of the larger context when making significant technology decisions.

Figure 6. Technology decisions must look beyond the current initiative

As mentioned above, set-based design has a cost. Architects and teams must balance the possibility of over-engineering the solution with the need to be prepared for near-term capabilities.

Make Decisions Based on Economic Trade-offs

Design choices have different financial implications. Effectively applying SBD requires knowledge of the broader goals of the system. As described in Principle #1 – Take an economic view, and Reintersen [3], making decisions based on economics requires an understanding of the trade-offs (Figure 7) between a set of related factors:

Figure 7. Economic trade-offs help quantify design options

Development expense – the cost of labor and materials required to implement a capability
Lead time – the time needed to implement the capability
Product cost – the manufacturing cost (cost of goods sold) and deployment and operational costs
Value – the economic worth of the capability to the business and the customer
Risk – the uncertainty of the solution's technical or business success

Trade-offs between these factors help illustrate which design options provide the most benefits. For instance, in the earlier collision prevention example, understanding the balance between the accuracy of various detection technologies vs. their added manufacturing cost can dramatically change the decision, as shown in Figure 8.

Figure 8. A trade-off between cost and performance (error margins in this case) helps select the best designs alternatives

Learn More

[1] Ward, Allen C., and Durward K. Sobek II. Lean Process and Product Development. Lean Enterprise Institute, 2014.

[2] Oosterwal, Dantar P. The Lean Machine: How Harley-Davidson Drove Top-Line Growth and Profitability with Revolutionary Lean Product Development. Amacom, 2010.

[3] Reinertsen, Donald G. Principles of Product Development Flow: Second Generation Lean Product Development. Celeritas Publishing, 2009.

Last update: 9 October 2023
