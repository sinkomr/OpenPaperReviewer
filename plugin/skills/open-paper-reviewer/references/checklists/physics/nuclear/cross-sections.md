---
id: T-CROSS-SECTIONS
name: Nuclear cross-section measurements
type: technique
field: physics/nuclear
applies_when: the paper reports a measured nuclear reaction cross section, excitation function, reaction yield, astrophysical S-factor, resonance strength, angular distribution or activation result from neutron or charged-particle beams, or compares such data with evaluated nuclear data libraries
version: "0.1"
---

# Nuclear cross-section measurements

## 1. Target areal density, composition and beam overlap

**Question.** How were the number of target nuclei per unit area, the isotopic and chemical composition and the uniformity of the target measured, and how was the overlap between the beam spot and the target taken into account?

**Why it matters.** The areal density of the target enters the cross section as a direct factor, so any error in it shifts every data point together. Powders and dissolved samples can contain air pockets or absorbed water, enriched samples have uncertain isotopic fractions, and a non-uniform target gives a wrong effective areal density when the beam is smaller or larger than the target.

**Resolved by.** The target thickness or areal density measured by a stated method, such as weighing, ion beam analysis, a resonance scan or the decay activity of a radioactive target, with its uncertainty; isotopic enrichment and impurities given; uniformity checked, and the beam profile and beam-target overlap measured; corrections for attenuation and multiple scattering in the sample stated, or shown to be negligible.

**Benchmark.** [1], [2], [3], [7]

## 2. Target stability under beam

**Question.** Was the target checked for loss of material, change of composition or deposits during the irradiation, for example by repeated yield measurements at a fixed energy or repeated resonance scans?

**Why it matters.** Intense beams heat, sputter and damage solid targets, and residual gas in the beam line can build up carbon on the surface. The number of target nuclei and the energy loss in the target then change during the run, and data taken late in an irradiation can be biased against data taken early.

**Resolved by.** The accumulated charge on each target stated; the target profile or yield at a reference energy remeasured at intervals and the change reported; measures against heating and carbon build-up described; any loss corrected for, with its uncertainty, or data from degraded targets excluded by a stated rule.

**Benchmark.** [2], [3]

## 3. Beam current, fluence and normalization

**Question.** How was the number of incident particles determined: by current integration, a monitor reaction, a flux detector or normalization to a standard cross section, and which reference cross-section values were used?

**Why it matters.** Most neutron cross sections are measured relative to a standard cross section, and a cross section cannot be more accurate than the reference it is measured against. Monitor reactions used to determine charged-particle fluence carry their own cross-section, decay-data and foil-thickness uncertainties, and a value that has since been revised shifts the whole data set.

**Resolved by.** The fluence method stated, with the beam's charge state when Faraday-cup charge is converted to particles; for monitor reactions or standards, the reaction, the source and version of the reference cross section and its uncertainty; the monitor foils or flux detector characterized with the same care as the main target; where several monitors are used, agreement between them shown; the normalization uncertainty reported separately from point-to-point uncertainties.

**Benchmark.** [1], [4], [5], [6], [10]

## 4. Beam energy, energy loss and resolution

**Question.** How was the incident energy calibrated, how was the effective reaction energy inside the target obtained from the energy loss in it, and what energy spread is assigned to each data point?

**Why it matters.** The beam loses energy as it crosses the target and any degraders, so the effective energy depends on stopping powers, target thickness and composition. Stopping-power errors have shifted low-energy cross sections by several per cent or more, energy straggling broadens the beam progressively through a stack of foils, and an energy-scale error near a resonance or a steep threshold produces large errors in the cross section.

**Resolved by.** The beam-energy calibration and its uncertainty stated; the stopping-power tables or transport code named, with an uncertainty assigned to the computed energy loss; where the cross section varies steeply with energy, the effective energy defined and its uncertainty carried into the result; for stacked foils, energies checked against monitor reactions and not only computed; the energy spread or resolution function given for each point; for time-of-flight measurements, the flight path, time binning and any overlap of slow neutrons from earlier pulses described.

**Benchmark.** [1], [3], [4], [6]

## 5. Detection efficiency and decay data

**Question.** How was the efficiency of the detection system determined, including solid angle, thresholds and particle-identification cuts, dead time and, for gamma-ray counting, coincidence summing, and which decay data were used to convert activities into numbers of product nuclei, separating direct production from decay feeding?

**Why it matters.** The efficiency enters the cross section as a direct factor. Close counting geometry raises the count rate but brings in true coincidence summing, which can be corrected only if the decay cascade is well known; thresholds and event-selection cuts can reject real events, as when two reaction products travel together and fail the selection, and thick samples can stop the products before they reach the detector. Outdated half-lives or gamma-ray intensities bias activation results, and a product also fed by the decay of a precursor gives a cumulative cross section, not an independent one.

**Resolved by.** The efficiency calibration sources and method stated, with simulations used only to interpolate between measured points or validated against them; for gamma rays above calibration-source energies, efficiency extended with resonances of known cascades and checked against a validated simulation; summing corrections given, or shown to be negligible by counting at more than one distance; the effect of thresholds and cuts on the efficiency estimated; dead-time corrections stated; the half-lives and emission probabilities used, with their sources; for activation, each cross section labelled as independent or cumulative, with precursor feeding subtracted where an independent value is claimed.

**Benchmark.** [1], [4], [6], [7], [11]

## 6. Backgrounds and competing reactions

**Question.** Which background sources were identified and how was each measured or modelled: room background, beam-induced reactions on contaminants and backings, scattered neutrons, and other reactions that produce the same product or the same signal?

**Why it matters.** Light-element contaminants in target backings and in materials near the target can produce gamma rays or particles close to the signal of interest. Neutrons scattered from the surroundings, if underestimated, raise apparent cross sections of reactions that are large at low energy. In activation measurements on natural targets, several isotopes can produce the same product, and material near the foils can add its own activity.

**Resolved by.** Each background source listed with the measurement used to determine it, such as runs without the target, with a blank backing or with the beam off; contaminant reactions identified and their contribution estimated; backgrounds found to be negligible reported as such; for natural targets, the contributing isotopes and how the result was converted to an isotopic cross section stated.

**Benchmark.** [1], [2], [4], [6], [7]

## 7. Angular distributions and angle integration

**Question.** When a total cross section is derived from measurements at a few angles, how were the angular distribution and the integration over angle treated, and how much of the full angular range was measured?

**Why it matters.** Reaction products and prompt gamma rays are emitted anisotropically. Converting yields measured at a few angles into an angle-integrated cross section depends on assumptions about the angular distribution, and the correction for anisotropy can be as large as the quoted uncertainty. Reported uncertainties from Legendre-polynomial fits vary widely with angular coverage.

**Resolved by.** Differential cross sections reported at each measured angle, with the frame (laboratory or centre of mass) stated; the angular coverage and solid-angle corrections given; the Legendre order or other model used for integration justified, with its uncertainty included; any assumption of isotropy tested or its effect estimated.

**Benchmark.** [1], [3]

## 8. Comparison with evaluated data and earlier measurements

**Question.** When the results are compared with evaluated libraries or earlier measurements, are the library and version named, are the reference data on the same footing, is the energy resolution matched, and is the uncertainty given in enough detail, with its correlations, for the data to be renormalized and used in an evaluation?

**Why it matters.** Earlier measurements often have to be adjusted for revised standards, monitor cross sections and decay data before they can be compared, and published uncertainties are often incomplete. Systematic differences between measurement techniques for the same reaction can exceed the quoted uncertainties, so agreement or disagreement with one library or one earlier data set means little unless these are accounted for.

**Resolved by.** The evaluated library and version named; comparison data renormalized to the same standards and decay data, or the difference discussed; high-resolution data reduced to comparable resolution before comparison; the observable stated clearly; an uncertainty budget that separates correlated contributions, such as target areal density and normalization, from uncorrelated ones; numerical data provided in a form a data compilation can take up.

**Benchmark.** [1], [6], [7], [8], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. M. Lewis et al., Templates of expected measurement uncertainties for neutron-induced capture and charged-particle production cross section observables, EPJ Nuclear Sci. Technol. 9, 33 (2023); read as the published open-access PDF hosted at Rensselaer Polytechnic Institute | doi:10.1051/epjn/2023015 |
| 2 | C. Ananna et al., Recent results and future perspectives with solid targets at LUNA, Front. Astron. Space Sci. 10, 1325053 (2024) | doi:10.3389/fspas.2023.1325053 |
| 3 | E. G. Adelberger et al., Solar fusion cross sections II: the pp chain and CNO cycles, Rev. Mod. Phys. 83, 195 (2011); read as arXiv:1004.2318 | doi:10.1103/RevModPhys.83.195 |
| 4 | A. S. Voyles et al., Excitation functions for (p,x) reactions of niobium in the energy range of Ep = 40–90 MeV, Nucl. Instrum. Methods Phys. Res. B 429, 53 (2018); read as arXiv:1804.06548 | doi:10.1016/j.nimb.2018.05.028 |
| 5 | International Atomic Energy Agency (IAEA), International Evaluation of Neutron Cross-Section Standards, STI/PUB/1291 (IAEA, Vienna, 2007) | https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1291_web.pdf |
| 6 | A. Hermanne et al., Upgrade of IAEA recommended data of selected nuclear reactions for production of PET and SPECT isotopes, arXiv:2006.03125 (2020) | doi:10.48550/arXiv.2006.03125 |
| 7 | R. Capote et al., Unrecognized Sources of Uncertainties (USU) in Experimental Nuclear Data, Nucl. Data Sheets 163, 191 (2020); read as the accepted manuscript at OSTI (LA-UR-19-27617) | doi:10.1016/j.nds.2019.12.004 |
| 8 | D. Neudecker et al., Templates of expected measurement uncertainties, EPJ Nuclear Sci. Technol. 9, 35 (2023) | doi:10.1051/epjn/2023014 |
| 9 | D. A. Brown et al., ENDF/B-VIII.0: The 8th Major Release of the Nuclear Reaction Data Library with CIELO-project Cross Sections, New Standards and Thermal Scattering Data, Nucl. Data Sheets 148, 1 (2018); read as the published open-access PDF hosted at Rensselaer Polytechnic Institute | doi:10.1016/j.nds.2018.02.001 |
| 10 | International Atomic Energy Agency, Charged particle cross-section database for medical radioisotope production: diagnostic radioisotopes and monitor reactions, final report of a co-ordinated research project, IAEA-TECDOC-1211 (2001) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_1211_prn.pdf |
| 11 | C. Broggini et al., LUNA: Status and prospects, Prog. Part. Nucl. Phys. 98, 55 (2018); read as arXiv:1707.07952v4 | doi:10.1016/j.ppnp.2017.09.002 |
