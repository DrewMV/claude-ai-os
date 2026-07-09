---
type: team-artifact
workspace: Work
project: CMDB-CSDM
pi: PI-2
updated: 2026-07-08
tags: [work, cmdb-csdm, governance]
---

# CMDB Data Dictionary (CMP Stage 1) — CCB Decision Sheet

**Companion to** [[configuration-management-plan-stage1]] · part of the [[configuration-management-plan]] umbrella. **For:** CMDB CCB vote, **7/21/2026**.

**Purpose.** Every cell marked `[CCB confirm]` in the Data Dictionary is a PPL governance decision left intentionally open. This sheet lists all **38** of them, grouped by class, so the board can rule on them efficiently rather than hunting through the document.

> **How to read this.** The **Team suggestion** column is the delivery team's proposed default to speed the vote — it is *not* a decision. The **CCB ruling** column is authoritative; the chair captures the outcome there on 7/21. Generated from the **2026-06-29** draft — regenerate if the document changes before distribution.

**Decision types:**
- **Mandatory?** — confirm whether the attribute is required (Y/N)
- **Audited?** — confirm inclusion in audit / certification scope (Y/N)
- **Owner?** — assign a Certification Owner / Class Manager (none mapped)
- **Values?** — confirm the allowed-value (choice) list

## At a glance

| Class | Class Manager | # Decisions |
|-------|---------------|-------------|
| Business Application | Todd Dierksheide | 4 |
| Service Instance | ⚠️ **none assigned** | 5 |
| Computer | Monica Green (Phys) / Paul Becker (Virt) | 3 |
| Server (parent) | Ray Reuter | 5 |
| Windows Server (child) | Ray Reuter | 5 |
| Linux Server (child) | Ray Reuter | 4 |
| Database (parent) | Ray Reuter | 3 |
| Oracle DB (child) | Ray Reuter | 4 |
| SQL Server DB (child) | Ray Reuter | 5 |
| **Total** | | **38** |

By type: **Mandatory? 14 · Audited? 20 · Owner? 2 · Values? 2.**

> ⚠️ **Two things to resolve before the vote:**
> 1. **Service Instance has no Class Manager** (items 5–6). The board must **assign a Certification Owner** (EA/Platform — e.g., Gaurav Parmar or Sonika Das) or defer the class. Its items can't be ratified without an owner.
> 2. **Ray Reuter owns 26 of 38 decisions** (all Server + Database classes). Pre-brief him so Server/Database aren't stranded if attention runs short.

---

## 1. Business Application — Todd Dierksheide (`cmdb_ci_business_app`)

| # | Attribute | Decision | Context | Team suggestion | CCB ruling |
|---|-----------|----------|---------|-----------------|-----------|
| 1 | Application Category | Mandatory? | Choice; auth = EA/LeanIX | Mandatory = **Y** (core classification) | |
| 2 | Life Cycle Stage | Mandatory? | Choice (CSDM stages); auth = EA | Mandatory = **Y** (lifecycle reporting) | |
| 3 | IT Application Owner | Mandatory? | sys_user; via Data Certification | Mandatory = **Y** (ownership/audit) | |
| 4 | Business Owner | Mandatory? | sys_user; via Data Certification | Mandatory = **Y** (Dec audit remediation) | |

## 2. Service Instance — ⚠️ NO Class Manager assigned

| # | Attribute | Decision | Context | Team suggestion | CCB ruling |
|---|-----------|----------|---------|-----------------|-----------|
| 5 | Name | Owner? | "no dedicated CCB Class Mgr mapped" | **Assign class owner** (EA/Platform) | |
| 6 | Environment | Owner? | Prod/QA/Dev/Test | Same owner as #5 | |
| 7 | Service Owner (`owned_by`) | Mandatory? | sys_user | Mandatory = **Y** | |
| 8 | ITSM Support Group | Mandatory? | sys_user_group | Mandatory = **Y** (governance) | |
| 9 | Change Approval Group | Mandatory? | sys_user_group | Mandatory = **Y** (governance) | |

## 3. Computer — Monica Green (Physical) / Paul Becker (Virtual) (`cmdb_ci_computer`)

| # | Attribute | Decision | Context | Team suggestion | CCB ruling |
|---|-----------|----------|---------|-----------------|-----------|
| 10 | Assigned To | Mandatory? | sys_user; Asset Mgmt | — (PPL call) | |
| 11 | Operating System | Audited? | SCCM/Intune authoritative | Align to Dec audit scope | |
| 12 | MAC Address | Audited? | Endpoint connector / Discovery | Align to Dec audit scope | |

## 4. Server (parent) — Ray Reuter (`cmdb_ci_server`)

| # | Attribute | Decision | Context | Team suggestion | CCB ruling |
|---|-----------|----------|---------|-----------------|-----------|
| 13 | Operational Status | Values? | Build / Operational / Non-Operational / Retired | Confirm full list vs OOB choices | |
| 14 | IP Address | Audited? | Discovery authoritative | Align to Dec audit scope | |
| 15 | MAC Address | Audited? | Discovery authoritative | Align to Dec audit scope | |
| 16 | CPU Count | Audited? | vCenter override (else Discovery) | Align to Dec audit scope | |
| 17 | RAM (MB) | Audited? | vCenter override (else Discovery) | Align to Dec audit scope | |

## 5. Windows Server (child of Server) — Ray Reuter

| # | Attribute | Decision | Context | Team suggestion | CCB ruling |
|---|-----------|----------|---------|-----------------|-----------|
| 18 | OS Version | Audited? | SCCM overrides Discovery | Align to Dec audit scope | |
| 19 | OS Domain | Audited? | SCCM overrides Discovery | Align to Dec audit scope | |
| 20 | OS Service Pack | Audited? | SCCM overrides Discovery | Align to Dec audit scope | |
| 21 | ITSM Support Group | Mandatory? | "Wintel Infrastructure Ops"; not auto-writable | Mandatory = **Y** (governance) | |
| 22 | Change Approval Group | Mandatory? | "Wintel CAB"; not auto-writable | Mandatory = **Y** (governance) | |

## 6. Linux Server (child of Server) — Ray Reuter

| # | Attribute | Decision | Context | Team suggestion | CCB ruling |
|---|-----------|----------|---------|-----------------|-----------|
| 23 | OS Architecture | Audited? | Discovery via SSH authoritative | Align to Dec audit scope | |
| 24 | Kernel Release | Audited? | Discovery via SSH authoritative | Align to Dec audit scope | |
| 25 | ITSM Support Group | Mandatory? | "Unix/Linux Administration Team" | Mandatory = **Y** (governance) | |
| 26 | Change Approval Group | Mandatory? | "Linux CAB" | Mandatory = **Y** (governance) | |

## 7. Database (parent) — Ray Reuter (Database CIs)

| # | Attribute | Decision | Context | Team suggestion | CCB ruling |
|---|-----------|----------|---------|-----------------|-----------|
| 27 | Version | Audited? | Discovery authoritative | Align to Dec audit scope | |
| 28 | TCP Port | Audited? | Discovery authoritative | Align to Dec audit scope | |
| 29 | Operational Status | Values? | Operational, Retired, … | Confirm full list | |

## 8. Oracle Database (child) — Ray Reuter

| # | Attribute | Decision | Context | Team suggestion | CCB ruling |
|---|-----------|----------|---------|-----------------|-----------|
| 30 | SID | Audited? | Oracle probes | Align to Dec audit scope | |
| 31 | Oracle Edition | Audited? | Oracle probes | Align to Dec audit scope | |
| 32 | Oracle Version | Audited? | Oracle probes | Align to Dec audit scope | |
| 33 | Support Group | Mandatory? | "Oracle DBA Team" | Mandatory = **Y** (governance) | |

## 9. SQL Server Database (child) — Ray Reuter

| # | Attribute | Decision | Context | Team suggestion | CCB ruling |
|---|-----------|----------|---------|-----------------|-----------|
| 34 | Instance Name | Audited? | Discovery / SCCM | Align to Dec audit scope | |
| 35 | Clustered | Audited? | Discovery authoritative | Align to Dec audit scope | |
| 36 | SQL Edition | Audited? | SCCM authoritative (edition/license) | Align to Dec audit scope | |
| 37 | TCP Port | Audited? | Discovery overrides SCCM | Align to Dec audit scope | |
| 38 | Support Group | Mandatory? | "SQL DBA Team" | Mandatory = **Y** (governance) | |

---

**Vote capture.** Record each ruling as **Accept** (as suggested), **Amend** (note the change), or **Defer** (note owner + date). A class is accepted once all its items are ruled. Roll per-class results into the overall Data Dictionary acceptance in the CCB minutes.
