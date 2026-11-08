---
id: T-FISSION-YIELDS
name: Fission yields and isotope production
type: technique
field: physics/nuclear
applies_when: the paper reports fission fragment or product yields, isotope production yields or cross sections from reactor or accelerator irradiations, element contents from neutron activation analysis, or results after radiochemical separation, or bases a claim on numbers of fissions or of atoms produced
version: "0.1"
---

# Fission yields and isotope production

## 1. Yield type, timing and precursors

**Question.** Does the paper say which yield it reports (independent, cumulative, chain or mass yield; fragment yield before prompt neutron emission or product yield after it; a fractional or partial yield), and do the irradiation, cooling and separation times match that definition?

**Why it matters.** Most products form both directly and through the beta decay of precursors, and beta-delayed neutron emission moves atoms between mass chains, so a cumulative or chain yield is not the sum of the independent yields of its precursors. An independent yield needs a short irradiation and a fast measurement or separation before the precursors decay, while a chain yield needs a wait until they have. Isomeric states and poorly known branching between them add a further ambiguity, and yields measured at one kinetic energy or ionic charge are partial until integrated.

**Resolved by.** The yield type named for each value, with the convention for chain or mass yields and for any fractional yield; for accelerator production, the yield quantity named (physical, after a stated irradiation, or saturation yield) with its unit, irradiation time and current; irradiation, decay and counting times stated and shown to suit that yield type, with precursor ingrowth or decay modelled where it matters; for isomers, the branching ratios used and which state was measured; the decay data used listed so that the values can be recalculated when those data change.

**Benchmark.** [1], [2], [6]

## 2. Number of fissions and normalisation

**Question.** How was the number of fissions (or the absolute normalisation of relative yields) obtained, by a fission counter, a reference yield, a monitor or a sum rule, and how much of the final uncertainty does this step contribute?

**Why it matters.** Every fission yield is per fission, so the absolute fission rate in the sample is a prerequisite. Fission counters may perturb the flux at the irradiation position, a reference product carries the uncertainty of its own adopted yield, and methods such as classical mass spectrometry or recoil separators give only relative yields, for which the normalisation is often the largest single uncertainty. The chain yields should sum to 200%, but this is a check only if the data have not already been normalised to that sum.

**Resolved by.** The normalisation method described with its own uncertainty: for a fission counter, the deposit mass and how it was determined and the counter's position relative to the sample; for a reference yield, which product and which adopted value; for relative data, how they were tied to an absolute scale; a statement of whether the yields sum to about 200% before any renormalisation, and which chains were missing or estimated.

**Benchmark.** [1]

## 3. Incident energy and neutron spectrum

**Question.** Is the energy of the particles that caused fission or activation characterised (monoenergetic energy and spread, or the reactor spectrum with its thermal, epithermal and fast components), and is the yield attributed to that energy and not to a nominal one?

**Why it matters.** Fission yields change with incident energy and excitation energy, most strongly in the symmetric valley and near resonances, and above the threshold for neutron emission before fission several fissioning nuclei contribute. In a reactor, epithermal neutrons can dominate the activation of nuclides with large resonance integrals: a gold monitor can take about half of its activity from them, so it cannot normalise irradiations in different positions or reactors.

**Resolved by.** The neutron or particle spectrum given, at least by a cadmium ratio or flux-parameter measurement in a reactor and by energy and energy spread for a monoenergetic source; the fissioning system and excitation energy stated, including whether neutron emission before fission is possible; monitors chosen so that they respond to the same part of the spectrum as the measured reaction; comparisons with other data or evaluations made at matching energies.

**Benchmark.** [1], [2]

## 4. Competing and secondary reactions, burn-up and self-shielding

**Question.** Does the paper identify every other route that makes the measured nuclide or one that interferes with it (other target isotopes, threshold reactions with fast neutrons, fission of uranium in the sample, decay of progenitors, capture on precursors or on stable neighbours), and, for long or high-flux irradiations and thick or strongly absorbing samples, correct for burn-up of the target and for neutron self-shielding in the sample and the monitors?

**Why it matters.** The same product can come from several target isotopes, from progenitors, from fission or from capture on a neighbour, so a yield, cross section or element content that ignores them is too high: fission products from uranium in a sample coincide with capture products of several elements, and a shielded fission product may be formed mainly by capture on its stable neighbour. At high fluence, products with large capture cross sections are depleted and their neighbours enhanced, and a strongly absorbing sample or monitor sees a lower flux inside than outside. Isotopic and isomeric impurities in a produced radionuclide cannot be removed chemically: isotopic ones can be limited only by target enrichment and energy window, and isomeric ones not by the energy window.

**Resolved by.** Competing routes listed and either excluded by energy, target enrichment or chemistry, or corrected with stated data; the actual isotopic composition of enriched targets measured, not only taken from the supplier's certificate; for produced radionuclides, radionuclidic and isomeric purity reported at a stated time; the fluence, irradiation history and sample mass and thickness reported; capture and burn-up corrections applied with the cross sections used, or a calculation showing they are negligible; self-shielding and flux depression estimated for samples and monitors, or sample thicknesses shown to be well below the level where they matter.

**Benchmark.** [1], [4], [5], [6], [7]

## 5. Fragment masses from kinematic measurements

**Question.** When fragment masses come from measured energies or velocities of coincident fragments, how were prompt neutron emission, the pulse-height defect, energy loss in the source and backing, and the mass resolution treated, and are pre-neutron and post-neutron masses kept distinct?

**Why it matters.** Mass from momentum conservation assumes the fragment masses before neutron emission; energies change when neutrons are emitted, so an energy-only analysis needs the neutron multiplicity as a function of mass, while velocities are only broadened. Silicon detectors show a pulse-height defect that depends on fragment mass and charge, and thick sources and backings degrade the energies. Limited mass resolution raises low yields and lowers high ones wherever the yield varies steeply with mass, and charge identification by energy loss cannot reliably resolve small fractional yields.

**Resolved by.** The measured quantities (two energies, two velocities, or both) and the neutron-emission correction stated, with its source and uncertainty; pulse-height-defect calibration and target and backing thicknesses given; mass and charge resolution quoted and its effect on peaks, flanks and the valley either unfolded or discussed; the yield's dependence on kinetic energy and, for spectrometers, on ionic charge integrated over the whole distribution.

**Benchmark.** [1], [2]

## 6. Chemical separation and chemical yield

**Question.** After any chemical separation, how was the chemical yield of each element measured, was the carrier or tracer brought into the same chemical form as the radionuclide before separation, and how were losses and cross-contamination between fractions checked?

**Why it matters.** A carrier or tracer measures the recovery of the radionuclide only if the two have exchanged completely. Elements with several oxidation states, such as iodine, or elements that form colloids or adsorb on vessel walls, can stay in a different form, so the measured chemical yield is not the yield of the product. Fast separations needed for short-lived products have the least time to reach exchange, and tracer impurities and ingrowth of tracer progeny bias the result.

**Resolved by.** The separation scheme described with the point at which carrier or tracer was added; a redox step or other treatment that brings all species to a common form before the first separation; the chemical yield measured for each sample by a stated method, with its uncertainty; tracer purity and progeny ingrowth addressed; decontamination from interfering elements shown, for example by the absence of their lines in the separated fraction.

**Benchmark.** [1], [3]

## 7. Standardisation in activation analysis

**Question.** For activation analysis, which standardisation method was used (relative, single-comparator or k0), and does it apply to the facility and reactions?

**Why it matters.** Single-comparator factors hold only for one detector, geometry and irradiation facility, the k0 method needs measured flux parameters and detector efficiencies and covers (n,γ) reactions only, and tabulated cross sections and gamma yields are not accurate enough for an absolute calculation without calibration for the facility.

**Resolved by.** The standardisation method named, with comparator or flux-monitor calibration for the facility, matched sample and standard geometry, and extra calibration where fast-neutron threshold reactions contribute.

**Benchmark.** [5], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | International Atomic Energy Agency, Compilation and evaluation of fission yield nuclear data, final report of a co-ordinated research project 1991–1996, IAEA-TECDOC-1168 (2000) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_1168_prn.pdf |
| 2 | A. N. Andreyev et al., Nuclear fission: a review of experimental advances and phenomenology, Rep. Prog. Phys. 81, 016301 (2018); read as the accepted manuscript in White Rose Research Online | doi:10.1088/1361-6633/aa82eb |
| 3 | U.S. Environmental Protection Agency and others, Multi-Agency Radiological Laboratory Analytical Protocols Manual (MARLAP), NUREG-1576, EPA 402-B-04-001B, Volume II, Chapter 14, Separation Techniques (2004) | https://www.epa.gov/sites/default/files/2015-05/documents/402-b-04-001b-14-final.pdf |
| 4 | P. Bode et al., Neutron activation analysis: a primary (ratio) method to determine SI-traceable values of element content in complex samples, CHIMIA 63, 678 (2009) | doi:10.2533/chimia.2009.678 |
| 5 | International Atomic Energy Agency, Use of research reactors for neutron activation analysis, report of an Advisory Group meeting, IAEA-TECDOC-1215 (2001) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_1215_prn.pdf |
| 6 | International Atomic Energy Agency, Charged particle cross-section database for medical radioisotope production: diagnostic radioisotopes and monitor reactions, final report of a co-ordinated research project, IAEA-TECDOC-1211 (2001) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_1211_prn.pdf |
| 7 | International Atomic Energy Agency, Practical aspects of operating a neutron activation analysis laboratory, IAEA-TECDOC-564 (1990) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_564_web.pdf |
