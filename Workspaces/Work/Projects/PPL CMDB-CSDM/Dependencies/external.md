---
type: dependency-tracker
workspace: Work
project: CMDB-CSDM
dependency-team: External
updated: 2026-06-01
tags: [work, cmdb-csdm, dependencies]
---

# Dependencies — External

Dependencies outside the INFOPS ART (other ARTs, vendors, business units, platform teams).

## Active Dependencies

| # | Description | External Party | Contact | Iteration | Status |
|---|-------------|---------------|---------|-----------|--------|
| 1 | ServiceNow Australia version upgrade — cascading environment schedule affects deployment windows and code freeze dates across PI-2 and PI-3 | ServiceNow Platform Team | TBD | 2.2 – 3.1 | Active |

### Australia Version Upgrade — Full Schedule

| Environment | Change ID | Upgrade Date | Clone Date | Code Freeze | Status |
|-------------|-----------|-------------|-----------|-------------|--------|
| pplwebsandbox | CHG70100867 | June 6, 2026 | May 29, 2026 | Not applicable | Approved |
| pplwebdev | CHG70100870 | June 27, 2026 | June 19, 2026 | June 27 – July 18, 2026 | Approved |
| pplwebtest | CHG70100865 | July 18, 2026 | July 10, 2026 | July 18 – August 15, 2026 | Approved |
| pplweb (Prod) | CHG70121033 | August 15, 2026 | — | — | Approved |
| pplwebtraining | CHG70100868 | Not applicable | August 21, 2026 | — | Approved |

**Delivery impact summary:**
- Sandbox on Australia from **June 6** (Iter 2.2 — imminent)
- Dev frozen June 27 – July 18 → constrains Iter 2.4 and most of 2.5
- Test frozen July 18 – Aug 15 → constrains end of 2.5, all of IP (2.6), and PI-3 Iter 3.1
- Prod upgrades **Aug 15** — 10 days into PI-3; PI-3 Iter 3.1 begins on pre-Australia prod

## Resolved Dependencies

| # | Description | External Party | Resolved | Notes |
|---|-------------|---------------|---------|-------|
| | | | | |
