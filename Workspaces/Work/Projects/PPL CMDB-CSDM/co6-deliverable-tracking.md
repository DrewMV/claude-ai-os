---
type: contract-tracker
workspace: Work
project: PPL CMDB-CSDM
contract: CO6 (Change Order #6) — v3 AUTHORITATIVE
updated: 2026-07-12
tags: [work, cmdb-csdm, contract, deliverables, traceability]
---

# CO6 Deliverable Tracker + CO5 Gap-Closure Map

> ✅ **AUTHORITATIVE SOURCE: CO6 v3** — [[Contract/AP00105-6 to ServiceNow Release 2 and 3 Deployment v3]] (confirmed by Manuel 2026-07-12).
> The earlier **3/27 working draft** ([[Contract/CO6-DRAFT-3.27-unsigned.docx]]) is **SUPERSEDED — do not use for scope.**
> Term: targeted start **June 30, 2026 → complete by October 30, 2026**. Spans the tail of PI-2 + all of PI-3.
> ⚠️ **Signature block in the v3 copy is blank — confirm execution status with Christian** (tracked in Actions).

- **Source contract:** [[Contract/AP00105-6 to ServiceNow Release 2 and 3 Deployment v3]] (authoritative)
- **Superseded draft:** [[Contract/CO6-DRAFT-3.27-unsigned.docx]] (3/27)
- **Predecessor:** [[co5-deliverable-tracking]] (CO5, term ended 6/30/2026)
- **Deliverables:** **9** (v3 — clean numbering; the 3/27 draft's duplicate "#3" is resolved)
- **Fees (v3):** CO6 prof. fees est. **$2,724,109** (excl. travel; expenses not-to-exceed $68,103)
- **Decks built from v3:** [[Contract/CO6-Deliverables-2026-07-12-A-with-extras]] · [[Contract/CO6-Deliverables-2026-07-12-B-pure-sow]]

---

## What changed: 3/27 draft → v3 (authoritative)

| Area | 3/27 draft (superseded) | v3 (authoritative) |
|---|---|---|
| Deliverable count | 10 entries, **two numbered "3"** | **9**, clean 1–9 |
| **Qualys** | one-way **Qualys → ServiceNow** (vulnerability data ingest); due **Oct 27** | one-way **ServiceNow → Qualys** (owner / support-group / **SOX-flag** sync); due **Sep 30** |
| **CI Coverage** (Computers, Servers) | **separate deliverables #4/#5** incl. explicit **90% coverage** | **removed as deliverables** — coverage folds into CMDB Governance data-certification + PI-2 carryover |
| **CMDB Governance** | data dictionary incl. Databases + Data Cert + **ESS-02** + **SOX BA review** | **per-class data certification** (Computers, Servers, Databases, Network Devices); data-dictionary / ESS-02 / SOX-BA-review **not present** |
| **NERC-CIP Strategy** | not present | **NEW deliverable #9** (dual-instance evaluation + executive package) |
| **Legacy Platform** | staged per platform (iTeam Aug 31 / DISCO Sep 30 / Cherwell+AIM Oct 30) | **one 4-platform gap analysis Aug 31**, plan Sep 30, October execution Oct 30 |
| **Platform Support** | team size "XXX" placeholder | **2 BAU/DevOps + 4 major-enhancement developers** |
| **ATF Strategy** | Oct 31 | **Oct 30** |

> 🔴 **v3 addresses FEWER CO5 gaps than the 3/27 draft did.** Absent anywhere in v3 (paragraphs + tables): **data dictionary / class attributes**, **ESS-02**, **SOX BA review** (SOX appears only as the Qualys SOX-flag sync), explicit **90% coverage for Computers & Servers**, and **enhanced DB Discovery (MS-SQL/Oracle)**. If these remain PPL expectations — especially for **CO5 acceptance / the $533,775 holdback** — they need a contractual home. **Confirm with Christian / Joe.** See *v3 scope gaps* below.

---

## Timeline relationship

```
CO5  ──────────────┤ (ended Jun 30)
CO6                 ├────────────────────────────► (Jun 30 – Oct 30)
PI-2  ───────────────────┤ (ends Aug 4)
PI-3                      ├──────────────────────► (Aug 5 – Oct 27)
```

- CO6 spans the **tail of PI-2** (to Aug 4) **+ all of PI-3** (Aug 5 – Oct 27).
- Earliest gates: **Jul 31** — ITSM Product Management + Platform Support monthly lanes begin (PI-2 tail).
- **Aug 31 / Sep 30** gates land in **PI-3**.
- **Oct 30** final gates land **~3 days after PI-3 ends (Oct 27)** → the IP iteration / post-PI-3 tail. Plan Oct-30 acceptance into the final sprint.

---

## CO5 → CO6 Gap-Closure Map (v3)

> How the authoritative v3 addresses each CO5 gap. **Several CO5 items no longer have an explicit CO6 contractual home** — flagged below.

| CO5 gap (from [[co5-deliverable-tracking]]) | v3 CO6 deliverable that addresses it | Due | Effect |
|---|---|---|---|
| **D1.1 Database data dictionary — GAP** | CMDB Governance — *data certification for Databases* (no explicit data-dictionary AC in v3) | Oct 30 | ⚠️ **Partial** — certification, not a data-dictionary deliverable |
| **D1.2 Data Cert (BA only) + KB docs** | CMDB Governance — **per-class data certification** (Computers, Servers, Databases, Network) w/ process, PROD build, dashboards, training | Sep 30 / Oct 30 | ✅ Expands to 4 CI classes (KB articles not an explicit v3 AC) |
| **D2.1 Computers 90% coverage** | *Not an explicit v3 deliverable* — folds into data cert + PI-2 carryover (G2) | — | 🔴 **No dedicated 90% deliverable in v3** |
| **D2.2 Servers 90% non-NERC-CIP** | *Not an explicit v3 deliverable* — PI-2 carryover (G3) | — | 🔴 **Same — no v3 home** |
| **D2.3 DB enhanced Discovery (MS-SQL/Oracle)** | *Not present in v3* (was in the 3/27 draft) | — | 🔴 **Dropped from v3 — confirm** |
| **D3 Qualys — BLOCKED, "evaluate" only** | **Qualys Integration** — one-way **ServiceNow → Qualys** owner/support-group/SOX-flag sync, live in PROD | Sep 30 | 🔁 Continues, but **scope pivoted** (attribute sync, not vuln ingest) |
| **D1.5 Monthly CCB + future-PI backlog** | ❌ Not a CO6 deliverable | — | 🔴 **Remains a CO5-only obligation** |

> **Bottom line:** v3 firmly covers **Data Certification (4 classes)** and **Qualys (re-scoped)**, but the **90% coverage** goals, **enhanced DB discovery**, **data dictionary**, **ESS-02**, **SOX BA review**, and **monthly CCB** do **not** have explicit v3 acceptance criteria. Treat these as **open CO5-acceptance risks**, not "closed by CO6."

---

## CO6 v3 Deliverables (all 9)

> Acceptance dates are **staged** for the discovery / mapping / coverage items. Numbering per v3.

| # | Deliverable | Key acceptance criteria (v3) | Due | PI | Existing work / stories |
|---|-------------|------------------------------|-----|----|--------------------------|
| 1 | **Network Gear Discovery** | Device types discovered w/ validated creds (no failed auth) + schedules active (Aug 31); mandatory attrs populated (Sep 30); **90% coverage** business-owner validated (Oct 30) | Aug 31 → **Oct 30** | PI-3 | feat **1356646**, stories 1402572/574/575; creds 1444864/1459721; dep 1383487 |
| 2 | **Service Mapping** | **15 Silver-tier** app→infra maps + **≥75% business-service inventory** (Aug 31); Gold-tier service→app maps + Silver validation (Sep 30); remaining Silver + service→app (Oct 30) | Aug 31 → **Oct 30** | PI-3 | Wave features **1355866/1355868/1355871**; per-app WATT, Oceana, SolarWinds PoC 1431652. *Assumes business services pre-defined* |
| 3 | **Qualys Integration** | One-way **ServiceNow → Qualys** (owner, support group, SOX flag) fully configured/tested/**live in PROD**, scheduled sync, no manual handoffs | **Sep 30** | PI-3 | **1428703/1428704** (BLOCKED), spike 1234585, issue 1465952 — ⚠️ confirm stories match the **SN→Qualys** direction |
| 4 | **CMDB Governance** | **Data certification** (process + PROD build + dashboards + training) for **Computers & Servers** (Sep 30); **Databases & Network Devices** (Oct 30) | Sep 30 → **Oct 30** | PI-3 | Data Cert 1247179/1402727/1402958/1435307; audit spikes 1480112/1480113/1480114 |
| 5 | **Legacy Platform Rationalization** | **4-platform gap analysis** (iTeam, DISCO, Cherwell, AIM) vs. ServiceNow, PPL docs validated (Aug 31); migration plan + roadmap (Sep 30); October execution (Oct 30) | Aug 31 → **Oct 30** | PI-3 | iTeam import **1452028**; no analysis/plan stories yet |
| 6 | **ITSM Product Management** | ITSM PO activities each period — stakeholder engagement, backlog prioritization in ceremonies, cross-functional coordination, governance forums | **Monthly** Jul 31 → Oct 30 | PI-2/3 | 🆕 workstream — owner TBD |
| 7 | **ATF Strategy** | Published ATF implementation plan for all prod capabilities in use as of Jul 31 — coverage criteria, sequenced rollout timeline, reusable approach | **Oct 30** | PI-3 | 🆕 no stories |
| 8 | **Platform Support** | Time/effort tracking operational; **2 BAU/DevOps + 4 major-enhancement devs**; each member **40 hrs of completed stories/week** (PTO-adjusted); allocation reports | **Monthly** Jul 31 → Oct 30 | PI-2/3 | 🆕 BAU/DevOps workstream |
| 9 | **NERC-CIP ServiceNow Platform Strategy** | Dual-instance **evaluation** (considerations, pros/cons, risks, deps) (Sep 30); **executive strategy package** (options, tradeoffs, high-level steps) (Oct 30) | Sep 30 → **Oct 30** | PI-3 | 🆕 no stories; leadership deliverable |

---

## Net-new vs. continuing (v3)

| # | v3 Deliverable | Net-new? | Notes |
|---|-----------------|----------|-------|
| 1 | Network Gear Discovery | 🆕 NEW as a deliverable | Was PI-2 Obj 1; story scaffolding exists |
| 2 | Service Mapping | 🆕 NEW as a deliverable | Was PI-2 Obj 3; v3 sets 15 Silver + Gold + 75% targets |
| 3 | Qualys Integration | 🔁 Continues — **re-scoped** | CO5 D3 → v3 SN→Qualys attribute sync (direction changed) |
| 4 | CMDB Governance | 🔁 Continues — **re-focused** | CO5 D1 → v3 per-class data certification (drops dictionary/ESS-02/SOX-BA) |
| 5 | Legacy Platform Rationalization | 🆕 NEW | Only iTeam import 1452028 today |
| 6 | ITSM Product Management | 🆕 NEW workstream | ITSM PO role — outside CMDB |
| 7 | ATF Strategy | 🆕 NEW | Greenfield |
| 8 | Platform Support | 🆕 NEW workstream | 2 BAU + 4 enhancement devs |
| 9 | NERC-CIP Platform Strategy | 🆕 NEW | Leadership strategy deliverable |

> **7 net-new / re-scoped** deliverables; only **Data Certification** and **Qualys** clearly continue CO5 threads. ITSM PM + Platform Support are **ongoing-capacity** commitments (40 hrs/wk/person), not finite deliverables — they need staffing, not just stories.

---

## v3 scope gaps vs. CO5 (open risks)

> Items PPL may still expect that have **no explicit v3 acceptance criteria**. Each is a potential CO5-acceptance / holdback exposure.

| Expectation | In CO5? | In 3/27 draft? | In v3? | Action |
|---|---|---|---|---|
| Data dictionary / class attributes | ✅ (D1.1) | ✅ | ❌ | Confirm where it lives (data-cert scope? side note?) |
| ESS-02 alignment | ✅ (D1.3) | ✅ | ❌ | Confirm with Jason Dubreuil / Joe |
| SOX BA review (governance) | ✅ (D1.4) | ✅ | ❌ (SOX only as Qualys flag) | Confirm SOX governance obligation |
| Computers/Servers 90% coverage | ✅ (D2) | ✅ | ❌ | Carryover (G2/G3) — no v3 deliverable |
| Enhanced DB Discovery (MS-SQL/Oracle) | ✅ (D2.3) | ✅ | ❌ | Confirm — dropped from v3 |
| Monthly CCB facilitation | ✅ (D1.5) | ❌ | ❌ | Remains CO5-only |

---

## Caveats — v3

- **Signature block is blank** in the v3 copy — v3 is the authoritative *scope* but confirm it is **executed**.
- **Qualys direction changed** vs. the 3/27 draft (now ServiceNow → Qualys attribute sync). The BLOCKED stories 1428703/1428704 were scoped under the older framing — **verify they match v3** or re-scope.
- **CI Coverage** is no longer a standalone deliverable; the CO5 90%-coverage goals live only as **PI-2 carryover**, not CO6 acceptance.
- Fees $2,724,109 (excl. travel); invoicing table in v3 (not tracked here).

---

## Actions

| # | Action | Owner | Priority |
|---|--------|-------|----------|
| 1 | Confirm **v3 execution/signature** status (blank signature block in the copy) | Manuel → Christian | 🔴 |
| 2 | Confirm the **CO5 scope gaps** (data dictionary, ESS-02, SOX BA review, 90% coverage, DB discovery) have a home — CO5 acceptance / holdback exposure | Manuel → Christian / Joe | 🔴 |
| 3 | Verify Qualys stories **1428703/1428704** match the v3 **SN→Qualys** direction or re-scope | Manuel → Stan | 🟡 |
| 4 | Confirm **CCB/governance cadence** contractual home (not a v3 deliverable) | Manuel → Joe | 🟡 |
| 5 | Identify **ITSM PO** owner + staffing for ITSM / Platform Support / ATF / NERC-CIP workstreams | Manuel → Christian | 🟡 |
| 6 | Build CO6 deliverable→story matrix at PI-3 planning (most CO6 stories not yet created) | Manuel | 🟡 |
