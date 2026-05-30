---
source_url: https://framework.scaledagile.com/measure-and-grow
scraped: 2026-05-30
authenticated: true
---

Home » Measure and Grow
Measure and Grow

The great thing about fact-based decisions is that they overrule the hierarchy.

– Jeff Bezos, founder of Amazon [1]

Definition: Measure and Grow is an approach SAFe enterprises use to evaluate progress towards Business Agility and determine improvement actions.

Summary

SAFe's Measure and Grow approach evaluates business agility through three key domains: outcomes, flow, and competency. Outcomes measure if solutions meet business and customer needs using KPIs, OKRs, and employee engagement metrics. Flow metrics assess delivery efficiency and predictability, including flow distribution, velocity, time, load, efficiency, and predictability. Assessments measure proficiency in SAFe Disciplines and practices.

Effective measurement requires using metrics with other discovery methods, focusing on metrics that drive decision-making, understanding how metrics impact behavior, and interpreting metrics carefully. By measuring these domains and adhering to best practices, organizations can improve their business agility and achieve better outcomes.

What is meant by measure and grow in SAFe?

When it comes to metrics, the first and most important thing is understanding what to measure. The goal of Business Agility is clear: quickly respond to market changes and emerging opportunities with innovative, digitally-enabled business solutions. The Business Agility Value Stream visualizes the steps needed to achieve this. SAFe's three measurement domains, Outcomes, Flow, and Competency, support this process and provide a comprehensive yet simple model for measuring progress toward this goal. The insights provided by these three measurement domains support better decision-making and help to identify opportunities for improvement.

Figure 1. Three SAFe measurement domains support the goal of business agility

The three measurement domains are defined as follows:

Outcomes: Do our solutions meet the needs of our customers and the business?
Flow: How efficient is the organization at delivering value to the customer?
Competency: How proficient is the organization in the practices that enable agility?

These three measurement domains apply at every level of an organization. They can be used to measure performance within a SAFe portfolio, a Solution Train, an Agile Release Train (ART), or even a single Agile Team.

Each measurement domain contains a set of specific metrics, which are described in the sections below.

Read more about the Business Agility Value Stream:

Business Agility Value Stream

Why measure outcomes, and which metrics are meaningful?

Outcomes help determine whether an organization's efforts produce the desired business benefit. They may measure external results, such as revenue and customer retention increases, or internal concerns, such as employee engagement.

KPIs and OKRs

A SAFe portfolio uses key performance indicators (KPIs) and strategic themes to measure outcomes. Each KPI is a specific and quantifiable measure of results for the value streams in that portfolio. These outcome metrics are typically context-specific and depend on the organization, business model, and the type of customer solutions. For example, the customer conversion rate that may be a meaningful metric for an eCommerce business would not apply to a microchip manufacturer. Some indicators, however, may be used successfully across contexts, such as Net Promoter Score.

The value stream KPIs article provides guidance for defining appropriate KPIs for that particular SAFe Portfolio.

The strategy helps identify the goals, which means that the main themes of the portfolio influence the KPIs. KPIs are ongoing measures that show how well the business is doing overall. In contrast, the strategic themes are set up as objectives and key results (OKRs), which focus on the specific outcomes the portfolio aims to achieve for future success. The key results linked to these objectives create another vital set of metrics that are usually measured every three months.

In a large portfolio, creating specific OKRs for each value stream that align with the portfolio's strategic themes can be helpful. For large value streams that contain multiple ARTs, this process can be repeated to create a set of OKRs that define the goals for each ART. This approach also allows teams at each level of the organization to see the direct impact of their work against the key results of the OKRs they are aligning to.

Read more about OKRs and KPIs:

OKRs
KPIs

Employee Engagement

Employee engagement is another revealing internal outcome metric. It measures a person's level of motivation and engagement toward supporting the organization's goals and values. Higher levels result in higher productivity, efficiency, and innovation. Lower levels can lead to poor motivation, lower-quality work, and higher staff turnover.

Different methods exist for measuring employee engagement, and each organization needs to determine what is right for them. Some organizations will use an annual employee engagement survey. Others use an employee Net Promoter Score (eNPS), which asks, 'How likely are you to recommend your employer to others as a place of work?' It is measured on a 10-point scale.

Iteration Goals and PI Objectives

Teams and Agile Release Trains (ARTs) use specific metrics like iteration goals and PI objectives to measure if they are meeting their targets. This helps them stay focused on what customers and the business need, give feedback, prioritize work, and ensure that the work is accepted. To set up good outcome metrics, teams, value streams, and portfolios must work closely with their business partners.

Read more about Iteration Goals and PI Objectives:

Iteration Goals
PI Objectives

How does SAFe measure flow?

Flow measures determine how effective an organization is at delivering value. The Flow Framework created by Mik Kersten [2] provides five metrics that can be used to measure different aspects of flow. As SAFe is a flow-based system, each metric is directly applicable. In addition, SAFe defines Flow Predictability to measure how Teams, ARTs, and Solution Trains deliver business value against their planned objectives. These six flow metrics are shown below.

Figure 5. The six SAFe flow metrics

Flow Distribution

What does it measure? Flow distribution measures the amount of each type of work in the system over time. This could include the balance of new business Features (or Stories, Capabilities, or Epics) relative to Enabler work, as well as the work to resolve defects and mitigate risks.

How is this measured? One simple comparison is to count the number of each type of work item at any point in time. A more accurate measure might consider the size of each work item. Agile Teams may measure flow distribution per iteration, but PI boundaries are commonly used to calculate this at the ART level and above.

Why is this important? To balance both current and future velocity, it is important to be able to track the amount of work of each type that is moving through the system. Too much focus on new business features will leave little capacity for architecture/infrastructure work that addresses various forms of technical debt and enables future value. Alternatively, too much investment in technical debt could leave insufficient capacity for delivering new and current value to the customers.

Flow Velocity

What does it measure? Flow velocity measures the number of backlog items (stories, features, capabilities, epics) completed in a given timeframe; this is also known as the system's throughput.

How is this measured? The simplest measure of velocity is to count the number of work items completed over a time period, such as an iteration or PI. Those items can be stories, features, capabilities, or even epics. However, since work items are not all the same size, a more common measure is the total number of completed story points for work items of a type over the timeframe.

Why is this important? All other things being equal, higher velocity implies a higher output and is a good indicator that process improvements are being applied to identify and remove system delays. However, the system's velocity will not increase forever, and over time, the stability of the system is important. Significant drops in velocity highlight problems that warrant investigation.

Flow Time

What does it measure? Flow time measures the total time elapsed for all the steps in a workflow and is, therefore, a measure of the efficiency of the entire system. Flow Time is typically measured from ideation to production. Still, it can also be useful to measure Flow Time for specific parts of a workflow, such as code commit to deployment, to identify opportunities for improvement.

How is this measured? Flow time is typically measured by the average length of time it takes to complete a particular type of work item (stories, features, capabilities, epics). A histogram is a useful visualization of flow time since it helps identify outliers that may need attention and supports the goal of reducing the overall average flow time.

Why is this important? Flow time ensures that organizations and teams focus on what is essential – delivering value to the business and customer in the shortest possible time. The shorter the flow time, the less time our customers spend waiting for new features and the lower the cost of delay incurred by the organization.

Flow Load

What does it measure? Flow load indicates how many items are currently in the system. Keeping a healthy, limited number of active items (limiting work in process) is critical to enabling a fast flow of items through the system (SAFe Principle #6).

How is it measured? A Cumulative Flow Diagram (CFD) is one common tool used to effectively visualize flow load over time. The CFD shows the quantity of work in a given state, the rate at which items are accepted into the work queue (arrival curve), and the rate at which they are completed (departure curve). At a given point in time, the flow load is the vertical distance between the curves.

Why is this important? Increasing flow load is often a leading indicator of excess work in process. All other things being equal, the likely result will be an increase in future flow times as queues start to build up in the system. For this reason, measuring and reducing flow load is of critical importance. Furthermore, it is easy to see how more frequent delivery lowers flow load while improving flow time and flow velocity.

Flow Efficiency

What does it measure? Flow efficiency measures how much of the overall flow time is spent in value-added work activities vs. waiting between steps.

How is it measured? To correctly measure flow efficiency, the teams, trains, and value streams must clearly understand what the flow is in their case and what steps it passes through. This understanding is achieved with the help of Value Stream Mapping – a process of identifying workflow steps and delays in a system. Once the steps have been mapped, flow efficiency is calculated by dividing the total active time by the flow time and is expressed as a percentage.

Why is this important? In a typical system that has not yet been optimized, flow efficiency can be extremely low, often in single digits. Low flow efficiency indicates excessive bottlenecks and delays in the system. Conversely, the higher the flow efficiency, the better the system can deliver value quickly.

Flow Predictability

What does it measure? Flow predictability measures how well teams, ARTs, and Solution Trains can plan and meet their PI objectives.

How is it measured? Flow Predictability is measured via the ART Predictability Measure. This measure calculates the ratio of actual business value delivered in a PI to the planned business value. For more information on calculating this important metric, see the Inspect and Adapt article.

Why is this important? Low or erratic predictability makes delivery commitments unrealistic and often highlights underlying problems in technology, planning, or organization performance that need addressing. Reliable trains should operate in the 80 – 100 percent range; this allows the business and its stakeholders to plan effectively.

Note on DORA Metrics: Within and across the three measurement domains, it can often be helpful to bring together complementary metrics to provide a specific view of performance. An example is the DORA metrics used to measure the performance of an organization's DevOps capabilities. The four DORA metrics are 1) deployment frequency, 2) lead time for changes, 3) time to restore service, and 4) change failure rate.

Each of these is an application of a flow metric designed for a particular use case. Deployment frequency is a productivity metric and an example of flow velocity. Both lead time for changes and time to restore service are examples of flow time metrics, focusing on specific steps in the workflow. Finally, change failure rate represents the percentage of changes that require remediation after they have gone to production.

Read more about Accelerating Flow:

Accelerating Flow with SAFe

How does SAFe measure competency?

Achieving business agility requires significant expertise across its Disciplines and Competencies. Each can deliver value alone; however, they are interdependent.

The SAFe business agility assessment is meant for business and portfolio stakeholders to evaluate their progress in achieving true business agility.

In addition to the Business Agility assessment, there is one for each of the SAFe Disciplines. These assessments help teams and ARTs improve on the technical and business practices they need to help the portfolio achieve that larger goal. They identify potential SAFe Competencies to concentrate on next.

Each assessment follows a standard process pattern of running the assessment, analyzing the results, taking action, and celebrating successes. In addition, comparative analysis against the competition is achievable via online assessment tools available to SAFe members.

The SAFe DevOps Health Radar helps ARTs and Solution Trains optimize their value stream performance. It provides a holistic DevOps health check by assessing the maturity of the four aspects and 16 activities of the continuous delivery pipeline. The Health Radar is used to measure baseline maturity at any point in a DevOps transformation and guide fast, incremental progress thereafter.

What are the critical success factors for effective measurement?

Measuring organizational performance is one of the most sensitive areas in every business, often subject to politics and various dysfunctions. Additionally, since measurement inevitably involves the interpretation of data, it is subjected to cognitive bias, communication issues, and alignment disconnects. All this leads to a substantial danger in any measurement system: if not correctly implemented, some measurements can do more harm than good. The following success factors will help guide the enterprise to more effective measurements and more importantly, better business results.

1. Use measurement in conjunction with other discovery tools

However well-designed, any measurement system provides only a partial picture of reality. And adding more metrics does not always improve visibility. There is a story behind every number, which often contains more information than the number alone can convey. A powerful tool to use along with measurement is direct observation. 'Gemba' is the Japanese term and practice for observing the actual environment where value is created and where it meets the customer. Formal measures and informal observations reinforce one another. Managing by just the numbers, without qualitative data, can lead to poor outcomes and even worse morale.

2. Apply metrics where they support improved decision-making

A common trap when applying metrics is over-measuring for fear of not measuring enough. Although many metrics can be automated, as the number of metrics and frequency of measurement increase, so will the effort needed to collect and analyze the data. When considering whether to include an additional metric in your measurement system it can be prudent to ask the question, 'what decisions will this metric help inform that isn't supported today with our existing metrics?' If the new metric helps to drive better decision-making, it should be a candidate for inclusion; if not, then omit it.

3. Understand the effect of metrics on behaviors

In a positive culture, knowledge workers are motivated to deliver winning solutions and work with purpose, mastery, and autonomy. However, when too much emphasis is placed on a specific numerical indicator and when that indicator is directly tied to compensation or career growth opportunities, achieving that number becomes the goal instead of creating effective solutions.

Additionally, the pressures to succeed often lead to the misuse of metrics. For example, flow efficiency may be used to assign blame for a missed delivery date to a particular ART that has become a bottleneck rather than using this information to identify systemic problems that need addressing.

In each case, SAFe's Core Values of transparency and alignment must provide the proper foundation for an effective measurement system, alongside creating an environment where the facts are always friendly.

4. Interpret metrics carefully

Just collecting specific measures is not enough. If interpreted without proper understanding, an indicator may be quite misleading. For example, when measuring flow time, the work items must be actual, valuable features (stories, and so on) that carry business benefits; otherwise, the train may be reporting improvements in the flow of work but struggling to get any real value out of the door.

References

[1] Hunt, Helena, ed. First Mover: Jeff Bezos In His Own Words. Agate Publishing, 2018.

[2] Kersten, Mik. Project to Product: How to Survive and Thrive in the Age of Digital Disruption with the Flow Framework. IT Revolution Press, 2018.

[3] Martin, Karen, and Mike Osterling. Value Stream Mapping: How to Visualize Work and Align Leadership for Organizational Transformation. McGraw-Hill Education, 2018.

[4] Accelerate. 2023 State of DevOps Report. Google.

Key Takeaways
Business agility requires measuring outcomes, flow, and competency.
KPIs and OKRs track strategic goals and value stream performance.
Flow metrics measure delivery efficiency and predictability.
Competency assessments guide improvement in SAFe practices.

Last Update: 8 September 2025
