---
workspace: Work
project: CMDB-CSDM
type: reference
status: draft
updated: 2026-10-15
tags: [work, cmdb-csdm, governance, data-definitions, reference]
sources:
  - file: "Config-Mgmt-Plan/Application-Ownership-Framework-v2.pptx"
    title: "Application Ownership Framework (v2)"
    ingested: 2026-10-15
---

# Application Ownership Framework (v2)

> **What it is:** A PPL Enterprise Architecture / Governance deck (13 slides, v2, not yet ratified) defining a federated application ownership model across all application types, aligned to the Business and Tech Foundation Value Stream interaction model. Grounded in ISO/IEC 27001 A.5.9, ServiceNow CSDM, and IT4IT.
>
> **Why it matters to CMDB-CSDM:** It is the EA-side answer to "who should be in the owner fields." It names the roles; it does **not** map them to ServiceNow technical fields. That mapping is the open work tracked in [[ownership-terminology-mapping]] and [[cmdb-ownership-scoping-matrix]].
>
> **Status:** v2 draft for ARB / SteerCo endorsement. Not an approved PPL standard as of 2026-10-15.
>
> **Source:** [[Config-Mgmt-Plan/Application-Ownership-Framework-v2.pptx]] · reviewed 2026-10-15.

---

## The Governing Rule

Every application has **ONE Business Owner (Accountable)** and **ONE IT / Technical Owner (Responsible)**, mapped to **one Home Value Stream**, registered in **APO → CMDB**.

- Business apps: Business Owner sits in a vertical Business Value Stream.
- IT-owned tools: Business Owner sits in the consuming IT function; run by Tech Foundation.
- **Never one person in both seats.**

**What "good" looks like (slide 4):** every application has a named Business Owner and a named IT/Technical Owner, mapped to one Home Value Stream, registered in APO → CMDB.

### Industry anchors cited

| Anchor | Claim made in the deck |
|---|---|
| ISO/IEC 27001 A.5.9 | Every information asset has a named owner accountable for classification, risk and review — ownership ≠ administration |
| ServiceNow CSDM | Business Application carries both a Business Owner and an IT/Technical Owner as distinct, mandatory roles |
| IT4IT + Plan-Build-Run | Ownership follows the service lifecycle: business intent (Plan) → build (Solution/System Architect) → run (Support/Ops) |

---

## Section 1 — Application Taxonomy (12 types)

| # | Type | PPL Examples |
|---|---|---|
| 1 | Enterprise / ERP | SAP S/4HANA, HXM, Concur |
| 2 | On-Prem, COTS / Packaged | PowerPlan, Infor FSM |
| 3 | SaaS / Multi-tenant Cloud | Octave EAM, ServiceNow, S/4HANA |
| 4 | Custom / Bespoke | PA.NET, KY .NET, in-house apps |
| 5 | Integration Platforms | LWC, SAP BTP, GlobalScape, webMethods, APIMs |
| 6 | Data & Analytics Platform | Snowflake, Databricks, Datasphere |
| 7 | AI / Agentic Applications | Now Assist, Copilot, AI agents |
| 8 | Infrastructure Tooling / Platform Services | Azure, shared compute & IaC |
| 9 | Security Tooling | CyberArk PAM, SailPoint, KY AIM |
| 10 | OT / Embedded / Field | ADMS, PLC / gas-control, Genetec |
| 11 | Legacy / End-of-Life | 7-R decommission candidates |
| 12 | Reporting / BI Assets | Power BI, business-built reports |

---

## Section 2 — The Problem Statement (slide 4)

| Problem | Detail |
|---|---|
| Ownership drifted after re-org | Two years of reorganization left no clean application ownership matrix — owners change on immediate need, not by design |
| No rule for "who owns what" | Mixed ownership across value streams (webMethods vs GlobalScape, PVCS vs ADO, KY AIM vs SailPoint) |
| Gaps create real risk | Unowned apps (e.g. legacy .NET) surface only when something breaks, is audited, or must be decommissioned |

---

## Section 3 — Value Stream Alignment (slide 5)

**Vertical — Business Value Streams** own *business* ownership of their apps:
Advanced Customer Ops & Engagement · NextGen Enterprise Technology · Field & Colleague Technology · Grid & Pipeline of the Future.
Each app is "homed" to exactly one vertical stream.

**Horizontal — Tech Foundation Value Streams** own *technical* ownership of shared services:

| Tech Foundation VS | Scope |
|---|---|
| Infrastructure & Operations | Hosting · Platform Eng · IaC · environments |
| Data & AI | Data platforms · analytics · AI / agentic |
| Cybersecurity | Security baselines · IAM · SOC · controls |

**Enabling function — Enterprise & Business Architecture** owns the decision rights (RAPID / RACI), standards, taxonomy, and the APO → CMDB system of record. Sets "who owns what"; does **not** own day-to-day run. Resolves cross-value-stream ownership via ARB / Cross-VS Architecture Sync.

---

## Section 4 — The Decision Matrix (slide 7)

`A` = Accountable · `R` = Responsible · `C` = Consulted · `(TF)` = Tech Foundation VS · `(H)` = Horizontal / shared service

| # | Application Type | Business Owner (A) | IT / Technical Owner (R) | Key Supporting Owners (C) | Home Value Stream |
|---|---|---|---|---|---|
| 1 | ERP / Enterprise Platform | Enterprise VS Business Lead (Finance / SCM / HR process owners) | Enterprise VS IT Lead + Solution Architect | Product Mgr · Data · Security · Integration CoE | NextGen Enterprise |
| 2 | COTS / Packaged | Owning business function lead | VS IT / Application Owner | Vendor Mgr · Infra · Security | Aligned Business VS |
| 3 | SaaS / Cloud | Business function / department head | VS IT Owner (config, access, integration) | Vendor/Partner Mgr · Security (SSO/IAM) | Aligned Business VS |
| 4 | Custom / Bespoke | Sponsoring business function | VS IT Owner + System Architect / Dev | Security · Infra · EA (tech-debt) | Aligned Business VS |
| 5 | Integration | Integration lead (IT-owned tool); consuming VSs = C | Integration CoE run team (EA sets standards) | Infra · Security · Domain Architects | EA / Enabling (H) |
| 6 | Data & Analytics | Platform: Data & AI lead. Data products: domain owner | Data & AI Value Stream | Architecture (standards) · Security | Data & AI (TF) |
| 7 | AI / Agentic | Business sponsor of the use case | Data & AI VS + AI CoE | Security · EA · Compliance (AIGC) | Data & AI + AI Gov |
| 8 | Infrastructure Tooling / Platform | Infra & Operations leadership (IT) | Platform Engineering / Infra & Ops | Security · Enterprise Architecture | Infra & Ops (TF) |
| 9 | Security Tooling | Cybersecurity leadership | Cybersecurity Value Stream | Infra · IAM · EA | Cybersecurity (TF) |
| 10 | OT / Embedded / Field | Operations business owner (Grid / Field) | OT / Field IT Owner — must be named\* | OT Security · Infra · Vendor | Grid / Field |
| 11 | Legacy / End-of-Life | Retiring business function | IT Owner + Product Mgr (R decom; BO = A) | Data · Security · Infra · Supply Chain · EA | Business VS + EA |
| 12 | Reporting / BI Assets | Business function / department head | VS IT / Application Owner | Security · Domain Architects · Data | Aligned Business VS |

**Platform ownership decision rule (slide 7 footnote):**
- IT Ownership: align with Enterprise VS **and/or** Infrastructure VS
- Business Ownership: align with the largest stakeholder VS

\* The asterisk on row 10 has no corresponding footnote in the deck — see [Review Findings](#review-findings).

---

## Section 5 — Mode 1 vs Mode 2 (slide 8)

The most operationally useful idea in the deck. Every application still needs one named Business Owner (A) and one IT/Technical Owner (R) — the difference is **who fills the Business Owner seat**.

| | **Mode 1 — Business-Owned Application** | **Mode 2 — IT-Owned Tool** |
|---|---|---|
| **What it is** | Supports a business process or capability | A tool used inside IT to build, run, secure or integrate |
| **Examples** | SAP S/4HANA, Octave EAM, PowerPlan, ADMS, Power BI business reports | ADO / PVCS, GlobalScape, webMethods, CyberArk, SailPoint, Azure tooling |
| **Business Owner** | Business process / function leader in the Business VS or LOB | The IT leader who knows how the tool is used (lead of its main user community — e.g. DevOps practice lead for ADO) |
| **IT Owner** | VS IT / application owner | Tech Foundation team that runs the platform |
| **Funding / priority** | Sits with the business | Sits with the consuming IT function |

### The four decision rules

| Rule | Test |
|---|---|
| **MODE TEST** | Do the primary users *run a business process* (Mode 1) or *build, run, secure or integrate technology* (Mode 2)? Platforms hosting business content are Mode 2; the content (report, data product, interface) is its own Mode 1 CI. |
| **TIEBREAKER** | Tool used across many IT teams? Business Owner comes from the function that funds the licences. If still tied, the ARB decides. |
| **AUTHORITY** | The Business Owner must be able to fund the app and accept risk. If the person who knows the tool best lacks that authority, record them as *delegate* and their director as Business Owner. |
| **SAME TEAM** | If users and platform team are one team, the team leader is Business Owner and a separate technical lead is IT Owner. **Never one person in both seats.** |

---

## Section 6 — Primary Role Cards (slides 9–10)

### Business Owner — Accountable (A)

**Purpose:** Speaks for the application's users and value. Accountable for why the app exists, how critical it is, and what risk the organization accepts by running it.

**Key responsibilities:**
- Define business value, scope and success measures
- Set criticality / recovery tier with the IT Owner
- Classify data and confirm regulatory flags (SOX, NERC-CIP, BCSI) with the Data Platform SME
- Approve access models and accept residual risk
- Fund run and change; prioritize enhancements
- **Attest CMDB ownership on the certification cadence**

**Decisions owned:** invest/keep/replace/retire (7-R) · risk acceptance and exceptions · priority of enhancements and releases · who uses the app and how.

**Not responsible for:** day-to-day technical operation · patching, hosting, infrastructure · running the CMDB process.

**CMDB fields named in the deck:** Business Owner · Value Stream · Data Classification · Regulatory Indicator · Service Tier (with IT).

### IT / Technical Owner — Responsible (R; A for technical decisions only)

**Purpose:** Keeps the application technically healthy, secure, supportable and current through its lifecycle, and delivers on the Business Owner's direction.

**Key responsibilities:**
- Own technical health, lifecycle, upgrades and tech debt
- Run releases, configuration and change approval for the CI
- Manage integrations and dependencies with EA / Integration CoE
- Maintain security posture with the Security SME
- Coordinate support, AMS and vendor escalations
- **Certify technical CMDB attributes**

**Decisions owned:** technical design and configuration within standards · change approval (normal/emergency) · technical remediation plans · upgrade and patch timing (with BO) · executes decommission (R; BO decides A).

**Not responsible for:** business value or funding decisions · accepting business or regulatory risk · defining who should use the app.

**CMDB fields named in the deck:** CI Owner / Tech Owner · Technical Owner Group · Support Group · App OS & Version · Change Approval Group.

> ⚠️ These field names are where the framework collides with the open PPL labeling conflict — see [Review Findings](#review-findings) finding 2 and [[ownership-terminology-mapping]] row O5.

---

## Section 7 — Supporting / Consulted Roles (slides 6, 11–12)

| | Role | Purpose | Engaged when | Mode 1 vs Mode 2 |
|---|---|---|---|---|
| A | **Product Manager** | Bridges business SMEs and delivery; owns the product roadmap | Enhancements, new initiatives, LPM stage gates, 7-R retirement | Same role in both modes |
| B | **Data Platform Owner (IT)** | Steward of the data the app creates, holds or consumes; recommends classification (Business Owner decides) | Regulated or sensitive data (Q4), migrations, archival, decommissioning | Same for both modes |
| C | **Solution / Domain Architect** | Design authority — Domain owns "what & why", Solution owns "how" | New solutions, significant change, integration design, TAR reviews | Business-owned: VS-aligned architect. IT-owned: Tech Foundation architect for the platform |
| D | **Security SME** | Security baselines, IAM/SSO/PAM, SOX / NERC-CIP / BCSI controls; coordinates pen testing; owns RBAC and role assignments | Regulated data, external exposure, new access patterns, audits | Same role in both modes. **For security tooling (CyberArk, SailPoint) Cybersecurity is also IT Owner, so IT Risk / GRC acts as independent reviewer — Segregation of Duties** |
| E | **Infra / Platform SME** | Hosting, golden images, IaC, environments (Dev/Test/Pre-Prod/Prod), backup, DR, capacity, non-functional standards | Hosting changes, cloud migration, environment requests, DR testing | Business-owned: consulted service provider. IT-owned infra tools: usually the IT Owner itself |
| F | **Enterprise Architecture** | Architecture guidelines and standards, future-state alignment and 7-R guidance, runs the ownership tree and taxonomy, resolves cross-VS ownership through ARB, coordinates Application Environment check-out / check-in | Intake, new technology review, ownership disputes, rationalization | Same role in both modes. EA sets standards and does not run platforms; the Integration CoE run team is IT Owner for integration platforms |
| G | **Vendor / Partner Manager** | Contracts, licensing and renewals, SLAs and supplier performance, runbooks and support model, supplier lifecycle and exit terms | SaaS / COTS sourcing (Q3), renewals, escalations, decommissioning | Role grows as sourcing moves to SaaS. For IT-owned tools, partners with the consuming IT function on renewals |

---

## Section 8 — Rollout and Guardrails (slide 13)

| Step | Action |
|---|---|
| 1 — Ratify the model | Endorse role definitions, the matrix, both RACIs and the tree as the PPL ownership standard through ARB / SteerCo |
| 2 — Home every app | Run each application through the tree; assign Business + Technical Owner and one Home Value Stream |
| 3 — Register & certify | Reconcile APO → CMDB owner fields; enforce mandatory attributes; certify with no direct user edits |
| 4 — Close the gaps | Prioritize un-owned OT / legacy / .NET CIs; assign named owners; escalate conflicts via ARB |

**Governance guardrails:**
- One Home Value Stream per app — no gaps, no overlap
- Business Owner (A) ≠ IT Owner (R) — two distinct, named roles
- Ownership changes route through certification + 2nd-level approval
- **APO is the interim system of record feeding CMDB**
- IT-owned tools: BO = consuming IT lead; IT Owner = Tech Foundation
- Cross-VS conflicts escalate: Release Captains → Env Mgmt → VS Leads → IMPACT

**Stated outcome:** "a defensible, audit-ready ownership model that survives re-orgs — every application, every type, one accountable owner."

---

## Review Findings

Review performed 2026-10-15 against the v2 deck. Ordered by impact on CMDB-CSDM delivery.

### Strengths

1. **The Mode 1 / Mode 2 split is the load-bearing idea.** It resolves the real problem that ADO, GlobalScape and CyberArk have no business owner in the conventional sense, without weakening the one-BO-one-ITO rule. The mode test is a genuine decision rule, not a platitude.
2. **The three tiebreakers make it operable** — licence funding decides cross-IT tools; the BO must hold funding *and* risk authority (otherwise delegate + director); same-team case splits leader and technical lead. "Never one person in both seats" is the right hard line and is directly enforceable in CMDB.
3. **Segregation of Duties on security tooling** — when Cybersecurity is also IT Owner for CyberArk/SailPoint, IT Risk / GRC becomes the independent reviewer. Audit-defensible, and worth mirroring in certification campaign design.
4. **"Platforms hosting business content are Mode 2; the content is its own Mode 1 CI"** — clean separation of Power BI-the-platform from the reports on it. This is the CI-granularity rule the taxonomy needs.

### Gaps and risks

| # | Finding | Impact on CMDB-CSDM |
|---|---|---|
| 1 | **The decision tree is referenced but never shown.** Slides 5 and 13 both point to "the tree" ("run each application through the tree", "the tree as the PPL ownership standard") — it is not in the deck. | Step 2 is the entire operational workload and its instrument is missing. ARB is being asked to ratify an artifact the deck does not contain. |
| 2 | **The CMDB field names assume a conflict that is not resolved.** Slide 10 lists `CI Owner / Tech Owner · Technical Owner Group` for the IT Owner. PPL labels `managed_by` as "CI Owner" on `cmdb_ci_business_app` (confirmed 2026-09-09), which conflicts with CSDM 5.0's `owned_by`/`managed_by` split — an **open CCB item**. | The framework's two-seat model maps cleanly onto CSDM's intended split, but slides 9/10 never say which ServiceNow attribute each seat lands in. Ratifying as-is resolves the CCB question by implication rather than by decision. See [[ownership-terminology-mapping]] O5 / Q1. |
| 3 | **APO → CMDB has no reconciliation cadence or conflict rule.** "APO is the interim system of record feeding CMDB" — when the two disagree on an owner, which wins and who adjudicates? | Directly affects certification design: certifying a CMDB value that APO will overwrite is wasted effort. |
| 4 | **Step 2 "Home every app" is unsized.** No count, no timeline, no owner, no phasing. Steps 1, 3 and 4 are governance ceremony; step 2 is months of effort. | This is the work that would land on the CMDB-CSDM backlog. Needs sizing before it becomes an unspoken expectation. |
| 5 | **No materiality threshold on type 12 (Reporting / BI Assets).** If every business-built Power BI report becomes its own Mode 1 CI with a named BO and IT Owner, the CI population explodes. | Needs a cutoff rule before it reaches the CMDB taxonomy. |
| 6 | **Business Owner is required to "attest CMDB ownership on the certification cadence" — but no such campaign exists.** Certification in flight covers Computers, Servers, Databases and Network Devices (infrastructure classes); the Business Application certification pilot is separate and narrower. | The deck assigns an obligation with no delivery vehicle behind it. Either a BA ownership attestation campaign gets scoped, or the responsibility is aspirational. |
| 7 | **"Set criticality / recovery tier with the IT Owner"** lands on the open DR field gap — hundreds of apps are missing Criticality / RTO / RPO on the Service Instance. | The framework assigns the accountability; it does not address the existing backlog. Useful leverage for the DR field escalation, but only once owners are named. |
| 8 | **Two mechanical defects.** Slide 7 row 10 has an asterisk ("OT / Field IT Owner — must be named\*") with no footnote text. Footer slide numbers are out of sequence (slide 3 → "5", slide 4 → "2", slide 5 → "7", slide 7 → "6"). | Cosmetic, but visible to ARB. Looks like leftover numbering from a slide reorder. |

### Assessment

The conceptual model is sound, and Mode 1 / Mode 2 is the piece that survives contact with reality. What is missing is the execution layer: the decision tree artifact, the ServiceNow field mapping, and a sized plan for step 2. Ready to present as a **model**; not yet ready to be ratified as a **standard**.

---

## Open Questions for CMDB-CSDM

| # | Question | Resolves | Bring to |
|---|---|---|---|
| AOF-1 | Which ServiceNow field carries the framework's "Business Owner (A)" — `business_owner`, or something else? | Finding 2 | Josh Sterling (CCB Chair) · Todd Dierksheide |
| AOF-2 | Which field carries "IT / Technical Owner (R)" — `owned_by`, `managed_by`, or `it_application_owner`? The deck's "CI Owner / Tech Owner" phrasing is ambiguous against PPL's current labels | Finding 2 · [[ownership-terminology-mapping]] O1/O3/O5 | CCB · platform team |
| AOF-3 | Does the framework's "Technical Owner Group" mean `managed_by_group` (PPL's confirmed mapping) or the custom `u_technical_owner_group` on Business Application? | [[ownership-terminology-mapping]] S3/S4 | Todd Dierksheide · platform team |
| AOF-4 | Where is the ownership decision tree, and who owns producing it? | Finding 1 | Enterprise Architecture (Sam Hamilton / Matt Newhouse / Gaurav Parmar) |
| AOF-5 | APO vs CMDB — which is authoritative on an owner-field conflict, and what is the reconciliation cadence? | Finding 3 | EA · Josh Sterling |
| AOF-6 | Is a Business Application **ownership** attestation campaign in scope, and in which PI? | Finding 6 | Sonika Das · Joe Dames |
| AOF-7 | What is the materiality threshold for Reporting / BI assets becoming CIs? | Finding 5 | CCB · Todd Dierksheide |

---

## Related

- [[ownership-terminology-mapping]] — the ServiceNow-side vocabulary this framework needs to bind to; the `managed_by` / "CI Owner" conflict (O5) is the single biggest blocker to field-level adoption
- [[cmdb-ownership-scoping-matrix]] — AUTHORITATIVE v2.0 scoped attribute mapping across Business Applications, Application Services and Hardware Classes
- [[cmdb-csdm-attribute-schema]] — AUTHORITATIVE v2.0 per-attribute narrative for the 9 CMDB ownership/management attributes
- [[csdm5-terminology]] — CSDM 5 (Yokohama) Application Service → Service Instance rename
- [[configuration-management-plan-stage1]] — CMP Stage 1 and the CCB-ratified Data Dictionary this framework would feed
- [[data-dictionary-ccb-decision-sheet]] — the CCB mechanism that would ratify any field-label change arising from finding 2
