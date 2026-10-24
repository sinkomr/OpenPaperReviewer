---
id: T-ION-BEAM-ANALYSIS
name: Ion-beam analysis
type: technique
field: physics/nuclear
applies_when: the paper uses Rutherford or elastic backscattering, particle-induced X-ray emission, nuclear reaction analysis, elastic recoil detection or ion channelling to claim a composition, areal density, film thickness, depth profile, hydrogen content, crystal damage or impurity lattice site
version: "0.1"
---

# Ion-beam analysis

Ion-beam analysis uses beams of light or heavy ions, usually of a few MeV, to claim the elemental composition, areal density and depth profile of the near-surface region of a sample and, through channelling along crystal axes, its crystal damage and the lattice sites of impurities. The main methods are Rutherford and elastic backscattering spectrometry (RBS, EBS), particle-induced X-ray emission (PIXE), nuclear reaction analysis (NRA) and elastic recoil detection analysis (ERDA), and each turns counts and energies into amounts and depths through stopping powers, cross sections and a model of the sample.

## 1. Stopping powers and the depth scale

**Question.** Which stopping-power tables or code, and which rule for compounds, convert energy loss into depth, are amounts reported as areal density (atoms per unit area) with the density used for any linear thickness stated, and is the uncertainty of the stopping powers carried into the depths and thicknesses?

**Why it matters.** The conversion of energy to depth in RBS, ERDA and NRA profiles is only as good as the stopping powers used. Many ion-target combinations have one measured data set or none, a widely used semi-empirical code departs from recent measurements by about ten per cent on average, the additive rule for compounds is unreliable for slow ions, and the heavy-ion stopping that ERDA relies on is less well known than helium stopping. A thickness in nanometres also rests on an assumed density, because the measured quantity is atoms per unit area.

**Resolved by.** The tables or code and version named, with the rule used for compounds; an uncertainty assigned to the stopping powers that suits the ion, target and energy range, not taken as exact; results given as areal densities, with the density used for any conversion to thickness stated and justified; for ERDA, the stopping of each recoil species in the sample and in any absorber foil treated with its own uncertainty; where accuracy matters, a check against an independent thickness or a certified reference sample.

**Benchmark.** [1], [2], [3]

## 2. Cross sections

**Question.** For each element quantified, does the paper state whether the cross section used is the Rutherford value (with a screening correction where needed), an evaluated or measured non-Rutherford elastic cross section, or a nuclear reaction cross section, give its source and uncertainty, and show that the beam energy and detection angle lie in the range where that cross section holds?

**Why it matters.** The Rutherford formula fails for light elements above about 2.4 MeV for helium and above a few hundred keV for protons, where nuclear resonances can change the cross section by orders of magnitude, and electron screening lowers it by a few per cent for heavy elements at low energy. A concentration is only as well known as its cross section, and unevaluated non-Rutherford and reaction cross sections from the literature disagree beyond their stated errors. NRA cross sections vary irregularly with energy and element, so most NRA results rest on comparison with a standard.

**Resolved by.** The cross-section source named for each element and reaction, with its uncertainty; for non-Rutherford scattering, data that have been evaluated or validated on a thick sample of known composition, or a check on such a sample in the same set-up; for NRA, a standard of known content measured under the same conditions; the screening correction applied for heavy elements at low beam energy.

**Benchmark.** [1], [4], [5]

## 3. Absolute normalisation and detector response

**Question.** How was the product of collected charge and detector solid angle determined (charge integration with secondary-electron suppression, a reference sample or an internal standard), how were the beam energy and the energy calibration of the detector established, including its pulse-height defect, and were pile-up and dead time corrected?

**Why it matters.** Absolute amounts scale with the product of charge and solid angle, which is hard to determine accurately, and ordinary charge integration is good to only about 5 to 10 per cent, depending on the neutral fraction of the beam and on how well secondary electrons are suppressed. A gain that ignores the pulse-height defect, or a beam energy read from an uncalibrated terminal voltmeter, shifts energies and therefore depths. Pulse pile-up distorts the spectrum, increasingly so at high count rates, and uncorrected dead time loses counts.

**Resolved by.** The method for the charge-solid-angle product stated with its uncertainty, preferably checked against a certified reference or internal standard measured in the same run; the energy calibration points and a check of the beam energy, such as a known nuclear resonance, given; the pulse-height defect included where heavy elements or heavy ions are detected; pile-up modelled or rejected, dead time or live time corrected, and count rates stated; an uncertainty budget that lists these terms alongside the stopping powers.

**Benchmark.** [3], [4]

## 4. Uniqueness of the fitted sample model

**Question.** When a depth profile or layer structure comes from fitting a layered model to the spectra, does the paper name the code, show measured and fitted spectra, state which parameters were fixed, and show that the solution is unique, for example by fitting spectra from several geometries, beams or techniques to one sample model?

**Why it matters.** A single spectrum can often be fitted equally well by different profiles: RBS cannot separate elements of similar mass, and broadening from roughness, beam-induced mixing or sputtering looks like interdiffusion. Several independent spectra may be needed to fix several sample parameters. Fitting them together removes much of the ambiguity, but the choice of objective function and of the weights given to each data set can itself bias the result.

**Resolved by.** The code and version named; measured and fitted spectra shown for each data set; constrained or fixed parameters listed with the reason; for claims about interfaces, layer order or composition gradients, two or more geometries, beam energies or techniques fitted to a single sample model; roughness and interdiffusion distinguished by an independent measurement such as microscopy, or by a second geometry; the weighting of data sets in any combined fit stated.

**Benchmark.** [1], [6], [7], [8]

## 5. Beam-induced changes during the measurement

**Question.** What fluence, current density and beam spot did each analysed area receive, and does the paper show that the reported quantities did not change during the measurement, for example by splitting the data into fluence intervals from the same spot?

**Why it matters.** The analysing beam deposits far more energy than it returns as signal, and it can drive out hydrogen and other volatile elements, sputter away thin surface layers, mix interfaces, heat or melt the sample, add defects to radiation-sensitive crystals and deposit carbon cracked from the residual gas. Such changes are often invisible in a single spectrum, so a good fit to data from an altered sample can still give the wrong answer.

**Resolved by.** Fluence, current, beam spot size and sample temperature stated; yields shown as a function of fluence on the same spot, with stable values or an extrapolation to zero fluence, especially for hydrogen, thin films and channelling measurements; fresh spots, larger or scanned beams, cooling or reduced dose used for sensitive materials; any carbon build-up at the surface considered in the fit.

**Benchmark.** [8], [9]

## 6. Channelling and crystal orientation

**Question.** For claims of crystal quality, damage profiles or impurity lattice sites from channelling, how was the random spectrum obtained, how were dechannelling and the depth scale for channelled ions treated, and along how many crystal axes were the impurity and host signals measured? For composition measured on crystalline samples, was unintended channelling avoided?

**Why it matters.** The defect fraction taken from the aligned yield depends directly on the random spectrum, which is wrong if it is taken too close to an axis or includes partial planar channelling. The yield behind a damaged layer contains ions dechannelled by that layer, which must be subtracted, and channelled ions lose energy more slowly, which changes the depth scale. One axis shows only displacements perpendicular to that axis, so a lattice site needs several axes, and mosaic spread blurs the channelling and makes different axes give inconsistent fractions.

**Resolved by.** The random spectrum measured several degrees off axis with the sample rotating; the host minimum yield stated; dechannelling subtracted with a stated model or a Monte Carlo simulation; a reduced stopping power used for the channelled depth scale; angular scans across at least two axes for any lattice-site claim, giving consistent fractions; mosaic spread measured, for example by X-ray diffraction, and included; for composition, the sample tilted and rotated or made amorphous to avoid channelling.

**Benchmark.** [3], [9]

## 7. PIXE quantification

**Question.** For PIXE concentrations, does the paper state whether the sample was treated as thin or thick, which matrix composition was assumed for X-ray attenuation and secondary fluorescence, how the detector efficiency and absorber transmission were established, and which reference materials of similar matrix validated the result?

**Why it matters.** In a thick sample X-rays are produced at a range of depths and beam energies and are attenuated on the way out, so the yield of each element depends on the others and the calculation must be iterated over an assumed matrix composition, which includes light elements that PIXE does not detect. The low-energy efficiency of an X-ray detector cannot be measured with radioactive sources, and absorber transmission often differs from that calculated from the nominal thickness; a one-degree tilt or a one-millimetre shift of distance changes light-element intensities by a few per cent. At high count rates pile-up adds sum peaks and a continuum.

**Resolved by.** The thin or thick treatment stated, with sample thickness, homogeneity and surface condition; the assumed matrix, including undetected light elements, stated and iterated; the code and its database named; detector efficiency and absorber transmission calibrated with thin or thick standards; certified reference materials of similar matrix analysed in the same conditions, with the agreement shown; count rates and pile-up treatment given.

**Benchmark.** [1], [4]

## 8. Depth resolution and multiple scattering

**Question.** Is the depth resolution stated at the depths where interface widths, thin layers or near-surface features are claimed, with the contributions of detector resolution, beam energy spread, energy straggling, multiple scattering and the spread of angles from the beam spot and detector aperture, and are counts below the signal of a heavy layer attributed to material only after plural scattering has been considered?

**Why it matters.** The depth resolution of a backscattering, recoil or reaction spectrum is set by all of these contributions together, so it differs from one depth and geometry to another. Glancing geometries improve resolution near the surface, but the spread of exit angles across the detector smears features deeper in the sample. A width close to the resolution cannot be told apart from a sharp interface, and plural scattering puts counts below the signal of a heavy layer that a single-scattering model can read as diffusion or extra material.

**Resolved by.** The depth resolution at the relevant depths calculated with a named code or model and compared with each claimed width or thickness; incidence and exit angles, beam spot size and detector aperture given; straggling, multiple scattering and plural scattering included in the simulation where heavy layers, thick samples or glancing geometries are involved; widths that do not exceed the resolution reported as upper limits.

**Benchmark.** [4], [5]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | J. A. Cookson and T. W. Conlon, MeV ion-beam analysis, J. Res. Natl. Bur. Stand. 93, 473–479 (1988); read as the public-domain copy in PubMed Central (PMC5181966) | doi:10.6028/jres.093.123 | full text | Sec. 2.2: RBS measures one parameter and cannot resolve elements of similar mass. Sec. 4 (Improved quantification): thick-target PIXE needs iteration because each element's yield depends on the others, X-ray attenuation coefficients are the main uncertainty and secondary fluorescence adds a term; H, C, N and O are not measured by PIXE, and in biological matrices, where attenuation is mild, their assumed amounts affect results for elements above Z = 18 very little; RBS cross sections good to 1% with a screening correction except for the lightest nuclei; helium stopping known to about 5%, with Bragg-rule deviations of a few per cent at low energy; in ERDA heavy-ion stopping, known to about 10%, is the main uncertainty and recoils also cross an absorber foil and a dead layer; NRA cross sections vary irregularly, so most NRA relies on standards |
| 2 | C. C. Montanari, P. Dimitriou, L. Marian, A. M. P. Mendez, J. P. Peralta and F. Bivort-Haiek, The IAEA electronic stopping power database: modernization, review, and analysis of the existing experimental data, Nucl. Instrum. Methods B 551, 165336 (2024); read as preprint arXiv:2402.03080 | doi:10.1016/j.nimb.2024.165336 | full text | Sec. 1: about 60% of the 1526 systems in the database have a single data set and under 30% are reasonably well known; SRIM-2013 departs from data published after 2013 by 11.4% on average; the Bragg rule for compounds is unreliable at low ion velocity, and data for slow heavy ions are scarce |
| 3 | C. Jeynes, N. P. Barradas and E. Szilágyi, Accurate determination of quantity of material in thin films by Rutherford backscattering spectrometry, Anal. Chem. 84, 6061–6069 (2012); read as the submitted manuscript hosted by the University of Surrey | doi:10.1021/ac300904c | full text | Abstract: accuracy dominated by electronic stopping, with the detector gain needing special care. Introduction: uncertainty budgets not widely used in ion-beam analysis. "Traceability of RBS" sections: yield depends on the cross section and the charge-solid-angle product, which is notoriously hard to determine accurately and normally fixed against a standard; results come in atoms per area, equal to thickness only through the density; the sample was amorphised to exclude channelling; beam energy from a terminal voltmeter has limited precision and is checked with the 3038 keV oxygen resonance; the pulse-height defect must be included; pile-up and the lower-level discriminator distort the spectrum |
| 4 | International Atomic Energy Agency, Instrumentation for PIXE and RBS, IAEA-TECDOC-1190 (2000) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_1190_prn.pdf | full text | Sec. 3.2: standardless PIXE needs the charge, filter transmission, detector efficiency and the sample's matrix, thickness and surface morphology. Sec. 3.2.5, Table IV: a 1° tilt or 1 mm distance change alters K X-ray intensities by up to about 4%. Sec. 3.3.3: pile-up gives sum peaks and a continuum above about 1000 counts per second. Sec. 3.3.5: low-energy detector efficiency cannot be measured with radioactive sources and is checked with element standards. Sec. 3.3.6: filter thickness tuned with reference materials because nominal thickness does not match modelled attenuation. Sec. 3.4.1: ADC dead time requires a live-time correction. Sec. 3.5: codes correct for secondary fluorescence and self-absorption. Sec. 4.3.2: glancing incidence improves near-surface depth resolution about tenfold, while at large tilt the spread of exit angles smears deeper features. Sec. 4.6.1: depth-resolution calculations include beam energy spread, geometric spread from beam spot and detector solid angle, straggling, multiple scattering and absorber foils; plural scattering produces background below the signal of high-Z layers. Sec. 4.6.2: charge integration precise to 5-10%, depending on the neutral fraction of the beam and on secondary-electron suppression; Rutherford valid for helium up to about 2.4 MeV and protons up to about 0.7 MeV on light elements, with resonances raising cross sections by two to three orders of magnitude; screening lowers the cross section by 3.5% for 1 MeV helium on bismuth |
| 5 | International Atomic Energy Agency, Development of a Reference Database for Ion Beam Analysis: Report of a Coordinated Research Project on Reference Database for Ion Beam Analysis, IAEA-TECDOC-1780 (2015) | https://www-pub.iaea.org/MTCD/Publications/PDF/TE-1780_web.pdf | full text | Foreword: unevaluated non-Rutherford and reaction cross sections showed discrepancies beyond the authors' stated errors. Sec. 1: a concentration can only be determined as well as its cross section is known; measured cross sections were normalised to Rutherford scattering; cross sections are validated by benchmark spectra from thick samples of known composition, and a failed benchmark may also point to stopping powers, straggling, or multiple and plural scattering |
| 6 | T. F. Silva, C. L. Rodrigues, N. Added, M. A. Rizzutto, M. H. Tabacniks, T. Höschen, U. von Toussaint and M. Mayer, Self-consistent ion beam analysis: an approach by multi-objective optimization, Nucl. Instrum. Methods B 506, 32–40 (2021); read as preprint arXiv:2108.01498 | doi:10.1016/j.nimb.2021.09.007 | full text | Abstract and Sec. 1: self-consistent analysis of several measurements reduces ambiguity; a single RBS spectrum can admit degenerate solutions, and up to N-1 independent spectra may be needed to fix N sample parameters; the combined analysis inherits the accuracy of its most accurate component |
| 7 | T. F. Silva, C. L. Rodrigues, M. H. Tabacniks, U. von Toussaint and M. Mayer, Bias and synergy in the self-consistent approach of data analysis of ion beam techniques, Nucl. Instrum. Methods B 533, 9–16 (2022); read as preprint arXiv:2111.13298 | doi:10.1016/j.nimb.2022.10.008 | full text | Abstract and Sec. 1: combining measurements resolves ambiguities and improves depth resolution; the choice of objective function and of weights in a combined fit introduces a systematic error that shrinks with better statistics; some combinations of measurements constrain the solution better than others |
| 8 | D. Benzeggouta and I. Vickridge (eds), with N. P. Barradas, M. Döbeli, C. Jeynes and A. Vantomme, Handbook on Best Practice for Minimising Beam Induced Damage during IBA, SPIRIT project, version 1.0 dated March 2011, posted as arXiv:1303.3171 (2013) | doi:10.48550/arXiv.1303.3171 | full text | Introduction (pp. 1-2): the beam deposits vastly more energy than it yields as information; damage visible in the measurement includes crystal damage during channelling, sputtering and element loss, and other damage is not visible; carbon is deposited from cracked residual gas. Sec. 1.1 (p. 9): a thin gold layer can be sputtered away within about 200 counts. Metals section (pp. 19-21): films can melt under the beam; data split into time intervals allow extrapolation to zero fluence. Semiconductors section (p. 24): repeated channelling runs raised the minimum yield of germanium each time. Polymers section (p. 28): 10% hydrogen loss during ERD of Kapton at about 3×10^14 ions/cm². "Maximum Data Extraction" (pp. 34-35): hydrogen loss revealed by fluence-resolved ERDA spectra; sputtering mimics roughness and beam mixing can be taken as pre-existing; a perfect fit can hide damage |
| 9 | A. Vantomme, 50 years of ion channeling in materials science, Nucl. Instrum. Methods B 371, 12–26 (2016); read as the open-access copy in the KU Leuven repository | doi:10.1016/j.nimb.2015.11.035 | full text | Sec. 3.2: dechannelling must be subtracted (two-beam model) to obtain the defect density; the defect fraction depends on the quality of the random spectrum, ideally taken 5-7° off axis with azimuthal rotation; a reduced electronic stopping is needed for the depth scale, and these pitfalls are often overlooked; the extended irradiation of channelling creates defects, raising the germanium minimum yield after each run. Sec. 3.5: one axis gives only displacements perpendicular to it, so lattice sites need at least two axes. Sec. 3.6: mosaic spread broadens angular scans and gives inconsistent substitutional fractions across axes unless the measured tilt and twist are modelled |
