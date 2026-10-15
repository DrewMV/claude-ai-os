---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
status: draft
updated: 2026-09-09
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification, communication]
relationships:
  - target: "[[PI-3/pi3-physical-computer-data-validation-stories]]"
    type: derived_from
  - target: "[[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]]"
    type: related_to
---

# Email Draft — Physical Computer Data Validation: Follow-up to Monica Green

> **Status: DRAFT — not sent.** Prepared 2026-09-09 as a follow-up to a discussion with Monica Green (CCB Class Manager, Computers – Physical) on the Physical Computer Data Validation effort — see [[PI-3/pi3-physical-computer-data-validation-stories]]. Requests her confirmation on the attribute set, cadence, population scope, and location list — operationalizes **DEP-4** in that file. Log her response back against DEP-4 once received.

---

**To:** Monica Green (mmgreen@pplweb.com)
**Subject:** Physical Computer Data Validation — Follow-up & Confirmation Needed

Hi Monica,

Following up on our discussion about validating and certifying data on physical computers — here's a summary of the approach for your review and confirmation before we move into build and pilot.

**What we're proposing:** every employee with a company computer gets a short self-service task, done about once or twice a year, asking them to check two things about their own device:

- **Location** — the most common issue. People move desks, sites, or go remote, and the record doesn't update on its own, so this needs regular re-checking, not a one-time fix.
- **Asset Tag** — checked for accuracy, and recorded if it's currently blank.

Assigned To is shown on the task too, but only as reference — it's how the employee can tell "this is my device" — not something they edit or are asked to confirm. There's no fallback logic here either: a device with no listed owner at all doesn't get routed to anyone else (like the last person who logged into it); it's handled separately as a data-quality item, not through this employee-facing flow.

**Not included:** CI Owner, Technical Owner Group, and Support Group — per your confirmation, these are determined automatically from the computer's characteristics, so there's nothing for an employee to manually validate there.

**Notifications:** employees get automatic reminders as their task deadline approaches. If someone doesn't respond in time, a past-due notice goes out that also copies their manager — that's the platform's standard behavior, not something we're customizing, but you may get questions about it from Computer owners or their managers, so wanted you aware of it going in.

**What I need from you:**
1. Confirmation that Location and Asset Tag are the right (and only) fields for employees to validate on physical computers
2. Sign-off on the proposed once/twice-yearly cadence
3. Agreement on the physical-computer population this applies to (virtual computers excluded)
4. Once drafted, a quick review of the approved-location list, so the picker only shows options employees will actually recognize

One operational note for when results come in: employees who don't respond in the task window aren't individually chased — they roll into the next scheduled cycle and show up as "incomplete" rather than "certified." That's expected, not something requiring action each time.

Let me know if you'd like to discuss, or if this is good to move forward on as described.

Thanks,
Manuel
