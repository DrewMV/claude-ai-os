---
workspace: Work
project: PPL CMDB-CSDM
type: reference
tags: [work, cmdb-csdm, servicenow]
updated: 2026-07-10
---

# CSDM 5 — Application Service → Service Instance

## Finding

In **CSDM 5** (aligned with the ServiceNow **Yokohama** release), **"Application Service" was renamed to "Service Instance."** Service Instance is the broader parent concept; **Application Service is now one *type* of Service Instance**, and ServiceNow added new "Service Instance siblings" alongside the pre-existing Application Service table.

The two are not different things — Service Instance is the renamed/generalized parent of what we historically called Application Service.

## Why it matters for CMDB-CSDM

- Use the terminology **"Service Instance / Application Service"** in stories and artifacts until PPL's exact class/table is confirmed (see [[service-instance-modify-storyA-core]], [[service-instance-modify-storyB-sox]]).
- **Verify against PPL's deployed instance / CSDM version with Stan Tomberg** before building — the label and available siblings depend on the deployed version.
- Relevant to the Business Application → Application Service migration already in flight (BA enhancements paused until that migration completes).

## Supporting sources (official ServiceNow)

- **CSDM 5 white paper** (ServiceNow Community): *"We have added several new Service Instance siblings to the preexisting Application Service table. An Application Service remains a logical or designated…"* — [PDF](https://www.servicenow.com/community/s/cgfwn76974/attachments/cgfwn76974/common-service-data-model-kb/744/3/CSDM%205%20w%20links.pdf)
- **"Application Service and Service Instance: What is new in Yokohama"** (ServiceNow Community): explains how *"Application Service is being renamed to Service Instance to better accommodate a wider range of services."* — [link](https://www.servicenow.com/community/common-service-data-model/application-service-and-service-instance-what-is-new-in-yokohama/ta-p/3193268)
- **"CSDM 5 — Get the White Paper HERE"** (ServiceNow Community) — [link](https://www.servicenow.com/community/common-service-data-model/csdm-5-finally-get-the-csdm-5-white-paper-here/ta-p/3254967)

## Caveat

Captured from official ServiceNow Community sources (search results + white-paper references), not a full read of the white paper. Confirm specifics — exact table names and the full list of Service Instance siblings — against the CSDM 5 white paper and PPL's deployed version.
