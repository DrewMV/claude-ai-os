---
source_url: https://framework.scaledagile.com/compliance
scraped: 2026-05-30
authenticated: true
---

SAFe Knowledge Base » Compliance

Compliance

Trust, but verify.

—Ronald Reagan, citing a Russian proverb

Definition: Compliance refers to the strategy, activities, and artifacts that allow teams to apply Lean-Agile development methods to build systems that have the highest possible quality, while simultaneously ensuring they meet regulatory, industry, and other relevant standards.

Enterprises use SAFe to build some of the world's largest and most important systems, the failure of which may have unacceptable social or economic costs. These high-assurance systems include medical devices, automobiles, avionics, banking and other financial services, aerospace, and defense. To protect public safety, these systems are often subject to extensive regulatory or customer oversight and rigorous compliance requirements. In addition, many enterprises are subject to government regulations (examples: Sarbanes-Oxley, HIPAA, ACA, state insurance regulations) that require similar attention and auditing to ensure compliance.

Organizations operating under such regulations have relied on comprehensive quality management systems (QMS). However, legacy QMS systems are based on traditional, phase-gated development models that cannot keep pace with accelerating time-to-market demands. Of more significant concern is that even when the higher Cost of Delay (CoD) is accepted, these traditional approaches often do not increase quality or eliminate risk. As Deming notes, "Inspection is too late. The quality, good or bad, is already in the product." [1]

One of the ten practices of SAFe's Enterprise Solution Delivery competency is 'continually addressing compliance concerns'. This article extends that knowledge and offers guidance on applying Lean-Agile methods to build these systems faster and better while addressing critical compliance requirements.

Note: A white paper supports this article, 'Achieving Regulatory and Industry Standards Compliance with the Scaled Agile Framework(SAFe),' which you can download at the SAFe website. In addition, there is a SAFe webinar on the topic, with Q&A.

Details

Traditional waterfall practices often mandate that full system specifications are defined and committed to in detail, up-front, long before all the actual needed system behaviors can be known. Worse, the sequential nature of phase-gate development produces large batches of work, long cycles between system integration points, and late feedback. In addition, compliance activities are typically deferred until the end of the project, providing little insight into compliance progress.

This often results in missed deadlines, disappointing business or mission outcomes, lower quality, and substantial (and late) compliance challenges. In contrast, high-assurance Lean-Agile development builds in quality incrementally—early and throughout the development lifecycle.

The Role of the Quality Management System

To satisfy compliance requirements, organizations must demonstrate that their system meets its intended purpose and has no unintended consequences that might cause harm. They must also develop the objective evidence required to prove that the system conforms to those standards. To that end, organizations that build high-assurance systems define their approved practices, policies, and procedures in a QMS. These systems ensure that development activities and outcomes comply with all relevant regulations and provide the required documentation to prove it.

Unfortunately, many QMS systems are heavily influenced by traditional phase-gated waterfall methods. This seriously inhibits, and can even prevent, the adoption of newer techniques, as the older methods are hard-coded into the only approved way of working. As Figure 1 illustrates, SAFe describes an incremental approach to development and compliance that includes five recommended practices.

Figure 1. A Lean-Agile quality management system improves quality and makes compliance more predictable

Clearly, those who want the benefits of Lean-Agile development (faster time to market and higher quality, to name a few) will have to evolve a Lean QMS.

The remainder of this article provides guidance on these five specific practices teams can use to achieve high-assurance systems compliance.

Build the Solution and Compliance Incrementally

Even with a set of robust specifications, Agile Teams never have all the answers when development begins. Instead, they have a set of hypotheses that must be tested through a series of short, iterative experiments, providing validated learning to advance toward the ultimate solution. Figure 2 highlights SAFe's incremental development approach, comparing Shewhart/Deming's Plan-Do-Check-Adjust (PDCA) [2] learning cycles with a traditional waterfall model.

Figure 2. Rapid Plan-Do-Check-Adjust learning cycles increase system quality and reduce compliance risk

Figure 2 illustrates two important implications for compliance. First, building smaller, working parts of the solution early allows compliance activities to also begin early, removing the large set of such actions at the end. Each increment assesses both the viability of the current solution and its progress toward compliance, providing early feedback on the system's ultimate fitness for use. Second, specifications are created early and evolve over time in small batches, with faster feedback on decisions and the opportunity for continuous review and assessment.

Organize for Value and Compliance

Agile Release Trains (ARTs) are the primary value delivery organizations in SAFe. Each train requires all the skills necessary to build and release the Solution, including those responsible for Quality Assurance (QA), security, testing, and Verification and Validation (V&V). (Note: While some regulations require independent, objective assurance, compliance representatives can still participate continuously as ART members). The result is an ART that includes compliance competency, as illustrated in Figure 3.

Figure 3. Agile Release Trains include all disciplines, including compliance

Solution and Product Management ensure that the Solution Intent and backlog properly reflect compliance requirements. Teams also ensure that their work includes appropriate compliance activities.

Build In Quality and Compliance

Built-In Quality is a dimension of SAFe's Team and Technical Agility competency and a core tenet of the Lean-Agile Mindset. SAFe describes using Built-In Quality practices, including automation, to detect compliance and quality problems. This philosophy applies Systems Thinking by 'optimizing the whole,' ensuring fast flow across the entire Development Value Stream, and making quality everyone's job. Quality becomes a culture, not a job title.

To that end, compliance concerns are also built directly into the development process, and automated wherever possible, as illustrated in Figure 4.

Figure 4. Automating compliance with design-build-test automation

However, not all compliance activities can be automated, as some regulatory requirements mandate manual activities, such as Failure Mode and Effects Analysis (FMEA) and audits. This work is planned as part of the Team Backlog as part of the regular flow of work. The goal is to conduct these activities and reviews as the solution is being built, reducing the last sign-off activity from a significant, extended event to a quick and boring 'non-event.'

This approach provides early feedback on the degree to which the team's compliance activities are being performed and how those activities may impact team performance. Figure 5 shows the feedback cycle between compliance and the practices defined by the Lean QMS.

Figure 5. PIs and retrospectives provide feedback loops for compliance activities

Continuously Verify and Validate (V&V)

High-assurance systems require Verification and Validation (V&V) to ensure that:

The system works as designed (verification)
It meets the intent of its purpose and functions (validation)

V&V must always occur against a known set of requirements. Otherwise, there is nothing to V&V. As Figure 6 illustrates, SAFe uses solution intent as the repository for existing and emerging requirements and designs that are the subject of V&V.

Figure 6. SAFe's Solution Intent provides support for Verification and Validation

Traceability within the solution intent ensures that the artifacts produced—the actual software, hardware components, etc.—always address regulatory and compliance specifications, providing end-to-end evidence that V&V requirements have been met.

The SAFe Requirements Model Supports V&V

To assure compliance, all material requirements elements (feature, story, NFRs) have test cases that are created at the same time as the functionality (Figure 7).

Figure 7. SAFe's requirements meta-model supports Verification and Validation

Each increment yields new functionality and, consequently, adds new tests. As the number of tests grows, automation is vital to prevent testing activities from becoming bottlenecks.

Make V&V and Compliance Activities Part of Flow

To improve flow, V&V activities are performed in small batches. Each work item includes all the necessary information required for compliance. Any reviews, audits, and sign-offs are included in the work item's definition of done (DoD), as shown in Figure 8. Each PI, the System Demo evaluates the solution's progress toward its operational goals and the objective evidence necessary to assure compliance.

Figure 8. Verification and Validation activities are integral to a continuous flow of value

Release Validated Solutions on Demand

Finally, although the product development process happens on a predictable cadence (See Principle #7 - Apply cadence, synchronize with cross-domain planning), the release process may require additional activities. These can include:

Validation testing of the final release candidate (examples: medical trial, flight test)
Review of the objective evidence needed before production approval and release
Customer and user acceptance tests, document submissions, regulatory approvals

These can be extensive activities and must be included in planning and development. Even then, Lean-thinking organizations constantly strive to fully automate the delivery and, wherever possible, build in automated final release checks as part of a SAFe Continuous Delivery Pipeline and Release on Demand.

Learn More

[1] Deming, W. Edwards. Out of the Crisis. The MIT Press, 2018.

[2] PDCA. Wikipedia.

Leffingwell, Dean. Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise. Addison-Wesley Professional, 2010.

Last update: 4 October 2023
