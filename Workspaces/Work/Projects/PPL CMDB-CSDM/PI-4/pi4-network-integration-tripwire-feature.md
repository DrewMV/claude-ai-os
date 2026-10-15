---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-4
feature: "Network Inventory Integration POC — Tripwire"
objective: "PI-4 Obj 1 (1639022) — Automate Network Gear Inventory in the CMDB"
sow: "none — not an AP00288 deliverable"
gate: TBC
sprint: TBC
status: draft
updated: 2026-10-15
tags: [work, cmdb-csdm, safe, pi-planning]
relationships:
  - target: "[[PI-4/pi-planning]]"
    type: derived_from
  - target: "[[PI-4/Memory]]"
    type: related_to
  - target: "[[PI-4/pi4-implementation-plan-appendix]]"
    type: related_to
  - target: "[[Backlog/feature-implementation-structure]]"
    type: related_to
---

# Feature — Network Inventory Integration POC — Tripwire (Draft)

**Fourth integration.** Modeled field-for-field on ADO **1639206 (SolarWinds)**. Siblings: 1639225 (Cisco Catalyst), 1639239 (Qualys).

> **Status: DRAFT (2026-10-15)** — not yet created in ADO. Read the three flags below before creating it.

---

## Before this is created in ADO

**1. No contract vehicle.** AP00288 funds **two** integrations — D1 (1 of 3, Dec 31) and D2 (2 of 3, Feb 2) — while *naming four*: Cisco Catalyst, Qualys, SolarWinds, Tripwire. SolarWinds holds D1, Cisco Catalyst holds D2. Qualys (1639239) was already deferred to PI-1 2027 as uncontracted ([[PI-4/pi-planning]] Risk 5 / Risk 7). Tripwire would be the **second uncontracted integration**, behind Qualys in the same queue, with no deliverable number and no gate. See [[PI-4/pi4-implementation-plan-appendix]] Open Question 5.

**2. The NERC-CIP exclusion may invert this feature's value.** SolarWinds' scope NFR excludes NERC-CIP-classified gear. Tripwire Enterprise is typically deployed at a utility *for* CIP-010 configuration-change monitoring, so a large share of its monitored node set is likely to be exactly the gear AP00288 puts out of scope. **The in-scope device count is unknown and could be small.** DEP-3 below exists to size it before any build commitment — this is the question that decides whether the feature is worth running at all.

**3. Source precedence is a fourth-integration problem, not a first.** SolarWinds, Cisco Catalyst and Qualys can all return the same device. Adding a fourth source without agreed IRE precedence risks duplicate CIs and attribute flapping. DEP-4 and the optional AC-6 cover it.

---

## ADO field text

Paste the two blocks below into the new Feature.

### Description

**Benefit Hypothesis:** We believe automating network gear discovery via Tripwire will result in CMDB becoming a self-updating, authoritative source for configuration-state and firmware attributes of non-NERC-CIP network devices for Network Core, Cyber Security governance, and change-management teams. We will know we've succeeded when the validated device set requires zero manual CMDB updates post-production-promotion and discovery-populated attributes match Tripwire source data with no unexplained variance.

**Nonfunctional Requirements:**

* Security — integration credentials retrieved from the approved credential vault, not hardcoded; read-only, least-privilege service account against Tripwire Enterprise
* Scope/Compliance — discovery must exclude NERC-CIP-classified network gear; because Tripwire's monitored node set is CIP-weighted, the CIP/non-CIP node split must be established and enforced at the integration filter, not left to post-import cleanup
* Reliability — failed authentication or sync failures alert the Discovery team rather than fail silently
* Auditability — CI creates/updates from this source are logged and attributable to Tripwire discovery, for CCB/audit traceability
* Performance — polling schedule must not trigger Tripwire-side rate-limiting or degrade platform performance

**Dependencies:**

* Credential distribution/access to Tripwire-monitored devices — active, documented organizational risk (CO5 risk language: "no scalable solution for the distribution of credentials to target CIs"; open RAID item owned by Stan Tomberg)
* Tripwire Enterprise platform/API access and vendor licensing terms for the ServiceNow connector
* Authoritative CIP/non-CIP classification of Tripwire-monitored network gear, with the resulting in-scope device count — owner: Cyber Security / NERC-CIP compliance (unassigned)
* Discovery source precedence and IRE reconciliation rules across SolarWinds, Cisco Catalyst, Qualys and Tripwire for devices returned by more than one source

### Acceptance Criteria

* Tripwire discovery integration configured and running in a lower (non-prod) environment
* Discovered network gear records validated against Tripwire source data for accuracy (no false positives/negatives on a defined test device set)
* Mandatory CMDB attributes for in-scope device types populated via discovery, no manual backfill required
* Validated integration promoted to production, with discovery schedules running on defined intervals
* Rollback/fallback plan documented in case production promotion surfaces data-quality issues

**Optional sixth criterion — not in the SolarWinds original, added because this is the fourth source.** Delete if precedence is being handled as a separate enabler:

* Reconciliation precedence agreed and configured for devices also returned by SolarWinds, Cisco Catalyst or Qualys — no duplicate CIs created and no attribute flapping between sources across two consecutive discovery cycles

---

## What differs from the SolarWinds original, and why

| Field | Change | Reason |
|---|---|---|
| Benefit Hypothesis — data claim | "non-NERC-CIP network device data" → "configuration-state and firmware attributes of non-NERC-CIP network devices" | Tripwire's authoritative contribution is configuration and version state, not base inventory — SolarWinds and Cisco Catalyst already cover presence. Firmware version is a known gap in the PI-3 Network Gear data dictionary against ESS-02 Section 5. |
| Benefit Hypothesis — consumers | Added Cyber Security governance and change management | Configuration-change data serves those consumers; incident response is better served by the SolarWinds feed. |
| NFR — Scope/Compliance | Added the filter-not-cleanup clause | Flag 2 above. A CIP-weighted source makes this NFR load-bearing rather than boilerplate. |
| Dependencies | Added CIP/non-CIP classification + source precedence | Flag 2 and Flag 3. Neither applied to SolarWinds as the first integration. |
| Acceptance Criteria | Five bullets mirrored verbatim; one optional sixth added | Keeps the block paste-clean and comparable across the four features; precedence surfaced separately so it can be dropped. |

Everything else — Security, Reliability, Auditability, Performance NFRs, the credential RAID dependency, and all five original acceptance criteria — is carried across unchanged.

---

## Open questions

| # | Question | Blocks |
|---|----------|--------|
| 1 | How many Tripwire-monitored network devices are **non-CIP**? | Whether the feature has enough scope to be worth running (DEP-3) |
| 2 | Does Tripwire go in the same uncontracted queue as Qualys (PI-1 2027 / follow-on SOW), or is it being proposed to displace an existing D1/D2 integration? | Sprint, gate, and whether this gets an ADO item now |
| 3 | Who owns the CIP/non-CIP classification call? | The dependency has no named owner |
| 4 | Is discovery source precedence an enabler story under Objective 1 rather than an AC on this feature? | Whether AC-6 stays |
| 5 | Does Tripwire overlap Qualys as a source? Both are security-tooling feeds. | Whether a fourth integration adds coverage or duplicates the third |
