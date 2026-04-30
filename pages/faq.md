---
layout: single
title: "FAQ"
permalink: /faq/
toc: true
toc_label: "Questions"
toc_icon: "question-circle"
---
## What Does "Open-Source" Mean?

Open-source software is software whose source code is publicly available for anyone to read,
use, modify, and redistribute. Unlike proprietary software, where the code is hidden and
access requires a licence, open-source tools are transparent by design. Anyone can inspect
how the model works, verify its results, and build on top of it. For energy planning, this
means regulators, researchers, and TSOs can independently verify modelling assumptions and
outcomes.


## What Is a "Workflow" and Why Does It Matter?

A workflow is an automated sequence of modelling steps, from data preparation and network
construction through to optimisation and results, that can be run end-to-end with a single
command. Open-TYNDP uses [Snakemake](https://snakemake.readthedocs.io) to manage its
workflow. This means every result is fully reproducible: given the same inputs, anyone running
the workflow will get the same outputs. It also means the entire modelling process is
documented in code rather than in manual steps that are hard to audit.


## Is Open-TYNDP a Replacement for ENTSO-E's TYNDP Process?

No. Open-TYNDP is designed as a complementary, transparent tool that enables independent benchmarking and scenario testing independently from the official TYNDP process. It focuses on replicating Scenarios Building and Cost Benefit Analysis of the TYNDP 2024. It is built to strengthen — not replace — ENTSO-E’s planning process.

## How Does Open-TYNDP Relate to [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/)?

Open-TYNDP is a soft-fork of [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/), adapted specifically to align with TYNDP 2024 methodology, input data, and network topology. It tracks upstream [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) developments and benefits from the broader PyPSA community.


## What Is a "Soft-Fork"?

A fork is a copy of an existing software project that is developed independently. A soft-fork
stays closely aligned with the original project, regularly incorporating updates and
improvements from upstream, rather than diverging into a fully separate codebase. Open-TYNDP
is a soft-fork of [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/): it adds
TYNDP-specific data, methodology, and network topology on top of PyPSA-Eur, while continuing
to benefit from the broader PyPSA community's development. This means improvements to
PyPSA-Eur flow through to Open-TYNDP over time.

## Can I Run My Own Scenarios?

Yes. The model is fully open-source and reproducible via Snakemake. New scenarios can typically be configured and run within hours. See the [documentation](https://open-tyndp.readthedocs.io) for details.

## What Scenarios Are Currently Benchmarked?

Benchmarking has been performed for the National Trends (NT) scenario from TYNDP 2024, using climate year 2009. Results are compared against ENTSO-E reference outputs and  market model data.

## Where Can I Report Issues or Contribute?

Open an issue or pull request on [GitHub](https://github.com/open-energy-transition/open-tyndp). Contributions are welcome.

## Who Funds and Maintains Open-TYNDP?

Open-TYNDP is funded by [Breakthrough Energy](https://breakthroughenergy.org), [QCF](https://www.qc.foundation/), and other philanthropies, with previous support from [Google.org](https://google.org).

Open-TYNDP is developed and maintained by [Open Energy Transition (OET)](https://openenergytransition.org). As an open-source project, contributions from the wider community are welcome. Anyone can propose improvements, report issues, or extend the tool's functionality via the [GitHub repository](https://github.com/open-energy-transition/open-tyndp).

## What Tools Is This Website Built With?

This website is built with [Jekyll](https://jekyllrb.com) using the [Minimal Mistakes](https://mademistakes.com/work/minimal-mistakes-jekyll-theme/) theme.
