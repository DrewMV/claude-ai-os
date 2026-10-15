---
type: team-artifact
workspace: Work
project: CMDB-CSDM
status: proposed
updated: 2026-10-14
tags: [work, cmdb-csdm, backlog]
---

# Feature Implementation Structure — CMDB-CSDM

**Status: PROPOSED (2026-10-14)** — not yet agreed. See [Adoption](#adoption) for who needs to sign off.

Every feature decomposes into the same three stages. See [[definition-of-ready]] for story entry gates, [[definition-of-done]] for story acceptance, and [[requirements-process]] for the intake flow this sits on top of.

Origin: project DL feedback on the PI-4 deck (Oct 2026) — the sprint, commitment and program-board views show hard due dates but not the activities needed to hit them. A fixed feature structure makes that timing derivable instead of estimated feature by feature.

---

## The three stages

```
Feature
├── [Spike]  Discovery & requirements        → exit: build stories pass DoR gates 1–4
├── [Story]  Build …                          → exit: DoD met
├── [Story]  Build …                          → exit: DoD met
└── [Story]  Implement — release, OCM, acceptance   → exit: gate evidenced
```

### Stage 1 — Spike (exactly one per feature)

Exists to answer questions, not to build. Timeboxed to one iteration.

- [ ] Requirements gathered and confirmed with the stakeholder, in writing
- [ ] Technical approach agreed with the dev team
- [ ] Build stories listed and sized
- [ ] Dependencies named, each with an owner
- [ ] **Configuration vs. customization determined**

**Exit:** the build stories pass [[definition-of-ready]] Gates 1–4.

The customization call is the reason this stage cannot be skipped. Per [[requirements-process#Customization Governance]], anything with custom logic needs a Customization tag, a linked RAID issue, and Sonika Das's approval **before it can be implemented**. Finding that during build costs an iteration. The spike is where it surfaces while there is still time to absorb it.

### Stage 2 — Build & Test (one or more stories)

Standard stories under the Feature, created with the "+" icon per the ADO hierarchy rule. [[definition-of-done]] applies unchanged.

- [ ] Each story fits one iteration
- [ ] Testing is inside the story — no separate test story, no QA handoff item
- [ ] Staging deploy + PO demo per DoD

### Stage 3 — Implement (exactly one per feature)

- [ ] Change request raised and scheduled into a change window
- [ ] Deployed to PROD
- [ ] OCM communications / training delivered where [[requirements-process#OCM Coordination]] triggers apply
- [ ] Evidence package assembled
- [ ] Deliverable submitted and customer acceptance received

**Exit:** the contract or governance gate is evidenced.

---

## Why Stage 3 is a separate story

[[definition-of-done]] ends at *"deployed to staging / test environment"* and *"PO demo accepted at Sprint Review."*

Contract acceptance requires PROD plus a customer sign-off — under AP00288, on a three-business-day deemed-acceptance clock.

**A feature can therefore be fully Done by the team's own definition and still not be a delivered deliverable.** That gap is currently unowned, and it is why completion dates read earlier than delivery dates.

Stage 3 also has different owners (change/CCB, OCM, PO) and a different blocking dependency (the change window) than Stage 2. Folded into the last build story as acceptance criteria, both become invisible. As its own story it can be tracked, blocked, and reported.

---

## Sizing the structure

The shape is fixed; the weight is not.

| Feature type | Spike | Build | Implement |
|---|---|---|---|
| OOTB configuration | Thin — confirm requirements, size the work | 1–2 stories | Standard |
| Customization-tagged | Full — plus RAID lead time before build can start | n stories | Standard |
| User-facing change | Full — plus early OCM engagement | n stories | Heavier — comms + training |

The middle column is `n`, not three. A thin config feature may have one build story; Service Mapping may have six.

---

## What this does not change

- [[definition-of-ready]] — unchanged, and still the enforcement point
- [[definition-of-done]] — unchanged (see open decision below)
- ADO hierarchy, the "+" creation rule, PO ownership of Epic and Feature levels
- P1–P4 priority model and numeric sub-ranking
- Customization governance and the RAID path
- Existing ceremonies and refinement cadence

This is a decomposition convention, not a new process.

---

## What it gives us

- **Three dated exit gates per feature** — the intermediate due dates the DL asked for, without reading individual stories
- **Derivable phase timing** — once every feature has the same stages, a timeline is generated rather than estimated
- **Parallelism becomes visible** — which features are in spike while others are in build, and who is loaded across both
- **A home for release, OCM and acceptance work** that currently has none

---

## Open decision — the DoD boundary

Stage 3 sits outside the current Definition of Done. Two ways to handle it:

| Option | Effect |
|---|---|
| **A — Give the Implement story its own acceptance criteria** (recommended) | [[definition-of-done]] stays as agreed. The Implement story carries explicit AC for CR, PROD, OCM, evidence, acceptance. Surgical; does not reopen a settled team artifact. |
| B — Extend the Definition of Done to include PROD + customer acceptance | One consistent bar for every story, but it makes build stories undeliverable within a sprint, since PROD release depends on a change window outside the team's control. |

**Recommendation: Option A.** Option B would make most build stories permanently un-Done through no fault of the team.

---

## Adoption

| # | Item | Owner |
|---|------|-------|
| 1 | Agree the structure — PO owns Epic and Feature levels, so this is Joe's call to make | Joe Dames |
| 2 | Process-change confirmation | Sonika Das |
| 3 | Confirm it answers the implementation-plan feedback | Project DL |
| 4 | Story-creation convention applied in ADO | Anuradha Rai |
| 5 | Decide Option A vs. B above | Joe Dames / team |
| 6 | Check ART-level consistency before it becomes a local-only convention | Nolan LeBlanc (RTE) |

**Proposed adoption point:** PI-4 features at PI Planning, Nov 4, 2026. Not retrofitted to PI-3 or earlier.

**Precedent already in the vault:** [[PI-4/pi4-adoption-1639308-campaign-stories-dependencies]] breaks D7 into Define → Build → Roll out → Evidence — this same skeleton with Implement split into two waves. The pattern exists for one feature; this generalises it.

**Follow-up once adopted:** add a cross-reference line to [[definition-of-ready]] and [[definition-of-done]]. Not done yet — those are agreed artifacts and this is still a proposal.
