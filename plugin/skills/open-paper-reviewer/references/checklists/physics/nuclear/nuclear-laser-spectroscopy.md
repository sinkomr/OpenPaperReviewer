---
id: T-NUCLEAR-LASER-SPECTROSCOPY
name: Laser spectroscopy of nuclei
type: technique
field: physics/nuclear
applies_when: the paper measures isotope shifts or hyperfine structure in atomic or ionic spectra, by collinear, resonance ionisation, trap or gas-cell laser spectroscopy, and derives nuclear spins, magnetic dipole or electric quadrupole moments, or changes in mean-square charge radii from them
version: "0.1"
---

# Laser spectroscopy of nuclei

Laser spectroscopy of nuclei uses the hyperfine structure (HFS) and isotope shift (IS) of atomic or ionic transitions to claim nuclear spins, magnetic dipole moments, spectroscopic electric quadrupole moments and changes in mean-square charge radii, δ⟨r²⟩, often along chains of radioactive isotopes. The nuclear quantities follow from fitted hyperfine constants A and B and line centroids only through atomic factors: the field-shift factor F and the mass-shift factor K, obtained by atomic calculation or by a King plot, which compares isotope shifts in two transitions, together with reference isotopes whose moments or radii are known from other methods such as nuclear magnetic resonance (NMR), muonic atoms or electron scattering.

## 1. Line-shape model and extracted centroids

**Question.** Which line-shape model was fitted to the hyperfine spectrum, were the relative peak intensities fixed or left free, and does the paper show that the centroid and the A and B values do not depend on laser power, on optical pumping or on how partially resolved components were treated?

**Why it matters.** Saturation broadens the lines, and optical pumping or other stimulated effects move the peak intensities away from the theoretical values, so a model with fixed intensities can pull the fitted line positions. Where components overlap within their widths, interference between them gives non-Lorentzian, polarisation-dependent shapes that can shift fitted centres, and in pulsed or optically pumped schemes the line shape also depends on laser timing and field conditions. A shift of the centroid passes directly into the isotope shift.

**Resolved by.** The fitted spectra shown with residuals; the line profile, the intensity treatment and the fit procedure stated; laser power, polarisation and timing given, with the result shown to be stable when they change; for partially resolved lines, a check of the centroid against alternative models or interference effects; where possible, mirrored or repeated scans showing the same centroid.

**Benchmark.** [1], [2], [3], [5]

## 2. Spin and state assignment

**Question.** How was each hyperfine structure attributed to a nuclear state, ground or isomeric, and how was its spin fixed in the fit: by counting resolved peaks, by the ratio of upper- to lower-state A constants, or by relative intensities; and are the fits with other candidate spins shown?

**Why it matters.** The spin is an input to the hyperfine fit, and a wrong spin, or peaks attributed to the wrong one of overlapping ground and isomeric structures, changes A, B, the centroid and every quantity derived from them. Counting peaks fixes the spin only when the spin is no larger than the electronic angular momentum J; for larger spins the pattern often allows only a lower limit. Peak intensities are distorted by laser power, so a spin taken from intensities alone is weak unless isotopes are compared under identical conditions.

**Resolved by.** Where an isomer may be present, the attribution of each peak to the ground or isomeric state supported by an independent handle, such as decay-tagged detection; the fit quality for each candidate spin reported; the upper- to lower-state A ratio compared with that of isotopes of known spin in the same transition; intensity comparisons made only between isotopes measured under the same conditions; the spin stated as an assignment or as a limit, matching what the data allow.

**Benchmark.** [1], [2]

## 3. Frequency scale and Doppler calibration

**Question.** How was the frequency axis calibrated: which laser frequency reference was used, and, for fast-beam work, how were the acceleration and scanning voltages measured; or, for gas-cell and hot-cavity work, how were pressure and environmental shifts handled?

**Why it matters.** In collinear spectroscopy the frequency seen by the ions depends on the beam velocity, so a relative error of 10⁻⁴ in the acceleration voltage can produce a spurious isotope shift that is large compared with the field shift in light elements. Such voltage errors behave much like a mass shift and can be partly absorbed by a King plot, but not for the lightest nuclei. In buffer-gas cells, collisions broaden and shift the lines, and drifts in laser frequency or voltage during a scan add to the error.

**Resolved by.** The voltage-measurement chain and its calibration stated, with the resulting isotope-shift uncertainty given; for light elements, a method that removes the dependence on voltage, such as collinear and anticollinear measurement with frequency-comb-referenced lasers; laser frequency referenced and logged throughout; reference-isotope scans interleaved to track drift; pressure shifts measured or bounded where gas cells are used.

**Benchmark.** [1], [3], [4]

## 4. Atomic factors and their uncertainty

**Question.** Where do the field-shift factor F and the specific mass-shift factor come from, what uncertainty is assigned to each, and is that uncertainty shown separately from the experimental uncertainty in δ⟨r²⟩?

**Why it matters.** The normal mass shift can be calculated exactly, but the specific mass shift must be calculated or calibrated, and in light elements the mass shift exceeds the field shift by orders of magnitude, so a small error in it dominates δ⟨r²⟩. Ab initio field-shift factors are typically quoted with uncertainties of about 15%. Because δ⟨r²⟩ is the field shift divided by F, an error in F rescales every δ⟨r²⟩ in the chain by the same factor.

**Resolved by.** The source of each atomic factor named, with method and uncertainty; for calculated factors, a comparison between transitions or with calibrated values; the experimental and atomic-factor uncertainties on δ⟨r²⟩ given separately; for light elements, mass-shift calculations of an accuracy matched to the size of the field shift.

**Benchmark.** [1], [2]

## 5. King-plot analysis

**Question.** If the atomic factors are calibrated by a King plot, which isotopes and independent radii or second transition were used, how many isotope pairs enter, and is linearity tested?

**Why it matters.** A King plot of modified isotope shifts, each multiplied by the inverse-mass factor, is linear at leading order, and a test of linearity needs at least three independent isotope pairs; with only two points the line always fits. The calibration is only as good as the independent radii it rests on, and higher-order effects, such as a field shift that depends on isotope mass, can make the plot non-linear. Systematic errors that behave like a mass shift, such as a voltage miscalibration, are partly absorbed into the fitted intercept.

**Resolved by.** The King plot shown with the isotopes, the modified isotope shifts and the reference radii or reference-transition data identified and sourced; the number of independent pairs stated; a linearity test with residuals; the fit method stated; the uncertainties of the fitted slope and intercept carried into δ⟨r²⟩.

**Benchmark.** [2], [4], [6]

## 6. From field shift to radii and deformation

**Question.** Does the paper state whether it reports the Seltzer moment λ or δ⟨r²⟩, how the higher radial moments were treated, which reference radius was used to convert to absolute charge radii, and which model links radii to deformation?

**Why it matters.** The field shift measures the Seltzer moment, which in heavier elements includes contributions from δ⟨r⁴⟩ and higher moments, and treating it as δ⟨r²⟩ needs a correction. Absolute radii add a reference radius from muonic atoms or electron scattering, whose uncertainty is common to the whole chain. Changes in δ⟨r²⟩ contain both static and dynamic deformation, so a deformation parameter read from them rests on a model.

**Resolved by.** The quantity reported named, with the correction from λ to δ⟨r²⟩ and its uncertainty; the reference isotope, its radius and the source of that radius given, with its uncertainty kept separate; any deformation inferred labelled with the model used and compared, where possible, with deformation measures from other observables.

**Benchmark.** [1], [2]

## 7. Magnetic moments from A constants

**Question.** Which reference isotope and reference moment were used to scale the A constants to magnetic moments, and how was the differential hyperfine anomaly handled?

**Why it matters.** Magnetic moments are usually obtained from the ratio of A constants to those of a reference isotope with a moment known from NMR or similar methods. That ratio equals the ratio of g-factors only for a point nucleus: the finite distribution of charge and magnetisation adds a differential hyperfine anomaly, usually of order 1% or less but up to about 10% in some cases, and it differs between atomic states because it enters through s and p1/2 electrons.

**Resolved by.** The reference isotope, its moment and the source of that moment given; the state whose A constant was used stated, preferring the more sensitive one; the hyperfine anomaly included as a correction or as an uncertainty of stated size, larger for heavy elements; agreement of moments derived from two atomic states shown, or a difference explained.

**Benchmark.** [1], [2], [7]

## 8. Quadrupole moments from B constants

**Question.** How was the electric field gradient obtained, from atomic calculation or from a reference isotope of known quadrupole moment, and what is the reference value and its uncertainty?

**Why it matters.** The B constant is the product of the spectroscopic quadrupole moment and the electric field gradient at the nucleus, so the moment is only as good as the calculated gradient or the reference moment; reference quadrupole moments are known at best to about 1%. Small B values, or B constants from states with little sensitivity, give large relative errors, and converting a spectroscopic moment into an intrinsic moment or a deformation assumes strong coupling and a radius parameter.

**Resolved by.** The reference quadrupole moment or the calculated gradient given with its source and uncertainty, and that uncertainty kept separate from the experimental one; the atomic state used stated, or values from two states combined with their correlation taken into account; any intrinsic moment or deformation labelled with the coupling model and parameters used.

**Benchmark.** [1], [2]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | P. Campbell, I. D. Moore and M. R. Pearson, Laser spectroscopy for nuclear structure physics, Prog. Part. Nucl. Phys. 86, 127–180 (2016); read as the accepted manuscript in the University of Jyväskylä repository | doi:10.1016/j.ppnp.2015.09.003 | full text | Sec. 2.2: moments usually scaled from A and B ratios to a reference isotope known from NMR; reference quadrupole moments known at best to about 1%; spin from zero-field splittings often only a lower limit when I > J. Sec. 2.2.1: Bohr-Weisskopf and Breit-Rosenthal anomalies, usually below 1% but near 10% in some cases. Sec. 2.3: normal mass shift exactly calculable, specific mass shift calculated or calibrated; mass shift dominates in light nuclei; field shift expressed through the Seltzer moment including higher radial moments; F calibrated with muonic, X-ray or electron-scattering radii or calculated, ab initio values typically cited as accurate to 15%. Sec. 2.5: intrinsic moment and deformation from Qs are model-dependent; δ⟨r²⟩ contains static and dynamic deformation. Sec. 3.1: theoretical hyperfine intensities hold without stimulated effects; saturation parameter enters the absorption profile. Sec. 3.4.1: voltage and laser-frequency calibration and drift limit relative frequencies, and for very light elements the voltage uncertainty exceeds the field shift. Sec. 3.7.1: buffer-gas pressure broadening and shift in gas cells |
| 2 | X. F. Yang, S. J. Wang, S. G. Wilkins and R. F. Garcia Ruiz, Laser spectroscopy for the study of exotic nuclei, Prog. Part. Nucl. Phys. 129, 104005 (2023); read as preprint arXiv:2209.15228 | doi:10.1016/j.ppnp.2022.104005 | full text | Sec. 2.1: moments from reference-isotope A and B with moments from NMR or NQR; otherwise field and field gradient must be calculated; hyperfine anomaly negligible in most light and medium nuclei but significant in heavy ones. Sec. 2.2: Seltzer moment as a series of radial moments; specific mass shift hard to calculate, King-plot calibration preferred. Sec. 2.3: spin is predefined in the fit; spin from peak count when I ≤ J, from constant upper- to lower-state A ratio, or from intensities, which laser power distorts so isotopes are compared under identical conditions; moments from the more sensitive state or a correlated average; absolute radius uses a reference radius from electron scattering or muonic data; calculation is the only route when fewer than three stable isotopes, or none with known radii, are available. Sec. 3.2.4: King-plot non-linearity signals extra terms, such as higher-order nuclear effects. Sec. 4.1.2: in collinear resonance ionisation, the relative timing of the laser pulses can strongly affect linewidth and line shape. Sec. 4.2.2: decay-assisted detection separates the hyperfine structures of ground and isomeric states even where they largely overlap |
| 3 | R. Neugart, J. Billowes, M. L. Bissell, K. Blaum, B. Cheal, K. T. Flanagan, G. Neyens, W. Nörtershäuser and D. T. Yordanov, Collinear laser spectroscopy at ISOLDE: new methods and highlights, J. Phys. G 44, 064002 (2017); read as the accepted manuscript in the University of Liverpool repository | doi:10.1088/1361-6471/aa6642 | full text | Sec. 3.1.1: complicated line shapes from optical pumping in a magnetic field varying along the beam were of limited use for accurate isotope shifts; restricting the resonance to a well-defined low-field region and simulating the line shape addressed this. Sec. 3.1.2: a 10⁻⁴ voltage uncertainty gives about 15 MHz in a light-element isotope shift against a field shift of about 5 MHz; combined collinear and anticollinear measurement with frequency-comb lasers removes the voltage dependence, and mirror-image spectra make line-shape modelling errors shift centres in opposite directions |
| 4 | A. Krieger, Ch. Geppert, R. Catherall, F. Hochschulz, J. Krämer, R. Neugart, S. Rosendahl, J. Schipper, E. Siesling, Ch. Weinheimer, D. T. Yordanov and W. Nörtershäuser, Calibration of the ISOLDE acceleration voltage using a high-precision voltage divider and applying collinear fast beam laser spectroscopy, Nucl. Instrum. Methods Phys. Res. A 632, 23–31 (2011); read as preprint arXiv:1101.2536 | doi:10.1016/j.nima.2010.12.145 | full text | Sec. 1: 10⁻⁴ voltage accuracy suffices for medium and heavy nuclei but not for the lightest elements. Sec. 2 with Table 1: spurious isotope shift from a 10⁻⁴ voltage error compared with the accuracy needed for charge radii; the voltage error behaves largely like a mass shift, so a King plot with known radii partly absorbs it, though not for the lightest nuclei |
| 5 | R. C. Brown, S. Wu, J. V. Porto, C. J. Sansonetti, C. E. Simien, S. M. Brewer, J. N. Tan and J. D. Gillaspy, Quantum interference and light polarization effects in unresolvable atomic lines: application to a precise measurement of the 6,7Li D2 lines, Phys. Rev. A 87, 032504 (2013) | doi:10.1103/PhysRevA.87.032504 | abstract | Abstract: interference between excited states split by about a natural linewidth gives non-Lorentzian, polarisation-dependent line shapes; ignoring it shifted line centres by up to about 1 MHz, and the corrected line shape gave an improved difference in mean-square charge radii |
| 6 | J. C. Berengut, D. Budker, C. Delaunay, V. V. Flambaum, C. Frugiuele, E. Fuchs, C. Grojean, R. Harnik, R. Ozeri, G. Perez and Y. Soreq, Probing new long-range interactions by isotope shift spectroscopy, Phys. Rev. Lett. 120, 091801 (2018); read as preprint arXiv:1704.05068, which carries a different title | doi:10.1103/PhysRevLett.120.091801 | full text | Eq. 3 and following text: modified isotope shifts of two transitions lie on a straight line at leading order whatever the electronic factors; testing linearity needs at least three independent isotope pairs. Later text: some non-linearity is expected from higher-order Standard Model effects, such as a mass-dependent field shift, not yet understood quantitatively for many-electron atoms |
| 7 | J. R. Persson, Table of hyperfine anomaly in atomic systems, At. Data Nucl. Data Tables 99, 62–68 (2013); read as preprint arXiv:1110.5991 | doi:10.1016/j.adt.2012.04.002 | full text | Sec. 1: the ratio of A constants equals the g-factor ratio only up to the differential Bohr-Weisskopf and Breit-Rosenthal anomaly; extracting it needs A and g known to 10⁻⁴. Sec. 2: the anomaly is state-dependent, normally about 1% and up to 10%, and arises from the contact interaction of s and p1/2 electrons |
