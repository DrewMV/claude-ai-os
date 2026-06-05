---
title: PI2 ADO Flagged Risks — Nolan
type: project-note
workspace: Work
project: ServiceNow
tags: [work, cmdb, risk, pi2, ado, tracking]
created: 2026-06-05
updated: 2026-06-05
summary: "ADO-flagged feature-level risks for PI2 CMDB-CSDM workstream. Shared by Nolan; he is the owner tracking these. Validated and annotated by Manny June 2026."
base_confidence: 0.95
lifecycle: draft
lifecycle_changed: 2026-06-05
provenance: "Risk list shared by Nolan via email '[External] INFOPS Feature Risks - Please take action', week of June 5, 2026. Validated against PI2 ADO backlog snapshot."
---

# PI2 ADO Flagged Risks — Nolan

> **Source:** Nolan — he shared this list and is actively tracking it.
> **Validated by:** Manuel Vazquez, June 5, 2026
> **Scope:** CMDB-CSDM team, PI2

These risks are tracked separately from the [[sprint-2-3-risk-summary]] (which covers sprint-level planning risks). This list reflects ADO-flagged structural issues at the feature level.

---

## Risk Register

### 🔴 High — Genuine Planning Gaps

---

**Feature 1370224 — Define NERC-CIP CI Security Requirements (PI2)**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1370224)
- **Flag:** Feature Has No Start Date; All Children Unscheduled
- **Validation:** ✅ Confirmed accurate
- **Context:** Only child is Spike 1402602. No iteration, no dates. Actively blocked — waiting on Joe Dames (PO) to return before Manny can proceed. No regulatory deadline documented yet.
- **Action needed:** Confirm Joe's return date; assign spike to an iteration; determine if there is a hard NERC-CIP compliance deadline driving urgency.

---

**Feature 1371672 — Governance Model for Requesting New Business Applications**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1371672)
- **Flag:** Feature Has No Start Date; All Children Unscheduled
- **Validation:** ✅ Confirmed accurate
- **Context:** Only child is Story 1455827 (SOX Team Notification). No iteration, no dates. Has fallen off active planning entirely.
- **Action needed:** Determine if this is PI2 committed or should move to PI3 backlog.

---

**Feature 1402979 — Data Certification Pilot - Implementation Support (PI2)**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1402979)
- **Flag:** Feature Has No Start Date; All Children Unscheduled
- **Validation:** ⚠️ Partially accurate — children are assigned to Sprint 2.3 but have no start/end dates set
- **Context:** Stories 1402984 (Office Hours), 1402980 (Monitor Progress), 1402985 (Process Feedback) are all in 2.3 iteration but missing dates. This is **Priority 1 objective** work. Real risk: pilot group may not be confirmed or ready to engage.
- **Action needed:** Set start/end dates on all three stories; confirm pilot group is confirmed and trained before support stories become active.

---

### 🟡 Medium — Feature Hygiene + Partial Gaps

---

**Feature 1383523 — Unplanned Backlog - CMDB Workstream (PI2)**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1383523)
- **Flag:** Feature Not Decomposed; Feature Has No Start Date
- **Validation:** ⚠️ Partially accurate — Story 1452028 exists but is also assigned to Feature 1411480 (duplicate)
- **Context:** "Not decomposed" is misleading — one story exists but is duplicated across two features. No dates at any level.
- **Action needed:** Resolve duplicate assignment of Story 1452028; assign to one feature only; set dates.

---

**Feature 1355866 — Service Mapping PI2 Wave 17 & 18**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1355866)
- **Flag:** Feature Has No Start Date
- **Validation:** ⚠️ Partially accurate — some children have Sprint 2.2 dates, others are unscheduled
- **Context:** Stories 1431652, 1380747, 1281189 have Sprint 2.2 dates. Stories 1400696 (Einstein) and 1281205 (Foglight) have no iteration or dates. Story 1281209 (OEM) is marked "removed" but still on the board.
- **Action needed:** Set feature-level dates; schedule or defer Einstein/Foglight stories; close/remove Story 1281209.

---

### ⚠️ Hygiene — Flags Are Misleading, Real Risk Is Different

---

**Feature 1451935 — Now Assist Natural Language CMDB Search (Phase 3)**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1451935)
- **Flag:** Feature Has No Start Date; All Children Unscheduled
- **Validation:** ⚠️ Misleading — Stories 1455811 and 1455812 are in Sprint 2.3 with dates (6/10–6/23)
- **Context:** Flag likely reflects missing dates at the feature level, not the story level. Real risk is sprint overload — all NowAssist phases are in one sprint and Phase 3 depends on Phase 1 completing first.
- **Action needed:** Set feature-level start/end dates to clear the flag.

---

**Feature 1451936 — Now Assist Guided CI Creation (Phase 4)**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1451936)
- **Flag:** Feature Has No Start Date; All Children Unscheduled
- **Validation:** ⚠️ Misleading — Stories 1451947 and 1451948 are in Sprint 2.3 with dates
- **Context:** Same pattern as Phase 3. Feature-level dates missing.
- **Action needed:** Set feature-level start/end dates.

---

**Feature 1451937 — Now Assist Governance Advice Agentic Workflow (Phase 5)**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1451937)
- **Flag:** Feature Has No Start Date; All Children Unscheduled
- **Validation:** ⚠️ Misleading — Stories 1451949 and 1451950 are in Sprint 2.3 with dates
- **Context:** Same pattern. Feature-level dates missing.
- **Action needed:** Set feature-level start/end dates.

---

**Feature 1451938 — Now Assist Custom Skills / NASK (Phase 5)**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1451938)
- **Flag:** Feature Has No Start Date; All Children Unscheduled
- **Validation:** ⚠️ Misleading — Story 1451955 is in Sprint 2.3 with dates
- **Context:** Same pattern. Feature-level dates missing.
- **Action needed:** Set feature-level start/end dates.

---

### ❓ Unverified — Not in Current Backlog Snapshot

---

**Feature 1355868 — Service Mapping PI2 Wave 19 & 20**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1355868)
- **Flag:** Feature Not Decomposed; Feature Has No Start Date
- **Validation:** ❓ Cannot confirm — not present in backlog data reviewed June 2026
- **Context:** Future wave; likely not yet decomposed by design. Low risk unless Wave 17&18 is closer to done than expected.

---

**Feature 1355871 — Service Mapping PI2 Wave 20 & 21**
[ADO Link](https://dev.azure.com/PPLElectric/A-INFOPS/_workitems/edit/1355871)
- **Flag:** Feature Not Decomposed; Feature Has No Start Date
- **Validation:** ❓ Cannot confirm — not present in backlog data reviewed June 2026
- **Context:** Future wave; same as above.

---

## Summary

| ID | Feature | Flag Accuracy | Risk Level | Owner |
|----|---------|--------------|------------|-------|
| 1370224 | NERC-CIP Requirements | ✅ Accurate | 🔴 High | Manny (after Joe returns) |
| 1371672 | SOX Governance | ✅ Accurate | 🔴 High | TBD |
| 1402979 | Data Cert Support | ⚠️ Partial | 🔴 High | TBD |
| 1383523 | Unplanned Backlog | ⚠️ Partial | 🟡 Medium | TBD |
| 1355866 | Service Mapping 17&18 | ⚠️ Partial | 🟡 Medium | TBD |
| 1451935–1451938 | NowAssist Ph 3–5 | ⚠️ Misleading | 🟡 Hygiene fix | TBD |
| 1355868 | Service Mapping 19&20 | ❓ Unverified | 🟡 Low (future wave) | TBD |
| 1355871 | Service Mapping 20&21 | ❓ Unverified | 🟡 Low (future wave) | TBD |

---

## Related Pages

- [[cmdb-governance-roadmap]] — overall PI2 governance context
- [[nowassist-for-cmdb]] — NowAssist phased activation detail
- [[data-certification-program]] — Data Certification pilot structure
