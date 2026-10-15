---
type: team-artifact
workspace: Work
project: PPL CMDB-CSDM
pi: PI-3
feature: "1517032 — Certify Servers — CMDB Data Certification"
objective: CO6 Obj 3 — Expand CI Data Certification Across All Major Classes
status: draft
updated: 2026-09-10
tags: [work, cmdb-csdm, safe, pi-planning, co6, data-certification]
relationships:
  - target: "[[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]]"
    type: related_to
  - target: "[[PI-3/pi3-physical-computer-data-validation-stories]]"
    type: related_to
---

# Windows Server Data Gap Analysis

**Reference data pulled to inform Feature 1517032 (Certify Servers) — `cmdb_ci_win_server` slice**
Captured 2026-09-10 · Source: ad hoc ServiceNow query, not yet reconciled to the audit dashboard

---

## Population queried

`cmdb_ci_win_server`, filtered:

```
operational_status NOT IN (2,6)
^ install_status NOT IN (4,6,7)
^ last_discovered ON Last 30 days@javascript:gs.beginningOfLast30Days()@javascript:gs.endOfLast30Days()
```

**Total: 3,011** active, recently-discovered Windows servers.

Ownership split within this population: **Ray 2,510 · Paul 82 · Monica 419** (sums to 3,011).

> This 3,011 figure is a different cut than the 3,917 vs 15,218 dispute already open at DEP-5 on [[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]] — it's Windows-only, and adds a 30-day discovery-recency filter neither of those two figures applies. Treat as a third data point for that reconciliation, not a resolution of it.

---

## Per-attribute gap findings

| Attribute | Empty count | Notes |
|---|---|---|
| CI Owner (`managed_by`) | 0 | Fully populated. Owner split: Ray 2,510 / Paul 82 / Monica 419 |
| Technical Owner Group (`managed_by_group`) | 0 | Only 2 distinct group values in use: `AAD.SaaS.ServiceNow.ACN.IMS.Server.Windows.AG`, `AAD.SaaS.ServiceNow.Server.TechApprover` |
| Support Group (`support_group`) | 0 | Only 1 distinct group value in use: `AAD.SaaS.ServiceNow.ACN.IMS.Server.Windows.AG` |
| Asset Tag (`asset_tag`) | **176** | Corrected 2026-09-10 — an earlier read of this data showed 210; 176 is confirmed |
| Value Stream (`business_unit`) | **2,510** | **Systemic, not scattered — confirmed 2026-09-10: every Windows server owned by Ray is missing Value Stream.** Count matches Ray's entire ownership slice exactly. Looks like `business_unit` was never set on whatever process created/onboarded Ray's servers, not a per-record data-entry gap |
| Data Classification (`classification`) | 19 | Distinct values in use elsewhere in the population: Business Use, Confidential, Production, Public, Restricted |
| Location (`location`) | 17 | Spread across 7 distinct location values |
| Environment (`environment`) | 70 | Spread across 6 distinct environment values |

---

## Open items

1. **Value Stream / Ray correlation** — worth a direct question to Ray (or whoever provisions his servers) on *why* `business_unit` is unset across the whole slice, since it points at a build/onboarding gap rather than something a per-CI certification task would catch or fix one record at a time.
2. **Reconciliation with DEP-5** — this 3,011 figure should be reconciled against the 3,917 / 15,218 figures already in dispute on [[PI-3/pi3-cert-1517032-certify-servers-stories-dependencies]] once Ray/Stan close that out.
3. **Linux server equivalent** — Feature 1517032 covers Windows + Linux additively from the parent `cmdb_ci_server` class; this note is Windows-only. A matching Linux (`cmdb_ci_linux_server`) pull has not been done yet.
