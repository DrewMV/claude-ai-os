---
title: CSDM OT Domain
category: concepts
workspace: Work
project: nerc-cip
tags: [csdm, servicenow, cmdb, ot-security, operational-technology, nerc-cip]
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  CSDM 5.0 adds OT CI classes, OT System Services, and dependency mapping, enabling
  utilities to model BES Cyber Systems natively in ServiceNow's CMDB.
provenance:
  extracted: 0.80
  inferred: 0.18
  ambiguous: 0.02
base_confidence: 0.83
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# CSDM OT Domain

## Overview

The Common Service Data Model (CSDM) is ServiceNow's standardized framework for organizing CMDB data into services, applications, infrastructure, and now operational technology. CSDM provides naming conventions, table relationships, and ownership structures that ensure consistent data across all ServiceNow products.

**CSDM 5.0** is the version that explicitly extends the model to OT environments, adding new CI classes for industrial equipment and enabling service mapping between physical assets and BES functions.

## The Seven CSDM Domains

| Domain | Purpose | NERC CIP Relevance |
|---|---|---|
| **Foundation** | Organizational data, product models, contracts, lifecycle statuses | CI lifecycle aligns with BES Cyber Asset lifecycle management |
| **Ideation & Strategy** | Strategic planning | — |
| **Design & Planning** | Logical architecture, business capabilities, Information Objects | BCSI data governance via Information Objects |
| **Build & Integration** | DevOps, digital assets | Patch and firmware build artifacts |
| **Service Delivery** | Operational service instances, infrastructure CIs | **Primary domain for BES Cyber Systems** |
| **Service Consumption** | Business service catalog, service offerings | — |
| **Manage Portfolio** | Service oversight, strategic portfolio | — |

## OT-Specific CI Classes (CSDM 5.0)

ServiceNow OT Manager uses CSDM tables with dedicated classes for industrial environments:

- **OT Configuration Item Extension Classes** — Extend standard CMDB CI classes to capture OT-specific attributes (firmware version, communication protocol, physical location zone)
- **CMDB CI Classes for Operational Technology Manager** — Purpose-built for industrial equipment types: PLCs, RTUs, HMIs, historians, protective relays
- **OT System Services** — Represent the operational function a set of OT CIs performs (e.g., SCADA Control, Energy Management System, Protection Relay System)

### Why This Matters for NERC CIP

The **OT System Service** entity is the structural analog to a **BES Cyber System**. By mapping physical OT CIs to an OT System Service, an organization can:
1. Assess which BES functions depend on which physical assets (CIP-002 impact analysis)
2. Apply change management workflows at the service level (CIP-010)
3. Define access controls and ownership at the service level (CIP-007)

## Dependency Mapping

CSDM enables viewing "the dependency map for an Operational Technology system service" — a visual and queryable graph of all CIs that support a given OT function. For NERC CIP, this dependency map is the evidence base for:
- Determining the 15-minute impact threshold (CIP-002)
- Scoping the control impact analysis required when a change is made (CIP-010 R1.4)
- Identifying all assets in an Electronic Security Perimeter (CIP-005)

## Data Quality and Governance

CSDM 5.0 introduces:
- **Teams** — Flexible tracking of user groups assigned to each CI, supporting ownership accountability (who is responsible for a given BES Cyber System's configuration record)
- **CMDB OT Data Certification Policies** — Scheduled reviews of OT CI data quality, supporting the 15-month CIP-002 review requirement
- **Software Bill of Materials (SBOM)** — Inventory of software components within a CI, directly supporting CIP-010 R1.1 baseline requirements (software name/version)

## Limitations

- There are no native "BES Cyber Asset" or "BES Cyber System" CI classes in ServiceNow out of the box. Utilities must implement these as:
  - Custom CI classes extending OT CI classes, OR
  - CMDB CI Groups configured to represent BES Cyber System boundaries
- OT asset data typically flows into ServiceNow from OT discovery tools (Dragos, Forescout, Tenable) via integrations — the CSDM structure defines *where* that data lands, not how it gets there

## Related Concepts

- [[CMDB as NERC CIP Asset Registry]] — How CMDB CIs satisfy CIP-002 inventory requirements
- [[CIP-002 BES Cyber System Categorization]] — The standard that CSDM's OT System Services are designed to support
- [[CIP-010 Configuration Change Management]] — CSDM dependency maps support R1.4 control impact analysis
- [[ServiceNow OT Manager]] — The ServiceNow product that implements OT CI classes and OT System Services
