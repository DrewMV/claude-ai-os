---
source_url: https://framework.scaledagile.com/lean-ux
scraped: 2026-05-30
authenticated: true
---

SAFe Knowledge Base » Lean UX

Lean UX

What if we found ourselves building something that nobody wanted? In that case, what did it matter if we did it on time and on budget?

—Eric Ries

Definition: Lean User Experience (Lean UX) is a team-based approach to building better products by focusing less on theoretically ideal design and more on iterative learning, overall user experience, and customer outcomes.

Lean UX design extends the traditional UX role beyond merely executing design elements and anticipating how users might interact with a system. Instead, it encourages a far more comprehensive view of why a Feature exists, the functionality required to implement it, and the benefits it delivers. By getting immediate feedback to understand if the system will meet the fundamental business objectives, Lean UX provides a closed-loop method for defining and measuring value.

Details

Generally, UX represents a user's perceptions of a system—ease of use, utility, and the user interface's (UI) effectiveness. UX design focuses on building systems that demonstrate a deep understanding of end users. It considers users' needs and wants while making allowances for their context and limitations.

When using Agile methods, a common problem is how best to incorporate UX design into a rapid Iteration cycle, resulting in a full-stack implementation of the new functionality. When teams attempt to resolve complex and seemingly subjective user interactions while simultaneously trying to develop incremental deliverables, they can often churn through many designs, creating frustration with Agile.

Fortunately, the Lean UX movement addresses this using Agile development with Lean Startup implementation approaches. The mindset, principles, and practices of SAFe reflect this thinking. This process often begins with the SAFe Lean Startup Cycle described in the Epic article. It continues developing Features and Capabilities using the Lean UX process described here.

As a result, Agile Teams and Agile Release Trains (ARTs) can leverage a common strategy to generate rapid development, fast feedback, and a holistic user experience that delights users.

The Lean UX Process

In Lean UX, Gothelf and Seiden [2] describe a model we have adapted to SAFe, as Figure 1 illustrates.

Figure 1. The Lean UX Process (adapted from Ref [2])
Benefit Hypothesis

The Lean UX approach starts with a benefit hypothesis: Agile teams and UX designers accept that the right answer is unknowable up-front. Instead, teams apply Agile methods to avoid Big Design Up-front (BDUF), focusing on creating a hypothesis about the feature's expected business result. Then they implement and test that hypothesis incrementally.

The SAFe Feature and Benefits matrix (FAB) can be used to describe the hypothesis as it moves through the Continuous Exploration aspect of the CDP:

Feature – A short phrase giving a name and context
Benefit hypothesis – The proposed measurable benefit to the end-user or business

Note: Design Thinking practices suggest changing the order of the feature benefit hypothesis elements to identify the customer benefits first and then determine what features might satisfy their needs.

Outcomes are measured in the Release on Demand aspect of the CDP. They are best done using leading indicators (see Innovation Accounting in [1]) to evaluate how well the new feature meets its benefits hypothesis. For example, "We believe the administrator can add a new user in half the time it took before."

Collaborative Design

Traditionally, UX design has been an area of high specialization. People with a talent for design, a feel for user interaction, and specialty training are often entirely in charge of the design process. The goal was 'pixel perfect' early designs, done before the implementation. But this work was often done in silos by specialists that may or may not know the most about the system and its context. Success was measured by how well the implemented user interface complied with the initial UX design. In Lean UX, this changes dramatically:

"Lean UX has no time for heroes. The entire concept of design as a hypothesis immediately dethrones notions of heroism; as a designer, you must expect that many of your ideas will fail in testing. Heroes don't admit failure. But Lean UX designers embrace it as part of the process." [2]

Continuous exploration takes the hypothesis and facilitates an ongoing and collaborative process that solicits input from a diverse group of stakeholders – Architects, Customers, Business Owners, Product Owners, and Agile Teams. This group further refines the problem and creates artifacts that clearly express the emerging understanding, including personas, empathy maps, and customer experience maps (see Design Thinking).

Agile teams are empowered to design and implement collaborative UX, significantly improving business outcomes and time-to-market. Moreover, another important goal is to deliver a consistent user experience across various system elements or channels (for example, mobile, web, kiosk) or even different products from the same company. Enabling this consistency requires balancing decentralized control with centralizing certain reusable design assets (following Principle #9 – Decentralize decision-making). For example, creating a design system [2] with a set of standards that contains whatever UI elements ARTs and Value Streams find helpful, including:

Editorial rules, style guides, voice and tone guidelines, naming conventions, standard terms, and abbreviations
Branding and corporate identity kits, color palettes, usage guidelines for copyrights, logos, trademarks, and other attributions
UI asset libraries, which include icons and other images, templates, standard layouts, and grids
UI widgets, which include the design of buttons and other similar elements

These centralized assets are integral to the Architectural Runway, which supports decentralized control while recognizing that some design elements must be centralized. After all, these decisions are infrequent, long-lasting, and provide significant economies of scale across both the user base and enterprise applications, as described in Principle #9.

Building a Minimum Marketable Feature

With a hypothesis and design, teams can implement the functionality as a Minimal Marketable Feature (MMF). The MMF should be the smallest amount of functionality that must be provided for a customer to recognize any value and for the teams to learn whether the benefit hypothesis is valid.

By creating an MMF, the ARTs apply SAFe Principle #4 – Build incrementally with a fast, integrated learning cycle to implement and evaluate the feature. Teams may preserve options with Set-Based Design as they define the initial MMF.

In many cases, extremely lightweight and not even functional designs can help validate user requirements (ex., paper prototypes, low-fidelity mockups, simulations, API stubs). In other cases, a vertical thread (full stack) of just a portion of an MMF may be necessary to test the architecture and get fast feedback at a System Demo. However, in some instances, the functionality may need to proceed to deployment and release, where application instrumentation and telemetry provide feedback data from production users.

Evaluating

MMFs are evaluated as part of deploying and releasing (where necessary). There are various ways to determine if the feature delivers the proper outcomes. These include:

Observation – Wherever possible, directly observe the actual usage of the system. It's an opportunity to understand the user's context and behaviors.
User surveys – A simple end-user questionnaire can obtain fast feedback when direct observation isn't possible.
Usage analytics – Lean-Agile teams build analytics into their applications, which helps validate initial use and provides the application telemetry needed to support a Continuous Delivery model. Application telemetry offers constant operational and user feedback from the deployed system.
A/B testing – This is a form of statistical hypothesis comparing two samples, which acknowledges that user preferences are unknowable in advance. Recognizing this is liberating, eliminating endless arguments between designers and developers—who likely won't use the system. Teams follow Principle #3 – Assume variability; preserve options to keep design options open as long as possible. And wherever it's practical and economically feasible, they should implement multiple alternatives for critical user activities. Then they can test those other options with mockups, prototypes, or even full-stack implementations. In this latter case, differing versions may be deployed to multiple subsets of users, perhaps sequenced over time and measured via analytics.

In short, measurable results deliver the knowledge teams need to refactor, adjust, redesign—or even pivot to abandon a feature based solely on objective data and user feedback. Measurement creates a closed-loop Lean UX process that iterates toward a successful outcome, driven by evidence of whether a feature fulfills the hypothesis.

Implementing Lean UX in SAFe

Lean UX differs from the traditional, centralized approach to user experience design. The primary difference is how the hypothesis-driven aspects are evaluated by implementing the code, instrumenting where applicable, and gaining user feedback in a staging or production environment. Implementing new designs is primarily the responsibility of the Agile Teams, working in conjunction with Lean UX experts.

Of course, this shift, like many others with Lean-Agile development, can cause significant changes to the way teams and functions are organized, enabling a continuous flow of value. For more on coordinating and implementing Lean UX —specifically how to integrate Lean UX in the PI cycle—read the advanced topic article Lean UX and the PI Lifecycle.

Learn More

[1] Ries, Eric. The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses. Random House, Inc, 2011.

[2] Gothelf, Jeff, and Josh Seiden. Lean UX: Designing Great Products with Agile Teams. O'Reilly Media, 2016.

[3] Leffingwell, Dean. Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise. Addison-Wesley, 2011.

Last update: 21 February 2023
