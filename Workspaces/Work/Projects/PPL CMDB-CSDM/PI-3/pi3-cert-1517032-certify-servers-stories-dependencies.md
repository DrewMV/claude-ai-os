---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1517032 — Certify Servers — CMDB Data Certification"
objective: CO6 Obj 3 — Expand CI Data Certification Across All Major Classes
sprint: "3.2 (build start); process-flow doc 3.1"
co6-due: 2026-09-30
status: reference-draft
updated: 2026-07-28
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification]
relationships:
  - target: "[[PI-3/pi3-data-certification-feature-breakdown]]"
    type: derived_from
  - target: "[[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-cmdb-csdm-ado-tracking]]"
    type: related_to
  - target: "[[PI-3/pi3-objectives]]"
    type: related_to
  - target: "[[cmdb-health-completeness-correctness-stories]]"
    type: related_to
  - target: "[[server-environment-mandatory-spike]]"
    type: related_to
---

# Feature 1517032 — Stories & Dependencies

**Certify Servers — CMDB Data Certification**
Sprint 3.2 (build) · process-flow doc starts 3.1 · CO6 due Sep 30 · Owner: M. Vazquez

> **Status: REFERENCE / DRAFT** — Manuel creates the real items in ADO under Feature 1517032 and reconciles IDs back here (ADO authoritative). Per [[definition-of-ready]], create stories from the Feature "+" link, never standalone.
> Parallel to [[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]] (Computers). Both certify a CI class off the PI-2 BA pilot pattern to the same Sep 30 gate. See [[PI-3/pi3-data-certification-feature-breakdown]] for the full feature-level breakdown.

---

## Sprint reconciliation note (raise at Sprint Planning)

ADO records Feature 1517032's start as **Sprint 3.2 (Aug 19)**; the [[PI-3/pi3-data-certification-feature-breakdown]] shapes it **3.1 → 3.4**. The reconciliation: the **test code freeze runs through Aug 15** (mid-3.1), so no PROD deployment is possible early — the feature's *build* work correctly starts in 3.2. The only 3.1 work is **doc-only process-flow definition (SV-1)** off the 1480112 gap plan, which needs no deployment.

---

## Server starting position vs Computers (why this feature is not a straight clone)

Servers run in parallel with Computers, but the class is in a **stronger and messier** position:

- **Ahead on remediation:** recent work took Server **Location 44%→100%** and **IP 43%→91%** — the ownership/location gaps that dominate Computers are largely closed on Servers.
- **One Mandatory attribute — `environment`:** per the delivered Data Dictionary, Server is the only class with a **Mandatory** managed attribute. Its designation is **unresolved** — an open spike ([[server-environment-mandatory-spike]]) questions whether it is integration-fed (audit shows Missing Environment ≈11,665) and whether "Mandatory" means *scoring weight* or an *enforced save-time constraint*. This directly affects what the certification attests to → **DEP-7**.
- **Disputed active count:** dictionary shows **3,917** active servers; the audit dashboard scopes **15,218**. The certification scope must land on one reconciled number → **DEP-5**.

---

## CO6 Acceptance Criteria this feature delivers (Sep 30)

From [[PI-3/pi3-objectives]] — Obj 3 (CO6 §4), Sep 30 gate:

> *Data certification process for **Servers**: end-to-end process documented, technical build to PROD, dashboards live, training delivered.*

"Certified" = all four artifacts present for the Server class:

| Artifact | Delivered by |
|----------|--------------|
| Documented process flow | SV-1 |
| Technical build in PROD | SV-2 |
| Tracking dashboard live | SV-3 |
| Certification cycle executed + monitored | SV-4 |
| Training delivered | SV-5 |

---

## ADO item reconciliation note

Clones the **PI-2 Business-Application certification pilot pattern**; no net-new *process* is invented. Reusable story shapes (from the feature breakdown):

| PI-2 pilot item | Shape it provides | Clones to |
|-----------------|-------------------|-----------|
| 1480112 | Servers audit-dashboard scope + gap-remediation plan (**anchor**) | Input to SV-1 (see DEP-1) |
| 1402962 | Kick-off / training | SV-5 |
| 1402976 | Execute certification policies | SV-2 / SV-4 |
| 1402980 | Monitor completeness | SV-4 |
| 1402984 | Office hours | SV-5 |
| 1402985 | Process feedback | optional SV-6 |
| 1402727 | Dashboard | SV-3 |

Stories SV-1 through SV-5 are **net-new** for the Server class — the pilot shapes re-scoped from Business Application to `cmdb_ci_server` (Windows + Linux inherit additively from the parent class).

---

## Stories (5)

---

### SV-1 · [User Story] Document the Server Data Certification process flow

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517032 |
| Sprint | 3.1 (doc-only — no PROD dependency) |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones the BA pilot process definition, re-scoped to Server |
| Depends on | DEP-1 (1480112 gap plan), DEP-5 (Class Manager), DEP-7 (Environment ruling) |
| Tags | `Data-Certification` `Server` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the end-to-end Server data-certification process documented — trigger, attestation steps, roles, escalation, and remediation path — built off the 1480112 gap-remediation plan,
**So that** the certification campaign for the Server class runs on an agreed, repeatable workflow before any PROD configuration is built.

**Acceptance criteria:**
- [ ] Process flow diagram covers the full cycle: campaign trigger → owner attestation → gap identification → remediation → re-attestation → sign-off
- [ ] Roles defined at each step (CI Owner, Technical Owner Group, Support Group, Process Owner) using the delivered Data Dictionary field mappings (`managed_by`, `managed_by_group`, `support_group`)
- [ ] Attested attribute set for Server confirmed against the delivered dictionary (10 managed attributes) and the 1480112 gap plan — no attribute drift
- [ ] **`environment` handling explicitly stated** — whether it is attested as Mandatory or Recommended, per the DEP-7 ruling; if unresolved, the process documents both branches
- [ ] Escalation and non-response handling defined
- [ ] Process documented in the agreed location and reviewed with the Server CCB Class Manager, Ray Reuter (DEP-5)
- [ ] Doc-only — no PROD change; demonstrable during the Aug 5–15 test freeze

**Dependencies:** DEP-1 (audit spike 1480112 gap plan), DEP-5 (Class Manager confirmation), DEP-7 (Environment Mandatory ruling).

---

### SV-2 · [Enabler – Configuration] Build Server certification policies/rules to PROD

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1517032 |
| Sprint | 3.2 |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402976 (execute policies), re-scoped to Server |
| Depends on | SV-1, DEP-3 (Data Dictionary CCB), DEP-4 (test freeze lifts), DEP-7 (Environment ruling) |
| Tags | `Data-Certification` `Server` `Configuration` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the ServiceNow data-certification campaign, filters, and attestation rules for `cmdb_ci_server` configured and deployed to PROD,
**So that** Server CI owners can be issued attestation tasks against the agreed attribute set on a defined schedule.

**Acceptance criteria:**
- [ ] Certification definition/filter created scoping the reconciled active `cmdb_ci_server` population (DEP-5 resolves 3,917 vs 15,218); Windows + Linux inherit the parent-class attribute set additively
- [ ] Attestation rules configured for the Server managed attribute set per SV-1: CI Owner (`managed_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Asset Tag (`asset_tag`), Value Stream (`business_unit`), SOX Type (`u_sox_type`), Data Classification (`classification`), Location (`location`), IP Address (`ip_address`), Environment (`environment`)
- [ ] **`environment` configured per the DEP-7 ruling** — as a scored Mandatory attribute, or Recommended, or Mandatory-on-manual-create-only — not enforced in a way that breaks Discovery/integration inserts
- [ ] Certification schedule configured (frequency + first run window) and documented
- [ ] Configuration migrated to PROD via a governed update set / change (post-freeze, on/after Aug 15 — DEP-4)
- [ ] Task routing verified — attestation tasks land with the correct owner group (`managed_by_group` / `support_group`)
- [ ] Dry-run on a bounded owner group confirms tasks generate and complete without error before full launch

**Dependencies:** SV-1, DEP-3 (attribute set locked by CCB), DEP-4 (test freeze), DEP-5 (active population), DEP-7 (Environment ruling).

---

### SV-3 · [Enabler – Configuration] Stand up the Server certification tracking dashboard

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1517032 |
| Sprint | 3.2 → 3.3 |
| Owner | Kiran (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402727 (dashboard), re-scoped to Server |
| Depends on | SV-2 |
| Tags | `Data-Certification` `Server` `Dashboard` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** a live tracking dashboard for the Server certification cycle — coverage, attestation status, and outstanding gaps,
**So that** certification progress against the Sep 30 gate is visible to the team and stakeholders without manual reporting.

**Acceptance criteria:**
- [ ] Dashboard shows Server certification coverage: % attested, pending, and overdue against the scoped active population
- [ ] Outstanding-gap view surfaces the attributes driving non-certification (cross-checks the 1480112 audit gaps so remediation is not double-counted — DEP-1); reflects the closed Location/IP gaps and highlights Environment
- [ ] Dashboard reads from the live certification records created by SV-2 (not a static export)
- [ ] Coordinated with the CMDB Health Completeness (Server) config so the two do not build overlapping scoring — see [[cmdb-health-completeness-correctness-stories|CP-2]] (DEP-6)
- [ ] Dashboard reviewed with PO (Joe Dames) and confirmed as the reporting source for the Sep 30 gate
- [ ] Refresh cadence confirmed — scores update on schedule, not stale

**Dependencies:** SV-2 (records must exist to report on), DEP-1 (audit-gap alignment), DEP-6 (CP-2 coordination).

---

### SV-4 · [User Story] Run the Server certification cycle and monitor completeness

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517032 |
| Sprint | 3.3 |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402980 (monitor completeness), re-scoped to Server |
| Depends on | SV-2, SV-3 |
| Tags | `Data-Certification` `Server` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the first Server certification cycle executed end-to-end with completeness monitored on the dashboard,
**So that** attestation is actively driven to the target coverage and the process is proven before the Sep 30 gate.

**Acceptance criteria:**
- [ ] First certification cycle launched to Server CI owners via the SV-2 configuration
- [ ] Attestation progress tracked on the SV-3 dashboard through the cycle
- [ ] Gaps surfaced during attestation routed to remediation per the SV-1 process; Environment gaps handled per the DEP-7 ruling
- [ ] Coverage reaches the agreed acceptance target for Servers (ties the 90%-coverage acceptance G3 — DEP-2); shortfall documented with cause if target not met
- [ ] Non-responding owners escalated per the SV-1 escalation path
- [ ] Cycle outcome (coverage %, gaps closed, gaps outstanding) recorded and reviewed at Sprint Review

**Dependencies:** SV-2 (PROD build), SV-3 (dashboard), DEP-2 (90%-coverage acceptance G3).

---

### SV-5 · [User Story] Deliver Server certification training to CI owners

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517032 |
| Sprint | 3.4 |
| Owner | Joe Dames (PO) / Manuel Vazquez |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402962 (kick-off/training) + 1402984 (office hours), re-scoped to Server |
| Depends on | SV-2, SV-4 |
| Tags | `Data-Certification` `Server` `Training` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** Server CI owners trained on the certification process — how to attest, correct gaps, and use office hours,
**So that** owners can sustain certification independently and the CO6 "training delivered" artifact is satisfied for the Server class.

**Acceptance criteria:**
- [ ] Training material produced covering the Server certification workflow (attest, remediate, re-attest) per SV-1, including how `environment` is to be attested
- [ ] Training delivered to the Server CI owner / support-group audience; attendance or distribution recorded
- [ ] Office-hours / support channel established and communicated for attestation questions
- [ ] Quick-reference (job aid) distributed to owners
- [ ] Training completion evidenced for the Sep 30 gate (session recording, deck, or sign-off log)
- [ ] PO (Joe Dames) confirms the training artifact satisfies the CO6 Server certification acceptance criterion

**Gate note:** CO6 due Sep 30 lands on the 3.4/3.5 boundary → this story is the tight item; it must be **done by end of Sprint 3.4 (Sep 29)**.

---

## Dependencies (7)

**Work item type:** Dependency · **Linked to:** Feature 1517032 (Blocked By) · **Area path:** A-INFOPS\FY26\PI3

Each dependency is stated as **Problem** (why it blocks) + **Acceptance criteria** (what "resolved" looks like), per SAFe.

---

### DEP-1 · Server audit-dashboard scope + gap-remediation spike (1480112) closed

| Field | Value |
|-------|-------|
| Title | [Dependency] Close Server audit spike 1480112 — Feature 1517032 |
| Assigned To | Anthony (Tony) (confirm) |
| Priority | 1 |
| State | ✅ **CLOSED** — 1480112 completed (ADO PI2.6, confirmed 2026-07-28) |
| Due Date | 2026-08-05 (met early) |

**RESOLVED (2026-07-28):** Spike 1480112 is closed (ADO PI2.6 board, parent "Data Certification Rollout (PI2)"). SV-1 (process-flow doc) is **no longer blocked by this dependency** — the Server gap-remediation plan is available to anchor it. Confirm the "reviewed with Class Manager" sub-criterion below was satisfied inside 1480112; if not, it rolls into DEP-5.

**Problem:** SV-1 documents the certification process *off the 1480112 gap-remediation plan*, and SV-3's dashboard cross-checks the same audit gaps. If 1480112 has not closed, the Server attribute gap picture is undefined and SV-1 cannot anchor to it — blocking the feature at story 1.

**Acceptance criteria:**
- [ ] Spike 1480112 completed and its Server gap-remediation plan published
- [ ] Server attribute gaps quantified (reflecting closed Location/IP gaps and the outstanding Environment gap) and available as SV-1/SV-3 input
- [ ] Gap plan reviewed with the Server CCB Class Manager, Ray Reuter (links DEP-5)

---

### DEP-2 · Servers 90%-coverage acceptance story (G3) created and accepted

| Field | Value |
|-------|-------|
| Title | [Dependency] Create + accept Servers 90%-coverage story (G3) — Feature 1517032 |
| Assigned To | Manuel Vazquez |
| Priority | 1 |
| State | Open (net-new — no formal story exists) |
| Due Date | 2026-08-19 |

**Problem:** The CO6 Server certification acceptance is evidenced by a 90%-coverage acceptance story (gate G3). No formal ADO story exists yet. Without an agreed coverage target and acceptance vehicle, SV-4's completeness cycle has no defined "done" and the feature cannot be signed off at the Sep 30 gate.

**Acceptance criteria:**
- [ ] 90%-coverage acceptance story for Servers (G3) created in ADO and linked to Feature 1517032
- [ ] Coverage target and measurement basis (which attributes — and whether Environment is included — which active population) agreed with PO (Joe Dames) and PM (Sonika Das)
- [ ] Story referenced as the acceptance target in SV-4
- [ ] Accepted at the appropriate Sprint Review as the Server certification evidence

---

### DEP-3 · Data Dictionary CCB approval — Server attribute set

| Field | Value |
|-------|-------|
| Title | [Dependency] Data Dictionary CCB approval covering Server attributes — Feature 1517032 |
| Assigned To | Manuel Vazquez / Josh Sterling (CCB Chair) |
| Priority | 1 |
| State | Open (delivered to PPL 2026-07-21; CCB vote pending) |
| Due Date | 2026-08-19 |

**Problem:** SV-2 configures attestation rules against the Server managed-attribute set. If the Data Dictionary is not CCB-approved, the certified attribute list — including the contested Environment designation — can still change under the team, forcing rework of the PROD build and invalidating early attestations.

**Acceptance criteria:**
- [ ] Data Dictionary CCB approval recorded covering the 10 Server managed attributes and their field mappings (`managed_by`, `managed_by_group`, `support_group`, `business_unit`, `classification`, `environment`, etc.)
- [ ] Environment's requirement designation resolved in the approved dictionary (coordinated with DEP-7)
- [ ] Approved attribute set matches the set configured in SV-2 — no drift
- [ ] Approval date and CCB decision referenced in SV-1 / SV-2

---

### DEP-4 · Test code freeze lifts (no PROD deploy before Aug 15)

| Field | Value |
|-------|-------|
| Title | [Dependency] Test code freeze through Aug 15 — Feature 1517032 |
| Assigned To | Manuel Vazquez |
| Priority | 2 |
| State | Open |
| Due Date | 2026-08-15 |

**Problem:** SV-2 requires a governed PROD deployment of the certification configuration. The test code freeze (PI-3 Risk #1, CHG70100865) runs through Aug 15 — the first 10 days of PI-3 — so no deployment can occur in early Sprint 3.1. This is why the feature's build start is Sprint 3.2, not 3.1.

**Acceptance criteria:**
- [ ] Freeze end date (Aug 15) confirmed unchanged; if extended, SV-2 sprint placement re-planned
- [ ] Deployment window for the certification update set secured on/after Aug 15
- [ ] SV-1 (doc-only) confirmed as the only 1517032 work scheduled during the freeze

---

### DEP-5 · Class Manager confirms attribute set + reconciled active-population count

| Field | Value |
|-------|-------|
| Title | [Dependency] Ray Reuter sign-off — Server attribute set + active scope (3,917 vs 15,218) — Feature 1517032 |
| Assigned To | Manuel Vazquez |
| Priority | 2 |
| State | Open |
| Due Date | 2026-08-19 |

**Problem:** SV-2's scoped population must be ratified by the Server CCB Class Manager (Ray Reuter). The active-server count is **disputed** — the delivered dictionary shows 3,917 while the audit dashboard scopes 15,218 (Missing Environment 11,665 is measured against the larger set). Certifying against the wrong population invalidates the coverage %.

**Acceptance criteria:**
- [ ] Ray Reuter confirms the Server managed-attribute set to be certified
- [ ] The 3,917 vs 15,218 discrepancy explained — exact `install_status` / `operational_status` filter behind each figure agreed with Ray / Stan, and one scored population fixed for certification
- [ ] Any attribute an owner cannot reasonably attest to flagged and dispositioned before SV-2 build

---

### DEP-6 · Coordinate with CMDB Health Completeness (Server) config — CP-2

| Field | Value |
|-------|-------|
| Title | [Dependency] Align cert dashboard with CMDB Health Completeness CP-2 — Feature 1517032 |
| Assigned To | Manuel Vazquez |
| Priority | 3 |
| State | Open — CP-2 exists in ADO as **US 1520424** (Validation) |
| Due Date | 2026-08-19 |

**Problem:** The CMDB Health **Completeness (Server)** KPI ([[cmdb-health-completeness-correctness-stories|CP-2]] = ADO **1520424**, parent "Governance Validation & Acceptance"; and the linked `environment` Spike **1526856**) scores the same Server attribute population that SV-3's certification dashboard reports on. Building the two independently risks overlapping/contradictory scoring of the same gaps.

**Acceptance criteria:**
- [ ] SV-3 and CP-2 owners agree which artifact is authoritative for "attribute populated" scoring vs "owner attested"
- [ ] No double-counting of the same Server gap across the certification dashboard and the CMDB Health completeness score
- [ ] Coordination decision recorded (ADO comment) and reflected in SV-3 acceptance

---

### DEP-7 · Resolve the Server `environment` Mandatory designation (spike)

| Field | Value |
|-------|-------|
| Title | [Dependency] Resolve Server `environment` Mandatory ruling — Feature 1517032 |
| Assigned To | Stan Tomberg (technical) w/ Ray Reuter (requestor) (confirm) |
| Priority | 2 |
| State | Open — created in ADO as **Spike 1526856** (New; parent "Governance Validation & Acceptance") — [[server-environment-mandatory-spike]] |
| Due Date | 2026-08-19 |

**Problem:** `environment` is the only Mandatory Server managed attribute, but its designation is unresolved: (a) it is normally non-discoverable, (b) the delivered slide names no source, (c) audit shows ≈11,665 missing — inconsistent with a reliable integration feed. Two open questions block the build: *what is the source* (integration vs manual), and *does "Mandatory" mean scored-weight or an enforced save-time constraint*. If SV-2 configures Environment as enforced-Mandatory and it is not integration-fed, it can break Discovery/integration inserts and block server creation; if it is attested but unpopulated, it drags Server coverage below the DEP-2 target for reasons owners cannot fix.

**Acceptance criteria:**
- [ ] Spike [[server-environment-mandatory-spike]] completed: source of `cmdb_ci_server.environment` identified with evidence; SCCM hypothesis confirmed or denied
- [ ] "Mandatory" interpretation confirmed with Ray / CCB — scoring designation vs enforced field constraint
- [ ] Enforcement mode decided (scored-only, Recommended, or Mandatory-on-manual-create-only) so SV-2 can configure without breaking inserts
- [ ] Decision fed into DEP-3 (dictionary) and SV-1/SV-2/SV-4; [[cmdb-health-completeness-correctness-stories|CP-2]] updated to match

---

## Sequence summary

```
DEP-1 (Aug 5, 1480112 gap plan) ─┐
DEP-5 (Ray — attr set + count) ──┤
DEP-7 (Environment ruling) ──────┼─► SV-1 (process flow, 3.1 doc-only)
DEP-3 (Data Dictionary CCB) ──────┤        │
DEP-4 (freeze lifts Aug 15) ──────┴────────┼─► SV-2 (PROD build, 3.2)
                                            │        │
                                            │        ├─► SV-3 (dashboard, 3.2→3.3) ◄── DEP-6 (CP-2 align)
                                            │        │        │
DEP-2 (90% acceptance G3) ──────────────────┘        └────────┼─► SV-4 (run cycle + monitor, 3.3)
                                                              │        │
                                                              └────────┴─► SV-5 (training, 3.4) ── done by Sep 29
```

**Freeze-window rule:** only SV-1 (doc-only) runs during the Aug 5–15 test freeze. All PROD work (SV-2 onward) starts Sprint 3.2.
**Gate:** CO6 Sep 30 lands on the 3.4/3.5 boundary → the feature must be **done by end of Sprint 3.4 (Sep 29)**; SV-5 training is the tight item.
**Server-specific critical path:** DEP-7 (Environment ruling) gates SV-1 *and* SV-2 — if the spike is not resolved by ~Aug 19, the build either stalls or proceeds on an assumption that may force rework. Raise DEP-1/DEP-2/DEP-3/DEP-7 (all PI-2 carryover or open spikes) at PI Planning (IP Iteration, Jul 22–Aug 4).
