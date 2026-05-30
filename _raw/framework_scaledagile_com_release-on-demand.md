---
source_url: https://framework.scaledagile.com/release-on-demand
scraped: 2026-05-30
authenticated: true
---

Home » Release on Demand

Release on Demand

Develop on cadence. Release on demand.

– A SAFe mantra

Definition: Release on Demand is an aspect of the Continuous Delivery Pipeline that releases new functionality immediately or incrementally based on business and customer needs.

Summary

Release on demand (RoD), the last part of the continuous delivery pipeline (CDP), allows companies to deliver software quickly and efficiently. The CDP has four aspects: continuous exploration (CE), continuous integration (CI), continuous deployment (CD), and release on demand (RoD). Each part is vital to ensure that the product or solution is developed and delivered effectively, as illustrated in Figure 1. It is important to release new features at the right time and allow customers to put them to work. That is the primary function of RoD.

Figure 1. Release on demand is the fourth aspect of the continuous delivery pipeline

What is release on demand?

The activities associated with the RoD aspect of the CDP allow Agile Teams to launch new features, products, or solutions when users or customers need them most. This process helps teams deliver updates quickly and ensures that releases benefit users immediately. This is crucial because it affects business performance and customer satisfaction. Deciding what and when to release is a critical economic driver. Ideally, new features are released after they're ready, but often, they are launched based on specific user needs or market conditions.

Of course, this raises questions for Product Management and Business Owners: When should a release happen? What features should be released? Which end-users should receive the release?

A customer-centric mindset provides the answers. Market rhythms and milestones on the roadmap inform release timing and align with customer needs. Specific features or an entire product may be released, either to specific customer segments or to all customers.

Critically, releases are decoupled from the work to deploy the functionality. Decoupling releases ensures that Product Marketing can target promotional activities to specific audiences, and sales teams can schedule activities with greater confidence in the solution's timing and functionality.

What are the four activities of release on demand?

Figure 2 illustrates the four activities of Release on Demand.

Release – the practices needed to deliver the new functionality to end users, all at once or incrementally
Stabilize and Operate – ensures the release is working well from a functional and nonfunctional requirements (NFR) perspective
Measure – quantifies whether newly-released functionality provides the intended value
Learn – collecting feedback and feeding back learning into the continuous exploration aspect of the CDP

Figure 2. Four activities of release on demand

Release

Once the updated product or solution is ready and verified, it's time to release it to customers. However, launching too early or too late can hurt the business. So, Product Management works with other teams to set rules for how and when the release happens. Sometimes, qualified code can go straight to customers; other times, a more formal review is needed.

The following practices contribute to the ability to release:

Dark launches – Allows deployment to a production environment without releasing the functionality to end users.
Feature toggles – A mechanism that turns code "on" or "off" without requiring additional deployment.
Canary releases – The practice of releasing the new functionality to a specific customer segment and measuring the results before expanding and releasing it to more customers.
Decoupled release elements – Identifies elements that can be released independently. Even simple products and solutions will have multiple release elements, each operating with different release strategies.

Figure 3. Decouple release elements from the solution

For example, the SAFe website has multiple and somewhat independent release cycles, including infrastructure security fixes (ad hoc/expedited), article updates (high frequency), new extended guidance (medium frequency), and major Framework updates (low frequency).

These separate flows, or 'value streamlets,' continue to represent a complete, end-to-end flow of value within a value stream. Identifying streamlets is critical to enable RoD, as they allow the different elements of the solution to be released independently in a separate cadence.

Stabilize and operate

After customers have access to the new functionality, unanticipated problems may occur, such as higher-than-predicted usage volumes or unexpected usage patterns. Teams must quickly resolve incidents and security threats within their service-level agreements (SLAs). Several practices can help:

Site reliability engineering (SRE): Digitally enabled solutions often involve complicated networks of connected systems that serve users worldwide. Site reliability engineering helps make them more reliable and able to grow using software tools to automate tasks.
Failover/disaster recovery – Failures will occur. Developing a failover mechanism is vital to allow service to resume quickly or avoid interruption. Disaster recovery must be planned, architected into the service, and practiced.
Continuous security monitoring – Security as code and penetration testing help prevent known problems from reaching production. It's also important to continue testing services for new issues and to detect intrusions and attacks on services and infrastructure.
Architect for operations – Businesses need to consider their operational needs. Their challenges include heavy traffic, security threats, and the need to respond to problems.
Monitor nonfunctional requirements (NFRs) – Teams must monitor reliability, performance, scalability, and more to avoid service disruptions.

Measure

Once the new functionality has been released, application telemetry can be used to validate or invalidate the original hypothesis and determine whether the expected business value was achieved.

Then, to judge a hypothesis, teams need different metrics from what they might use for finished products. Innovation accounting is an approach to study early results and determine potential outcomes while developing and testing a Minimum Viable Product (MVP).

Learn

The information gathered from the release feeds back into the CDP. Product Management will use this feedback to make investment decisions about future features and epics. Product Management and Product Owners evaluate the hypothesis for MVPs and minimum marketable features (MMFs). Then, it decides if development should continue, stop, or pivot to a new idea and experiment with different approaches.

Only when features are in customers' hands do they realize value. And when that value is measured, the new knowledge informs the ongoing exploration efforts, starting the cycle over again.

What is release governance?

Release governance includes planning, managing, and governing releases. In some organizations, especially those with significant regulatory and compliance needs, a centralized function ensures that releases meet all the relevant business criteria.

In either case, release governance helps internal and external stakeholders receive and deploy the new product or solution. This ensures the ART addresses critical elements in advance, including internal and external security, regulatory, and other compliance concerns.

ARTs plan releases during PI Planning. That's the easy part. The difficulty lies in coordinating the implementation of features across multiple iterations in the PI. This is especially true when new issues, roadblocks, dependencies, and gaps in vision and backlogs arise. Due to these challenges, the scope of each release must be continually managed, revalidated, and communicated. This includes:

Ensuring the organization's release governance is understood and followed
Communicating release status to internal and external stakeholders
Ensuring that an appropriate deployment plan is in place
Coordinating communications with marketing and Product and Solution Management
Validating that the solution meets relevant solution quality and compliance criteria
Participating in Inspect and Adapt (I&A) to improve the release process, value stream productivity, and solution quality
Providing final authorization for the release
Acting as a liaison with Lean Portfolio Management (LPM) as appropriate
Participating in and overseeing final release activities

Key Takeaways:
Release on demand is the fourth aspect of the Continuous Delivery Pipeline.
Releasing on demand delivers products and solutions to customers at the right time.
Release on demand includes measuring and evaluating outcomes.
Release on Demand activities feed back into the continuous exploration process.

References

Ries, Eric. The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses. Random House, Inc, 2011.

Leffingwell, Dean. Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Agile Software Development Series). Pearson Education, 2011.

Gothelf, Jeff, and Josh Seiden. Lean UX: Designing Great Products with Agile Teams. O'Reilly Media, 2016.

Last Update: 25 February 2025
