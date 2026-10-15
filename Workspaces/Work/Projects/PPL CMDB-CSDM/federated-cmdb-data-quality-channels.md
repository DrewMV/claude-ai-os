---
type: concept
workspace: Work
project: PPL CMDB-CSDM
updated: 2026-09-14
tags: [work, cmdb-csdm, governance, federated, draft, communication]
---

# Federated CMDB Data Quality — Three Channels

> 🟡 **Status: DRAFT — not yet sent to the team.** Written as a message to introduce the concept and gather feedback/consensus before it's built into anything.

## Message to send

**Subject: Proposal — three channels for surfacing CMDB data quality issues**

Team,

As we move to the federated model, I want to lock down *how* data issues actually reach the right owner — not just who's accountable once they do. I see three distinct channels, and I'd like your read on whether this covers the real-world cases we're seeing, before we build anything around it.

**Proactive** — Data Manager certification and validation policies run on a schedule and push attestation tasks straight to the accountable owners. This catches issues before anyone's affected, and coverage doesn't depend on someone noticing.

**Intentional** — the service catalog, for when someone already knows what they need: a new CI, an ownership change, a bad value they want corrected. The accountable party reviews every request before anything's written, so the catalog can't be used to route around ownership.

**Reactive** — the help desk, for issues nobody was looking for. A user hits a wall trying to do something else, and it turns into an incident that gets escalated for triage.

Between the three, every way a data issue can surface — scheduled, requested, or stumbled into — should land with the same owners the federated model already defines.

A few things I want your take on:
- Are there issue-discovery paths we're missing, or cases that don't cleanly fit one of these three?
- Any concerns with how this maps to your team's current workflow?

Let me know if this holds up or if I'm missing something — trying to get to consensus before this goes further.
