---
source_url: https://framework.scaledagile.com/story
scraped: 2026-05-30
authenticated: true
---

Home » Story
Story

Stories act as a 'pidgin language,' where both sides (users and developers) can agree enough to work together effectively.

– Bill Wake, co-inventor of Extreme Programming

Definition: Stories are short descriptions of a small piece of desired functionality written from the user's perspective.

Summary

Stories are short, simple descriptions of functionality. They are told from the user's perspective and written in simple language. They are the primary tool Agile Teams use to describe a small, vertical slice of intended system behavior. A story provides enough information for business and technical people to understand the intent. Details are deferred until the story is ready to be implemented. Through acceptance criteria and tests, stories become more specific, helping to ensure system quality.

What is a story?

A story describes a small piece of functionality that an Agile Team can finish in a few days or less. User stories outline the value to the end user. Enabler stories outline the necessary work of exploration, architecture, infrastructure, and compliance. Each story focuses on a specific behavior that can be developed in incremental steps to offer value to the user or the solution. Keeping stories small ensures they can be completed in a single iteration, allowing every iteration to deliver value.

SAFe describes four tiers of work items that detail functional system behavior: Epic, Capability, Feature, and Story. Collectively, they represent the solution's intended behavior. The detailed implementation work is expressed through stories in the backlogs of the Agile Teams. Some stories emerge from business and enabler features in the ART Backlog, while others come from the team's local context.

Read more about the Agile Team Backlog and Enabler Stories:

Team Backlog
Enablers

How are stories created by Agile Teams?

Agile Teams usually write their stories on an index card or a sticky note. They also help visualize work and can be placed on a wall or table, rearranged in sequence, and passed around when necessary. This creates a relationship between the team, the story, and the user. The entire team participates. Stories allow an improved understanding of the scope and progress of the solution.

While anyone can write stories, the Product Owner (PO) is responsible for approving them into the team backlog and accepting them into the system baseline. Because sticky notes don't scale well across the company, stories move quickly into Agile Lifecycle Management (ALM) tooling.

In SAFe, there are two types of stories: user stories and enabler stories. These stories help break down business and enabler features.

Figure 1. Example of a business feature split into stories

User story creation

User stories are the primary way Agile Teams express the needed functionality. They replace the traditional requirements specification. In some cases, however, they help explain and develop system behavior later recorded in specifications that support compliance, suppliers, traceability, or other needs.

Since user stories are value- and customer-centric, the recommended form of expression is the 'user-voice form,' as follows:

As a (user role), I want to (activity) so that (business value)

This format guides teams to understand who is using the system, what they are doing with it, and why they are doing it. Routinely applying the 'user voice' format increases the team's domain competence; they learn to better understand their users' real business needs.

In design thinking, personas embody the characteristics of representative users to help teams better understand their potential customers. Example personas for the rider could be a thrill-seeker 'Jane' and a timid rider 'Bob.' Stories descriptions can then reference these personas. For example, "As Jane, I want…"

While the user story voice is typical, not every system interacts with a person. Sometimes, the 'user' is a device (for example, a printer) or a system (for example, a transaction server). In these cases, the story can take on the form with a 'system' as a user.

Enabler story creation

Agile Teams also develop the new architecture and infrastructure needed to implement new user stories. In this case, the story may not directly reach any end user. Teams use 'enabler stories' to support exploration, architecture, or infrastructure. Enabler stories can be expressed in technical rather than user-centric language. Agile Teams often invite System Architects to support them in writing enabler stories.

There are many other types of Enabler stories, including:

Refactoring and spikes (as traditionally defined in XP)
Building or improving development/deployment infrastructure
Running jobs that require human interaction (for example, indexing 1 million web pages)
Creating the required product or component configurations for different purposes
Verification of system qualities (for example, performance and vulnerability testing)

Enabler stories are demonstrated like user stories, typically by showing the knowledge gained, artifacts produced, or the user interface, stub, or mock-up.

What are some tips for writing good stories?

Good stories require multiple perspectives. Agile Teams use stories to create a shared understanding of what to build to reduce rework and increase throughput. Using behavior-driven development (BDD), teams collaborate to define detailed acceptance tests that describe each story thoroughly.

Collaborative story writing ensures all perspectives are addressed and everyone agrees on the story's behavior. The story's description, acceptance criteria, and acceptance tests represent its results. Using BDD, the acceptance tests are written in the system's domain language. BDD tests are then automated and run continuously to maintain built-in Quality. The BDD tests are written against system requirements (stories) and, therefore, can be used as the final statement for the system's behavior, replacing document-based specifications.

Story Writing 3Cs: the card, the conversation, and the confirmation

Ron Jeffries, one of the inventors of XP, is credited with describing the 3Cs of a story:

Card – This captures the user story's statement of intent on an index card, sticky note, or in a tool. The benefit is that the card's size limits story length and premature suggestions for the specificity of the system behavior. Cards also help the team fully grasp the scope of the work ahead. Holding ten cards in your hand is more tangible than looking at ten lines on a spreadsheet.

Conversation – This promises "a conversation" about the story between the team, the customer (or the customer's proxy), the PO (who may be representing the customer), and other stakeholders. The goal is to uncover the detailed behavior required to implement the intent. The conversation may add details to the acceptance criteria (the confirmation below) or attachments to the user story.

These just-in-time discussions create a shared understanding of the scope that a formal document cannot provide. Specifying by example replaces detailed documentation. Conversations also uncover gaps in user scenarios and non-functional requirements (NFRs).

Confirmation – The acceptance criteria provide the information needed to ensure the story is implemented correctly and covers the relevant functional and NFRs. Some teams use the confirmation section of the story card to point out what they will demo.

Agile Teams automate acceptance tests wherever possible, often in a business-readable, domain-specific language. Automation creates an executable specification to validate and verify the solution. It also enables a quick regression test of the system, enhancing Continuous Integration (CI), refactoring, and maintenance.

Attributes of a good story: applying INVEST

Agile Teams devote time to discovering, elaborating on, and understanding user stories and writing acceptance tests. This is normal since developing the solution for a desired change or addition to a product is not necessarily the most challenging part of software development.

Instead, it is understanding the details of the code to be created or changed. So, investing in good user stories at the last responsible moment is time well spent for the team. To describe the attributes of a good user story, Bill Wake coined the acronym INVEST [1]:

I – Independent (among other stories)
N – Negotiable (a flexible statement of intent, not a contract)
V – Valuable (providing a valuable vertical slice to the customer)
E – Estimatable (small and negotiable)
S – Small (fits within an iteration)
T – Testable (understood enough to know how to test it)

Creating flow: splitting stories sensibly

Smaller stories allow teams to implement them more quickly and reliably since small items flow through any system faster, reducing variability and risk. Therefore, splitting bigger stories into smaller ones is a vital skill for every Agile team. It embodies the art and the science of incremental development. The book, Agile Software Requirements, describes ten ways to split stories, including: [1]

Workflow steps
Business rule variations
Major effort
Simple/complex
Variations in data
Data entry methods
Deferred system qualities
Operations (ex., Create, Read, Update, Delete [CRUD])
Use-case scenarios
Break-out spike

Read more about Behavior Driven Development (BDD):

Behavior Driven Development (BDD)

How are stories estimated?

Agile Teams use story points and 'estimating poker' to value their work [1, 2]. A story point is a singular number that represents a combination of qualities:

Volume – How much is there?
Complexity – How hard is it?
Knowledge – What's known?
Uncertainty – What's unknown?

Story points are relative, without a connection to any specific unit of measure. Each story's size (effort) is estimated relative to the smallest story, which is assigned a size of 'one.' A modified Fibonacci sequence (1, 2, 3, 5, 8, 13, 20, 40, 100) is applied that reflects the inherent uncertainty in estimating, especially large numbers.

Agile teams often use 'estimating poker' to create quick but reliable estimates. It combines expert opinion, analogy, and disaggregation, such as splitting a story or feature into smaller, easier-to-estimate pieces.

The rules of estimating poker are:

Participants include all team members
Each estimator receives a deck of cards containing the modified Fibonacci sequence
The PO participates but does not estimate
The Scrum Master/Team Coach participates but does not estimate unless they are doing the development work
For each backlog item to be estimated, the PO reads the story's description
Questions are asked and answered
Each estimator privately selects an estimating card representing their estimate
All cards are turned over at the same time to avoid bias and to make all estimates visible
High and low estimators explain their estimates
After a discussion, each estimator re-estimates by selecting a card
The estimates will likely converge; if not, participants repeat the process

Some preliminary design discussion is appropriate. However, too much time spent preparing is often a wasted effort. The real value of estimating poker is agreeing on a story's scope. It's also fun!

How is an estimation baseline created across the ART?

In standard Scrum, each team figures out its own story point estimates and velocity without worrying about the other teams. At scale, predicting the story point size for more significant epics and features becomes difficult when team velocities vary wildly. To overcome this, SAFe teams initially calibrate a starting story point baseline where one story point is valued roughly the same across all teams.

The steps below help teams normalize story points and agree on a starting baseline for their stories and velocity:

Give every developer-tester eight points for a two-week iteration (one point for each ideal workday, subtracting two days for general overhead).
Subtract one point for every team member's vacation day and holiday.
Find a small story that would take about a half-day to code and a half-day to test and validate. Call it a 'one.'
Estimate every other story relative to that 'one.'

In this way, story points are nearly comparable across teams. Management can better understand the cost for a story point and more accurately determine the cost of an upcoming feature or epic.

While teams will usually increase their velocity over time—and that's a good thing— in reality, the number tends to remain stable. Changing team size and technical context affects a team's velocity more than productivity variations.

Velocity measures how much work a team can complete during a specific period. It is the sum of the points of the completed stories that met their definition of done (DoD). Over time, the team's average velocity (completed story points per iteration) becomes reliable and predictable. This helps with planning and limiting Work in Process (WIP), as teams don't take on more stories than their past velocity would allow.

Capacity is the available portion of the team's velocity for any given iteration. Vacations, training, and other events can make team members unavailable for an iteration's goals or some portion of the iteration. This decreases the team's maximum potential velocity for that iteration.

Note: SAFe Kanban teams typically spend less time estimating stories than Scrum teams do. The work items are generally smaller and come in to the team more frequently. In the context of SAFe, where all teams participate in Iteration Planning and associate stories to future iterations, some notion of sizing is required.

SAFe Kanban teams may initially use estimating poker or a similar process to size their stories. More likely, however, they begin breaking work into similarly sized stories, as that assists flow in general and assures that no large story blocks other stories that also need to make their way through the Kanban system.

For Agile Teams doing regular maintenance and support activities, estimating everyday backlog items has less value. However, all teams have retro items, and their Continuous Development Pipeline (CDP) may require improvements. These and other vital tasks need attention, scheduling, and estimating.

Read more about SAFe Scrum and SAFe Team Kanban:

SAFe Scrum
SAFe Team Kanban

References

[1] Leffingwell, Dean. Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise. Addison-Wesley, 2011.

[2] Cohn, Mike. User Stories Applied: For Agile Software Development. Addison-Wesley, 2004.

Key Takeaways
A story expresses a deliverable piece of functionality that an Agile Team can complete within an iteration.
User stories describe the value of work to an end user.
Enabler stories describe the value of exploration, architecture, infrastructure, and compliance work.
Agile Teams write and estimate stories together.

Last Update: 5 February 2025
