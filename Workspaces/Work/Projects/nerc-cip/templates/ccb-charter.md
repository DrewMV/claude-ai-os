---
title: Configuration Control Board Charter — Template
category: template
workspace: Work
project: nerc-cip
tags: [nerc-cip, cip-010, change-management, ccb, cab, governance, template]
created: 2026-06-03
updated: 2026-06-03
---

# Configuration Control Board Charter

| Field | Value |
|---|---|
| **Document Title** | Configuration Control Board Charter |
| **Document ID** | CCB-[ORG]-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Charter Owner** | [CIP Compliance Manager / CISO] |
| **Approved By** | [Executive Sponsor Name / Title] |
| **Effective Date** | [YYYY-MM-DD] |
| **Next Review Date** | [YYYY-MM-DD] (annual minimum) |

---

## Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | [Author] | Initial release |

---

## Table of Contents

1. Purpose and Authority
2. Scope
3. Membership and Quorum
4. Change Authorization Criteria
5. Change Request Review Process
6. Meeting Cadence and Minutes
7. Emergency Change Authorization
8. Post-Implementation Review
9. Escalation and Dispute Resolution
10. Relationship to the Configuration Management Plan
11. Document Control

---

## 1. Purpose and Authority

### 1.1 Purpose

The Configuration Control Board (CCB) — also referred to as the Change Advisory Board (CAB) — is the governance body responsible for reviewing, authorizing, and tracking changes to BES Cyber Systems operated by [Organization Name]. The CCB provides the organizational accountability required by NERC CIP standards and ensures that only authorized, documented changes are made to systems within the Electronic Security Perimeter (ESP).

> **NERC CIP — CIP-010 R1.2**: *"Authorize and document changes that deviate from the existing baseline configuration."* The CCB is the formal body through which this authorization is granted. Its existence, membership, and meeting minutes constitute the organizational evidence that a repeatable authorization process is in place.

### 1.2 Authority

The CCB is authorized to:
- Approve, reject, or defer change requests affecting in-scope BES Cyber Systems
- Grant standing (pre-approved) authorizations for defined low-risk change categories
- Authorize emergency changes outside the standard review cycle
- Direct remediation of unauthorized configuration changes detected during monitoring
- Recommend updates to the Configuration Management Plan (CMP)

The CCB does **not** have authority to override NERC CIP requirements, waive documentation obligations, or approve changes that would place the organization out of compliance with applicable standards.

### 1.3 Governing Documents

This charter operates in conjunction with:

- **Configuration Management Plan (CMP-[ORG]-001)** — defines what constitutes a baseline, documentation standards, and monitoring obligations
- **CIP-010-[version]** — NERC Reliability Standard for Configuration Change Management and Vulnerability Assessments
- **CIP-002-[version]** — defines which systems are in scope for CCB oversight
- **CIP-005-[version]** — Electronic Security Perimeter; ESP boundary changes require CCB review

---

## 2. Scope

> **NERC CIP — CIP-002**: CCB oversight applies to systems identified and categorized under CIP-002. High and Medium impact BES Cyber Systems and their associated EACMS, PACS, and PCA are subject to full CCB review. Low impact systems are not required but may be included at the organization's election.

### 2.1 In-Scope Systems

The CCB has authority over changes to all systems listed in the CMP (§1.2) and the CIP-002 asset inventory, including:

- **BES Cyber Systems** — High and Medium impact
- **EACMS** — Electronic Access Control or Monitoring Systems supporting in-scope BES Cyber Systems
- **PACS** — Physical Access Control Systems for facilities containing High and Medium impact BES Cyber Systems
- **PCA** — Protected Cyber Assets in the same Electronic Security Perimeter

### 2.2 What Constitutes a Change Requiring CCB Review

A change requiring CCB review is any modification that deviates from the established baseline configuration (as defined in CMP §3), including but not limited to:

- Operating system or firmware upgrades or downgrades
- Installation, removal, or version change of any software
- Addition, removal, or modification of logical network ports
- Application of or removal of security patches
- Changes to access control configurations affecting BES Cyber System access
- Network architecture changes that affect ESP boundaries
- Changes to authentication mechanisms (passwords, certificates, MFA)
- Physical relocation of BES Cyber Assets between security zones

---

## 3. Membership and Quorum

> **NERC CIP — CIP-010 R1.4**: *"Identify and verify the controls that could be impacted by the change."* The CCB's cross-functional composition ensures that OT, IT, and security perspectives are represented in the impact analysis before authorization is granted.

### 3.1 Standing Members

| Role | Name / Title | Domain | Voting |
|---|---|---|---|
| **CCB Chair** | [Name] | Compliance / Leadership | Yes |
| **OT Engineering Lead** | [Name] | Operational Technology | Yes |
| **IT/Cybersecurity Manager** | [Name] | Information Security | Yes |
| **Operations Representative** | [Name] | BES Operations / Reliability | Yes |
| **Compliance Analyst** | [Name] | NERC CIP Compliance | Advisory (non-voting) |
| **Executive Sponsor** | [Name] | Leadership | Escalation only |

### 3.2 Ad Hoc Members

The CCB Chair may invite subject-matter experts on a per-change basis (e.g., vendors, system administrators) when their expertise is needed to evaluate a specific change. Ad hoc members are non-voting.

### 3.3 Quorum Requirements

| Change Category | Minimum Members Present to Authorize |
|---|---|
| **High-Risk** | CCB Chair + OT Engineering + IT/Cybersecurity (3 voting members minimum) |
| **Medium-Risk** | Any 2 voting members |
| **Low-Risk / Pre-Approved** | Self-authorized; CCB notification only |
| **Emergency** | CCB Chair or designated alternate (single authority) |

If quorum cannot be met for a scheduled meeting, the meeting is rescheduled within **[X] business days** or decisions are deferred unless an emergency authorization is warranted.

### 3.4 Conflicts of Interest

A CCB member who submitted or directly benefits from a change request must recuse themselves from the authorization vote for that change. The recusal is documented in the meeting minutes.

---

## 4. Change Authorization Criteria

> **NERC CIP — CIP-010 R1.2**: Authorization must occur *before* the change is implemented (except emergency changes). The criteria below define what the CCB evaluates to determine whether a change is authorized.

### 4.1 Change Risk Categories

| Category | Definition | Examples |
|---|---|---|
| **High-Risk** | Affects ESP boundary; major version change; new persistent port; architectural change; access control redesign | OS upgrade, new firewall rule, SCADA platform migration |
| **Medium-Risk** | Incremental change within existing ESP; patch application; minor config change | Security patch, port disable, user account modification |
| **Low-Risk / Pre-Approved** | Change type previously reviewed and approved as a standing authorization by the CCB | Approved patch bundles, routine cert renewals per standing SOPs |
| **Emergency** | Immediate threat to BES reliability or active security incident requiring immediate action | Active exploit in production, hardware failure requiring replacement |

### 4.2 Authorization Criteria

The CCB evaluates each change request against the following criteria:

- [ ] **Completeness**: CR contains all required fields (per CMP §4.3)
- [ ] **Justification**: Business or security need is clearly stated and credible
- [ ] **Baseline impact**: Affected baseline components are accurately identified
- [ ] **Control impact**: CIP-005 and CIP-007 control impacts are identified and assessed (per CMP §6)
- [ ] **Implementation plan**: Step-by-step plan is feasible and complete
- [ ] **Rollback plan**: Rollback procedure is documented and executable within the implementation window
- [ ] **Testing**: Pre- and post-change verification approach is defined
- [ ] **Schedule**: Implementation window does not conflict with operational constraints (e.g., peak load periods, planned outages)
- [ ] **Risk acceptability**: Residual risk after implementation is acceptable

### 4.3 Authorization Outcomes

| Outcome | Meaning | Next Step |
|---|---|---|
| **Approved** | CR meets all criteria; authorized for implementation in the proposed window | Change proceeds to implementation |
| **Approved with Conditions** | CR authorized with specific conditions or modifications | Requester confirms conditions; change proceeds |
| **Deferred** | More information required; implementation window reassigned | Requester provides information; resubmits to CCB |
| **Rejected** | Change is not authorized; specific reasons documented | Requester may revise and resubmit |

---

## 5. Change Request Review Process

> **NERC CIP — CIP-010 R1.3**: The authorization and review process must be documented. These steps define how the CCB produces the documentation NERC auditors require.

### 5.1 Submission

1. Requester opens a Change Request (CR) in ServiceNow Change Management.
2. CR is assigned to the relevant System Owner for technical review.
3. System Owner validates baseline impact and control impact assessment sections.
4. Completed CR is submitted to the CCB queue at least **[X] business days** before the next CCB meeting (High-Risk) or **[Y] business days** (Medium-Risk).

### 5.2 Pre-Meeting Review

CCB members review submitted CRs **[48 hours]** before the scheduled meeting. Members prepare questions or concerns to raise during the meeting.

### 5.3 CCB Meeting Review

During the CCB meeting, each CR is:
1. **Introduced** by the Requester or System Owner (5–10 minutes)
2. **Reviewed** by CCB members against authorization criteria (Section 4.2)
3. **Discussed** — members raise technical, operational, or compliance concerns
4. **Voted** — members vote Approve / Approve with Conditions / Defer / Reject
5. **Recorded** — outcome and rationale documented in meeting minutes

### 5.4 Post-Approval Actions

Following CCB approval:
1. Requester schedules implementation within the approved window.
2. Change Implementer executes per the approved implementation plan.
3. Post-change verification is completed and attached to the CR (per CMP §7).
4. CMDB CI baseline attributes are updated.
5. CR is closed with all evidence attached.
6. CCB is notified of closure at the next meeting.

---

## 6. Meeting Cadence and Minutes

> **NERC CIP — CIP-010 evidence**: CCB meeting minutes are required audit evidence demonstrating that a formal authorization process exists. Minutes must capture enough detail to prove each change was reviewed and authorized before implementation.

### 6.1 Meeting Schedule

| Meeting Type | Frequency | Purpose |
|---|---|---|
| **Regular CCB** | [Weekly / Bi-weekly] | Review pending change requests; track open items |
| **Emergency CCB** | As needed | Authorize emergency changes; review post-emergency documentation |
| **Quarterly Review** | Quarterly | Review CCB effectiveness; review pre-approved change categories; review CMP alignment |

### 6.2 Meeting Minutes — Required Contents

Minutes for every CCB meeting must include:

- [ ] Date, time, and location (or video conference link)
- [ ] Attendees (name and role) and any members absent
- [ ] Quorum confirmation
- [ ] List of CRs reviewed, with CR number and system name
- [ ] For each CR: authorization outcome (Approved / Approved with Conditions / Deferred / Rejected)
- [ ] Rationale for each decision, including any dissenting views
- [ ] Any conditions attached to conditional approvals
- [ ] Action items with owner and due date
- [ ] Next meeting date

### 6.3 Minutes Distribution and Retention

- Draft minutes are circulated to CCB members within **[2 business days]** of the meeting.
- Members have **[3 business days]** to raise corrections.
- Final minutes are approved by the CCB Chair and filed in [Document Store].
- Minutes are classified as **BCSI** and retained for a minimum of **3 calendar years**.

> **NERC CIP — Evidence**: Retain meeting minutes as primary evidence that CIP-010 R1.2 authorization requirements were met. Auditors will request minutes to confirm that changes were reviewed before implementation.

---

## 7. Emergency Change Authorization

> **NERC CIP — CIP-010 R1.5**: Emergency changes must be authorized and documented, but the standard allows for after-the-fact completion of documentation when an immediate response is required. The key obligation: **all documentation must be complete within the organization's defined window** (this charter sets 7 calendar days).

### 7.1 What Qualifies as an Emergency

An emergency change is required when:
- An active exploit or attack is occurring or imminent against a BES Cyber System
- A hardware failure requires immediate replacement to restore BES reliability
- A regulatory authority (e.g., NERC, FERC) directs an immediate action
- An operational emergency requires configuration changes to prevent BES outage

Routine changes that missed the standard submission deadline are **not** emergencies.

### 7.2 Emergency Authorization Procedure

```
1. Change Implementer contacts CCB Chair (or designated alternate) immediately.
2. CCB Chair grants verbal or email authorization.
   - Email authorization is documented with timestamp and response.
   - Verbal authorization is followed by an email confirmation within 1 hour.
3. Change Implementer proceeds with the change, documenting steps taken in real-time.
4. Within 24 hours: Change Implementer opens a CR in ServiceNow marked "Emergency."
5. Within 7 calendar days: Full CR documentation is completed (all Section 4.3 fields).
6. Within 7 calendar days: Post-change verification completed and attached to CR.
7. At next scheduled CCB meeting: CCB reviews the emergency change; outcome recorded in minutes.
```

### 7.3 Designated Alternates for Emergency Authorization

| Primary | Alternate | Contact |
|---|---|---|
| CCB Chair: [Name] | [Alternate Name / Title] | [Phone / Email] |
| [Name] | [Alternate] | [Contact] |

---

## 8. Post-Implementation Review

> **NERC CIP — CIP-010 R1.3**: Post-change verification is a documentation requirement, not just a best practice. Evidence of verification must be retained.

### 8.1 Routine Post-Implementation

Following each approved change:
1. Change Implementer completes the Post-Change Verification Report (per CMP §7.2).
2. Report is attached to the CR in ServiceNow before the CR is closed.
3. System Owner confirms CMDB baseline attributes have been updated.

### 8.2 CCB Post-Implementation Notification

At the next regular CCB meeting following a change implementation:
- System Owner confirms the change was implemented as approved.
- Any deviations from the approved implementation plan are disclosed.
- If a deviation occurred, the CCB determines whether a new CR is required.

### 8.3 Failed Implementation

If a change cannot be implemented as approved or post-change verification fails:
1. Change Implementer notifies CCB Chair within **1 business day**.
2. Rollback is executed per the CR rollback plan, unless CCB Chair authorizes an alternative.
3. CCB reviews the failed change at the next scheduled or emergency meeting.
4. A new CR is opened for any remediation or revised approach.

---

## 9. Escalation and Dispute Resolution

### 9.1 Intra-CCB Disputes

When CCB members cannot reach consensus on a change authorization:
1. CCB Chair attempts to resolve through discussion and additional information.
2. If unresolved, the CCB Chair has casting vote authority for Medium and Low risk changes.
3. High-Risk disputes are escalated to the **Executive Sponsor** for resolution within **[X] business days**.

### 9.2 Escalation to Executive Sponsor

Escalation to the Executive Sponsor is required when:
- A High-Risk change cannot be authorized by the CCB
- A change is time-critical and quorum cannot be achieved
- The CCB discovers a potential NERC CIP compliance issue requiring leadership decision

The Executive Sponsor's decision is documented and attached to the relevant CR.

---

## 10. Relationship to the Configuration Management Plan

The CCB Charter and the Configuration Management Plan are **companion documents**. Neither is complete without the other.

| The CMP defines... | The CCB Charter defines... |
|---|---|
| What a baseline configuration is (§3) | Who authorizes deviations from it (§3–4) |
| Change documentation standards (§5) | Meeting minutes format and retention (§6) |
| Control impact assessment approach (§6) | Which CCB members perform the assessment (§3.1) |
| Emergency change documentation (§4.4) | Who grants emergency authorization (§7) |
| Evidence retention periods (§12) | Minutes and decision record retention (§6.3) |
| Post-change verification steps (§7) | How CCB is notified of outcomes (§8) |

> **NERC CIP**: The two documents together satisfy CIP-010 R1.1 through R1.5. The CMP is the procedural evidence; the CCB Charter is the governance evidence. Auditors will look for both.

---

## 11. Document Control

### 11.1 Review Cycle

This charter is reviewed and updated:
- At least **annually**
- When membership changes (new personnel in named roles)
- When the CMP scope changes (new systems added to CIP-002 inventory)
- When NERC revises CIP-010 requirements

### 11.2 Approval

Amendments to this charter require approval from the CCB Chair and Executive Sponsor.

### 11.3 Classification

This document is classified as **BCSI** under CIP-011 and is distributed only to CCB members and personnel with a demonstrated need.

---

## Appendix A: NERC CIP Requirement Traceability Matrix

| CIP Requirement | Charter Section | Description |
|---|---|---|
| CIP-002 (scope) | §2 | Systems subject to CCB oversight |
| CIP-005 R1 | §2.2, §4.1 | ESP boundary changes require CCB review |
| CIP-010 R1.1 | §1.3, §10 | Baseline definition in CMP; CCB authorizes deviations |
| CIP-010 R1.2 | §1, §4, §5 | CCB is the authorization body |
| CIP-010 R1.3 | §5, §6, §8 | Change records and minutes are the documentation |
| CIP-010 R1.4 | §3.1, §4.2 | Cross-functional composition enables control impact review |
| CIP-010 R1.5 | §7 | Emergency change authorization procedure |
| CIP-011 R1 | §6.3, §11.3 | Minutes are BCSI; access controlled; 3-year retention |

---

## Appendix B: CCB Decision Log Template

*To be completed in meeting minutes for each CR reviewed:*

| Field | Value |
|---|---|
| CR Number | [ServiceNow CR#] |
| System(s) Affected | [System name / CI] |
| Change Description | [Brief description] |
| Risk Category | High / Medium / Low / Emergency |
| Decision | Approved / Approved with Conditions / Deferred / Rejected |
| Conditions (if any) | [Specific conditions or modifications required] |
| Rationale | [Why this decision was made] |
| Dissenting Views | [Any member dissent and reasoning] |
| Voted By | [Names of members who voted] |

---

## Appendix C: Member Contact List

*Maintained by the Compliance Analyst. Updated whenever membership changes.*

| Role | Name | Phone | Email | Alternate |
|---|---|---|---|---|
| CCB Chair | [Name] | [Phone] | [Email] | [Alternate] |
| OT Engineering Lead | [Name] | [Phone] | [Email] | [Alternate] |
| IT/Cybersecurity Manager | [Name] | [Phone] | [Email] | [Alternate] |
| Operations Representative | [Name] | [Phone] | [Email] | [Alternate] |
| Compliance Analyst | [Name] | [Phone] | [Email] | [Alternate] |
| Executive Sponsor | [Name] | [Phone] | [Email] | — |
