---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1517040 — Certify Network Devices — CMDB Data Certification"
objective: CO6 Obj 3 — Expand CI Data Certification Across All Major Classes
sprint: "3.4 (ADO start); build 3.4–3.5, sign-off 3.6 IP"
co6-due: 2026-10-30
status: reference-draft
updated: 2026-07-27
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification]
relationships:
  - target: "[[PI-3/pi3-data-certification-feature-breakdown]]"
    type: derived_from
  - target: "[[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-nd-1516993-stories-dependencies]]"
    type: depends_on
  - target: "[[PI-3/pi3-cmdb-csdm-ado-tracking]]"
    type: related_to
  - target: "[[PI-3/pi3-objectives]]"
    type: related_to
---

# Feature 1517040 — Stories & Dependencies

**Certify Network Devices — CMDB Data Certification**
ADO start Sprint 3.4 · build 3.4–3.5 · sign-off 3.6 IP · CO6 due Oct 30 · Owner: M. Vazquez

> **Status: REFERENCE / DRAFT** — Manuel creates the real items in ADO under Feature 1517040 and reconciles IDs back here (ADO authoritative). Per [[definition-of-ready]], create stories from the Feature "+" link, never standalone.
> Fourth and last certification feature. Same PI-2 BA pilot pattern as the other three, but the **most back-loaded and most dependent** — see below. See [[PI-3/pi3-data-certification-feature-breakdown]] for the full feature-level breakdown.

---

## Sprint reconciliation & gate note (raise at Sprint Planning)

- **Sprint:** ADO records Feature 1517040's start as **3.4 (Sep 16)**; the [[PI-3/pi3-data-certification-feature-breakdown]] shapes it **3.4 → 3.5** with sign-off in **3.6 IP**. It cannot start earlier because it depends on Obj 4 populating network mandatory attributes first (DEP-1, Sep 30).
- **Gate date open item:** [[pi3-objectives]] and CO6 show **Oct 30**; the objectives deck says **Oct 27**. Build done by **end of Sprint 3.5 (Oct 13)**; 3.6 IP (Oct 14–27) is validation/training buffer. Confirm at planning.

---

## Why this feature is the riskiest of the four (surface at planning)

1. **No audit spike exists yet.** Computers/Servers/Databases each have a completed audit-dashboard scope + gap spike (1480114 / 1480112 / 1480113) as their anchor. Network has **none** — one must be created as the first story (NW-1). That is why this feature has **6 stories, not 5**.
2. **No Network CCB Class Manager is named.** Computers (Monica Green / Paul Becker), Servers & Databases (Ray Reuter), BA (Todd Dierksheide) all have Class Managers. Network devices have **no named governance owner** — required for attribute sign-off and attestation routing (DEP-4).
3. **The certified attribute set isn't in the delivered dictionary.** The 2026-07-21 Data Dictionary covered Computer / Server / Database / BA — **not** network devices. The set is "all mandatory CMDB attributes for network devices per CMDB governance," which must be defined (DEP-3) and approved (DEP-5).
4. **Certification depends on Obj 4 finishing first.** You cannot certify attributes that discovery has not populated. Obj 4 Feature **1517005** (Mandatory Attribute Population via Discovery) gates **Sep 30** — the same window this feature must start. If Obj 4 slips, this feature slips with it (DEP-1). This is the critical path.

---

## CO6 Acceptance Criteria this feature delivers (Oct 30)

From [[PI-3/pi3-objectives]] — Obj 3 (CO6 §4), Oct 30 gate:

> *Data certification process for **Network Devices**: end-to-end process documented, technical build to PROD, dashboards live, training delivered.*

**Device types in scope (CO6 §1, via Obj 4):** Routers · Switches · Firewalls · Load Balancers · Wireless Access Points · Network Controllers

"Certified" = all four artifacts present for the Network Device classes:

| Artifact | Delivered by |
|----------|--------------|
| Audit scope + gap baseline (net-new anchor) | NW-1 |
| Documented process flow | NW-2 |
| Technical build in PROD | NW-3 |
| Tracking dashboard live | NW-4 |
| Certification cycle executed + monitored | NW-5 |
| Training delivered | NW-6 |

---

## ADO item reconciliation note

Clones the PI-2 BA certification pilot pattern, plus a **net-new audit spike** (no existing anchor). Reusable story shapes:

| PI-2 pilot item | Shape it provides | Clones to |
|-----------------|-------------------|-----------|
| *(none — no network audit spike exists)* | Audit-dashboard scope + gap plan | NW-1 (**create net-new**) |
| 1402976 | Execute certification policies | NW-3 / NW-5 |
| 1402980 | Monitor completeness | NW-5 |
| 1402962 / 1402984 | Kick-off / training / office hours | NW-6 |
| 1402727 | Dashboard | NW-4 |

Cross-objective anchor: Obj 4 Feature **1517005** (mandatory attribute population) must complete before NW-3 build is meaningful — see DEP-1. Discovery of the devices themselves is Obj 4 Feature **1516993** — see DEP-2.

> **Prefix note:** these certification stories use **NW-**; the Obj 4 network *discovery* stories use **ND-** ([[PI-3/pi3-nd-1516993-stories-dependencies]]). Different features, different work.

---

## Stories (6)

---

### NW-1 · [Enabler – Exploration (Spike)] Network audit-dashboard scope + gap-remediation baseline

| Field | Value |
|-------|-------|
| Type | Enabler – Exploration (Spike) |
| Parent feature | 1517040 |
| Sprint | 3.3 → 3.4 |
| Owner | Stan Tomberg (confirm) |
| Points | TBD (hard timebox) |
| ADO note | Net-new — the network equivalent of 1480112/113/114, which do not exist yet |
| Depends on | DEP-2 (discovery live), DEP-3 (attribute set) |
| Tags | `Data-Certification` `Network` `Spike` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** an audit-dashboard scope and gap-remediation baseline for the six network device classes,
**So that** the network certification process (NW-2+) has the same gap-plan anchor the other three classes already have.

**Acceptance criteria:**
- [ ] Audit view scoped to the six device classes (Routers, Switches, Firewalls, Load Balancers, WAPs, Network Controllers) with exact `sys_class_name` values confirmed
- [ ] Per-attribute population baseline captured for the mandatory attribute set (DEP-3) — % populated / missing per class
- [ ] Gap-remediation plan drafted (which gaps are discovery-fixable vs owner-attestable)
- [ ] Baseline reconciled against the Obj 4 ≥90% coverage denominator (1356646) so counts agree
- [ ] Findings written up as the anchor input to NW-2 / NW-4

**Dependencies:** DEP-2 (devices discovered as CIs), DEP-3 (attribute set defined).

---

### NW-2 · [User Story] Document the Network Device certification process flow

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517040 |
| Sprint | 3.4 |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones the BA pilot process definition, re-scoped to Network |
| Depends on | NW-1, DEP-3 (attribute set), DEP-4 (Class Manager) |
| Tags | `Data-Certification` `Network` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the end-to-end Network Device certification process documented — trigger, attestation steps, roles, escalation, and remediation path — built off the NW-1 baseline,
**So that** the certification campaign runs on an agreed, repeatable workflow before any PROD configuration is built.

**Acceptance criteria:**
- [ ] Process flow covers the full cycle: trigger → owner attestation → gap identification → remediation → re-attestation → sign-off
- [ ] Roles defined at each step, with the Network CCB Class Manager / governance owner identified (DEP-4)
- [ ] Attested attribute set confirmed against the network mandatory-attribute set (DEP-3) and the NW-1 baseline
- [ ] Process distinguishes discovery-populated attributes (fixed via Obj 4) from owner-attestable attributes
- [ ] Escalation and non-response handling defined
- [ ] Reviewed with the network governance owner (DEP-4)
- [ ] Doc-only — no PROD change required

**Dependencies:** NW-1 (baseline), DEP-3 (attribute set), DEP-4 (governance owner).

---

### NW-3 · [Enabler – Configuration] Build Network Device certification policies/rules to PROD

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1517040 |
| Sprint | 3.4 → 3.5 |
| Owner | Stan Tomberg / Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402976 (execute policies), re-scoped to Network |
| Depends on | NW-2, DEP-1 (Obj 4 attributes populated), DEP-5 (Data Dictionary CCB) |
| Tags | `Data-Certification` `Network` `Configuration` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the ServiceNow data-certification campaign, filters, and attestation rules for the network device classes configured and deployed to PROD,
**So that** network device owners can be issued attestation tasks against the mandatory attribute set on a defined schedule.

**Acceptance criteria:**
- [ ] Certification definition/filter created scoping the active network device population across the six classes (baseline per NW-1)
- [ ] Attestation rules configured for the network mandatory attribute set (DEP-3 / DEP-5)
- [ ] **Attributes confirmed populated by Obj 4 discovery (DEP-1) before the cycle runs** — certification does not attest empty fields discovery was supposed to fill
- [ ] Certification schedule configured (frequency + first run window) and documented
- [ ] Configuration migrated to PROD via a governed update set / change
- [ ] Task routing verified — attestation tasks land with the correct owner group
- [ ] Dry-run on a bounded device set confirms tasks generate and complete without error

**Dependencies:** NW-2, DEP-1 (Obj 4 mandatory attributes populated — critical), DEP-5 (attribute set CCB-approved).

---

### NW-4 · [Enabler – Configuration] Stand up the Network Device certification tracking dashboard

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1517040 |
| Sprint | 3.4 → 3.5 |
| Owner | Kiran (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402727 (dashboard), re-scoped to Network |
| Depends on | NW-3 |
| Tags | `Data-Certification` `Network` `Dashboard` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** a live tracking dashboard for the Network Device certification cycle — coverage, attestation status, and outstanding gaps,
**So that** certification progress against the Oct 30 gate is visible without manual reporting.

**Acceptance criteria:**
- [ ] Dashboard shows network certification coverage: % attested, pending, and overdue against the scoped active population per device class
- [ ] Outstanding-gap view surfaces the attributes driving non-certification (cross-checks the NW-1 baseline so remediation is not double-counted)
- [ ] Dashboard reads from the live certification records created by NW-3 (not a static export)
- [ ] Coverage aligns with the Obj 4 ≥90% network coverage reporting (1356646) so the two objectives tell a consistent story
- [ ] Dashboard reviewed with PO (Joe Dames) and confirmed as the reporting source for the Oct 30 gate
- [ ] Refresh cadence confirmed — scores update on schedule, not stale

**Dependencies:** NW-3 (records must exist to report on).

---

### NW-5 · [User Story] Run the Network Device certification cycle and monitor completeness

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517040 |
| Sprint | 3.5 |
| Owner | Bhushan Salsekar (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402980 (monitor completeness), re-scoped to Network |
| Depends on | NW-3, NW-4, DEP-1 |
| Tags | `Data-Certification` `Network` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** the first Network Device certification cycle executed end-to-end with completeness monitored on the dashboard,
**So that** attestation is actively driven to the target coverage and the process is proven before the Oct 30 gate.

**Acceptance criteria:**
- [ ] First certification cycle launched to network device owners via the NW-3 configuration
- [ ] Attestation progress tracked on the NW-4 dashboard through the cycle
- [ ] Gaps surfaced during attestation routed to remediation per the NW-2 process
- [ ] Coverage reaches the agreed acceptance target for network devices; shortfall documented with cause (esp. gaps traceable to Obj 4 discovery not yet populating attributes — DEP-1)
- [ ] Non-responding owners escalated per the NW-2 escalation path
- [ ] Cycle outcome recorded and reviewed at Sprint Review

**Dependencies:** NW-3 (PROD build), NW-4 (dashboard), DEP-1 (attributes populated — gaps from unpopulated discovery are not owner-attestable).

---

### NW-6 · [User Story] Deliver Network Device certification training to owners

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1517040 |
| Sprint | 3.5 → 3.6 IP (sign-off) |
| Owner | Joe Dames (PO) / Manuel Vazquez |
| Points | TBD at refinement |
| ADO note | Net-new — clones pilot 1402962 (kick-off/training) + 1402984 (office hours), re-scoped to Network |
| Depends on | NW-3, NW-5 |
| Tags | `Data-Certification` `Network` `Training` `CO6-Obj3` |

**As** the CMDB Configuration Management Process Owner,
**I want** network device owners trained on the certification process — how to attest, correct gaps, and use office hours,
**So that** owners can sustain certification independently and the CO6 "training delivered" artifact is satisfied for the Network Device class.

**Acceptance criteria:**
- [ ] Training material produced covering the network certification workflow (attest, remediate, re-attest) per NW-2
- [ ] Training delivered to the network device owner audience; attendance or distribution recorded
- [ ] Office-hours / support channel established and communicated
- [ ] Quick-reference (job aid) distributed to owners
- [ ] Training completion evidenced for the Oct 30 gate (session recording, deck, or sign-off log)
- [ ] PO (Joe Dames) confirms the training artifact satisfies the CO6 Network Device certification acceptance criterion

**Gate note:** build done by end of Sprint 3.5 (Oct 13); training/validation sign-off completes in **3.6 IP (Oct 14–27)** ahead of the Oct 30 external date.

---

## Dependencies (5)

**Work item type:** Dependency · **Linked to:** Feature 1517040 (Blocked By) · **Area path:** A-INFOPS\FY26\PI3

Each dependency is stated as **Problem** (why it blocks) + **Acceptance criteria** (what "resolved" looks like), per SAFe.

---

### DEP-1 · Obj 4 mandatory attribute population complete (Feature 1517005) — CRITICAL PATH

| Field | Value |
|-------|-------|
| Title | [Dependency] Obj 4 network mandatory attributes populated (1517005) — Feature 1517040 |
| Assigned To | Manuel Vazquez (Obj 4 owner) |
| Priority | 1 |
| State | Open (Obj 4 Feature 1517005, gated Sep 30) |
| Due Date | 2026-09-30 |

**Problem:** Certification attests that mandatory CMDB attributes are populated and correct. For network devices those attributes are populated by **Obj 4 Feature 1517005 (Mandatory Attribute Population via Discovery)**, which gates Sep 30. If 1517005 has not completed, NW-3/NW-5 would certify empty fields discovery was supposed to fill — producing false gaps and an invalid certification. This is the single hardest constraint on the feature.

**Acceptance criteria:**
- [ ] Obj 4 Feature 1517005 confirmed complete — mandatory network attributes populated via discovery, no mandatory fields blank
- [ ] Populated attribute set matches the certification attribute set (DEP-3) — no field certified that discovery does not populate
- [ ] If 1517005 slips: certification scope re-planned (subset of device types where attributes are populated) with PO (Joe Dames) sign-off

---

### DEP-2 · Network devices discovered as CIs (Feature 1516993)

| Field | Value |
|-------|-------|
| Title | [Dependency] Network discovery live — devices exist as CIs (1516993) — Feature 1517040 |
| Assigned To | Manuel Vazquez (Obj 4 owner) |
| Priority | 1 |
| State | Open (Obj 4 Feature 1516993, gated Aug 31) |
| Due Date | 2026-08-31 |

**Problem:** There is nothing to certify until the network devices exist as CMDB records. Obj 4 Feature **1516993** (Automated Credentialed Discovery Live) creates those records and gates Aug 31. NW-1's audit baseline needs the discovered population in place.

**Acceptance criteria:**
- [ ] Obj 4 Feature 1516993 confirmed live — network device CIs created/updated by discovery across the six classes
- [ ] CI population per class available and plausible against the Obj 4 baseline (ties [[PI-3/pi3-nd-1516993-stories-dependencies|DEP-5]] baseline counts)
- [ ] Discovered population is the scope basis for NW-1

---

### DEP-3 · Define the network device mandatory-attribute set (per CMDB governance)

| Field | Value |
|-------|-------|
| Title | [Dependency] Define network device certification attribute set — Feature 1517040 |
| Assigned To | Manuel Vazquez / Josh Sterling (CCB Chair) |
| Priority | 1 |
| State | Open (not in the delivered 2026-07-21 Data Dictionary) |
| Due Date | 2026-09-16 |

**Problem:** The delivered Data Dictionary (2026-07-21) covered Computer / Server / Database / Business Application — **not** network devices. There is no agreed managed/mandatory attribute set for the six network classes to certify against. Without it, NW-1's baseline and NW-3's attestation rules have nothing to measure.

**Acceptance criteria:**
- [ ] Mandatory + recommended attribute set defined for each of the six network device classes, aligned with the Obj 4 "mandatory attributes per CMDB governance" definition
- [ ] Field names confirmed in the live instance per class
- [ ] Set documented as the certification basis and fed into NW-1, NW-2, NW-3, and DEP-5

---

### DEP-4 · Identify / confirm the Network CCB Class Manager (governance owner)

| Field | Value |
|-------|-------|
| Title | [Dependency] Name the Network device CCB Class Manager — Feature 1517040 |
| Assigned To | Joe Dames (PO) / Josh Sterling (CCB Chair) |
| Priority | 2 |
| State | Open (no Class Manager named for network devices) |
| Due Date | 2026-09-16 |

**Problem:** Every other certified class has a named CCB Class Manager (Computers: Monica Green / Paul Becker; Servers & Databases: Ray Reuter; BA: Todd Dierksheide). Network devices have **none**. Without a governance owner there is no one to ratify the attribute set (DEP-3), approve targets, or own attestation routing and escalation in NW-2.

**Acceptance criteria:**
- [ ] Network device CCB Class Manager / governance owner identified and confirmed
- [ ] Owner engaged to ratify the attribute set (DEP-3) and the certification process (NW-2)
- [ ] Attestation routing and escalation path confirmed with that owner

---

### DEP-5 · Data Dictionary CCB approval — Network device attributes

| Field | Value |
|-------|-------|
| Title | [Dependency] CCB approval of network device attribute set — Feature 1517040 |
| Assigned To | Manuel Vazquez / Josh Sterling (CCB Chair) |
| Priority | 2 |
| State | Open (depends on DEP-3, DEP-4) |
| Due Date | 2026-09-23 |

**Problem:** NW-3 configures attestation rules against the network attribute set. Until that set is CCB-approved (which itself needs DEP-3 defined and DEP-4's owner in place), the certified attribute list can change under the team, forcing rework of the PROD build.

**Acceptance criteria:**
- [ ] Network device attribute set (DEP-3) ratified by the Network Class Manager (DEP-4) and approved at CCB
- [ ] Approved set matches the set configured in NW-3 — no drift
- [ ] Approval date and CCB decision referenced in NW-2 / NW-3

---

## Sequence summary

```
                          Obj 4 upstream
DEP-2 (1516993 discovery live, Aug 31) ───────────┐
DEP-1 (1517005 attributes populated, Sep 30) ─────┼── CRITICAL PATH
                                                   │
DEP-3 (define attr set) ─┐                         │
DEP-4 (name Class Mgr) ──┼─► DEP-5 (CCB approve)   │
                         │        │                │
DEP-2 ───────────────────┴─► NW-1 (audit baseline spike, 3.3→3.4)
                                   │
                                   └─► NW-2 (process flow, 3.4)
                                          │
                          DEP-1 ──────────┼─► NW-3 (PROD build, 3.4→3.5)
                          DEP-5 ──────────┘        │
                                                   ├─► NW-4 (dashboard, 3.4→3.5)
                                                   │        │
                                                   └────────┼─► NW-5 (run cycle + monitor, 3.5) ◄── DEP-1
                                                            │
                                                            └─► NW-6 (training, 3.5 → 3.6 IP)
```

**Gate:** CO6 Oct 30 falls after PI-3 ends (Oct 27). Build done by **end of Sprint 3.5 (Oct 13)**; training/validation completes in **3.6 IP (Oct 14–27)**.
**Critical path:** DEP-1 (Obj 4 attribute population, Sep 30) is the binding constraint — this feature has the **least buffer of the four**. If Obj 4 slips, Network certification slips. DEP-3/DEP-4 (attribute set + Class Manager) are net-new governance gaps that must close before the build. Raise all five dependencies at PI Planning; flag Network certification as the highest-risk item in the objective.
