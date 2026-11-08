---
id: T-X-RAY-ABSORPTION
name: X-ray absorption spectroscopy and magnetic dichroism
type: technique
field: physics/condensed-matter
applies_when: the paper reports X-ray absorption spectra (XAS, XANES, NEXAFS or EXAFS) or X-ray magnetic circular or linear dichroism, or bases a claim about oxidation state, coordination, bond lengths, element-specific spin or orbital moments, magnetic order or spin orientation on them
version: "0.1"
---

# X-ray absorption spectroscopy and magnetic dichroism

## 1. Detection mode and probing depth

**Question.** Which detection mode (transmission, electron yield or fluorescence yield) was used for each spectrum, what depth does it probe, and is the probed region representative of the material the claim is about?

**Why it matters.** Electron yield comes from roughly the top 10 nm, where stoichiometry, valence, hybridisation and magnetic anisotropy can differ from the bulk, and where capping layers, contamination and charging act on the signal. Fluorescence and transmission probe much deeper, so a claim about the bulk, or about a buried interface, depends on which signal was recorded.

**Resolved by.** The detection mode named for each data set; the surface preparation (in situ cleaving or cleaning) or capping layer described, with evidence that a cap does not alter the layer beneath; for poorly conducting samples, a check for charging, such as the time response of the signal or the L3 to L2 intensity ratio; where surface and bulk could differ, a comparison with a more bulk-sensitive mode.

**Benchmark.** [1], [2]

## 2. Transmission samples and beam quality

**Question.** For transmission data, does the paper state the sample thickness (edge step and total absorption) and show that the sample was uniform and free of pinholes, and does it say how harmonics were rejected and detector linearity ensured?

**Why it matters.** Absorption is the logarithm of an intensity ratio, so pinholes, thickness variations and grains larger than an absorption length let a disproportionate share of the beam through and distort the edge step and the oscillations, with no reliable correction afterwards. Harmonics in the beam and non-linear detectors stop intensity fluctuations from cancelling and produce glitches and distortions that can be mistaken for spectral features.

**Resolved by.** Edge step and total absorption stated; a preparation that gives uniform thickness, such as fine sieved powder in stacked layers or a continuous film, described; harmonic rejection by mirror or monochromator detuning stated; detector settings and dark-current subtraction described; any glitch that survives normalisation identified as such and not interpreted.

**Benchmark.** [1], [2], [3]

## 3. Self-absorption, saturation and deadtime

**Question.** For fluorescence or electron-yield data on concentrated or thick samples, or at grazing incidence, does the paper estimate self-absorption or saturation and correct for it, and does it describe the deadtime correction of fluorescence detectors?

**Why it matters.** When the element of interest dominates the absorption, the fluorescence signal no longer follows the absorption coefficient: white lines and EXAFS amplitudes are damped, the distortion depends on geometry, and coordination numbers, white-line intensities and branching ratios are biased. In electron yield at grazing incidence the signal saturates, which can change orbital moments from the sum rules by more than 100 per cent and hole counts and spin moments by 10 to 20 per cent. In the soft X-ray range the fluorescence decay itself depends on the excited state, so fluorescence yield is not strictly proportional to absorption.

**Resolved by.** Concentration, thickness and incidence and exit angles given; a self-absorption correction with the composition used, or data at two geometries that agree after correction; saturation corrections for electron yield as a function of thickness and angle; deadtime correction described; for quantitative soft X-ray work, a signal shown to follow the absorption, such as transmission or inverse partial fluorescence yield.

**Benchmark.** [1], [2], [3], [4], [5]

## 4. Energy calibration, normalisation and edge positions

**Question.** How was the energy scale calibrated, how were the edge energy and the normalisation defined, and are claimed edge or pre-edge shifts large compared with the calibration reproducibility and interpreted against reference compounds of known oxidation state and coordination?

**Why it matters.** The energy scale can drift with monochromator mechanics and temperature and with movement of the source, so a shift of a fraction of an electronvolt means something only against a reference recorded at the same time. The edge energy has no unique definition and the edge step is only approximated, which affects white-line intensities and EXAFS coordination numbers. Edge and pre-edge position and intensity depend on coordination and site symmetry as well as oxidation state, and mixtures of phases do not combine linearly in these parameters, so a shift alone does not give a valence. An intense beam can itself reduce or otherwise alter the sample during the measurement.

**Resolved by.** A reference foil or compound measured simultaneously, with its assigned edge energy stated; the edge-energy definition and the pre-edge and post-edge normalisation ranges stated and kept the same across compared spectra; shifts quoted with an uncertainty from repeated scans; oxidation-state assignments calibrated against reference compounds of known valence and similar coordination, with mixed-valence estimates tested against known mixtures; successive scans, or scans on fresh spots, showing that the spectrum does not change with exposure.

**Benchmark.** [1], [2], [6], [7]

## 5. EXAFS fitting

**Question.** Does the paper state the k and R ranges and k-weighting of each fit, the number of free parameters compared with the number of independent points, the theory and scattering paths used, how the amplitude reduction factor was set, and the uncertainties and correlations of the fitted parameters?

**Why it matters.** A spectrum over a given k and R range holds only about 2ΔkΔR/π independent points, and that is an upper estimate, so fits with many shells or free parameters can be underdetermined. The amplitude reduction factor enters the fit only as a product with the coordination number, so the two cannot be separated by the fit, and the edge-energy shift is typically strongly correlated with distance. Neighbours of similar atomic number at nearly the same distance are hard to tell apart. The reduced chi-square of EXAFS fits is usually far above one because the noise is underestimated and the model is imperfect, and underestimated errors in background removal give optimistic error bars on fitted parameters.

**Resolved by.** Fit ranges, weighting, number of variables and number of independent points stated; the theory code and paths named; the amplitude reduction factor stated, with how it was obtained, for example from a reference compound of known structure fitted the same way; fits to reference compounds shown; split shells or assignments of neighbour type supported by the k range and tested against simpler models; correlations between strongly correlated parameters reported; uncertainties given with the method that produced them, together with the reduced chi-square and R-factor.

**Benchmark.** [2], [8], [13]

## 6. Measuring the dichroism

**Question.** For XMCD or XMLD, does the paper show the absorption spectra for both polarisations and not only their difference, say whether the dichroism came from helicity reversal, field reversal or both, and state the degree of polarisation, angle of incidence, temperature, and field magnitude, direction and history?

**Why it matters.** A dichroism is a small difference between two spectra, so background drift between them, the effect of the magnetic field on electron-yield detection, and a degree of circular polarisation that differs between helicities all enter it. Reversing helicity and reversing the field are equivalent only when the sample shows no optical activity. The spectra are sensitive to strain, defects, stoichiometry and impurity phases, and the beam can alter the sample, so a dichroism has to be shown to be reproducible and to belong to the phase the claim is about.

**Resolved by.** Both polarisation-dependent spectra shown, normalised with the pre-edge set to zero and the post-edge to one; dichroism from pairs of spectra with opposite magnetisation as well as opposite helicity, found consistent; the degree of polarisation stated and corrected for; element-specific hysteresis loops or field and temperature dependence linking the signal to the magnetic order; repeated spectra, or spectra on fresh spots, showing no beam damage, with the exposure stated.

**Benchmark.** [1], [9]

## 7. Spin and orbital moments from sum rules

**Question.** When spin and orbital moments are derived from the sum rules, does the paper state the number of holes and its source, how the isotropic spectrum and the continuum background were obtained, the integration ranges, and how the magnetic dipole term, the spin sum-rule correction for the element and valence, and any saturation or self-absorption were treated?

**Why it matters.** The number of holes cannot be measured on an absolute scale and is usually estimated; the average of the two circular spectra equals the isotropic spectrum only when there is no linear dichroism; and the step-function background is approximate and often unsuitable for ionic compounds. The magnetic dipole term can be large at surfaces and in low symmetry, and mixing of the spin-orbit-split core levels makes the spin sum rule unreliable for the earlier 3d ions: an error of 5 to 10 per cent for late transition metals grows to about 30 per cent for d5 ions and makes the result meaningless for d4 ions without further information. Even with care, moments from the sum rules agree with bulk measurements to about 10 per cent.

**Resolved by.** Hole number, background function, integration ranges and correction factors stated, with their effect on the moments; the ratio of orbital to spin moment, which does not depend on the hole number, reported alongside the absolute moments; the dipole term estimated, for example from angle-dependent spectra, or argued to be negligible for the symmetry; for early transition metals and light rare earths, a correction factor from multiplet calculations, or a comparison with multiplet simulations instead of the sum rules; moments compared with bulk magnetometry where possible; uncertainties that include these systematic contributions.

**Benchmark.** [1], [5], [9], [10]

## 8. Origin of linear dichroism

**Question.** When X-ray linear dichroism is used to claim magnetic order or a spin orientation, does the paper separate the magnetic contribution from linear dichroism caused by low-symmetry crystal fields, and take into account the orientation of the crystal axes relative to the polarisation and the field?

**Why it matters.** Low-symmetry crystal fields in thin films, at surfaces and interfaces and in strained layers can produce a linear dichroism that closely resembles magnetic linear dichroism, so a dichroism alone does not establish order or fix a spin direction. Magnetic linear dichroism also depends on the orientation of the moments and the polarisation relative to the crystal axes, so one spectral ratio need not give a unique spin axis.

**Resolved by.** Temperature dependence through the ordering temperature, since for the high-spin ions concerned crystal-field dichroism does not change with temperature while magnetic dichroism follows the order; spectral signatures of the crystal field, such as polarisation-dependent energy shifts, analysed; spectra at several orientations of polarisation and field relative to the crystal axes; comparison with multiplet calculations that include both the crystal field and exchange.

**Benchmark.** [11], [12]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | C. A. F. Vaz et al., X-ray magnetic circular dichroism, Nat. Rev. Methods Primers 5, 27 (2025); read as the accepted author version in the White Rose repository (eprint 226671) | doi:10.1038/s43586-025-00397-9 |
| 2 | M. Newville, Fundamentals of XAFS, tutorial notes, revision 1.8 (2008), hosted by the International XAFS Society | https://docs.xrayabsorption.org/tutorials/XAFS_Fundamentals.pdf |
| 3 | H. Abe et al., Improving the quality of XAFS data, J. Synchrotron Rad. 25, 972 (2018) | doi:10.1107/S1600577518006021 |
| 4 | L. Tröger et al., Full correction of the self-absorption in soft-fluorescence extended x-ray-absorption fine structure, Phys. Rev. B 46, 3283 (1992) | doi:10.1103/PhysRevB.46.3283 |
| 5 | R. Nakajima et al., Electron-yield saturation effects in L-edge x-ray magnetic circular dichroism spectra of Fe, Co, and Ni, Phys. Rev. B 59, 6421 (1999) | doi:10.1103/PhysRevB.59.6421 |
| 6 | S. Diaz-Moreno, XAFS data collection: an integrated approach to delivering good data, J. Synchrotron Rad. 19, 863 (2012) | doi:10.1107/S090904951203854X |
| 7 | M. Wilke et al., Oxidation state and coordination of Fe in minerals: An Fe K-XANES spectroscopic study, Am. Mineral. 86, 714 (2001); abstract read through the OpenAlex record | doi:10.2138/am-2001-5-612 |
| 8 | K. V. Klementev, XAFS spectroscopy. II. Statistical evaluations in the fitting problems, arXiv:physics/0003087 (2000) | doi:10.48550/arXiv.physics/0003087 |
| 9 | C. T. Chen et al., Experimental confirmation of the X-ray magnetic circular dichroism sum rules for iron and cobalt, Phys. Rev. Lett. 75, 152 (1995) | doi:10.1103/PhysRevLett.75.152 |
| 10 | C. Piamonteze et al., Accuracy of the spin sum rule in XMCD for the transition-metal L edges from manganese to copper, Phys. Rev. B 80, 184410 (2009) | doi:10.1103/PhysRevB.80.184410 |
| 11 | M. W. Haverkort et al., Magnetic versus crystal-field linear dichroism in NiO thin films, Phys. Rev. B 69, 020408 (2004); read as preprint arXiv:cond-mat/0310634 | doi:10.1103/PhysRevB.69.020408 |
| 12 | E. Arenholz et al., Anisotropic x-ray magnetic linear dichroism at the Fe L2,3 edges in Fe3O4, Phys. Rev. B 74, 094407 (2006) | doi:10.1103/PhysRevB.74.094407 |
| 13 | M. Newville, Fitting XAFS to Feff Paths, chapter of the Larch documentation (online, read October 2026) | https://xraypy.github.io/xraylarch/xafs_feffit.html |
