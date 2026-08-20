---
type: tracking-list
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
status: pending-validation
owner: Manuel Vazquez
validator: Stan Tomberg
created: 2026-08-05
updated: 2026-08-05
tags: [work, cmdb-csdm, safe, pi-planning, network-discovery]
relationships:
  - target: "[[PI-3/pi3-network-discovery-feature-breakdown]]"
    type: related_to
  - target: "[[PI-3/pi3-nd-1356646-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-cmdb-csdm-ado-tracking]]"
    type: related_to
---

# Networking stories — pending validation by Stan

10 stories across the two remaining Network Discovery objective features (Automate Network Device Discovery in the CMDB, CO6 Obj 4). All **State: New**, none yet validated by Stan Tomberg. Flagged 2026-08-05 for review at the 2026-08-06 sync — outcome feeds back into PI-3 planning.

## Feature 1517005 — Mandatory Attribute Population via Discovery — Network Devices (Sprint 3.3 → 3.4)

| ID | Story | Points | Iteration | State |
|----|-------|--------|-----------|-------|
| 1537633 | CMDB: Define mandatory attribute set for network device classes | 3 | 3.3 | New |
| 1537635 | CMDB: Baseline mandatory-attribute population and gap analysis (network devices) | 3 | 3.3 | New |
| 1537636 | CMDB: Tune discovery patterns to populate discoverable mandatory attributes | 3 | 3.3 | New |
| 1537637 | CMDB: Populate non-discoverable mandatory attributes via authoritative source | — | 3.4 | New |
| 1537638 | CMDB: Validate no blank mandatory fields and reconcile with governance | — | 3.4 | New |

Full detail: [[PI-3/pi3-network-discovery-feature-breakdown]] Feature 2.

## Feature 1356646 — Network Inventory Coverage Reconciliation & Owner Validation (≥90%) (Sprint 3.5 → 3.6 IP)

| ID | Story | Points | Iteration | State |
|----|-------|--------|-----------|-------|
| 1559163 | CMDB: Define the authoritative network device inventory (coverage denominator) | 3 | 3.5 | New |
| 1559166 | CMDB: Gap analysis — discovered inventory vs. authoritative list | 3 | 3.5 | New |
| 1559175 | CMDB: Gap closure — expand credential/access/subnet scope for missing devices | 5 | 3.5 | New |
| 1559183 | CMDB: Coverage metric dashboard by device class | 3 | 3.5 | New |
| 1559193 | CMDB: Business-owner validation and sign-off on ≥90% coverage | 5 | 3.6 | New |

Full detail: [[PI-3/pi3-nd-1356646-stories-dependencies]].

## Why Stan needs to validate these

- Feature 1517005 defines the mandatory-attribute set and discovery-pattern tuning — Stan owns the discovery technical side and needs to confirm scope/feasibility, especially 1537637/1537638 which carry no point estimate yet.
- Feature 1356646's gap-closure story (1559175) was created at 5 points vs. the 8 originally proposed — confirm with Stan whether that's a real scope reduction or an under-estimate, since it's the credential/access remediation work tied to this objective's top risk (RAID: Incomplete Discovery Coverage).
- Both features feed the same objective as 1516993, which is missing ND-4/ND-5 (removed 2026-08-05, no replacement yet) — worth checking whether any of these 10 stories should absorb that now-unstaffed device-type coverage.

## Action items

- [ ] **2026-08-06** — Review this list with Stan and team; confirm scope, points, and owners
- [ ] Update PI-3 planning (ado-tracking, feature-breakdown, and per-feature files) with outcomes
