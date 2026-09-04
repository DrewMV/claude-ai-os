---
type: ado-tracking
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
contract: CO6 (Change Order #6)
source: Azure DevOps (A-INFOPS\FY26\PI3)
sources:
  - "Azure DevOps (A-INFOPS\\FY26\\PI3)"
  - "C:\\Users\\manuel.b.vazquez\\Desktop\\PI3-Objectives-Features-2026-07-22.pptx"
  - "ADO board export, screenshots (2026-08-05) — full PI-3 query sorted by Iteration Path"
  - "ADO board export, screenshots (2026-09-03) — CMDB/CSDM team query sorted by State, labeled 'Sprint 3.1 update'"
as-of: 2026-09-03
updated: 2026-09-03
summary: "CMDB/CSDM team PI-3 ADO objectives (5) and features (15): 4 CO6-gated objectives + 1 non-CO6 PI-2 carryover objective with 3 features."
base_confidence: 0.9
lifecycle: draft
lifecycle_changed: "2026-07-27"
tier: supporting
provenance:
  extracted: 0.95
  inferred: 0.05
  ambiguous: 0.0
tags: [work, cmdb-csdm, safe, pi-planning, co6]
---

# PI-3 — CMDB/CSDM Team ADO Objectives & Features

**What this is:** The authoritative record of the **CMDB/CSDM team's** PI-3 objectives and features **as they exist in Azure DevOps** (ADO). The CMDB/CSDM focus area is a **subset of CO6** — it is the slice of the contract this team owns, executes, and reports on.

**What this is not:** The full CO6 contract scope. The 7 governing CO6 objectives are unchanged and live in [[PI-3/pi3-objectives]]. CO6 does not change; this file tracks only the CMDB/CSDM ADO items and keeps them traceable back to CO6.

> **Subset relationship:** 4 ADO objectives map to CO6 Objectives 2, 3, 4, and 5. CO6 Objectives 1 (Platform Ops), 6 (NERC-CIP Strategy), and 7 (Legacy Migration) sit outside the CMDB/CSDM focus area. A 5th objective — the PI-2 carryover — is a **non-CO6 team commitment** tracked here for ART visibility; it has no CO6 delivery gate.

---

## Snapshot (as of 2026-07-31)

| Metric | Value |
|--------|-------|
| ADO area path | `A-INFOPS\FY26\PI3` |
| Objectives | 5 (4 CO6-gated + 1 non-CO6 PI-2 carryover) |
| Features | 15 (11 CO6-gated + 1 data-quality enabler 1537867 + 3 under PI-2 carryover objective) |
| State | Objectives + 3.2–3.5 features: **New**; the four 3.1 features (1516993, 1517650, 1517065, 1537867): **Defining/New** — confirm 1537867's exact state in ADO |
| PI-3 window | Aug 5 – Oct 27, 2026 |
| Sprints in use | 3.1 – 3.5 (2–3 features each; 3.6 IP empty) |

**Revision 2026-09-03 (ADO export, screenshots, sorted by State — full CMDB/CSDM team query, Manuel-labeled "Sprint 3.1 update"):** No Iteration column in this export, so sprint assignments below are unconfirmed unless otherwise stated.

*Two new, unmapped Features surfaced — likely the "CMDB Role Matrix" initiative and a new Workspace effort, neither yet CO6-traced:*
- **1595485 "CMDB - Role-Based Access and Permission Management"** (Feature, New, no parent shown) — 7 children, all New/Active: 1593513 (Spike, "Conduct Gap Analysis between PPL roles and ServiceNow OOB," 2 pts, Active, Alex Lim), 1595488 ("Assess Current Roles and ACL Configuration," Active, Alex Lim), 1595517 ("Define Role and Permission Matrix," Active, Alex Lim), 1595527 ("Design Role-Based Security Architecture," New), 1595528 ("Implement Roles and ACL Controls," New), 1595529 ("Validate Role-Based Access Controls," New), 1595531 ("Conduct Permission Model UAT," New). Matches the "CMDB Role Matrix" work referenced in recent stakeholder threads (Sonika accepted the plan 2026-09-02/03, weekly review cadence expected) — likely the ADO home for that initiative, but not yet linked to any of the 5 tracked PI-3 objectives.
- **1595440 "CMDB - Workspace Enhancement"** (Feature, New, no parent shown) — 11 children, all New: 1595453 (Define Persona Workspace Requirements), 1595457 (Design Persona-Based Workspace Architecture), 1595460 (Configure Technical Owner Workspace), 1595463 (Configure Support Group Workspace), 1595465 (Configure CI Owner Workspace), 1595474 (Configure Administrator Workspace Dashboard), 1595475 (Configure Class Manager Workspace), 1595477 (Implement Workspace Filters and Drill-Downs), 1595478 (Configure Persona-Based Workspace Security), 1595483 (Validate Workspace Readiness for Production), 1595484 (Deploy Workspace to Production). Entirely new scope with no prior mention anywhere in this file.
- A third possibly-new feature is visible only as a Parent name, no ID captured: **"Business Application / Business Capability / Services / Service Offerings Updates and Definition"**, parent of **1574799** ("Create Relationships Between Application Services, and Services for Gold-Tier Apps," 3 pts, New, Michael Allison). Could be the ADO title for the existing Gold-Tier feature (1517655) under a different name, or a genuinely separate feature.

*Discovery-credential/firewall blockers — active risk theme, 4 related items, none previously grouped together:*
- **1520824** (Issue, "Credential Issues impacting Linux\Database(oracle) discovery," Active, Adam Griffis, tag Discovery)
- **1526877** (Dependency, "SNMP & SSH credentials from network team," Active, Jeff Schwartzkopf, parent Feature 1516993)
- **1526885** (Dependency, "Firewall rule confirmation — SNMP 161/UDP and SSH 22/TCP," New, Adam Griffis, parent Feature 1516993)
- **1571603** (User Story, "Linux Discovery Credential Issues," 8 pts, Active, Jeff Schwartzkopf) — **parent conflict:** this export shows parent **Feature 1517650 (Silver-Tier Service Maps)**, not Feature 1554951 (DB Class Clean up) as Manuel confirmed on 2026-08-19. Reconfirm the correct parent in ADO.

Together these suggest credential/firewall access is the live blocker for both network-device and Linux/Oracle discovery, worth surfacing at the next status update given Feature 1516993's Aug 31 CO6 gate has already passed.

*State changes / scope reductions:*
- **1537636** ("CMDB: Tune discovery patterns to populate discoverable mandatory attributes," parent Feature 1517005) — now **Removed**. Logged New on 2026-08-05 alongside siblings 1537633/1537635/1537637/1537638.
- **1553648 (S04), 1553649 (S10), 1553651 (S05)** — all three BA→Service Instance migration stories (Feature 1537867) now **Removed**. Previously logged New (3.3/3.4) on 2026-08-05.
- **1558255 (Paymentus)** Silver-Tier service-map story — now **Resolved**, its 4 template tasks (Data Gathering/Build Mapping/Publish/Validate & Sign-off) all Removed alongside it.

*Progress on certification-cycle stories:*
- **1535490** "Run the Computer certification cycle and monitor completeness" (Kiran Dhobale) → **Validation**.
- **1535491** "Deliver Computer certification training to CI owners" (Manuel, tag OCM, 3 pts) → **Ready DoR**.
- **1535502** "Run the Server certification cycle and monitor completeness" (Kiran Dhobale, 1 pt) → **Ready DoR**.
- **1504320** "Database Clean up: IP address and Location" (Anthony, 3 pts) confirmed still **Ready DoR** — matches 2026-08-19 log.

*New stories under Feature 1517005 (Mandatory Attribute Population — Network Devices):*
- **1587192** "Configure Required and Recommended fields for Network Gear & sub classes" (Vinay Geddannavar, 1 pt, Active)
- **1587208** "Create CMDB inclusion rules" (Vinay Geddannavar, 1 pt, Ready DoR)
- **1537635** "Baseline mandatory-attribute population and gap analysis (network devices)" (Vinay Geddannavar, 3 pts) → **Ready DoR** (up from New)
- **1595055** "Network Discovery - Coverage metric dashboard by device class" (Kiran Dhobale, 2 pts, Refinement Ready) — net-new
- **1595067** "Add a 'discovered in last week / last month' filter to the coverage dashboard" (Kiran Dhobale, 3 pts, Refinement Ready) — net-new

*Silver-Tier Service Maps — spike-to-story progression, 10 more apps now have full User Stories* (each with Build Mapping + Publish tasks, 1 pt, State New unless noted): Portfolio Management Identity Management (1558250), TaskOp (1558260), LWC Micronaut (1558265), ADP ShareFile (1558270), Documentum (1560651), MITS (1560656), Survey 123 (1560661), GeoDigital (1558234), DocuFind (1558239), MaxQueue (1558244). Three of these (GeoDigital, DocuFind, Documentum) now have both the original identify/confirm-inputs Spike **and** the full Gather/Build/Publish User Story. Five more spikes (identify/confirm-inputs stage only, no story yet, 1 pt each, New) surfaced for apps not previously named: Cadency (1547748), MDTDocuments (1547777), MaxQueue (1547780, sibling to its story), Portfolio Management Identity Management (1547781, sibling to its story), Resource Innovations - Trade Ally Connect (1547790).

**Note on Task-level items:** Service Mapping User Stories carry a standard 4-task template (Data Gathering, Build Mapping, Publish, Validate & Sign-off). This file tracks Story/Spike/Feature/Dependency/Issue level only — individual task state isn't itemized here.

*Net-new items needing triage (no clear CO6/feature linkage confirmed):*
- **1560566** "Dependency with CI owners for Network" (Manuel, New) — parent Feature 1517040 (Certify Network Devices); check against the 5 dependencies already logged in [[PI-3/pi3-cert-1517040-certify-network-devices-stories-dependencies]], may be a 6th or a duplicate.
- **1560878** "CMDB Validation of CI to Application Relationships" (Sonika Das, New, Dependency) — no parent shown.
- **1582669** "CMDB: BUG — QA/TEST MID Servers unhealthy (4 of 10 Up)" (Anthony, Active) — no parent shown; MID Server health affects discovery reliability broadly, worth watching against the CO6 discovery gates even though it reads as platform-ops rather than CMDB-CSDM data scope.
- **1587385** "CMDB: Validate ServiceNow MID Servers Against the CyberArk Cloud Migration" (Anthony, Active) — no parent; follow-on to the now-**Closed** Issue **1536150** "PA CyberArk Moving to Cloud - Potential Impact to Access" (Manuel).

**Revision 2026-07-31:** Story-level reconciliation from the ADO board. **Also corrects an under-count:** Feature **1537867** ("Migration of Business Apps to Application Services," under the Service Mapping objective 1516955, Iteration 3.1, data-quality enabler — not a CO6 gate) was already documented in the Features-by-Objective section below but had been left out of the Snapshot's feature count (11 → 12) and the Features-by-Iteration table (3.1: 3 → 4). Both corrected. Otherwise, objectives/features unchanged from the 7/28 snapshot — all still match. 20 user stories now confirmed created in ADO: 5 under Feature 1516993 (Network Discovery), 5 under Feature 1517005 (Mandatory Attribute Population), 5 under Feature 1517029 (Certify Computers), 5 under Feature 1517032 (Certify Servers). No stories yet visible in ADO for Features 1537867, 1517650, 1517655, 1518000, 1517037, 1517040, 1356646, 1517065. **Sequencing flag:** Certify Computers' stories landed off-plan — CC-1 (doc-only) built in 3.2 instead of 3.1 (no impact), but CC-5 (training) landed in **3.2**, ahead of CC-4 (run the cert cycle, 3.3) which it nominally depends on; Certify Servers' 5 stories landed exactly as planned (3.1/3.2/3.2/3.3/3.4). See [[PI-3/pi3-nd-1516993-stories-dependencies]], [[PI-3/pi3-network-discovery-feature-breakdown]] (Feature 2), [[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]], and [[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]] for full detail.
**Revision 2026-07-28:** State refresh from the ADO board — the three Iteration-3.1 features (1516993 Network Discovery, 1517650 Silver Service Maps, 1517065 Qualys) have moved New → **Defining**; all objectives and the 3.2–3.5 features remain New. Sprint assignments unchanged.
**Revision 2026-08-19 (cont'd — Sprint 3.2 board export, sorted by State):** A broader ADO export covering Iteration 3.2 items surfaced two significant findings and resolved a long-open item.

**Resolved:** the four database attribute stories under Feature 1554951 — **1504309, 1504316, 1504318, 1504320** — are now confirmed **Iteration 3.2** (all Ready DoR). This closes the "iteration reassignment in progress" open item tracked since 2026-07-31.

**Finding — Certify Databases (1517037) and Certify Network Devices (1517040) stories are pulling forward from their planned Sprint 3.4 start:**
- **DB-2 (1560067)** "Build Database certification policies/rules to PROD" — shows **Iteration 3.2**, State Ready DoR, 3 pts. Planned/documented start was Sprint 3.4 (per [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]]).
- **NW-2 (1560089)** "Document the Network Device certification process flow" — shows **Iteration 3.2**, State Active, 3 pts, ADO type **Spike** (drift from User Story). Planned start was Sprint 3.4 (per [[PI-3/pi3-cert-1517040-certify-network-devices-stories-dependencies]]).
- **NW-3 (1560091)** "Build Network Device certification policies/rules to PROD" — shows **Iteration 3.2**, State Refinement Ready, 3 pts. Planned start was Sprint 3.4.
- This is consistent with DB-1 (1560066) and NW-1 (1560087) already showing **Resolved** as of the earlier 2026-08-19 snapshot above — the whole Databases/Network Devices certification build appears to be running ~2 sprints ahead of the drafted 3.4–3.5 shape. Good news for the Oct 30 gate (more buffer), but the per-feature files' "Sprint reconciliation" sections should be updated once confirmed directly in ADO — not yet done here, flagged as an open item below.

**Finding — orphaned/duplicate governance stories persist into Sprint 3.2, one now shows a different parent-visibility state than logged:**
- **1508982** (Spike, "Service Catalog for New Business Application/Update Business Application," 1 pt, Active) — still shows **no parent** in this export. Duplicate-suspect of 1553978 remains unresolved.
- **1553978** — now Active, 1 pt, Iter 3.2, ADO type **Spike** (was logged as User Story) — parent confirmed 1553982.
- **1553980** ("Modify SR: SOX-Flagged CI Handling (Governed)") — Active, 1 pt, Iter 3.2, ADO type Spike — this export shows **no parent**, though it was previously confirmed parented to 1553982. Likely the same view-scope limit seen elsewhere in this file, not an actual reparenting — confirm in ADO.
- **1513944** (duplicate of 1553980) — still exists, Ready DoR, 1 pt, Iter 3.2, no parent shown.

**Net-new items, no parent shown (need triage):**
- **1563085** "Import Capabilities/Services" — 2 pts, Ready DoR, Michael Allison
- **1574773** "Import Business Applications" — 3 pts, Ready DoR, Michael Allison
- **1575789** "Sync Metal Tier field from application service to business application and update mapped service form view" — 2 pts, Ready DoR, Joshua Miller
- **1526856** Spike "Validate Server environment Integration Source Behind the Mandatory Designation" — 1 pt, Validation, Israel Shlomi Laurent — likely related to Server cert DEP-7 (Environment mandatory ruling) but not linked to a feature in this view.

**Service Mapping (1517650) backlog progress:** many spikes now carry confirmed real business-application names (OEM, Techniart, ADP ShareFile, Einstein, Geostan/LOB, L+G MDMS, LWC Micronaut, MITS, SMS/Two-Way Text-Twilio, Survey123, TaskOp, Energy Hub Mercury, Oracle Opower) plus User Stories for Transmission Modeling System, Workforce Management System, Paymentus, RI Web Call Tool (CTP), RI FIELDNET, RightFax, SiteScan — all New/Ready DoR/Validation, 1 pt each (consistent with the re-pointing noted above). Four more PLACEHOLDER stories (1558208, 1558213, 1558218, 1558224) added. One spike's title (1547764, "DLC") carries an inline note: *"We're no longer using Geostan for address validation"* — a scope/process change worth confirming with Adam Griffis rather than treating as just a title. Three more stories reached **Validation**: 1547519 (PCS), 1547222 (Fleet Focus FA Suite - Fleet Anywhere), 1547695 (Trading Networks).

**Revision 2026-08-19 (Sprint 3.1 closeout):** ADO screenshot taken at Sprint 3.1 close (Sprint 3.2 opens 2026-08-19). State changes: **ND-1 (1526911)** Ready DoR → **Validation**; **ND-2 (1526947)** Ready DoR → **Active**; **ND-3 (1526951)** Ready DoR → **Validation**; **SV-1 (1535496)** Ready DoR → **Resolved**; **CC-1 (1535486)** → **Validation** (3.1, confirmed); **DB-1 (1560066)** → **Resolved**; **NW-1 (1560087)** → **Resolved**; **Qualys 1428703** → **Validation**; **11 service-mapping stories** (1543982, 1547081, 1547086, 1547091, 1547212, 1547217, 1547283, 1547304, 1547310, 1547324, 1547513) → **Validation**; **BA-migration S01 (1553645)** → **Validation**. Points re-pointed (confirm with Adam): service-mapping user stories 5 pts → **1 pt each**; service-mapping spikes 3 pts → **1 pt each**. Net-new items: **1402555** (Spike, 3 pts, Active, Stan Tomberg, under Feature 1356646 ≥90% coverage, Iter 3.1); **1560527** "CMDB: Fix credentials for Linux Servers" (3 pts, Ready DoR, Stan Tomberg, under Feature 1554951, Iter 3.1); **1571603** "Linux Discovery Credential Issues" (8 pts, Active, Jeff Schwartzskopf, under Feature 1554951 per Manuel, Iter 3.1 — ADO parent not yet shown); four new PLACEHOLDER service-mapping stories **1558187/1558192/1558197/1558202** (1 pt each, New, Michael Allison, under Feature 1517650, Iter 3.1).
**Revision 2026-08-06 (cont'd — ADO board export, sorted by Work Item Type):** Anu created all 11 remaining certification stories — Databases (1517037): DB-1 1560066, DB-2 1560067, DB-3 1560068, DB-4 1560069, DB-5 1560071; Network Devices (1517040): NW-1 1560087, NW-2 1560089, NW-3 1560091, NW-4 1560093, NW-5 1560094, NW-6 1560096. Points match what was submitted exactly. Both files now `status: reconciled` — see [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]] and [[PI-3/pi3-cert-1517040-certify-network-devices-stories-dependencies]]. **All four certification features (Computers, Servers, Databases, Network Devices) are now fully reconciled in ADO.** Also from this export: PI-2 carryover Features 1554951/1557616/1553982 now show Feature-level rows with confirmed owners, resolving the 2026-08-05 query-scope gap (see note below). This export's view does not include an Iteration/Sprint column, so sprint assignments for the 11 new stories are not yet re-confirmed against ADO. Two open items from this export not yet reconciled anywhere: (1) net-new story **1393089** "CMDB: Requirement Gathering for Non-OT devices" (0 pts, Refinement Ready, no parent shown) — unclear which feature this belongs to; (2) Feature 1517005 (Mandatory Attribute Population — Network Devices) now shows **8** stories, not 5 as previously logged — 3 net-new items (1560305, 1560306, 1560308) covering Support Group / Technical Group Owner / Environment population — not yet written up in [[PI-3/pi3-network-discovery-feature-breakdown]].
**Revision 2026-08-06:** Story-creation requests for the remaining two certification features sent to Anu: Feature 1517037 (Databases, 5 stories) and Feature 1517040 (Network Devices, 6 stories). Both submitted with small sprint/points adjustments from the reference drafts — see [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]] and [[PI-3/pi3-cert-1517040-certify-network-devices-stories-dependencies]] revision notes for detail. ADO IDs not yet assigned — reconcile this file once confirmed. All four certification features (Computers, Servers, Databases, Network Devices) now have story-creation requests in flight or complete.
**Revision 2026-08-05 (cont'd):** Full-board ADO export (sorted by Iteration Path, 3.1–3.5) confirmed the PI-2 carryover objective's ADO ID — **1557673** — and surfaced Planned Value scores for all 5 objectives (8/9/7/6/5). See "Full Board Reconciliation" section below for corrections (CC-1 actually 3.1 not 3.2; service-mapping spikes span 3.1–3.3, not just 3.1) and net-new items (story 1557701 under Network Discovery; 9 of ~10 BA-migration stories already created under Feature 1537867, contradicting its prior "not yet in ADO" status). Two possible duplicate-story pairs flagged for ADO confirmation, not resolved here.
**Revision 2026-08-05:** New PI-2 carryover objective confirmed in ADO — "Close PI-2 carryover: (database discovery and Azure Airlift CMDB support)" — with 3 features: 1554951 (Database Class Clean up and Populate Missing Attributes), 1557616 (CMDB Support for Air Lift - PI3), 1553982 (Governance model for requesting New Business Applications PI3). Objectives updated 4→5, features 12→15. Known ADO issues noted in Reconciliation section. Iteration assignments for 4 database stories (1504309/1504316/1504318/1504320) pending — to be updated when confirmed.
**Revision 2026-07-22:** ADO re-sequenced feature sprint assignments — features now span 3.1–3.5 (previously front-loaded in 3.1–3.4). CO6 compliance re-checked below.

---

## Objectives (5)

| ADO ID | Objective | Planned Value | Owner | State | Maps to CO6 |
|--------|-----------|---------------|-------|-------|-------------|
| 1516954 | Automate Network Device Discovery in the CMDB | 8 | Vazquez, Manuel (Contractor) | New | CO6 Obj 4 |
| 1516955 | Build & Validate Service Maps for Priority Business Apps | 9 | Adam Griffis | New | CO6 Obj 5 |
| 1516956 | Certify CMDB Data Across the Four Major CI Classes | 7 | Vazquez, Manuel (Contractor) | New | CO6 Obj 3 |
| 1516957 | Activate the ServiceNow → Qualys Attribute Sync in Production | 6 | Vazquez, Manuel (Contractor) | New | CO6 Obj 2 |
| 1557673 | Close PI-2 carryover: (database discovery and Azure Airlift CMDB support) | 5 | Vazquez, Manuel (Contractor) | New | Non-CO6 team commitment |

**Objective descriptions** (from PI Planning deck, Jul 22):

| ADO ID | One-line description |
|--------|----------------------|
| 1516954 | Automated credentialed discovery of all network device types, mandatory attribute population, and ≥90% owner-validated coverage. |
| 1516955 | Owner-validated Silver- and Gold-tier service maps, with ≥75% of the business-service inventory represented. |
| 1516956 | End-to-end data certification — process, PROD build, dashboards, training — across Computers, Servers, Databases, Network Devices. |
| 1516957 | One-way ServiceNow → Qualys sync of owner, support group, and SOX flag, live in production on a defined schedule. |

---

## Features by Objective (11)

### Automate Network Device Discovery in the CMDB — 1516954 (CO6 Obj 4)
Owner: Vazquez, Manuel (Contractor) · Breakdown: [[PI-3/pi3-network-discovery-feature-breakdown]]

| ADO ID | Feature | Owner | State | Iteration | Start | CO6 Delivery |
|--------|---------|-------|-------|-----------|-------|--------------|
| 1516993 | Automated Credentialed Discovery Live — All Network Device Types | Vazquez, Manuel (Contractor) | Defining | 3.1 | 8/5/2026 | Aug 31, 2026 |
| 1517005 | Mandatory Attribute Population via Discovery — Network Devices | Vazquez, Manuel (Contractor) | New | 3.3 | 9/2/2026 | Sep 30, 2026 |
| 1356646 | Network Inventory Coverage Reconciliation & Owner Validation (≥90%) | Vazquez, Manuel (Contractor) | New | 3.5 | 9/30/2026 | Oct 30, 2026 — 5 stories (CR-1..CR-5) created 2026-08-05, see [[PI-3/pi3-nd-1356646-stories-dependencies]]. Net-new 2026-08-19: Spike **1402555** "CMDB: Identify CI classes to be included in group 1" (3 pts, Active, Tomberg, Stan) placed in Iter **3.1** — likely early-discovery prep work ahead of the 3.5 feature. |

### Build & Validate Service Maps for Priority Business Apps — 1516955 (CO6 Obj 5)
Owner: Adam Griffis · Breakdown: [[PI-3/pi3-service-mapping-feature-breakdown]]

| ADO ID | Feature | Owner | State | Iteration | Start | CO6 Delivery |
|--------|---------|-------|-------|-----------|-------|--------------|
| 1537867 | Migration of Business Apps to Application Services (data-quality prerequisite; breakdown: [[PI-3/pi3-ba-to-service-instance-migration-feature-breakdown]]) | Vazquez, Manuel (Contractor) | New | 3.1 | 8/5/2026 | n/a (data-quality enabler, not a CO6 gate) |
| 1517650 | Silver-Tier Service Maps (App → Infrastructure) + ≥75% Business-Service Inventory | Adam Griffis | Defining | 3.1 | 8/5/2026 | Aug 31, 2026 |
| 1517655 | Gold-Tier Service Maps (Service → App) + Silver Validation Pass | Adam Griffis | New | 3.3 | 9/2/2026 | Sep 30, 2026 |
| 1518000 | Remaining Contractor-Managed Silver-Tier Maps + All-Silver Service → App Layer | Adam Griffis | New | 3.5 | 9/30/2026 | Oct 30, 2026 |

### Certify CMDB Data Across the Four Major CI Classes — 1516956 (CO6 Obj 3)
Owner: Vazquez, Manuel (Contractor) · Breakdown: [[PI-3/pi3-data-certification-feature-breakdown]]
Story + dependency drafts (SAFe), all four classes:
- **1517029** Computers → [[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]] (5 stories + 6 deps)
- **1517032** Servers → [[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]] (5 stories + 7 deps)
- **1517037** Databases → [[PI-3/pi3-cert-1517037-certify-databases-stories-dependencies]] (5 stories + 6 deps; all 5 created in ADO 2026-08-06, see below)
- **1517040** Network Devices → [[PI-3/pi3-cert-1517040-certify-network-devices-stories-dependencies]] (6 stories + 5 deps; highest-risk — depends on Obj 4 1517005; all 6 created in ADO 2026-08-06, see below)

| ADO ID | Feature | Owner | State | Iteration | Start | CO6 Delivery |
|--------|---------|-------|-------|-----------|-------|--------------|
| 1517029 | Certify Computers — CMDB Data Certification | Vazquez, Manuel (Contractor) | New | 3.2 | 8/19/2026 | Sep 30, 2026 |
| 1517032 | Certify Servers — CMDB Data Certification | Vazquez, Manuel (Contractor) | New | 3.2 | 8/19/2026 | Sep 30, 2026 |
| 1517037 | Certify Databases — CMDB Data Certification | Vazquez, Manuel (Contractor) | New (feature-level; stories now Active/Ready DoR as early as 3.2 — see 2026-08-19 pull-forward note) | 3.4 | 9/16/2026 | Oct 30, 2026 |
| 1517040 | Certify Network Devices — CMDB Data Certification | Vazquez, Manuel (Contractor) | New (feature-level; stories now Active/Refinement Ready as early as 3.2 — see 2026-08-19 pull-forward note) | 3.4 | 9/16/2026 | Oct 30, 2026 |

### Close PI-2 carryover: database discovery and Azure Airlift CMDB support — 1557673 (Non-CO6 team commitment)
Owner: Vazquez, Manuel (Contractor) · Planned Value 5

> ✅ **Resolved 2026-08-06:** the 2026-08-05 query-scope gap below is closed — a 2026-08-06 board export (sorted by Work Item Type) shows Feature-level rows for all three, with owners and states confirmed: 1554951 (Vazquez, Manuel — Active), 1557616 (Laurent, Israel Shlomi — Active), 1553982 (Dames, Joe — Active).
>
> ⚠️ **2026-08-05 ADO query note:** the 2026-08-05 PI-3 board export (sorted by Iteration Path) confirms Objective 1557673 and several of the stories below (1512084, 1553978, 1553980), but does **not** show Feature-level rows for 1554951, 1557616, or 1553982 themselves. Likely a view/query scope limit rather than removal (their child stories still show the matching parent titles) — confirm directly in ADO rather than treating this as a deletion.

| ADO ID | Feature | Owner | State | Iteration | Start | Notes |
|--------|---------|-------|-------|-----------|-------|-------|
| 1554951 | CMDB: Database Class Clean up and Populate Missing Attributes | Vazquez, Manuel (Contractor) — confirmed 2026-08-06 | Active | 3.1 | 8/5/2026 | 4 stories in PI2/Iter 2.6 — iterations pending update; 1 story (1512084) confirmed misplaced in ADO (Computer Class item — needs reparenting; still misplaced as of 2026-08-06 export) |
| 1557616 | CMDB Support for Air Lift - PI3 | Laurent, Israel Shlomi (Contractor) — confirmed 2026-08-06 | Active | 3.1 | 8/5/2026 | 2 Airlift stories (During 1418618, Post 1418621) + 1 Next Action Points story (1509235, still in PI2/Iter 2.6); Pre-Migration (1418610) not carried into PI-3 |
| 1553982 | Governance model for requesting New Business Applications PI3 | Dames, Joe (Contractor) — confirmed 2026-08-06 | Active | 3.1 | 8/5/2026 | 2 stories: 1553978 (Service Catalog), 1553980 (Modify SR SOX-Flagged CI Handling) — both Iter 3.1 |

**Stories — Feature 1554951 (Database Class Clean up and Populate Missing Attributes):**

| ADO ID | Story | Iteration | Notes |
|--------|-------|-----------|-------|
| 1504309 | CMDB: Database — Populate Environment Attribute | **3.2** (confirmed 2026-08-19) | 1 pt, Ready DoR, de Araujo Anthony |
| 1504316 | CMDB: Database — Populate Support Group | **3.2** (confirmed 2026-08-19) | 1 pt, Ready DoR, de Araujo Anthony |
| 1504318 | CMDB: Database — Populate SOX Indicator | **3.2** (confirmed 2026-08-19) | 1 pt, Ready DoR, de Araujo Anthony |
| 1504320 | CMDB: Database Clean up — IP address and Location | **3.2** (confirmed 2026-08-19) | 3 pts, Ready DoR, de Araujo Anthony |
| 1512084 | CMDB: Populate Assigned to field in Computer Class | 3.1 | ⚠️ Misplaced — this is a Computer Class story; should not be under Database feature. ADO reparenting needed. Confirmed still misplaced in 2026-08-05 and 2026-08-19 exports — 2 pts, State: Active. |
| 1560527 | CMDB: Fix credentials for Linux Servers | 3.1 | Net-new as of 2026-08-19 — 3 pts, State: Ready DoR, Tomberg, Stan. |
| 1571603 | Linux Discovery Credential Issues | 3.1 | Net-new as of 2026-08-19 — 8 pts, State: Active, Schwartzskopf, Jeff. No ADO parent shown; confirmed by Manuel as belonging to this feature. ADO reparenting needed. |

**Stories — Feature 1557616 (CMDB Support for Air Lift - PI3):**

| ADO ID | Story | Iteration | Notes |
|--------|-------|-----------|-------|
| 1418618 | Airlift to Azure — During Migration | 3.1 | PI-2 carryover |
| 1418621 | Airlift to Azure — Post-Migration | 3.1 | PI-2 carryover |
| 1509235 | CMDB: Next Action Points | PI2/Iter 2.6 | Needs iteration assignment review |
| ~~1418610~~ | ~~Airlift to Azure — Pre-Migration~~ | — | Not carried into PI-3 |

**Stories — Feature 1553982 (Governance model for requesting New Business Applications PI3):**

| ADO ID | Story | Iteration | Notes |
|--------|-------|-----------|-------|
| 1553978 | CMDB: Service Catalog for New Business Application / Update Business Application | 3.1 | 1 pt, State: Active (confirmed 2026-08-05) |
| 1553980 | CMDB: Modify SR SOX-Flagged CI Handling (Governed) | 3.1 | 1 pt, State: Active (confirmed 2026-08-05) — likely the "Story B" governed-SOX-handling item from the [[PPL CMDB-CSDM/Memory\|2026-07-10 Key Decision]] |

> ⚠️ **Possible duplicate stories (2026-08-05 ADO export):** two pairs of items share near-identical titles with **no parent feature shown** on one member of each pair — these look like they may be orphaned duplicates of the correctly-parented stories above, but could also be distinct items; **confirm in ADO before treating either as redundant**:
> - **1508982** "CMDB:Service Catalog for New Business Application/Update Business Application" — 1 pt, Active, Iter 3.1, no parent shown (vs. **1553978**, same title, parented to 1553982)
> - **1513944** "CMDB:Modify SR SOX-Flagged CI Handling (Governed)" — 1 pt, Ready DoR, Iter 3.1, no parent shown (vs. **1553980**, same title, parented to 1553982)

---

### Activate the ServiceNow → Qualys Attribute Sync in Production — 1516957 (CO6 Obj 2)
Owner: Vazquez, Manuel (Contractor) · Breakdown: [[PI-3/pi3-qualys-integration-feature-breakdown]]

| ADO ID | Feature | Owner | State | Iteration | Start | CO6 Delivery |
|--------|---------|-------|-------|-----------|-------|--------------|
| 1517065 | Activate ServiceNow → Qualys Attribute Sync (PROD) | Tomberg, Stan (Contractor) | Defining | 3.1 | 8/5/2026 | Sep 30, 2026 |

---

## Features by Iteration (load view)

| Iteration | Start | Features |
|-----------|-------|----------|
| 3.1 | 8/5/2026 | 1516993, 1517650, 1517065, 1537867 (CO6) + 1554951, 1557616, 1553982 (PI-2 carryover) = 7 total |
| 3.2 | 8/19/2026 | 1517029, 1517032 (2) |
| 3.3 | 9/2/2026 | 1517005, 1517655 (2) |
| 3.4 | 9/16/2026 | 1517037, 1517040 (2) |
| 3.5 | 9/30/2026 | 1356646, 1518000 (2) |

---

## CO6 Delivery Gates — Compliance Check (2026-07-22)

Each feature delivers a CO6 acceptance criterion with a fixed completion date. Check: does each feature's assigned sprint close on/before its CO6 delivery date?

| CO6 gate | Features | Latest sprint | Sprint ends | Verdict |
|----------|----------|---------------|-------------|---------|
| Aug 31, 2026 | 1516993, 1517650 | 3.1 | Aug 18 | ✅ ahead (13 days) |
| Sep 30, 2026 | 1517065, 1517029, 1517032, 1517005, 1517655 | 3.3 | Sep 15 | ✅ ahead (15 days) |
| Oct 30, 2026 | 1517037, 1517040, 1356646, 1518000 | 3.5 | Oct 13 | ✅ ahead (17 days) |

**Result: PASS** — the ADO schedule fits within CO6. Every feature completes in a sprint that closes before its CO6 delivery date. The two Aug 31 items stayed in Sprint 3.1 (the only tight gate). The Oct 30 gates fall after PI-3 close (Oct 27); those features complete by Sprint 3.5 (Oct 13), leaving the 3.6 IP iteration (Oct 14–27) as validation/hardening buffer before the external date.

**Note:** this table covers the 11 CO6-gated features only. Feature **1537867** (Migration of Business Apps to Application Services, Iteration 3.1) is intentionally excluded — it is a data-quality enabler for the Service Mapping objective, not a CO6 acceptance-criteria gate, so it has no delivery date to check against.

---

## CO6 Traceability

| CMDB/CSDM ADO Objective | CO6 Objective | In CMDB/CSDM focus area? |
|-------------------------|---------------|--------------------------|
| Automate Network Device Discovery in the CMDB (1516954) | Obj 4 — Automate Network Device Discovery | Yes |
| Build & Validate Service Maps for Priority Business Apps (1516955) | Obj 5 — Build Service Maps for Business Applications | Yes |
| Certify CMDB Data Across the Four Major CI Classes (1516956) | Obj 3 — Expand CI Data Certification | Yes |
| Activate ServiceNow → Qualys Attribute Sync in Production (1516957) | Obj 2 — Activate Qualys Integration | Yes |
| — | Obj 1 — Sustain ServiceNow Platform Operations | No (outside CMDB/CSDM focus) |
| — | Obj 6 — NERC-CIP ServiceNow Platform Strategy | No (outside CMDB/CSDM focus) |
| — | Obj 7 — Legacy Platform Migration | No (outside CMDB/CSDM focus) |

Full CO6 objective detail and acceptance criteria: [[PI-3/pi3-objectives]].

---

## Sprint 3.1 — Stories & Spikes Snapshot (as of 2026-08-03)

Full point count from the ADO board, Iteration 3.1, sorted by parent. **Supersedes the earlier 2026-07-31 story-level notes** below for point values (several items were re-pointed during refinement) and adds a large backlog under 1517650 that did not exist as of 2026-07-31.

| Parent feature | Items | State (as of 2026-08-19) | Points each | Subtotal |
|---|---|---|---|---|
| 1516993 — Automated Credentialed Discovery Live | 1526911 (ND-1, 5 pts), 1526951 (ND-3, 2 pts), 1557701 (ND-6, 3 pts) | **Validation** | 5 / 2 / 3 | 10 |
| 1516993 — Automated Credentialed Discovery Live | 1526947 (ND-2, 1 pt) | **Active** | 1 | 1 |
| 1517032 — Certify Servers | 1535496 (SV-1, 2 pts) | **Resolved** | 2 | 2 |
| 1517029 — Certify Computers | 1535486 (CC-1, 2 pts) | **Validation** | 2 | 2 |
| 1517037 — Certify Databases | 1560066 (DB-1, 2 pts) | **Resolved** | 2 | 2 |
| 1517040 — Certify Network Devices | 1560087 (NW-1, 5 pts) | **Resolved** | 5 | 5 |
| 1517065 — Qualys Sync | 1428703 (1 pt) | **Validation** | 1 | 1 |
| 1537867 — BA → Service Instance Migration | 1553645 (S01, 8 pts) | **Validation** | 8 | 8 |
| 1537867 — BA → Service Instance Migration | 1553653 (S07, 8 pts) | **Ready DoR** | 8 | 8 |
| 1517650 — Silver-Tier Service Maps | 1547758 (DocuFind), 1547760 (Documentum), 1547762 (GeoDigital) (3 Spikes in 3.1 — re-pointed) | **New** | 1 each | 3 |
| 1517650 — Silver-Tier Service Maps | 1543982, 1547081, 1547086, 1547091, 1547212, 1547217, 1547283, 1547304, 1547310, 1547324, 1547513 (11 User Stories — re-pointed from 5 to 1 pt each) | **Validation** | 1 each | 11 |
| 1517650 — Silver-Tier Service Maps | 1558187, 1558192, 1558197, 1558202 (4 PLACEHOLDER stories — net-new) | **New** | 1 each | 4 |
| 1554951 — DB Class Clean up | 1512084 (2 pts, ⚠️ misplaced Computer Class item) | **Active** | 2 | 2 |
| 1554951 — DB Class Clean up | 1560527 "Fix credentials for Linux Servers" (3 pts, net-new) | **Ready DoR** | 3 | 3 |
| 1554951 — DB Class Clean up | 1571603 "Linux Discovery Credential Issues" (8 pts, net-new, no ADO parent shown — confirmed by Manuel) | **Active** | 8 | 8 |
| **Total (Sprint 3.1 items in this view)** | | | | **~70** (service-mapping re-pointing reduced total significantly from prior 107 estimate) |

**Note:** the 1517650 spikes/stories carry a different Area Path (`A-INFOPS\CMDB-CSDM` / `A-INFOPS\CMDB-CSDM\CSDM`) than the Network Discovery / Servers items (`A-INFOPS\CMDB-CSDM`) — worth confirming whether the CSDM sub-team's items roll up into the same CMDB/CSDM PI-3 reporting as the rest of this tracking file. This view may not show every 3.1 item (table could extend past the last row captured) — treat 107 as a floor, not a confirmed final count.

**Also confirmed in this view:** ADO Work Item Type for 1526911/1526947/1526951/1526959/1526973 is plain **User Story**, not the "Enabler – Infrastructure/Configuration" types drafted in [[PI-3/pi3-nd-1516993-stories-dependencies]] — a naming drift between the plan and what was actually created, doesn't affect points.

---

## Full Board Reconciliation — Iterations 3.1–3.5 (as of 2026-08-05)

A fuller ADO export (sorted by Iteration Path, spanning the whole PI rather than just 3.1) surfaced corrections and net-new items. Full story-level detail lives in the per-feature files (updated alongside this); this section records what changed and why. Treat this export as the fullest view captured so far, not a guaranteed-complete one — it ends at Feature 1518000 (Iteration 3.5).

**Corrections:**
- **CC-1 (1535486)** is actually **Iteration 3.1**, not 3.2 as logged in the 2026-07-31 reconciliation note in [[PI-3/pi3-cert-1517029-certify-computers-stories-dependencies]] — CC-1 was never delayed; the CC-5-ahead-of-CC-4 sequencing flag there still stands. Also: CC-1 and SV-1 (1535496) both show ADO Work Item Type **Spike**, not User Story as drafted — naming drift only, doesn't affect points.
- **ND-2 (1526947)** shows **1 point** in this export, not 2 as logged in the Sprint 3.1 snapshot above — likely re-pointed during refinement; reconfirm before treating as final.
- **1517650 spikes span Sprints 3.1–3.3**, not just 3.1 as the snapshot above implied: 3 in Sprint 3.1 (GeoDigital 1547762, DocuFind 1547758, Documentum 1547760), 13 in Sprint 3.2, 5 in Sprint 3.3 — **21 spikes total visible**, more than the 11 captured 2026-08-03.

**Net-new items surfaced:**
- **1557701** "CMDB: Analysis of Network ranges" — 2 pts, **State: Validation**, parent Feature 1516993 (Automated Credentialed Discovery Live), Iteration 3.1. Documented as ND-6 in [[PI-3/pi3-nd-1516993-stories-dependencies]].
- **1526959 and 1526973 removed from ADO (confirmed 2026-08-05 by Manuel)** — these were ND-4 (Load Balancers/WAPs/Network Controllers discovery validation) and ND-5 (discovery scheduling automation) under Feature 1516993. Feature 1516993 now has 4 live stories (ND-1, ND-2, ND-3, ND-6), down from 5. ⚠️ No replacement stories exist yet — 3 of the 6 in-scope device types and the "auto-updated without manual intervention" Aug 31 acceptance criterion are currently unstaffed. See [[PI-3/pi3-nd-1516993-stories-dependencies]] for full detail.
- **Feature 1517005 (Mandatory Attribute Population) stories now fully visible** with points/state: 1537633 (3 pts, New, 3.3), 1537635 (3 pts, New, 3.3), 1537636 (3 pts, New, 3.3), 1537637 (New, 3.4), 1537638 (New, 3.4) — confirms the 5-story count already logged in [[PI-3/pi3-network-discovery-feature-breakdown]] Feature 2.
- **Feature 1537867 (BA → Service Instance migration) already has stories created in ADO** — contradicts [[PI-3/pi3-ba-to-service-instance-migration-feature-breakdown]]'s current "drafted outside ADO, not yet created" status. 9 stories confirmed: 1553645 (S01, 8 pts, Ready DoR, 3.1), 1553653 (S07, 8 pts, Ready DoR, 3.1), 1553646 (S02, 8 pts, New, 3.2), 1553656 (S09 spike, 1 pt, New, 3.2), 1553648 (S04, 3 pts, New, 3.3), 1553649 (S10, 5 pts, New, 3.3), 1553651 (S05, 8 pts, New, 3.3), 1553652 (S06, 3 pts, New, 3.4), 1553654 (S08, 5 pts, New, 3.4). **S03 not visible in this export** — confirm whether it exists or was intentionally skipped.

---

## Reconciliation Notes (confirm in ADO)

- **1356646** carries a work-item ID from a much lower range than the other PI-3 items (1.35M vs 1.51M) — likely a pre-existing item pulled into PI-3. Confirm it is the intended Feature.
- **1356646** now sits in **Iteration 3.5** with start **9/30/2026** (per ADO re-sequencing, 2026-07-22) — consistent with the 3.5 window (Sep 30 – Oct 13); CO6 delivery Oct 30. (Earlier 3.4 / 9-16 placement superseded.) — resolved
- **1512084 misplaced** — "CMDB: Populate Assigned to field in Computer Class" is a child of Feature 1554951 (Database Class Clean up) in ADO, but it is a Computer Class story, not a database story. Needs reparenting in ADO to the correct parent feature. — **open / ADO correction required**
- ~~**1504309 / 1504316 / 1504318 / 1504320** — four database stories still showing PI2/Iteration 2.6 in ADO~~ — **resolved 2026-08-19**, all four confirmed Iteration 3.2.
- **1509235 (CMDB: Next Action Points)** — child of Airlift feature 1557616 but still in PI2/Iteration 2.6. Confirm whether this needs to move to a PI-3 iteration or be closed.
- **1418610 (Pre-Migration)** — intentionally not carried into PI-3. Pre-migration work was either completed or descoped. Record kept for traceability only.
- **Possible duplicate stories (2026-08-05 export)** — 1508982 / 1513944 (no parent shown) vs. 1553978 / 1553980 (parented to Feature 1553982), same titles respectively. May be orphaned duplicates or distinct items — confirm in ADO before treating either as redundant. — **open**
- **1554951 / 1557616 / 1553982 (PI-2 carryover Features)** — not visible as Feature-type rows in the 2026-08-05 export, though their Objective (1557673) and several child stories are. Likely a query/view scope limit, not a deletion — confirm directly in ADO. — **open**
- ~~**1557701 (Analysis of Network ranges)** — net-new story under Feature 1516993, State: Validation; not yet written up as ND-6~~ — **resolved**, documented as ND-6 in [[PI-3/pi3-nd-1516993-stories-dependencies]].
- **1526959 (ND-4) and 1526973 (ND-5) removed from ADO (confirmed 2026-08-05 by Manuel)** — Feature 1516993 now has 4 live stories, not 5/6. No replacement created yet for the Load Balancer/WAP/Network Controller discovery-validation work or the scheduling-automation work — CO6 Aug 31 gate coverage gap. — **open, needs replacement stories or scope decision**
- **S03 of Feature 1537867 (BA→Service Instance migration)** — not visible in the 2026-08-05 export; the other 9 stories (S01/S02/S04–S10) are confirmed created. Confirm S03 exists or was intentionally skipped. — **open**
- **1571603 "Linux Discovery Credential Issues"** (8 pts, Active, Jeff Schwartzskopf) — surfaced 2026-08-19 with no ADO parent shown. Manuel confirmed it belongs under Feature 1554951 (DB Class Clean up). Needs formal reparenting in ADO — currently orphaned in the system. — **open, ADO correction required**
- **Service-mapping re-pointing (2026-08-19)** — the 11 Silver-Tier Service Map user stories and the 3 spikes visible in this export now show **1 pt each**, down from 5 pts / 3 pts respectively as logged 2026-07-31/2026-08-05. This significantly reduces the feature's total point count from the ~93-point estimate implied by the earlier snapshot. Confirm with Adam Griffis whether this is a deliberate re-scoping/re-estimation or a data artifact of the current view. — **open**
- **Databases (1517037) and Network Devices (1517040) certification stories pulling forward from planned Sprint 3.4** — DB-2 (1560067), NW-2 (1560089), NW-3 (1560091) all confirmed **Iteration 3.2** in the 2026-08-19 export, ~2 sprints ahead of the drafted 3.4 start in both per-feature files. Not a compliance risk (more buffer to the Oct 30 gate) but the per-feature "Sprint reconciliation" sections should be re-confirmed and corrected once verified directly in ADO. — **open**
- **Governance duplicate pair still unresolved as of 2026-08-19** — 1508982 (dup of 1553978) and 1513944 (dup of 1553980) both still exist in ADO, Iteration 3.2, neither shows a parent feature. 1553980 itself now also shows no parent in this export (previously confirmed parented to 1553982) — likely the same view-scope limitation seen elsewhere in this file, not an actual removal. Confirm all four directly in ADO. — **open**
- **3 net-new stories with no parent shown (2026-08-19)** — 1563085 "Import Capabilities/Services," 1574773 "Import Business Applications," 1575789 "Sync Metal Tier field..." — likely Service Mapping (1516955) scope but unconfirmed. Also 1526856 Spike "Validate Server environment Integration Source Behind the Mandatory Designation" (Validation state, no parent) — likely tied to Server cert DEP-7. — **open, needs triage**
- **Geostan address-validation process note (2026-08-19)** — spike 1547764 ("DLC") carries the inline comment "We're no longer using Geostan for address validation" — a possible scope/process change for the Service Mapping data-source work, not just a title edit. Confirm with Adam Griffis. — **open**
- **Two new unmapped Features surfaced 2026-09-03** — 1595485 "CMDB - Role-Based Access and Permission Management" (7 stories) and 1595440 "CMDB - Workspace Enhancement" (11 stories), both New, no parent shown, no CO6/objective mapping confirmed. 1595485 likely maps to the "CMDB Role Matrix" initiative Sonika accepted 2026-09-02/03. — **open**
- **1574799's parent feature has no ID captured (2026-09-03)** — shown only as "Business Application / Business Capability / Services / Service Offerings Updates and Definition." Confirm whether this is Feature 1517655 (Gold-Tier Service Maps) under a different title or a separate item. — **open**
- **1571603 parent conflict (2026-09-03)** — shows parent Feature 1517650 (Silver-Tier Service Maps) in this export vs. Feature 1554951 (DB Class Clean up) per Manuel's 2026-08-19 confirmation. — **open**
- **1560566 and 1560878 (net-new Dependencies, 2026-09-03)** — need parent/feature triage; see revision note above. — **open**
- **1582669 and 1587385 (infrastructure items, 2026-09-03)** — MID Server health bug and CyberArk MID Server validation; confirm whether these belong in CMDB-CSDM PI-3 tracking or platform-ops. — **open**

---

## Maintenance

Update this file whenever ADO changes for the CMDB/CSDM PI-3 items: refresh the `State` column as items move (New → Active → Closed), add/remove features, and bump `as-of` / `updated`. This file is the reporting source for CMDB/CSDM PI-3 objective and feature status.
