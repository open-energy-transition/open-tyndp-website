---
layout: single
title: "Introduction"
permalink: /introduction/
toc: true
toc_label: "Contents"
toc_icon: "info-circle"
---

Open-TYNDP is an open-source implementation following the ENTSO-E [TYNDP 2024 methodology](https://www.entsoe.eu/outlooks/tyndp/2024/): transparent, reproducible, and built for collaboration. This page explains what it is, how it works, and who it is for.

## What Is Open-TYNDP?

Open-TYNDP is an open-source energy system model for the ENTSO-E Ten-Year Network Development Plan (TYNDP), developed by [Open Energy Transition (OET)](https://openenergytransition.org) in collaboration with ENTSO-E. It is built on [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur), adapted to the TYNDP 2024 methodology and input data. It focuses on two blocks of TYNDP 2024: Scenario Building and Cost Benefit Analysis.


## What Did We Do?

- Exploratory study in coordination with ENTSO-E, for replicating TYNDP Scenario Building 2024 and Cost Benefit Analysis 2024
- Soft-forked [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur) and adapted its methodology, assumptions, and input data to align with TYNDP 2024
- Implemented TYNDP-specific scenario logic, demand projections, and network topology
- Benchmarked model outcomes against ENTSO-E reference data for the National Trends (NT) scenario, using 2009 as the reference climate year

## Results

- Capacity, generation mix, network flows, cross-border flows, and marginal prices can be explored interactively on the [Results](/results/) page
- Open-TYNDP outcomes are benchmarked against ENTSO-E reference outputs — remaining deviations are documented and traceable to specific modeling choices

## Where Can Open-TYNDP Help?

- **Transparency** — not only assumption and input are visible and auditable, but also the models.
- **Reproducibility** — any stakeholder is able to re-run TYNDP 2024 National Trends scenario independently.
- **Additional resource** — allow for broader expert contribution.
- **Automated workflow** — The entire modelling process runs automatically, from raw inputs to final outputs

## What Can People Do with Open-TYNDP?

- Independently reproduce and examine official TYNDP 2024 National Trends scenario
- Test custom scenarios (e.g. alternative demand or RES assumptions) without starting from scratch
- Directly compare open-source model results for TYNDP 2024 with ENTSO-E outputs in a transparent framework
- Build on a common, community-maintained European planning model
- Collaborate across organisations and institutions using a shared, open codebase
- Benefit from the continuous developments and features of an open-source framework, driven by a broad community of researchers and practitioners

## Code & Data Availability

- Fully open-source on [GitHub](https://github.com/open-energy-transition/open-tyndp)
- Reproducible workflows via [Snakemake](https://snakemake.readthedocs.io/en/stable/) and [pixi](https://pixi.prefix.dev/latest/) environment management
- Get started easily with the [documentation](https://open-tyndp.readthedocs.io) and hands-on [workshop notebooks](https://open-energy-transition.github.io/open-tyndp-workshops/intro.html)
- [One-click Windows installer](https://github.com/open-energy-transition/open-tyndp/releases) available for easy setup
- Input and output data archived on [Zenodo](https://doi.org/10.5281/zenodo.18608105) for full reproducibility
