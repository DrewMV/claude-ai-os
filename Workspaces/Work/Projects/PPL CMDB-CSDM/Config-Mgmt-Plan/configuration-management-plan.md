---
workspace: Work
tags: [cmdb-csdm, servicenow, governance, ccb, data-definitions]
type: umbrella
status: draft
updated: 2026-06-29
---

# Configuration Management Plan (CMP)

> **Audience:** CMDB Change Control Board (CCB). **Status:** DRAFT for CCB review. **Updated:** 2026-06-29.
>
> The Configuration Management Plan is the **umbrella governance document** for PPL's CMDB. It houses the policies, definitions, and targets that govern how Configuration Items are defined, populated, maintained, certified, and audited. The CMP is built up in **stages** — each stage is a **separate document** (a deliverable in its own right) linked from the roadmap below. **Stage 1** establishes the class & attribute data definitions; later stages add health targets, data certification, lifecycle policy, and security/compliance alignment.
>
> This is a **living document.** Stages beyond Stage 1 are placeholders on the roadmap — to be developed in later increments, not yet authored.

## Deliverable Roadmap

| Stage | Deliverable | Scope | Status | Document |
|---|---|---|---|---|
| **1** | **Class & Attribute Data Definitions** (data dictionary) | Business Application · Computer · Server (+ Windows/Linux) · Database (+ Oracle/MSSQL) · Service Instance | 🟢 **Drafted** | [[configuration-management-plan-stage1]] |
| 2 | CMDB Health Targets & KPIs | Completeness / Compliance / Correctness scores + thresholds per class | ⚪ Planned | _TBD_ |
| 3 | Data Certification Process | Certification cadence, intake, ownership, attestation flow | ⚪ Planned | _TBD_ |
| 4 | Lifecycle Management Policy | Staleness rules, Lifecycle Stage/Status transitions, retirement | ⚪ Planned | _TBD_ |
| 5 | Governance & CCB Operating Model | Roles, CCB cadence, change control, precedence-rule ownership | ⚪ Planned | _TBD_ |
| 6 | Security & Compliance Alignment | ESS-02, SOX scoping, audit coverage targets (e.g., 90%) | ⚪ Planned | _TBD_ |

> Stages 2–6 are a **proposed roadmap** — confirm scope/sequence with Joe & Sonika before authoring.

## CO5 Contract Linkage

- **Stage 1** is the acceptance artifact for **CO5 Governance Deliverable 1.1 (Data Dictionary)**; validation stories 1.1a–1.1d in [[../Backlog/co5-governance-validation-stories]] validate it.
- Later stages map to **CO5 D1.2** (Data Certification), the non-SOW **Health & Lifecycle** lane ([[../Backlog/cmdb-health-lifecycle-validation-stories]]), and **CO6** governance scope.
- Deliverable tracking: [[../co5-deliverable-tracking]] · [[../co6-deliverable-tracking]].

## Sync Convention (umbrella ↔ stage docs)

The umbrella and each stage are **separate, cross-linked documents** kept in sync by this rule:

1. **Content lives only in the stage doc.** Never copy data-dictionary (or other stage) content into this umbrella — link to it. The umbrella holds roadmap + governance only.
2. **Status is mirrored.** Each stage doc carries a `status` (and `cmp-stage`) field in its frontmatter. When a stage's status changes, update **both** the stage doc frontmatter **and** that stage's `Status` cell in the roadmap above.
3. **Adding a stage:** create the stage doc with `parent: configuration-management-plan` in frontmatter, then add/replace its `_TBD_` row here with a `[[wikilink]]` to it.
4. **Single source of truth:** the stage doc is authoritative for its own content and status; this table is the index/rollup.
