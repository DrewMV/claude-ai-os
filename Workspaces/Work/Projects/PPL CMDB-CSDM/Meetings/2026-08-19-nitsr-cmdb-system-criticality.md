---
type: meeting-notes
workspace: Work
project: CMDB-CSDM
date: 2026-08-19
topic: NITSR — CMDB & System Criticality Assessment (SCA) Sequencing
organizer: Shannon Redmond
attendees: [Rohan Dixit, Shannon Redmond, Gaurav Parmar, Charles Getz, Don Udhus, Joe Dames, Ryan Jolliffe, Andy Keller, Manuel Vazquez, Jordan Yung, Dan Miller]
updated: 2026-08-19
tags: [work, cmdb-csdm, nitsr, system-criticality, servicenow-irm, lifecycle]
source: email — Rohan Dixit, "Notes: NITSR: CMDB & System Criticality Assessment", 2026-08-19 08:35
---

# NITSR — CMDB & System Criticality Assessment (SCA) Sequencing

**Meeting:** Tuesday, August 18, 2026, 2:30–3:00 PM ET
**Notes distributed:** Rohan Dixit, 2026-08-19

## Objective

Discuss whether CMDB CI creation and the System Criticality Assessment (SCA) can be moved earlier in the NITSR process to better support architecture reviews, procurement activities, and the future ServiceNow IRM process.

## Action Items

| Action Item | Owner | Due Date |
|---|---|---|
| Evaluate feasibility of creating CMDB application records earlier in the NITSR process and confirm recommended lifecycle/status approach | Jordan Yung / **Manuel Vazquez** (with Joe Dames) | **Target feedback by Aug 28** |
| Review handling of applications that do not receive NITSR approval (inactive, deletion, lifecycle status, etc.) | Jordan Yung / CMDB Team | TBD |
| Research ServiceNow out-of-the-box lifecycle stage options that support applications under evaluation | **Manuel Vazquez** | TBD |
| Create visual comparison of current-state vs. proposed future-state NITSR process flow | Rohan Dixit / Shannon Redmond | Aug 18 |
| Share updated process diagrams with Cyber Governance stakeholders once future-state approach is defined | Rohan Dixit / Shannon Redmond | Aug 18 tentative, Aug 28 target |
| If earlier CI creation is not feasible, reconvene with additional ServiceNow IRM stakeholders to evaluate alternatives | Charles Getz / Cyber Governance Team / Shannon Redmond | As needed |

## Key Discussion Points

### 1. Why system criticality matters
- System Recovery Tier / SCA influences solution architecture requirements, technology approval discussions, and procurement/cost considerations.
- Concern: assessing criticality *after* Technology Approval may be too late to inform architecture design and funding decisions made during Technology Approval Review (TAR).

### 2. Current state challenges
- Criticality assessments currently performed in **OneTrust**.
- Assessments can start before a CMDB CI exists — causes reconciliation issues later when names/identifiers differ between systems.
- Historical tracking is difficult when app names change or original requestors leave.

### 3. Future ServiceNow IRM requirements
- Cyber Governance moving from OneTrust to **ServiceNow IRM** next month (~Sept 2026).
- Without a CI record, IRM cannot automatically identify applications requiring assessment.
- CI is required to associate applications with governance entities, controls, risk assessments, and compliance activities.

### 4. Proposal — move CMDB/SCA earlier
- Create a preliminary application record (CI) earlier in the process, enabling SCA earlier in NITSR.
- Run SCA in parallel with architecture, security, and compliance reviews.
- Use a lifecycle stage/status (e.g., "Under Evaluation," "Pending") to represent apps still under review.

### 5. CMDB team considerations (Jordan & Manuel)
Support for exploring earlier CI creation, with concerns:
- Preventing stale/obsolete application records if a NITSR is ultimately rejected.
- Aligning with ServiceNow lifecycle stage/status standards.
- Preferring out-of-the-box lifecycle functionality over customization.

Concepts discussed:
- Statuses: **Under Evaluation**, **Non-Operational**, other OOTB lifecycle stages.
- Automate status sync between CMDB and NITSR so CI entries update automatically if a NITSR is rejected.

### 6. NITSR process impacts
- **Current state:** Technology Approval + Supply Chain (PO) Approval occur *before* CMDB CI creation and SCA.
- **Proposed future state:** CMDB CI creation + SCA occur earlier, in parallel with initial technology review.
- Don Udhus: if SCA moves earlier, it should be **required before TAR** — recovery tier drives architecture design and associated costs.

### 7. Alternate approach (if earlier CI creation isn't approved)
- NITSR form could capture an *expected* recovery tier.
- Risk: technology approvals proceed on assumptions instead of a completed assessment → possible rework after NITSR approval.

## Decisions

- **Confirmed:** No final decision made. CMDB team to evaluate feasibility and alignment with ServiceNow standards.
- **Tentative direction:** Viable path exists to create application records earlier using lifecycle stages + automated status updates, pending CMDB team review.

## Open Questions

- Can a CI be created before Technology Approval without creating long-term CMDB data quality issues?
- What lifecycle/status values should represent applications still under evaluation?
- Can the CMDB CI be automatically updated based on NITSR lifecycle (e.g., on rejection)?
- How should rejected NITSR requests be represented in CMDB?
- Should SCA completion become a prerequisite for Technology Approval Review?
- **Manuel's follow-up (2026-08-19):** Does NITSR request only applications, or other component types too (hardware, SaaS software, customer apps were seen as options on the form)? CIs are class-specific — unclear how a single NITSR request maps to CMDB if it spans multiple CI classes. Needs clarification before scoping the Aug 28 feedback.

## Related

- Ties into [[csdm5-terminology]] (Application Service / Service Instance) — if NITSR-driven CIs are Business Applications, need to confirm which class/table they land in given the CSDM 5 Service Instance shift.
- Feeds the **Aug 28 target feedback** owned by Manuel (with Jordan/Joe) — track in [[Memory]] Open Action Items once scoped.
