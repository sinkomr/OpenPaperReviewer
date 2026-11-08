---
id: T-NEUTRON-SCATTERING
name: Neutron scattering
type: technique
field: physics/condensed-matter
applies_when: the paper reports neutron diffraction, inelastic neutron scattering or small-angle neutron scattering from solids, or bases a claim about a nuclear or magnetic structure, an ordered moment, phonons, magnetic excitations or spectral weight on neutron data; soft-matter scattering has its own card
version: "0.1"
---

# Neutron scattering

## 1. Magnetic or nuclear origin of the scattering

**Question.** How does the paper show that the scattering it attributes to magnetism is magnetic: by its temperature or field dependence, by a fall of intensity with Q that follows the magnetic form factor, or by polarisation analysis?

**Why it matters.** Unpolarised neutrons scatter from nuclei and from magnetic moments alike, so a new peak or a change in diffuse scattering at low temperature can also come from a structural distortion, an impurity phase or nuclear diffuse scattering. Magnetic intensity falls with Q as the form factor does and comes only from the moment component perpendicular to Q, while phonon intensity grows with Q.

**Resolved by.** Intensities followed through the ordering temperature or in field; the Q dependence of the signal compared with the expected form factor across several Brillouin zones; where nuclear and magnetic contributions overlap, polarisation analysis that separates nuclear, magnetic and spin-incoherent cross-sections.

**Benchmark.** [1], [2], [3]

## 2. Magnetic structure model and its alternatives

**Question.** Was the magnetic structure derived with a symmetry analysis of the paramagnetic phase, are the irreducible representation or magnetic space group stated, and were the other symmetry-allowed models refined against the same data?

**Why it matters.** Magnetic structures have often been found by intuition or trial-and-error refinement, and published structures are often wrong or incompletely refined. Powder data can be fitted well by simple models that symmetry does not allow, and correlations between moments that the stated symmetry does not impose have been added by hand.

**Resolved by.** The propagation vector, the irreducible representation or magnetic space group and the resulting constraints on the moments stated; each symmetry-allowed candidate refined and its fit reported, with the reason for preferring one; the structure given in a form that others can reuse, such as a magnetic crystallographic information file.

**Benchmark.** [3], [4]

## 3. Size of the ordered moment

**Question.** How was the ordered moment obtained from magnetic intensities: against which nuclear reflections was it normalised, with which form factor, and were extinction and absorption considered?

**Why it matters.** The moment follows from the ratio of magnetic to nuclear intensities, so errors in the nuclear model, in the form factor or in extinction of strong reflections pass directly into its size. Because only the component perpendicular to Q scatters and magnetic intensity is confined to low Q, least-squares refinements of moment size and direction can be unstable.

**Resolved by.** The nuclear structure refined from the same data set and used for normalisation; the form factor named; extinction treated or shown to be small for the reflections used; the moment given with an uncertainty that includes these steps, and its direction with the constraints that fix it.

**Benchmark.** [3], [5]

## 4. Absorption, incoherent scattering and sample composition

**Question.** Does the paper account for strongly absorbing elements and hydrogen in the sample or its environment, by correction, isotope substitution or deuteration, and does it report the sample mass, transmission and isotopic composition?

**Why it matters.** Some elements, such as boron, cadmium, samarium and gadolinium, absorb thermal neutrons hundreds to tens of thousands of times more strongly than most elements, which distorts intensities unless corrected. Hydrogen has an incoherent cross-section of about 80 barn, which adds a large flat background that can mask weak signals and makes background subtraction difficult.

**Resolved by.** Absorption corrections applied with the measured transmission or a calculated attenuation; strongly absorbing isotopes replaced where possible, or a geometry chosen to limit absorption; deuterated samples or solvents with the level of deuteration stated; the incoherent background estimated and subtracted by a stated method.

**Benchmark.** [6], [7], [8]

## 5. Spurious scattering and background

**Question.** Does the paper show that a feature it interprets is not spurious scattering from the instrument or sample environment, such as Bragg peaks from aluminium or copper, higher-order wavelengths, or scattering that is incoherent at the monochromator or analyser, and was an empty holder or environment measured?

**Why it matters.** A small fraction of the beam is always scattered incoherently by the monochromator or analyser, and can then be Bragg diffracted by the sample or its container to give a peak at an energy transfer where nothing happens in the sample. Higher-order wavelengths and phonons in the monochromator or analyser give further features, and incoherent scattering from holders and sample environment can also bias normalisation.

**Resolved by.** An empty holder or sample-environment measurement subtracted under the same conditions; filters against higher-order contamination stated; features checked against the known positions of spurious peaks, for instance by changing the incident or final energy and seeing whether the feature moves; the feature followed in temperature or in sample rotation where that tests its origin.

**Benchmark.** [5], [9]

## 6. Identifying excitations in inelastic spectra

**Question.** On what evidence does the paper assign an inelastic feature to a magnetic excitation, a phonon or another mode, and are claimed gaps, widths and dispersions compared with the instrumental resolution?

**Why it matters.** Phonon and magnetic intensities both follow the Bose factor, so temperature dependence alone does not separate them; their Q dependence differs, with magnetic intensity falling with the form factor and phonon intensity growing with Q. Triple-axis instruments have a resolution function that is not trivial, and measurements taken without care can produce spurious features or apparent widths and shifts.

**Resolved by.** The Q dependence of the feature followed over several zones, with polarisation analysis where the assignment is in doubt; temperature dependence compared with the Bose factor; the resolution calculated or measured at the relevant positions and models convolved with it before gaps, widths or dispersions are quoted.

**Benchmark.** [1], [2], [10]

## 7. Absolute normalisation of spectral weight

**Question.** Where the paper quotes spectral weight, a fluctuating moment or a susceptibility in absolute units, which normalisation was used (vanadium, incoherent scattering of the sample, phonons or Bragg peaks), and what systematic errors does it carry?

**Why it matters.** Absolute units allow the spectral weight to be compared with sum rules and with the bulk susceptibility, but each route has its own errors: incoherent scattering from the holder and sample environment leads to an overestimate of the resolution volume and so an underestimate of the magnetic intensity, phonon normalisation carries errors of order 20 percent, and extinction affects normalisation to Bragg peaks.

**Resolved by.** The normalisation route and the quantities that enter it stated, such as sample mass, form factor and g-factor; the result cross-checked by a second route where possible; the integrated weight compared with the relevant sum rule and with bulk measurements, with the systematic uncertainty given.

**Benchmark.** [5]

## 8. Small-angle scattering: reduction, absolute scale and model choice

**Question.** For SANS results, does the paper describe the reduction (transmission, thickness, background and solvent subtraction), place intensities on an absolute scale with a stated standard, test for multiple scattering, and show that the chosen model is preferred over others that fit as well?

**Why it matters.** Errors in background or solvent subtraction mainly affect the weak high-Q data. Multiple scattering grows in thick, strongly scattering samples and changes the profile. Size, shape, polydispersity and packing cannot all be determined from one pattern, so a good fit does not show that the model is unique.

**Resolved by.** The reduction steps and blank listed; intensities in absolute units against a named standard; multiple scattering checked, for instance by measuring samples of different thickness or at another wavelength; residuals and goodness of fit shown; alternative models compared; supporting information from microscopy or another technique where shape and polydispersity must both be fixed.

**Benchmark.** [7], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J. R. Stewart et al., Disordered materials studied using neutron polarization analysis on the multi-detector spectrometer, D7, J. Appl. Cryst. 42, 69 (2009) | doi:10.1107/S0021889808039162 |
| 2 | I. A. Zaliznyak and J. M. Tranquada, Neutron scattering and its application to strongly correlated systems, in Strongly Correlated Systems: Experimental Techniques, Springer Series in Solid-State Sciences 180, 205 (2015); read as preprint arXiv:1304.4214 | doi:10.1007/978-3-662-44133-6_7 |
| 3 | A. S. Wills, Symmetry and magnetic structure determination: developments in refinement techniques and examples, Appl. Phys. A 74, S856–S858 (2002); read as preprint arXiv:cond-mat/0109391 | doi:10.1007/s003390101159 |
| 4 | J. Rodríguez-Carvajal and J. M. Perez-Mato, Magnetic space groups versus representation analysis in the investigation of magnetic structures: the happy end of a strained relationship, Acta Cryst. B80, 370 (2024); read through Europe PMC (PMC11457108) | doi:10.1107/S2052520624007479 |
| 5 | G. Xu et al., Absolute cross-section normalization of magnetic neutron scattering data, Rev. Sci. Instrum. 84, 083906 (2013); read as preprint arXiv:1305.5521 | doi:10.1063/1.4818323 |
| 6 | National Institute of Standards and Technology (NIST) Center for Neutron Research, Neutron scattering lengths and cross sections, web table entered from the special feature in Neutron News 3(3), 29 (1992) | https://www.ncnr.nist.gov/resources/n-lengths/list.html |
| 7 | J. Trewhella et al., 2017 publication guidelines for structural modelling of small-angle scattering data from biomolecules in solution: an update, Acta Cryst. D73, 710 (2017); read through Europe PMC (PMC5586245) | doi:10.1107/S2059798317011597 |
| 8 | B. R. Pauw, Everything SAXS: small-angle scattering pattern collection and correction, J. Phys.: Condens. Matter 25, 383201 (2013); read as preprint arXiv:1306.0637 | doi:10.1088/0953-8984/25/38/383201 |
| 9 | Institut Laue-Langevin (ILL), Spectroscopy group, Useful links: spurions in triple-axis experiments, web page (accessed 2026) | https://www.ill.eu/users/scientific-groups/spectroscopy/useful-links |
| 10 | T. Weber et al., Takin: an open-source software for experiment planning, visualisation, and data analysis, SoftwareX 5, 121 (2016); read as preprint arXiv:1903.02632v1 | doi:10.1016/j.softx.2016.06.002 |
