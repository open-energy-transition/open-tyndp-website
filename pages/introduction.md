---
layout: single
title: "Introduction"
permalink: /introduction/
toc: true
toc_label: "Contents"
toc_icon: "info-circle"
---

Open-TYNDP is an open-source implementation following the ENTSO-E [TYNDP 2024 methodology](https://www.entsoe.eu/outlooks/tyndp/2024/): transparent, reproducible, and built for collaboration. This page explains what it is, how it works, and who it is for.

## What is Open-TYNDP?

Open-TYNDP is an open-source energy system model for the ENTSO-E Ten-Year Network Development Plan (TYNDP), developed and maintained by [Open Energy Transition (OET)](https://openenergytransition.org) in dialogue with ENTSO-E. It is built on [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur), adapted to the TYNDP 2024 methodology and input data. It focuses on two blocks of TYNDP 2024: Scenario Building and Cost Benefit Analysis.


## What did we do?

- Exploratory study in coordination with ENTSO-E, for producing TYNDP Scenario Building 2024 and Cost Benefit Analysis 2024 in an open-source framework
- Soft-forked [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur) and adapted its methodology, assumptions, and input data to align with TYNDP 2024
- Implemented TYNDP-specific scenario logic, demand projections, and network topology
- Benchmarked model outcomes for Scenario Building and Cost Benefit Analysis against ENTSO-E reference data for the National Trends (NT) scenario, using 2009 as the reference climate year for the Scenario Building.

## Results

- Capacity, generation mix, network flows, cross-border flows, and marginal prices can be explored interactively on the [Results](/results/) page
- Open-TYNDP outcomes are benchmarked against ENTSO-E reference outputs — remaining deviations are documented and traceable to specific modelling choices that are often tool specific

## Where can Open-TYNDP help?

- **Transparency** — not only assumption and input are visible and auditable, but also the models.
- **Reproducibility** — any stakeholder is able to re-run TYNDP 2024 National Trends scenario independently.
- **Additional resource** — allows for broader expert contribution.
- **Automated workflow** — The entire modelling process runs automatically, from raw inputs to final outputs

## Who benefits from this?

- **TSO planners** — additional open-source alternative for grid investment scenarios and sensitivity analysis
- **ENTSO-E leadership** — broader benchmarking of TYNDP results builds process legitimacy
- **Researchers & policymakers** — full access to a pan-European model calibrated to TYNDP 2024 data
- **Grid planners beyond Europe** — the same methodology can be applied to regional data, making Open-TYNDP a reusable framework for sharing the know-how and experience of the TSOs performing the TYNDP

## What can people do with the Open-TYNDP?

- Independently reproduce and examine TYNDP 2024 National Trends scenario based on published data from ENTSO-E
- Test custom scenarios (e.g. alternative demand or RES assumptions) without starting from scratch
- Directly compare open-source PyPSA model results with ENTSO-E outputs in a transparent framework
- Build on a common, community-maintained European planning model
- Collaborate more easily across organisations and institutions using a shared, open codebase
- Benefit from the continuous developments and features of an open-source framework, driven by a broad community of researchers and practitioners

## Code & data availability

- Fully open-source on [GitHub](https://github.com/open-energy-transition/open-tyndp)
- Reproducible workflows via [Snakemake](https://snakemake.readthedocs.io/en/stable/) and [pixi](https://pixi.prefix.dev/latest/) environment management
- Get started easily with the [documentation](https://open-tyndp.readthedocs.io) and hands-on [workshop notebooks](https://open-energy-transition.github.io/open-tyndp-workshops/intro.html)
- [One-click Windows installer](https://github.com/open-energy-transition/open-tyndp/releases) available for easy setup
- Input and output data archived on [Zenodo](https://doi.org/10.5281/zenodo.18608105) for full reproducibility
