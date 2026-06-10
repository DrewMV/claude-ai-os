---
type: ceremony
ceremony: backlog-refinement
meeting-name: SCCM Backlog Refinement
pi: PI-2
iteration: 2.2
iteration-start: 2026-05-27
iteration-end: 2026-06-09
date: 2026-06-08
duration-seconds: 1623
status: completed
workspace: Work
project: CMDB-CSDM
attendees: [Alex Phan (SM), Joe Dames (PO), Kiran, Vinay, Stan, Manuel, Tony, Laurent]
mentioned: [Sonica, Anu, Bhushan, Dan]
tags: [work, agile, safe, backlog-refinement, cmdb-csdm, sccm, nowassist]
---

# SCCM Backlog Refinement — Iteration 2.2 (2026-06-08)

> **Transcript note:** "CNEB" and "CNMB" in the source transcript are transcription errors for **CMDB**. "ServiceNet Discovery" = **ServiceNow Discovery**.

This session focused on SCCM precedence stories, upgrade-related spikes, NowAssist assignments, and capacity planning heading into Sprint 2.3 (starting June 10).

---

## Stories Reviewed

### SCCM Stories (Feature 1356826)

| ADO Story ID | Title | Decision | Notes |
|---|---|---|---|
| 1403763 | SCCM Server Hardware & Software Attribute Data Precedence | ✅ Ready | SCCM is authoritative for Manufacturer, Model, BIOS serial, CPU, Disk, RAM. ServiceNow Discovery updates only if value is blank. ~1 day effort incl. testing. Approved the previous Thursday. Joe confirmed no objections. |
| 1403760 | SCCM: Servers — Domain and Network Attribute Data Precedence | ✅ Ready (P2) | Assigned to Vinay. Approved the previous Thursday. Vinay confirmed ready to proceed. |
| 1403762 | SCCM: Servers — Last Seen Timestamp Alignment | ⚠️ Blocked | Requires adding 2 new attributes to computer class. Fields created in dev. **Pending Sonica approval** before moving forward. Vinay confirmed he has what he needs technically. Coordination needed with Dan. Stan to send customization details to Alex for approval issue creation. |
| 1403759 | SCCM: Servers — De-Prioritize SCCM Attributes (asset tag, OU name) | 🔴 On Hold | Pending attribute mapping review with Ray. Analysis shows most records lack these values — precedence roles will be adjusted to unselect these attributes. Approval status unclear. **Separate call required** with Alex, Vinay, Joe, and Manuel to resolve. |

### Spike Stories

| ADO ID | Title | Decision | Notes |
|---|---|---|---|
| 1402555 | CMDB: Identify CI Classes for Group 1 | ✅ Approved | Onboarding network devices into CMDB ecosystem for improved visibility, data accuracy, and service mapping. Approved Friday. Sized 2 pts. Stan and Joe confirmed ready. |
| 1403733 | Identify deprecated plugins/features that could impact CMDB capabilities | ✅ Approved | Identify plugins/features for platform upgrade planning to avoid capability loss. Approved by Manuel and Joe given upcoming ServiceNow upgrade. |

### NowAssist Stories (Feature 1436574 — Obj 5)

| ADO Story ID | Title | Assigned To | Size |
|---|---|---|---|
| 1436576 | Confirm Platform Prerequisites for NowAssist Activation | Karen | 1 pt |
| 1436579 | Activate Now Assist for CMDB Plugin | Karen | 1 pt |
| 1436593 | Activate Contextual CI Form Help Skill | Karen | 1 pt |
| 1436592 | Activate CI Summarization Skill | Karen | 1 pt |

Karen assigned due to Vinay's SCCM workload. Primarily configuration/activation tasks.

---

## Capacity & Assignments Heading into Sprint 2.3

| Team Member | Sprint 2.3 Focus |
|---|---|
| Vinay | SCCM domain/network attributes + timestamp alignment stories |
| Karen | NowAssist feature activation stories (4 stories) |
| Tony | Business app cleanup + credentials work (ongoing); begin business app migration |
| Laurent | Azure Airlift stories (prioritized by Alex); resolve dev admin access (meeting with Stan at 12pm June 8) |
| Alex Lim | Azure Airlift stories |
| Stan | SCCM customization approval packaging; admin access resolution for Laurent |

> **Laurent blocker:** No admin access in dev environment. Stan scheduled meeting at 12pm June 8 to resolve.

---

## Customization Governance Reminder

Any customization requiring new fields must receive **formal Sonica approval** before moving from dev to production. Stan will provide customization details to Alex to create the approval issue (RAID/Decision).

---

## Action Items

| Owner | Action | Due |
|---|---|---|
| Stan | Send customization details for new SCCM timestamp attributes to Alex for approval issue creation | ASAP |
| Stan | Close update set for new fields; package for deployment after Sonica approval | After approval |
| Stan | Attend 12pm admin access meeting with Laurent | June 8 |
| Alex | Coordinate separate call with Manuel, Vinay, and Joe to resolve SCCM attribute mapping (Spike 1403759) approvals | ASAP |
| Alex | Update ADO items with sprint planning details and comments | June 8–9 |
| Alex | Review team capacity and finalize task assignments for Sprint 2.3 | June 9–10 |
| Manuel | Coordinate with Anu on approval status of SCCM attribute mapping | ASAP |
| Manuel | Join follow-up call with Alex, Vinay, and Joe on Spike 1403759 | ASAP |
| Vinay | Proceed with stories 1403760 and 1403762 | Sprint 2.3 |
| Vinay | Join follow-up call for Spike 1403759 approval clarification | ASAP |
| Karen | Take ownership of NowAssist stories 1436576, 1436579, 1436593, 1436592; update ADO progress | Sprint 2.3 |
| Tony | Continue business app cleanup + credentials; begin app migration | Sprint 2.3 |
| Laurent | Resolve admin access via Stan meeting; coordinate with Tony | June 8 |
| Joe | Support follow-up on SCCM attribute mappings; sprint planning support | ASAP |

---

## Open Issues / Flags

- **Spike 1403759 (De-prioritize SCCM)** — approval status ambiguous; dedicated call needed before this can enter a sprint
- **Story 1403762 (Timestamp Alignment)** — technically ready but Sonica approval is a hard gate
- **Laurent admin access** — blocks Airlift work; must resolve June 8
- **NowAssist feature IDs** — stories created; feature-level ADO linkage still unconfirmed (Anu to verify on return)
