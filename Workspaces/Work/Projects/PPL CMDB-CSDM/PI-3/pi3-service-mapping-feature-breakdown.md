---
type: feature-breakdown
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
objective: Build & Validate Service Maps for Priority Business Apps (deck "Objective 2" = master Obj 5 = CO6 Deliverable #2)
contract: CO6 (Change Order #6)
status: draft
updated: 2026-07-20
tags: [work, cmdb-csdm, safe, pi-planning, co6]
---

# PI-3 — Service Maps for Priority Business Apps: Feature Breakdown

Feature-and-sprint plan for the **Build & Validate Service Maps for Priority Business Apps** objective, aligned to the acceptance gates on the PI-3 Objectives deck (Jul 12 v). Planning input for reconciliation against ADO at PI Planning (Jul 22 – Aug 4). See [[pi3-objectives]] (Obj 5) and [[co6-deliverable-tracking]] (Deliverable #2).

> **Numbering note:** the **Jul 12 deck** labels this **Objective 2** (the earlier Jul 11 draft had it as Objective 5). Master [[pi3-objectives]] lists it as **Obj 5**; it is **CO6 v3 Deliverable #2** (Service Mapping). Cite the CO6 deliverable # to stay unambiguous.

## Assumptions

- **Gates = the deck's acceptance gates:**
  - **Aug 31** — 15 Silver-tier apps mapped (business app → infrastructure), owner-validated, teams enabled + **≥75% of business-service inventory** represented, owner-validated
  - **Sep 30** — Gold-tier maps (business service → business app), owner-validated, teams enabled + an additional validation pass on the 15 Silver
  - **Oct 27** — remaining **Contractor-managed** Silver-tier maps (app → infra) + Silver-tier maps at the **service → app** layer
- **Two map layers:** *app → infra* (Silver, Aug 31) and *service → app* (Gold Sep 30; all Silver Oct 27).
- **Date note:** the Jul 12 deck sets the final gate at **Oct 27** (= PI-3 end / IP iteration end). The CO6 contract gate is **Oct 30** (3 days later) — plan final sign-off into IP with that tail in mind.
- **App-owner availability is the HARD entry criterion** — CO6 assumes business services are defined pre-start; the deck marks this the objective's **highest risk** and says secure the app-owner list **before Aug 5**.
- **Commit-vs-stretch (deck guidance):** commit **8–10 Silver** as the Aug 31 gate; treat **full 15 + Gold** as stretch. This plan adopts that hedge.
- **Relevance:** faster incident triage and change-impact assessment; lower MTTR.
- **Sprint cadence** per [[PI-3/Memory]]: 3.1 (Aug 5–18) · 3.2 (Aug 19–Sep 1) · 3.3 (Sep 2–15) · 3.4 (Sep 16–29) · 3.5 (Sep 30–Oct 13) · 3.6 IP (Oct 14–27).
- **Existing scaffolding** (PI-2 obj 1366660):
  - Wave features **1355866** (Wave 17&18), **1355868** (Wave 19&20), **1355871** (Wave 20&21). *(Removed: 1355872/73/75.)*
  - Per-app story pattern **Gather → Build → Validate → Publish** — e.g. WATT (1281161), Oceana (1281189), Einstein (1400696), Vault Inspection (1400703), + 8 net-new apps (Gentec, Cascade, EViews, etc.).
  - Discovery-method work: **1326754** (endpoint-based discovery eval), **1431652** (SolarWinds PoC), **1420634** (migrated-apps impact), dep **1383493** (endpoint credentials).

## Feature → sprint → acceptance-gate map

| # | Feature | Maps to gate | Sprint(s) | Existing ADO anchor | Net-new needed |
|---|---------|--------------|-----------|---------------------|----------------|
| **E** | Enabler: Secure app-owner list + tier apps + confirm discovery method ("Lock before planning") | Hard entry criterion (before Aug 5) | pre-PI-3 / **3.1** | 1326754, 1431652, 1420634, dep 1383493 | Silver/Gold tier app lists; app-owner commitments |
| **1** | Silver-Tier Service Maps (app → infra) + ≥75% Business-Service Inventory | **Aug 31** — 15 Silver (commit 8–10) + ≥75% inventory | **3.1 → 3.2** | Wave 1355866 + per-app stories (WATT/Oceana/Einstein/…) | Re-tier to Silver; map + owner-validate committed batch; inventory reconciliation |
| **2** | Gold-Tier Service Maps (service → app) + Silver Validation Pass | **Sep 30** — Gold service→app + 15 Silver re-validation | **3.2 → 3.4** | Wave 1355868 rollover | Gold tier list; service→app maps; Silver validation pass |
| **3** | Remaining Contractor-Managed Silver (app → infra) + All-Silver service → app Layer | **Oct 27** — remaining Contractor-managed Silver + Silver service→app | **3.4 → 3.5**, sign-off **3.6 IP** | Wave 1355871 rollover | Remaining Silver maps; service→app layer for all Silver |

The existing Waves are the PI-2 vehicle — for PI-3, re-tier their apps into Silver/Gold and re-parent the per-app stories under these gate-features.

## Feature detail

### Enabler (E) — Secure app-owner list + tier apps + confirm discovery method · before Aug 5 / 3.1
The deck's "Lock before planning," and a **hard entry criterion** — the objective's top risk.
- **Secure the app-owner list** for Silver/Gold-tier apps (owner: Tanzeel / Joe Dames). Without committed owners to validate maps, the Aug 31 gate is at risk from day one.
- **Confirm business services are defined pre-start** (CO6 assumption).
- **Lock the Silver/Gold tier app lists** — which apps count toward "15 Silver," "Gold-tier," and the ≥75% inventory denominator.
- **Confirm the discovery method** — close the endpoint-based vs. pattern-based question (1326754, 1431652 SolarWinds PoC) and migrated-apps impact (1420634).

### Feature 1 — Silver-Tier Service Maps (app → infra) + ≥75% Inventory · Sprints 3.1 → 3.2 · gate Aug 31
Done = committed Silver batch mapped app→infra, owner-validated, teams enabled; ≥75% of business-service inventory represented and owner-validated.
- **Scope hedge:** commit **8–10 Silver**; stretch to **15**.
- **Anchor:** Wave 1355866 + per-app stories; apply Gather → Build → Validate → Publish per app.
- **Shape:** 3.1 = owner engagement + Gather/Build for the committed batch (discovery-side, works under the test freeze); 3.2 = Validate/Publish + owner sign-off + inventory reconciliation to ≥75%. Done by Aug 31.

### Feature 2 — Gold-Tier Service Maps (service → app) + Silver Validation Pass · Sprints 3.2 → 3.4 · gate Sep 30
Done = Gold-tier apps mapped service→app, owner-validated, teams enabled; the 15 Silver get an additional validation pass.
- **Anchor:** Wave 1355868 rollover; same per-app pattern at the service→app layer.
- **Shape:** 3.2–3.3 = Gold service→app builds; 3.4 = Silver re-validation pass + Gold sign-off. Done by end 3.4.

### Feature 3 — Remaining Contractor-Managed Silver + All-Silver service → app Layer · Sprints 3.4 → 3.5, sign-off 3.6 IP · gate Oct 27
Done = remaining Contractor-managed Silver apps complete (app→infra); all Silver apps have the service→app layer built and validated.
- **Anchor:** Wave 1355871 rollover.
- **Shape:** 3.4–3.5 = remaining Contractor-managed Silver (app→infra) + service→app layer for all Silver; 3.6 IP = validation sign-off. Deck gate Oct 27; CO6 contract gate Oct 30 (3-day tail).

## Sequencing rationale

- **Aug 31 lands in Sprint 3.2** → committed Silver batch done by end of 3.2. The **app-owner list must be secured before Aug 5** (enabler) or 3.1 can't start map validation. The **test code freeze through Aug 15** favors front-loading Gather/Build (discovery-side) in 3.1 and Validate/Publish in 3.2.
- **Sep 30 (Gold + Silver validation)** → build 3.2–3.3, validate 3.4.
- **Oct 27 (remaining Contractor Silver + all-Silver service→app)** → 3.4–3.5, sign-off in 3.6 IP (with the Oct 30 contract tail in mind).

## Dependencies / risks to flag at PI Planning

1. **App-owner availability is the highest risk** (deck) — CO6 assumes business services defined pre-start. No committed owners → no validation → the whole gate arc slips. This is the reason to commit 8–10, not 15, at Aug 31.
2. **Tier definition** — "15 Silver," "Gold-tier," and the ≥75% inventory denominator must be pinned down at planning or the gates are unmeasurable.
3. **Discovery method unsettled** — endpoint-based vs. pattern-based (1326754, 1431652 PoC); pick before scaling map builds.
4. **Migrated-apps impact (1420634)** — Airlift/migration churn can invalidate maps mid-flight; sequence around migration waves.
5. **Capacity + ownership shift** — Service Mapping delivery moved Tanzeel → Bhushan/Vinay; confirm capacity for parallel Silver + Gold builds.

## Open reconciliation items

- Confirm the **Silver/Gold tier app lists** and the **≥75% inventory denominator**.
- Confirm **committed vs. stretch** scope for Aug 31 (8–10 vs. 15).
- Confirm the **final gate date** — deck Oct 27 (PI/IP end) vs. CO6 contract gate Oct 30.
- Re-tier existing Wave apps (1355866/68/71) into Silver/Gold and re-parent under Features 1–3.
- Net-new stories above are **proposals** — create in ADO and reconcile IDs back into this table and [[co6-deliverable-tracking]].
