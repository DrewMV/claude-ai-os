---
type: contract-tracker
workspace: Work
project: PPL CMDB-CSDM
contract: CO6 (Change Order #6) — DRAFT / UNSIGNED
updated: 2026-06-20
tags: [work, cmdb-csdm, contract, deliverables, traceability, draft]
---

# CO6 Deliverable Tracker + CO5 Gap-Closure Map

> 🟠 **STATUS: DRAFT — NOT SIGNED.** Source is the **3/27 working draft** ([[Contract/CO6-DRAFT-3.27-unsigned.docx]]).
> Effective date (proposed): **July 1, 2026**. Term: **Jul 1 → Oct 30, 2026**.
> Tracked because it is the **likely re-baselining vehicle** for the CO5 gaps in [[co5-deliverable-tracking]].
> **Treat nothing here as committed scope until executed.** Draft artifacts noted in *Caveats* below.

- **Source contract:** [[Contract/CO6-DRAFT-3.27-unsigned.docx]]
- **Predecessor:** [[co5-deliverable-tracking]] (CO5, signed, term ends 6/30/2026)
- **Fees (draft):** CO6 prof. fees est. **$1,577,072** (excl. travel); totals/team-size left blank in draft.

## Timeline relationship

```
CO5  ──────────────┤ (ends Jun 30)
CO6                 ├────────────────────────────► (Jul 1 – Oct 30)
PI-2  ───────────────────┤ (ends Aug 4)
PI-3                      ├──────────────────────► (Aug 5 – Oct 27)
```

- CO6 spans the **tail of PI-2** (Jul 1 – Aug 4) **+ all of PI-3** (Aug 5 – Oct 27).
- CO6 deliverables due **Jul 31** land in **PI-2 Iter 2.5 / 2.6 (IP)**.
- CO6 deliverables due **Aug 31 / Sep 30 / Oct 30** land in **PI-3**.

> ⚠️ **Signature gap risk:** if CO6 is not executed before **July 1**, the CO5 **June 30 deadline + $533,775 holdback stand with no relief**. **Signature status is itself a critical tracking item.**

---

## CO5 → CO6 Gap-Closure Map (the reason we're tracking this)

| CO5 gap (from [[co5-deliverable-tracking]]) | CO6 deliverable that resolves it | New due date | Effect |
|---|---|---|---|
| **D1.1 Database data dictionary — GAP** | **CMDB Governance** — data dictionary/class attributes incl. **Databases** | **Jul 31** | ✅ Closes the gap (+1 month) |
| **D1.2 Data Cert pilot = BA only; KB docs unowned** | **CMDB Governance** — pilot release for **ALL CI classes** + KB articles | **Jul 31** | ✅ Expands scope |
| **D2.1 Computers 90% coverage — no measurement story** | **CI Coverage – Computers** — coverage validation, 90% managed | **Sep 30** | ✅ Re-baselined w/ realistic date |
| **D2.2 Servers 90% non-NERC-CIP — no measurement story** | **CI Coverage – Servers** — coverage validation, 90% | **Oct 30** | ✅ Re-baselined |
| **D2.3 DB enhanced Discovery (MS-SQL/Oracle)** | **CI Coverage – Servers** — enhanced Discovery MS-SQL & Oracle (same RISK note) | **Jul 31** | ✅ Carried forward |
| **D3 Qualys — BLOCKED, "evaluate" only** | **Qualys Integration** — full one-way Qualys→SNOW, deployed to PROD | **Oct 27** | ✅ Escalates evaluate → operationalize, w/ runway |
| **D1.5 Monthly CCB facilitation + future-PI backlog** | ❌ **Not carried as a CO6 deliverable** (only in CMDB PO role text) | — | 🔴 **Remains a CO5-only obligation** — CCB feature-Removed fix still needed |

> **Bottom line:** CO6 closes **5 of 6** CO5 gaps by re-dating them to Jul 31 → Oct 30. The **CCB/governance-cadence** item is the exception — do not assume CO6 covers it.

---

## CO5 → CO6 Timeline Shift

> How CO6 re-dates each CO5 deliverable. CO5 had a single hard **Jun 30** cliff; CO6 splits it into **two tiers** — foundation work to **Jul 31** (+1 mo) and the hard coverage/integration work to **Sep 30 / Oct 30** (+3–4 mo).

| CO5 Deliverable | CO5 date | CO6 date | Shift | Lands in |
|---|---|---|---|---|
| **D1 Governance** — data dictionary (incl. Databases), Data Cert, ESS-02, SOX | Jun 30 | **Jul 31** | **+1 mo** | PI-2 Iter 2.5/2.6 |
| **D2.1 Computers** — SCCM precedence, bulk life-cycle | Jun 30 | **Jul 31** | **+1 mo** | PI-2 |
| **D2.1 Computers** — 90% coverage validation | Jun 30 | **Sep 30** | **+3 mo** | PI-3 |
| **D2.2 Servers** — SCCM precedence, enhanced DB Discovery | Jun 30 | **Jul 31** | **+1 mo** | PI-2 |
| **D2.2 Servers** — 90% non-NERC-CIP coverage | Jun 30 | **Oct 30** | **+4 mo** | PI-3 |
| **D3 Qualys** (was "evaluate" only) | Jun 30 | **Oct 27** | **+4 mo** + scope ⬆️ | PI-3 |
| **D1.5 Monthly CCB** | Jun 30 | *(none)* | **No relief — stays CO5** | CO5 only |

**Two gates on whether this relief is real:**
1. 🔴 **Signature before July 1.** Unsigned ⇒ every row above snaps back to the **Jun 30** CO5 deadline.
2. 🔴 **$533,775 holdback unresolved.** CO5 ties the holdback to *final acceptance of CO5 deliverables*; the CO6 draft re-dates those deliverables but **does not state what happens to the holdback** (fee table blank). Confirm whether signing CO6 **releases** it or leaves it pinned to a 6/30 acceptance that won't occur.

---

## CO6 Deliverables (draft — all 9)

> Acceptance dates are **staged** (monthly) for the discovery/mapping/coverage items.

| # | Deliverable | Key acceptance criteria | Due | PI | Existing work / stories |
|---|-------------|-------------------------|-----|----|--------------------------|
| 1 | **Network Gear Discovery** | Creds configured/validated (excl. OT); schedules active; mandatory attrs populated; **90% coverage** (business-owner validated) | Aug 31 → **Oct 30** | PI-3 | PI-2 Obj 1 features **1356646** (Network Device Coverage), stories 1402572/574/575; dep 1383487 |
| 2 | **Service Mapping** | Maps for **10 priority business apps** to infra CIs; owner-validated; consumable in SNOW | Aug 31 → **Oct 30** | PI-3 | PI-2 Obj 3 — Wave features **1355866/1355868/1355871**; per-app stories (WATT, Oceana, SolarWinds PoC 1431652, etc.) |
| 3a | **Qualys Integration** | One-way Qualys→SNOW fully configured/tested/**deployed to PROD**; vuln data ingests on schedule, no loss | **Oct 27** | PI-3 | Stream C — **1428703/1428704** (currently BLOCKED), spike 1234585, issue 1465952 |
| 3b | **CMDB Governance** *(dup. #3 in draft)* | Data dictionary incl. **Databases**; Data Cert pilot **all CI classes** + KB; **ESS-02**; **SOX** BA review (not NERC/CIP) | **Jul 31** | PI-2 | CO5 D1 work continues — Data Cert (1247179/1402727/1402958…), ESS-02 spike 1420244, SOX 1438967/1455827 |
| 4 | **CI Coverage – Computers** | SCCM/Discovery precedence; bulk life-cycle (Asset Mgmt-defined); **90% managed** | Jul 31 → **Sep 30** | PI-2/3 | SCCM Computer Class 1348712/16/17/15; Computer Class 1354794 |
| 5 | **CI Coverage – Servers** | SCCM/Discovery precedence; **enhanced DB Discovery MS-SQL/Oracle**; **90%** computers + non-NERC-CIP servers | Jul 31 → **Oct 30** | PI-2/3 | SCCM Server Class 1356826 (1403759/60/62/63); creds 1444864 |
| 6 | **Legacy Platform Rationalization** | Analysis + migration plan for **iTeam → DISCO/Cherwell → AIM** (Cherwell/AIM only "if applicable at PI-3 planning") | Aug 31 → **Oct 30** | PI-3 | iTeam import **1452028**; ties to Ray's 450-server app↔server gap (Risk #13) |
| 7 | **ITSM Product Management** | ITSM PO role — stakeholder mgmt, backlog prioritization, agile ceremonies, governance | Jul 31 → Oct 30 (monthly) | PI-2/3 | 🆕 **New ITSM workstream** — outside CMDB; owner TBD (Joe? new hire?) |
| 8 | **ATF Strategy** | Plan for Automated Test Framework rollout across in-prod SNOW capabilities (criteria, timeline, approach) | **Oct 31** | PI-3 | 🆕 No existing stories |
| 9 | **Platform Support** | Dedicated BAU team (size **TBD/"XXX"**); time-tracking per sprint; **40 hrs stories/wk per member**; excl. <40hr enhancements | Aug 31 → Oct 30 (monthly) | PI-3 | 🆕 **New BAU/DevOps workstream** — not project-based |

---

## New CO6 Deliverables (net-new scope — no CO5 antecedent)

> Distinguishes **net-new** CO6 deliverables from the ones that merely **re-baseline** CO5 items (those are in the gap-closure map above). Net-new = brand-new contractual obligations to plan, staff, and story-out — mostly at **PI-3 planning**.

| # | CO6 Deliverable | Net-new? | Why | Story status today |
|---|-----------------|----------|-----|--------------------|
| 1 | **Network Gear Discovery** | 🆕 **NEW as a deliverable** | Was PI-2 *objective* (Obj 1), never a contracted CO5 deliverable | PI-2 stories exist (1356646, 1402572/574/575) but not contracted/accepted |
| 2 | **Service Mapping** | 🆕 **NEW as a deliverable** | Was PI-2 *objective* (Obj 3); CO6 sets a hard **10-priority-app** target | Wave features + per-app stories exist; no 10-app acceptance defined |
| 3a | Qualys Integration | ⬆️ Not new — **escalated** | Continues CO5 D3 (evaluate → full PROD) | 1428703/1428704 (blocked) |
| 3b | CMDB Governance | 🔁 Not new — **re-baselined** | Continues CO5 D1 | see CO5 acceptance tracking |
| 4 | CI Coverage – Computers | 🔁 Not new — **re-baselined** | Continues CO5 D2.1 | — |
| 5 | CI Coverage – Servers | 🔁 Not new — **re-baselined** | Continues CO5 D2.2/2.3 | — |
| 6 | **Legacy Platform Rationalization** | 🆕 **NEW** | Analysis + migration plan for **iTeam / DISCO / Cherwell / AIM** | Only iTeam import 1452028; ties to Ray's 450-server gap (Risk #13). No analysis/plan stories |
| 7 | **ITSM Product Management** | 🆕 **NEW workstream** | New **ITSM PO** role (#26) — outside CMDB | No stories; owner TBD (ties to CR6 role segmentation w/ Aaron Simeon) |
| 8 | **ATF Strategy** | 🆕 **NEW** | Automated Test Framework rollout plan | No stories |
| 9 | **Platform Support** | 🆕 **NEW workstream** | Dedicated **BAU/DevOps** team, 40 hrs/wk per member | No stories; team size "XXX" placeholder in draft |

> **6 net-new deliverables** (#1, #2, #6, #7, #8, #9). #1/#2 have *story scaffolding* from PI-2 objectives but **no contractual acceptance criteria met**; #6–#9 are **greenfield** — to be planned and staffed at PI-3.
> **Net-new ≠ free:** ITSM PM + Platform Support are **ongoing-capacity** commitments (40 hrs/wk/person), not finite deliverables — they need staffing decisions, not just stories.

---

## Structural changes vs CO5

- 🆕 **ITSM Product Owner** role added (staff #26) + **ITSM Product Management** deliverable (#7) → engagement broadens beyond CMDB into ITSM.
- 🆕 **Platform Support / BAU** team (#9) → ongoing production support, separate from project delivery.
- 🆕 **ATF Strategy** (#8) → test-automation planning.
- 🆕 **Network Gear Discovery**, **Service Mapping**, **Legacy Platform Rationalization** become **formal contractual deliverables** (in CO5 these were PI objectives, not contracted deliverables).
- Coverage targets move to **staged monthly acceptance** (Aug/Sep/Oct) rather than a single hard date.

---

## Caveats — this is a working draft

- **Unsigned**; signature block erroneously says "Change Order #4."
- **Deliverable numbering duplicated** — two items numbered "3" (Qualys + CMDB Governance).
- **Fee table incomplete** — CO6 row, monthly Jul–Oct fees, totals, and team size ("XXX") all blank/placeholder; carried totals still reflect CO5.
- Filename `_3.27` indicates a **March 27 draft** — newer revisions may exist. **Confirm this is the current version.**
- Effective date July 1, 2026 with an unsigned doc as of today (6/20) ⇒ **~10 days to execute or risk a coverage gap.**

---

## Actions

| # | Action | Owner | Priority |
|---|--------|-------|----------|
| 1 | Confirm CO6 **signature timeline** — must execute before July 1 to avoid CO5 holdback exposure | Manuel → Christian | 🔴 |
| 2 | Confirm this 3/27 draft is the **latest revision**; obtain any newer version | Manuel → Christian | 🔴 |
| 3 | Confirm **CCB/governance cadence** has a contractual home (CO6 doesn't list it as a deliverable) | Manuel → Joe | 🟡 |
| 4 | Identify **ITSM PO** owner + how the new ITSM/BAU/ATF workstreams staff up (ties to CR6 role segmentation w/ Aaron Simeon) | Manuel → Christian | 🟡 |
| 5 | Once signed: build a CO6 deliverable→story matrix at PI-3 planning (most CO6 stories not yet created) | Manuel | 🟡 |
