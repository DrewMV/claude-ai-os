---
type: project-note
workspace: Work
project: ServiceNow
tags: [work, operations, tool]
updated: 2026-05-30
summary: "Work involving ServiceNow data analysis — ticket resolution metrics, operational dashboards, and CMDB governance. All using PowerShell and Python."
base_confidence: 0.85
lifecycle: draft
lifecycle_changed: 2026-05-30
provenance: "Distilled from 3 Claude conversations (May 2026). Extracted from actual session work with PowerShell scripts and Excel exports."
---

# ServiceNow Analytics

Overview of work done analyzing ServiceNow data and building operational reports.

## Ticket Resolution Analysis

Pulled a CSV export from ServiceNow and computed resolution-time statistics using PowerShell:

- **Tools:** `Import-Csv`, date arithmetic, `Measure-Object`
- **Metrics computed:** average days to close, median days to close, cohort breakdown by month (January 2026 highlighted)
- **Pattern:** Identify tickets still open past a configurable threshold as a backlog health signal
- Key insight ^[inferred]: cohort-based analysis (group tickets by open month) reveals whether resolution performance is trending better or worse over time

## Operational Dashboard

Built a dashboard from a ServiceNow YTD activity Excel export. Populated a PowerPoint presentation with current metrics.

- **Fiscal week framing:** FW2 = week starting January 4, 2026 (Sundays); fiscal weeks anchor metric comparisons
- **Stack:** `openpyxl` or `pandas` to read XLSX → `python-pptx` to write slides
- See [[python-document-automation]] for the PowerPoint generation patterns

## Related Pages

- [[cmdb-governance-roadmap]] — the governance initiative built on top of this analytics work
- [[python-document-automation]] — the Python toolchain used for reports
