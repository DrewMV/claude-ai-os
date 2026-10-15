---
type: contract-tracker
workspace: Work
project: PPL CMDB-CSDM
contract: CO7 (Change Order #7) — DRAFT PROPOSAL, not yet reviewed with Jordan
updated: 2026-09-13
tags: [work, cmdb-csdm, contract, deliverables, co7, draft, governance, federated]
---

# CO7 Proposed Workstreams — Governance Automation (Draft for Jordan)

> 🟡 **Status: DRAFT — Manuel's proposal, not yet validated with Jordan Yung.** This is a **separate, brand-new proposal** — no carryover from CO5/CO6 legacy gaps, holdback items, or other open backlog threads (see [[co7-proposed-workstreams-draft]] for that separate, excluded set).
>
> **Format mirrors [[Contract/AP00105-6 to ServiceNow Release 2 and 3 Deployment v3|CO6 v3]]:** Workstream → Description (capability + why it matters) → AC# → Acceptance Criteria → Due Date. No legal/Article language.
>
> **Operating model (per Manuel, 2026-09-13):** Four tiers. **(1) CMDB [delivery] team** builds the central framework — rules, tooling, and the platform access model (Workstream 0). **(2) Configuration Management team (Ops)** runs that framework day-to-day: monitors CMDB health, produces reports, and routes issues to the right resolver team. **(3) Technical Owner Groups** remediate and dispose issues on **non-discoverable attributes** within their own in-scope class/subclass, using the access Workstream 0 configures. **(4) Discovery team** resolves issues on **discoverable attributes** (missing, stale, or incorrect values caused by a discovery gap — credentials, schedule, pattern) when Ops flags them. Workstreams 1 and 2 operate through all four tiers.
>
> **Class scope, with subclass detail:** "All classes covered in CO5 and CO6" is read as the **union** of classes with an existing data-certification baseline: **Business Application** (certified under CO5) + **Computers, Server, Database, Network Gear** (certified under CO6 v3, deliverable #4) — broken down to the subclass level below.
>
> | Class | Subclasses in scope |
> |---|---|
> | Business Application | — (class-level) |
> | Computers | — (class-level) |
> | Server | Windows Server, Linux Server |
> | Database | Oracle Instance, MS SQL Instance |
> | Network Gear | Routers, Switches, Firewalls, Load Balancers, Wireless Access Points (WAP), Network Controllers |
>
> Server/Database/Network Gear subclasses per the device/instance types named in CO6 v3's Network Gear Discovery deliverable and standard CMDB CI class hierarchy. Flag if Computers or Business Application should also be broken down (e.g., Desktop vs. Laptop).
>
> **Due dates are placeholders** ("TBD — CO7 term") pending actual CO7 term negotiation.

---

## 0. Federated Access Configuration (Foundational)

**Description:** Configures the ServiceNow platform so that, for each in-scope class/subclass, the assigned Technical Owner Group has write access to only the **non-discoverable attributes** on its own CI records — fields discovery cannot populate and that require manual/business input. **Discoverable attributes remain read-only to Technical Owner Groups and stay system/discovery-managed** — issues on those fields are a Discovery team problem, not a Technical Owner Group edit. This workstream also stands up the Configuration Management (Ops) team's operating responsibilities — monitoring, reporting, and routing escalations to whichever resolver team (Technical Owner Group or Discovery) an issue belongs to.

**Why it matters:** Today there is no confirmed, class/subclass-scoped access model letting the group closest to an asset maintain the fields only they can accurately supply, no defined operational function to monitor federated activity, and no clear split between "fix the data manually" (Technical Owner Group) versus "fix the discovery source" (Discovery team) when a field is wrong. Without all three, remediation either has no clear owner, or the wrong team gets the ticket — a Technical Owner Group cannot fix a discoverable field it doesn't control, and Discovery shouldn't be asked to fix a business-context field it was never meant to populate. This workstream is the platform-configuration **and** operating-model prerequisite Workstreams 1 and 2 depend on.

**Unit of organization: the roster below is the backbone of this workstream and of Workstreams 1 and 2.** Every AC is executed once per row.

| # | Class | Subclass | Technical Owner Group |
|---|---|---|---|
| 1 | Business Application | — (class-level) | TBD |
| 2 | Computers | — (class-level) | TBD |
| 3 | Server | Windows Server | TBD |
| 4 | Server | Linux Server | TBD |
| 5 | Database | Oracle Instance | TBD |
| 6 | Database | MS SQL Instance | TBD |
| 7 | Network Gear | Routers | TBD |
| 8 | Network Gear | Switches | TBD |
| 9 | Network Gear | Firewalls | TBD |
| 10 | Network Gear | Load Balancers | TBD |
| 11 | Network Gear | Wireless Access Points (WAP) | TBD |
| 12 | Network Gear | Network Controllers | TBD |

> **"Row" means a class/subclass pair, not a class.** There are **5 classes** but **12 rows** — Server, Database, and Network Gear each split into multiple subclasses; Business Application and Computers do not. The 12 rows, spelled out: (1) Business Application, (2) Computers, (3) Windows Server, (4) Linux Server, (5) Oracle Instance, (6) MS SQL Instance, (7) Routers, (8) Switches, (9) Firewalls, (10) Load Balancers, (11) Wireless Access Points (WAP), (12) Network Controllers. Every "per row" / "12 rows" reference in Workstreams 0, 1, and 2 means this list.

| AC # | Acceptance Criteria | Due Date |
|---|---|---|
| 0.1 | Non-discoverable attributes identified and documented per roster row — the specific fields on each class/subclass that no discovery source populates and that require manual/business input | TBD — CO7 term |
| 0.2 | The "Technical Owner Group" column is fully populated — a named group assigned to each of the 12 rows, with none left TBD | TBD — CO7 term |
| 0.3 | An access model (roles/ACLs) is designed per roster row: write access to that row's non-discoverable attributes scoped to its assigned Technical Owner Group only; discoverable attributes remain read-only and discovery-managed | TBD — CO7 term |
| 0.4 | The role/ACL configuration is built and deployed to production for all 12 roster rows | TBD — CO7 term |
| 0.5 | Access is validated per row: the assigned Technical Owner Group can modify its own non-discoverable attributes, cannot modify another row's records, and cannot modify discoverable attributes | TBD — CO7 term |
| 0.6 | Technical Owner Groups are notified/trained on their new access and which fields they are now responsible for maintaining | TBD — CO7 term |
| 0.7 | Configuration Management (Ops) team's responsibilities defined per roster row: health monitoring, report generation, and first-line escalation support for that row's Technical Owner Group | TBD — CO7 term |
| 0.8 | Configuration Management (Ops) team is provisioned with cross-class oversight access (not scoped to a single row like Technical Owner Groups) so it can monitor and report across all 12 rows | TBD — CO7 term |
| 0.9 | Routing rule defined and agreed with the Discovery team: issues on discoverable attributes are triaged by Ops and escalated to Discovery (not to the row's Technical Owner Group) for resolution via discovery configuration, credentials, or source data | TBD — CO7 term |

---

## 1. CMDB Health & Compliance Monitoring

**Description:** The CMDB team builds and owns the central framework — correctness/compliance rules and the automated health dashboard, covering both discoverable and non-discoverable attributes. Configuration Management (Ops) monitors that dashboard, produces reports, and routes each finding to its correct resolver: **Technical Owner Group** for non-discoverable attribute issues, **Discovery team** for discoverable attribute issues.

**Why it matters:** Continuous health visibility catches configuration drift and compliance violations as they occur, rather than at the next certification cycle. Remediation only works at scale if every finding reaches the team that can actually fix it — a Technical Owner Group fixing its own non-discoverable fields, Discovery fixing a broken credential or stale discovery pattern — with Ops as the single point that tells the two apart, so neither the CMDB delivery team, Ops, Technical Owner Groups, nor Discovery becomes a bottleneck for the other's issues.

| AC # | Acceptance Criteria | Due Date |
|---|---|---|
| 1.1 | Correctness and compliance rules are defined and documented for each of the 12 roster rows, covering both discoverable and non-discoverable attributes (required relationships, valid values, minimum-field policy), owned centrally by the CMDB team | TBD — CO7 term |
| 1.2 | An automated health dashboard is live in production: Technical Owner Groups see a view scoped to their own row; Configuration Management (Ops) sees a cross-class rollup of all 12 rows, split by discoverable vs. non-discoverable findings | TBD — CO7 term |
| 1.3 | Records failing a check on a **non-discoverable** attribute automatically route a remediation notification to that row's Technical Owner Group, with a defined correction SLA and visibility to Ops | TBD — CO7 term |
| 1.4 | Records failing a check on a **discoverable** attribute automatically route a remediation notification to the Discovery team (per the Workstream 0 routing rule), with a defined correction SLA and visibility to Ops | TBD — CO7 term |
| 1.5 | Technical Owner Groups and the Discovery team each remediate findings directly within their own domain; items unresolved within SLA escalate to Configuration Management (Ops), who tracks the item to resolution and engages the CMDB team only if a systemic/tooling issue is found | TBD — CO7 term |
| 1.6 | Configuration Management (Ops) produces a recurring report on remediation performance (time-to-resolve, escalation rate), broken out per roster row for Technical Owner Groups and separately for the Discovery team's discoverable-attribute queue | TBD — CO7 term |

---

## 2. CI Lifecycle & Retirement Automation

**Description:** The CMDB team builds and owns the central retirement/archiving rules and automation engine. Configuration Management (Ops) monitors retirement activity and supports Technical Owner Groups on exceptions. Each Technical Owner Group disposes of ambiguous or flagged records within its own class/subclass, exercising the non-discoverable-attribute access Workstream 0 configures (e.g., setting a lifecycle/retirement status field).

**Why it matters:** Automating lifecycle management prevents stale CIs from silently accumulating and inflating coverage metrics. Disposition of ambiguous records is a judgment call best made by the group that knows the asset, with Ops available to help when a Technical Owner Group is unsure how to proceed or an exception queue backs up.

| AC # | Acceptance Criteria | Due Date |
|---|---|---|
| 2.1 | Retirement trigger conditions are defined for each of the 12 roster rows (discovery-confirmed decommission, inactivity threshold, authoritative-source flag), owned centrally by the CMDB team | TBD — CO7 term |
| 2.2 | Archiving rules are defined per roster row (retention period, archive destination, audit-trail capture) and documented for governance review | TBD — CO7 term |
| 2.3 | Automated retirement/archiving is live in production for all 12 roster rows, processing eligible records on a defined schedule with no manual step required | TBD — CO7 term |
| 2.4 | An exception workflow routes ambiguous or flagged records to that row's Technical Owner Group for disposition; items unresolved within SLA escalate to Configuration Management (Ops) for support; no record is retired without automated clearance or Technical Owner Group sign-off | TBD — CO7 term |
| 2.5 | Configuration Management (Ops) produces a reconciliation report across all 12 rows (rolled-up view); each Technical Owner Group receives the equivalent report scoped to its own row | TBD — CO7 term |

---

## Open questions before this goes to Jordan

1. Should Computers or Business Application also get subclass-level breakdown (e.g., Desktop vs. Laptop), for consistency with Server/Database/Network Gear?
2. Who fills the "Technical Owner Group" column in the Workstream 0 roster for each of the 12 rows — does every row already have a natural group, or does Workstream 0 need to include standing up ownership where none exists?
3. Does the Configuration Management (Ops) team already exist today, or is standing it up itself part of this proposal's scope (staffing, not just process/access)?
4. Does the existing Discovery team have capacity to take on this ongoing remediation-support role, or does it need dedicated allocation/staffing for it?
5. What is the actual list of non-discoverable attributes per class/subclass (AC 0.1)? Confirm whether a version of this already exists (e.g., from the ESS-02 gap analysis or the data dictionary work) that can be reused instead of redone.
6. Should these workstreams stay standalone, or fold under the existing CMDB Governance deliverable line as its natural next phase?
7. What is the actual proposed CO7 term (start/end)? All due dates here are placeholders until that's set.
