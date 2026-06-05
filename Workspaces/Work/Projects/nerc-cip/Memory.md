---
level: project
workspace: Work
project: nerc-cip
status: active
created: 2026-06-03
updated: 2026-06-03
tags: [work, nerc-cip, compliance, servicenow, cmdb]
---

## Goal

Research how ServiceNow CSDM/CMDB governance — specifically the Configuration Management Plan (CMP) and Configuration Control Board (CCB) Charter — supports NERC CIP compliance for electric utilities.

## Current State

Round 1–3 research complete (2026-06-03). 13 wiki pages created across synthesis, concepts, sources, and entities.

## Key Decisions

- Treating CCB and CAB as equivalent for NERC CIP purposes (literature uses both terms for the same governance function)
- Filing all pages under `Workspaces/Work/Projects/nerc-cip/` with subdirectories for synthesis/, concepts/, sources/, entities/

## Active Context

- Synthesis page is the primary deliverable: `synthesis/Research- ServiceNow CMDB-CSDM Governance and NERC CIP.md`
- Core CIP standards covered: CIP-002, CIP-007, CIP-010, CIP-011
- Key finding: CMP maps to CIP-010 R1–R4; CCB Charter provides the authorization body required by R1.2
- CSDM 5.0 OT domain enables BES Cyber System modeling natively in ServiceNow
- No native "BES Cyber Asset" or "BES Cyber System" CI class in ServiceNow — requires custom extension
- CMDB data containing network topology/port configs is likely BCSI (CIP-011)

## Open Questions

- Which specific NERC CIP requirements apply to PPL's particular BES Cyber System portfolio?
- Does PPL use ServiceNow OT Manager, or just standard CMDB for OT assets?
- Are CMP and CCB Charter documents currently in place at PPL, or are these to be created?
- What OT discovery tools (Dragos, Forescout, Tenable) feed into the ServiceNow CMDB?

## Templates

- [Configuration Management Plan](templates/configuration-management-plan.md) — Full template, 13 sections, NERC callouts, traceability matrix in Appendix A
- [CCB Charter](templates/ccb-charter.md) — Full template, 11 sections, NERC callouts, decision log in Appendix B

## Sources

- [NERCipedia CIP-010-4](sources/nercipedia-cip-010-4.md)
- [Shieldworkz NERC CIP Evidence Pack](sources/shieldworkz-nerc-cip-evidence-pack.md)
- [ServiceNow Community NERC CIP](sources/servicenow-community-nerc-cip.md)
- [CSDM 5.0 Explained](sources/csdm-5-explained.md)
