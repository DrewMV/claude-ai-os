---
source_url: https://framework.scaledagile.com/domain-modeling
scraped: 2026-05-30
authenticated: true
---

SAFe Knowledge Base » Domain Modeling

Domain Modeling

Essentially, all models are wrong, but some are useful.

—George E. P. Box

Domain Modeling is a method to describe and model entities and the relationships between them, which collectively represent the problem domain space.

Derived from understanding system-level requirements, identifying domain entities and their relationships provides a basis for understanding and designing systems for maintainability, testability, and incremental development. Because there is often a gap between understanding the problem domain and interpreting requirements, domain modeling is essential to Agile development at scale. Driven partly by object-oriented design approaches, domain modeling envisions the solution as domain objects collaborating to fulfill system-level scenarios.

In SAFe, domain models connect to the Team, ART, Solution Train, and Portfolio backlogs, providing a common language. The connection between domain models and Nonfunctional Requirements (NFRs) often helps identify alternative design approaches to satisfy the corresponding NFRs.

Domain modeling also enables organizations to use Agile design patterns and approaches that enhance long-term velocity. As the system design changes, updating and improving the domain model is vital to a continued understanding of the system and helps refactor code to reduce the system's complexity.

Introduction

Domain modeling is an essential tool for software engineering: if you only model one thing in Agile, model the domain. Even a relatively small domain modeling effort is an excellent tool for reducing the complexity of system development. It helps clarify requirements and the design intent. It reflects the current understanding of entities and their relationships and responsibilities with the problem domain. Figure 1 shows an example of a domain model for a consumer subscription management system.

Figure 1. The domain model for a consumer subscription management system

Several different views of domain models express the essential aspects of the problem domain (see [1] in chapter 8 for more detail):

Robustness diagram – a simplified UML communication and collaboration diagram. Its primary purpose is to ensure that the solution's use cases are sufficiently robust to represent its usage requirements.
CRC (Class, Responsibilities, Collaborators) cards – a tool used in brainstorming sessions to help teams collaborate on product design with an object orientation.
Object role model (ORM) diagram – shows the relationships between objects in a database and offers a conceptual approach to database modeling through objects and roles.

However, the most simple and common domain model is a class diagram illustrated in Figure 1. Such a diagram primarily shows the key conceptual entities and their relationships.

Effective domain modeling can only occur in the context of the system-level requirements, often captured as use cases or other means. Nouns from requirements become candidates for domain entities, while verbs may represent behaviors and their relationships. Together they form a Common Language (sometimes called Ubiquitous language, see [2], chapter 2) that allows engineering, business, and user representatives to speak the same language, minimizing miscommunication.

Domain Modeling in Agile at Large Scale

In large-scale Agile development, domain modeling is continuously used to support the following:

Analysis of Epics
Backlog Refinement for ARTs and Solution Trains
Design workshops at different levels
Refining Vision and Roadmap (typically in preparation for PI)

Domain modeling is generally developed and continuously refined by the System Architect in collaboration with other stakeholders to understand the impact of epics and features on the system. It's an excellent tool to prepare for PI Planning to understand the work in the upcoming PI.

The following example in Figure 2 shows how a domain model is used to clarify the impact of an epic:

Figure 2. A Domain Model Helps in understanding the scope of an epic

Requirements and domain modeling are mutually dependent. Domain modeling supports the clarification of requirements, while requirements help build and clarify the model. Moreover, the domain model should be updated once new requirements are implemented.

Figure 3 illustrates the relationship between SAFe backlog items and their impact on the domain model.

Backlog Item / Impact on Domain Model:
Epic – Typically introduces new entities, relationships, and responsibilities.
Feature – Introduces new entities, typically new relationships or responsibilities.
Story – Introduces new and updated relationships, responsibilities, value objects, and service interfaces.
Enabler Epic – Typically affects implementation and design aspects of a range of entities, services, and repositories, such as underlying technology or platform, a generic life cycle of the entities, API constraints, and so on.
Enabler Feature – Introduces changes to implementation and design aspects for specific entities and services, typically for one product or system. Enabler features may also result in a shift in responsibilities or may introduce new value objects.
Refactor – It may identify individual helper or value objects from an entity and change internal interfaces between entities, protocols, or APIs.

Figure 3. Impact of SAFe backlog items on the domain model

Relationships between entities are critical to effective modeling—without them, the model is just a vocabulary of terms since they lack their collaborative context. Relationships drive practical requirements definition and design decisions (Figure 4). Relationships in a domain model are typically standard (for example, 'includes,' 'is a') or concrete (for example, ML Admin 'defines/patches' the mailing list in our case). When determining the relationships, it is much more important to adequately capture the connections between entities that convey the meaning of their role rather than to follow format agreements indiscriminately.

The common language resulting from domain modeling is used at all levels of the Agile organization to foster a clear shared understanding of the problem domain, requirements, and architecture—see Figure 4.

Figure 4. The common language used throughout an Agile organization

Even though it is crucial to product development, a common language has limitations that every organization should know. For example, the language of marketing materials may sometimes use terms that diverge from the standard language to emphasize certain temporal or subjective aspects associated with current market trends or challenges.

Teams that use Behavior-Driven Development (BDD) inevitably use a common language in specification workshops when defining human-readable tests.

The Domain Model and System Design

Domain-Oriented vs. Alternative Approaches

Domain modeling is helpful for analysis and often a good conceptual model for system design. Domain modeling is one of the key design patterns/approaches that assume deriving the solution object model directly from the problem domain while preserving both behavior and data (see [3]). See [2] for a systematic and detailed outline of such best practices, known by Domain-Driven Design. This approach provides a natural and very effective way of managing the inherent complexity of software development that is vital at scale. Figure 5, adapted from [3], chapter 2, compares the effort spent on enhancing software functionality versus complexity when the design is based on the domain, data structure, or transaction scripts.

Figure 5. A sense of the relationship between domain-oriented and data- or transaction-centric approaches.

Large-scale software solutions almost inevitably have complex domain logic. Data- or transaction-centric design approaches imply a very high maintenance cost. Nevertheless, too many organizations end up with highly intricate system designs that require much effort to enhance the system. While in some cases, such approaches may make sense—and we will discuss those below—most often, such a design, in reality, is based on the system architects' and teams' preferences rather than on business drivers.

One of the many reasons to base system design on the domain structure is to foster reasonable usage of patterns that support maintainability and enable highly incremental, concurrent development. So, in our example of the subscription management system, domain modeling, and requirements may logically suggest that subscription methods will represent the primary source of change. Given the different scenarios for opt-in and opt-out functionality, it's logical to use a Bridge Pattern, shown in Figure 6, to isolate the area of frequent change and reduce the number of entities in the system—(see [4], Appendix B).

Figure 6. A bridge pattern derived from analysis of the domain model

This is just one example of how domain modeling can be effectively used for Commonality-Variability Analysis (CVA) to foster effective system object models. (See [5], chapter 8 for more detail on the CVA method).

Domain Modeling, System Design, and Nonfunctional Requirements

Nonfunctional Requirements, on the other hand, represent the primary reason for building system design around data structure or transaction scripts rather than the domain model. Typically NFRs like performance or scalability may result in domain logic being spread across large SQL scripts, where too much logic is in the client-side validation scripts, and so on. Even though the use of such a transaction script approach (see [3], chapter 9) can be legitimate in some instances, it should be used as an exception rather than the rule. Few properly implemented exceptions will allow the Agile enterprise to benefit from a domain-oriented approach.

Refactoring the Model

Developing a shared understanding of the system with the help of domain modeling is an incremental process, just like creating code that implements the underlying domain logic. This means that just like the code, the domain model is also subject to refactoring as our knowledge about the system improves and new domain entities and their relations actualize. Keeping the system design and the current understanding of the problem domain updated in the domain-driven design approach is relatively simple. Refactoring of both typically happens synchronously or nearly so (see [2], part III). Designing an effective domain model is both an art and a science. Not uncommonly, great insights about the structure and relationships in the domain model emerge eventually. However, it is never late to start building the proper understanding and gradually improving the code towards it—as new functionality allows—to control complexity.

Summary

Domain modeling is an excellent tool for Agile enterprises to carry out a common language and a fundamental structure for analyzing features and epics. The domain model is defined and continuously refactored as enterprise knowledge about the domain improves, and the system functionality evolves.

Domain models provide a vital link between the problem domain and the code. Domain-oriented design approaches enable controlling the growing complexity and cost of maintenance and enhancement effort. Domain modeling is a highly visual and collaborative effort that creates a shared understanding of the priorities and better ways to implement them. It typically involves System Architects, Product Management, Agile Teams, and stakeholders. No other models cover as many aspects of Agile development at scale. If you only model one thing, model the domain.

Learn More

[1] Ambler, Scott. Agile Model-Driven Development with UML 2.0. Cambridge University Press, 2004.

[2] Evans, Eric. Domain-Driven Design: Tackling Complexity in the Heart of Software. Addison Wesley, 2003.

[3] Fowler, Martin. Patterns of Enterprise Application Architecture. Addison Wesley, 2002.

[4] Bain, Scott. Emergent Design: The Evolutionary Nature of Professional Software Development. Addison Wesley, 2008.

[5] Shalloway, Alan, and James Trott. Design Patterns Explained: A New Perspective on Object-Oriented Design. Addison Wesley, 2004.

Last update: 2 March 2023
