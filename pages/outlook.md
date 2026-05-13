---
layout: single
title: "Outlook"
permalink: /outlook/
toc: true
toc_label: "Roadmap"
toc_icon: "road"
---

## Overview for Policy and Planning Stakeholders

Open-TYNDP is developed by [Open Energy Transition](https://openenergytransition.org/) to strengthen European energy infrastructure planning through open, reproducible, and auditable modelling. It enables ENTSO-E and its member TSOs to make every assumption, input, and modelling step openly accessible via an additional open source platform for European studies. Therefore, Open-TYNDP allows TSOs, regulators, researchers, and other stakeholders to understand and build confidence in model outcomes and to contribute more efficiently in the planning process.

Open-TYNDP potentially complements ENTSO-E’s existing suite of tools as an additional open-source contribution, broadening the basis for understanding the energy system and expanding the range of insights available.

This page gives an overview of where Open-TYNDP is heading. It covers three areas: the **innovation roadmap**, which tracks planned improvements to align Open-TYNDP with the evolving TYNDP methodology; the **integrated model builder**, which explains how Open-TYNDP currently automates the full workflow from raw data to final results in a single terminal command; and **advanced modelling capabilities** already available in the underlying framework that could support more robust and comprehensive infrastructure planning in the future.

## Innovation Roadmap

The Open-TYNDP innovation roadmap is structured to directly reflect the evolution of the TYNDP process itself. It compares the current and upcoming features of the Open-TYNDP workflow, including those already implemented in the underlying PyPSA-Eur framework, against the **TYNDP Innovation Roadmap**, which lists desirable features for the 2026 TYNDP cycle. This means Open-TYNDP development is guided by the official process, ensuring the open-source alternative stays relevant and complementary as methodology requirements evolve. The full roadmap is maintained in the documentation:
[open-tyndp.readthedocs.io ↗](https://open-tyndp.readthedocs.io/en/latest/innovation_roadmap.html)

## Open-TYNDP as an Integrated Model Builder

Open-TYNDP is not just an optimisation model. It is a complete, automated model builder powered by [Snakemake](https://snakemake.readthedocs.io/en/stable/). Currently, a single command in the terminal takes the full workflow from raw input data all the way through to fully optimised results and their visualisations, with no manual preprocessing or separate toolchain required.

### The Open-Source Toolchain Behind Open-TYNDP

Open-TYNDP is built on two open-source components. [PyPSA](https://pypsa.org/) (Python for Power Systems Analysis) is the core modelling engine, a software framework for modelling energy systems that is independent of any country-specific data and widely maintained by a broad open-source community. It supports large, sector-coupled energy system optimisation problems and provides the mathematical and computational foundation for everything built on top of it.

[PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) is a fully sector-coupled energy system model and model builder of the European energy sector that uses PyPSA under the hood. It combines PyPSA with a complete, automated data pipeline built on Snakemake, using only publicly available data to create model instances that are built, solved, and post-processed in a single integrated workflow. PyPSA-Eur is highly configurable: a single configuration file controls spatial and temporal resolution, enables or disables features such as synthetic fuels, hybrid heating, electric vehicles, or split H₂ zones, and selects between open-source and commercial solvers.

Open-TYNDP is a PyPSA-Eur-compatible soft fork, a model extension that replaces PyPSA-Eur's default datasets with ENTSO-E input data and adjusts the configuration to recreate the TYNDP 2024 Scenario Building methodology. All differences between PyPSA-Eur and Open-TYNDP are visible by comparing the two [GitHub repositories](https://github.com/open-energy-transition/open-tyndp). The soft-fork structure means that improvements developed in either project can be transferred to the other, while keeping Open-TYNDP aligned with the TYNDP methodology.

### From Raw Data to Final Modelling Results

The workflow automatically derives everything the optimisation needs directly from raw geographic and weather data: capacity factors for wind and solar, heat demand profiles, heat pump COPs, hydro inflow time series, spatially resolved biomass and biogas potentials, and CO₂ geological sequestration capacities. Open-TYNDP currently uses the TYNDP 2024 input files for these quantities to ensure comparability with the market model, but the framework can generate all of them independently, reducing the number of models and manual steps required in the process.

### CBA — Streamlined Process

In Open-TYNDP, the Cost-Benefit Analysis workflow is integrated into the Snakemake pipeline, covering the full path from Scenario Building to CBA in a single reproducible workflow. This makes the link between the two steps explicit: the network simplification and additional assumptions required for CBA are applied directly on top of the Scenario Building output.


### An Open Interface for the Modelling Community

Because each processing step is a self-contained Snakemake rule with defined inputs and outputs, it is straightforward for other modelling teams to plug in: replace a single rule with an alternative script, inject outputs from another model at a specific step, or run the Open-TYNDP workflow to a certain point and convert the results to a different format. This makes Open-TYNDP a practical entry point for a broader open-source modelling ecosystem around European infrastructure planning.

## Potential Features from the Open-Source Framework

Beyond the TYNDP-aligned roadmap, the underlying [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) framework provides a range of advanced modelling capabilities that could be activated or integrated in future Open-TYNDP releases. These are already fully implemented and used in peer-reviewed research.

### Modelling to Generate Alternatives (MGA)

Exploring "What If" Scenarios: Standard models usually give you one "cheapest" answer. However, there are often many different ways to build a system that cost almost the same but look very different—like using more wind versus more solar. MGA helps us find these alternatives so planners can choose the one that is most socially or politically acceptable.

This is particularly valuable for infrastructure planning, where understanding which features are robust across many cost-equivalent solutions strengthens policy advice and acknowledges structural model uncertainties. For example, MGA can reveal whether offshore wind is essential across all near-optimal solutions, or whether onshore wind and storage could substitute it at similar cost.

Read the full publications:

[Neumann & Brown (2021): "The near-optimal feasible space of a renewable power system model", *Electric Power Systems Research*, Vol. 190 →](https://doi.org/10.1016/j.epsr.2020.106690)
{: .notice--info}

[Millinger, Hedenus, Zeyen, Neumann, Reichenberg & Berndes (2025): "Diversity of biomass usage pathways to achieve emissions targets in the European energy system", *Nature Energy*, Vol. 10 →](https://doi.org/10.1038/s41560-024-01693-6)
{: .notice--info}

### Risk-Averse Optimisation

Planning for the "Worst-Case". Most models plan for the "average" year. The risk-aware approach implemented in PyPSA-Eur integrates rare but severe events, such as a "Dunkelflaute" (a prolonged period without sun or wind), into the optimisation. This ensures the infrastructure plan is both resilient and cost-effective.

This capability is particularly relevant for long-term infrastructure planning, where investments must remain robust across a wide range of future weather years and demand conditions. Results from risk-averse optimisation tend to favour greater long-duration storage, cross-border interconnection, and geographic diversity of renewables — key considerations for TYNDP infrastructure assessment.

Read the full publication:

[Bernecker, Sgarciu, Kan, Anvari, Riepin & Müsgens (2026): "Adaptive robust optimization for European electricity system planning considering regional Dunkelflaute events", *Applied Energy*, Vol. 412 →](https://doi.org/10.1016/j.apenergy.2026.127671)
{: .notice--info}

### Cross-Sectoral Planning and Sector Coupling

As described in detail in the [Features](/features/#full-sector-coupling) section, PyPSA-Eur already supports full sector coupling — simultaneous optimisation across electricity, heat, hydrogen, methane, biomass, and CO₂ networks. Activating these capabilities within Open-TYNDP would enable a genuinely interlinked multi-carrier model, addressing the growing need for cross-sectoral infrastructure planning in European energy policy.

## Open-Source Community Benefits

Open-TYNDP is built on PyPSA-Eur, which is actively developed by a broad community of researchers and practitioners. This means Open-TYNDP continuously benefits from upstream improvements in solver interfaces, network representation, and sector-coupling features — without additional development effort.
