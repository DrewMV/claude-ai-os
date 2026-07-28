---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1517029 — Certify Computers — CMDB Data Certification"
objective: CO6 Obj 3 — Expand CI Data Certification Across All Major Classes
sprint: "3.2 (build start); process-flow doc 3.1"
co6-due: 2026-09-30
status: reference-draft
updated: 2026-07-28
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification]
relationships:
  - target: "[[PI-3/pi3-data-certification-feature-breakdown]]"
    type: derived_from
  - target: "[[PI-3/pi3-cmdb-csdm-ado-tracking]]"
    type: related_to
  - target: "[[PI-3/pi3-objectives]]"
    type: related_to
  - target: "[[cmdb-health-completeness-correctness-stories]]"
    type: related_to
---

# Feature 1517029 — Stories & Dependencies

**Certify Computers — CMDB Data Certification**
Sprint 3.2 (build) · process-flow doc starts 3.1 · CO6 due Sep 30 · Owner: M. Vazquez

> **Status: REFERENCE / DRAFT** — Manuel creates the real items in ADO under Feature 1517029 and reconciles IDs back here (ADO authoritative). Per [[definition-of-ready]], create stories from the Feature "+" link, never standalone.
> See [[PI-3/pi3-data-certification-feature-breakdown]] for the full feature-level breakdown and the PI-2 BA pilot pattern these stories clone.

---

## Sprint reconciliation note (raise at Sprint Planning)

ADO records Feature 1517029's start as **Sprint 3.2 (Aug 19)**; the [[PI-3/pi3-data-certification-feature-breakdown]] shapes the feature as **3.1 → 3.4**. The reconciliation: the **test code freeze runs through Aug 15** (mid-3.1), so no PROD deployment is possible early — the feature's *build* work correctly starts in 3.2. The only 3.1 work is **doc-only process-flow definition (CC-1)** off the 1480114 gap plan, which needs no deployment. Everything requiring a PROD change is sequenced 3.2+.

---

## CO6 Acceptance Criteria this feature delivers (Sep 30)

From [[PI-3/pi3-objectives]] — Obj 3 (CO6 §4), Sep 30 gate:

> *Data certification process for **Computers**: end-to-end process documented, technical build to PROD, dashboards live, training delivered.*

"Certified" = all four artifacts present for the Computer class:

| Artifact | Delivered by |
|----------|--------------|
| Documented process flow | CC-1 |
| Technical build in PROD | CC-2 |
| Tracking dashboard live | CC-3 |
| Certification cycle executed + monitored | CC-4 |
| Training delivered | CC-5 |

---

## ADO item reconciliation note

This feature clones the **PI-2 Business-Application certification pilot pattern**; no net-new *process* is invented. Reusable story shapes to clone per class (from the feature breakdown):

| PI-2 pilot item | Shape it provides | Clones to |
|-----------------|-------------------|-----------|
| 1480114 | Computer audit-dashboard scope + gap-remediation plan (**anchor**) | Input to CC-1 (see DEP-1) |
| 1402962 | Kick-off / training | CC-5 |
| 1402976 | Execute certification policies | CC-2 / CC-4 |
| 1402980 | Monitor completeness | CC-4 |
| 1402984 | Office hours | CC-5 |
| 1402985 | Process feedback | optional CC-6 |
| 1402727 | Dashboard | CC-3 |

Stories CC-1 through CC-5 are **net-new** for the Computer class — created from the pilot shapes above, re-scoped from Business Application to `cmdb_ci_computer`.

---

## Stories (5)

---

### CC-1 · [User Story] Document the Computer Data Certification process flow

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517029 |
| Sprint | 3.1 (doc-only — no PROD dependency) |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones the BA pilot process definition, re-scoped to Computer |
| Depends on | DEP-1 (1480114 gap plan), DEP-5 (Class Manager) |
| Tags | `Data-Certification` `Computer` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the end-to-end Computer data-certification process documented — trigger, attestation steps, roles, escalation, and remediation path — built off the 1480114 gap-remediation plan,
**So that** the certification campaign for the Computer class runs on an agreed, repeatable workflow before any PROD configuration is built.

**Acceptance criteria:**
- [ ] Process flow diagram covers the full cycle: campaign trigger → owner attestation → gap identification → remediation → re-attestation → sign-off
- [ ] Roles defined at each step (CI Owner, Technical Owner Group, Support Group, Process Owner) using the delivered Data Dictionary field mappings (`managed_by`, `managed_by_group`, `support_group`)
- [ ] Attested attribute set for Computer confirmed against the delivered dictionary (9 managed attributes) and the 1480114 gap plan — no attribute drift between the two
- [ ] Escalation and non-response handling defined (what happens when an owner does not attest within the cycle)
- [ ] Process documented in the agreed location and reviewed with the Computer CCB Class Manager (DEP-5)
- [ ] Doc-only — no PROD change required; deliverable is demonstrable during the Aug 5–15 test freeze

**Dependencies:** DEP-1 (audit spike 1480114 gap plan), DEP-5 (Class Manager attribute confirmation).

---

### CC-2 · [Enabler – Configuration] Build Computer certification policies/rules to PROD

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1517029 |
| Sprint | 3.2 |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402976 (execute policies), re-scoped to Computer |
| Depends on | CC-1, DEP-3 (Data Dictionary CCB), DEP-4 (test freeze lifts) |
| Tags | `Data-Certification` `Computer` `Configuration` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the ServiceNow data-certification campaign, filters, and attestation rules for `cmdb_ci_computer` configured and deployed to PROD,
**So that** Computer CI owners can be issued attestation tasks against the agreed attribute set on a defined schedule.

**Acceptance criteria:**
- [ ] Certification definition/filter created scoping the active `cmdb_ci_computer` population (≈19,901 — reconcile to the "active" lifecycle definition, DEP-5)
- [ ] Attestation rules configured for the Computer managed attribute set per CC-1 (Assigned To, CI Owner, Technical Owner Group, Support Group, Asset Tag, OS, Location, IP Address, Serial Number)
- [ ] Certification schedule configured (frequency + first run window) and documented
- [ ] Configuration migrated to PROD via a governed update set / change (post-freeze, on/after Aug 15 — DEP-4)
- [ ] Task routing verified — attestation tasks land with the correct owner group (`managed_by_group` / `support_group`)
- [ ] Dry-run on a bounded owner group confirms tasks generate and complete without error before full launch

**Dependencies:** CC-1, DEP-3 (attribute set locked by CCB), DEP-4 (test freeze), DEP-5 (active-population definition).

---

### CC-3 · [Enabler – Configuration] Stand up the Computer certification tracking dashboard

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1517029 |
| Sprint | 3.2 → 3.3 |
| Owner | Kiran (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402727 (dashboard), re-scoped to Computer |
| Depends on | CC-2 |
| Tags | `Data-Certification` `Computer` `Dashboard` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** a live tracking dashboard for the Computer certification cycle — coverage, attestation status, and outstanding gaps,
**So that** certification progress against the Sep 30 gate is visible to the team and stakeholders without manual reporting.

**Acceptance criteria:**
- [ ] Dashboard shows Computer certification coverage: % attested, pending, and overdue against the scoped active population
- [ ] Outstanding-gap view surfaces the attributes driving non-certification (cross-checks the 1480114 audit gaps so remediation is not double-counted — DEP-1)
- [ ] Dashboard reads from the live certification records created by CC-2 (not a static export)
- [ ] Coordinated with the CMDB Health Completeness (Computer) config so the two do not build overlapping scoring — see [[cmdb-health-completeness-correctness-stories|CP-1]] (DEP-6)
- [ ] Dashboard reviewed with PO (Joe Dames) and confirmed as the reporting source for the Sep 30 gate
- [ ] Refresh cadence confirmed — scores update on schedule, not stale

**Dependencies:** CC-2 (records must exist to report on), DEP-1 (audit-gap alignment), DEP-6 (CP-1 coordination).

---

### CC-4 · [User Story] Run the Computer certification cycle and monitor completeness

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517029 |
| Sprint | 3.3 |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402980 (monitor completeness), re-scoped to Computer |
| Depends on | CC-2, CC-3 |
| Tags | `Data-Certification` `Computer` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the first Computer certification cycle executed end-to-end with completeness monitored on the dashboard,
**So that** attestation is actively driven to the target coverage and the process is proven before the Sep 30 gate.

**Acceptance criteria:**
- [ ] First certification cycle launched to Computer CI owners via the CC-2 configuration
- [ ] Attestation progress tracked on the CC-3 dashboard through the cycle
- [ ] Gaps surfaced during attestation routed to remediation per the CC-1 process (owner correction / support-group action)
- [ ] Coverage reaches the agreed acceptance target for Computers (ties the 90%-coverage acceptance — DEP-2); shortfall documented with cause if target not met
- [ ] Non-responding owners escalated per the CC-1 escalation path
- [ ] Cycle outcome (coverage %, gaps closed, gaps outstanding) recorded and reviewed at Sprint Review

**Dependencies:** CC-2 (PROD build), CC-3 (dashboard), DEP-2 (90%-coverage acceptance target).

---

### CC-5 · [User Story] Deliver Computer certification training to CI owners

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517029 |
| Sprint | 3.4 |
| Owner | Joe Dames (PO) / Manuel Vazquez |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402962 (kick-off/training) + 1402984 (office hours), re-scoped to Computer |
| Depends on | CC-2, CC-4 |
| Tags | `Data-Certification` `Computer` `Training` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** Computer CI owners trained on the certification process — how to attest, correct gaps, and use office hours,
**So that** owners can sustain certification independently and the CO6 "training delivered" artifact is satisfied for the Computer class.

**Acceptance criteria:**
- [ ] Training material produced covering the Computer certification workflow (attest, remediate, re-attest) per CC-1
- [ ] Training delivered to the Computer CI owner / support-group audience; attendance or distribution recorded
- [ ] Office-hours / support channel established and communicated for attestation questions
- [ ] Quick-reference (job aid) distributed to owners
- [ ] Training completion evidenced for the Sep 30 gate (session recording, deck, or sign-off log)
- [ ] PO (Joe Dames) confirms the training artifact satisfies the CO6 Computer certification acceptance criterion

**Dependencies:** CC-2 (process live to train against), CC-4 (real cycle to reference in training).

**Gate note:** CO6 due Sep 30 lands on the 3.4/3.5 boundary → this story is the tight item; it must be **done by end of Sprint 3.4 (Sep 29)**.

---

## Dependencies (6)

**Work item type:** Dependency · **Linked to:** Feature 1517029 (Blocked By) · **Area path:** A-INFOPS\FY26\PI3

Each dependency is stated as **Problem** (why it blocks) + **Acceptance criteria** (what "resolved" looks like), per SAFe.

---

### DEP-1 · Computer audit-dashboard scope + gap-remediation spike (1480114) closed

| Field | Value |
|-------|-------|
| Title | [Dependency] Close Computer audit spike 1480114 — Feature 1517029 |
| Assigned To | Stan (confirm) |
| Priority | 1 |
| State | ✅ **CLOSED** — 1480114 completed (confirmed 2026-07-28) |
| Due Date | 2026-08-05 (met early) |

**RESOLVED (2026-07-28):** Spike 1480114 is closed. CC-1 (process-flow doc) is **no longer blocked by this dependency** — it may proceed on the published gap plan once DEP-5 (Class Manager attribute confirmation) also clears. Confirm the two sub-criteria below (gap plan published + reviewed with Class Manager) are satisfied by the closed spike; if the review with the Computer Class Manager did not happen inside 1480114, it rolls into DEP-5.

**Problem:** CC-1 documents the certification process *off the 1480114 gap-remediation plan*, and CC-3's dashboard cross-checks the same audit gaps. If 1480114 has not closed, the Computer attribute gap picture is undefined and CC-1 cannot anchor to it — blocking the whole feature at story 1.

**Acceptance criteria:**
- [ ] Spike 1480114 completed and its Computer gap-remediation plan published
- [ ] The audited Computer attribute gaps (Missing CI Owner, Assigned To empty, Location empty, Missing IP) quantified and available as CC-1/CC-3 input
- [ ] Gap plan reviewed with the Computer CCB Class Manager (links DEP-5)

---

### DEP-2 · Computers 90%-coverage acceptance story (G2) created and accepted

| Field | Value |
|-------|-------|
| Title | [Dependency] Create + accept Computers 90%-coverage story (G2) — Feature 1517029 |
| Assigned To | Manuel Vazquez |
| Priority | 1 |
| State | Open (net-new — no formal story exists) |
| Due Date | 2026-08-19 |

**Problem:** The CO6 Computer certification acceptance is evidenced by a 90%-coverage acceptance story (gate G2). No formal ADO story exists yet. Without an agreed coverage target and acceptance vehicle, CC-4's completeness cycle has no defined "done" and the feature cannot be signed off at the Sep 30 gate.

**Acceptance criteria:**
- [ ] 90%-coverage acceptance story for Computers (G2) created in ADO and linked to Feature 1517029
- [ ] Coverage target and measurement basis (which attributes, which active population) agreed with PO (Joe Dames) and PM (Sonika Das)
- [ ] Story referenced as the acceptance target in CC-4
- [ ] Accepted at the appropriate Sprint Review as the Computer certification evidence

---

### DEP-3 · Data Dictionary CCB approval — Computer attribute set (1480097/1480098)

| Field | Value |
|-------|-------|
| Title | [Dependency] Data Dictionary CCB approval covering Computer attributes — Feature 1517029 |
| Assigned To | Manuel Vazquez / Josh Sterling (CCB Chair) |
| Priority | 1 |
| State | Open (target Jul 21 — PI-2 carryover) |
| Due Date | 2026-08-19 |

**Problem:** CC-2 configures attestation rules against the Computer managed-attribute set. If the Data Dictionary is not CCB-approved, the certified attribute list can still change under the team, forcing rework of the PROD build and invalidating early attestations.

**Acceptance criteria:**
- [ ] Data Dictionary CCB approval recorded covering the 9 Computer managed attributes and their field mappings (`managed_by`, `managed_by_group`, `support_group`, etc.)
- [ ] Approved attribute set matches the set configured in CC-2 — no drift
- [ ] Approval date and CCB decision referenced in CC-1 / CC-2

---

### DEP-4 · Test code freeze lifts (no PROD deploy before Aug 15)

| Field | Value |
|-------|-------|
| Title | [Dependency] Test code freeze through Aug 15 — Feature 1517029 |
| Assigned To | Manuel Vazquez |
| Priority | 2 |
| State | Open |
| Due Date | 2026-08-15 |

**Problem:** CC-2 requires a governed PROD deployment of the certification configuration. The test code freeze (PI-3 Risk #1, CHG70100865) runs through Aug 15 — the first 10 days of PI-3 — so no deployment can occur in early Sprint 3.1. This is why the feature's build start is Sprint 3.2, not 3.1.

**Acceptance criteria:**
- [ ] Freeze end date (Aug 15) confirmed unchanged; if extended, CC-2 sprint placement re-planned
- [ ] Deployment window for the certification update set secured on/after Aug 15
- [ ] CC-1 (doc-only) confirmed as the only 1517029 work scheduled during the freeze

---

### DEP-5 · Computer CCB Class Manager confirms attribute set + active-population definition

| Field | Value |
|-------|-------|
| Title | [Dependency] Class Manager sign-off — Computer attribute set + active scope — Feature 1517029 |
| Assigned To | Manuel Vazquez |
| Priority | 2 |
| State | Open |
| Due Date | 2026-08-19 |

**Problem:** CC-2's scoped population (≈19,901 active `cmdb_ci_computer`) and the attested attribute set must be ratified by the Computer CCB Class Manager (Monica Green / Paul Becker). Without confirmation, the certification may score the wrong population (e.g. include retired CIs) or attest attributes owners cannot control.

**Acceptance criteria:**
- [ ] Monica Green / Paul Becker confirm the Computer managed-attribute set to be certified
- [ ] "Active" population definition (`install_status` / `operational_status` values) confirmed so the scored count reconciles to the dictionary figure (19,901)
- [ ] Any attribute an owner cannot reasonably attest to flagged and dispositioned before CC-2 build

---

### DEP-6 · Coordinate with CMDB Health Completeness (Computer) config — CP-1

| Field | Value |
|-------|-------|
| Title | [Dependency] Align cert dashboard with CMDB Health Completeness CP-1 — Feature 1517029 |
| Assigned To | Manuel Vazquez |
| Priority | 3 |
| State | Open — CP-1 exists in ADO as **US 1520415** (Ready DoR); ⚠️ possible duplicate **1526839** (New) to resolve |
| Due Date | 2026-08-19 |

**Problem:** The CMDB Health **Completeness (Computer)** KPI ([[cmdb-health-completeness-correctness-stories|CP-1]] = ADO **1520415**, parent "Governance Validation & Acceptance") scores the same Computer attribute population that CC-3's certification dashboard reports on. Building the two independently risks overlapping/contradictory scoring of the same gaps.

**Acceptance criteria:**
- [ ] CC-3 and CP-1 owners agree which artifact is authoritative for "attribute populated" scoring vs "owner attested"
- [ ] No double-counting of the same Computer gap across the certification dashboard and the CMDB Health completeness score
- [ ] Coordination decision recorded (ADO comment) and reflected in CC-3 acceptance

---

## Sequence summary

```
DEP-1 (Aug 5, 1480114 gap plan) ─┐
DEP-5 (Class Manager) ───────────┼─► CC-1 (process flow, 3.1 doc-only)
                                  │        │
DEP-3 (Data Dictionary CCB) ──────┘        │
DEP-4 (freeze lifts Aug 15) ───────────────┼─► CC-2 (PROD build, 3.2)
                                            │        │
                                            │        ├─► CC-3 (dashboard, 3.2→3.3) ◄── DEP-6 (CP-1 align)
                                            │        │        │
DEP-2 (90% acceptance G2) ──────────────────┘        └────────┼─► CC-4 (run cycle + monitor, 3.3)
                                                              │        │
                                                              └────────┴─► CC-5 (training, 3.4) ── done by Sep 29
```

**Freeze-window rule:** only CC-1 (doc-only) runs during the Aug 5–15 test freeze. All PROD work (CC-2 onward) starts Sprint 3.2.
**Gate:** CO6 Sep 30 lands on the 3.4/3.5 boundary → the feature must be **done by end of Sprint 3.4 (Sep 29)**; CC-5 training is the tight item. Raise DEP-1/DEP-2/DEP-3 (all PI-2 carryover) at PI Planning (IP Iteration, Jul 22–Aug 4).
