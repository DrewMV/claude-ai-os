---
source_url: https://framework.scaledagile.com/continuous-deployment
scraped: 2026-05-30
---

[SAFe Knowledge Base](https://framework.scaledagile.com/safe-knowledge-base/#extended-guidance) » Continuous Deployment

# Continuous Deployment

> In order for you to keep up with customer demand, you need to create a deployment pipeline. You need to get everything in version control. You need to automate the entire environment creation process. You need a deployment pipeline where you can create test and production environments, and then deploy code into them, entirely on demand.
>
> —Erik to Grasshopper, The Phoenix Project

**Definition:** Continuous Deployment (CD) is an aspect of the Continuous Delivery Pipeline that automates the migration of new functionality from a staging environment to production, where it is made available for release.

CD is the third aspect in the four-part Continuous Delivery Pipeline (CDP) of Continuous Exploration (CE), Continuous Integration (CI), Continuous Deployment (CD), and Release on Demand.

Features must be available and verified in production before the business needs them to support Release on Demand. Therefore, it's optimal to separate the deployment process from releasing, enabling changes to move into production without affecting the behavior of the current system. Continuous deployment allows teams to deploy small, incremental changes to production continually.

The capability to continuously deploy is critical for releasing on demand. In turn, it allows Agile Release Train (ARTs) to respond to market opportunities with the highest possible value in the shortest sustainable lead time, permitting customers to consume new functionality when they are ready.

## Details

Traditional development practices treat deployment and release as the same activity. In this model, changes deployed to production are immediately available to users. Continuous deployment, however, separates the deployment and release processes. This practice fosters design thinking and fast value flow by:

- **Targeting functionality to specific customers** – Enables the organization to target customers with particular functionality, allowing the organization to assess the impact of changes before deploying functionality to all customers.
- **Promoting experimentation, such as A/B Testing** – Design thinking practices, such as A/B testing, require the ability to present different functionality to distinct target users.
- **Promoting small batches** – Automating the CDP makes deploying in small batches economically feasible.
- **Releasing on business needs** – ARTs tend to release less frequently when the deployment process is complex and error-prone.

## The Four Activities of Continuous Deployment

SAFe describes four activities of Continuous Deployment:

1. **Deploy** - the practices necessary to deploy a solution to a production environment
2. **Verify** - the practices needed to ensure solution changes operate in production as intended before releasing them to customers
3. **Monitor** - the practices to monitor and report on any issues that may arise in production
4. **Respond** - the practices to address any problems rapidly which may occur during deployment
