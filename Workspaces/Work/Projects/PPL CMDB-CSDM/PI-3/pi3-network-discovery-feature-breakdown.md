---
type: feature-breakdown
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
objective: Network Gear Discovery (deck "Objective 1" = CO6 Deliverable #1 = master Obj 4)
contract: CO6 (Change Order #6)
status: draft
updated: 2026-07-20
tags: [work, cmdb-csdm, safe, pi-planning, co6]
---

# PI-3 — Network Device Discovery: Feature Breakdown

Feature-and-sprint plan for the **Automate Network Device Discovery in the CMDB** objective, aligned to the acceptance criteria on the PI-3 Objectives deck. Planning input for reconciliation against ADO at PI Planning (Jul 22 – Aug 4). See [[pi3-objectives]] (Obj 4) and [[co6-deliverable-tracking]] (Deliverable #1).

> **Numbering note:** the PI-3 deck orders this as **Objective 1** (by first gate / delivery priority); the CO6 master list has it as **Obj 4 / Deliverable #1**. Same workstream — Network Gear Discovery (CO6 §1).

## Assumptions

- **Gates = the deck's acceptance criteria:** Aug 31 / Sep 30 / Oct 27.
  - ⚠️ **Date reconciliation open:** [[pi3-objectives]] and [[co6-deliverable-tracking]] show the 90% gate as **Oct 30** (contract gate, 3 days after PI-3 ends Oct 27). Deck says **Oct 27 + "stretch."** Confirm commit vs. stretch at planning.
- **Sprint cadence** per [[PI-3/Memory]]: 3.1 (Aug 5–18) · 3.2 (Aug 19–Sep 1) · 3.3 (Sep 2–15) · 3.4 (Sep 16–29) · 3.5 (Sep 30–Oct 13) · 3.6 IP (Oct 14–27).
- **Existing ADO home:** Feature **1356646** ("Network Device Coverage Reconciliation - Group 1") with credential, discovery-config, and reconciliation stories already created. This plan **extends** it — it does not create a parallel feature set. Re-parenting proposed below.
- **Device types in scope (CO6 §1):** Routers, Switches, Firewalls, Load Balancers, Wireless Access Points, Network Controllers.

## Feature → sprint → acceptance-criteria map

| # | Feature | Maps to AC (gate) | Sprint(s) | Existing ADO anchor | Net-new needed |
|---|---------|-------------------|-----------|---------------------|----------------|
| **E** | Enabler: Credential proof + coverage denominator ("Lock before planning") | Prereq to AC1 & AC3 | **3.1** | 1383487; spikes 1402555 / 1402559 / 1402567; 1459721 (SNMP/MID pilot) | Pilot-subnet 0-failed-auth proof; denominator sign-off |
| **1** | Automated Credentialed Discovery Live — all 6 device types, scheduled, auto-updating | AC row 1: validated creds / 0 failed auth **+** schedules on intervals + CMDB auto-updated each cycle (**Aug 31**) | **3.1 → 3.2** | 1444864, 1459721, 1402572, 1402574 (re-parent from 1356646) | Scheduling + auto-update-per-cycle stories |
| **2** | Mandatory Attribute Population via Discovery — no mandatory field blank | AC row 2: all mandatory attributes populated (**Sep 30**) | **3.3 → 3.4** | — | Attribute mapping + blank-remediation per device type |
| **3** | Network Inventory Coverage Reconciliation & Owner Validation (≥90%) | AC row 3: ≥90% vs owner-validated inventory (**Oct 27 / Oct 30, stretch**) | **3.4 → 3.5**, validate in **3.6 (IP)** | **1356646** itself, 1402575, 1402567, 1402559 | Gap-closure + business-owner validation sign-off |

**Re-parenting:** move 1356646's credential/config stories (1444864, 1459721, 1402572, 1402574) up to **Feature 1**; leave 1356646 as the spine of **Feature 3** (its literal name is coverage reconciliation). If the team wants fewer work items, Feature 1's two threads (creds/discovery + scheduling) can stay one feature — both are Aug 31 — or split per bullet.

## Feature detail

### Enabler (E) — Credential proof + coverage denominator · Sprint 3.1
The deck's "Lock before planning" box. Must clear before committing the Aug 31 and 90% gates.
- **Prove credential distribution on a pilot subnet** — 0 failed auth on a representative sample of all 6 device types. (Existing: 1459721 SNMP/MID pilot; credential child tasks under 1444864.)
- **Define the coverage denominator** — the authoritative device list the 90% is measured against, sourced/validated by business owners. (Existing: dependency 1383487; spikes 1402555 identify CI classes, 1402559 compare sources, 1402567 analyze missing devices.)
- **Why 3.1:** fits the **test code freeze through Aug 15** — this is discovery/MID-side config + business engagement, no test deployments required.

### Feature 1 — Automated Credentialed Discovery Live · Sprints 3.1 → 3.2 · AC row 1 (Aug 31)
Done = all 6 device types discovering with validated credentials (no failed auth), on active schedules, CMDB auto-updating each cycle with no manual intervention.
- **Thread A (creds + discovery):** 1444864 (fix creds), 1459721 (SNMP/MID), 1402572 (adjust discovery config), 1402574 (adjust device config).
- **Thread B (scheduling) — net-new:** define discovery schedules per device type on defined intervals; confirm auto-update each cycle with no manual step; validate 0 failed auth at scale across all 6 types.
- **Gate:** Aug 31 lands inside Sprint 3.2 → both threads *done* by end of 3.2.

### Feature 2 — Mandatory Attribute Population via Discovery · Sprints 3.3 → 3.4 · AC row 2 (Sep 30)
Done = every mandatory CMDB attribute (per governance) populated via discovery for each device type; no mandatory field blank.
- **Net-new stories:** confirm the mandatory-attribute set for Network Devices (per governance); map discovery output → attributes per device type; remediate blanks; validate none-blank.
- **Cross-objective dependency:** the mandatory-attribute definition comes from **Obj 3 (CMDB Governance)** / Data Dictionary. Its network-device certification gate is Oct 30 — sequence the *attribute-set definition* early (3.1–3.3) or this Sep 30 gate is blocked.
- **Gate:** Sep 30 sits on the 3.4/3.5 boundary → target completion by end of **3.4** (Sep 29) for buffer.

### Feature 3 — Coverage Reconciliation & Owner Validation (≥90%) · Sprints 3.4 → 3.5, validate 3.6 (IP) · AC row 3 (Oct 27 / Oct 30, stretch)
Done = ≥90% of the expected (authoritative) network inventory represented in CMDB, validated by business owners.
- **Existing:** 1356646 (coverage reconciliation spine), 1402575 (rerun comparison to validate), 1402567 (analyze missing), 1402559 (compare sources).
- **Net-new:** gap analysis discovered vs. authoritative list; gap closure (credential/access/subnet scope); coverage metric/dashboard; business-owner validation & sign-off.
- **Gate:** drive to 90% in **3.5**; reserve **3.6 (IP)** for owner sign-off. This is the stretch — treat as such.

## Sequencing rationale

- **Aug 31 (AC row 1) lands inside Sprint 3.2**, so discovery + scheduling must be *done* by end of 3.2. The **test code freeze through Aug 15** (PI-3 Risk #1) means 3.1 can't rely on test deployments — 3.1 = enabler + discovery/MID-side config; deploy-and-prove-at-scale runs 3.2.
- **Sep 30 (AC row 2)** target end of **3.4** (Sep 29) for buffer.
- **Oct 27/30 (AC row 3)** → 90% in **3.5**, owner validation sign-off in **3.6 (IP)**.

## Dependencies / risks to flag at PI Planning

1. **Credential distribution is the #1 threat** — the deck's own "At risk" note, and the RAID "Incomplete Discovery Coverage" item (account permissions; Oracle/Kentucky). The 3.1 pilot must prove 0-failed-auth on a representative sample of all 6 types before committing the Aug 31 "all types" gate.
2. **AC row 2 ↔ Obj 3 (CMDB Governance) dependency** — "mandatory per governance" needs the Network Device mandatory-attribute set defined (Data Dictionary / per-class certification, network gate Oct 30). If that lags, the Sep 30 gate is blocked. Sequence the attribute-set definition early.
3. **Coverage denominator ("90% of what?")** must be locked in 3.1 via 1383487 + business owners, or AC row 3 is unmeasurable.
4. **Prod upgrade Aug 15 (Australia, PI-3 Risk #2)** — mid-3.1; confirm discovery patterns/probes are unaffected post-upgrade before scaling.

## Open reconciliation items

- Confirm **90% gate date** — Oct 27 (deck, stretch) vs. Oct 30 (CO6 contract gate).
- Confirm **re-parenting** of 1444864 / 1459721 / 1402572 / 1402574 from 1356646 to Feature 1.
- Confirm the **mandatory-attribute set** for Network Devices with governance (Josh Sterling / Adam Gross as Network Gear CI Class Manager).
- Net-new stories above are **proposals** — create in ADO and reconcile IDs back into this table and [[co6-deliverable-tracking]].
