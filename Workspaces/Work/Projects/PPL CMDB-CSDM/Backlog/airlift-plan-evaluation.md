---
type: reference
workspace: Work
project: CMDB-CSDM
pi: PI-3
updated: 2026-07-08
tags: [work, cmdb-csdm]
---

# Airlift × CMDB Plan (Draft) — Evaluation & Gaps

> **Reference only.** Evaluation of the draft **`ServiceNow_Airlift_CMDB_Plan_Draft.xlsx`** (in Manuel's Downloads — **not stored in the vault**), reviewed **2026-07-08**. To be worked as part of **CO6**. This is a review of a DRAFT, not a committed plan.
> Related: [[airlift-decomposition]] · [[configuration-management-plan-stage1]] · [[co6-deliverable-tracking]] · [[weekly-activity-reference-2026-07-08]].

## Plan snapshot

**Operating model:** Airlift executes all data changes in ServiceNow; the ServiceNow team **enables** (best practices, training, validation) but performs **no direct uploads or modifications**.

**Workstreams:**
- **WS1 — Application Attribute Enrichment** — move app data (business owners, support groups, manual attributes) into CMDB application records. (steps 1.1–1.4)
- **WS2 — Server Decommissioning** — identify retired servers, set Non-Operational. (2.1–2.5)
- **WS3 — New Server Discovery & Onboarding** — ensure new servers are discovered and added to the CMDB. (3.1–3.7)
- **WS4 — Service Mapping (TBD)** — scope / gather / create / validate / remediate service maps. (4.1–4.5)

Sheets: Overview · WS1 - App Attributes · WS234 - Server Decom+Onboard+SM · WS3 - New Servers.

## Verdict

Solid skeleton, but a **task inventory, not yet an execution plan.** Good decomposition and a clear RACI; missing owners, dates, dependencies, acceptance criteria, resourcing, and governance linkage. Appropriate for a draft — needs a firming-up pass before CO6 commitment.

## Strengths
- Clear ownership boundary (Airlift executes / ServiceNow enables + validates).
- Logical phase flow: inventory → discovery → validation → gap remediation → attribute update → service mapping.
- Reuses real CMDB mechanics (Discovery, import sets/transform maps, App Services vs. Business Applications, decom→replacement mapping).

## Gaps

**A. Not execution-ready (accountability & schedule)**
- No owners or dates anywhere — only **Jordan** (ServiceNow) and **Daniel** (Airlift) are named, on step 1.1; every other Owner/Date cell is blank and all steps are "Not Started."
- No dependencies, critical path, or milestones; no alignment to **Airlift migration waves** — yet timing drives correctness (e.g., decom 2.5 depends on reconciliation 2.2 + replacement mapping 3.2; Discovery 3.4 depends on prep/credentials 3.3).
- No acceptance criteria / definition of done — "validate / verify / confirm" with no measurable bar (% coverage, counts).

**B. Governance & data-quality linkage missing**
- No tie to the **CMP Stage 1 Data Dictionary** (attribute definitions, mandatory fields, authoritative sources being ratified 7/21). Risk: Airlift bulk-loads attributes with no governance standard → recreates the December-audit data debt.
- Reconciliation method unspecified (1.1, 2.2) → **duplicate-CI risk** on mass load (no IRE / matching-key approach).
- Change control / CI-retirement workflow not represented (2.5 mass status changes) — needs change tickets / CAB and the retirement lifecycle (Operational Status allowed values are an open `[CCB confirm]` item on the decision sheet).

**C. Scope & sequencing risks**
- **BA → Application Service collision:** step 1.2 flags the timing of migrating BA records to the App Service table + mass app load, but leaves it unresolved — collides with Tony's BA-table migration and the 6/10 "pause Business App enhancements" decision.
- Resourcing unresolved — 5+ steps marked *"TBD based on CMDB resourcing availability";* competes with CO6's new ITSM / BAU / ATF workstreams.
- **Service Mapping (WS4) entirely TBD** — a major workstream folded in as placeholders; depends on WS3 completing first.

**D. Plan hygiene**
- **Numbering conflict:** the standalone "WS3 - New Servers" sheet and the combined "WS234" sheet both define steps 3.1–3.x with *different activities* under the same numbers → two sources of truth; consolidate.
- No risk / assumptions log (credentials, network reachability, IP-reuse Discovery collisions, premature CI retirement, data-freeze / cutover windows).
- No progress KPIs for Go Green / leadership reporting.

## Moving forward under CO6
1. Use the plan as the **decomposition backbone** — each step (1.1, 2.1, 3.x, 4.x) → a story with owner + date + acceptance criteria, feeding the forward/CO6 lane of [[airlift-decomposition]].
2. Anchor every data step to the ratified **Data Dictionary + Data Certification** so Airlift loads governance-compliant data.
3. Add a schedule tied to **migration waves** + a critical path; resolve the resourcing "TBDs" against confirmed CO6 capacity before committing.
4. Stand up a **risk log** and per-workstream **KPIs**; fix the WS3 numbering so there's one source of truth.
