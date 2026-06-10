---
type: meeting-notes
workspace: Work
project: CMDB-CSDM
date: 2026-06-08
topic: Cherwell CMDB Import — Laptop Inventory Import & ServiceNow Integration
organizer: Uloma, Adelufosi (not present)
attendees: [Trevor (Speaker 2), Monica Green (Speaker 3), Speaker 1, Speaker 4]
updated: 2026-06-10
tags: [work, cmdb-csdm, cherwell, laptop-inventory, servicenow-import, vendor-feed]
---

# Cherwell CMDB Import — Laptop Inventory Import & ServiceNow Integration

**Date:** 2026-06-08 10:32  
**Format:** Virtual  
**Organizer (absent):** Uloma, Adelufosi  
**Attendees:** Speaker 1, Trevor (Speaker 2), Monica Green (Speaker 3), Speaker 4

> **Note on transcript:** "Sharewell" in the transcript is a transcription error for **Cherwell**. "Aloma" (referenced as the absent organizer) is **Uloma, Adelufosi**.

---

## Purpose

Establish a reliable process to import laptop purchase data from vendors directly into ServiceNow CMDB, replacing the legacy Cherwell system. The goal is to automate workstation tracking (model number, serial number, etc.) as soon as laptops are shipped.

---

## Key Discussion Points

### Background & History
- Previous/current vendors providing purchase data: Pomeroy, Windsight, SHI, SBI, Insight, CDW, Broadway
- The import serves as a checks-and-balances mechanism — verifying received equipment against purchase orders
- Cherwell is obsolete; ServiceNow CMDB is the current system of record for inventory and lifecycle management

### Import Mechanism
- Import is triggered by **emails with specific subject line formats** that cause ServiceNow to automatically ingest the attached vendor data
- **Daily import frequency** is preferred over weekly to ensure equipment data is immediately available for provisioning and deployment

### Vendor Template
- A standardized import template exists but is not immediately on hand — it lives in historical email threads
- All vendors (Insight, Pomeroy, CDW, Broadway, etc.) should use the same template for consistency
- Trevor needs to review the template to confirm ServiceNow import compatibility

---

## Action Items

| Owner | Action | Due |
|---|---|---|
| Speaker 4 | Locate and share the standardized import template (used for Insight and other vendors) with Trevor | ASAP |
| Speaker 4 | Forward relevant email threads with vendor feed discussions and attachments to Trevor | ASAP |
| Trevor (Speaker 2) | Review the standardized template for ServiceNow import compatibility | Within 48 hrs of receipt |
| Trevor (Speaker 2) | Follow up with Uloma (Adelufosi) to clarify project status and next steps | Within 48 hrs |
| Trevor (Speaker 2) | Provide update to team after review and coordination with Uloma | Within 48 hrs |

---

## Open Questions

- What is Uloma's current project status — is there an existing ADO story or backlog item for this work?
- **Validate with Trevor:** Is this work related to US 1452028 (Import records from iteam to CMDB), or is it a separate stream? This meeting focused on *new purchases* flowing in from vendors — iteam may be a different data source entirely. Confirm scope boundary before assuming coverage.
- Which ServiceNow import table/transform map is being used for laptop CIs?
- Are all vendors currently sending data in a compatible format, or does template adoption need to be enforced?
