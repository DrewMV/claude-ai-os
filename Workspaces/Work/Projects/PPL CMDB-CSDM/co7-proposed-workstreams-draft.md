---
type: contract-tracker
workspace: Work
project: PPL CMDB-CSDM
contract: CO7 (Change Order #7) — DRAFT PROPOSAL, not yet reviewed with Jordan
updated: 2026-09-13
tags: [work, cmdb-csdm, contract, deliverables, co7, draft]
---

# CO7 Proposed Workstreams — Draft for Jordan

> 🟡 **Status: DRAFT — Manuel's proposal, not yet validated with Jordan Yung.** Compiled from open items already tracked across the vault (not from a Jordan-supplied list — none exists yet). Scope is **new/incremental work only**; continuation/BAU items already covered by CO6 (Platform Support, ITSM PM, ongoing certification upkeep) are deliberately excluded per Manuel's direction.
>
> **Format mirrors [[Contract/AP00105-6 to ServiceNow Release 2 and 3 Deployment v3|CO6 v3]]:** Workstream → Description (capability + why it matters) → AC# → Acceptance Criteria → Due Date. No legal/Article language — this is planning input for Jordan/Christian, not contract text.
>
> **Due dates are placeholders** ("TBD — CO7 term") pending actual CO7 term negotiation, except where a workstream is anchored to an external fixed date already on record (SailPoint release waves) — those are referenced as constraints, not committed internal delivery dates.

---

## 1. SailPoint / IAM CMDB Readiness

**Description:** Establishes accurate, governed CMDB ownership, support-group, and approver data for the ~70 applications SailPoint IdentityIQ is onboarding across four release waves, plus CMDB support for Non-Person Account (NPA) governance use cases if confirmed in scope.

**Why it matters:** SailPoint's certification and access-approval routing depend on accurate application ownership data in CMDB. 64 of the 70 applications are SOX-scoped — without this work, IAM cannot certify SOX-scoped access on schedule, and this is already flagged as **unfunded and unscoped** in CO6 (due 2026-10-30, while all three major waves land in 2027).

| AC # | Acceptance Criteria | Due Date |
|---|---|---|
| 1.1 | CMDB–SailPoint data contract confirmed with Jordan Yung: required attributes per application, target CMDB class (Business Application vs. Service Instance), and lead time needed ahead of each release wave | TBD — CO7 term |
| 1.2 | Application-to-CI crosswalk built for all 70 applications (App Code → CMDB CI sys_id), per-OpCo duplicates dispositioned, gap list produced (no record / no owner / ambiguous identity) | TBD — CO7 term |
| 1.3 | CMDB records for Wave 2 (26 apps) fully populated with confirmed ownership/support-group data, validated ahead of the **2027-02-01** release | Ahead of 2027-02-01 |
| 1.4 | CMDB records for Wave 3 (20 apps) fully populated, validated ahead of the **2027-02-22** release | Ahead of 2027-02-22 |
| 1.5 | CMDB records for Wave 4 (19 apps) fully populated, validated ahead of the **2027-03-15** release | Ahead of 2027-03-15 |
| 1.6 | NPA (Non-Person Account) CMDB governance scope defined and implemented, if confirmed as a CMDB deliverable | TBD — pending scope confirmation |

*Assumes: the Business Application enhancement pause is either reconciled as an exception for this work, or the Application Services migration completion date is accepted as a hard predecessor.*

---

## 2. Data Certification & Compliance Carryover (CO5 Holdback Closure)

**Description:** Closes the CO5-era items that CO6 v3 did not carry forward as explicit deliverables: CI-class data dictionary, ESS-02 minimum-field alignment, SOX Business Application (BA) review, and 90%+ coverage for Computers and Servers.

**Why it matters:** These items remain tied to the **CO5 $533,775 fee holdback** and to Corporate Audit Services' active "CMDB Governance and Lifecycle Advisory Review" engagement (fieldwork through 2026-09-11, reporting week of 2026-10-20). Without an explicit contractual home, there is no agreed path to close either the holdback or the audit exposure.

| AC # | Acceptance Criteria | Due Date |
|---|---|---|
| 2.1 | Data dictionary defining minimum required/recommended attributes per CI class (Computers, Servers, Databases, Network Devices) published and CCB-ratified | TBD — CO7 term |
| 2.2 | ESS-02 Section 5 alignment: CI Owner, Technical Owner Group/Support Group, and Location promoted from Recommended to Required; firmware/OS-version field added for network gear; three-way sign-off obtained (Network Core, Cybersecurity/ESS-02, Corporate Audit Services) | TBD — CO7 term |
| 2.3 | SOX Business Application review process defined and executed for in-scope BA records | TBD — CO7 term |
| 2.4 | 90%+ CMDB coverage validated for Computers and Servers against authoritative business-owner inventories | TBD — CO7 term |
| 2.5 | Enhanced database discovery (MS-SQL, Oracle) configured, tested, and live in production | TBD — CO7 term |

⚠️ **Needs Christian/Joe involvement before this goes near contract language** — this workstream is a direct extension of the open CO5-acceptance risk, not a clean net-new ask.

---

## 3. Disaster Recovery Field Population (Service Instance)

**Description:** Populates the Service Instance table with the full set of business applications/services so the existing Criticality, RTO, and RPO fields can actually be used.

**Why it matters:** Hundreds of applications are currently missing from Service Instance — the fields exist but are unusable for those apps. This is an active, leadership-visible escalation (Charlie Getz / Dan Miller) tied to disaster-recovery readiness, currently unanswered.

| AC # | Acceptance Criteria | Due Date |
|---|---|---|
| 3.1 | Gap list produced: applications/services expected in Service Instance vs. currently present | TBD — CO7 term |
| 3.2 | Missing applications/services created in Service Instance with Criticality, RTO, and RPO populated, validated by business/service owners | TBD — CO7 term |
| 3.3 | Ongoing intake process defined so newly onboarded applications are added to Service Instance without manual backfill | TBD — CO7 term |

---

## 4. NITSR Early CI Creation & System Criticality Integration

**Description:** Moves CMDB CI creation and the System Criticality Assessment (SCA) earlier in the NITSR (New IT System Request) process — ahead of Technology Approval Review — with a defined lifecycle/status model for applications still under evaluation.

**Why it matters:** Cyber Governance is migrating criticality assessments from OneTrust to ServiceNow IRM (~Sept 2026). IRM cannot auto-identify applications needing assessment without a CI record already existing — without earlier CI creation, the IRM migration cannot achieve its intended automation.

| AC # | Acceptance Criteria | Due Date |
|---|---|---|
| 4.1 | Lifecycle/status model for "under evaluation" applications defined and approved (e.g., ServiceNow OOTB lifecycle stages) | TBD — CO7 term |
| 4.2 | CI class/table determination confirmed for NITSR-driven CI creation, reconciled with the CSDM 5.0 Business Application → Service Instance model | TBD — CO7 term |
| 4.3 | Updated NITSR process (CI creation moved ahead of Technology Approval Review) implemented and communicated to Cyber Governance and NITSR requesters | TBD — CO7 term |
| 4.4 | Handling defined and implemented for applications that do not receive NITSR approval (inactive/deletion/lifecycle disposition) | TBD — CO7 term |

*Note: the CI-class question in AC 4.2 is the same open question blocking SailPoint AC 1.1 (SP-4) — resolve once, reuse both places.*

---

## 5. CI Ownership Governance Alignment (CSDM 5.0)

**Description:** Resolves the conflict between PPL's current field labeling (`managed_by` displayed as "CI Owner") and CSDM 5.0's `owned_by`/`managed_by` accountability split, and formally ratifies the correct definition and field mapping through CCB.

**Why it matters:** The current labeling risks the anti-pattern CSDM 5.0 is designed to prevent — operational owners populate `managed_by` while `owned_by`, the field meant to carry accountability, goes unpopulated — undermining data quality for governance, incident response, and audit reporting.

| AC # | Acceptance Criteria | Due Date |
|---|---|---|
| 5.1 | Platform-wide confirmation of current `managed_by`/`owned_by` field labeling across all in-scope CI classes (confirmed today only on `cmdb_ci_business_app`) | TBD — CO7 term |
| 5.2 | CCB decision issued: relabel `managed_by`, or formally redefine "CI Owner" and reconcile with `owned_by` | TBD — CO7 term |
| 5.3 | Approved labeling/definition implemented across affected forms; CMDB Ownership and Routing Glossary updated to match | TBD — CO7 term |

---

## 6. CI Lifecycle Auto-Retirement

**Description:** Defines and implements an automated CI retirement process — triggered by discovery-confirmed decommission signals — replacing manual, ad hoc retirement handling.

**Why it matters:** Without automated retirement, stale/decommissioned CIs accumulate in the CMDB, degrading data accuracy and inflating coverage metrics with records that no longer reflect production reality. Already raised as an open concern in the CMDB Go Green weekly review.

| AC # | Acceptance Criteria | Due Date |
|---|---|---|
| 6.1 | Auto-retirement rules defined per CI class (decommission signal source, grace period, approval requirement) | TBD — CO7 term |
| 6.2 | Auto-retirement technical build released to production with audit logging | TBD — CO7 term |
| 6.3 | Dashboard/report available showing retirement activity and exceptions requiring manual review | TBD — CO7 term |

---

## Candidates considered and excluded

- **SCCM/CMDB integration sync reliability** — treated as a resolved/point-in-time operational incident (2026-09-04), not a recurring pattern with enough evidence yet to justify a contract workstream. Revisit if it recurs.
- **CO6 continuation items** (Platform Support, ITSM PM, ongoing per-class certification upkeep) — excluded per Manuel's direction to keep this draft to new scope only.

## Open questions before this goes to Jordan

1. Does Jordan already have SailPoint-specific commitments in flight that should supersede Workstream 1 here (see [[Dependencies/sailpoint-iam]] SP-5 through SP-8)?
2. Is Workstream 2 (CO5 holdback carryover) something Jordan wants folded into CO7, or should it be negotiated separately given its tie to the existing holdback?
3. What is the actual proposed CO7 term (start/end)? All due dates here are placeholders until that's set.
4. Should Workstreams 4 and 5 (NITSR, CI ownership governance) be CO7 deliverables at all, or are they better handled as no-cost governance/CCB decisions outside a change order?
