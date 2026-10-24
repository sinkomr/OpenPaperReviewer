---
id: T-CROSS-SECTIONS
name: Nuclear cross-section measurements
type: technique
field: physics/nuclear
applies_when: the paper reports a measured nuclear reaction cross section, excitation function, reaction yield, astrophysical S-factor, angular distribution or activation result from neutron or charged-particle beams, or compares such data with evaluated nuclear data libraries
version: "0.1"
---

# Nuclear cross-section measurements

Cross-section measurements are used to claim how probable a nuclear reaction is as a function of energy and angle, and to confirm, correct or extend evaluated nuclear data libraries. The cross section is never measured directly: it is inferred from a count of reaction products divided by the number of target nuclei per unit area, the number of beam particles (the fluence) and the detection efficiency, each of which is a separate measurement.

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

**Resolved by.** The fluence method stated; for monitor reactions or standards, the reaction, the source and version of the reference cross section and its uncertainty; the monitor foils or flux detector characterized with the same care as the main target; where several monitors are used, agreement between them shown; the normalization uncertainty reported separately from point-to-point uncertainties.

**Benchmark.** [1], [4], [5], [6]

## 4. Beam energy, energy loss and resolution

**Question.** How was the incident energy calibrated, how was the effective reaction energy inside the target obtained from the energy loss in it, and what energy spread is assigned to each data point?

**Why it matters.** The beam loses energy as it crosses the target and any degraders, so the effective energy depends on stopping powers, target thickness and composition. Stopping-power errors have shifted low-energy cross sections by several per cent or more, energy straggling broadens the beam progressively through a stack of foils, and an energy-scale error near a resonance or a steep threshold produces large errors in the cross section.

**Resolved by.** The beam-energy calibration and its uncertainty stated; the stopping-power tables or transport code named, with an uncertainty assigned to the computed energy loss; for stacked foils, energies checked against monitor reactions and not only computed; the energy spread or resolution function given for each point; for time-of-flight measurements, the flight path, time binning and any overlap of slow neutrons from earlier pulses described.

**Benchmark.** [1], [3], [4], [6]

## 5. Detection efficiency and decay data

**Question.** How was the efficiency of the detection system determined, including solid angle, thresholds and particle-identification cuts, dead time and, for gamma-ray counting, coincidence summing, and which decay data were used to convert activities into numbers of product nuclei, separating direct production from decay feeding?

**Why it matters.** The efficiency enters the cross section as a direct factor. Close counting geometry raises the count rate but brings in true coincidence summing, which can be corrected only if the decay cascade is well known; thresholds and event-selection cuts can reject real events, as when two reaction products travel together and fail the selection, and thick samples can stop the products before they reach the detector. Outdated half-lives or gamma-ray intensities bias activation results, and a product also fed by the decay of a precursor gives a cumulative cross section, not an independent one.

**Resolved by.** The efficiency calibration sources and method stated, with simulations used only to interpolate between measured points or validated against them; summing corrections given, or shown to be negligible by counting at more than one distance; the effect of thresholds and cuts on the efficiency estimated; dead-time corrections stated; the half-lives and emission probabilities used, with their sources; for activation, each cross section labelled as independent or cumulative, with precursor feeding subtracted where an independent value is claimed.

**Benchmark.** [1], [4], [6], [7]

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | A. M. Lewis et al., Templates of expected measurement uncertainties for neutron-induced capture and charged-particle production cross section observables, EPJ Nuclear Sci. Technol. 9, 33 (2023); read as the published open-access PDF hosted at Rensselaer Polytechnic Institute | doi:10.1051/epjn/2023015 | full text | Sec. 2.1: sample non-uniformity, overfilled and underfilled samples and the beam interception factor; efficiency includes thresholds and cuts; background categories and sample-out runs; flux by monitor, fission chamber or associated particle, with reference cross sections from evaluated libraries and decay data from ENSDF. Sec. 2.2.4: thick samples stop products; identification thresholds. Sec. 2.3.1: calibration sources, coincidence summing in close geometry, checked by counting at different distances. Sec. 3.3: report sample composition and corrections, energy resolution and wrap-around, efficiency, dead-time and summing corrections, all backgrounds, flux method; keep the observable clear. Secs. 4.2.1 and 4.2.2: powder samples affected by air pockets and water; areal-density uncertainty fully correlated across energies; enrichment uncertainty. Sec. 4.5.2: Legendre angle integration depends on assumed distributions and coverage, with reported uncertainties from 0.2% to 15%. Sec. 4.5.3: reference-data uncertainties |
| 2 | C. Ananna, L. Barbieri, A. Boeltzig, M. Campostrini, F. Casaburo, G. F. Ciani et al., Recent results and future perspectives with solid targets at LUNA, Front. Astron. Space Sci. 10, 1325053 (2024) | doi:10.3389/fspas.2023.1325053 | full text | Sec. 2: target thickness and stoichiometry from narrow-resonance scans and gamma-ray line shapes, cross-checked by elastic recoil detection or backscattering; degradation monitored under beam; light-element impurities in backings and cleaning of backings; cold trap against carbon build-up. Secs. 3 to 5: yield losses under beam tracked by gamma-ray line shapes, repeated resonance scans or yields at fixed energy; hygroscopic targets. Sec. 6.1: fluorine in tantalum backings gives a gamma line close to the line of interest |
| 3 | E. G. Adelberger, A. B. Balantekin, D. Bemmerer et al., Solar fusion cross sections II: the pp chain and CNO cycles, Rev. Mod. Phys. 83, 195–245 (2011); read as arXiv:1004.2318 | doi:10.1103/RevModPhys.83.195 | full text | Sec. IV.A: early low-energy data may be about 15% too high because of incorrect stopping powers. Sec. VI.A: prompt gamma-ray yields are anisotropic, the anisotropy corrections can be as large as the quoted uncertainty, and activation and prompt results differ systematically. Sec. IX.A.1: beam-target overlap and tails of target and beam profiles; atom number from target activity. Sec. IX.A.3: energy averaging depends on target profile, composition and carbon build-up; sputtering losses. Sec. IX.D: data close to a resonance excluded to limit energy-averaging errors; an extra target-damage error added to some points |
| 4 | A. S. Voyles, L. A. Bernstein, E. R. Birnbaum, J. W. Engle, S. A. Graves, T. Kawano, A. M. Lewis and F. M. Nortier, Excitation functions for (p,x) reactions of niobium in the energy range of Ep = 40–90 MeV, Nucl. Instrum. Methods Phys. Res. B 429, 53–74 (2018); read as arXiv:1804.06548 | doi:10.1016/j.nimb.2018.05.028 | full text | Abstract: contamination from adhesive in tape around monitor foils added activity, noted as a caution for stacked-target work. Sec. 2.2: cumulative cross sections reported where decay feeding from precursors cannot be separated, independent ones otherwise. Sec. 2.3: monitor foils used alongside direct current measurement as more sensitive beam monitors; fluence uncertainty includes activity, foil areal density, half-life and monitor cross section. Sec. 2.4: straggling broadens the energy distribution towards the rear of the stack; disagreement between monitors points to stopping-power or areal-density errors, corrected by variance minimization |
| 5 | International Atomic Energy Agency (IAEA), International Evaluation of Neutron Cross-Section Standards, STI/PUB/1291 (IAEA, Vienna, 2007) | https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1291_web.pdf | full text | Foreword: few cross sections can be determined absolutely, and most are normalized by measuring them relative to the standards. Sec. 1.1: a measurement made relative to a standard can be no more accurate than the standard's uncertainty allows, and improving a standard improves every measurement made relative to it |
| 6 | A. Hermanne, F. T. Tárkányi, A. V. Ignatyuk, S. Takács and R. Capote, Upgrade of IAEA recommended data of selected nuclear reactions for production of PET and SPECT isotopes, arXiv:2006.03125 (2020) | doi:10.48550/arXiv.2006.03125 | full text | Sec. I: published data sets corrected for outdated monitor cross sections and decay data before selection; abstract: comparison with a model-based library. Sec. II introduction: natural-target data converted to isotopic cross sections. Reaction subsections: data sets scaled for revised monitor values and gamma intensities, shifted in energy, or rejected for energy-scale problems, poor resolution, outdated monitors or summed contributions |
| 7 | R. Capote et al., Unrecognized Sources of Uncertainties (USU) in Experimental Nuclear Data, Nucl. Data Sheets 163, 191–227 (2020); read as the accepted manuscript at OSTI (LA-UR-19-27617) | doi:10.1016/j.nds.2019.12.004 | full text | Sec. III.B: raw data usually need adjusting to contemporary standards and decay data, and reported uncertainties are often incomplete. Sec. IV.C: comparing different techniques for the same quantity can reveal bias. Sec. V.E.1: early 235U fission cross sections were too high, plausibly because scattered-neutron background was underestimated. Sec. V.E.2: events rejected when both reaction products travel in nearly the same direction lowered measured cross sections. Sec. V.E.3: water in a sample affected capture data. Sec. V.E.4: time-of-flight and accelerator mass spectrometry capture data differ systematically |
| 8 | D. Neudecker, A. M. Lewis, E. F. Matthews, J. Vanhoy, R. C. Haight, D. L. Smith et al., Templates of expected measurement uncertainties, EPJ Nuclear Sci. Technol. 9, 35 (2023) | doi:10.1051/epjn/2023014 | abstract | Abstract (HZDR repository record): templates list the uncertainty sources expected for each measurement type, with typical values and correlations, to help experimenters give more complete uncertainty information and evaluators estimate missing uncertainties |
| 9 | D. A. Brown et al., ENDF/B-VIII.0: The 8th Major Release of the Nuclear Reaction Data Library with CIELO-project Cross Sections, New Standards and Thermal Scattering Data, Nucl. Data Sheets 148, 1–142 (2018); read as the published open-access PDF hosted at Rensselaer Polytechnic Institute | doi:10.1016/j.nds.2018.02.001 | full text | Sec. III.B.1: higher-resolution 56Fe inelastic data and newer lower-resolution data were binned on a common energy mesh before the former were rescaled to agree on average with the latter; the evaluated elastic cross section was resolution-broadened before its consistency with measured data was checked. Sec. III.C.4: above the resolved resonance range the recommended 197Au capture cross sections are bin averages up to 20 keV, and the resonance evaluation was tuned to agree with those bin averages |
