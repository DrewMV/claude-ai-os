---
type: team-artifact
workspace: Work
project: CMDB-CSDM
pi: PI-2
updated: 2026-06-12
tags: [work, cmdb-csdm, backlog, validation]
---

# PI-2 Story Validation Worksheet

**Purpose:** Validate the status of every known PI-2 work item against ADO so the leadership scorecard statistics become ADO-true instead of derived.

**6/12 update:** State / Pts / Assigned filled from the **6/12 12:00pm story pull** (authoritative) + the 6/11 board snapshot for items the 12pm pull didn't cover. Where the two disagreed, the **6/12 pull wins**. ⚠️ No stories are confirmed Done — the 6/11 board's two "Done" items proved unreliable (1407572 = Validation at 12pm; 1413033 absent from 12pm pull).

**How to fill (you or Anu):**
1. Open the matching CSV (`pi2-story-validation-worksheet.csv`) in Excel — or pull an ADO query and paste values.
2. Fill the three blank columns: **State** (New / Active / Resolved / Closed / Removed), **Story Points**, **Assigned To**.
3. For rows with a blank **ADO ID**, add the ID from ADO (these are the items Anu still owes us).
4. The **Notes** column is my *current assumption* — correct it where wrong; it is not authoritative.
5. Return it and I'll re-ingest to rebuild the scorecard with real counts (Done / In-Progress / Blocked) and velocity.

**Fastest path:** an ADO query (`Area Path = CMDB-CSDM`, `Iteration ∈ 2.1/2.2/2.3`) exported with columns ID, Title, Type, State, Story Points, Iteration, Parent, Assigned To.

> 🔴 = highest validation priority. Rows with no ADO ID block counting entirely.

| Pri | Objective | Parent Feature | ADO ID | Type | Title | State | Pts | Assigned To | Notes (current assumption — verify/replace) |
|-----|-----------|---------------|--------|------|-------|-------|-----|-------------|----------------------------------------------|
| P0 | Airlift | 1420613 | 1418610 | Story | Airlift to Azure – Pre-Migration | Validation |  | Laurent / Alex Lim | Board state (not in 6/12 pull) |
| P0 | Airlift | 1420613 | 1418618 | Story | Airlift to Azure – During Migration | Validation |  | Laurent / Alex Lim | Board state |
| P0 | Airlift | 1420613 | 1418621 | Story | Airlift to Azure – Post-Migration | Validation |  | Laurent / Alex Lim | Board state |
| P0 | Airlift | 1420613 | 1416384 | Story | Auto Populate CI Owner / Support Group / Tech Owner for Server Class | _(not on board)_ |  |  | Not in either pull; virtual variant 1407572 = Validation (not Done) |
| P1 | Discovery/SCCM | 1383523 | 1421790 | Spike | Gap Analysis for Servers – Linux & Windows | Active | 0 | Tony De Araujo | ⚠️ ADO parent shows 1354797 (Server Class), not 1383523 |
| P1 | Discovery/SCCM | 1356646 | 1402555 | Spike | Identify CI Classes for Group 1 | Ready DoR | 3 | Stan + Joe | Pts 2 → 3 |
| P1 | Discovery/SCCM | 1356826 | 1403763 | Story | SCCM Server Hardware & Software Attribute Data Precedence | Validation | 1 | Vinay | 6/12: Active → Validation |
| P1 | Discovery/SCCM | 1356826 | 1403760 | Story | SCCM: Servers – Domain and Network Attribute Data Precedence | Validation | 1 | Vinay | 6/12: Active → Validation |
| P1 | Discovery/SCCM | 1356826 | 1403762 | Story | SCCM: Servers – Last Seen Timestamp Alignment | Validation | 1 | Vinay | Was BLOCKED → Validation; Blocked=No (gate cleared) |
| P1 | Discovery/SCCM | 1356826 | 1403759 | Spike | SCCM: Servers – De-Prioritize Attributes (asset tag, OU name) | Validation | 1 | Vinay | Was ON HOLD → Validation |
| 🔴 P1 | Discovery/SCCM | 1354797 | _(needed)_ | Story | CI Auto-Population – CI Owner |  |  |  | **ID NEEDED**; may be Closed (showback-accepted 6/8) |
| 🔴 P1 | Discovery/SCCM | 1354797 | _(needed)_ | Story | CI Auto-Population – Support Group |  |  |  | **ID NEEDED**; possibly showback-accepted 6/8 |
| 🔴 P1 | Discovery/SCCM | 1354797 | _(needed)_ | Story | CI Auto-Population – Technical Owner |  |  |  | **ID NEEDED**; possibly showback-accepted 6/8 |
| 🔴 P1 | Discovery/SCCM | 1354797 | _(needed)_ | Story | Custom Fields (Asset Criticality, RPO, RTO, Recovery Tier, Tier Data Class, Stocks, Stocks Type) |  |  |  | **ID NEEDED**; PMDB fields accepted at showback 6/8 – may be Closed |
| 🔴 P1 | Discovery/SCCM | _(confirm)_ | _(needed)_ | Story | SCCM Ingestion Validation |  |  |  | **ID NEEDED**; from 2.1 refinement |
| P1 | Discovery/SCCM | 1355890 | 1411237 | Story | Review & Validate CMDB Dynamic IRE Behaviour Post-Australia Upgrade | Defining | 1 | Stan Tomberg | 6/12: parent confirmed 1355890; state Defining (was "Ready" on board) |
| P1 | Discovery/SCCM | 1354794 | 1455858 | Story | Virtual Location Management | Active | 2 | Kiran Dhobale | ⚠️ ADO parent = "Computer Class Data Reconciliation", not 1354794. Task 1460378 Closed |
| 🔴 P1 | Discovery/SCCM | 1354794 | 1452028 | Story | iteam import (laptop / vendor purchase feed) |  |  | Uloma | Not in either pull; scope unclear vs Cherwell |
| P1 | Discovery/SCCM | 1355890 | 1403733 | Spike | Identify deprecated plugins/features impacting CMDB | Ready DoR | 2 | Stan | gates on sandbox restore |
| P1 | Discovery/SCCM | 1383523 | 1402559 | Spike | Compare CI Class Sources | New | 3 |  | Parent: Network Device Coverage Reconciliation |
| P1 | Discovery/SCCM | 1355890 | 1403725 | Spike | Impact Assessment of Discovery & Integration Touchpoints (mid-stream) | Ready | 1 | Stan |  |
| P1 | Discovery/SCCM | 1355888 | 1339116 | Spike | Define Process to Monitor / Update CI Owners Who Have Left PPL | Ready DoR | 0 | Anuradha Rai | Parent feature 1355888 (Operational Monitoring) |
| P1 | Discovery/SCCM | 1354794 | 1413033 | Spike | Import User Location Values in sys_user | Done/Closed? | 2 | Vinay | ⚠️ UNCONFIRMED — board said Done; absent from 6/12 pull; no ADO parent |
| P1 | Discovery/SCCM | 1354794 | 1407572 | Story | Auto Populate CI Owner/Support/Tech Owner Group (Virtual Computers) | Validation | 2 | Bhushan Salsekar | 6/12: Validation (6/11 board wrongly showed Done) |
| P1 | Discovery/SCCM | 1411480 | 1387236 | Story | Discovery: Install AIM API on PROD MID Servers | Validation | 1 | Tony De Araujo | 6/12: parent confirmed 1411480; gives that feature its first child |
| P1 | Discovery/SCCM | 1354797 | 1444864 | Story | Fix credentials for Servers, Databases and Network | Validation | 5 | Tony De Araujo | ⚠️ ADO parent = Network Device Coverage Reconciliation – Group 1 (1356646) |
| P1 | Discovery/SCCM | 1354797 | 1454371 | Story | Extract Servers Without Support Groups and Validate Routing | Active | 2 | Bhushan Salsekar | NEW to worksheet; parent Server Class Data & Form Updates |
| 🟡 P1 | Discovery/SCCM | _(none)_ | 1472365 | Story | Update server values post validation of data | Ready DoR |  |  | ⚠️ NEW ORPHAN — no assignee, no parent feature; triage needed |
| 🟡 P1 | Discovery/SCCM | 1411480 | 1411480 | Feature | CMDB PI2.26 Enhancements |  |  |  | FEATURE – now has child 1387236 |
| 🟡 P1 | Discovery/SCCM | 1355888 | 1355888 | Feature | Update Operational Monitoring Activities P2 |  |  |  | FEATURE – ✅ ID confirmed (was wrongly 1354797 in traceability doc) |
| P2 | Data Certification | 1247179 | 1435307 | Story | Data Certification Pilot Changes | Validation | 3 | Bhushan Salsekar | ✅ Re-filed from P1 (was "correctness metric"); parent = Data Certification Pilot - Functionality |
| P2 | Data Certification | 1402979 | 1402727 | Story | Update Data Certification Dashboard | Active (UAT) |  | Kiran | UAT signed off 6/10; PROD 6/23. Not in 6/12 pull |
| 🔴 P2 | Data Certification | _(confirm)_ | 1402976 | Story | Execute Data Certification Policies |  |  |  | No iteration assigned; confirm feature + iteration |
| 🟡 P2 | Data Certification | 1247179 | 1247179 | Feature | Data Certification Pilot – Functionality |  |  |  | FEATURE – now has child 1435307 |
| 🟡 P2 | Data Certification | 1371672 | 1371672 | Feature | Governance Model for Requesting New Business Apps |  |  |  | FEATURE – no stories listed; confirm |
| 🟡 P2 | Data Certification | 1382404 | 1382404 | Feature | Data Certification Rollout |  |  |  | FEATURE – no stories listed; confirm |
| 🟡 P2 | Data Certification | 1402958 | 1402958 | Feature | Data Certification Pilot – Implementation Planning |  |  |  | FEATURE – no stories listed; confirm |
| P3 | Service Mapping | 1355866 | 1380747 | Story | MV90 User Access |  |  | Tanzeel | Not in either pull; assumed Active |
| P3 | Service Mapping | 1355866 | 1380757 | Story | RIE Electric Wholesale Settlement |  |  |  | Not in either pull; assumed Active |
| P3 | Service Mapping | 1355866 | 1400703 | Story | Vault Inspection System |  |  |  | Not in either pull; assumed Active |
| P3 | Service Mapping | 1355866 | 1281161 | Story | WATT |  |  |  | Not in either pull; assumed Active |
| P3 | Service Mapping | 1355868 | 1420634 | Spike | Review Apps Being Migrated & Impact to Service Mapping |  |  |  | Not in either pull; assumed Active |
| P3 | Service Mapping | 1355868 | 1326754 | Spike | Evaluate Automated Service Mapping via Endpoint-Based Discovery |  |  |  | Not in either pull; assumed Active |
| P3 | Service Mapping | 1355868 | 1355167 | Spike | Define Solution for Migrating Business App to Service Instance | Validation | 3 | Tony De Araujo | From board |
| 🟡 P3 | Service Mapping | _(confirm)_ | 1281209 | Story | OEM Service Map |  |  |  | Marked REMOVED but still on board – confirm/close |
| 🟡 P3 | Service Mapping | 1355871 | 1355871 | Feature | Service Mapping PI2 Wave 20 & 21 |  |  |  | FEATURE – no stories listed; confirm |
| P3 | Service Mapping | 1355868 | 1383493 | Dependency | Date Mapping from App PoC – EndPoint (Credentials Support) | New |  | John Benedict Ortega | Discovery/credentials dependency |
| 🔴 P4 | Regulatory/Qualys | _(see note)_ | 1428703 | Story | Install x_qual5_itam_nwapp plugin (Part 1) | Active – BLOCKED | 1 | Stan | 🔴 Blocked: Qualys replaced plugin version; uninstalled, requested new; pending vendor approval. ADO parent = Integration Qualys & ServiceNow (CMDB Data Read Only) |
| 🔴 P4 | Regulatory/Qualys | _(see note)_ | 1428704 | Story | Configure Qualys integration for CMDB to Qualys (Part 2) | Active – BLOCKED | 1 | Stan | 🔴 Blocked: same vendor-approval reason |
| P4 | Regulatory/Qualys | 1250905 | 1234585 | Spike | Define and Configure Data Scope and Import Views in Qualys | Ready DoR | 1 | Stan | Board state |
| 🔴 P4 | Regulatory/Qualys | _(Qualys feat)_ | 1465952 | Issue | Qualys Plugin Replacement Awaiting Vendor Approval | Active | 1 | Rich Santillo | ✅ Confirmed gating 1428703/1428704 |
| 🔴 P4 | Regulatory/Qualys | 1370224 | 1402602 | Spike | NERC SIP CI requirements / CMP |  |  |  | Confirm title; NERC-CIP + CMP doc |
| P4 | Regulatory/Qualys (Stream A) | _(governance)_ | 1420244 | Spike | ESS-02 Policy and CMDB Alignment | Active | 0 | Joe Dames | ADO parent "CMDB Governance & Monthly…" |
| P4 | Regulatory/Qualys (Stream B) | 1370224 | 1383515 | Dependency | Cyber Security Team Coordination – NERC CIP | New |  | Sonika Das | Formalizes engage Sonika/Cyber open item |
| 🟡 P4 | Regulatory/Qualys | 1370224 | _(needed?)_ | Story | CCB ceremony formalization (Stream A) |  |  |  | No story yet; confirm if needed (CCB 6/16, Audit 6/18) |
| 🟡 P4 | Regulatory/Qualys | 1370224 | _(needed?)_ | Story | NERC-CIP CI Security Requirements (Stream B) |  |  |  | No story yet; engage Jason Dubriel |
| P5 | NowAssist | 1436574 | 1436576 | Story | Confirm Platform Prerequisites for NowAssist Activation (Part 1) | Active | 1 | Kiran Dhobale | ✅ 6/12 confirmed Active |
| P5 | NowAssist | 1436574 | 1436579 | Story | Activate NowAssist for CMDB Plugin | Ready DoR | 1 | Kiran Dhobale | Reassigned from Karen |
| P5 | NowAssist | 1436574 | 1436593 | Story | Activate Contextual CI Form Help Skill | Ready DoR | 1 | Kiran Dhobale | Reassigned from Karen |
| P5 | NowAssist | 1436574 | 1436592 | Story | Activate CI Summarization Skill | Ready DoR | 1 | Kiran Dhobale | Reassigned from Karen |
| P5 | NowAssist | 1436574 | 1436581 | Spike | NowAssist: Establish CMDB Health Baseline Score (Last Part) | Ready DoR | 2 |  | New; parent 1436574 |
| P5 | NowAssist | _(none)_ | 1470837 | Spike | Analyze CMDB Health Indicators Configured for 35 Principal Classes | Ready DoR | 0 |  | Feeds health baseline; no ADO parent set |
| P5 | NowAssist | _(PI-3)_ | 1451930 | Feature | Now Assist Duplicate CI Elimination (Phase 2) | New |  |  | PI-3; ⚠️ "Phase 2" (ADO) vs plan's Phase 1 — reconcile |
| 🟡 Other | Needs classification | _(confirm)_ | 1455827 | Story | SOX – CI ownership change notification |  |  |  | Committed PI2 or PI3? Undecided (email); confirm |

## Summary of what's needed

| Validation gap | Count | Items |
|----------------|-------|-------|
| 🔴 **Blocked** (confirmed 6/12) | 2 | 1428703, 1428704 (Qualys vendor approval — Issue 1465952) |
| 🔴 Stories with **no ADO ID** | 5 | CI auto-pop (3), Custom Fields, SCCM Ingestion Validation |
| ⚠️ **No confirmed Done** | — | 1407572 = Validation; 1413033 unconfirmed (absent 6/12) |
| 🟡 **Orphan needing triage** | 1 | 1472365 (no owner, no parent) |
| 🟡 **Parent mismatches to reconcile** | 3 | 1455858 (Computer Class Data Reconciliation), Qualys (Integration Qualys & ServiceNow), 1421790 (1354797 vs 1383523) |
| 🟡 **Features with no child stories** | 5 | 1371672, 1382404, 1402958, 1355871, (1247179 & 1411480 now have children) |
| 🟡 **Hygiene / decision** | 4 | 1281209 (removed?), 1455827 (PI2/PI3?), 1402602 (title?), 1451930 (phase naming) |
| ⚪ **Story Points still missing** | ~18 | Mostly Service Mapping + airlift + no-ID rows |
