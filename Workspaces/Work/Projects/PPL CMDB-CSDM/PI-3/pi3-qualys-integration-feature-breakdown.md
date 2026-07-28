---
type: feature-breakdown
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
objective: ServiceNow → Qualys Attribute Sync (deck "Objective 4" = master Obj 2 = CO6 Deliverable #3)
contract: CO6 (Change Order #6)
status: draft
updated: 2026-07-20
tags: [work, cmdb-csdm, safe, pi-planning, co6]
---

# PI-3 — ServiceNow → Qualys Attribute Sync: Feature Breakdown

Feature-and-sprint plan for the **Activate the ServiceNow → Qualys Attribute Sync in Production** objective, aligned to the acceptance criteria on the PI-3 Objectives deck. Planning input for reconciliation against ADO at PI Planning (Jul 22 – Aug 4). See [[pi3-objectives]] (Obj 2) and [[co6-deliverable-tracking]] (Deliverable #3).

> **Numbering note:** deck **Objective 4** = master [[pi3-objectives]] **Obj 2** = **CO6 v3 Deliverable #3** (Qualys Integration). Three different numbers for the same workstream — cite all three.

> **Right-sizing note:** unlike Network Discovery and Data Certification, this is **one integration, one hard gate (Sep 30), three fields**. The correct decomposition is **1 delivery feature + 1 enabler** — not a multi-feature set. Splitting further (e.g., per attribute) would be over-engineering. A build-vs-deploy split into two features is available if the team wants phase-gated tracking, but it is not recommended for a single-gate integration.

## Assumptions

- **Gate = the deck's acceptance criterion:** integration live in PROD with scheduled sync of the 3 fields, 0 manual handoffs — **Sep 30** (single mid-PI gate, no earlier checkpoint).
- **Direction = ServiceNow → Qualys** (one-way): syncs **CI owner, support group, SOX flag** out to Qualys. This is a **re-scope** from the PI-2 read-only framing (Qualys → ServiceNow).
- **Sprint cadence** per [[PI-3/Memory]]: 3.1 (Aug 5–18) · 3.2 (Aug 19–Sep 1) · 3.3 (Sep 2–15) · 3.4 (Sep 16–29) · 3.5 (Sep 30–Oct 13) · 3.6 IP (Oct 14–27).
- **Contingent on the Qualys plug-in** (CO6 dependency clause). Issue 1465952 (plugin replacement) is Closed, but stories 1428703/1428704 never advanced — plug-in availability must be re-confirmed before commit.
- **Existing scaffolding** (PI-2 Stream C, parent feature *"Integration Qualys & ServiceNow (CMDB Data Read Only) (PI2)"*, obj 1366662):
  - **1428703** — Install `x_qual5_itam_nwapp` plugin (Dev/Test/Prod, Part 1) — Stan; still valid.
  - **1428704** — Configure Qualys Integration (Part 2) — Stan; **BLOCKED, old-direction scope → re-scope.**
  - **1234585** — Spike: define/configure data scope + import views in Qualys — Stan; aligns to SN → Qualys; needs parent link.
  - **1465952** — Issue: Qualys plugin replacement awaiting vendor approval — Rich Santillo; **Closed** (confirm landed).
  - **1383519** — Dependency: Qualys Development / Support Team — Rich Santillo (external).

## Feature → sprint → acceptance-criteria map

| # | Feature | Maps to AC (gate) | Sprint(s) | Existing ADO anchor | Net-new needed |
|---|---------|-------------------|-----------|---------------------|----------------|
| **E** | Enabler: Confirm plug-in + re-scope to SN → Qualys ("Lock before planning") | Prereq (contingency) | pre-PI-3 / **3.1** | 1465952, 1383519, 1234585; re-scope 1428703/1428704 | Plug-in go/no-go confirmation |
| **1** | Activate ServiceNow → Qualys Attribute Sync (PROD) | Integration live, scheduled sync of 3 fields, 0 manual handoffs (**Sep 30**) | **3.1 → 3.4** (buffer 3.5/IP) | 1428703 (plugin install), 1234585 (import views), 1428704 (re-scoped config) | Field mapping/transform (owner, support group, SOX flag) · scheduled sync job · test · PROD cutover + validation |

## Feature detail

### Enabler (E) — Confirm plug-in + re-scope · pre-PI-3 (PI-2 IP), or 3.1
The deck's "Lock before planning," and a **hard go/no-go**: if the plug-in isn't available, the objective can't start.
- **Confirm the Qualys plug-in is available/approved** — 1465952 is Closed but stories never advanced; verify with Rich Santillo / Stan that the replacement plugin actually landed. (Dep 1383519 is the external Qualys team.)
- **Re-scope the blocked stories to SN → Qualys** — re-scope 1428704 (config) to the one-way attribute sync; confirm 1428703 (plugin install) still valid; link 1234585 (import views spike) to the feature; **rename the parent feature** (drop "CMDB Data Read Only").

### Feature 1 — Activate ServiceNow → Qualys Attribute Sync (PROD) · Sprints 3.1 → 3.4 · gate Sep 30
Done = one-way SN → Qualys integration configured, tested, live in PROD; owner, support group, and SOX flag auto-synchronized on a defined schedule with zero manual handoffs.
- **Child stories:**
  - *Existing:* 1428703 (install plugin Dev/Test/Prod), 1234585 (data scope + import views in Qualys), 1428704 (re-scoped: configure SN → Qualys attribute sync).
  - *Create:* field mapping/transform for **owner + support group + SOX flag** · scheduled sync job (defined interval) · end-to-end test in non-prod + validate 0 manual handoffs · PROD deploy/cutover + go-live validation.
- **Shape:** 3.1 = enabler + plugin install + field-mapping/schedule design (test-frozen to Aug 15, so no test deploys yet); 3.2 = build config + transform maps + sync job; 3.3 = end-to-end test in non-prod (freeze lifted), validate 0 handoffs; 3.4 = PROD cutover + go-live validation. **Live by Sep 30**; hold 3.5/IP as buffer.

## Sequencing rationale

- **Single hard Sep 30 gate, no earlier checkpoint** → front-load build (3.2) and test (3.3) so PROD cutover (3.4) has buffer before the gate, with 3.5/IP as contingency. There is no recovery room if this slips into October.
- **Test code freeze through Aug 15** (PI-3 Risk #1) → 3.1 is plug-in confirmation + config/mapping design, not test deployments.

## Dependencies / risks to flag at PI Planning

1. **Plug-in availability is the #1 risk** — the deck's red "Achievable" note and "Committed (contingent on plug-in)." 1465952 is Closed but the stories never moved; **re-confirm the plugin landed with Rich Santillo / Stan before committing.** No plug-in → no objective.
2. **Direction re-scope** — 1428704 and the parent feature name are scoped for the old read-only (Qualys → SN) direction. Re-scope to SN → Qualys attribute sync and rename, or the stories build the wrong thing.
3. **Single hard gate, no mid-PI checkpoint** — no recovery room; keep 3.5/IP as buffer.
4. **SOX flag field ↔ SOX governance** — syncing the SOX flag out assumes it is reliably populated on CIs (ties to the Service Instance modify Story B / SOX work). Confirm SOX-flag data quality before syncing it to Qualys.
5. **External vendor dependency (1383519)** — plug-in and Qualys-side import views depend on the Qualys support team (Rich Santillo).

## Open reconciliation items

- Confirm **plug-in availability/approval** landed (Rich Santillo / Stan) — gates the whole objective.
- **Re-scope 1428704** and **rename the parent feature**; link spike 1234585 to the feature.
- Confirm the **3 attributes** and their Qualys-side targets (owner, support group, SOX flag) and the **sync schedule interval**.
- Net-new stories above are **proposals** — create in ADO and reconcile IDs back into this table and [[co6-deliverable-tracking]].
