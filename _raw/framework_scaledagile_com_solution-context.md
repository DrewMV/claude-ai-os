---
source_url: https://framework.scaledagile.com/solution-context
scraped: 2026-05-30
authenticated: true
---

SAFe Knowledge Base » Solution Context

Solution Context

Context is the key—from that comes the understanding of everything.

—Kenneth Noland

Definition: Solution Context identifies the critical aspects of the environment in which a solution operates.

Many solution development initiatives are unsuccessful—not due to the inability to create the solution—but because the developed solution fails to perform as expected in its actual operating environment. Examples abound:

A mobile app for equipment inspection that the rig worker cannot use because they wear gloves
A payroll management system that cannot connect to the corporate identity management server
A software solution that doesn't anticipate needed field support or modifications

Naturally, the impact on the customer and the business can be significant or even catastrophic.

Understanding the Solution Context is crucial to value delivery. It provides an essential understanding of the solution's requirements, usage, installation, operation, and support. It impacts development priorities, Solution Intent, Capabilities, Features, and Nonfunctional Requirements (NFRs). It provides opportunities, limits, and constraints for the Continuous Delivery Pipeline, including Release on Demand activities. The solution context represents various environmental and deployment factors that are often outside the control of the organization developing the solution.

Details

Understanding the context in which a Solution operates is critical for every solution builder. It often requires the same degree of discipline as in building the solution itself. This effort can be compounded by the fact that it's easier (and perhaps more interesting) for a solution builder to focus on developing the solution than on understanding where and how it will be operated.

While enterprises are increasingly applying iterative methods of building solution functionality, exposing that functionality to the operating environment often happens only at release time. And that is too late to respond to the new learnings without significant delay or rework.

Instead, solution builders should understand the solution's operating environment and design and test for success in that environment. This means that Agile Teams and trains must:

Recognize the critical aspects of the solution context
Expose the solution to its environment early and often
Continually address the evolving solution context

Recognize the Critical Aspects of Solution Context

The environment in which a solution operates impacts all elements of solution development, including solution intent and design, NFRs, development priorities, solution implementation and testing, release governance, and more. These critical aspects generally fall into seven categories, as illustrated in Figure 1:

Figure 1. Key aspects of the solution context

Customer Usage

Customer experiences can depend heavily on the location, availability, and convenience of the solution. How a solution is used is often better observed than elicited directly from the customer. For instance, a first responder may not follow a strict sentence format for a voice command system during a critical situation. Also, a customer service representative may be unable to record a complaint in the CRM system during peak load times. There is no good substitute for the learnings gained in actual observation.

Physical Environment

The physical conditions of the environment also influence solution design. These conditions often relate to the effect that temperature, humidity, vibration, weight, volume, power, speed, bandwidth, and similar factors have on the solution. For instance, ice build-up may prevent a vehicle sensor from detecting oncoming objects; a blizzard may prevent a traffic control system from detecting a gridlocked intersection; prolonged exposure to direct sunlight may prevent a mobile phone from placing an emergency call; and strong winds may prevent voice recognition software from interpreting commands.

Standards and Regulations

Solutions often operate in regulated environments where teams must ensure compliance with externally imposed standards. For example, privacy and data protection regulations may prevent a software system from treating user data similarly in all jurisdictions. Organizations also establish their own efficacy, quality, and reliability standards to support desired customer and business outcomes.

Maintenance and Operational Support

The practicality and feasibility of maintenance and operational support are also critical aspects of the solution context. These include many 'routine' functions, such as:

Configuring system settings and business rules
Maintaining user accounts and administrative access
Diagnosing and troubleshooting issues
Applying hotfixes and security patches
Scaling software, hardware, and infrastructure for performance

Understanding the maintenance and support a solution requires can be vital to its success. For example, a heavily customized Enterprise Resource Planning (ERP) system may have significantly different maintenance and operational procedures than one used 'off-the-shelf.'

Supporting Infrastructure

Solutions typically require supporting infrastructure, such as servers, data centers, power, fiber optic networks, communications satellites, etc. In addition to understanding a solution's current infrastructure needs, future flexibility, scalability, and resiliency must also be considered. For instance, an artificial intelligence (AI) solution may require increasingly more computing power as it increases in sophistication.

Interoperability with Other Solutions

In today's highly connected world, solutions seldom operate in isolation. Instead, they are likely to interact with many other solutions. The number of such connections varies from a few to hundreds or thousands depending on the complexity of the solution.

A connected solution imposes requirements upon other solutions while also needing to adhere to requirements from those solutions. As a result, the solutions ecosystem can contain a complex network of interdependencies that must be managed carefully.

System-of-Systems

Often, a solution performs a function as a part of a larger system-of-systems. A solution may then be a subsystem in a complex cyber-physical solution (for example, a vehicle entertainment system). Or it may be a suite of solutions that perform adjacent functions and are tightly coupled with common platforms and data sources. In these cases, the system-of-systems' solution context informs the subsystems' context.

Expose the Solution to Its Environment Early and Often

It's easy to underestimate the impact of a solution's operating environment on its design. Therefore, it is crucial to explore the solution context early and revisit it frequently during development. Waiting until release can produce costly mistakes.

Exposing the solution to different aspects of its operating environment early tests design assumptions sooner and reduces the impact of necessary changes (Figure 2).

Figure 2. Early exposure to the solution environment accelerates learning and reduces risk

Lean-Agile solution builders understand and embrace this concept: A solution's context almost always contains unknowns that can only be revealed through direct, intensive, factual exploration of the solution in its intended operating environment.

Although customers can provide valuable insight into the solution context, Agile teams and ARTs advance their understanding by obtaining regular feedback directly from the solution environment.

Figure 3. Example solution context considerations for a drilling rig equipment inspection system

A disciplined approach to exposing a solution to its environment early and often may include activities such as those described below.

Direct Observation

There is no substitute for directly observing users in the solution environment. This may reveal aspects of the solution context, such as:

The actual work a user performs and the challenges they face
How the physical characteristics of the environment affect the solution and its users
How specific standards and regulations impact the customer experience
The type and integrity of supporting infrastructure required by the solution
The effort and challenges that maintenance and operational support teams experience
Other systems in the ecosystem and how they interact with the subject solution

Examples of direct observation could include a Product Owner traveling onsite to examine the solution environment, a System Architect examining detailed production environment logs, or a team of solution builders gathering data from adjacent solutions in the Operational Value Stream.

Simulating the Solution Environment During Development

To understand how the solution context will affect the solution under development, it is usually necessary to approximate or mimic the solution environment. This involves selecting and simulating key aspects of the environment so that testing can be performed more frequently. This requires investments in simulation technology, but the solution's value offsets these costs demonstrated incrementally and empirically.

Examples of simulation methods include test harnesses, labs, wind tunnels, digital twins, and mule vehicles. Cyber-physical solution builders leverage Model-Based Systems Engineering (MBSE) to mimic the solution environment's software- and hardware-based aspects.

Figure 4. Agile team simulates aspects of the solution environment during the development

For software, simulation environments are an essential prerequisite to a reliable continuous deployment pipeline so that testing can occur during development and at the deployment point.

Simulating the solutions context in the development environment significantly reduces the cost of exposing it to its actual environment and accelerates the feedback loop. However, every approximation instantiates and simulates only a portion of the solution context. Agile teams must be mindful of this limitation.

Testing the Riskiest Solution Characteristics in Context

The solution's characteristics critical to its proper functioning are the highest priority for testing in the solution environment. As development progresses, the answer must be quickly exposed to the operational environment to test these characteristics in context. Typically, this involves investments in prototypes and simulations of varying fidelity.

Testing the Full Solution in Context

At some point, the integrated solution must be exposed to its actual environment. Even then, however, it needn't be an all-or-nothing affair, and various aspects of the solution may be incrementally tested against various aspects of its context. For example, in the case of software systems, two commonly used approaches are 'shadow testing' and 'canary releases.'

Shadow testing involves creating a 'sandbox' (isolated working area) in the actual solution's environment and deploying and testing the new version there before its official release (Figure 5).

Figure 5. Shadow testing validates a solution in 'dark mode' in its production environment

A 'canary release' exposes a fully functional solution to a small subset of users. This allows the solution to be validated in the production environment while minimizing the impact of unforeseen issues.

Address the Evolving Solution Context

Solution context rarely remains static over the lifespan of the solution. While some elements may remain unchanged, others can change, sometimes radically. For example, customer usage or load patterns may shift dramatically; new solutions may be incorporated into the ecosystem that changes the operating environment, or regulations may change suddenly.

After releasing a solution, teams are naturally anxious to build the next one. But every release reveals new unknowns about the operating environment. This necessitates treating the solution context as seriously as the solution itself.

Last update: 22 May 2023
