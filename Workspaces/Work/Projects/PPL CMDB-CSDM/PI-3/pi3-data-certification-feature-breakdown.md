---
type: feature-breakdown
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
objective: CMDB Data Certification — Four Major CI Classes (deck "Objective 3" = master Obj 3 = CO6 Deliverable #4)
contract: CO6 (Change Order #6)
status: draft
updated: 2026-07-28
tags: [work, cmdb-csdm, safe, pi-planning, co6]
---

# PI-3 — CMDB Data Certification (4 CI Classes): Feature Breakdown

Feature-and-sprint plan for the **Certify CMDB Data Across the Four Major CI Classes** objective, aligned to the acceptance criteria on the PI-3 Objectives deck. Planning input for reconciliation against ADO at PI Planning (Jul 22 – Aug 4). See [[pi3-objectives]] (Obj 3) and [[co6-deliverable-tracking]] (Deliverable #4).

> **Numbering note:** deck **Objective 3** = master [[pi3-objectives]] **Obj 3** = **CO6 v3 Deliverable #4** (CMDB Governance). The objective number and the CO6 deliverable number differ — cite both to avoid confusion.

## Assumptions

- **Gates = the deck's acceptance criteria:** Computers & Servers **Sep 30**; Databases & Network Devices **Oct 27**.
  - ⚠️ **Date reconciliation open:** [[pi3-objectives]] and [[co6-deliverable-tracking]] show Databases & Network Devices at **Oct 30** (contract gate, 3 days after PI-3 ends Oct 27). Deck says Oct 27. Confirm at planning.
- **Sprint cadence** per [[PI-3/Memory]]: 3.1 (Aug 5–18) · 3.2 (Aug 19–Sep 1) · 3.3 (Sep 2–15) · 3.4 (Sep 16–29) · 3.5 (Sep 30–Oct 13) · 3.6 IP (Oct 14–27).
- **Each class = the same 4 artifacts** (per the deck): documented **process flow** + **technical build in PROD** + **tracking dashboards** + **delivered training**. "Certified" = all 4 present for that class.
- **Existing scaffolding = the PI-2 BA pilot pattern.** PI-3 replicates it per class; it does not invent a new process:
  - Pattern features: **1247179** (Pilot – Functionality), **1402958** (Pilot – Implementation Planning), **1402979** (Pilot – Implementation Support), **1382404** (Rollout).
  - Reusable story shapes to clone per class: **1402962** (kick-off/training), **1402976** (execute policies), **1402980** (monitor completeness), **1402984** (office hours), **1402985** (process feedback), **1402727** (dashboard).
  - Per-class gap-remediation carryover spikes: **1480112** (Servers — ✅ CLOSED 7/28), **1480113** (Database — status unconfirmed on PI2.6 view), **1480114** (Computer — ✅ CLOSED 7/28). *(BA spike 1480111 was the pilot; no network audit spike exists yet.)*

## Feature → sprint → acceptance-criteria map

| # | Feature | Maps to AC (gate) | Sprint(s) | Existing ADO anchor | Net-new needed |
|---|---------|-------------------|-----------|---------------------|----------------|
| **E** | Enabler: Close PI-2 carryover ("Lock before planning") | Prereq to all four | pre-PI-3 (PI-2 IP); slips → **3.1** | Data Dictionary 1480097/1480098; audit spikes **1480112 ✅ + 1480114 ✅ CLOSED 7/28** / 1480113 (unconfirmed) | 90%-coverage acceptance stories (Computers G2, Servers G3) |
| **1** | Certify Computers | Row 1: Computers cert (**Sep 30**) | **3.1 → 3.4** | 1480114 (Computer audit spike ✅ CLOSED 7/28) + pilot pattern | 4 artifacts (process / PROD build / dashboards / training) |
| **2** | Certify Servers | Row 1: Servers cert (**Sep 30**) | **3.1 → 3.4** | 1480112 (Servers audit spike) + pilot pattern | 4 artifacts |
| **3** | Certify Databases | Row 2: Databases cert (**Oct 27 / Oct 30**) | **3.3 → 3.5**, sign-off **3.6 IP** | 1480113 (Database audit spike), 1480098 (Data Dictionary: Databases) + pilot pattern | 4 artifacts |
| **4** | Certify Network Devices | Row 2: Network Devices cert (**Oct 27 / Oct 30**) | **3.4 → 3.5**, sign-off **3.6 IP** | pilot pattern (no audit spike yet) | 4 artifacts + audit-dashboard scope spike |

If the team wants fewer work items, Features 1+2 can collapse into one "Certify Computers & Servers (Sep 30)" feature and 3+4 into "Certify Databases & Network Devices (Oct 27/30)" — but per-class keeps each demoable at its own gate and matches the existing per-class audit spikes.

## Feature detail

### Enabler (E) — Close PI-2 carryover · pre-PI-3 (PI-2 IP), or 3.1 if slipped
The deck's "Lock before planning": close these before PI-3 starts or Sprint 3.1 is blocked.
- **Data Dictionary CCB approval** (target Jul 21) — stories 1480097 (BA/App Instances), 1480098 (Databases, closes CO5 gap G1) under Feature 1480087.
- **3 audit-dashboard gap spikes complete** — 1480112 (Servers ✅ CLOSED 7/28), 1480113 (Database — unconfirmed), 1480114 (Computer ✅ CLOSED 7/28). These produce the per-class gap-remediation plans that feed Features 1–3. **2 of 3 confirmed done; Database 1480113 to verify.**
- **90%-coverage acceptance stories** for Computers (G2) and Servers (G3) — *no formal story yet; create and accept.*

### Feature 1 — Certify Computers · Sprints 3.1 → 3.4 · AC row 1 (Sep 30)
Done = Computers class certified end-to-end (process flow, PROD build, dashboards, training).
- **Anchor:** 1480114 (Computer audit-dashboard scope + gap-remediation plan) — ✅ CLOSED 7/28; gap plan available to feed the stories below.
- **Child stories (clone pilot pattern):** document certification process flow (Computers) · technical build to PROD — certification policies/rules (Computers) · tracking dashboards live (Computers) · training delivered to CI owners (Computers).
- **Shape:** 3.1 = process flow off the 1480114 gap plan (test-frozen → no PROD build); 3.2–3.3 = PROD build + dashboards; 3.4 = training. Done end 3.4.

### Feature 2 — Certify Servers · Sprints 3.1 → 3.4 · AC row 1 (Sep 30)
Done = Servers class certified end-to-end.
- **Anchor:** 1480112 (Servers audit-dashboard scope + gap-remediation plan) — ✅ CLOSED 7/28; gap plan available to feed the stories below.
- **Child stories:** process flow (Servers) · PROD build (Servers) · dashboards (Servers) · training (Servers).
- **Shape:** parallel to Computers, 3.1 → 3.4.

### Feature 3 — Certify Databases · Sprints 3.3 → 3.5, sign-off 3.6 IP · AC row 2 (Oct 27 / Oct 30)
Done = Databases class certified end-to-end.
- **Anchor:** 1480113 (Database audit-dashboard scope + gap plan), 1480098 (Data Dictionary: Databases).
- **Child stories:** process flow (Databases) · PROD build (Databases) · dashboards (Databases) · training (Databases).
- **Dependency:** database discovery data quality — the RAID "Oracle visibility / Kentucky" gap threatens the "trustworthy data to certify" precondition. Confirm Oracle discovery is remediated before the build.

### Feature 4 — Certify Network Devices · Sprints 3.4 → 3.5, sign-off 3.6 IP · AC row 2 (Oct 27 / Oct 30)
Done = Network Devices class certified end-to-end.
- **Anchor:** pilot pattern (no network audit spike exists — add one).
- **Child stories:** audit-dashboard scope + gap spike (Network) · process flow (Network) · PROD build (Network) · dashboards (Network) · training (Network).
- **Cross-objective dependency:** certification needs discovered network devices with **populated mandatory attributes** — that is Obj 4 (Network Discovery) Feature 2, gated Sep 30. Network cert therefore starts in 3.4 (after attributes land) and runs into IP.

## Sequencing rationale

- **Sep 30 (Computers + Servers) lands on the 3.4/3.5 boundary** → both must be *done* by end of **3.4** (Sep 29). Run them in parallel 3.1 → 3.4. The **test code freeze through Aug 15** (PI-3 Risk #1) means 3.1 is process-flow documentation off the carryover gap plans — no PROD build until after Aug 15.
- **Oct 27/30 (Databases + Network Devices)** → build 3.3/3.4 → 3.5, reserve **3.6 IP** for training completion and validation sign-off. Databases can start earlier (3.3); Network waits on Obj 4 attributes (3.4).

## Dependencies / risks to flag at PI Planning

1. **PI-2 carryover is the gating risk** — the deck's own "Achievable" caveat. Data Dictionary CCB approval (Jul 21), the 3 audit spikes, and the 90%-coverage stories must close before PI-3, or Features 1–3 Sprint 3.1 start is blocked.
2. **Capacity / scale-up** — the team certified **one** class (BA) across all of PI-2; PI-3 asks for **four**, two by Sep 30. The reusable pilot pattern is the lever, but PROD build + dashboards + training ×4 is heavy. Stress-test velocity at planning; this is the objective most likely to over-commit.
3. **Network Devices cert ← Obj 4** — depends on network mandatory attributes populated (Obj 4, Sep 30). If Obj 4 slips, Feature 4 slips.
4. **Databases cert ← data quality** — Oracle/Kentucky discovery gap (RAID) must be remediated so there is trustworthy data to certify.
5. **No network audit spike yet** — the other three classes have one (1480112/113/114); Network needs an equivalent scope/gap spike created.

## Open reconciliation items

- Confirm **Databases & Network gate date** — Oct 27 (deck) vs. Oct 30 (CO6 contract gate).
- Create the **90%-coverage acceptance stories** (Computers G2, Servers G3) and the **Network audit-dashboard scope spike**.
- Confirm **per-class feature owners** at planning (audit-spike owners: Servers→Anthony, Database/Computer→Stan; pilot build lead→Bhushan).
- Net-new stories above are **proposals** — create in ADO and reconcile IDs back into this table and [[co6-deliverable-tracking]].
