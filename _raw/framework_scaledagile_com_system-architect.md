---
source_url: https://framework.scaledagile.com/system-architect
scraped: 2026-05-30
authenticated: true
---

Home » System Architect
System Architect

[A] system must be continually adapted, or it becomes progressively less satisfactory.

-Manny Lehman, "Metrics and Laws of Software Evolution" [1]

Definition: The System Architect is responsible for defining and communicating a shared technical and architectural vision for the solutions developed by an ART.

Summary

The System Architect plays a crucial role in ensuring that there is an architectural vision implemented that aligns with business goals. They do this by defining enablers, participating in solution definition, outlining non-functional requirements(NFRs), and managing capacity for enablement work. The System Architect ensures effective communication and implementation of the architectural vision, facilitates the architecture's adaptability, and guides Agile Teams through the evolution of system designs. This role is pivotal in maintaining the balance between technical possibilities and business priorities, driving value creation through strategic design and collaboration. They are integral to the ART leadership, collaborating with Product Management, the Release Train Engineer, and Business Owners to achieve effective outcomes on the ART.

What is a System Architect?

System Architects align the Agile Teams on an Agile Release Train (ART) to a common technical direction. They are part of the ART leadership and work closely with Product Management, the Release Train Engineer (RTE), and Business Owners.

An ART might have multiple System Architects. Each of these architects would focus on a specific part of designing the solution, like security, cloud services, data, and the design of the user interface. They work together to define the overall architecture.

The System Architect works with Enterprise and Solution Architects to ensure the ART is aligned with the organization's wider technology strategy and other solutions being developed.

On the ART, System Architects define and communicate the technical and architectural vision and ensure that it is aligned with and compatible with the product vision developed by Product Management. With input from the Agile Teams, they create the technical roadmap, which includes considerations for rapid integration and testing of new work.

Alongside Product Management, they ensure the ART backlog has an appropriate mix of features that deliver the product vision. This includes identifying the necessary infrastructure and technology enablers for the ART backlog.

Throughout development, the System Architect continues to explore and shape the emerging solution design, validate technical assumptions, and establish the continuous delivery pipeline. The System Architect focuses on designing systems for change and is also responsible for enabling teams to address compliance, new technology, and product operations. This requires them to pair and mentor Agile Team members.

What are the responsibilities of a System Architect?

The System Architect's responsibilities consist of the five areas shown in Figure 1.

Figure 1. Areas of responsibility of a System Architect

The remainder of this article further describes each responsibility area.

Aligning Architecture with business priorities

The main goal of any solution architecture is to help create and deliver value for the business. A System Architect needs to make sure their work aligns with the business's goals.

Define enablers and architectural runway – The System Architect will identify the needed enablers to build the runway to support upcoming Features in the ART backlog. This is done with feedback from the Agile Teams and informed by the technical strategy.
Participate in solution definition – As a part of design thinking the System Architect is often closely involved in defining the solution brings awareness to the technological and implementation capabilities and constraints of the ART. This includes being a part of product road mapping workshops, architecture reviews, and feature refinement with Agile Teams.
Define system NFRs – The System Architect defines the solution's non-functional requirements (NFRs) and ensures that the architecture will support them. System Architects help the Agile Teams decide on specific actions and the tools needed to develop and monitor the NFRs.
Ensure capacity allocation for enablement work – Improving the design and structure of systems requires the Agile Teams' time and effort. The System Architect works with Product Management to ensure enough time is set aside for this work. This occurs while preparing for each PI boundary and during the PI Planning event.

Read more about the architectural runway:

Architectural Runway

Defining and communicating architecture vision

Today's technology can be complex and hard to manage. To make development easier for teams and keep them productive, the architect plays an important role. They need to clearly explain the technology plan to the teams and everyone involved in the Agile Release Train (ART). This helps everyone understand how to design the system and do the work. As a result, we complete tasks more quickly and efficiently, offering better value to customers.

Present architectural vision to teams during PI planning – The System Architect updates the architectural vision before every PI Planning event. During PI planning, the architect presents the vision as part of the business context briefings and stays available to the teams during the rest of the planning activities.
Provide guidance on implementing the vision – During the PI, the System Architect stays aligned with the teams and provides further guidance as needed. It's normal for the original plan to change as the Agile Teams learn more while they develop each iteration. The architect ensures that any design issues teams encounter throughout the PI are solved.
Architect for agility and change – To change and embrace new facts that emerge during development, the system design must enable flexibility. Helpful tools for preserving options include using abstraction in system design thoughtfully and set-based design.

Read more about agile architecture and set-based design:

Agile Architecture
Set-Based Design

Evolving System Design with Teams

Any architecture requires ongoing adjustment. The System Architect works with the Agile Teams to help uncover inconsistencies in the architectural design and assist the ART in making necessary changes. This involves communicating changes based on what is learned during the development process.

Support architectural experiments and spikes – The System Architect helps teams plan and carry out important tests to check if their design ideas work. They help the teams test quickly and with as little effort as possible. This is done because if their initial design guesses are wrong, it can be very expensive to fix later. Doing these tests early on helps avoid a lot of work later on.
Collaborate with teams on optimal system design – The architect often works with the Agile Teams to share new ideas and get feedback about the current design. This teamwork usually happens during planning events, demos, and reviews. Also, the architect might join team meetings when there's a big change in the design needed.
Align architectural intent with the reality of implementation – The architect ensures that the architectural vision's expressed expectations and the reality of the team's capacities, skills, and available tools do not have a large gap. For this alignment to occur and continue, the architect must stay in close contact with the teams. Achieving this often involves the System Architect directly participating in the creation of work artifacts and conducting peer reviews. Additionally, it's helpful for the architect to involve themselves directly in the research spikes that teams undertake.

Read more about how to create enablers and features:

Enablers
Features and Capabilities

Fostering built-in quality and attending to NFRs

Architecture can determine how easy or hard it will be to implement new solution features that support quality standards for the new functionality without breaking the old. Likewise, architecture significantly impacts the ART's ability to implement and sustain the solution's NFRs.

Promote system design that supports built-in quality – The System Architect defines architectures that help the ART shift learning left. This helps teams discover problems early or prevent them in the first place. The System Architect helps teams create loosely coupled architectures, diligently follow design and coding standards, and refactor to help keep the solution healthy. This results in improved testing and upkeep of code and other solution assets.
Attend to the system NFRs – NFRs influence solution viability and sustainability. If not adequately attended to throughout development, they may create a large volume of rework or even thwart the entire solution development effort. The System Architect provides ongoing guidance to the ART to help build and sustain NFRs. The architect often assists teams in devising an effective strategy for new NFRs and helps create standards for maintaining the existing ones. Some of this is reflected in the corresponding definition of done.

Read more about NFRs and built-in quality:

Nonfunctional Requirements
Built-in Quality

Supporting DevOps and the continuous delivery pipeline

Architecture is deeply connected to customer value delivery. Good architecture can make value delivery a fast, incremental process that Agile Teams and stakeholders can control. To accomplish this, the continuous delivery pipeline (CDP) needs to be defined in a manner that best supports the needs of the ART.

Participate in the release governance process – The System Architect helps the ART develop system architecture in a way that supports incremental value delivery. Additionally, the System Architect assesses the impact of technology on specific releases.
Support design of the CDP – System Architects work on creating smooth and ongoing DevOps practices. They guide teams in planning how to set up and manage the release process, including choosing the right environments and tools. They also assist in picking the right setups for the system's infrastructure, often incorporating cloud-based solutions to make the system more scalable and adaptable. Additionally, they explore how AI can be integrated to further improve these processes.
Enable metrics instrumentation – The System Architect helps plan how a system is set up to make sure it can track important information. They use platforms and tools for this and make sure everything works together well. They also enable Lean UX by making prototypes or adding features to the system to study how users behave.

Read more about the continuous delivery pipeline:

Continuous Delivery Pipeline

References

[1] Lehman, M. M., J. F. Ramil, P. D. Wernick, D. E. Perry, and W. M. Turski. "Metrics and Laws of Software Evolution—The Nineties View." Proceedings Fourth International Software Metrics Symposium (METRICS '97), 1997.

Key Takeaways
System Architects guide Agile Release Trains (ARTs) by aligning technical visions with product goals.
System Architects foster collaboration across Agile Teams, focusing on the successful integration of technology and design.
Complex systems and products may require the involvement of multiple System Architects.
System Architects evolve architecture and ensure the adaptability of systems to meet both current and future needs.

Last update: 15 October 2024
