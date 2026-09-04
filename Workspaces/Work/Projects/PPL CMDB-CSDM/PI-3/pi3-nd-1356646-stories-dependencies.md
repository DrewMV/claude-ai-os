---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1356646 — Network Inventory Coverage Reconciliation & Owner Validation (≥90%)"
objective: CO6 Obj 4 — Automate Network Device Discovery in the CMDB
sprint: "3.5 (CR-1..CR-4); 3.6 IP (CR-5)"
co6-due: 2026-10-30
status: reconciled
updated: 2026-09-02
tags: [work, cmdb-csdm, safe, pi-planning, co6, network-discovery]
relationships:
  - target: "[[PI-3/pi3-network-discovery-feature-breakdown]]"
    type: derived_from
  - target: "[[PI-3/pi3-nd-1516993-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-cmdb-csdm-ado-tracking]]"
    type: related_to
  - target: "[[PI-3/pi3-objectives]]"
    type: related_to
---

# Feature 1356646 — Stories & Dependencies

**Network Inventory Coverage Reconciliation & Owner Validation (≥90%)**
Sprint 3.5 (Sep 30–Oct 13) · CR-5 in 3.6 IP · CO6 due Oct 30 · Owner: M. Vazquez

> **Status: RECONCILED (2026-08-05)** — all 5 proposed stories (CR-1..CR-5) created in ADO under Feature 1356646 same day, one point value adjusted at creation (CR-3: 8 proposed → 5 as created). See [[PI-3/pi3-network-discovery-feature-breakdown]] Feature 3 for the plan this was drafted from, and [[PI-3/pi3-nd-1516993-stories-dependencies]] for the parallel Feature 1 (Automated Credentialed Discovery Live) under the same objective.
>
> **Revision 2026-09-02:** CR-4 acceptance criteria refined to pin the dashboard's per-class scope to the exact six Network Gear `sys_class_name` values, closing the Network Controller table-name gap (confirmed `cmdb_ci_network_controller`) — see [[../Config-Mgmt-Plan/data-dictionary-network-gear|data-dictionary-network-gear]] Open Question 4 and [[../Config-Mgmt-Plan/data-dictionary-network-gear-validation|data-dictionary-network-gear-validation]] N6.

---

## CO6 Acceptance Criteria this feature delivers (Oct 30, stretch)

From [[PI-3/pi3-objectives]] — Obj 4 (CO6 §1), AC row 3:

> *≥90% of the expected (authoritative) network inventory represented in CMDB, validated by business owners.*

**Device types in scope:** Routers · Switches · Firewalls · Load Balancers · Wireless Access Points · Network Controllers

---

## ADO item reconciliation note

This feature extends existing pre-PI-3 ADO items rather than starting from zero:

| Existing ADO item | Maps to | Action |
|--------------------|---------|--------|
| 1383487 — coverage denominator dependency | CR-1 | Superseded by CR-1 — confirm closure |
| 1402555 — identify CI classes (spike) | CR-1 | Input to CR-1 |
| 1402559 — compare sources (spike) | CR-1, CR-2 | Input to CR-1 and CR-2 |
| 1402567 — analyze missing devices (spike) | CR-2 | Clones into CR-2 |
| 1402575 — rerun comparison to validate | CR-2 | Clones into CR-2 |

---

## Stories (5)

---

### CR-1 · [User Story] Define the authoritative network device inventory (coverage denominator)

| Field | Value |
|-------|-------|
| ADO ID | **1559163** |
| Type | User Story |
| Parent feature | 1356646 |
| Sprint | 3.5 |
| Points | 3 |
| State | New (confirmed 2026-08-05) |
| Tags | `Network-Discovery` `Coverage` `CO6-Obj4` |

**As** the CMDB Configuration Manager,
**I want** a single authoritative list of expected network devices per class (Routers, Switches, Firewalls, Load Balancers, WAPs, Network Controllers), sourced and validated by business/network owners,
**So that** the ≥90% coverage target has an agreed measurement basis instead of an assumed one.

**Acceptance criteria:**
- [ ] Authoritative device list compiled per class, sourced from network/business owners
- [ ] List reconciled against existing spikes 1402555 (CI class identification) and 1402559 (source comparison)
- [ ] Denominator formally agreed with PO (Joe Dames) and referenced by CR-2 through CR-5
- [ ] Existing dependency 1383487 closed or superseded by this story

**Depends on:** business-owner engagement.

---

### CR-2 · [User Story] Gap analysis — discovered inventory vs. authoritative list

| Field | Value |
|-------|-------|
| ADO ID | **1559166** |
| Type | User Story |
| Parent feature | 1356646 |
| Sprint | 3.5 |
| Points | 3 |
| State | New (confirmed 2026-08-05) |
| Tags | `Network-Discovery` `Coverage` `CO6-Obj4` |

**As** the CMDB Configuration Manager,
**I want** the CMDB's discovered network device inventory compared against the CR-1 authoritative list, per device class,
**So that** missing/undiscovered devices are identified and quantified before gap-closure work is scoped.

**Acceptance criteria:**
- [ ] Discovered-vs-authoritative comparison run for all 6 device classes
- [ ] Gap count and root cause (not-yet-discovered vs. credential/access blocked vs. out-of-scope subnet) captured per class
- [ ] Clones/extends existing items 1402567 (analyze missing) and 1402575 (rerun comparison)
- [ ] Gap list handed off as CR-3's scope

**Depends on:** CR-1 (denominator).

---

### CR-3 · [User Story] Gap closure — expand credential/access/subnet scope for missing devices

| Field | Value |
|-------|-------|
| ADO ID | **1559175** |
| Type | User Story |
| Parent feature | 1356646 |
| Sprint | 3.5 |
| Points | **5** (proposed at 8 — created in ADO at 5; lighter than initially scoped) |
| State | New (confirmed 2026-08-05) |
| Tags | `Network-Discovery` `Coverage` `CO6-Obj4` |

**As** the CMDB Configuration Manager,
**I want** the credential, access, and subnet-scope gaps identified in CR-2 resolved for missing devices,
**So that** previously undiscoverable devices become discoverable and get created in CMDB.

**Acceptance criteria:**
- [ ] Credential/access gaps from CR-2 remediated (ties to the RAID "Incomplete Discovery Coverage" risk — account permissions, Oracle/Kentucky pattern)
- [ ] Subnet scope expanded where gap was "out of scope," coordinated with network team
- [ ] Rerun of discovery shows measurable reduction in the CR-2 gap count
- [ ] Any gap that cannot be closed this PI is documented with cause (not silently dropped from the denominator)

**Depends on:** CR-2; network/security team for credential and subnet-scope changes. **Watch this one** — created at 5 points against a proposal of 8; confirm at refinement whether the lighter estimate reflects a narrower scope or under-estimation of the credential/access remediation work (the deck's own top risk for this objective).

---

### CR-4 · [User Story] Coverage metric dashboard by device class

| Field | Value |
|-------|-------|
| ADO ID | **1559183** |
| Type | User Story |
| Parent feature | 1356646 |
| Sprint | 3.5 |
| Points | 3 |
| State | New (confirmed 2026-08-05) |
| Tags | `Network-Discovery` `Dashboard` `CO6-Obj4` |

**As** the CMDB Process Owner,
**I want** a live dashboard showing CMDB coverage % vs. the authoritative inventory, broken out by device class,
**So that** progress toward ≥90% is visible to the team and stakeholders without manual reporting.

**Acceptance criteria:**
- [ ] Dashboard shows coverage % per class and overall, reading from live CMDB + CR-1 denominator (not a static export)
- [ ] Per-class breakout is scoped by exact `sys_class_name`, covering all six in-scope Network Gear subclasses:
  - Router — `cmdb_ci_ip_router`
  - Switch — `cmdb_ci_ip_switch`
  - Firewall — `cmdb_ci_ip_firewall`
  - Load Balancer — `cmdb_ci_lb`
  - Wireless Access Point — `cmdb_ci_wap`
  - Network Controller — `cmdb_ci_network_controller`
- [ ] Bare parent `cmdb_ci_netgear` excluded from the per-class breakout (exact-class only) — a device must resolve to one of the six leaf classes to count toward its class's bar
- [ ] Per-class list matches CR-1's authoritative-inventory class list exactly — dashboard and denominator can't drift
- [ ] All six classes report on the dashboard — no class deferred or flagged pending
- [ ] Reflects gap closures from CR-3 as they land
- [ ] **Dashboard also tracks the non-discoverable (manual / Data-Certification) governance attributes per class**, per [[../Config-Mgmt-Plan/data-dictionary-network-gear|data-dictionary-network-gear]]: CI Owner (`owned_by`), Technical Owner Group (`managed_by_group`), Support Group (`support_group`), Environment (`environment`), Location (`location`), Value Stream (`business_unit`), Operational Status (`operational_status`), Install Status (`install_status`)
- [ ] Non-discoverable attribute completeness is shown as its own % populated (per class and/or per attribute) — **distinct from** the existence-based coverage % above; a device counting toward ≥90% coverage does not imply its governance attributes are populated, so the two numbers are not conflated
- [ ] Non-discoverable attribute population is sourced from Data Certification records, not Discovery — consistent with the dictionary's data-precedence rule that Discovery cannot overwrite these fields
- [ ] Reconciled with Obj 4 Feature 1517005 (Mandatory Attribute Population via Discovery), specifically story 1537637 (populate non-discoverable mandatory attributes) — this dashboard reports the same gap, not a second, conflicting count
- [ ] Reviewed with PO and confirmed as the reporting source for the Oct 30 gate

**Depends on:** CR-1 (denominator), CR-2 (initial gap picture), Feature 1517005 (non-discoverable attribute population source).

**Note:** the non-discoverable attribute set above is still **DRAFT** — Mandatory designation for each is `[Network Core confirm]` pending sign-off in [[../Config-Mgmt-Plan/data-dictionary-network-gear-validation|data-dictionary-network-gear-validation]] (N9/N2/N10). Dashboard should read the designation from the ratified dictionary, not hardcode Recommended vs. Mandatory ahead of CCB approval. Adding this tracking widens CR-4 beyond pure existence-coverage — **re-point at refinement** (drafted at 3 points against existence-only scope).

---

### CR-5 · [User Story] Business-owner validation and sign-off on ≥90% coverage

| Field | Value |
|-------|-------|
| ADO ID | **1559193** |
| Type | User Story |
| Parent feature | 1356646 |
| Sprint | **3.6 (IP)** — as proposed |
| Points | 5 |
| State | New (confirmed 2026-08-05) |
| Tags | `Network-Discovery` `Validation` `CO6-Obj4` |

**As** the CMDB Configuration Manager,
**I want** business and network owners to validate the reconciled inventory and formally confirm the ≥90% coverage target is met,
**So that** the CO6 Oct 30 acceptance criterion ("≥90% of business-owner-validated device inventory") is signed off, not just measured.

**Acceptance criteria:**
- [ ] CR-4 dashboard shows ≥90% coverage at time of validation
- [ ] Business/network owners formally attest the represented inventory is accurate and complete for their class
- [ ] Any shortfall below 90% documented with cause and remediation plan
- [ ] Sign-off recorded and referenced as the Oct 30 gate evidence

**Depends on:** CR-3 (gap closure), CR-4 (dashboard).

---

### CR-6 · [User Story] Add a "discovered in last week / last month" filter to the coverage dashboard

| Field | Value |
|-------|-------|
| ADO ID | _(net-new — not yet created in ADO)_ |
| Type | User Story |
| Parent feature | 1356646 |
| Sprint | 3.5 (may slip to 3.6 IP if CR-4 lands late in 3.5) |
| Points | _(TBD at refinement)_ |
| State | Draft |
| Tags | `Network-Discovery` `Dashboard` `CO6-Obj4` |

**As** the CMDB Process Owner,
**I want** to filter the coverage dashboard's device list to CIs that Discovery has re-confirmed within the last 7 days or the last 30 days,
**So that** I have a working list of **likely-valid CIs** — devices Discovery has actively seen recently — to use for gap closure and owner validation, instead of trusting every record sitting in CMDB regardless of when it was last confirmed.

**Acceptance criteria:**
- [ ] Dashboard exposes a time-window filter with at least two presets — **Last 7 days** and **Last 30 days**
- [ ] Filter is based on Discovery's **last-scanned / last-confirmed** timestamp, not `sys_created_on` — a CI re-scanned within the window counts as recently confirmed regardless of how long ago it was first created; confirm the exact field with Stan before building
- [ ] Filtered result is the **likely-valid CI list** for that window — the set of devices with recent, positive discovery confirmation
- [ ] CIs **not** seen by Discovery within either window are surfaced as the complementary higher-risk set (not silently dropped) — these are the records most likely stale, decommissioned, or invalid, and are candidates for CR-2/CR-3 gap review
- [ ] Filtered list is usable as an input to **CR-5** (owner validation) — owners validate against the higher-confidence recently-confirmed list rather than the full unfiltered population
- [ ] Applies per device class (same six classes as CR-4) and to the overall total
- [ ] Reviewed with PO (Joe Dames) and confirmed useful for gap triage and owner-validation prep

**Depends on:** CR-4 (dashboard must exist before a filter can be added to it).

**Note:** this is a data-quality triage tool, not a discovery-velocity/trend metric — it separates "confirmed recently, trust it" from "not confirmed recently, verify it" within the existing coverage population. Field-level confirmation (which timestamp = "last confirmed by Discovery") is the one open item before this can be pointed.

---

## Sequence summary

```
CR-1 (denominator, 3.5) ─┬─► CR-2 (gap analysis, 3.5) ─► CR-3 (gap closure, 3.5) ─┐
                          │                                                        │
                          └─► CR-4 (dashboard, 3.5) ◄──────────────────────────────┤
                                    │                                              │
                                    └─► CR-6 (last week/month filter, 3.5/3.6 IP)   │
                                                                                    │
                                                              CR-5 (owner sign-off, 3.6 IP) ◄┘
```

**Total points:** 3 + 3 + 5 + 3 + 5 + TBD(CR-6) = **19 + CR-6** (CR-3 landed lighter than proposed — recheck at refinement; CR-6 not yet pointed).
**Gate:** CO6 Oct 30 falls after PI-3 close (Oct 27); CR-1–CR-4 must land coverage by end of 3.5 (Oct 13), leaving 3.6 IP (Oct 14–27) as the owner-sign-off buffer before the external date — consistent with [[PI-3/pi3-network-discovery-feature-breakdown]]'s original sequencing.
