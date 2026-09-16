---
layout: single
title: "Methodology"
permalink: /methodology/
toc: true
toc_label: "Contents"
toc_icon: "list"
---

## Overview for policy and planning stakeholders

Open-TYNDP is an open-source energy system model that implements the [TYNDP 2024](https://www.entsoe.eu/outlooks/tyndp/2024/) methodology in a similar way to what has been developed within the ENTSO-E TYNDP process under multiple, proprietary and open-source, tools. It is developed by [Open Energy Transition](https://openenergytransition.org/) and the project is in coordination with ENTSO-E. It portrays an additional open-source environment while disseminating, to the extent possible, the TSOs' experience accumulated over several years of collaborating within ENTSO-E on delivering the TYNDP. This page explains how the model works and what it offers to stakeholders involved in European energy infrastructure planning.

**Transparency:** Open-TYNDP is fully auditable, every assumption, input dataset, and modelling step is documented and openly accessible. This facilitates TSOs, authorities, industry associations, researchers and other stakeholders to understand how outcomes can be produced, verify them independently, and build trust in the results.

**Built for collaboration:** Because the model is open source, TSOs and other stakeholders can directly inspect and modify assumptions to reflect their own national contexts, test sensitivities, or contribute to improvements. There is no dependency on vendors or proprietary platforms, and no license fees, reducing barriers to participation for all stakeholders across the European TSO community.

**A streamlined, reproducible workflow:** Open-TYNDP provides a single, version-controlled workflow that takes raw input data all the way through to fully visualised results with a single command for each phase of the TYNDP. This makes analysis reproducible, updates straightforward to implement, and results easy to share and audit across organisations.

**European software:** The model is built entirely on open-source tools developed and maintained within Europe, with no dependency on software vendors outside of Europe.[^1]

**Rigorous benchmarking**: Open-TYNDP is benchmarked systematically against TYNDP 2024 reference data for the NT scenario to demonstrate that its outcomes are directionally consistent with the established TYNDP methodology. Benchmarking outcomes are discussed in the [Results](/results/) section.

## Input data & general process

Open-TYNDP is built on [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/), a free and open-source European energy system model developed and maintained by a broad international research community. Open-TYNDP is a soft-fork of PyPSA-Eur, adapted to align with the [TYNDP 2024](https://www.entsoe.eu/outlooks/tyndp/2024/) methodology, assumptions, and input data. This means it inherits the full modelling framework of PyPSA-Eur, including the optimisation structure, network representation, and sector-coupling capabilities, while replacing or adjusting specific inputs and assumptions to match the TYNDP 2024 reference scenario.

### Scenario Building (SB)

Public input data from ENTSO-E as well as the values observed in the Market Model output files have been used as the reference for fixed input assumptions. The diagram below gives an overview of the data sources and how they flow into Open-TYNDP and the benchmarking process. The depicted data flow applies strictly to exogenous variables that are not part of the optimisation.



<figure style="margin: 1.5rem 0;">

<svg style="width:100%;height:auto;" viewBox="0 0 980 680" xmlns="http://www.w3.org/2000/svg" width="980" height="680">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#888"/>
    </marker>
    <marker id="arr-blue" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#378ADD"/>
    </marker>
    <marker id="arr-orange" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#BA7517"/>
    </marker>
    <marker id="arr-purple" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#534AB7"/>
    </marker>
    <marker id="arr-red" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#E8311A"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="490" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="#1d1f2c" font-family="'Oxanium', sans-serif">TYNDP 2024 Scenario Building — Data Overview</text>
  <a href="https://2024.entsos-tyndp-scenarios.eu/download/" target="_blank">
    <text x="490" y="44" text-anchor="middle" font-size="11" fill="#185FA5" font-family="'Poppins', sans-serif" text-decoration="underline">All datasets available at 2024.entsos-tyndp-scenarios.eu/download</text>
  </a>
  <text x="490" y="58" text-anchor="middle" font-size="9" fill="#378ADD" font-family="'Poppins', sans-serif">↓ click any dataset name to download the source file</text>

  <!-- INPUT DATA BOX -->
  <g id="input-data-container">
    <rect x="20" y="65" width="240" height="305" rx="8" fill="#E6F1FB" stroke="#B5D4F4" stroke-width="1"/>
    <text x="140" y="87" text-anchor="middle" font-size="12" font-weight="700" fill="#0C447C" font-family="'Oxanium', sans-serif">Public Input Data</text>
  </g>

  <g id="input-pemmdb">
    <a href="https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-inputs/PEMMDB2.zip" target="_blank">
      <rect x="34" y="97" width="212" height="28" rx="4" fill="#ffffff" stroke="#B5D4F4" stroke-width="0.5"/>
      <text x="44" y="115" font-size="11" fill="#185FA5" font-family="'Poppins', sans-serif" text-decoration="underline">PEMMDB 2.5</text>
      <text x="239" y="115" text-anchor="end" font-size="10" fill="#666" font-family="'Poppins', sans-serif">capacities, must-runs</text>
    </a>
  </g>

  <g id="input-pecd">
    <a href="https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-inputs/PECD.zip" target="_blank">
      <rect x="34" y="131" width="212" height="28" rx="4" fill="#ffffff" stroke="#B5D4F4" stroke-width="0.5"/>
      <text x="44" y="149" font-size="11" fill="#185FA5" font-family="'Poppins', sans-serif" text-decoration="underline">PECD 3.1</text>
      <text x="239" y="149" text-anchor="end" font-size="10" fill="#666" font-family="'Poppins', sans-serif">RES profiles</text>
    </a>
  </g>

  <g id="input-hydro">
    <a href="https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-inputs/Hydro-Inflows.zip" target="_blank">
      <rect x="34" y="165" width="212" height="28" rx="4" fill="#ffffff" stroke="#B5D4F4" stroke-width="0.5"/>
      <text x="44" y="183" font-size="11" fill="#185FA5" font-family="'Poppins', sans-serif" text-decoration="underline">Hydro Inflows</text>
      <text x="239" y="183" text-anchor="end" font-size="10" fill="#666" font-family="'Poppins', sans-serif">hydro profiles</text>
    </a>
  </g>

  <g id="input-demand">
    <a href="https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-inputs/Demand-Profiles.zip" target="_blank">
      <rect x="34" y="199" width="212" height="28" rx="4" fill="#ffffff" stroke="#B5D4F4" stroke-width="0.5"/>
      <text x="44" y="217" font-size="11" fill="#185FA5" font-family="'Poppins', sans-serif" text-decoration="underline">Demand Profiles</text>
      <text x="239" y="217" text-anchor="end" font-size="10" fill="#666" font-family="'Poppins', sans-serif">elec + H₂</text>
    </a>
  </g>

  <g id="input-linedata">
    <a href="https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-inputs/Line-data.zip" target="_blank">
      <rect x="34" y="233" width="212" height="28" rx="4" fill="#ffffff" stroke="#B5D4F4" stroke-width="0.5"/>
      <text x="44" y="251" font-size="11" fill="#185FA5" font-family="'Poppins', sans-serif" text-decoration="underline">Line Data</text>
      <text x="239" y="251" text-anchor="end" font-size="10" fill="#666" font-family="'Poppins', sans-serif">elec + H₂, start 2030</text>
    </a>
  </g>

  <g id="input-investment">
    <a href="https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-inputs/Investment-Datasets.zip" target="_blank">
      <rect x="34" y="267" width="212" height="28" rx="4" fill="#ffffff" stroke="#B5D4F4" stroke-width="0.5"/>
      <text x="44" y="285" font-size="11" fill="#185FA5" font-family="'Poppins', sans-serif" text-decoration="underline">Investment Candidates</text>
      <text x="239" y="285" text-anchor="end" font-size="10" fill="#666" font-family="'Poppins', sans-serif">2035 / 2040</text>
    </a>
  </g>

  <g id="input-hydrogen">
    <a href="https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-inputs/Hydrogen.zip" target="_blank">
      <rect x="34" y="301" width="212" height="28" rx="4" fill="#ffffff" stroke="#B5D4F4" stroke-width="0.5"/>
      <text x="44" y="319" font-size="11" fill="#185FA5" font-family="'Poppins', sans-serif" text-decoration="underline">Hydrogen</text>
      <text x="239" y="319" text-anchor="end" font-size="10" fill="#666" font-family="'Poppins', sans-serif">stores, SMR, imports</text>
    </a>
  </g>

  <!-- more data indicator -->
  <g id="input-more">
    <rect x="34" y="335" width="212" height="24" rx="4" fill="#E6F1FB" stroke="#B5D4F4" stroke-width="0.5" stroke-dasharray="4,2"/>
    <text x="140" y="351" text-anchor="middle" font-size="10" fill="#888" font-family="'Poppins', sans-serif" font-style="italic">+ more datasets …</text>
  </g>

  <!-- SUPPLY TOOL BOX -->
  <g id="supply-tool">
    <a href="https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-outputs/20240518-Supply-Tool.xlsm.zip" target="_blank">
      <rect x="20" y="385" width="240" height="75" rx="8" fill="#FAEEDA" stroke="#FAC775" stroke-width="1"/>
      <text x="140" y="407" text-anchor="middle" font-size="12" font-weight="700" fill="#633806" font-family="'Oxanium', sans-serif" text-decoration="underline">Supply Tool</text>
      <text x="140" y="423" text-anchor="middle" font-size="10" fill="#854F0B" font-family="'Poppins', sans-serif">Methane demand, biomass potentials</text>
      <text x="140" y="439" text-anchor="middle" font-size="10" fill="#854F0B" font-family="'Poppins', sans-serif">Energy carriers modelled in Open-TYNDP</text>
    </a>
  </g>

  <!-- OPEN-SOURCE MODEL ADVANTAGE (separate box) -->
  <g id="opensource-note">
    <rect x="20" y="475" width="240" height="145" rx="8" fill="#E1F5EE" stroke="#9FE1CB" stroke-width="1"/>
    <text x="140" y="496" text-anchor="middle" font-size="11" font-weight="700" fill="#085041" font-family="'Oxanium', sans-serif">Open-source model advantage</text>
    <text x="140" y="512" text-anchor="middle" font-size="10" fill="#0F6E56" font-family="'Poppins', sans-serif">In the underlying open-source framework,</text>
    <text x="140" y="526" text-anchor="middle" font-size="10" fill="#0F6E56" font-family="'Poppins', sans-serif">RES profiles, hydro inflows, and demand</text>
    <text x="140" y="540" text-anchor="middle" font-size="10" fill="#0F6E56" font-family="'Poppins', sans-serif">time series can be derived directly from</text>
    <text x="140" y="554" text-anchor="middle" font-size="10" fill="#0F6E56" font-family="'Poppins', sans-serif">raw weather data — no additional model</text>
    <text x="140" y="568" text-anchor="middle" font-size="10" fill="#0F6E56" font-family="'Poppins', sans-serif">needed. The same applies to biomass</text>
    <text x="140" y="582" text-anchor="middle" font-size="10" fill="#0F6E56" font-family="'Poppins', sans-serif">potentials. Open-TYNDP currently uses the</text>
    <text x="140" y="596" text-anchor="middle" font-size="10" fill="#0F6E56" font-family="'Poppins', sans-serif">provided TYNDP input files for comparability.</text>
  </g>

  <!-- MARKET MODEL BOX -->
  <g id="market-model">
    <rect x="390" y="115" width="240" height="85" rx="8" fill="#2C2C2A" stroke="#444" stroke-width="0.5"/>
    <text x="510" y="148" text-anchor="middle" font-size="13" font-weight="700" fill="#F1EFE8" font-family="'Oxanium', sans-serif">Market Model</text>
    <text x="510" y="166" text-anchor="middle" font-size="10" fill="#aaaaaa" font-family="'Poppins', sans-serif">Current TYNDP process (proprietary)</text>
    <text x="510" y="182" text-anchor="middle" font-size="10" fill="#aaaaaa" font-family="'Poppins', sans-serif">used for Scenario Building</text>
  </g>

  <!-- OPEN-TYNDP BOX -->
  <g id="open-tyndp">
    <rect x="360" y="310" width="300" height="110" rx="8" fill="#FDECEA" stroke="#E8311A" stroke-width="1.5"/>
    <text x="510" y="333" text-anchor="middle" font-size="13" font-weight="700" fill="#B71C1C" font-family="'Oxanium', sans-serif">Open-TYNDP</text>
    <text x="510" y="351" text-anchor="middle" font-size="10" fill="#C62828" font-family="'Poppins', sans-serif">Open-source alternative for Scenario Building</text>
    <text x="510" y="367" text-anchor="middle" font-size="10" fill="#C62828" font-family="'Poppins', sans-serif">Can be used alongside the Market Model</text>
    <text x="510" y="383" text-anchor="middle" font-size="10" fill="#C62828" font-family="'Poppins', sans-serif">Benchmarks outcomes against public output data</text>
    <text x="510" y="403" text-anchor="middle" font-size="9" fill="#888" font-family="'Poppins', sans-serif"><a href="https://zenodo.org/records/18713081" target="_blank"><tspan text-decoration="underline">Results on Zenodo</tspan></a><tspan> · Interactive maps on this website</tspan></text>
  </g>

  <!-- OUTPUT DATA BOX -->
  <g id="output-data-container">
    <rect x="740" y="65" width="220" height="390" rx="8" fill="#EAF3DE" stroke="#C0DD97" stroke-width="1"/>
    <text x="850" y="87" text-anchor="middle" font-size="12" font-weight="700" fill="#27500A" font-family="'Oxanium', sans-serif">Public Output Data</text>
  </g>

  <g id="output-mmfiles">
    <a href="https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-outputs/MMStandardOutputFile_NT2030_Plexos_CY2009_2.5_v40.xlsx.zip" target="_blank">
      <rect x="754" y="97" width="192" height="50" rx="4" fill="#ffffff" stroke="#C0DD97" stroke-width="0.5"/>
      <text x="764" y="116" font-size="11" fill="#3B6D11" font-family="'Poppins', sans-serif" text-decoration="underline">Market Model Output Files</text>
      <text x="764" y="134" font-size="10" fill="#666" font-family="'Poppins', sans-serif">NT 2030 &amp; 2040 · hourly · per node</text>
    </a>
  </g>

  <g id="output-report">
    <a href="https://2024.entsos-tyndp-scenarios.eu/wp-content/uploads/2024/05/TYNDP_2024-Scenario-Report-Data-Figures_240522.xlsx" target="_blank">
      <rect x="754" y="155" width="192" height="50" rx="4" fill="#ffffff" stroke="#C0DD97" stroke-width="0.5"/>
      <text x="764" y="174" font-size="11" fill="#3B6D11" font-family="'Poppins', sans-serif" text-decoration="underline">Final Scenarios Report</text>
      <text x="764" y="192" font-size="10" fill="#666" font-family="'Poppins', sans-serif">EU27 annual aggregated</text>
    </a>
  </g>

  <g id="output-visplatform">
    <a href="https://2024.entsos-tyndp-scenarios.eu/visualisation-platform/" target="_blank">
      <rect x="754" y="213" width="192" height="28" rx="4" fill="#ffffff" stroke="#C0DD97" stroke-width="0.5"/>
      <text x="764" y="232" font-size="11" fill="#3B6D11" font-family="'Poppins', sans-serif" text-decoration="underline">Visualisation Platform</text>
    </a>
  </g>

  <g id="output-fixedinputs-note">
    <rect x="754" y="253" width="192" height="110" rx="4" fill="#F1EFE8" stroke="#C0DD97" stroke-width="0.5"/>
    <text x="764" y="270" font-size="10" fill="#5F5E5A" font-family="'Poppins', sans-serif">Output files also contain fixed</text>
    <text x="764" y="284" font-size="10" fill="#5F5E5A" font-family="'Poppins', sans-serif">input assumptions (e.g. demand).</text>
    <text x="764" y="300" font-size="10" fill="#5F5E5A" font-family="'Poppins', sans-serif">For benchmarking on this website,</text>
    <text x="764" y="314" font-size="10" fill="#5F5E5A" font-family="'Poppins', sans-serif">only Market Model Output Files and</text>
    <text x="764" y="328" font-size="10" fill="#5F5E5A" font-family="'Poppins', sans-serif">Scenarios Report figures are used.</text>
  </g>

  <!-- ARROWS -->

  <!-- Input Data → Market Model -->
  <line x1="260" y1="157" x2="388" y2="157" stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>

  <!-- Market Model → Output Data -->
  <line x1="630" y1="157" x2="738" y2="157" stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>

  <!-- Input Data → Open-TYNDP (①) -->
  <line x1="260" y1="360" x2="358" y2="360" stroke="#888" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arr)"/>
  <text x="263" y="352" font-size="10" fill="#555" font-family="'Poppins', sans-serif">① public input data</text>

  <!-- Supply Tool → Open-TYNDP -->
  <polyline points="260,422 310,422 310,365 358,365" fill="none" stroke="#BA7517" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arr-orange)"/>

  <!-- Market Model Output → Open-TYNDP (② fallback) -->
  <polyline points="850,455 850,560 510,560 510,422" fill="none" stroke="#BA7517" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arr-orange)"/>
  <text x="530" y="552" font-size="10" fill="#BA7517" font-family="'Poppins', sans-serif">② if public input data ≠ fixed values in output files</text>
  <text x="530" y="568" font-size="9" fill="#BA7517" font-family="'Poppins', sans-serif">(applied to H₂ demand, reference grids, maintenance profiles)</text>

  <!-- Open-TYNDP → Output (Benchmarking) -->
  <line x1="660" y1="360" x2="738" y2="360" stroke="#888" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arr)"/>
  <text x="663" y="352" font-size="10" fill="#555" font-weight="500" font-family="'Poppins', sans-serif">Benchmarking</text>

</svg>

<p style="font-size: 0.85rem; color: #666; text-align: center; margin-top: 0.5rem;">TYNDP 2024 Scenario Building data overview diagram</p>
</figure>

### Cost-Benefit Analysis (CBA)


Open-TYNDP also implements the [Cost-Benefit Analysis (CBA)](https://consultations.entsoe.eu/system-development/tyndp-2024-cba-implementation-guidelines/) methodology used by ENTSO-E to assess the costs and benefits of individual transmission and storage projects submitted for the TYNDP. Rather than optimising the network topology, the CBA workflow evaluates specific candidate projects against a common reference grid, quantifying their impact on the wider European energy system.

In Open-TYNDP, the CBA workflow is integrated into the Snakemake pipeline, covering the full path from SB to CBA in a single reproducible workflow. This makes the link between the two steps explicit: the network simplification and additional assumptions required for CBA are applied directly on top of the SB output.

<figure style="margin: 1.5rem 0;">

<svg style="width:100%;height:auto;" viewBox="0 0 1608 260" xmlns="http://www.w3.org/2000/svg" width="1608" height="260" role="img">
  <title>Open-TYNDP CBA workflow overview</title>
  <desc>Diagram of the Open-TYNDP Cost-Benefit Analysis workflow, read left to right: the Scenario Building network is modified for CBA using the CBA Implementation Guidelines by adjusting the reference grid, reducing lost of load costs, and merging nodes to a market model. The modified network, in combination with the TYNDP project map, is used to create a reference network and project networks. The reference network is solved once with full-year perfect foresight to extract marginal storage values. Afterwards, the reference network and every project network are each solved separately with rolling horizon and with the marginal storage values. Results between each project network and the reference network are compared to compute indicators, and indicators are benchmarked against the official TYNDP 2024 results. This whole process is done for each planning horizon.</desc>

  <defs>
    <marker id="arrow-gray" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#5f5e5a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#BA7517" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <a href="https://consultations.entsoe.eu/system-development/tyndp-2024-cba-implementation-guidelines/" target="_blank">
    <rect x="244" y="20" width="150" height="44" rx="8" fill="#FAEEDA" stroke="#BA7517" stroke-width="0.5"/>
    <text x="319" y="42" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#633806" text-decoration="underline">CBA guidelines</text>
  </a>
  <line x1="319" y1="64" x2="319" y2="140" stroke="#BA7517" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow-amber)"/>

  <a href="https://tyndp2024.entsoe.eu/projects-map/" target="_blank">
    <rect x="438" y="20" width="150" height="44" rx="8" fill="#FAEEDA" stroke="#BA7517" stroke-width="0.5"/>
    <text x="513" y="42" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#633806" text-decoration="underline">TYNDP project map</text>
  </a>
  <line x1="513" y1="64" x2="513" y2="140" stroke="#BA7517" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow-amber)"/>

  <a href="https://tyndp2024.entsoe.eu/projects-map/" target="_blank">
    <rect x="1408" y="20" width="150" height="44" rx="8" fill="#FAEEDA" stroke="#BA7517" stroke-width="0.5"/>
    <text x="1483" y="42" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#633806" text-decoration="underline">TYNDP project map</text>
  </a>
  <line x1="1483" y1="64" x2="1483" y2="140" stroke="#BA7517" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow-amber)"/>

  <rect x="40" y="140" width="170" height="90" rx="8" fill="#FAEEDA" stroke="#BA7517" stroke-width="0.5"/>
  <text x="125" y="170" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#633806">SB network</text>
  <text x="125" y="200" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#854F0B">Result of SB run</text>

  <line x1="210" y1="185" x2="234" y2="185" stroke="#5f5e5a" stroke-width="1.5" marker-end="url(#arrow-gray)"/>

  <rect x="234" y="140" width="170" height="90" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
  <text x="319" y="165" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#0C447C">Modify for CBA</text>
  <text x="319" y="185" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#185FA5">Adjust grid &amp; costs</text>
  <text x="319" y="201" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#185FA5">merge to market model</text>

  <line x1="404" y1="185" x2="428" y2="185" stroke="#5f5e5a" stroke-width="1.5" marker-end="url(#arrow-gray)"/>

  <rect x="428" y="140" width="170" height="90" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
  <text x="513" y="170" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#0C447C">Project scenarios</text>
  <text x="513" y="200" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#185FA5">PINT or TOOT</text>

  <line x1="598" y1="185" x2="622" y2="185" stroke="#5f5e5a" stroke-width="1.5" marker-end="url(#arrow-gray)"/>

  <rect x="622" y="140" width="170" height="90" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
  <text x="707" y="170" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#0C447C">Reference scenario</text>
  <text x="707" y="200" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#185FA5">Full-year foresight</text>
  <rect x="742" y="128" width="50" height="22" rx="11" fill="#444441" stroke="none"/>
  <text x="767" y="139" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="500" fill="#F1EFE8">1 run</text>

  <line x1="792" y1="185" x2="816" y2="185" stroke="#5f5e5a" stroke-width="1.5" marker-end="url(#arrow-gray)"/>

  <rect x="816" y="140" width="170" height="90" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
  <text x="901" y="170" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#0C447C">Storage values</text>
  <text x="901" y="200" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#185FA5">Long-term storage</text>

  <line x1="986" y1="185" x2="1010" y2="185" stroke="#5f5e5a" stroke-width="1.5" marker-end="url(#arrow-gray)"/>

  <rect x="1010" y="140" width="170" height="90" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
  <text x="1095" y="170" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#0C447C">Rolling horizon</text>
  <text x="1095" y="200" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#185FA5">Projects + reference</text>
  <rect x="1105" y="128" width="70" height="22" rx="11" fill="#444441" stroke="none"/>
  <text x="1140" y="139" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="500" fill="#F1EFE8">1 + N runs</text>

  <line x1="1180" y1="185" x2="1204" y2="185" stroke="#5f5e5a" stroke-width="1.5" marker-end="url(#arrow-gray)"/>

  <rect x="1204" y="140" width="170" height="90" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
  <text x="1289" y="170" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#0C447C">Compute indicators</text>
  <text x="1289" y="200" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#185FA5">Compare vs. reference</text>

  <line x1="1374" y1="185" x2="1398" y2="185" stroke="#5f5e5a" stroke-width="1.5" marker-end="url(#arrow-gray)"/>

  <rect x="1398" y="140" width="170" height="90" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
  <text x="1483" y="170" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#0C447C">Benchmark results</text>
  <text x="1483" y="200" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#185FA5">vs. TYNDP 2024</text>
</svg>

<p style="font-size: 0.85rem; color: #666; text-align: center; margin-top: 0.5rem;">Open-TYNDP CBA workflow overview diagram</p>
</figure>



Project-level data, including project identifiers, connecting nodes, capacities, and cost estimates, is sourced from the ENTSO-E [TYNDP projects map](https://tyndp2024.entsoe.eu/projects-map/) and associated project sheets. The reference grid is cross-checked against the [CBA Implementation Guidelines](https://consultations.entsoe.eu/system-development/tyndp-2024-cba-implementation-guidelines/) (Appendix B.1) to ensure a consistent reference grid. As with the Scenario Building in the Open-TYNDP, all data processing steps are version-controlled and reproducible.

The CBA process builds on the SB network, with a number of modifications applied to align with the CBA Implementation Guidelines:

- Change of the cost of lost load to 300 Eur/MWh
- Merge prosumer nodes and high voltage nodes to one single market node
- Modify the reference grid based on the CBA Implementation Guidelines Appendix B.1


The modified SB network is extended to form the CBA reference network by using the TNYDP project map, and this reference network is first solved using perfect foresight for the entire year to expose the marginal storage values (MSV). The reference network and MSV results are then combined and solved using rolling horizon, for the reference baseline and then for each project.

Indicators are computed as the difference between the reference and project dispatch solutions. The following indicators are calculated:

- B1: Impact on operational system costs (socio-economic welfare)
- B2: Impact on societal cost of CO2 emissions
- B3: Impact on renewable capacity, generation, and avoided curtailment
- B4: Impact on pollutants (NOx, SO2, PM)

Open-TYNDP currently implements the CBA as a pure market model. As a result, only the system-level indicators B1–B4 can be calculated at this stage; indicators that require a higher network resolution are currently not supported.

## Benchmarking

Results are benchmarked against ENTSO-E reference data for the National Trends (NT) scenario, climate year 2009 for the Scenario Building and three climate years for the Cost-Benefit Analysis (2009, 2008, and 1995).


### What is benchmarking?

Benchmarking is a structured approach to comparing the outcomes of two or more models. For Open-TYNDP, it provides a reproducible and automated way to compare outcomes against those from the TYNDP 2024, measure discrepancies, and trace their causes to specific modelling choices or input differences, inherent or not to the specific tools used.

Benchmarking was monitored continuously during the development phase of Open-TYNDP.
The Open Energy Transition (OET) team introduced benchmarking statistics to Open-TYNDP to
systematically measure differences between Open-TYNDP results and those from TYNDP 2024.
This allowed the team to identify how development actions,
such as aligning inputs and integrating new data sources,
closed the discrepancy between Open-TYNDP and TYNDP 2024 results.

### Why is benchmarking important?

Open-TYNDP is built entirely on publicly available data and open-source tools. Every assumption, input, and calculation is auditable, version-controlled, and reproducible. Benchmarking is how we demonstrate that this transparency does not come at the cost of accuracy: the goal is to show that an open-source modelling workflow can produce outcomes that are directionally consistent with TYNDP 2024 and therefore robust enough to support strategic planning discussions.

This matters because open-source energy system models, despite wide adoption in research and academia, are still underused in industry and regulatory contexts. Rigorous benchmarking against established reference data builds the evidence base that industry stakeholders need to trust and adopt open models with confidence.


### What results did you benchmark for the Open-TYNDP model?

#### Scenario Building

Open-TYNDP outcomes are benchmarked against ENTSO-E reference data for the National Trends (NT) scenario, climate year 2009. The following outputs were benchmarked:

- Cross-border electricity flows (yearly net flows)
- Generation mix by technology and country
- Installed generation capacities vs. TYNDP report figures
- Hydrogen supply and demand balances
- Marginal prices by region and carrier

Benchmarking outcomes are published with every release on [Zenodo](https://doi.org/10.5281/zenodo.18608105).

#### Cost-Benefit Analysis

For the Cost-Benefit Analysis (CBA), Open-TYNDP benchmarks:

- The system-level cost-benefit indicators B1–B4 for each project, compared against ENTSO-E reference values

Since Open-TYNDP currently implements the CBA as a market model, only indicators B1–B4 are benchmarked at this stage.

> **Note:** the official TYNDP 2024 CBA results published by ENTSO-E are themselves averaged values across five different models, with outliers removed. It is these publicly available, averaged reference results that Open-TYNDP results are benchmarked against — not the output of any single underlying model.

### Reference data sources

#### Scenario Building

Open-TYNDP is benchmarked against publicly available data,
such as that shared by ENTSO-E on the TYNDP
[scenarios website](https://2024.entsos-tyndp-scenarios.eu/download/).

Specific data sources used to benchmark Open-TYNDP results against include:

- [ENTSO-E TYNDP 2024 Scenarios Report figures](https://2024-data.entsos-tyndp-scenarios.eu/files/reports/TYNDP-2024-Scenarios-Package-20250128.zip)
- [Market model output files](https://2024.entsos-tyndp-scenarios.eu/download/)
- [TYNDP 2024 Visualisation platform data](https://2024.entsos-tyndp-scenarios.eu/visualisation-platform/)

#### Cost-Benefit Analysis


Open-TYNDP is benchmarked against publicly available CBA data shared by ENTSO-E on the [TYNDP 2024 projects map](https://tyndp2024.entsoe.eu/projects-map/).


### What happens if the results do not match?

All remaining deviations between Open-TYNDP and ENTSO-E reference results are documented
and traceable to specific modelling choices.
These are discussed in detail in the [Results](/results/) section.

### What input data is used and how does this affect the results?

All input data used in Open-TYNDP is documented and version-controlled. Key inputs include reference grids for electricity and hydrogen, final energy demands by sector and country, and installed capacity assumptions per TYNDP scenario.

Much of the work of developing Open-TYNDP was integrating these publicly available datasets from ENTSO-E into the
[PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) workflow.

[^1]: Solvers are external to the model and chosen by the user. The framework is solver-agnostic by design.
