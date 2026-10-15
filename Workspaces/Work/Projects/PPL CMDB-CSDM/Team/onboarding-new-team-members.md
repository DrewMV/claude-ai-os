---
workspace: Work
project: CMDB-CSDM
tags: [work, cmdb-csdm, team, reference, process, art, safe]
updated: 2026-10-13
---

# Onboarding New Team Members (A-INFOPS ART)

Source: A-INFOPS ADO wiki page *"Onboarding Team Members"*, authored by Nolan LeBlanc (RTE), last edited Sep 30. ART-level standard — applies to every INFOPS agile team, including CMDB-CSDM.

> Baseline accesses every INFOPS team member needs. Individual teams may require additional, team-specific access on top of this.

Child pages on the same ADO wiki: [[Team/offboarding-team-members]], *Requesting Access for the A-INFOPS Devops Project*, *SAFe Training and Certification*.

## The Steps

### 1. PAN submission
Verify the person's name is spelled correctly on the PAN. A misspelling propagates into every downstream account and access request.

### 2. PPL training (HCM)
Once the basic account exists, the new member must check HCM for assigned training. Required courses gate access — accesses are not granted (and can be *revoked later*) if training is not completed on schedule.

- Critical — FERC Standards of Conduct
- Critical — IT Cybersecurity Awareness

Tell them to re-check HCM every few weeks; new training gets assigned over time and lapsing can cost them access.

### 3. Provide key links
- MyApps — https://myapplications.microsoft.com/
- ADO Wiki home (Infrastructure and Operations ART) — https://dev.azure.com/PPLElectric/A-INFOPS/_wiki/wikis/A-INFOPS.wiki/12571/Infrastructure-and-Operations-ART

### 4. Add to the Master Roster
Update `SAFe Master Roster.xlsx`, **Infrastructure** tab. See also [[Team/team-roster]] and [[Team/art-staffing]].

### 5. SRS for other application access
Raise an SRS for anything else the role needs — e.g. Lucidchart, Miro, ServiceNow ITIL role (needed to view incidents/requests).

### 6. SAFe training
Enroll via the **SAFe Training Request**; check status in the **SAFe Training Tracker**.

| Role | SAFe training |
|---|---|
| Agile Team Member | Agile for Operators |
| PO | Agile for Leaders |
| SM | SAFe for Scrum Masters |
| PM | PO/PM |

**Accenture team members go through Jacob Oberman**, not the standard PPL request path — details on the *SAFe Training and Certification* child page. This is the path that applies to most of the CMDB-CSDM delivery team.

### 7. Brief on agile ceremonies
Share the ART Ceremonies article links. See [[safe-ceremony-schedule]] for the CMDB-CSDM cadence.

### 8. ADO access
Add the person to the INFOPS ADO project — see the *Requesting Access for the A-INFOPS Devops Project* child page.

### 9. ADO license
Confirm a **Basic** license (not Stakeholder). References on the wiki: *Access: ADO 'basic' License*, *ADO Access and License Check*, *ADO Licensing Access Types*.

### 10. Teams site access
Request access to **General | Infrastructure and Operations ART**. The RTE or PM may need to approve — for CMDB-CSDM that is Nolan LeBlanc.

### 11. IT Reinvention site access
For **POs, SMs, and Product Analysts** only: request access to **General | IT Reinvention**.

### 12. Team ceremonies
Add them to the team's recurring ceremonies, and forward the Demo Day series, Inspect & Adapt, and PI Planning invites.

## Notes for CMDB-CSDM

- Steps 2, 6, 9, and 11 are the ones that most often stall. Training (2/6) and ADO license (9) have external dependencies; IT Reinvention access (11) is role-gated and easy to miss for new POs/SMs.
- Access friction is a recurring theme on this team — see [[Team/impediments-log]]. Front-load steps 1, 8, and 9 so the person can see the backlog on day one.
- Reusable per-person checklist: [[Team/onboarding-checklist-template]].
