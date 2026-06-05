---
title: CIP-011 Information Protection
category: concepts
workspace: Work
project: nerc-cip
tags: [nerc-cip, cip-011, bcsi, information-security, data-classification, cmdb]
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
summary: >-
  CIP-011 requires an information protection program for BES Cyber System Information (BCSI),
  which can include CMDB configuration records containing network topology or access paths.
provenance:
  extracted: 0.80
  inferred: 0.15
  ambiguous: 0.05
base_confidence: 0.82
lifecycle: draft
lifecycle_changed: 2026-06-03
---

# CIP-011: Information Protection

## Purpose

CIP-011 requires responsible entities to implement a documented information protection program for BES Cyber System Information (BCSI). The standard recognizes that configuration data about BES Cyber Systems is itself a security risk if disclosed to unauthorized parties.

## What Is BCSI

**BES Cyber System Information (BCSI)** is information about a BES Cyber System that could be used to gain unauthorized access or pose a security threat.

BCSI includes (examples):
- Network diagrams showing Electronic Security Perimeter topology
- Port and protocol configurations that reveal attack surface
- Access path documentation combining IP addresses with system context
- Configuration baselines showing software versions (enabling targeted exploits)
- Authentication/access control configurations

BCSI does **not** include standalone items that by themselves pose no threat:
- Device names in isolation
- Individual IP addresses without system context
- Generic policy statements
- ESP names without topology

## CMDB Data as BCSI

This is the critical connection to ServiceNow governance: CMDB records for BES Cyber Systems often *do* constitute BCSI when they contain:
- Logical network port configurations (protocol, purpose, source/destination)
- Software and firmware version details linked to network-accessible systems
- Access path relationships between EACMS and BES Cyber Systems
- Combined records showing asset location, function, and connectivity

**Implication**: The CMDB itself must be treated as a BCSI store and protected accordingly.

## Information Protection Program Requirements (R1)

Responsible entities must implement a documented program that includes:

1. **Method(s) to identify BCSI** — How the organization determines what data qualifies as BCSI (this should explicitly address CMDB records)
2. **Handling procedures** — How BCSI is stored, transmitted, and accessed
3. **Access controls** — Limiting BCSI access to those with a demonstrated need
4. **Storage and transmission protection** — Encryption or equivalent for electronic BCSI
5. **Disposal procedures** — How BCSI is sanitized when no longer needed; asset reuse/disposal records must be maintained

## Data Classification and CMDB

CIP-011 does not require a formal data classification scheme — but it allows one. A CMDB implementation aligned with CIP-011 should:
- Add a BCSI classification attribute to CI records
- Restrict access to BCSI-classified CI records via role-based access control
- Log all views and exports of BCSI-classified records
- Define the disposal procedure for CI records when assets are retired

## Relationship to Other Standards

- [[CIP-002 BES Cyber System Categorization]] — Categorization records and the inventory itself may be BCSI
- [[CIP-010 Configuration Change Management]] — Baseline configuration records (OS, ports, patches) are likely BCSI
- [[CMDB as NERC CIP Asset Registry]] — The CMDB is the primary BCSI store in a ServiceNow-governed environment
- [[CSDM OT Domain]] — Design & Planning domain's Information Objects entity supports data governance for BCSI
