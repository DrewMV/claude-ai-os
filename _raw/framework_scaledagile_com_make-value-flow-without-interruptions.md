---
source_url: https://framework.scaledagile.com/make-value-flow-without-interruptions
scraped: 2026-05-30
authenticated: true
---

# Principle #6 – Make Value Flow without Interruptions

> When we start thinking about ways to line up all of the essential steps needed to get a job done into a steady, continuous flow, it changes everything.
>
> — James P. Womack and Daniel T. Jones, Lean Thinking

---

**About the Flow Article Series**

SAFe is a flow-based system. As such, any interruptions to flow must be identified and addressed systematically to enable continuous value delivery. While flow-based guidance is embedded throughout SAFe, a special collection of eight articles directly addresses impediments to flow. These are Value Stream Management, Principle #6 - Make value flow without interruptions, Team Flow, ART Flow, Solution Train Flow, Portfolio Flow, Accelerating Flow with SAFe, and the Extended Guidance article Coaching Flow.

---

Enterprises must respond quickly to market changes to remain competitive in the digital age. Delivering a continuous flow of value to customers in the 'shortest sustainable lead time' is the central theme of SAFe. Doing so requires moving new system features through the development value stream as quickly as possible. Achieving continuous flow requires a new way of working that eliminates the traditional start-stop-start project cycle and the waterfall phase gates that hinder flow.

The principles and practices that enable the uninterrupted flow of value in SAFe are integral to the Lean-Agile Mindset, Value Stream Management, and Lean Thinking, which can be summarized as:

- Precisely specify value by product
- Identify the value stream for each product
- Make value flow without interruptions
- Let the customer pull value from the producer
- Pursue perfection

This article, SAFe Principle 6, describes how to make value flow without interruptions by introducing 'eight flow accelerators' that can be used to improve flow at any level of SAFe.

## What is Flow?

Flow occurs when there is a smooth, linear, and fast movement of work product from step to step in a relevant value stream. While the details of any flow system are based on its context, all flow systems have eight common properties:

1. **Work in process** — There is always some work in process in the system; if there weren't, there could be no flow of value.
2. **Bottlenecks** — In every flow system, one or more bottlenecks effectively limit the flow through the entire system.
3. **Handoffs** — Handoffs wouldn't be necessary if one person could do all the work. But in any material flow system, different individuals and teams will have different skills and responsibilities. Each plays its part in moving a work item through the system.
4. **Feedback** — Customer and stakeholder feedback is integral to efficient and effective outcomes. Ideally, feedback happens throughout the entire process.
5. **Batch** — As any system has a finite capacity, all the work can't be done at once. Therefore, work through the system occurs in batches designed to be as efficient as possible.
6. **Queue** — It all starts with a set of work items to be done. In addition, each value stream needs a prioritizing mechanism to sequence the work for the best value.
7. **Worker** — People do the critical work of moving work items from one state to another.
8. **Policies** — Policies are integral to flow. They may be local policies — like team-based policies that determine how a work item moves from step to step — or global policies like those that govern how work is performed within the company.

## The Eight Flow Accelerators

Each flow property is subject to optimizations, and often many steps encounter unnecessary delays, bottlenecks, and other impediments to flow. Making value flow without interruptions can best be achieved by adopting the eight 'flow accelerators' described in this article. These powerful accelerators of value are relevant to all Framework levels, but the challenges differ for each.

### #1 Visualize and Limit WIP

Overloading teams and ARTs with more work than can be reasonably accomplished is a common and pernicious problem. Too much work in process (WIP) confuses priorities, causes frequent context switching, and increases overhead. It overloads people, scatters focus on immediate tasks, reduces productivity and throughput, and increases wait times for new functionality. Like a highway at rush hour, there is simply no upside to having more work in a system than the system can handle.

The first corrective action is to make the current WIP visible to all stakeholders. A simple Kanban board illustrates the total amount of WIP and the process state of each work item. This Kanban serves as an initial process diagnostic, showing the current bottlenecks. Often, simply visualizing the current volume of work is the wake-up call that causes the organization to address the systemic problems of too much work and too little flow.

The following action is balancing the amount of WIP against the available development capacity. This is done by establishing—and continually adjusting—WIP limits for the relevant states. No new work is started when any workflow state reaches its WIP limit. This matches demand to capacity and increases flow through the system.

Limiting WIP, however, requires knowledge, discipline, and commitment. It may even seem counterintuitive to those who believe that the more work you put into the system, the more you get out. That can be true up to a point, but when the system becomes overloaded, throughput decreases dramatically. Indeed, there is no substitute for effectively managing WIP.

### #2 Address Bottlenecks

Bottlenecks occur wherever people or resources in the flow of value experience demand greater than the available capacity. Examples include a shortage of a specialized skill (such as a data scientist), insufficient processing power for the build servers in the CI/CD pipeline, or a silicon supply shortage for building the integrated circuits of a cyber-physical system. Work piles up at a bottleneck and limits the effective throughput of value.

Upstream processes are blocked from moving value. Downstream processes are starved and waiting. Bottlenecks cause the value stream to operate slowly and uneconomically, far below its potential capacity. This is emphasized in the Theory of Constraints (Goldratt), which posits that the throughput of any flow system is limited by the capacity of a dominant constraint, or bottleneck. By this theory, investment in optimizing the system at any other point than the dominant constraint is waste, as it will not improve the throughput of the system.

No matter the theory, bottlenecks must be addressed, by adding additional skills, people, or other resources at the bottleneck step. While that is not always easy to do, eliminating dominant bottlenecks must be a primary focus as throughput will not increase until the bottleneck is addressed.

In the meantime, however, the complex workflows in solution development provide other options. It's often the case that not all the work is single-threaded. There is often other work that does not have to pass through the bottleneck. In this case, teams can selectively pick and deliver other valuable work, thus increasing value throughput, while the dominant bottleneck is being addressed.

### #3 Minimize Handoffs and Dependencies

Handoffs occur whenever there is a separation between knowledge, responsibility, action, and feedback. For example, dependencies happen between teams when the work of one team cannot continue until related work by another team is completed. Both result in development waste in the form of wait states in the flow of value. They can also lead to rework as the knowledge transfer is likely imperfect, causing further delays.

The best solution to overcome handoffs and dependencies is to create teams and ARTs with all the knowledge, resources, skills, and decision-making authority to create an end-to-end flow of value. However, unhealthy dependencies and handoffs can still occur even when teams and trains have all the skills to deliver end-to-end value. Activities like value stream mapping, retros, and the I&A problem-solving workshop can help identify the root causes and potential solutions.

### #4 Get Faster Feedback

Learning is the foundation of improvement and the engine that powers product development. Doing this as fast as possible speeds up and improves the overall development process. The goal is to get positive and negative feedback into the development process as early as possible.

However, we often discover that getting early feedback can be difficult for a variety of reasons:
- Lack of direct access to customers
- Delays in the development value stream
- Late or infrequent integration results in discovering hidden work and defects
- Developing more functionality than what's needed
- Building the wrong things or more functionality than what's needed

Fast feedback is generally achieved by applying the basic Plan-Do-Check-Adjust (PDCA) learning cycle. To accelerate flow further:
- Applying customer centricity and design thinking as part of product development and engaging with customers frequently
- Making improvements to the continuous delivery pipeline, including build and test automation, test-first practices, and continuous integration
- Keeping work items small results in faster working increments of value
- Using built-in quality practices, mob work, pairing, and swarming to increase team cohesion and focus on finishing one backlog item at a time
- Upholding a solid Definition of Done (DoD) to help teams work together to finish Increments of value and share knowledge
- Use "stop-the-line" to fix problems when they occur so they don't pile up

Generally, solution builders need two types of feedback from each PDCA cycle:
1. **Feedback about building the right thing** — This feedback can only come from those users, customers, and economic stakeholders who can measure a solution's actual value. Each PDCA cycle is an opportunity for this learning, from early mockups and storyboards to system demos during development to feedback on pre-releases and deployed systems in production.
2. **Feedback about building it right** — Innovative systems constantly push the bounds of technology and the developers' skills. Each PDCA cycle also evaluates if the right technology is applied to optimally solve the customer's problem and meet the critical nonfunctional requirements.

### #5 Work in Smaller Batches

Faster feedback is one of the primary reasons for working in smaller batches. The smaller the size, the faster teams can collect and evaluate the feedback to adjust. In addition, smaller batches reduce WIP by limiting the number of requirements, designs, code, tests, and other work items moving through the system at any point. Smaller batches go through the system faster and with less variability, fostering faster learning. Moreover, since each item in the batch has some variability, larger batches accumulate more variability.

The economically optimal batch size depends on the holding cost (the cost for delayed feedback, inventory decay, delayed value delivery, and so on) and the transaction cost (the cost of preparing and implementing the batch). To improve the economics of processing smaller batches — teams should focus on reducing the transaction costs — resulting in higher throughput for a batch of a given size. Reducing batch size typically involves investment in automating the Continuous Delivery Pipeline, including infrastructure and automation, continuous integration, builds, regression testing, and more.

### #6 Reduce Queue Length

Reducing the length of the queue that is feeding the system is another critical way to accelerate flow. Long queues introduce waste, delays, and information decay. In addition, Little's Law informs us that the average wait time equals the average queue length divided by the average processing rate. Therefore, assuming any average processing rate, the longer the queue, the longer the wait.

For solution development, the longer the queue of committed work awaiting implementation, the longer the wait time for new features, regardless of the team's efficiency. For example, suppose an ART has an average flow velocity of 10 features per quarter and a committed backlog of 30. In that case, the customer may have to wait as long as three quarters before any new features can start developing. This example explains why queues are fundamentally bad and can significantly delay the ability to respond to customer needs.

Reducing queue length decreases delays, reduces waste, increases flow, and improves predictability. It's a requisite for faster service and a more consistent flow of value.

### #7 Optimize Time 'In the Zone'

Being 'in the zone' (also described as being in a 'flow state') is an engaged mental state of extreme focus on an activity where the work feels effortless and time passes quickly. People and teams in the zone demonstrate higher creativity, productivity, happiness, and fulfillment. Getting into this mental state requires uninterrupted focus time, autonomy, competence, and connectedness to others to engender self-actualization and intrinsic motivation.

Contrast this to the conditions in a typical work environment where work occurs in functional siloes in a batch-queue-handoff system. These frequent interruptions (emergency requests, ad hoc status reports, constant communication alerts, and so on) are the norm, and excessive WIP drives frequent task switching.

There is an essential connection between creating a continuous flow of value and creating a working environment where individuals and teams can maximize their time in the zone. Knowledge workers also need the time and space free from interruption essential for complex tasks involving application, analysis, evaluation, and creativity, and ultimately the personal satisfaction that completion engenders.

### #8 Remediate Legacy Policies and Practices

During or after a Lean-Agile transformation, enterprises must constantly look out for legacy policies and practices that inhibit flow. Many of these practices became part of the culture and are described as "we've always done it this way," even when they are no longer fit for purpose. Examples include:

- Continued reliance on phase-gate milestones and the iron triangle of fixed scope, resources, and time
- Obsolete or unnecessary change control boards, including extraneous oversight and reporting
- Waterfall-based quality management systems for regulations and compliance
- Obsolete tech standards in environments where they are not mandated or required for quality
- Continuation of timesheet reporting in addition to Agile Lifecycle Management (ALM) tooling, requiring double recording of time
- Traditional HR performance reviews and compensation policies that cause unhealthy competition
- Agile is adopted only by teams; the mindset of management and portfolio governance remain unchanged

While many of these patterns may well have solved problems in the past, they now create new problems that become ongoing impediments to flow. They must be proactively or reactively discovered, eliminated, modified, or mitigated.

## Measuring Flow

It's difficult to improve what isn't measured. The SAFe Measure and Grow article describes six metrics for measuring flow:

- **Flow Distribution** — a measure of the proportion of work items by type in a system.
- **Flow Velocity** — measures the number of completed work items over a time period.
- **Flow Time** — a measure of the time elapsed from start to completion for a given work item.
- **Flow Load** — a measure of the number of work items currently in progress (active or waiting).
- **Flow Efficiency** — the ratio of the total time spent in value-added work activities divided by the flow time.
- **Flow Predictability** — a measure of how consistently teams, ARTs, and portfolios are able to meet their commitments.

Together, these metrics provide a comprehensive view as new value flows through the development value stream.

## Summary

These eight flow accelerators help teams increase throughput and deliver value faster. As an added benefit, implementing them gives people a sense of control over the process and triggers fast and measurable improvements in customer satisfaction and employee engagement.

## Learn More

[1] Womack, James P., and Jones, Daniel T. Lean Thinking: Banish Waste and Create Wealth in Your Organization. Free Press, 2003.

[2] Goldratt, Eliyahu M. The Goal: A Process of Ongoing Improvement. The North River Press Publishing Corporation, 1986.

[3] Goldratt, E. M. What is this Thing called Theory of Constraints and How should it be Implemented? North River Press, Inc, 1990.

[4] Oosterwal, Dantar P. The Lean Machine. AMACOM, 2010.

[5] Reinertsen, Donald G. The Principles of Product Development Flow: Second Generation Lean Product Development. Celeritas, 2009.

[6] Ward, Allen, and Durward Sobeck. Lean Product and Process Development. Lean Enterprise Institute, 2014.

[7] Csikszentmihalyi, Mihaly. Flow. HarperCollins, 1990.

[8] Kersten, Mik. Project to Product: How to Survive and Thrive in the Age of Digital Disruption with the Flow Framework. IT Revolution Press, 2018.

Last update: 6 February 2023
