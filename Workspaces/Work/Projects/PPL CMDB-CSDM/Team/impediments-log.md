---
type: team-artifact
workspace: Work
project: CMDB-CSDM
updated: 2026-06-03
tags: [work, cmdb-csdm, team, impediments]
---

# Impediments Log

Running log of impediments raised by the CMDB-CSDM team. SM (Manuel Vazquez, effective 2026-06-09) owns resolution tracking. Escalated items go to RTE (Nolan LeBlanc) via Scrum of Scrums. See [[PI-2/Memory]] for PI-level risks and [[Dependencies/servicenow-enhancements]] for cross-team blockers.

| # | Raised | Iteration | Description | Owner | Status | Resolved |
|---|--------|-----------|-------------|-------|--------|---------|
| 1 | 2026-05-13 | 2.1 | **Post-Clone Data Integrity** — Major Incident templates confirmed missing after Prod-to-Dev clone. Full validation of CMDB objects, templates, and relationships not yet confirmed complete. | TBD | Open | |
| 2 | 2026-05-13 | 2.1 | **Credential Readiness (Discovery-Critical)** — SNMP credentials not confirmed fully working. CyberArk integration not confirmed complete. Credential propagation across environments (servers, DBs, network devices) pending. Blocking discovery accuracy and CMDB integrity. | TBD | Open | |
| 3 | 2026-05-13 | 2.1 | **Discovery Strategy (DEV/QA vs PROD)** — Debate on scanning PROD from lower environments noted in standups. No approved, documented approach exists. Risk of inconsistent or non-compliant discovery approach. | TBD | Open | |
| 4 | 2026-05-13 | 2.1 | **Service Mapping Blocked** — Missing credentials and environment access restrictions preventing Service Mapping progress. Directly impacts PI Objective 3 (Expand Service Mapping Foundation). | TBD | Open | |
| 5 | 2026-05-13 | 2.1 | **Data Certification Readiness** — Dashboard and pilot in progress but data inputs, pilot scope, and reporting alignment to business outcomes not yet finalized. | TBD | In Progress | |
| 6 | 2026-05-13 | 2.1 | **Story Dependency Execution** — Tasks are dependency-sequenced. Risk that predecessor stories are incomplete, blocking downstream work. Critical path not explicitly tracked. | Alex Phan | In Progress | |
| 7 | 2026-05-13 | 2.1 | **External Dependency Bottlenecks** — Delivery reliant on Network team (intake, credentials), Ops team (support, escalation), and contractor onboarding. Responsiveness of external teams creating delivery risk. | TBD | Open | |
| 8 | 2026-05-28 | 2.2 | **Reverse DNS Not Functioning for Discovery** — Raised at PO Sync (2026-05-28). Reverse DNS failure blocking CMDB discovery accuracy, Airlift migration planning, and ServiceNow visibility. Core data foundation risk. | TBD | Open | |
| 9 | 2026-05-28 | 2.2 | **AVD + Windows 11 Unplanned Work Consuming ART Capacity** — Raised at PO Sync (2026-05-28). Unplanned production work pulling shared service teams away from PI commitments. Displacing planned delivery across the ART. | Nolan LeBlanc (RTE) | Open | |
| 10 | 2026-06-03 | 2.2 | **ServiceNow Credential Access Blocked** — Laurent, Alex Lim, and Manuel (onboarding) lack full ServiceNow access. Tony's team working on fix; expected resolution by 2026-06-06. Christian coordinating comms to stakeholders. | Tony / Christian | In Progress | |
| 11 | 2026-06-03 | 2.2 | **OPS Team Unavailable for Remainder of PI-2** — OPS team fully engaged with upgrade activities (sandbox → test → prod → hyper care) and unavailable for backlog stories after this iteration. Karen and JP analyzing impact on PI-2 story assignments. Narayan (OPS) to provide written confirmation of availability and upgrade breakdown. Risk escalation to Todd and Nolan pending impact analysis. | Karen / JP | Open | |
| 13 | 2026-06-03 | 2.2 | **Sandbox/Dev Upgrade Delay Pushing Story Work to July** — Upgrade analysis blocked pending sandbox and dev instance upgrades, not expected until July. Stories dependent on these environments cannot proceed. Justification for shifting focus to Now Assist stories in next sprint. | TBD | Open | |
| 12 | 2026-06-03 | 2.2 | **CMDB Field Customization Validation Needed** — Customization request for "metal tier" field flagged for potential duplication (field already exists on CIs). Also: need to clarify whether "data classification" and "SOX indicator" are both necessary or redundant. Alex assigned to validate by 2026-06-04. | Alex Phan | Open | |

## Escalated to ART

Impediments escalated to RTE (Nolan LeBlanc) via Scrum of Scrums:

| # | Date | Description | Escalated By | Resolution |
|---|------|-------------|-------------|-----------|
| | | | | |
