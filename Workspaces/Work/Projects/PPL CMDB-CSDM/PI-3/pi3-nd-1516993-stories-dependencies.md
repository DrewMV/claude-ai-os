---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1516993 — Automated Credentialed Discovery Live — All Network Device Types"
objective: CO6 Obj 4 — Automate Network Device Discovery in the CMDB
sprint: 3.1
co6-due: 2026-08-31
status: reference-draft
updated: 2026-07-27
tags: [work, cmdb-csdm, safe, pi-planning, co6, network-discovery]
relationships:
  - target: "[[PI-3/pi3-network-discovery-feature-breakdown]]"
    type: derived_from
  - target: "[[PI-3/pi3-cmdb-csdm-ado-tracking]]"
    type: related_to
  - target: "[[PI-3/pi3-objectives]]"
    type: related_to
---

# Feature 1516993 — Stories & Dependencies

**Automated Credentialed Discovery Live — All Network Device Types**
Sprint 3.1 · Aug 5–18 · CO6 due Aug 31 · Owner: M. Vazquez

> **Status: REFERENCE / DRAFT** — Manuel creates the real items in ADO under Feature 1516993 and reconciles IDs back here (ADO authoritative). Per [[definition-of-ready]], create stories from the Feature "+" link, never standalone.
> See [[PI-3/pi3-network-discovery-feature-breakdown]] for the full feature-level breakdown and existing ADO item references.

---

## CO6 Acceptance Criteria this feature delivers (Aug 31)

From [[PI-3/pi3-objectives]] — Obj 4 (CO6 §1), Aug 31 gate:

- All network device types actively discovered using validated credentials; no failed authentications on target devices
- Discovery schedules running on defined intervals; CMDB records auto-updated without manual intervention within each scheduled cycle

**Device types in scope (CO6 §1):** Routers · Switches · Firewalls · Load Balancers · Wireless Access Points · Network Controllers

---

## ADO item reconciliation note

The [[PI-3/pi3-network-discovery-feature-breakdown]] file references existing ADO items that cover parts of this feature's work:

| Existing ADO item | Maps to | Action |
|-------------------|---------|--------|
| 1444864 — fix credentials | ND-1 (partial) | Re-parent to Feature 1516993; add/confirm AC below |
| 1459721 — SNMP/MID pilot | ND-1, ND-2 (partial) | Re-parent to Feature 1516993; add/confirm AC below |
| 1402572 — adjust discovery config | ND-2 (partial) | Re-parent to Feature 1516993; add/confirm AC below |
| 1402574 — adjust device config | ND-2 (partial) | Re-parent to Feature 1516993; add/confirm AC below |

Stories ND-3 (validation), ND-4 (validation), and ND-5 (scheduling automation) are **net-new** — no existing ADO item covers them.

---

## Stories (5)

---

### ND-1 · [Enabler – Infrastructure] Configure credential records for network device discovery

| Field | Value |
|-------|-------|
| Type | Enabler – Infrastructure |
| Parent feature | 1516993 |
| Sprint | 3.1 |
| Owner | Stan Tomberg (confirm) |
| Points | TBD at refinement |
| ADO note | Extends / replaces 1444864 + 1459721 — confirm re-parent at Sprint Planning |
| Tags | `Network-Discovery` `Credentials` `CO6-Obj4` |

**As** the CMDB Configuration Manager,
**I want** SNMP (v2c/v3) and SSH credential records created and validated in ServiceNow for all six network device types,
**So that** discovery probes can authenticate against target devices without manual credential intervention.

**Acceptance criteria:**
- [ ] SNMP credential record(s) created for each vendor/protocol in scope (Routers, Switches, Firewalls, Load Balancers, WAPs, Network Controllers)
- [ ] SSH credential record(s) created where SSH is the required probe method for a device type
- [ ] Credential affinity rules configured — each credential mapped to the correct IP range(s) for its device type
- [ ] MID Server(s) confirmed to have network-layer access to all six device type subnets
- [ ] Test ping/SNMP walk from MID Server to at least one target device per type confirms connectivity and credential validity
- [ ] No credential stored in plaintext outside the ServiceNow credential vault

**Dependencies:** DEP-1 (credentials handoff), DEP-2 (IP subnets), DEP-3 (firewall rules) must be resolved before this story can close.

---

### ND-2 · [Enabler – Infrastructure] Configure discovery definitions and IP ranges for all network device types

| Field | Value |
|-------|-------|
| Type | Enabler – Infrastructure |
| Parent feature | 1516993 |
| Sprint | 3.1 |
| Owner | Stan Tomberg (confirm) |
| Points | TBD at refinement |
| ADO note | Extends / replaces 1402572 + 1402574 — confirm re-parent at Sprint Planning |
| Tags | `Network-Discovery` `Configuration` `CO6-Obj4` |

**As** the CMDB Configuration Manager,
**I want** discovery definitions configured with the correct IP ranges covering all six network device types,
**So that** scheduled discovery runs target the right hosts and do not scan unrelated subnets.

**Acceptance criteria:**
- [ ] Discovery definition(s) created in ServiceNow covering IP ranges for: Routers, Switches, Firewalls, Load Balancers, Wireless Access Points, Network Controllers
- [ ] Each IP range scoped to the correct network segments — confirmed with network team
- [ ] MID Server assigned to each definition and confirmed reachable for those ranges
- [ ] SNMP port 161/UDP and SSH port 22/TCP confirmed open between MID Server and target ranges
- [ ] Discovery definition set to appropriate scan type (Quick/Deep) for each device type — rationale documented
- [ ] Manual test run executed per definition; discovery log shows probe attempts with no silent drops

**Dependencies:** DEP-2 (IP subnet list), DEP-3 (firewall rules).

---

### ND-3 · [Enabler – Configuration] Credentialed discovery live and validated — Routers, Switches, Firewalls

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1516993 |
| Sprint | 3.1 |
| Owner | Stan Tomberg (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — no existing item covers validation at scale for these three types |
| Depends on | ND-1, ND-2 |
| Tags | `Network-Discovery` `Validation` `CO6-Obj4` |

**As** the CMDB Configuration Manager,
**I want** credentialed discovery confirmed live for Routers, Switches, and Firewalls,
**So that** CMDB records for these device types are being created or updated by discovery with no authentication failures.

**Acceptance criteria:**
- [ ] Discovery run completed for Routers, Switches, and Firewalls
- [ ] CMDB contains active CI records for each device type; count is plausible against baseline (DEP-5)
- [ ] Discovery log shows zero authentication failures for targeted devices
- [ ] CI records carry `discovery_source = ServiceNow Discovery` confirming automated origin
- [ ] No duplicate CIs created — IRE identification rules fired correctly; existing records updated, not duplicated
- [ ] Spot-check: 3–5 CIs per device type reviewed; hostname, IP, and sys_class_name correctly populated

---

### ND-4 · [Enabler – Configuration] Credentialed discovery live and validated — Load Balancers, WAPs, Network Controllers

| Field | Value |
|-------|-------|
| Type | Enabler – Configuration |
| Parent feature | 1516993 |
| Sprint | 3.1 |
| Owner | Stan Tomberg (confirm) |
| Points | TBD at refinement |
| ADO note | Net-new — no existing item covers validation at scale for these three types |
| Depends on | ND-1, ND-2 |
| Tags | `Network-Discovery` `Validation` `CO6-Obj4` |

**As** the CMDB Configuration Manager,
**I want** credentialed discovery confirmed live for Load Balancers, Wireless Access Points, and Network Controllers,
**So that** CMDB records for these device types are being created or updated by discovery with no authentication failures.

**Acceptance criteria:**
- [ ] Discovery run completed for Load Balancers, Wireless Access Points, and Network Controllers
- [ ] CMDB contains active CI records for each device type; count plausible against baseline (DEP-5)
- [ ] Discovery log shows zero authentication failures for targeted devices
- [ ] CI records carry `discovery_source = ServiceNow Discovery`
- [ ] No duplicate CIs created — IRE fired correctly
- [ ] Spot-check: 3–5 CIs per device type reviewed; hostname, IP, and sys_class_name correctly populated

> **Note:** Load Balancers (e.g. F5) and Network Controllers (e.g. Cisco DNA Center, Aruba) may require vendor-specific patterns or IntegrationHub spokes. Confirm via DEP-4 before sprint start — if a spoke is needed, that is a scope change requiring PO sign-off before this story is created.

---

### ND-5 · [User Story] Discovery schedules running — CMDB auto-updates without manual intervention

| Field | Value |
|-------|-------|
| Type | User Story |
| Parent feature | 1516993 |
| Sprint | 3.1 |
| Owner | Stan Tomberg / Manuel Vazquez |
| Points | TBD at refinement |
| ADO note | Net-new — Thread B (scheduling) per feature breakdown |
| Depends on | ND-3, ND-4 |
| Tags | `Network-Discovery` `Scheduling` `CO6-Obj4` |

**As** the CMDB Configuration Manager,
**I want** discovery schedules running on defined intervals for all six network device types,
**So that** CMDB records update automatically on each cycle without any manual trigger — satisfying the CO6 "no manual intervention" requirement.

**Acceptance criteria:**
- [ ] Scheduled discovery jobs created for all six device types; interval defined and documented (DEP-6)
- [ ] At least one scheduled run completes end-to-end without manual trigger; run log shows success
- [ ] CMDB CI records show `sys_updated_on` timestamps consistent with the scheduled run — confirming auto-update
- [ ] Discovery schedule is visible and manageable in ServiceNow (not a one-off manual run)
- [ ] Schedule interval and next-run time documented and communicated to CMDB Process Owner
- [ ] CO6 acceptance statement demonstrable at Sprint Review: *"discovery schedules running on defined intervals; CMDB records auto-updated without manual intervention within each scheduled cycle"*

---

## Dependencies (6)

**Work item type:** Dependency · **Linked to:** Feature 1516993 (Blocked By) · **Area path:** A-INFOPS\FY26\PI3

---

### DEP-1 · SNMP & SSH credentials from network team

| Field | Value |
|-------|-------|
| Title | [Dependency] SNMP & SSH credentials from network team — Feature 1516993 |
| Description | Discovery cannot authenticate against network devices without SNMP community strings (v2c/v3) and SSH credentials sourced from the network team. Values must be loaded into the ServiceNow credential vault before sprint start. Blocks ND-1 → ND-3, ND-4. |
| Assigned To | Manuel Vazquez |
| Priority | 1 |
| State | Open |
| Due Date | 2026-08-05 |

**Acceptance criteria:**
- [ ] SNMP community string(s) and SNMPv3 auth/priv credentials received from network team for all six device types in scope
- [ ] SSH credentials received where SSH is the required probe method
- [ ] All credential values loaded into ServiceNow credential vault — not stored in plaintext outside the vault
- [ ] Credential records confirmed accessible by the MID Server

---

### DEP-2 · IP subnet list per network device class

| Field | Value |
|-------|-------|
| Title | [Dependency] IP subnet list per network device class — Feature 1516993 |
| Description | Discovery definitions require the IP ranges for each device class in scope: Routers, Switches, Firewalls, Load Balancers, Wireless Access Points, Network Controllers. Network team must provide subnet list before sprint start. Blocks ND-2 → ND-3, ND-4. |
| Assigned To | Manuel Vazquez |
| Priority | 1 |
| State | Open |
| Due Date | 2026-08-05 |

**Acceptance criteria:**
- [ ] IP subnet list received from network team covering all six device classes
- [ ] Each subnet confirmed to contain only the intended device type — no overlap causing out-of-scope discovery
- [ ] Subnets documented and signed off by network team contact

---

### DEP-3 · Firewall rule confirmation — SNMP 161/UDP and SSH 22/TCP

| Field | Value |
|-------|-------|
| Title | [Dependency] Firewall rule confirmation — SNMP 161/UDP and SSH 22/TCP — Feature 1516993 |
| Description | MID Server must reach target network device subnets on SNMP port 161/UDP and SSH port 22/TCP. If a CHG is required, lead time may push into the sprint. Blocks ND-2. |
| Assigned To | Manuel Vazquez |
| Priority | 1 |
| State | Open |
| Due Date | 2026-08-05 |

**Acceptance criteria:**
- [ ] Network/security team confirms SNMP 161/UDP is open from MID Server to all six device type subnets
- [ ] Network/security team confirms SSH 22/TCP is open from MID Server to all subnets where SSH probes are required
- [ ] If a CHG was required: CHG approved and implemented prior to Aug 5
- [ ] Confirmation documented (email or ADO comment) from network/security team contact

---

### DEP-4 · Vendor probe confirmation — Load Balancers and Network Controllers

| Field | Value |
|-------|-------|
| Title | [Dependency] Vendor probe confirmation — Load Balancers and Network Controllers — Feature 1516993 |
| Description | Load Balancers (e.g. F5) and Network Controllers (e.g. Cisco DNA Center, Aruba) may require IntegrationHub spokes rather than standard SNMP probes. If a spoke is needed this is a scope change requiring PO sign-off. Blocks ND-4. |
| Assigned To | Stan Tomberg |
| Priority | 2 |
| State | Open |
| Due Date | 2026-08-05 |

**Acceptance criteria:**
- [ ] Stan Tomberg confirms whether standard SNMP discovery covers Load Balancers and Network Controllers in this environment, or whether vendor-specific spokes are required
- [ ] If standard SNMP is sufficient: documented confirmation — no scope change needed
- [ ] If spokes are required: scope change raised with Joe Dames (PO) and a decision recorded in ADO before sprint start

---

### DEP-5 · Baseline CI count per network device type

| Field | Value |
|-------|-------|
| Title | [Dependency] Baseline CI count per network device type — Feature 1516993 |
| Description | Acceptance of ND-3 and ND-4 requires validating that discovered CI counts are plausible against a known baseline. Network team provides expected device counts per class. Blocks acceptance of ND-3, ND-4. |
| Assigned To | Manuel Vazquez |
| Priority | 3 |
| State | Open |
| Due Date | 2026-08-12 |

**Acceptance criteria:**
- [ ] Network team provides expected device counts for each of the six classes: Routers, Switches, Firewalls, Load Balancers, Wireless Access Points, Network Controllers
- [ ] Counts documented and referenced in ND-3 / ND-4 acceptance
- [ ] Baseline agreed as the validation target for discovery completeness acceptance

---

### DEP-6 · Discovery schedule interval decision

| Field | Value |
|-------|-------|
| Title | [Dependency] Discovery schedule interval decision — Feature 1516993 |
| Description | ND-5 requires a defined schedule interval before discovery jobs can be configured. Confirm cadence with CMDB Process Owner before configuring. Blocks ND-5. |
| Assigned To | Manuel Vazquez |
| Priority | 3 |
| State | Open |
| Due Date | 2026-08-12 |

**Acceptance criteria:**
- [ ] Schedule interval (frequency) for network device discovery confirmed and approved by CMDB Process Owner (Josh Sterling)
- [ ] Decision documented in ADO (comment or attachment)
- [ ] Agreed interval ready to be configured in ServiceNow before ND-5 begins

---

## Sequence summary

```
DEP-1 (Aug 5) ─┐
DEP-2 (Aug 5) ─┼─► ND-1 ─┐
DEP-3 (Aug 5) ─┘          ├─► ND-3 (Routers/Switches/Firewalls) ─┐
                           │                                        ├─► ND-5 (Schedules)
               ND-2 ───────┴─► ND-4 (LBs/WAPs/Controllers) ───────┘
DEP-4 (Aug 5) ─────────────►  [scope confirm before ND-4 created]

DEP-5 (Aug 12) ────────────►  ND-3, ND-4 acceptance
DEP-6 (Aug 12) ────────────►  ND-5 configuration
```

**Sprint 3.1 blocker:** DEP-1, DEP-2, DEP-3, and DEP-4 must all be resolved by Aug 5. Raise at PI Planning (IP Iteration, Jul 22–Aug 4).
