---
source_url: https://framework.scaledagile.com/solution-train
scraped: 2026-05-30
authenticated: true
---

SAFe Knowledge Base » Solution Train

Solution Train

Principle of Alignment: There is more value created with overall alignment than with local excellence.

—Don Reinertsen

Definition: The Solution Train is the organizational construct used to build large solutions that requires the coordination of multiple ARTs and suppliers.

The Solution Train construct in SAFe describes the additional roles, events, and artifacts needed to build large solutions that require contributions from multiple ARTs and suppliers. These solutions often have an unacceptable social or economic cost for failure, are often subject to industry and regulatory standards and must provide objective evidence of compliance with those standards. Many large solutions are part of an even larger 'system-of-systems' built by an extended supply chain, as described in the Supplier article.

Details

Solution Trains provide the constructs businesses need to build large solutions—including cyber-physical systems—in a Lean-Agile manner. They align multiple Agile Release Trains (ARTs) and Suppliers to a shared mission (Figure 1). Solution Trains help manage the inherent risk and variability of large-scale solution development with additional roles, artifacts, and events described in this article.

Figure 1. ARTs and suppliers power the Solution Train

Why Solution Trains?

Solution Trains form for different reasons. Some trains form with new ARTs and Agile Teams to specifically address a large initiative, while others begin by combining existing ARTs and teams. This is particularly true in organizations operating with SAFe for some time as they recognize the opportunity and need to reorganize around value (see Principle #10) occasionally.

In the latter case, Solution Trains may experience an initial forming period even though its ARTs have been performing for quite some time with a mature backlog, roadmap, Continuous Delivery Pipeline (CDP) infrastructure, and other assets. When forming a Solution Train from existing ARTs, quickly creating the foundational SAFe artifacts (Solution Train Vision, Backlog, and roles) is critical to getting work to the existing ARTs and teams.

Solution Train Characteristics

Agile Release Trains Power the Solution Train

Each ART within a Solution Train contributes to the development of the solution, as shown in Figure 2. All development activities typically occur within each ART and are coordinated by the Solution Train.

To support the overall goal of continuous value delivery to the customer, each ART within the Solution Train must be designed to maximize flow across the entire Solution Train.

Figure 2. A mixture of topologies applied to ARTs within a Solution Train

Stream-aligned ARTs

A stream-aligned ART, just like a stream-aligned team, will have the necessary personnel, skills, and authority to deliver value, whether a whole product, service, or portion of the overall solution to the end user. For example, a navigation system for an autonomous vehicle may be developed and delivered by an integrated stream-aligned ART.

Complicated subsystem ART

Most large systems also include extensive subsystems. Complicated subsystem ARTs are common when building large-scale systems. These are unique subsystems managed by a single ART, and they reduce the cognitive load on stream-aligned ARTs, which are essentially consumers of that subsystem.

Platform ART

Similarly, it is common for a Solution Train to have Platform ARTs that provide services that the stream-aligned ARTs extend and build on.

Enabling ART

While less common than the other ART topologies, enabling ARTs provide specialty tools, services, or expertise to other ARTs and teams.

Enabled by Critical Roles

In addition to the ARTs and Agile teams, the following roles aid the Solution Train's successful execution:

Solution Management defines and supports building desirable, feasible, viable, and sustainable large-scale business solutions that meet customer needs over the solution's significant lifespan. They represent the customer and business needs to the ARTs.

Solution Architects define and communicate a shared technical and architectural vision across the Solution Train to help ensure the solution under development is fit for its intended purpose. They work with the ART's System Architects to help guide their portion of the solution's design.

Solution Train Engineer (STE) is the coach for the Solution Train, facilitating and guiding the work of all ARTs and suppliers. The STE works with Release Train Engineers (RTEs) to facilitate ART execution and coordinate delivery.

Suppliers are internal or external organizations that develop and deliver components, subsystems, or services, which help Solution Trains deliver solutions to customers.

Business Owners are key stakeholders of the Solution Train, with final responsibility for the business outcomes. They, along with Solution Train leaders, may also serve as business owners for the Solution Train's ARTs.

Customers are the buyers of the solution and ultimately determine value. When delivering in a supply chain, customers work closely with Solution Management and other key stakeholders to define and adjust the solution's vision, intent, and delivery roadmap.

Due to their size and cost, large solution development attracts a lot of attention, heightening stakeholder involvement and increasing opinions, governance, and oversight. The Solution Train leadership team – Solution Managers, Architects, and STE – must be aligned and represent a consistent force to realize the solution's vision.

A System Team is typically formed for the Solution Train to address the integration issues across the ARTs. Individual ARTs may have their own Systems Teams. All System Teams share resources and align on common infrastructure and toolchains where possible.

Shared Services represent the specialty roles, people, and services required for the success of the Solution Train, but that cannot be dedicated full-time.

Solution Train Responsibilities

ARTs within a Solution Train fulfill the responsibilities as described in the ART article. Since the ARTs and teams deliver most of the Solution Train's value, Solution Train leaders must support the ARTs in their value delivery. In doing so, Solution Trains also have their unique responsibilities, as shown in Figure 3.

Figure 3. Solution Train Responsibilities

Connecting with the Customer

Feedback is critical to value delivery. Inadequate feedback can result in high costs, rework, major delays, and unsatisfied customers. However, getting feedback presents unique challenges in large solution development. Significant organizational barriers often exist between the people building the solution and those who can provide the best input and feedback.

Planning and Roadmapping

No event is more powerful in SAFe than PI Planning. Solution Trains must ensure that their ARTs enter PI Planning aligned on a shared vision, goals, and objectives for the upcoming Planning Interval (PI). They perform Pre-Planning activities to prepare the ARTs and suppliers for PI Planning and foster alignment during the individual ART planning events.

Solution Train leaders use rolling-wave Roadmaps to align ARTs and suppliers and inform the features in their ART backlogs and PI roadmaps (Figure 4).

Figure 4. A Solution Train roadmap showing multiple planning horizons

Building Solution Capabilities

While some features come from local ART context, others implement the Solution Train's capabilities. Capabilities represent a higher level of solution behaviors that typically take multiple ARTs to implement, as shown in Figure 5. Like features, capabilities are also sized to fit within a PI.

Figure 5. Splitting capabilities into features facilitates implementation by multiple ARTs

A Solution Train kanban system helps manage the backlog of work to ensure the evaluation and analysis of capabilities before they are ready for implementation. The Kanban helps limit Work in Process (WIP) to ensure that all the ARTs are synchronized and have the capacity to deliver value together.

Coordinating ARTs and Suppliers

Solution Trains coordinate large solution development throughout the PI. They align all ARTs and suppliers on a common cadence and facilitate the events that create and maintain alignment, including PI Planning, Solution Train syncs, and Solution Demos. Strategic suppliers are critical to solution success and should also participate in these events. Figure 6 shows the ART and Solution Train events throughout the PI.

Figure 6. Solution Train coordination events

Releasing and Release Governance

Solution Trains apply cadence and synchronization to manage development. But, like ARTs, Solution Trains can deploy the solution, or an element of the solution, at any time the business and market dictates.

Ideally, teams and ARTs should be able to release at will for fast feedback, a flow of value delivery, and to learn in an operational environment. Automated testing, verification, and validation in the Continuous Delivery Pipeline (CDP) should address many release management quality concerns. However, releasing value in large solution development is often a significant governance concern as failures in these systems can have unacceptable social and economic costs.

Each Solution Train must establish—or operate within the governance of—a release management function with the authority, knowledge, and capacity to foster and approve releases. The release management function includes representatives from the Solution Train and ARTs. It may also include representatives from marketing, quality, Business Owners, IT Service Management, operations, deployment, and other areas.

Learn More

[1] Skelton, Mathew, and Manuel Pais. Team Topologies. IT Revolution Press, 2019.

[2] Knaster, Richard, and Dean Leffingwell. SAFe 5.0 Distilled, Achieving Business Agility with the Scaled Agile Framework. Addison-Wesley, 2020.

Last update: 23 January 2023
