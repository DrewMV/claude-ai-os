---
source_url: https://framework.scaledagile.com/continuous-integration
scraped: 2026-05-30
---

[SAFe Knowledge Base](https://framework.scaledagile.com/safe-knowledge-base/#extended-guidance) » Continuous Integration

# Continuous Integration

> The epiphany of integration points is that they control product development. They are the leverage points to improve the system. When timing of integration points slip, the project is in trouble.
>
> —Dantar Oosterwal, The Lean Machine

**Definition:** Continuous Integration (CI) is an aspect of the Continuous Delivery Pipeline in which new functionality is developed, tested, integrated, and validated in preparation for deployment and release.

CI is the second aspect in the four-part Continuous Delivery Pipeline of Continuous Exploration (CE), Continuous Integration (CI), Continuous Deployment (CD), and Release on Demand.

## Details

Continuous integration is a critical technical practice for each Agile Release Train (ART). It improves quality, reduces risk, and establishes a fast, reliable, and sustainable development pace.

With continuous integration, the system always runs, meaning it's potentially deployable, even during development. CI is most easily applied to software solutions where small, tested vertical threads can deliver value independently. In larger, multi-platform software systems, the challenge is harder. Each platform has technical constructs which need continuous integration to validate new functionality.

As a result, teams need a balanced approach that allows them to build-in quality and gets fast feedback on their integrated work. For purely software-based solutions, continuous integration is relatively easy to achieve with modern tools.

## The Four Activities of Continuous Integration

SAFe describes four activities associated with continuous integration:

1. **Develop** describes the practices necessary to implement stories and commit the code and components to version control
2. **Build** describes the techniques needed to create deployable binaries and merge development branches into the trunk
3. **Test end-to-end** describes the practices necessary to validate the solution
4. **Stage** describes the steps required to host and validate solutions in a staging environment before production
