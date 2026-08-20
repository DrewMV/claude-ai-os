---
type: feature-breakdown
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
objective: Build Service Maps for Business Applications (Obj 5 / CO6 Deliverable #2 — Service Mapping)
contract: CO6 (Change Order #6)
status: draft
updated: 2026-08-05
tags: [work, cmdb-csdm, safe, pi-planning, co6, service-mapping, data-quality]
---

# PI-3 — Migrate Misclassified Business Application CIs to Service Instances: Feature

Child feature under **Obj 5 — Build Service Maps for Business Applications** (CO6 §2), listed as **Feature DQ** in [[pi3-service-mapping-feature-breakdown]]. See also [[pi3-objectives]] (Obj 5).

**Stories:** ~~drafted outside ADO; not yet created as work items~~ **Update (2026-08-05):** 9 of ~10 stories confirmed already created in ADO under this feature — see table below. This supersedes the "not yet created" status; this file's AC above still describes the feature-level intent, but the story-level shapes (S01–S10 titles) predate what's recorded in this file and were not previously documented here.

**Why under Service Mapping:** Service maps are built on top of Business Application CIs. The customer misclassified running application instances as Business Applications — Service Maps built off those CIs would reference the wrong class. Correcting the CI class is a data-quality enabler for accurate service map construction.

---

## Feature Definition

**Feature title (ADO):** Migration of Business Apps to Application Services

**ADO ID:** 1537867 (State: New; Area: A-INFOPS\CMDB-CSDM; Iteration: A-INFOPS\FY26\PI3\Iteration 3.1, 8/5/2026 – 9/1/2026; Value Area: Business)

**Parent Objective (ADO):** 1516955 — Build & Validate Service Maps for Priority Business Apps (Owner: Adam Griffis; CO6 Obj 5) — confirmed linked in ADO

**Definition:**
The customer created their application portfolio using the Business Application CI class (`cmdb_ci_business_app`) when the records actually represent running application instances — the correct class is Service Instance (`cmdb_ci_service_auto`, the base Service Instance table under CSDM v5; "Application Service" was renamed to Service Instance in the Yokohama release). This feature migrates each misclassified Business Application CI into a new, correctly-classed Service Instance CI, then retires the original Business Application CI (rather than deleting it) because Incidents, Problems, and Changes are already associated to it and must not be orphaned.

> **Table name note:** confirm which Service Instance subclass fits — `cmdb_ci_service_auto` (basic, no automation) vs. a more specific subclass (e.g. `cmdb_ci_service_discovered` — Mapped Application Service) — depending on whether these will later be auto-populated/discovered or remain manually maintained.

**Benefit Hypothesis:**
We believe that by migrating customer-created Business Application CIs that represent running application instances into the correct Service Instance class — and retiring the originals to preserve ITSM history — the Service Mapping team will have an accurate CI foundation to build service maps from, and the CMDB CI class hierarchy will correctly reflect the CSDM model.

**Acceptance Criteria:**
1. All identified misclassified Business Application CIs are replicated as Service Instance CIs in PROD with accurate field data
2. Original Business Application CIs are retired (Operational Status = Retired) with a retirement note referencing the corresponding new Service Instance CI sys_id
3. All existing ITSM associations (Incidents, Problems, Changes) to the retired BA CIs remain intact — no orphaned records
4. Service Mapping team confirms the new Service Instance CIs are usable as mapping targets

---

## Stories — confirmed created in ADO (2026-08-05 full board export)

| ADO ID | Story | Points | Sprint | State |
|--------|-------|--------|--------|-------|
| 1553645 | CMDB: S01 Inventory and reference-map the table; confirm all-or-nothing scope | 8 | 3.1 | Ready DoR |
| 1553653 | CMDB: S07 Stakeholder communication, enablement and knowledge | 8 | 3.1 | Ready DoR |
| 1553646 | CMDB: S02 Copy each Business App to a new Application Service, link provenance, and retire the original | 8 | 3.2 | New |
| 1553656 | CMDB: S09 Spike: design the recurrence guardrail for the Business Application class (Spike) | 1 | 3.2 | New |
| 1553648 | CMDB: S04 Enable migrated services: population method, associations, Impacted Services | 3 | 3.3 | New |
| 1553649 | CMDB: S10 validate the migration end state | 5 | 3.3 | New |
| 1553651 | CMDB: S05 Retarget platform configuration off the retired class | 8 | 3.3 | New |
| 1553652 | CMDB: S06 Route operational CIs to Application Service and document correct class use | 3 | 3.4 | New |
| 1553654 | CMDB: S08 Post-migration hypercare and close-out | 5 | 3.4 | New |

**S03 not visible in this export** — the sequence jumps S02 → S04 with no S03 story shown. Confirm in ADO whether S03 exists (and was simply outside the captured rows) or was intentionally folded into another story / skipped.

These story shapes (S01–S10) were not previously documented anywhere in this vault — this is the first record of their titles. Story-level AC/dependencies detail has not yet been written up; add if/when reconciling further, following the pattern in [[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]].

---

## Open Items

- ~~Confirm ADO Epic / parent feature under which this Feature nests in ADO~~ Done — 1537867 parented to 1516955
- ~~Assign feature owner~~ Done — Vazquez, Manuel (for now)
- ~~Add draft stories to ADO under 1537867~~ Done — 9 of ~10 confirmed created (see table above)
- Confirm bulk CI retirement change process with [[cmdb-governance-contacts]] (Josh Sterling — standard vs. normal change)
- Confirm whether S03 exists in ADO
- Write up story-level AC/dependencies for S01–S10 (not yet documented)
