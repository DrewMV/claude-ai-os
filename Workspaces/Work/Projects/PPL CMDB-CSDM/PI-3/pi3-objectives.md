---
type: pi-objectives
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
contract: CO6 (Change Order #6)
updated: 2026-07-08
tags: [work, cmdb-csdm, safe, pi-planning, co6]
---

# PI-3 Objectives — CO6-Authoritative

**PI-3 Window:** Aug 5 – Oct 27, 2026  
**Contract:** Change Order #6 — effective Jun 30, 2026 → Oct 30, 2026 | $2,724,109  
**Source:** AP00105-6 to ServiceNow Release 2 and 3 Deployment v3.docx (authoritative)  
**Note:** CO6 is the governing scope document. Any prior CO5 framing is superseded for PI-3 planning purposes.

---

## Objective Summary

| # | Objective | CO6 Workstream | Priority | Final Gate |
|---|-----------|----------------|----------|------------|
| 1 | Sustain ServiceNow Platform Operations | Platform Support + ITSM PO + ATF Strategy | P0 | Oct 30 |
| 2 | Activate Qualys Integration in Production | Qualys Integration | P1 | Sep 30 |
| 3 | Expand CI Data Certification Across All Major Classes | CMDB Governance + PI-2 carryover | P1 | Oct 30 |
| 4 | Automate Network Device Discovery in CMDB | Network Gear Discovery | P1 | Oct 30 |
| 5 | Build Service Maps for Business Applications | Service Mapping | P2 | Oct 30 |
| 6 | Deliver NERC-CIP ServiceNow Platform Strategy | NERC-CIP Strategy | P2 | Oct 30 |
| 7 | Define and Begin Legacy Platform Migration | Legacy Platform Rationalization | P3 | Oct 30 |

---

## Objective Detail

### Obj 1 — Sustain ServiceNow Platform Operations
**CO6 Workstreams:** Platform Support (§8) + ITSM Product Management (§6) + ATF Strategy (§7)  
**Priority:** P0 — foundational; BAU delivery engine for all other objectives  
**Why P0:** The Platform Support team (2 BAU + 4 major enhancement devs) and ITSM PO underpin delivery velocity across the entire PI. If capacity drops below 40 hrs/sprint, every other objective slips.

**Acceptance Criteria (CO6 §6, §7, §8):**
- Each team member logs 40 completed story pts/sprint, adjusted for holidays/PTO — Jul 31, Aug 31, Sep 30, Oct 30
- Sprint allocation reports available to stakeholders each month
- ATF implementation plan published covering all production ServiceNow capabilities in use as of Jul 31, with defined coverage criteria, sequenced rollout timeline, and reusable implementation approach — Oct 30

---

### Obj 2 — Activate Qualys Integration in Production
**CO6 Workstream:** Qualys Integration (§3)  
**Priority:** P1 — highest contractual visibility; single hard date; carries over from CO5  
**Why P1 over Obj 3:** Single Sep 30 hard date with no mid-PI gate; Data Cert has two-phase arc (Sep 30 + Oct 30) giving more recovery room.

**Acceptance Criteria (CO6 §3):**
- One-way integration from ServiceNow to Qualys fully configured, tested, and live in production — Sep 30
- Owner, support group, and SOX flag data automatically synchronized to Qualys on a defined schedule with no manual handoffs — Sep 30
- *Assumption: Qualys vendor plugin is available (per CO6 dependency clause)*

---

### Obj 3 — Expand CI Data Certification Across All Major Classes
**CO6 Workstream:** CMDB Governance (§4)  
**Priority:** P1 — re-baselines CO5 D1; all four CI classes must be certified by Oct 30  
**PI-2 Carryover absorbed here:**
- Data Dictionary CCB approval (target Jul 21 — pre-PI-3 gate; tracks into PI-3 if slips)
- 3 audit dashboard spikes (Servers 1480112, Database 1480113, Computer 1480114) — Active, carried from Sprint 2.4; required as evidence for coverage acceptance
- 90%-coverage acceptance stories for Computers (G2) and Servers (G3) — no formal story yet; must be created and accepted

**Acceptance Criteria (CO6 §4 + PI-2 carryover):**
- **PI-2 carryover gates (target before PI-3 starts):**
  - Data Dictionary CCB approval — Jul 21
  - 3 audit dashboard spikes completed; 90%-coverage acceptance stories created and accepted
- **CO6 gates:**
  - Data certification process for **Computers**: end-to-end process documented, technical build to PROD, dashboards live, training delivered — Sep 30
  - Data certification process for **Servers**: same — Sep 30
  - Data certification process for **Databases**: same — Oct 30
  - Data certification process for **Network Devices**: same — Oct 30

---

### Obj 4 — Automate Network Device Discovery in CMDB
**CO6 Workstream:** Network Gear Discovery (§1)  
**Priority:** P1 — Aug 31 first gate; foundational for CMDB health and incident response  
**Device types in scope (per CO6):** Routers, Switches, Firewalls, Load Balancers, Wireless Access Points, Network Controllers

**Acceptance Criteria (CO6 §1):**
- All network device types actively discovered using validated credentials; no failed authentications on target devices — Aug 31
- Discovery schedules running on defined intervals; CMDB records auto-updated without manual intervention within each scheduled cycle — Aug 31
- All mandatory CMDB attributes for network devices (per CMDB governance) fully populated via discovery; no mandatory fields blank — Sep 30
- 90%+ expected network device inventory represented in CMDB, validated against authoritative data from business owners — Oct 30

---

### Obj 5 — Build Service Maps for Business Applications
**CO6 Workstream:** Service Mapping (§2)  
**Priority:** P2 — multi-gate arc; significant dependency on app owner availability  
**⚠️ Pre-PI dependency (flag at PI Planning):** CO6 states *"assumes business services have been defined prior to start."* App owner engagement must be secured before Aug 5; otherwise the Aug 31 gate is at risk from day one.

**Acceptance Criteria (CO6 §2):**
- Service maps for **15 Silver-tier (priority) business applications** built in ServiceNow, showing full dependencies from business application to infrastructure CIs, validated by service/application owners, operational teams communicated and trained — Aug 31
- **75%+ of identified business service inventory** represented in CMDB, validated by business service owners — Aug 31
- Service maps for **15 Silver-tier applications** (business application to infrastructure layer): additional validation pass — Sep 30
- Service maps for **Gold-tier business applications** built, showing full dependencies from business service to business application, validated and teams trained — Sep 30
- Service maps for **remaining Silver-tier applications** managed by Accenture complete — Oct 30
- Service maps for all Silver-tier applications: business service to business application layer complete — Oct 30

---

### Obj 6 — Deliver NERC-CIP ServiceNow Platform Strategy
**CO6 Workstream:** NERC-CIP ServiceNow Platform Strategy (§9)  
**Priority:** P2 — executive-level deliverable; Sep 30 + Oct 30 gates; regulatory context  

**Acceptance Criteria (CO6 §9):**
- Evaluation of dual-instance NERC-CIP strategy completed, with documented high-level considerations, pros/cons, risks, and dependencies — Sep 30
- Executive-level strategy package (PowerPoint or Word) describing go-forward solution options, tradeoffs, and high-level implementation steps — Oct 30

---

### Obj 7 — Define and Begin Legacy Platform Migration
**CO6 Workstream:** Legacy Platform Rationalization (§5)  
**Priority:** P3 — planning and analysis arc; execution scope limited to Oct efforts per the migration plan  
**Platforms in scope:** iTeam, DISCO, Cherwell, AIM  

**Acceptance Criteria (CO6 §5):**
- Gap analysis of functionality in iTeam, DISCO, Cherwell, and AIM vs. ServiceNow existing capabilities; existing PPL documentation reviewed and validated — Aug 31
- Migration plan delivered: prioritized functionality list + actionable roadmap with timelines — Sep 30
- Execution of October-scope items from the migration plan delivered in §5.2 — Oct 30

---

## Key Dependencies and Risks

| Risk | Objective | Detail |
|------|-----------|--------|
| App owner availability | Obj 5 | CO6 explicitly assumes business services are defined pre-start; must be resolved before Aug 5 |
| Qualys vendor plugin | Obj 2 | CO6 assumes plugin is available; confirm with Rich Santillo / Stan pre-PI |
| PI-2 carryover gates | Obj 3 | Data Dictionary CCB approval (Jul 21) and audit spikes must close before PI-3 starts; if not, Obj 3 Sprint 1 is blocked |
| Test code freeze Jul 18 – Aug 15 | All | Overlaps first two weeks of PI-3; sequences Obj 1 and Obj 2 first-sprint deliveries |
| CO6 signature | All | Effective Jun 30 retroactively; all objectives contingent on execution (expected this week) |

---

## CO6 Monthly Fee Schedule (Reference)

| Month | CO6 Fee |
|-------|---------|
| July 2026 | $448,900 |
| August 2026 | $726,037 |
| September 2026 | $774,586 |
| October 2026 | $774,586 |
| **CO6 Total** | **$2,724,109** |

---

## Open Actions Before PI Planning (Jul 22 – Aug 4)

| Action | Owner | Blocks |
|--------|-------|--------|
| Execute CO6 signature | Christian / Aaron Simeon | All objectives |
| Confirm Qualys vendor plugin available | Stan / Rich Santillo | Obj 2 |
| Secure app owner list for Silver/Gold-tier service mapping | Tanzeel / Joe Dames | Obj 5 |
| Close Data Dictionary CCB approval (Jul 21) | Manuel / Josh Sterling | Obj 3 PI-2 carryover |
| Complete 3 audit dashboard spikes + create 90%-coverage stories | Team | Obj 3 PI-2 carryover |
| Confirm NERC-CIP strategy stakeholder (PPL IT Leadership) | Joe Dames | Obj 6 |
