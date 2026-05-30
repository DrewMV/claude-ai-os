---
source_url: https://framework.scaledagile.com/behavior-driven-development
scraped: 2026-05-30
authenticated: true
---

SAFe Knowledge Base » Behavior-Driven Development

Behavior-Driven Development

It's just what I asked for, but not what I want.

—The Night Before Implementation poem, Author Unknown

Behavior-Driven Development (BDD) is a test-first, Agile Testing practice that provides Built-In Quality by defining (and potentially automating) tests before or as part of specifying system behavior. BDD is a collaborative process that creates a shared understanding of requirements between the business and the Agile Teams. Its goal is to help guide development, decrease rework, and increase flow. Without focusing on internal implementation, BDD tests are business-facing scenarios that attempt to describe the behavior of a Story, Feature, or Capability from a user's perspective.

When automated, these tests ensure that the system continuously meets the specified behavior even as the system evolves. That, in turn, enables Release on Demand. Automated BDD tests can also serve as the definitive statement regarding the as-built system behavior, replacing other types of behavioral specifications.

Details

Align on System Behavior

Aligning on precisely what to build is a challenge when developing innovative systems. In addition, new ideas are difficult to communicate with the diverse stakeholders responsible for system implementation. Figure 1 illustrates the three perspectives (called the triad [1]) required to define solution behavior clearly:

Customer-centric stakeholders understand customer and business needs and the relative desirability and viability of a new requirement
Development-centric stakeholders understand the solution space and technological feasibility
Test-centric stakeholders consider the exceptions, edge cases, and boundary conditions for the new behavior

Figure 1. Cognitive diversity is required to define solution behavior

Together, this group reaches alignment on precisely what to build to reduce the rework associated with making the wrong thing and accelerate the flow of value.

The Behavior-Driven Development Process

The BDD process moves through three phases—discovery, formulation, and automation—where the acceptance criteria are transformed into acceptance tests that are later automated. The process begins in the discovery phase. The Product Owner or Product Manager creates acceptance criteria for writing a story or feature (see the confirmation part of 3Cs in the "Writing Good Stories"). The discovery process is collaborative; team members also discover and contribute additional criteria.

As a backlog item moves closer to implementation, the formulation phase solidifies acceptance criteria by creating acceptance tests. Initial acceptance criteria are often described with ambiguous, general terms. The formulation phase resolves these ambiguities by turning the scenarios into detailed acceptance tests that are specific, clear, unambiguous examples of behavior.

The automation phase automates the acceptance tests, which can be run continuously and validate that the system supports the new behavior.

BDD aims to express requirements unambiguously, not simply create tests [1]. The result may be viewed as an expression of requirements or a test, but the result is the same. Acceptance tests record the decisions made in the conversation between the team and the Product Owner so that the team understands the intended behavior. There are three alternative labels to this detailing process:

Behavior Driven Design (BDD)
Acceptance Test-Driven Development (ATDD),
Specification by Example (SBE)

Although slight differences exist in these approaches, they all emphasize understanding requirements before implementation.

A Behavior-Driven Development Example

Behavior description begins with a story, feature, or capability specified by its acceptance criteria. All of these are defined using terms from the customer's domain, not from the implementation. Here is an example story and its acceptance criteria:

Figure 2. An example Story and acceptance criteria

The acceptance criteria could also be written in 'Given-When-Then' (GWT) format as shown below:

Given a speed limit
When the car drives
Then it is close to the speed limit but not above it

Even then, elaborated acceptance criteria are typically insufficient to code the story. To remove ambiguity, formulate the scenario into one or more examples that specify the details of the behavior, resulting in a specific acceptance test:

Given speed limit is 50 mph
When the car drives
Then its speed is between 49 and 50 mph

In collaboration with the team (the triad), additional acceptance criteria and scenarios will emerge; for example: When the speed limit changes, the speed changes without excessive force.

This criterion results in an additional test (or tests) that stipulate what excessive deceleration is acceptable:

Given speed limit is 50 mph
When the speed limit changes to 30 mph
Then deceleration rate should be less than 5 feet/sec/sec

Figure 3 illustrates the BDD process that begins with a story and details its specification in two dimensions. Horizontally, additional acceptance criteria describe the story's requirements. Vertically, other acceptance tests detail those acceptance test requirements.

Figure 3. The BDD process details behavioral specifications

Automating Acceptance Tests

Automating these business-facing tests is an important reason to use the Given-When-Then format. Frameworks, including Cucumber and 'Framework for Integrated Testing' (FIT), can be used to support this syntax. To support regression and continuous delivery, tests should be automated wherever possible.

Story acceptance tests are written and executed in the same iteration as the code development. If a story does not pass its tests, the team does not receive credit for that story. Features and capabilities have acceptance tests showing how several stories work together in a broader context. Typically, these tests represent the behavior of more significant workflow scenarios and should run during the iteration when the feature or capability is finished.

Learn More

[1] Pugh, Ken. Lean-Agile Acceptance Test-Driven Development: Better Software Through Collaboration. Addison-Wesley, 2011.

Last update: 27 February 2023
