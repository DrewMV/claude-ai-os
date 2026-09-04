---
type: dependency-tracker
workspace: Work
project: CMDB-CSDM
dependency-team: SailPoint / IAM
status: draft
updated: 2026-09-02
tags: [work, cmdb-csdm, dependencies, sailpoint, iam, sox, governance]
relationships:
  - target: "[[Backlog/service-instance-modify-storyA-core]]"
    type: blocked_by
  - target: "[[Backlog/service-instance-modify-storyB-sox]]"
    type: blocked_by
  - target: "[[PI-3/pi3-physical-computer-data-validation-stories]]"
    type: related_to
  - target: "[[csdm5-terminology]]"
    type: related_to
  - target: "[[co6-deliverable-tracking]]"
    type: related_to
---

# Dependencies — SailPoint / IAM

PPL is migrating identity governance onto **SailPoint IdentityIQ** (on-prem; confirmed by its own loop-back connector entry in the source list). The programme onboards **70 applications across 4 release waves**, and each application is stated to require CMDB prioritization first.

**Coordination owner:** **Jordan Yung** — recorded working "SailPoint alignment/escalation (CMDB/NPA use cases)" week of 2026-07-06/08. He is the entry point for scope questions.

> **Status: DRAFT — analysis only.** Built 2026-09-02 from *SailPoint Apps Needing CMDB Priority.xlsx* (source in `Downloads`, **not in vault** — same handling as [[Backlog/airlift-plan-evaluation]]). No ADO items created. The CMDB ask has **not** been confirmed with Jordan; see SP-5.

---

## Contacts

| Role | Name | Note |
|------|------|------|
| Coordination / escalation | Jordan Yung | Owns SailPoint alignment; key CO6+ scope resource |
| IAM POC | Pepper | Recorded POC for SOX-flagged CI ownership notification content/recipients |
| Cybersecurity (CCB) | Jason Dubreuil | CCB Consulting Member — Cybersecurity & Compliance |
| SOX distribution | ISDITCYBERCompliance@pplweb.com | Recipient list per story 1455827 acceptance criteria |
| ServiceNow Enhancements PO | JP Nair | Owns SailPoint→ServiceNow ticket fulfilment integration |

---

## Release waves

| Wave | Date | Apps | SOX App | SOX Tool | SOX Tool – Critical | Non SOX |
|---|---|---:|---:|---:|---:|---:|
| 8.24.26 Release | 2026-08-24 — **passed** | 5 | 0 | 0 | 0 | 5 |
| 2.1.27 Release | 2027-02-01 | 26 | 15 | 9 | 2 | 0 |
| 2.22.27 Release | 2027-02-22 | 20 | 8 | 7 | 5 | 0 |
| 3.15.27 Release | 2027-03-15 | 19 | 15 | 0 | 3 | 1 |
| **Total** | | **70** | **38** | **16** | **10** | **6** |

**OpCo split:** PA 46 · KY 23 · PA/RI/KY 1.
**Connector traits:** AD/Entra 40 · Disconnected 25 · JDBC 20 · aggregation-only 18 · retains SRS for access request 7.

### What the shape means

**Wave 1 was a deliberate low-risk pilot.** All 5 apps in the passed August wave are Non SOX (Cascade, Tanium, Lucidchart, TOA, Adobe Sign). The mechanism was proven on records auditors don't care about.

**Then a cliff.** 65 apps land in a **7-week window** (2027-02-01 → 2027-03-15), and 64 of 70 total are SOX-scoped (91%).

**This is a migration, not greenfield.** The list itself contains **RSA Identity Governance and Lifecycle**, **SRS (Security Request System)** and **IAM** as SOX Tool – Critical, and 7 entries note "access request stays with SRS." PPL is moving off RSA IGL + a homegrown request system onto SailPoint in stages, with SailPoint initially taking aggregation and certification while SRS retains access request.

**25 Disconnected apps mean ticket volume.** "Disconnected" = no automated provisioning; fulfilment is manual, typically via a ServiceNow ticket. That lands on ServiceNow ITSM (JP Nair's team) from Feb 2027, not on CMDB — but it is the same programme.

---

## ⚠️ Finding — ServiceNow itself is in scope, and it changes the Computer validation design

`SERVNW | ServiceNow | SOX Tool | AD` — **2.1.27 release.**

From Feb 2027, ServiceNow roles are aggregated, governed and **certified** in SailPoint as a SOX-scoped tool.

**Consequence for [[PI-3/pi3-physical-computer-data-validation-stories|PV-1]]:** granting `data_manager_user` + `sn_cmdb_editor` to ~21,000 employees would push ~21,000 entitlements into a SOX-scoped access-certification population, re-reviewed every cycle indefinitely. This converts PV-1's open licensing/role question into a **documented, dated reason to prefer the Service Catalog record producer** over broad role grants. Record as evidence in PV-1, not as an open question.

Also relevant: **AIM** and **CyberArk** both appear as SOX Tool – Critical. CyberArk/AIM credential work already touches CMDB Discovery (spike 1395085, "Install Cyberark AIM API on MID Servers", story 1387236) — those MID Server credential paths will be under SailPoint governance too.

---

## Dependencies (7)

Stated as **Problem** (why it blocks) + **Acceptance criteria** (what "resolved" looks like), per SAFe convention.

---

### SP-1 · Business Application enhancement pause vs. 70-app prioritization

| Field | Value |
|---|---|
| Assigned To | Manuel Vazquez → Joe Dames / Sonika Das |
| Priority | **1** |
| State | Open — **unreconciled contradiction** |
| Due Date | 2026-09-30 |

**Problem:** The 2026-06-10 decision paused **all** new Business Application enhancements pending the Application Services migration. This programme asks CMDB to prioritize 70 application records. Both positions cannot hold. Until reconciled, any SailPoint prep work either violates the pause or the pause silently blocks the programme.

**Acceptance criteria:**
- [ ] Decision recorded on whether SailPoint-driven application record work is an exception to the BA pause
- [ ] If an exception: scope of permitted work defined (create? ownership only? classification?) so it does not reopen general BA enhancement
- [ ] If not an exception: the Application Services migration completion date becomes a hard predecessor to wave 2 (2027-02-01) and is communicated to Jordan
- [ ] Reconciled against [[csdm5-terminology]] and the BA→Service Instance migration plan

---

### SP-2 · Story A blocks modification of SOX-flagged CIs — 64 of 70 apps are SOX-scoped

| Field | Value |
|---|---|
| Assigned To | Manuel Vazquez → Joe Dames |
| Priority | **1** |
| State | Open |
| Due Date | 2026-09-30 |

**Problem:** [[Backlog/service-instance-modify-storyA-core]] deliberately **blocks modification of SOX-flagged CIs** and keeps SOX fields read-only until [[Backlog/service-instance-modify-storyB-sox|Story B]] delivers the governed path (Option a, decided 2026-07-10 — chosen specifically to avoid an interim gap). **64 of these 70 applications are SOX-scoped.** If SailPoint onboarding requires ownership populated or corrected on them, CMDB's own governance design blocks the work.

Story B was targeted **early PI-3** and is blocked on Decision #2 (SOX approval vs. notification) and #3 (governance scope). PI-3 closes 2026-10-27.

**Acceptance criteria:**
- [ ] Confirm whether Story A's block covers the ownership fields SailPoint depends on (`owned_by` / `business_owner` / `it_application_owner`)
- [ ] Story B status confirmed and re-dated against the 2027-02-01 wave
- [ ] Decisions #2 and #3 closed with Joe/Compliance — they gate Story B, which gates this
- [ ] If bulk ownership population is required before Story B lands, an explicitly governed one-time path agreed (not a silent bypass of Story A)

---

### SP-3 · Sequence story 1455827 go-live against any bulk ownership work

| Field | Value |
|---|---|
| Assigned To | Manuel Vazquez |
| Priority | **1** |
| State | Open — **time-sensitive, this week** |
| Due Date | 2026-09-08 |

**Problem:** Story **1455827** sends a notification to **ISDITCYBERCompliance@pplweb.com** on every Business Owner or CI Owner change to a SOX-flagged CI. It is currently **Resolved, pending UAT by Manuel and Joe** (Kiran's request, 2026-08-19). If it goes live and bulk ownership population then runs across 64 SOX applications, the SOX distribution list is flooded with informational email — the classic way a well-designed notification gets muted or switched off.

Timing is still controllable **because** UAT hasn't happened. That advantage disappears once it deploys.

**Acceptance criteria:**
- [ ] Decision recorded: bulk-load ownership **before** 1455827 goes live, or notify Cyber Compliance ahead of the load, or suppress the notification for a defined bulk-change window
- [ ] Expected notification volume from SailPoint prep estimated and shared with the SOX distribution list owner
- [ ] Sequencing agreed with Kiran Dhobale before 1455827 deploys
- [ ] UAT completed and attached (clears the open item on Manuel — see [[Team/impediments-log]])

---

### SP-4 · Which CMDB class do SailPoint applications map to?

| Field | Value |
|---|---|
| Assigned To | Manuel Vazquez (w/ Stan Tomberg) |
| Priority | 2 |
| State | Open |
| Due Date | 2026-09-30 |

**Problem:** SailPoint governs "applications." CMDB has **Business Application** (strategic) and **Service Instance / Application Service** (operational), with a migration between them in flight and CSDM 5 terminology unresolved. Nobody has stated which class these 70 records live in. Story 1455827 is scoped to Application Service while referencing a **Business Owner** field that per [[Config-Mgmt-Plan/ownership-terminology-mapping]] belongs to Business Application — the same confusion, already in a built story.

This is the identical unresolved question blocking the NITSR feedback.

**Acceptance criteria:**
- [ ] Target class confirmed for SailPoint-governed applications
- [ ] Ownership field per class confirmed (`owned_by` / `business_owner` / `it_application_owner`) and reconciled with the terminology worksheet Q1/Q7
- [ ] Consistency confirmed with the BA→Service Instance migration so records are not built on a class about to be migrated
- [ ] Answer reused for the NITSR CI-class question rather than resolved twice

---

### SP-5 · Define what SailPoint actually needs from CMDB, per application

| Field | Value |
|---|---|
| Assigned To | Manuel Vazquez → Jordan Yung |
| Priority | **1** |
| State | Open — **blocks all planning** |
| Due Date | 2026-09-15 |

**Problem:** The source file lists OpCo, App Code, Application Name, SOX classification and Connector Type. It does **not** state what CMDB must deliver. "Needing CMDB Priority" is currently an **inference**: that each app needs an accurate CMDB record with populated ownership before SailPoint can onboard it, because SailPoint needs the app and its owner for approval routing and certification. That inference is unconfirmed, and without it "priority" is not actionable — no attribute list, no lead time, no definition of done.

**Acceptance criteria:**
- [ ] Confirm the CMDB ask with Jordan Yung — required attributes per application, and lead time needed ahead of each release date
- [ ] Confirm whether CMDB is authoritative for the app inventory, or SailPoint maintains its own and only consumes ownership
- [ ] Confirm what closed ADO **1426724** ("Create scripted REST API for SailPoint integration", Closed, Iter 2.2) actually delivered — it may already carry the data contract
- [ ] Confirm whether CMDB owes anything for the **NPA (Non-Person Account)** use cases Jordan escalated
- [ ] Resolve the unexplained **Feature 1411480 → "Create scripted REST API for SailPoint"** ADO parentage, flagged 2026-06-19 and never closed

---

### SP-6 · Application-to-CI crosswalk and duplicate resolution

| Field | Value |
|---|---|
| Assigned To | TBD (candidate: Anuradha Rai / Uloma Adelufosi) |
| Priority | 2 |
| State | Open |
| Due Date | 2026-10-31 |

**Problem:** SailPoint's app list does not obviously map 1:1 to CMDB records. **AIM appears twice** (KY Tools 2.1.27, PA Tools 2.22.27) and **CyberArk twice** (PA + KY, 3.15.27). There are three meter-data-management variants (MDMSCL, EnergyIP, SMP_MDMS), **Fieldnet** appears twice (base + RIE), and SMP_MDMS is flagged "(reopened)". Whether per-OpCo instances are one CI or two is an identification decision, and it is the same duplicate-CI problem NowAssist Phase 1 was scoped to attack.

Two systems each claiming to hold the authoritative application inventory is a known failure mode — and Enterprise Architecture (Sam Hamilton, Matt Newhouse) is separately cleaning up Business Application records.

**Acceptance criteria:**
- [ ] Crosswalk built: App Code → CMDB CI sys_id (or "no record exists")
- [ ] Per-OpCo duplicates dispositioned — one CI or two, with the rule recorded
- [ ] MDMS and Fieldnet variants resolved
- [ ] Gap list produced: apps with no CMDB record, apps with no owner, apps with ambiguous identity
- [ ] Coordinated with EA's BA cleanup so the two efforts do not contradict
- [ ] Overlap measured against the **BA Classification gap** (36% populated / 1,371 CIs) — do these 70 sit inside it?

---

### SP-7 · PI-4 capacity and CO7 contract scope

| Field | Value |
|---|---|
| Assigned To | Manuel Vazquez → Christian Aguilar Rodriguez / Jordan Yung |
| Priority | **1** |
| State | Open |
| Due Date | 2026-10-15 (ahead of PI-4 planning) |

**Problem:** **CO6 ends 2026-10-30.** All three major waves (2027-02-01, 02-22, 03-15) fall well outside it. This work is currently **unfunded and unscoped** in the change order. The Feb/Mar waves land in **PI-5**, which means CMDB preparation must be committed in the **PI-4** backlog — the next planning cycle, not this one.

Given how the CO5 holdback played out ($533,775 gated on final acceptance), an unbudgeted expectation arriving in PI-5 with no capacity allocation is a repeat of a pattern the team has already been burned by.

**Acceptance criteria:**
- [ ] SailPoint CMDB preparation raised with Christian for CO7 (or CO6 extension) scoping
- [ ] Effort estimated once SP-5 defines the ask
- [ ] PI-4 capacity allocation agreed before PI-4 planning
- [ ] Wave dates confirmed as firm or provisional — a 7-week compression of 65 apps invites slippage; know whether CMDB should plan to the stated dates
- [ ] Escalated as a risk to the RAID log if unfunded past 2026-10-30

---

## Sequence

```
SP-5 (what does SailPoint need? — Jordan) ── BLOCKS ALL PLANNING
   │
   ├─► SP-4 (which CMDB class?) ──┐
   │                               ├─► SP-6 (crosswalk + duplicates) ─► SP-7 (PI-4 / CO7 scope)
   ├─► SP-1 (BA pause exception?) ─┘
   │
   └─► SP-2 (Story A SOX block / Story B date)

SP-3 (1455827 sequencing) ── INDEPENDENT, act this week
```

**Critical path:** SP-5 → SP-4/SP-1 → SP-6 → SP-7, with PI-4 planning as the hard deadline.
**Act now regardless:** SP-3 — the timing advantage exists only until 1455827 deploys.

---

## Open questions

1. **Is the CMDB ask real, and is it ours?** SP-5. Patterns 1 and 3 (ticket fulfilment, catalog-fronted access request) belong to ServiceNow Enhancements under JP Nair; governance of ServiceNow roles belongs to IAM. CMDB's genuine exposure is only where SailPoint consumes CMDB data.
2. **Are the wave dates firm?** 65 apps in 7 weeks is aggressive. If they slip, CMDB prep priority slips with them — but planning to a date that moves is its own cost.
3. **What did the passed 2026-08-24 wave require of CMDB?** Five Non-SOX apps went live nine days before this analysis. Whether CMDB was asked for anything, and whether it was delivered, is the cheapest available evidence of what the real ask looks like.
4. **RSA IGL / SRS decommission** — both are in the onboarding list as SOX Tool – Critical. Are they being retired after migration? If so their CMDB records need lifecycle handling, and any CMDB integration pointing at them needs redirecting.
5. **NPA (Non-Person Account) use cases** — Jordan escalated these with CMDB named. Service-account governance typically needs application and ownership data. Scope unknown.

---

## Appendix — full application inventory (70)

Generated from the source workbook 2026-09-02. Columns as supplied.

### 8.24.26 Release — 5 applications

| OpCo | App Code | Application Name | SOX | Connector Type |
|---|---|---|---|---|
| PA | MNMS | MNMS - Cascade | Non SOX | JDBC (aggregation only) + Disconnected |
| PA/RI/KY | TAN | Tanium | Non SOX | AD |
| PA | LUCDCHRT | Lucidchart | Non SOX | AD |
| KY | TOA | TRANSMISSION OUTAGE APPLICATION (TOA) ACCESS | Non SOX | JDBC (aggregation only) + Disconnected |
| PA | ADBESIGN | Adobe Sign | Non SOX | EntraID |

### 2.1.27 Release — 26 applications

| OpCo | App Code | Application Name | SOX | Connector Type |
|---|---|---|---|---|
| PA | Sail | SailPoint IdentityIQ | SOX Tool | Loop back connector |
| PA Apps | ICSS | Integration Manager | SOX App | AD + JDBC (aggregation from DB) + Disconnected |
| KY Apps | Fieldnet | FIELDNET System | SOX App | JDBC (aggregation only) + Disconnected |
| KY Apps | Fieldnet RIE | FIELDNET System (RIE) | SOX App | JDBC (aggregation only) + Disconnected |
| KY Apps | MV90 | MV90 System | SOX App | AD + Disconnected (SFTP) |
| KY Apps | Webaccounting | OATI Webaccounting | SOX App | Disconnected |
| PA Apps | WHSETCL (Poweroptix) | RIE ELECTRIC WHOLESALE SETTLEMENT | SOX App | AD + Disconnected |
| KY Apps | ALIGNEKY | Aligne Fuels System | SOX App | JDBC (aggregation only) + Disconnected |
| KY Apps | SAPECC (Enterprise Core Component) | SAP ECC System | SOX App | Disconnected |
| PA Apps | HARTIGEN | HARTIGEN - POWEROPTIX | SOX App | AD + Disconnected -Delimited |
| PA Apps | HXGN EAM | Hexagon EAM | SOX App | AD |
| KY Tools | AIMKY | AIM | SOX Tool - Critical | AD |
| PA Tools | TRIPWIRE | TRIPWIRE | SOX Tool - Critical | AD |
| PA Apps | iEnergy | Resources Innovations iEnergy | SOX App | Disconnected |
| PA Apps | PAMDMS | PA Meter Data Management System | SOX App | AD |
| PA Apps | FISA | FIS Aligne - KY/RI | SOX App | AD + Disconnected |
| KY Apps | AFB | After the Fact Billing (AFB) | SOX App | AD |
| PA Apps | DPCORE | DATA PLATFORM CORE | SOX App | AD |
| KY Tools | GLBSCP | Globalscape | SOX Tool | AD |
| PA Tools | RPA2 | Robotic Process Automation | SOX Tool | AD |
| KY Tools | ESDFuels | ESDFuels System | SOX Tool | AD |
| PA Tools | CENTRIFY | CENTRIFY | SOX Tool | AD |
| PA Tools | CHSTY | Cohesity | SOX Tool | AD |
| PA | SERVNW | ServiceNow | SOX Tool | AD |
| KY Tools | ADSKY | Active Directory | SOX Tool | AD + SNOW ticket |
| PA Tools | CLOUD | CloudTeam | SOX Tool | AD |

### 2.22.27 Release — 20 applications

| OpCo | App Code | Application Name | SOX | Connector Type |
|---|---|---|---|---|
| PA Apps | CARA | EU Customer Data Mart | SOX App | AD |
| PA Apps | CARY | POLR Invoicing Data Mart | SOX App | AD |
| PA Apps | DPMN | DATA PLATFORM MODERNIZATION - NETEZZA | SOX App | AD |
| PA Apps | MDMSCL | RIE METER DATA MANAGEMENT SYSTEM (vendor SaaS) | SOX App | AD |
| PA Tools | INFA | INFORMATICA | SOX Tool | AD |
| KY Apps | EnergyIP | Energy IP MDMS | SOX App | JDBC (aggregation only) + Disconnected |
| PA Tools | MSTRAT | Microstrategy | SOX Tool | AD |
| PA Tools | AIM | AIM | SOX Tool - Critical | JDBC |
| PA Tools | IAM | IAM | SOX Tool - Critical | Disconnected + JDBC aggregation |
| PA Tools | RSAGOV | RSA Identity Governance and Lifecycle | SOX Tool - Critical | JDBC (aggregation only) + Disconnected |
| PA Apps | MS_FINHR | BMI Reporting and Time & Labor Data Marts | SOX App | AD (Aggregation only. Access will stay with SRS) |
| PA Tools | SRS | Security Request System | SOX Tool - Critical | JDBC (aggregation only) Access request remain in SRS. Certification is required |
| KY Tools | EMSNTDB | EMSNTDB | SOX Tool | Disconnected + JDBC aggregation |
| PA Tools | SNOW | Snowflake | SOX Tool - Critical | AAD |
| PA Tools | IDRCDC | InfoSphere Data Replication and CDC | SOX Tool | Disconnected |
| PA | DEVOPS | Microsoft DevOps | SOX Tool | AD |
| PA Apps | CSS1 | CSS1 | SOX App | JDBC + partial AD |
| PA Apps | CSSRI | CSSRI | SOX App | JDBC |
| PA Tools | PBI | Power BI | SOX Tool | AD (Complex) |
| KY Tools | SAPSM | SAP Central User Administration (CUA) & Solution Manager (Version 7.2) | SOX Tool | Disconnected |

### 3.15.27 Release — 19 applications

| OpCo | App Code | Application Name | SOX | Connector Type |
|---|---|---|---|---|
| PA Apps | Cadency | Trintech Cadency | SOX App | AD + Disconnected |
| PA Apps | DOA | Delegation of Authority | SOX App | JDBC (aggregation only) + Disconnected |
| KY Apps | Commodity Trading System (CTS) / After the Fact Billing (AFB) | CTS - Commodity Trading System | SOX App | AD |
| KY Apps | SAPBW (Business Warehouse) | SAP BW System | SOX App | Disconnected |
| PA Apps | QUANTUM | QUANTUM | SOX App | Aggregate only with CSV, Access request stay with SRS |
| PA Apps | TRAX | FIS TRAX centraliozed payment factory and hub solution "SaaS" | SOX App | Aggregate only with CSV, Access request stay with SRS |
| PA Apps | ORCLFCC | Oracle Financial Consolidation and Close - SaaS solution | SOX App | AD |
| KY Apps | ORCLEBUS | Oracle eBusiness Suite System | SOX App | JDBC aggregation |
| KY Apps | POWERPLNKY | PowerPlan System | SOX App | Disconnected |
| PA Apps | BMI | Business Management Information | SOX App | JDBC aggregation only & Certification, access request remain in SRS |
| KY Apps | PeopleSoft | PeopleSoft System | SOX App | JDBC + Disconnected |
| PA Apps | HCM | Human Capital Management | SOX App | Aggregation only with CSV+AD. Access will stay with SRS |
| PA Apps | INFOR | INFOR Asset Management SaaS solution | SOX App | AD + disconnected |
| PA apps | SMP_MDMS | Meter Data Management System(reopened) | SOX App | Access Request in SRS |
| PA Tools | CYBERARK | CyberArk | SOX Tool - Critical | AD |
| KY Tools | Cyberark | CyberArk | SOX Tool - Critical | AD |
| KY Apps | VOLTS | Virtual Online Time Systems (VOLTS) System | SOX App | JDBC |
| PA Tools | DISCO | DISCO | SOX Tool - Critical | JDBC |
| KY | BUSINESS INTELLIGENCE | BUSINESS INTELLIGENCE | Non SOX | AD + Multiple Owner group for approval |
