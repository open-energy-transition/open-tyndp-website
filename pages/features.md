---
layout: single
title: "Features"
permalink: /features/
toc: true
toc_label: "Features"
toc_icon: "cogs"
---

The National Trends (NT) scenario presented here reflects the TYNDP 2024 methodology. However, some modelling features that will play an important role in future TYNDP cycles are not yet part of the current NT scenario. This page provides an overview of how these features are implemented in Open-TYNDP in alignment with the TYNDP methodology, and of the additional modelling options available in the underlying [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) framework.

[PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) is an open-source energy system model with an active development community, widely used across academia, industry, NGOs, and policy institutions, including transmission system operators, research institutes, and consultancies, with a track record of peer-reviewed research across a wide range of European energy scenarios. The features described here are already fully implemented in [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/), providing a strong foundation. For each feature, we describe the current [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) implementation and, where applicable, the adaptations required to align it with TYNDP methodology within Open-TYNDP. Several features, including offshore grid modelling, split hydrogen zones, and electric vehicle modelling, are already fully available in Open-TYNDP and can be activated through configuration. Others, such as hybrid heating and synthetic fuels, are implemented in [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) but would require further adaptation to align with TYNDP methodology.

## Offshore Grid Modelling

A key innovation in TYNDP 2024 for the DE and GA scenarios was the move away from modelling offshore wind as simple
radial connections to onshore markets. Instead, the European offshore territory is divided
into 56 zones, with offshore hubs that can be interconnected to form a true offshore grid, carrying both electricity and hydrogen.

### Implementation in Open-TYNDP

Open-TYNDP implements this methodology in full. The offshore hub topology, including bus
coordinates, grid connections, capacity potentials, and cost assumptions, is read directly
from the official [TYNDP 2024 input data](https://2024-data.entsos-tyndp-scenarios.eu/files/scenarios-inputs/Offshore-hubs.zip).
Each hub can host electricity-generating and hydrogen-generating offshore wind farms,
standalone electrolysers, and connections to neighbouring hubs and onshore home market
zones. Capacity expansion is constrained by zone-level and technology-level potentials
as defined in the TYNDP 2024 data.

Offshore grid modelling is available in Open-TYNDP and can be activated via `offshore_hubs_tyndp: enable: true`.

<div style="display: flex; gap: 1rem; margin: 1.5rem 0; align-items: center;">
  <figure style="flex: 1; margin: 0;">
    <img src="{{ site.baseurl }}/assets/images/offshore-grid-report.png" alt="Offshore hub infrastructure as defined in TYNDP 2024"/>
  </figure>
  <figure style="flex: 1; margin: 0;">
    <img src="{{ site.baseurl }}/assets/images/offshore-grid.png" alt="Offshore hub infrastructure as implemented in Open-TYNDP"/>
  </figure>
</div>
<p style="font-size: 0.85rem; color: #666; text-align: center; margin-top: 0.5rem;">
  Offshore hub infrastructure as defined in TYNDP 2024 (left) and as implemented in Open-TYNDP (right).
</p>

### Additional Offshore Modelling Options in PyPSA-Eur

Beyond the TYNDP 2024 methodology, [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) supports offshore grid modelling at higher
spatial resolution with fully meshed grids, enabling a more detailed analysis of offshore
wind integration and infrastructure trade-offs.

A peer-reviewed study using [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) demonstrates this capability. The study assesses the
role of meshed offshore grids and offshore hydrogen networks in a carbon-neutral European
energy system.

Read the full publication:

[Glaum, Neumann & Brown (2024): "Offshore power and hydrogen networks for Europe's North Sea", *Applied Energy*, Vol. 369 →](https://doi.org/10.1016/j.apenergy.2024.123530)
{: .notice--info}

<div style="display: flex; gap: 1rem; margin: 1.5rem 0; align-items: center;">
  <figure style="flex: 1; margin: 0;">
    <img src="{{ site.baseurl }}/assets/images/glaum-conncetions-offshore.jpg" alt="Offshore connection types"/>
  </figure>
  <figure style="flex: 0 0 35%; margin: 0;">
    <img src="{{ site.baseurl }}/assets/images/glaum-network.jpg" alt="Offshore network topology" style="width: 100%;"/>
  </figure>
</div>
<p style="font-size: 0.85rem; color: #666; text-align: center; margin-top: -1rem;">
  Offshore connection configurations (left) and resulting network topology (right) from
  Glaum, Neumann & Brown (2024), <em>Applied Energy</em>.
</p>

> **Note:** Fully meshed offshore grids have been developed and demonstrated in peer-reviewed research using PyPSA-Eur. The code is available but not yet part of the main branch.


## Split H₂ Zones

In TYNDP 2024, hydrogen demand and supply are modelled across two distinct zones that
reflect different stages of hydrogen market development in Europe.

**Zone 1** represents decentralised hydrogen demand: plants and facilities distributed
across Europe that produce hydrogen locally, either from on-site electrolysers, shared
renewable sources, or steam methane reformers (SMR/ATR). This zone includes decentralised
pressurised storage sized to cover 24 hours of demand, providing operational flexibility. Over time, Zone 1 consumers are expected to
transition towards renewable hydrogen and connect to the emerging hydrogen grid.

**Zone 2** represents the national and European hydrogen market, a fully interconnected
transmission grid with multiple supply sources, including grid-connected electrolysis,
dedicated renewable feed-in zones with co-located electrolysers, underground storage
(e.g. salt caverns), and extra-EU pipeline imports. This zone captures the large-scale,
price-driven dynamics of a mature hydrogen market, analogous to today's electricity market.

### Implementation in Open-TYNDP

Open-TYNDP implements this two-zone hydrogen structure in full, following the TYNDP 2024
methodology. It can be activated via `h2_zones_tyndp: true`.

### Additional Hydrogen Modelling Options in PyPSA-Eur

Beyond the two-zone TYNDP 2024 methodology, PyPSA-Eur supports hydrogen network modelling at higher spatial resolution, enabling a more detailed analysis of infrastructure trade-offs. This includes endogenous optimisation of hydrogen pipeline expansion as well as retrofitting existing natural gas pipelines for hydrogen transport, capturing both the costs and the path-dependency of transitioning existing gas infrastructure. Underground storage potentials (e.g. salt caverns) are also resolved geographically.

These capabilities have been applied in both academic research and policy-facing analyses examining the role of a European hydrogen network in a net-zero energy system.


<figure style="margin: 1.5rem 0;">
  <img src="{{ site.baseurl }}/assets/images/neumann-h2-networks.jpg" alt="The potential role of a hydrogen network in Europe"/>
</figure>
<p style="font-size: 0.85rem; color: #666; text-align: center; margin-top: 0.5rem;">
  Neumann, Zeyen, Victoria & Brown (2023), <em>Joule</em>.
</p>


Read the full publications:

[Neumann, Zeyen, Victoria & Brown (2023): "The potential role of a hydrogen network in Europe", *Joule*, Vol. 7, Issue 8 →](https://doi.org/10.1016/j.joule.2023.06.016)
{: .notice--info}

[Agora Industry & Agora Energiewende (2024): "EU map of hydrogen production costs — documentation" →](https://www.agora-industry.org/fileadmin/Projekte/2024/2024-07_IND_H2_Production_Costs/EU_Map_H2_Production_Costs_Documentation_WEB.pdf)
{: .notice--info}

[Forschungsstelle für Energiewirtschaft et al. (2024): "European Hydrogen Infrastructure Planning — Insights from the TransHyDE Project System Analysis" →](https://www.wasserstoff-leitprojekte.de/lw_resource/datapool/systemfiles/elements/files/148FFEF003673B67E0637E695E8625E5/live/document/20240321_European_Hydrogen_Infrastructure_Planning.pdf)
{: .notice--info}

## Electric Vehicles

Electric vehicles are modelled as flexible batteries that interact with the electricity grid, capturing both the additional demand from road transport electrification and the system value of smart charging and vehicle-to-grid (V2G) capability.


### Implementation in Open-TYNDP

Open-TYNDP uses the PyPSA-Eur EV modelling methodology, with key input assumptions, including battery capacity, charging rate, and total electricity demand for EVs, adjusted to align with the TYNDP 2024 values.
Electric vehicle demand and charging behaviour are modelled using hourly time series derived from a characteristic weekly driving profile from the German Federal Highway Research Institute (BASt).  The underlying modelling methodology and timeseries approach follow the [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) framework. Road transport demand profiles are scaled to total final energy demand per country from the [JRC-IDEES](https://data.jrc.ec.europa.eu/collection/id-0110) and corrected for the higher efficiency of electric motors compared to internal combustion engines. Temperature-dependent heating and cooling demands are included: combustion vehicles benefit from engine waste heat, reducing their heating demand, while electric vehicles rely on electric heating, increasing electricity consumption in cold weather.

BEVs are modelled with vehicle-to-grid (V2G) capability, meaning a share of the fleet can feed electricity back to the grid when parked. Charging profiles are spread over three hours after travel to reflect typical behaviour. To reflect realistic user expectations, a minimum state of charge is required by early morning, limiting battery use to within-day demand shifting rather than seasonal storage.

In the Open-TYNDP, all vehicles are currently assumed to charge via the distribution network. The TYNDP 2024 methodology additionally models a share of vehicles charging via transmission grid-connected street infrastructure, which is noted as a planned improvement.

### Additional Land Transport Modelling Options in PyPSA-Eur

Beyond the assumed methodology in the Open-TYNDP 2024, [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) supports a more detailed representation of land transport that could be incorporated in future extensions of Open-TYNDP. This includes endogenous optimisation of vehicle type choices, a split between light- and heavy-duty transport, and country-specific vehicle fleet age distribution and fleet turnover. The fuel supply for internal combustion vehicles is also part of the optimisation, covering the full range of options: biofuels, electrofuels (e-fuels), synthetic fuels via Fischer-Tropsch synthesis, and conventional fossil fuels, allowing the model to determine the least-cost decarbonisation pathway across vehicle and fuel choices simultaneously. See the [innovation roadmap](https://open-tyndp.readthedocs.io/en/latest/innovation_roadmap.html) for planned developments.


<figure style="margin: 1.5rem 0;">
  <img src="{{ site.baseurl }}/assets/images/kalweit-land-transport.jpg" alt="Endogenous transformation of land transport in Europe"/>
</figure>
<p style="font-size: 0.85rem; color: #666; text-align: center; margin-top: 0.5rem;">
  Kalweit, Zeyen & Victoria (2025), <em>Energy Conversion and Management</em>, Vol. 344.
</p>



Read the full publication:

[Zeyen, Kalweit, Victoria & Brown (2025): "Shifting burdens: how delayed decarbonisation of road transport affects other sectoral emission reductions", *Environmental Research Letters*, Vol. 20, No. 4 →](https://doi.org/10.1088/1748-9326/adc290)
{: .notice--info}

[Kalweit, Zeyen & Victoria (2025): "Endogenous transformation of land transport in Europe for different climate targets", *Energy Conversion and Management*, Vol. 344 →](https://doi.org/10.1016/j.enconman.2025.120203)
{: .notice--info}

> **Note:** Additional land transport features have been developed and demonstrated in peer-reviewed research using PyPSA-Eur. The code is available but not yet part of the main branch.

## Hybrid Heating

Hybrid heating combines a heat pump with a backup boiler running on gas or hydrogen, providing flexibility to meet peak heat demand while minimising emissions under different decarbonisation pathways.

### Implementation in Open-TYNDP

Hybrid heating modelling is not yet implemented in Open-TYNDP, but the integration is planned following the TYNDP 2024 methodology. The TYNDP approach models hybrid heating as a combination of a heat pump and a backup boiler, running either with gas or hydrogen, with capacities set to meet peak heat demand, country-specific coefficient of performance for the heat pumps based on the climate year, and boiler efficiencies of 93%. Heating demand is prescribed as fixed inputs rather than optimised. See the relevant [issue](https://github.com/open-energy-transition/open-tyndp/issues/380) for the ongoing discussion on implementation.

### Additional Heating Modelling Options in PyPSA-Eur

While aligning with the TYNDP 2024 methodology ensures comparability with the market model, the underlying [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) framework offers a more comprehensive heating sector representation worth considering for future iterations. Rather than prescribing technology dispatch as fixed inputs, PyPSA-Eur optimises the full technology mix, including heat pumps, gas boilers, hybrid heating, combined heat and power (CHP), solar thermal, and resistive heating, endogenously for least-cost supply. Coeefficient of Performance (COPs) for different heat pump types are calculated directly from heating degree days rather than taken from an external model, ensuring consistency with the climate and weather data used throughout the rest of the model. Demand is further disaggregated into residential and service sectors, split between urban and rural areas, and between individual and district heating systems, capturing the full interaction between the heating sector and the electricity and gas systems. Building renovation can also be included as an additional degree of freedom, allowing the model to optimise insulation investments alongside energy supply. See the [innovation roadmap](https://open-tyndp.readthedocs.io/en/latest/innovation_roadmap.html) for further information.

PyPSA-Eur's heating sector capabilities have informed both policy-facing work and academic research. On the applied side, a report by EURIMA and the International Copper Association Europe, [Your Home, Our Future](https://www.yourhomeourfuture.eu/), draws on energy system modelling to assess the role of building renovation and heat pumps in Europe's decarbonisation pathway. Academic studies using PyPSA-Eur have examined a range of heating topics, from mitigating peak demand through renovation and storage to the role of enhanced geothermal systems in district heating.

<figure style="margin: 1.5rem 0;">
  <img src="{{ site.baseurl }}/assets/images/zeyen-heating-v6.svg" alt="Heating sector technologies and demand sectors in PyPSA-Eur"/>
</figure>
<p style="font-size: 0.85rem; color: #666; text-align: center; margin-top: -1rem;">
  Heating sector representation in PyPSA-Eur.
</p>


Read the full publications:

[EURIMA & International Copper Association Europe: "Your Home, Our Future" →](https://www.yourhomeourfuture.eu/)
{: .notice--info}

[Zeyen, Hagenmeyer & Brown (2021): "Mitigating heat demand peaks in buildings in a highly renewable European energy system", *Energy*, Vol. 231 →](https://doi.org/10.1016/j.energy.2021.120784)
{: .notice--info}

[Akhmetov, Fedotova & Frysztacki (2025): "Flattening the peak demand curve through energy efficient buildings: A holistic approach towards net-zero carbon", *Applied Energy*, Vol. 384 →](https://doi.org/10.1016/j.apenergy.2025.125421)
{: .notice--info}

[Franken, Zeyen, Angelidis, Brown & Friedrich (2025): "Market Integration Pathways for Enhanced Geothermal Systems in Europe", *arXiv* →](https://doi.org/10.48550/arXiv.2501.06600)
{: .notice--info}

## Synthetic Fuels

Synthetic fuels, including e-kerosene, e-diesel, and synthetic natural gas (SNG), are produced from renewable electricity and green hydrogen, and are critical for decarbonising hard-to-electrify sectors such as aviation, shipping, and parts of industry.

### Implementation in Open-TYNDP

Synthetic fuel modelling is not yet implemented in Open-TYNDP, but integration is planned in line with the TYNDP 2024 methodology. The TYNDP approach prescribes fixed exogenous demand for e-kerosene, e-diesel, and SNG rather than optimising their production endogenously. Aligning with this methodology would require introducing three additional buses representing these fuel streams, with supply and demand balanced according to the TYNDP assumptions. See the relevant [issue](https://github.com/open-energy-transition/open-tyndp/issues/393) for the ongoing discussion on implementation.

### Additional Synthetic Fuels Modelling Options in PyPSA-Eur

Beyond the TYNDP 2024 methodology, [PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/) models synthetic fuel production as part of the system-wide optimisation rather than as fixed inputs. Demand for SNG, e-diesel, e-kerosene, and other power-to-X products is met through least-cost pathways determined endogenously by the model. The full CO₂ management chain is explicitly modelled, including sourcing carbon feedstocks for synthetic fuel production from point-source capture, direct air capture, or biogenic sources. For example, fuel for internal combustion vehicles can be supplied through any combination of biofuels, electrofuels, synthetic fuels via Fischer-Tropsch synthesis, or conventional fossil fuels — with the model optimising across all options simultaneously. Imports of synthetic fuels and green steel can also be included, allowing the model to assess the role of global supply chains in meeting Europe's decarbonisation targets.

<figure style="margin: 1.5rem 0;">
  <img src="{{ site.baseurl }}/assets/images/neumann-imports.webp" alt="Green energy and steel imports in net-zero European energy scenarios"/>
</figure>
<p style="font-size: 0.85rem; color: #666; text-align: center; margin-top: -1rem;">
  Import volumes, costs, and vectors for net-zero European energy scenarios, from
  Neumann, Hampp & Brown (2025), <em>Nature Communications</em>.
</p>

Read the full publications:

[Neumann, Hampp & Brown (2025): "Green energy and steel imports reduce Europe's net-zero infrastructure needs", *Nature Communications*, Vol. 16 →](https://doi.org/10.1038/s41467-025-60652-1)
{: .notice--info}

[Millinger, Reichenberg, Hedenus, Berndes, Zeyen & Brown (2022): "Are biofuel mandates cost-effective? An analysis of transport fuels and biomass usage to achieve emissions targets in the European energy system", *Applied Energy*, Vol. 326 →](https://doi.org/10.1016/j.apenergy.2022.120016)
{: .notice--info}

[Glaum, Neumann, Millinger & Brown (2025): "A Minimal Methanol Backstop for High Electrification Scenarios", *arXiv* →](https://doi.org/10.48550/arXiv.2505.09277)
{: .notice--info}

## Cross-Sectoral Planning and Sector Coupling

Cross-sectoral planning is an evolving area in European energy infrastructure assessment, with increasing interest in more tightly coupled multi-carrier modelling. Sector coupling, the explicit modelling of linkages between electricity, heat, hydrogen, methane, biomass, and CO₂, is essential for understanding how decarbonisation pathways in one sector affect costs and infrastructure needs in others. This capability is already fully present in the PyPSA-Eur framework.

### Implementation in Open-TYNDP

Open-TYNDP inherits PyPSA-Eur's full sector-coupling architecture, enabling simultaneous optimisation across electricity, hydrogen, methane, biomass, and CO₂, including sequestration. Every region is represented by a set of buses for different energy carriers, connected within regions via conversion technologies (e.g. electrolysers, heat pumps) and across regions via transmission infrastructure. Some energy carriers, such as CO₂, are implemented as "copper plates" to align with the TYNDP 2024 methodology.


### Sector Coupling in PyPSA-Eur — Applications and Research

PyPSA-Eur's sector-coupling capabilities have been applied by transmission system operators, research institutions, and the European Commission for long-term infrastructure planning and policy analysis.

On the industry side, TransnetBW (electricity TSO, southwest Germany), ONTRAS (gas TSO, eastern Germany), and d-fine used PyPSA-Eur-Sec to study grid requirements in 2050 under a 90% CO₂ reduction scenario, published as [Stromnetz 2050](https://www.transnetbw.de/de/stromnetz2050), a 2021 article in *Energiewirtschaftliche Tagesfragen*, and the 2022 study [Energy System 2050 — Towards a Decarbonised Europe](https://www.transnetbw.de/de/energiesystem2050). Austrian Power Grid (APG), the Austrian electricity TSO, uses PyPSA for its long-term system vision up to 2050. Austrian Gas Grid Management AG (AGGM) maintains a high-resolution, sector-coupled model of the Austrian energy system based on PyPSA-Eur, which is used to inform its biannual long-term integrated planning report (Langfristige Integrierte Planung, LFiP). The Fraunhofer Institutes ISI and IEG, together with d-fine, applied a PyPSA-Eur-based approach to assess future-proof European energy infrastructures in the study [Integrated Infrastructure Planning and 2050 Climate Neutrality](https://www.isi.fraunhofer.de/en/presse/2023/presseinfo-27-future-proof-European-energy-infrastructures.html). The Joint Research Centre (JRC) of the European Commission has used PyPSA since 2022 for a range of studies, including analysis of the Fit for 55 package, the role of energy communities (MODECO, 2023), and congestion management (2024).

Academic research using PyPSA-Eur has further explored the interaction between hydrogen and CO₂ networks in a sector-coupled system.

Beyond the cost optimisation itself, PyPSA-Eur handles the full data preparation pipeline in a single automated workflow. Capacity factors for wind and solar, heat demand profiles, temperature-dependent efficiencies, hydro inflow time series, CO₂ sequestration potentials, hydrogen storage capacity, and biomass potentials are all derived directly from raw weather and geographic data. No separate model or manual preprocessing step is required. Open-TYNDP currently uses the provided TYNDP input files for comparability with the market model, but the underlying framework can derive all these inputs independently.

The maps below illustrate four examples of spatially resolved resource potentials that PyPSA-Eur builds directly from raw data: salt cavern hydrogen storage, CO₂ geological sequestration, biogas potentials, and solid biomass potentials.

<div style="display: flex; gap: 0.75rem; margin: 1.5rem 0; align-items: flex-start;">
  <figure style="flex: 1; margin: 0;">
    <img src="{{ site.baseurl }}/assets/images/caverns.png" alt="Salt cavern H₂ storage potential" style="width: 100%;"/>
    <p style="font-size: 0.8rem; color: #666; text-align: center; margin-top: 0.4rem;">Salt cavern H₂ storage potential</p>
  </figure>
  <figure style="flex: 1; margin: 0;">
    <img src="{{ site.baseurl }}/assets/images/co2-storage-potential-conservative.png" alt="CO₂ geological sequestration potential" style="width: 100%;"/>
    <p style="font-size: 0.8rem; color: #666; text-align: center; margin-top: 0.4rem;">CO₂ geological sequestration potential</p>
  </figure>
  <figure style="flex: 1; margin: 0;">
    <img src="{{ site.baseurl }}/assets/images/biogas_potentials.png" alt="Biogas potentials" style="width: 100%;"/>
    <p style="font-size: 0.8rem; color: #666; text-align: center; margin-top: 0.4rem;">Biogas potentials</p>
  </figure>
  <figure style="flex: 1; margin: 0;">
    <img src="{{ site.baseurl }}/assets/images/solid_biomass_potentials.png" alt="Solid biomass potentials" style="width: 100%;"/>
    <p style="font-size: 0.8rem; color: #666; text-align: center; margin-top: 0.4rem;">Solid biomass potentials</p>
  </figure>
</div>

These spatially resolved inputs feed into the full system optimisation. The figure below illustrates one example of a research outcome: the competition and complementarity between hydrogen and CO₂ transport networks in a cost-optimal, carbon-neutral European energy system.

<figure style="margin: 1.5rem 0;">
  <img src="{{ site.baseurl }}/assets/images/hofmann-carbon-networks-2.webp" alt="H2 and CO2 network strategies for the European energy system"/>
</figure>
<p style="font-size: 0.85rem; color: #666; text-align: center; margin-top: 0.5rem;">
  Optimisation of CO₂, H₂ and electricity networks in a sector-coupled European system (Hofmann, Tries, Neumann, Zeyen & Brown (2025), <em>Nature Energy</em>).
</p>

Read the full publications and reports:

[TransnetBW, ONTRAS & d-fine (2020): "Stromnetz 2050" →](https://www.transnetbw.de/de/stromnetz2050)
{: .notice--info}

[TransnetBW, ONTRAS & d-fine (2021): "Die Rolle von Wasserstoff in einem klimaneutralen europäischen Energiesystem", *Energiewirtschaftliche Tagesfragen* →](https://www.transnetbw.de/de/energiesystem2050)
{: .notice--info}

[TransnetBW, ONTRAS & d-fine (2022): "Energy System 2050 — Towards a Decarbonised Europe" →](https://www.transnetbw.de/de/energiesystem2050)
{: .notice--info}

[Austrian Power Grid (APG): System Vision of the Austrian Energy System up to 2050 →](https://www.apg.at/en/markt/netzentwicklung/netzentwicklungsplan)
{: .notice--info}

[Austrian Gas Grid Management AG (AGGM): Langfristige Integrierte Planung (LFiP) →](https://www.aggm.at/netzentwicklung/langfristige-integrierte-planung)
{: .notice--info}

[Fraunhofer ISI, Fraunhofer IEG & d-fine: "Integrated Infrastructure Planning and 2050 Climate Neutrality: Deriving Future-Proof European Energy Infrastructures" →](https://www.isi.fraunhofer.de/en/presse/2023/presseinfo-27-future-proof-European-energy-infrastructures.html)
{: .notice--info}

[Joint Research Centre (JRC) of the European Commission (2022): "PyPSA-based analysis of the Fit for 55 package", *Energies* →](https://doi.org/10.3390/en15124233)
{: .notice--info}

[Hofmann, Tries, Neumann, Zeyen & Brown (2025): "H2 and CO2 network strategies for the European energy system", *Nature Energy*, Vol. 10 →](https://doi.org/10.1038/s41560-025-01752-6)
{: .notice--info}
