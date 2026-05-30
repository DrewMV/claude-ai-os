---
source_url: https://framework.scaledagile.com/assume-variability-preserve-options
scraped: 2026-05-30
authenticated: true
---

# Principle #3 – Assume variability; preserve options

> Generate alternative system-level designs and subsystem concepts. Rather than try to pick an early winner, aggressively eliminate alternatives. The designs that survive are your most robust alternatives.
>
> —Allen C. Ward

Solution development is an inherently uncertain process. Technical variability and market variability are present throughout the development process. By definition, innovative new systems have never been developed, so there is no guaranteed path to success. If there were, it wouldn't be innovation. That's why we love this business.

System developers are naturally inclined to reduce variability as quickly as possible. The more deterministic things are, the better we feel. That's just human nature. It seems that the more we think we know and have already decided, the further along we think we are. And that's true up to a point, but variability is still present.

Variability is inherently neither bad nor good—it just is what it is. The economics associated with the timing and type of variability determines outcomes. The goal is to manage variability, and preserve options, providing the controls and flexibility teams need to build great solutions.

This article describes managing variability and preserving options with set-based design. For more on managing variability, see Principle #7—Apply cadence; synchronize with cross-domain planning.

## Development Occurs in an Uncertain World

Acknowledging the continued presence of variability in development causes us to reexamine our approach. Traditional, sequential, stage-gated development practices drive developers to quickly converge on a 'point-based' single option—an agreed to point in the requirements and design solution space—and then modify the design until it meets the system intent. Everyone feels good that they have the right requirements and the right design. At least for a while.

However, the probability that it is the right starting point is low. Subsequent development efforts to make that solution work waste time and lead to significant delivery problems [2].

There just isn't enough time to recover. The reason is that we are operating early in the 'cone of uncertainty [3] and attempting to force certainty by freezing requirements and design. The bigger and more technically innovative the system is, the higher the odds are that the agreed starting point was not the best one. And unfortunately, as that risk becomes more and more apparent, we often turn to even tighter specifications, even earlier in the discovery process. The problem isn't resolved; it's compounded.

## Preserve Options with Set-Based Design

A better approach, referred to as Set-Based Design (SBD) or Set-Based Concurrent Engineering (SBCE), provides multiple design options.

In this approach, developers initially cast a wider design net, considering multiple design choices at the start. After that, they continuously evaluate economic and technical trade-offs—typically exhibited by the objective evidence presented at integration-based learning points. Then they eliminate the weaker options over time and ultimately converge on a final design based on the knowledge gained to that point.

This process leaves the design options open for as long as possible, converges when necessary, and produces more optimal technical and economic outcomes.

Note: Due to big systems' scope and economic impact, set-based design is a fundamental construct of Large Solution SAFe. For more information, including guidance on applying set-based design to fixed schedule commitments, planning impact, and economic trade-offs, read the Set-Based Design article and the Enterprise Solution Delivery competency articles.

## Learn More

[1] Reinertsen, Donald G. The Principles of Product Development Flow: Second Generation Lean Product Development. Celeritas, 2009.

[2] Iansiti, Marco. Shooting the Rapids: Managing Product Development in Turbulent Environments. California Management Review, 38. 1995.

[3] McConnell, Steve. Software Project Survival Guide. Microsoft Press, 1997.

[4] Ward, Allan C., and Durward Sobek. Lean Product and Process Development. Lean Enterprise Institute Inc., 2014.

Last update: 14 March 2023
