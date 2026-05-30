---
source_url: https://framework.scaledagile.com/continuous-delivery-pipeline
scraped: 2026-05-30
authenticated: true
---

Home » Continuous Delivery Pipeline
Continuous Delivery Pipeline

Our highest priority is to satisfy the customer through early and continuous delivery of valuable software.

– Agile Manifesto

Definition: The Continuous Delivery Pipeline (CDP) represents the workflows, activities, and automation needed to guide new functionality from ideation to an on-demand release of value.

Summary

The continuous delivery pipeline (CDP) is an important part of accelerating product development flow. Each Agile Release Train (ART) builds and manages, or shares, a pipeline with the tools and resources to deliver value independently. Continuous exploration (CE), continuous integration (CI), and continuous delivery (CD)—work together to deliver small batches of updates to meet market demand which are then released on demand. Building and maintaining a CDP allows each ART to provide new functionality to users more frequently than traditional processes.

What is a continuous delivery pipeline?

A CDP allows Agile Teams and ARTs to deliver new functionality to users as needed. In some instances, 'continuous' may mean daily or even multiple releases per day. In others, this may mean weekly or monthly releases to satisfy market demands and business goals.

Figure 1 illustrates the pipeline's four aspects: continuous exploration (CE), continuous integration (CI), continuous deployment (CD), and release on demand (RoD).

Figure 1. The SAFe Continuous Delivery Pipeline

Legacy practices often cause ARTs to make solution changes in large chunks. However, this does not have to be an all-or-nothing approach. For example, a satellite system comprises a manufactured orbital object, a terrestrial station, and a web farm that feeds the acquired data to end users. Some components, such as the web farm functionality or satellite software, may be released daily. Others, like the hardware components, can only occur once every launch cycle.

Decoupling the web farm functionality from the physical launch eliminates the need for a monolithic release. It also increases agility, allowing teams to deliver solution components rapidly in response to market changes.

What are the four elements of a continuous delivery pipeline?

The CDP contains four elements: continuous exploration, continuous integration, continuous deployment, and release on demand. The paragraphs below describe each aspect.

Continuous exploration (CE) aligns what needs to be built. Design thinking helps the organization understand the market problem, customer needs, and required solutions. It begins with a hypothesis about what will add value for customers. Next, ideas are analyzed and researched to clarify the requirements for a minimum viable product (MVP) or minimum marketable feature (MMF). These details guide the exploration of how existing systems may need to change. Once Agile Teams determine which capabilities and features will meet customer and market needs, they define and prioritize them in the ART backlog.

Continuous integration (CI) focuses on implementing features from the ART backlog. CI applies design thinking tools to a problem and focuses on refining features (for example, designing a user story map). This may prompt more research employing solution space tools (such as seeking user feedback on a paper prototype). After specific features are understood clearly, Agile Teams implement them. The completed work is committed to version control, built and integrated, tested end-to-end, and validated in a staging environment.

Continuous deployment (CD) takes the changes from the staging environment and deploys them to production. Then, teams verify and monitor them to ensure they are working correctly. This step puts the features into production, and the business determines the appropriate time to release them to customers. CD allows the organization to respond, roll back, or fix forward as needed.

Release on demand (RoD) is the ability to make value available to customers in one event or in waves based on market and business needs. This permits the organization to release when the timing is best and carefully control the risk associated with each release. RoD also incorporates critical pipeline activities that preserve the solutions' stability and enduring value long after release.

Although described sequentially, the pipeline isn't strictly linear. Instead, it's a learning cycle that allows teams to establish one or more hypotheses, build a solution to test each one, and learn from that work.

Figure 2. The CDP fosters continuous learning and value delivery

Although a single feature flows through the value stream sequentially, the teams work through all aspects in parallel. That means that during every PI and iteration in the PI, ARTs and Solution Trains continuously:

Explore user value
Integrate and demo value
Continuously deploy to production
Release value whenever the business needs it

Read more about each aspect of the Continuous Delivery Pipeline:

Continuous Exploration
Continuous Deployment
Continuous Integration
Release on Demand

How is an existing workflow of a CDP mapped?

Organizations usually already have a delivery pipeline. Otherwise, they wouldn't be able to release any value. But too often, pipelines are not fully automated, contain significant delays, and require tedious and error-prone manual intervention. These factors cause delayed releases, increasing their size and scope. This approach is the opposite of the SAFe Principle #6, which makes value flow without interruption.

The first step to improving value flow is mapping the current pipeline. Teams collect and record metrics on the value stream map to note delays. This helps the Agile Release Train (ART) find ways to improve, like eliminating delays or cutting down on rework.

Active time is the period needed to complete work in any given step.
Wait time is the gap between steps when no work is happening. Locating and eliminating excessive wait time is critical to improving value flow.
Percent complete and accurate (%C&A) represents the percentage of work the next step can process without needing rework. Delays often result from poor quality in the prior steps. The %C&A metric helps identify the steps where poor quality might delay value delivery.

Once the current flow is understood, it can be mapped into the SAFe CDP. Mapping provides the organization with a shared mental image to communicate changes and improvements.

Teams look for opportunities to improve the efficiency of each step to reduce flow time. This includes addressing active time and end-to-end quality (%C&A).

The delay between steps is often the biggest problem at the start. The deployment process often has significant delays and a lot of rework. Reducing wait times is usually the quickest way to optimize flow time. Another is to remedy any step with a low %C&A. Cutting down on rework allows the ART to focus on adding value versus fixing errors. Future improvements should aim to reduce batch sizes and use the DevOps practices discussed in the articles about the CDP.

Read more about the importance of Flow:

Make Value Flow Without Interruptions

How does the ART Kanban enable flow and continuous delivery?

Continuous delivery is essential to ARTs and Solution Trains. Product Management and its stakeholders need to monitor ongoing work, even though much of it is automated. The ART Kanban helps manage the flow of features through the CDP. Setting work-in-process (WIP) limits can improve efficiency and help find and fix bottlenecks.

Read more detail about the ART Kanban:

ART and Solution Train Backlogs

How does DevOps support continuous delivery?

Building, maintaining, and optimizing a CDP requires specialized skills and tools throughout the value stream. DevOps methods are ideal because this delivery system needs to provide complex solutions with short learning periods and high degrees of collaboration. This practice makes it easier to implement CDPs.

SAFe's CALMR approach to DevOps guides continuous value delivery by improving Culture, Automation, LeanFlow, Measurement, and Recovery. DevOps technical skills, practices, and tooling are grouped into practice domains, depicted by the model's inner loops. The two outer loops illustrate the four aspects of the CDP, each of which has four activities.

Read more about DevOps and download the free DevOps Health Radar:

DevOps
DevOps Health Radar

References

[1] Martin, Karen. Value Stream Mapping: How to Visualize Work and Align Leadership for Organizational Transformation. McGraw-Hill Education, 2013.

[2] Kim, Gene. The Phoenix Project: A Novel about IT, DevOps, and Helping Your Business Win. IT Revolution Press, 2013.

[3] Kim, Gene, Jez Humble, Patrick Debois, and John Willis. The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations. IT Revolution Press, 2016.

Key Takeaways
The continuous delivery pipeline (CDP) allows organizations to map a new path using relentless improvement to deliver customer value as needed.
The CDP contains continuous exploration, integration, deployment, and demand release.
Teams look for ways to improve the efficiency of the CDP to improve the flow of value.
DevOps methods are ideal for building, maintaining, and optimizing a CDP.

Last Update: 6 February 2025
