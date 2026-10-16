---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: draft
updated: 2026-10-15
tags: [work, cmdb-csdm, backlog]
---

# Feature Story Templates — CMDB-CSDM

Backlog authoring aid. Hold one of these next to a feature in ADO and create the items listed. Applies the three buckets from [[feature-implementation-structure]]: **spike / requirements → build & test → promote to prod**.

Two templates, because the two families decompose with different weight:

| Template | Applies to | Weight |
|---|---|---|
| **A — Network inventory integration** | 1639206 SolarWinds · 1639225 Cisco Catalyst · 1639239 Qualys · Tripwire (no ADO item yet) | Fat spike, thin promote |
| **B — Lifecycle process flow** | 1640805 Server Build · 1640819 Server Decommission | Moderate spike, fat promote |

Story counts are a starting point, not a rule. Create items with the "+" link from the Feature per [[requirements-process#ADO Hierarchy Rule]] — never standalone.

---

## Template A — Network inventory integration

Discovery-heavy. Most of the risk is answered before any build starts: can we reach the source, what does it return, and how does it rank against discovery already in place.

### Spike / requirements

| # | Type | Item | Answers |
|---|------|------|---------|
| A-S1 | Spike | Source access and authentication | Can we connect? Which account, which credentials, who owns them, what network path |
| A-S2 | Spike | Data profile and field mapping | What does the source actually return, and how does it map to `cmdb_ci_netgear` and its subclasses |
| A-S3 | Spike | Reconciliation and precedence | Where this source ranks against existing discovery, IRE rules, duplicate-CI risk |

**Exit:** build stories pass [[definition-of-ready]] gates 1–4. A-S1/S2 must also settle **configuration vs. customization** — if any transform needs custom script, the RAID issue and Sonika's approval start now, not at build (see [[requirements-process#Customization Governance]]).

### Build & test

| # | Item |
|---|------|
| A-B1 | Configure the data source connection |
| A-B2 | Field mapping and transforms to CMDB classes |
| A-B3 | Identification and reconciliation rules configured |
| A-B4 | Scheduled sync, error handling and logging |
| A-B5 | Validate against a known sample set of devices |

### Promote to prod

| # | Item |
|---|------|
| A-P1 | Change request, PROD deploy, sync scheduled and live, evidence packaged for acceptance |

One item. An integration POC has no user-facing behaviour change, so there is little to communicate and nothing to train.

### Usual dependencies

- Source system owner — who authorises the account
- Credentials and account permissions — the recurring blocker on this project; see the discovery-coverage risk in [[Memory]]
- Network path / subnet access to the source

---

## Template B — Lifecycle process flow

Process-change-heavy. The build is modest; the weight sits in getting people to work the new way.

### Spike / requirements

| # | Type | Item | Answers |
|---|------|------|---------|
| B-S1 | Spike | Current-state process map | Who does what today, and where the CMDB is touched (or isn't) |
| B-S2 | Spike | Target-state flow and CI state model | Lifecycle states, what triggers each transition, who owns each step |
| B-S3 | Spike | Class Manager confirmation | Target flow agreed by the Class Manager before build |

**Exit:** build stories pass [[definition-of-ready]] gates 1–4, with B-S3 signed off. B-S3 is the long pole — it is an external dependency, not team capacity.

### Build & test

| # | Item |
|---|------|
| B-B1 | Configure lifecycle states and the flow |
| B-B2 | Triggers and automation for state transitions |
| B-B3 | Notifications and approvals |
| B-B4 | User entry point — catalog item or interface, where the flow needs one |
| B-B5 | Test against representative server records |

### Promote to prod

| # | Item |
|---|------|
| B-P1 | OCM — communications and training materials for the affected groups |
| B-P2 | Change request and PROD deploy |
| B-P3 | Evidence packaged, acceptance received |

Three items, against Template A's one. That difference is the point: a lifecycle flow changes how people work, so communication and training are delivery work, not an afterthought.

### Usual dependencies

- **Class Manager** — Ray Reuter for Servers and Storage CIs (see CCB roster in [[Memory]])
- **OCM** — Nora Lizenberg is OCM Support on the CCB; confirm who produces the materials
- Server support groups affected by the new flow

---

## Open items

| # | Item |
|---|------|
| 1 | Confirm Ray Reuter is the right Class Manager contact for both server lifecycle flows |
| 2 | Confirm who produces OCM materials for B-P1 — team, or Nora's group |
| 3 | Tripwire has no ADO feature yet. Create it, then apply Template A from the start |
| 4 | Qualys status is contradictory — deferred to PI-1 2027 on Oct 12, but back in Sprint 4.6 on the Oct 14 deck. Confirm before applying the template |
