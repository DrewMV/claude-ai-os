---
level: pi
workspace: Work
project: CMDB-CSDM
pi: PI-4
status: future
start: 2026-10-28
end: 2027-02-02
updated: 2026-10-12
tags: [work, safe, pi-planning, cmdb-csdm]
---

## PI Objectives

From the **official ADO objectives and features list as of 2026-10-08** (A-INFOPS\FY26\PI4), realigned to **SOW AP00288** on 2026-10-12. Commitment status is still TBD — set at PI Planning 2026-11-04.

> ⚠️ **Contract vehicle changed.** PI-4 is now governed by **AP00288 — "ServiceNow Configuration Management Database (CMDB)"**, a standalone Individual Contract (effective Oct 30, 2026 → Feb 2, 2027, fixed fee $1,525,826), *not* by AP00105-5 v3 as workstreams 1–4 of an 11-workstream change order. WS 5–11 do not appear in AP00288. **Stop using the "WS 1–4 of 11" framing in status reporting.** The SOW reviewed was an unsigned draft (blank signature blocks).

| # | ADO ID | Objective | AP00288 §  | Owner | ADO Feat | SOW Deliv | Gates |
|---|--------|-----------|------------|-------|----------|-----------|-------|
| 1 | 1639022 | Automate Network Gear Inventory in the CMDB | 3.1 | M. Vazquez | 3 | 2 | Dec 31 · Feb 2 |
| 2 | 1639027 | Build & Validate Service Maps for Priority Business Apps | 3.2 | A. Griffis | 3 | 4 | **Nov 30** · Dec 31 · Feb 2 |
| 3 | 1639072 | Drive CMDB Adoption Across PPL User Groups | 3.3 | M. Vazquez | 1 | 1 | **Jan 30** |
| 4 | 1639075 | Implement CMDB Lifecycle Management Process Flows | 3.4 | M. Vazquez | 5 | 5 | Dec 31 · Feb 2 |

12 ADO features against 12 SOW deliverables — but **not 1:1**. Full feature-to-deliverable mapping is in [[pi-planning]].

## AP00288 changes vs. AP00105-5 v3

| Area | Existing | Updated | Impact |
|---|---|---|---|
| Network Gear | 3 integrations (SolarWinds Dec 31; Cisco Catalyst + Qualys Feb 2); POC only; Tripwire out of scope | **2 integrations** (1 of 3 Dec 31; 2 of 3 Feb 2); **POC *and Production Release***; **Tripwire named as an option** | ADO 1639239 (Qualys) has no SOW deliverable |
| Service Mapping | 30 maps Dec 31; 15 maps Feb 2; notifications bundled | **15 by Nov 30**; 15 by Dec 31; 15 by Feb 2; notifications broken out as D6 | **New Nov 30 gate**; ADO 1642237 must split |
| CMDB Adoption | Feb 2, 2027 | **Jan 30, 2027** | Moves to its own January invoice |
| Lifecycle Mgmt | 5 deliverables | Unchanged | No action |

**New contract terms worth tracking:** deliverable acceptance period is **three business days**, after which a deliverable is *deemed accepted*. Invoicing is front-loaded — Nov $478,197 (D3 alone) · Dec $505,885 · Jan $493,794 · **Feb only $47,950** for five deliverables. "CMDB Product Owner" is a named role in §13.1.

**Drafting defects to raise before signature:** SOW says "three (3) integrations" but names four (Cisco Catalyst, Qualys, SolarWinds, Tripwire); Deliverables 1 and 2 have identical text (both read "one (1) of the three (3)"); Deliverable 7 is dated "January 30, **2026**" — before the contract starts; Todd's surname is spelled "Dierkshiede" in §6 and "Dierksheide" in §12.

**Ownership split:** A. Griffis owns all 6 Network Gear + Service Mapping features; M. Vazquez owns all 6 Adoption + Lifecycle features. Objective 1639022 is owned by M. Vazquez while all three of its features sit with A. Griffis.

**Dropped from the official list:** 1517655 (Business Application / Business Capability / Services / Service Offerings) appeared in the earlier Oct 5 backlog view as a PI-3 carryover under Objective 2 but is **not** on the Oct 8 official list. Treat as out of PI-4 scope unless it reappears.

**Also out of scope — no CO7 parent objective:** 1601904 (CMDB Integrations for Additional Data Sources) and 917586 (Integration iTeam & ServiceNow). Neither appears on the Oct 8 list.

## Iteration Summary

| Iteration | Start | End | Notes |
|-----------|-------|-----|-------|
| 4.1 | 2026-10-28 | 2026-11-10 | |
| 4.2 | 2026-11-11 | 2026-11-24 | Thanksgiving week — check capacity |
| 4.3 | 2026-11-25 | 2026-12-08 | |
| 4.4 | 2026-12-09 | 2026-12-22 | |
| 4.5 | 2026-12-23 | 2027-01-05 | ⚠ Christmas + New Year — reduced capacity |
| 4.6 | 2027-01-06 | 2027-01-19 | MLK Day Jan 19 |
| 4.7 (IP) | 2027-01-20 | 2027-02-02 | I&A + PI-5 Planning |

## Key Risks

- Holiday capacity impact on 4.5 (Dec 23 – Jan 5)
- Thanksgiving overlap with 4.2 review/retro (Nov 24–25)
- **A. Griffis carries half the PI-4 feature load at 50% allocation** — 6 of 12 features, spanning two objectives. Confirm this is viable at PI Planning.
- **Objective/feature ownership mismatch on 1639022** — objective sits with M. Vazquez, all three features with A. Griffis. Clarify who is accountable for the objective's delivery.
- **New Nov 30, 2026 gate is unevidenced in ADO** — AP00288 D3 requires 15 service maps by Nov 30. Nov 30 falls inside Sprint 4.3 (Nov 25 – Dec 8). ADO 1642237 is a single 30-map item in Sprint 4.1; if it lands on time the gate is met early, but there is no separate deliverable to evidence. **This gate carries the November invoice of $478,197 — the largest single milestone in the contract.**
- **ADO 1639239 (Qualys POC) is outside contract scope** — AP00288 requires two of three integrations; this is a third. Decide whether to keep it as uncontracted value-add, defer it, or seek a change order.
- **Three-business-day deemed acceptance** — if PPL does not respond in writing within three business days, a deliverable is automatically accepted. Tighter than the ESA default; make sure delivery notifications are tracked.

## Sources

- `PI4-Objectives-Features-2026-10-12.pptx` (in `~/Documents`, outside the vault) — **current** 7-slide deck, realigned to SOW AP00288. Adds a "What Changed" slide and an AP00288-deliverable-to-ADO mapping slide; flags the three misaligned ADO items inline.
- `SOW_ServiceNow_CMDB.pdf` (in `~/Downloads`, outside the vault) — AP00288 unsigned draft. Text extract at `scratchpad/sow_new.md` (session-scoped, not persistent).
- Superseded: `PI4-Objectives-Features-2026-10-08.pptx` (pre-AP00288 gates), `...-2026-10-05.pptx` (TBD ADO IDs). `...-2026-10-09.pptx` was deleted 2026-10-09.
