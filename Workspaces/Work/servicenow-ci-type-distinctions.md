---
type: concept
workspace: Work
tags: [work, servicenow, cmdb-csdm, cmdb, reference]
updated: 2026-06-01
sources:
  - title: "CMDB-CSDM Backlog Refinement discussion"
    ingested: 2026-06-01
---

# ServiceNow CI Type Distinctions

Key technical clarification made during CMDB-CSDM backlog refinement (May–Jun 2026). Relevant to service mapping, migration stories, and CMDB data modeling decisions.

## Business Application

A logical representation of a business capability or application from a business perspective.

- Owned by business stakeholders
- Represents *what* the business uses, not *how* it runs
- Used for business impact analysis, ownership tracking
- Example: "Accounts Payable System"

## Application Service (Service Instance)

A running instance of an application in a specific environment — the technical realization of a Business Application.

- Also called **Service Instance** in ServiceNow terminology
- Tied to specific infrastructure (servers, databases, middleware)
- Used for service mapping, dependency mapping, impact analysis
- Multiple Application Services can relate to one Business Application (e.g., DEV, TEST, PROD instances)
- Example: "Accounts Payable — Production"

## Application CI (Configuration Item)

The software component or executable installed on infrastructure.

- Represents the *software artifact* itself, not the service
- Discovered by CMDB Discovery (MID Server)
- Linked to servers/hosts where the software runs
- Lower level than Application Service
- Example: "Oracle E-Business Suite 12.2.x on server APP01"

## Why This Matters

| Decision | Implication |
|---------|------------|
| Service Mapping | Maps Application Services, not Application CIs — must use correct CI type |
| Migration planning | VMware-to-Azure migration tracks Application Services and their dependencies |
| Ownership assignment | CI Owner and Support Group go on Business Application level |
| NERC CIP compliance | Compliance attributes linked at Application Service level |
| Impact analysis | Business impact traced through Business Application → Application Service → Application CI hierarchy |

## Common Mistakes to Avoid

- Creating a Business Application when a Service Instance is needed (or vice versa)
- Assigning infrastructure-level attributes to Business Application records
- Building service maps off Application CIs instead of Application Services

See also: [[SAFe-devops-and-technical-practices]], [[requirements-process]]
