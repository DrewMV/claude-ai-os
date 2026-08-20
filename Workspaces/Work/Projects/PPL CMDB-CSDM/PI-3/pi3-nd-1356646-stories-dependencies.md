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
updated: 2026-08-05
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
- [ ] Reflects gap closures from CR-3 as they land
- [ ] Reviewed with PO and confirmed as the reporting source for the Oct 30 gate

**Depends on:** CR-1 (denominator), CR-2 (initial gap picture).

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

## Sequence summary

```
CR-1 (denominator, 3.5) ─┬─► CR-2 (gap analysis, 3.5) ─► CR-3 (gap closure, 3.5) ─┐
                          │                                                        │
                          └─► CR-4 (dashboard, 3.5) ◄──────────────────────────────┤
                                                                                    │
                                                              CR-5 (owner sign-off, 3.6 IP) ◄┘
```

**Total points:** 3 + 3 + 5 + 3 + 5 = **19** (CR-3 landed lighter than proposed — recheck at refinement).
**Gate:** CO6 Oct 30 falls after PI-3 close (Oct 27); CR-1–CR-4 must land coverage by end of 3.5 (Oct 13), leaving 3.6 IP (Oct 14–27) as the owner-sign-off buffer before the external date — consistent with [[PI-3/pi3-network-discovery-feature-breakdown]]'s original sequencing.
