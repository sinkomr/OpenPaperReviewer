---
id: T-FISSION-YIELDS
name: Fission yields and isotope production
type: technique
field: physics/nuclear
applies_when: the paper reports fission fragment or product yields, isotope production yields or cross sections from reactor or accelerator irradiations, element contents from neutron activation analysis, or results after radiochemical separation, or bases a claim on numbers of fissions or of atoms produced
version: "0.1"
---

# Fission yields and isotope production

Fission yield and isotope production measurements are used to claim how many atoms of a nuclide are formed per fission, per incident particle or per unit of beam charge, and, in neutron activation analysis (NAA), how much of an element a sample contains. The result is a ratio of counted atoms or activities to a number of fissions or to a particle fluence, so it depends on how both were measured, on what happened to the products during irradiation, decay and chemical separation, and on which yield was actually defined.

## 1. Yield type, timing and precursors

**Question.** Does the paper say which yield it reports (independent, cumulative, chain or mass yield; fragment yield before prompt neutron emission or product yield after it; a fractional or partial yield), and do the irradiation, cooling and separation times match that definition?

**Why it matters.** Most products form both directly and through the beta decay of precursors, and beta-delayed neutron emission moves atoms between mass chains, so a cumulative or chain yield is not the sum of the independent yields of its precursors. An independent yield needs a short irradiation and a fast measurement or separation before the precursors decay, while a chain yield needs a wait until they have. Isomeric states and poorly known branching between them add a further ambiguity, and yields measured at one kinetic energy or ionic charge are partial until integrated.

**Resolved by.** The yield type named for each value, with the convention for chain or mass yields and for any fractional yield; irradiation, decay and counting times stated and shown to suit that yield type, with precursor ingrowth or decay modelled where it matters; for isomers, the branching ratios used and which state was measured; the decay data used listed so that the values can be recalculated when those data change.

**Benchmark.** [1], [2]

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

**Benchmark.** [1], [4], [5], [6], [8]

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

## 7. Beam, target and energy scale in accelerator production

**Question.** For cross sections or yields from charged-particle irradiations, how were the number of incident particles, the number of target atoms and the energy in each target layer determined, and which yield quantity, with what unit and irradiation time, is reported?

**Why it matters.** Faraday-cup charge needs good vacuum, insulation and secondary-electron suppression, and converting charge to particles needs the beam's charge state, an error of a factor of two for helium beams. Monitor reactions are only as good as their cross sections, which are updated, and an error in the energy at the monitor matters most where its excitation function is steep. Target thickness, surface oxidation, non-uniformity and the accumulated energy loss through a stack of foils shift both the number of atoms and the energy scale. Thick-target yields are defined in several ways (physical yield, activity after a stated irradiation such as 1 h at 1 µA, or saturation yield) that differ by factors depending on the irradiation time and half-life.

**Resolved by.** The beam-current method described, with monitor reactions identified and their cross sections taken from a current recommended evaluation; target thicknesses measured, with uniformity and chemical state checked; the energy in each foil calculated from a stated stopping-power source, with its uncertainty growing through the stack; the yield quantity named, its unit given, and the irradiation time and current stated so that it can be converted to other definitions.

**Benchmark.** [6], [7]

## 8. Activity measurement and standardisation

**Question.** How were measured gamma-ray peak areas converted to numbers of atoms: is the detector efficiency valid for the actual sample geometry, are coincidence summing, self-attenuation in the sample, dead time and pile-up corrected, are the gamma lines and emission probabilities used stated, and, for activation analysis, which standardisation method was used and does it apply to the facility and reactions?

**Why it matters.** Efficiencies measured with point sources do not apply directly to extended samples or target foils, cascade coincidence summing depends on the counting geometry, low-energy gamma rays are absorbed in dense samples, and published emission probabilities for many products are later revised. In activation analysis, single-comparator factors hold only for one detector, geometry and irradiation facility, the k0 method needs measured flux parameters and detector efficiencies and covers (n,γ) reactions only, and tabulated cross sections and gamma yields are not accurate enough for an absolute calculation without calibration for the facility.

**Resolved by.** An efficiency calibration for the counting geometry actually used, with corrections for source extent, coincidence summing and self-attenuation stated or shown to be small; dead-time and pile-up corrections at the count rates involved; the gamma lines used, their emission probabilities and the data source given, with interfering lines identified and corrected, and consistency between several lines and half-lives shown; for NAA, the standardisation method named, with comparator or flux-monitor calibration for the facility, matched sample and standard geometry, and extra calibration where fast-neutron threshold reactions contribute.

**Benchmark.** [1], [4], [5], [6], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | International Atomic Energy Agency, Compilation and evaluation of fission yield nuclear data, final report of a co-ordinated research project 1991–1996, IAEA-TECDOC-1168 (2000) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_1168_prn.pdf | full text | Sec. 2.2: definitions of independent, cumulative, chain, mass, fragment, fractional and partial yields; delayed neutron emission makes chain yields differ from sums of independent yields; isomer branching often poorly known. Sec. 2.3.1: absolute fission rate is a prerequisite; fission counters can perturb the flux; reference yields; chain yields should sum to 200%, and evaluated files were forced to it. Sec. 2.3.2: capture on fission products depletes and enhances neighbouring yields; a shielded nuclide formed by capture. Sec. 2.3.3: reactor spectrum components; about half of gold monitor activity can be epithermal; report at least the cadmium ratio. Sec. 2.3.4: sample thickness limits for self-shielding. Secs. 2.4.1.1 to 2.4.1.2: chemical yield by added carrier only after complete chemical exchange, problems with iodine oxidation states, colloids and wall adsorption; absolute gamma-ray intensities are often poorly known and later corrected; independent yields need short irradiation and fast separation. Sec. 2.4.2.1: mass-spectrometric yields are relative and normalisation is often the main uncertainty. Sec. 2.4.4: neutron emission shifts energies but only broadens velocities; pulse-height defect; poor mass resolution raises low yields and lowers high ones; small fractional yields below about 5% uncertain; integration over kinetic energy and ionic charge. Sec. 2.6: give decay data so values can be recalculated. Sec. 5.1: valley yields generally rise with excitation energy and fluctuate near resonances |
| 2 | A. N. Andreyev, K. Nishio and K.-H. Schmidt, Nuclear fission: a review of experimental advances and phenomenology, Rep. Prog. Phys. 81, 016301 (2018); read as the accepted manuscript in White Rose Research Online | doi:10.1088/1361-6633/aa82eb | full text | Sec. 3.1.1: with energy-only kinematic analysis the prompt-neutron multiplicity per fragment is needed, whereas velocity measurements need no neutron correction; silicon detectors show a pulse-height defect depending on fragment mass and charge. Sec. 3.2.1: the 2v-2E method gives pre-neutron masses from velocities and post-neutron masses from energies. Sec. 4.3.1: symmetric yields rise with excitation energy, and neutron emission before fission lowers the excitation energy actually reached |
| 3 | U.S. Environmental Protection Agency and others, Multi-Agency Radiological Laboratory Analytical Protocols Manual (MARLAP), NUREG-1576, EPA 402-B-04-001B, Volume II, Chapter 14, Separation Techniques (2004) | https://www.epa.gov/sites/default/files/2015-05/documents/402-b-04-001b-14-final.pdf | full text | Sec. 14.2.1: complete isotopic exchange between added carrier or tracer and all analyte species is needed for quantitative yields, and depends on oxidation state. Sec. 14.9.2.1: the carrier must share the analyte's oxidation state and chemical form and be added early; radioiodine example; carrier recovery gives the chemical yield. Sec. 14.9.3: tracer definition; tracer radionuclide impurities and progeny ingrowth bias results; complete dissolution and exchange needed |
| 4 | P. Bode, R. R. Greenberg and E. A. De Nadai Fernandes, Neutron activation analysis: a primary (ratio) method to determine SI-traceable values of element content in complex samples, CHIMIA 63, 678–680 (2009) | doi:10.2533/chimia.2009.678 | full text | Sec. 1: unique combinations of gamma energies, intensity ratios and half-lives allow consistency checks. Sec. 2: several constants in the absolute measurement equation are hard to know well, so the comparator method is preferred; sample-to-standard ratios of isotopic abundance, neutron fluence (including fluence drop-off, self-shielding and scattering), effective cross section and counting efficiency (geometry and gamma-ray self-shielding). Sec. 3: dense matrices with high-Z elements (gamma-ray self-attenuation) and strongly neutron-absorbing matrices are hard to measure accurately |
| 5 | International Atomic Energy Agency, Use of research reactors for neutron activation analysis, report of an Advisory Group meeting, IAEA-TECDOC-1215 (2001) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_1215_prn.pdf | full text | Annex I, Secs. I.2.1 to I.2.2: relative standardisation is most accurate when standard and sample match; single-comparator k-factors are valid only for a specific detector, geometry and irradiation facility; non-relative and k0 methods need flux parameters and efficiencies, and software handling burn-up, coincidence summing, pile-up and dead time. Secs. I.3.2 to I.4: chemical yield from re-determined carrier in radiochemical NAA; epithermal irradiation to suppress interfering low-Q0 nuclides; neutron self-shielding limits sample mass |
| 6 | International Atomic Energy Agency, Charged particle cross-section database for medical radioisotope production: diagnostic radioisotopes and monitor reactions, final report of a co-ordinated research project, IAEA-TECDOC-1211 (2001) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_1211_prn.pdf | full text | Chapter 1, pp. 1–3: isotopic impurities can only be limited by enriched targets and energy window, isomeric impurities not by energy window; Faraday-cup errors from secondary electrons; monitor foils. Chapter 2, pp. 14–15: sources of discrepancy, namely outdated monitor cross sections, wrong energy where the monitor excitation function is steep, real target thickness, charge-state error of a factor of two for alpha and helium-3 beams, collimator losses, surface oxidation and non-uniform foils, gas-target density reduction, cumulative energy error in stacks; in activity measurement, detector efficiency at low energies, self-absorption of low-energy gamma rays, point-source calibration applied to extended targets, dead time, pile-up and incorrect decay data; parent decay and unclear quantity definitions; enriched targets may not match their certified composition. Appendix, pp. 281–282: physical, 1 h–1 µA and saturation yields and their relation through irradiation time and half-life; elemental and cumulative production cross sections |
| 7 | A. Hermanne and others, Reference cross sections for charged-particle monitor reactions, Nucl. Data Sheets 148, 338–382 (2018); abstract read in the Australian National University research portal record | doi:10.1016/j.nds.2018.02.009 | abstract | Abstract: monitor reactions serve as reference cross sections for accelerator measurements; an IAEA project produced least-squares evaluations with uncertainties for proton, deuteron, helium-3 and alpha monitor reactions, with recommended values distributed by the IAEA Nuclear Data Section |
| 8 | International Atomic Energy Agency, Practical aspects of operating a neutron activation analysis laboratory, IAEA-TECDOC-564 (1990) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_564_web.pdf | full text | Sec. 8.5, pp. 129–130: epithermal irradiation reduces interference from uranium fission, notably for molybdenum and zirconium. Sec. 8.8, pp. 148–150: tabulated cross sections and gamma yields are not accurate enough, so production rates relative to the flux monitor are measured for each facility; the k0 method covers (n,γ) reactions and facilities with fast neutrons need extra calibration for threshold reactions; fission products from uranium coincide with capture products of La, Ce, Nd, Sm, Mo and Ba and need tabulated corrections; spectral interferences corrected using a clean peak of the interfering nuclide |
