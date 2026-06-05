---
title: Configuration Management Plan — Template
category: template
workspace: Work
project: nerc-cip
tags: [nerc-cip, cip-010, configuration-management, template, governance]
created: 2026-06-03
updated: 2026-06-03
---

# Configuration Management Plan

| Field | Value |
|---|---|
| **Document Title** | Configuration Management Plan |
| **Document ID** | CMP-[ORG]-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Owner** | [Name / Title] |
| **Approved By** | [Name / Title] |
| **Effective Date** | [YYYY-MM-DD] |
| **Next Review Date** | [YYYY-MM-DD] (annual minimum) |

---

## Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | [Author] | Initial release |

---

## Table of Contents

1. Purpose and Scope
2. Roles and Responsibilities
3. Baseline Configuration
4. Change Authorization Process
5. Change Documentation Standards
6. Control Impact Assessment
7. Post-Change Verification
8. Configuration Monitoring
9. Vulnerability Assessments
10. Transient Cyber Assets and Removable Media
11. BES Cyber System Information Protection
12. Evidence Retention
13. Document Control

---

## 1. Purpose and Scope

### 1.1 Purpose

This Configuration Management Plan (CMP) establishes the processes and controls governing configuration management for BES Cyber Systems operated by [Organization Name]. It defines how configuration baselines are established, how changes are authorized and documented, and how unauthorized modifications are detected.

> **NERC CIP — CIP-010 R1**: *"Each Responsible Entity shall implement, in a manner that identifies, assesses, and corrects deficiencies, one or more documented process(es) that collectively include each of the applicable requirement parts."* This CMP is the primary documented process satisfying CIP-010 R1.

### 1.2 Scope

This CMP applies to all BES Cyber Systems and their associated components as identified and categorized under CIP-002. Specifically:

**In-Scope Systems:**

| System Name | Impact Level | Location / ESP | Asset Owner |
|---|---|---|---|
| [System Name] | High / Medium / Low | [ESP Name] | [Owner] |
| [System Name] | High / Medium / Low | [ESP Name] | [Owner] |

**In-Scope Asset Categories:**
- BES Cyber Assets (BCA) — High and Medium impact
- Electronic Access Control or Monitoring Systems (EACMS)
- Physical Access Control Systems (PACS)
- Protected Cyber Assets (PCA)

> **NERC CIP — CIP-002**: The asset inventory above must be reviewed and updated at least every **15 months**. This CMP is scoped to match the current CIP-002 inventory. Any addition of new BES Cyber Systems triggers a scope update to this document.

**Out-of-Scope:** Low impact BES Cyber Systems are excluded from CIP-010 R1–R3 requirements unless the organization elects to apply them.

---

## 2. Roles and Responsibilities

> **NERC CIP — CIP-010 R1.2**: The authorization process must identify who is authorized to approve changes that deviate from the established baseline. This section establishes those roles.

| Role | Responsibilities | Name / Title |
|---|---|---|
| **CIP Compliance Manager** | Owns this document; ensures processes are current and followed; coordinates with auditors | [Name] |
| **OT Engineering Lead** | Maintains baseline configuration records for OT assets; reviews and approves OT change requests | [Name] |
| **IT/Cybersecurity Manager** | Assesses CIP-005/CIP-007 control impacts; reviews security patch changes | [Name] |
| **Configuration Control Board (CCB) Chair** | Chairs CCB meetings; holds final approval authority for High-risk changes | [Name] |
| **System Owners** | Responsible for maintaining accurate CI baseline records in CMDB; submit change requests | [Names] |
| **Change Implementer** | Executes authorized changes; documents implementation evidence | [Assigned per change] |
| **Compliance Evidence Custodian** | Retains and organizes CIP-010 evidence; coordinates evidence production for audits | [Name] |

---

## 3. Baseline Configuration

> **NERC CIP — CIP-010 R1.1**: *"Develop a baseline configuration, individually or by grouping, which shall include the following applicable items: (1) Operating system(s) including version; (2) Any commercially available or open-source application software installed; (3) Any custom software installed; (4) Any logical network accessible port; (5) Any security patches applied."*

### 3.1 Baseline Components

A baseline configuration must be maintained for each in-scope BES Cyber System and must include all of the following:

| Component | Description | Where Recorded |
|---|---|---|
| **Operating System / Firmware** | Name and version (or firmware version if no OS applies, e.g., protective relays) | CMDB CI attribute |
| **Commercial / Open-Source Software** | Name and version of all installed applications | CMDB CI attribute |
| **Custom Software** | Name, version, and purpose of any internally developed software | CMDB CI attribute |
| **Logical Network Accessible Ports** | Port number, protocol (TCP/UDP), and business justification for each enabled port | CMDB CI attribute |
| **Security Patches Applied** | Patch identifier, application date, and source | CMDB CI attribute |

### 3.2 Baseline Establishment

1. An initial baseline is established at the time of commissioning or at this CMP's effective date, whichever comes first.
2. Baselines are recorded in the CMDB as CI attributes on the relevant Configuration Item.
3. The CCB reviews and formally approves the initial baseline before the system enters production.
4. Each baseline record includes the date established and the name of the approving authority.

### 3.3 System of Record

The ServiceNow CMDB is the authoritative system of record for all baseline configurations. CMDB CI records for in-scope BES Cyber Assets must include all five baseline component types listed in Section 3.1. Baselines stored outside the CMDB (e.g., in engineering documentation) must be synchronized with the CMDB within **5 business days** of any change.

---

## 4. Change Authorization Process

> **NERC CIP — CIP-010 R1.2**: *"Authorize and document changes that deviate from the existing baseline configuration."* No change to a BES Cyber System baseline may be implemented without prior written authorization from the CCB (or designated authority per risk category).

### 4.1 Change Risk Categories

| Category | Definition | Authorization Required |
|---|---|---|
| **High-Risk** | Affects ESP boundary; OS upgrade; major software version change; new logical port; architectural change | Full CCB review and vote |
| **Medium-Risk** | Security patch application; minor software update; configuration parameter change within existing ESP | Abbreviated CCB review (2+ members) |
| **Low-Risk / Pre-Approved** | Change type previously approved by CCB as a standing authorization (must be documented) | Change implementer self-authorizes; CCB notification within 3 business days |
| **Emergency** | Immediate threat to BES reliability or security requires change outside normal cycle | Verbal/email from CCB Chair or designee; full documentation within **7 calendar days** |

### 4.2 Standard Change Request Process

```
1. Requester submits Change Request (CR) in CMDB/ServiceNow Change Management
2. System Owner reviews for completeness and accuracy
3. CCB receives CR for review (see CCB Charter)
4. CCB approves, rejects, or defers with documented rationale
5. Approved CR is assigned an implementation window
6. Change Implementer executes change per the approved implementation plan
7. Post-change verification performed (see Section 7)
8. CMDB baseline updated to reflect new authorized configuration
9. CR closed with implementation evidence attached
```

### 4.3 Change Request Required Fields

Each CR submitted to the CCB must include:

- [ ] Description of the proposed change
- [ ] Affected BES Cyber Systems and CIs (CMDB record numbers)
- [ ] Business or security justification
- [ ] Risk category (High / Medium / Low / Emergency)
- [ ] Implementation plan (step-by-step)
- [ ] Rollback / contingency plan
- [ ] Proposed implementation window
- [ ] Pre-implementation verification steps
- [ ] Post-implementation verification steps
- [ ] CIP-005/CIP-007 control impact analysis (see Section 6)

### 4.4 Emergency Change Process

> **NERC CIP — CIP-010 R1.5**: Emergency changes must still be documented. Verbal or email authorization is acceptable in an emergency, but the full change record must be completed within **7 calendar days** of implementation.

1. Change Implementer contacts CCB Chair (or designee) immediately.
2. Verbal or email authorization is obtained and recorded.
3. Change is implemented.
4. Full CR documentation is completed within 7 calendar days.
5. CCB reviews emergency change at the next scheduled meeting.

---

## 5. Change Documentation Standards

> **NERC CIP — CIP-010 R1.3**: Entities must document changes including: the baseline components affected, the authorization, the implementation, and verification. Evidence must be retained for **3 calendar years**.

### 5.1 Required Change Records

For every approved change to a BES Cyber System baseline, the following records must exist:

| Record | Description | Retained In |
|---|---|---|
| **Change Request** | Submitted CR with all required fields (Section 4.3) | ServiceNow Change Management |
| **CCB Approval** | Meeting minutes or email approval with approver identity | ServiceNow / Document store |
| **Implementation Evidence** | Work log, system logs, or screenshots confirming the change was made as authorized | ServiceNow CR attachment |
| **Post-Change Verification Report** | Results of control verification (Section 7) | ServiceNow CR attachment |
| **Updated CMDB Record** | Screenshot or export of CI record showing updated baseline attributes | ServiceNow / exported evidence |

### 5.2 Record Completeness Check

The Compliance Evidence Custodian performs a completeness check on all CRs within **5 business days** of closure to confirm all required records are present and legible.

---

## 6. Control Impact Assessment

> **NERC CIP — CIP-010 R1.4**: *"For a change that deviates from the existing baseline configuration, prior to the change, identify and verify the controls that could be impacted by the change."* Only controls **actually relevant** to the change type need to be assessed.

### 6.1 Control Impact Matrix

| Change Type | CIP-005 Controls to Verify | CIP-007 Controls to Verify |
|---|---|---|
| New or changed logical port | CIP-005 R1 (ESP boundary ports) | CIP-007 R1 (Ports and Services) |
| OS or firmware upgrade | CIP-005 R2 (remote access) | CIP-007 R2 (Patch Management), R4 (Logging) |
| Software install / removal | — | CIP-007 R1 (ports), R2 (patches) |
| Security patch | — | CIP-007 R2 (Patch Management) |
| Access control configuration | CIP-005 R1–R2 | CIP-007 R5 (Account Management) |
| Network architecture change | CIP-005 R1–R3 (full ESP review) | CIP-007 R1 |

### 6.2 Assessment Process

1. Change Requester completes control impact section of the CR (using matrix above as guidance).
2. IT/Cybersecurity Manager reviews and confirms or expands the impact assessment.
3. Assessment results are documented on the CR before CCB review.
4. Post-change verification confirms affected controls still meet requirements (Section 7).

---

## 7. Post-Change Verification

> **NERC CIP — CIP-010 R1.3**: Changes must be verified after implementation. Verification confirms the change was implemented as documented and that affected controls remain functional.

### 7.1 Verification Steps

1. Change Implementer confirms implementation matches the approved implementation plan.
2. Affected controls identified in the impact assessment (Section 6) are tested or reviewed.
3. CMDB CI baseline attributes are updated to reflect the new authorized configuration.
4. A Post-Change Verification Report is completed and attached to the CR.
5. System Owner signs off on verification completion.

### 7.2 Verification Report Contents

- Date and time of verification
- Name of verifier
- Each affected control verified (CIP-005 / CIP-007 reference)
- Verification method (test, review, screenshot, log excerpt)
- Pass / Fail result for each control
- Any issues identified and remediation actions

### 7.3 Failed Verification

If post-change verification fails:
1. Change is escalated to the CCB Chair within **1 business day**.
2. Rollback is executed unless the CCB Chair determines a remediation path is acceptable.
3. A new CR is opened for the remediation action.

---

## 8. Configuration Monitoring

> **NERC CIP — CIP-010 R2**: *"Monitor at least every 35 calendar days for changes to the baseline configuration (as described in Requirement R1, Part 1.1) of in-scope Cyber Assets."* Unauthorized changes must be investigated.

### 8.1 Monitoring Method

[Select one or both methods used by the organization:]

**Option A — Automated Drift Detection**
- Tool: [e.g., Tripwire, Industrial Defender, Forescout]
- Frequency: Continuous / Daily / Weekly scan of BES Cyber System configurations
- Alerts route to: [Team / Queue]
- Unauthorized change alert SLA: Investigated within **[X] business days**

**Option B — Scheduled Manual Review**
- Reviewer: [Role / Name]
- Frequency: Every **35 calendar days** (maximum)
- Process: Compare current CI attributes in CMDB against last approved baseline snapshot
- Results documented in: [Location / ServiceNow record]

### 8.2 Unauthorized Change Response

If a configuration deviation is detected that does not correspond to an approved CR:

1. Alert or finding is logged in ServiceNow as a Security Incident.
2. OT Engineering and IT/Cybersecurity are notified within **[X] hours**.
3. Root cause analysis is initiated.
4. If change is determined unauthorized, it is remediated (reverted or authorized via emergency CR).
5. Incident record documents the detection, investigation, and resolution.
6. Finding is reviewed by the CCB at the next scheduled meeting.

### 8.3 Monitoring Evidence

For each 35-day monitoring cycle, the following evidence is retained:
- Date monitoring was performed
- Method used (automated alert log or manual review record)
- Systems reviewed
- Any deviations identified and their disposition
- Name of reviewer / system

---

## 9. Vulnerability Assessments

> **NERC CIP — CIP-010 R3**: Periodic vulnerability assessments are required for High and Medium impact BES Cyber Systems. High impact systems require at least one assessment every **15 calendar months**. Medium impact systems require at least one every **36 calendar months**.

### 9.1 Assessment Schedule

| System | Impact Level | Assessment Frequency | Next Assessment Due |
|---|---|---|---|
| [System Name] | High | 15 months | [Date] |
| [System Name] | Medium | 36 months | [Date] |

### 9.2 Assessment Process

1. Scope is defined to include all in-scope BES Cyber Assets and their EACMS/PCA.
2. Assessment methodology: [e.g., NERC-endorsed method, vendor tool, qualified assessor]
3. Results documented in a Vulnerability Assessment Report.
4. Identified vulnerabilities are tracked in ServiceNow with:
   - Vulnerability description and CVE (if applicable)
   - Risk rating
   - Remediation plan and owner
   - Target remediation date

### 9.3 Remediation Tracking

All identified vulnerabilities are remediated or have a documented acceptance/mitigation plan within **[X] days** of discovery. The CIP Compliance Manager reviews open vulnerabilities at each CCB meeting.

---

## 10. Transient Cyber Assets and Removable Media

> **NERC CIP — CIP-010 R4**: Plans must exist for transient cyber assets and removable media used with BES Cyber Systems. This applies to both entity-managed and third-party-managed transient assets.

### 10.1 Entity-Managed Transient Cyber Assets

- **Authorization**: Only authorized personnel may connect transient cyber assets to BES Cyber Systems. A list of authorized users, authorized locations, and permitted use cases is maintained by [Owner / Role].
- **Software Vulnerability Mitigation**: Before connection, transient assets must have current patches applied or an approved compensating control documented.
- **Malicious Code Prevention**: Transient assets must have active, updated endpoint protection. Results of a scan within **[X] days** of connection must be documented.
- **Unauthorized Use Controls**: Transient assets must not be connected to non-BES systems (e.g., corporate network) without documented review of associated risks.

### 10.2 Third-Party-Managed Transient Cyber Assets

Before a third-party transient asset is connected to a BES Cyber System:
1. Review the third party's patching and malicious code mitigation processes.
2. Document the review outcome and any additional mitigations required.
3. Obtain sign-off from the OT Engineering Lead.

### 10.3 Removable Media

- Only organizationally authorized removable media may be used with BES Cyber Systems.
- All removable media must be scanned for malicious code before use. Scan results are retained.
- A log is maintained of all removable media use (who, when, which system, purpose).

---

## 11. BES Cyber System Information Protection

> **NERC CIP — CIP-011 R1**: Configuration records that could enable unauthorized access to BES Cyber Systems constitute **BES Cyber System Information (BCSI)** and must be protected under the organization's information protection program.

### 11.1 CMDB Data as BCSI

The following CMDB record types are classified as BCSI:
- Logical port and protocol configurations for BES Cyber Systems
- Network topology records showing ESP boundaries and connectivity
- Combined records showing asset function, location, and access paths
- Baseline configuration records with software version and patch details

### 11.2 Access Controls

- CMDB CI records for in-scope BES Cyber Systems are restricted to personnel with a demonstrated business need.
- Role-based access control in ServiceNow enforces this restriction.
- All exports of BES Cyber System CI data to external formats (Excel, PDF) are logged.

### 11.3 Disposal

When a BES Cyber System is decommissioned:
1. CMDB record is updated to reflect decommissioned status.
2. Electronic records containing BCSI are sanitized per the organization's information disposal procedures.
3. A record of sanitization actions is retained.

---

## 12. Evidence Retention

> **NERC CIP — CIP-010 / CIP-011**: Evidence supporting compliance with CIP-010 R1–R4 and CIP-011 R1 must be retained for a minimum of **3 calendar years**.

| Evidence Type | Retention Period | Storage Location | Access Control |
|---|---|---|---|
| Change request records | 3 years | ServiceNow | BCSI-restricted |
| CCB meeting minutes | 3 years | [Document store] | BCSI-restricted |
| Baseline configuration records | 3 years from decommission | CMDB + archive | BCSI-restricted |
| Configuration monitoring records | 3 years | ServiceNow / [store] | BCSI-restricted |
| Vulnerability assessment reports | 3 years | [Document store] | BCSI-restricted |
| Post-change verification reports | 3 years | ServiceNow | BCSI-restricted |
| Transient asset / removable media logs | 3 years | [Document store] | BCSI-restricted |

Evidence is organized and retrievable by CIP standard and requirement part to support audit production within **[X business days]** of an audit request.

---

## 13. Document Control

### 13.1 Review Cycle

This CMP is reviewed and updated:
- At least **annually**
- When the CIP-002 in-scope system inventory changes
- When NERC revises CIP-010 or CIP-011 requirements
- Following a NERC audit finding related to configuration management

### 13.2 Approval

Changes to this document require approval from the CIP Compliance Manager and, for significant scope or process changes, the CCB Chair.

### 13.3 Distribution

This document is classified as BCSI and is distributed only to personnel with a demonstrated need under Section 11.2 access controls.

---

## Appendix A: NERC CIP Requirement Traceability Matrix

| CIP Requirement | CMP Section | Description |
|---|---|---|
| CIP-002 (scope) | §1.2 | In-scope system inventory; 15-month review |
| CIP-010 R1.1 | §3 | Baseline configuration components |
| CIP-010 R1.2 | §4 | Change authorization process |
| CIP-010 R1.3 | §5 | Change documentation standards |
| CIP-010 R1.4 | §6 | Control impact assessment |
| CIP-010 R1.5 | §4.4 | Emergency change process |
| CIP-010 R2 | §8 | Configuration monitoring (35-day) |
| CIP-010 R3 | §9 | Vulnerability assessments |
| CIP-010 R4 | §10 | Transient cyber assets and removable media |
| CIP-011 R1 | §11 | BCSI identification and protection |
| Evidence retention | §12 | 3-year retention requirement |

---

## Appendix B: Related Documents

- Configuration Control Board Charter (CCB-[ORG]-001)
- CIP-002 Asset Inventory
- CIP-005 Electronic Security Perimeter documentation
- CIP-007 System Security Management procedures
- CIP-011 Information Protection Program
- ServiceNow CMDB CI baseline fields reference
