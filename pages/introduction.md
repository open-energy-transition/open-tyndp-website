---
layout: single
title: "Introduction"
permalink: /introduction/
toc: true
toc_label: "Contents"
toc_icon: "info-circle"
---

Open-TYNDP is an open-source implementation following the ENTSO-E [TYNDP 2024 methodology](https://www.entsoe.eu/outlooks/tyndp/2024/).
It is a transparent and reproducible workflow, built for collaboration in the energy sector.
This page explains why Open Energy Transition built it, what it is, how it works, and who it is for.

## Why did Open Energy Transition build Open-TYNDP?

The [TYNDP](https://tyndp.entsoe.eu/) guides billions of euros in European grid infrastructure investment — decisions that will shape the continent's energy system for decades. Getting these decisions right is critical for Europe's net-zero 2050 goals. Open-TYNDP makes this process open: a pan-European model calibrated to TYNDP 2024 data, available for independent audit and benchmarking.

It supports:

* **Transparency** — not only are assumptions and inputs visible and auditable, but also the models.

* **Reproducibility** — any stakeholder is able to re-run TYNDP 2024 National Trends scenario independently.

* **Additional resources** — allows for broader expert contribution.

* **Automated workflow** — The entire modelling process runs automatically, from raw inputs to final outputs

## What is Open-TYNDP?

Open-TYNDP is an open-source energy system model for the ENTSO-E Ten-Year Network Development Plan (TYNDP),
developed and maintained by [Open Energy Transition (OET)](https://openenergytransition.org) in dialogue with ENTSO-E.
It is built on [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur), adapted to the TYNDP 2024 methodology and input data.
It focuses on two blocks of TYNDP 2024: Scenario Building and Cost Benefit Analysis.

## How does it work?

Open-TYNDP was adapted by Open Energy Transition from a soft-fork of the open-source [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur)
modelling workflow to the methodology, assumptions, and input data of TYNDP 2024.

Open Energy Transition also implemented TYNDP-specific scenario logic, demand projections, and network topology.

Then, the model outcomes for Scenario Building and Cost Benefit Analysis were benchmarked with ENTSO-E reference data for the National Trends (NT) scenario, using 2009 as the reference climate year for the Scenario Building.

Open-TYNDP produces results for the capacity, generation mix, network flows, cross-border flows, and marginal prices which can be explored interactively on the [Results](/results/) page. The Open-TYNDP outcomes are benchmarked against ENTSO-E reference outputs and remaining deviations are documented and traceable to modelling choices that are often tool specific.

## What can you do with the Open-TYNDP?

- Independently reproduce and examine TYNDP 2024 National Trends scenario based on published data from ENTSO-E
- Test custom scenarios (e.g. alternative demand or RES assumptions) without starting from scratch
- Directly compare open-source PyPSA model results with ENTSO-E outputs in a transparent framework
- Build on a common, community-maintained European planning model
- Collaborate more easily across organisations and institutions using a shared, open codebase
- Benefit from the continuous developments and features of an open-source framework, driven by a broad community of researchers and practitioners

## Who is it for?

Open-TYNDP is intended for a range of users involved in energy system planning, analysis, and policy.

* **TSO planners** — Open-TYNDP can be used as an additional open-source alternative for grid investment scenarios and sensitivity analysis.

* **ENTSO-E leadership** — the model provides a broader benchmarking of TYNDP results which increases process legitimacy.

* **Researchers & policymakers** — an open-source solution gives researchers and policymakers full access to a pan-European model calibrated to TYNDP 2024 data.

* **Independent project developers** - an open-source model aligned with TYNDP assumptions and scenarios enables project developers to identify investment opportunities compatible with European and national planning.

* **Grid planners beyond Europe** — the Open-TYNDP methodology can be applied to regional data, which makes it a reusable framework for sharing the know-how and experience of the TSOs performing the TYNDP.

## Code & Data Availability

- Fully open-source on [GitHub](https://github.com/open-energy-transition/open-tyndp)
- Reproducible workflows via [Snakemake](https://snakemake.readthedocs.io/en/stable/) and [pixi](https://pixi.prefix.dev/latest/) environment management
- Get started easily with the [documentation](https://open-tyndp.readthedocs.io) and hands-on [workshop notebooks](https://open-energy-transition.github.io/open-tyndp-workshops/intro.html)
- [One-click Windows installer](https://github.com/open-energy-transition/open-tyndp/releases) available for easy setup
- Input and output data archived on [Zenodo](https://doi.org/10.5281/zenodo.18608105) for full reproducibility

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-4PQV9MZ7EQ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-4PQV9MZ7EQ');
</script>
