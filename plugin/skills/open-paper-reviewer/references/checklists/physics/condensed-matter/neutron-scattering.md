---
id: T-NEUTRON-SCATTERING
name: Neutron scattering
type: technique
field: physics/condensed-matter
applies_when: the paper reports neutron diffraction, small-angle neutron scattering or inelastic neutron scattering, or bases a claim about a nuclear or magnetic structure, an ordered moment, nanoscale structure, phonons, magnetic excitations or spectral weight on neutron data
version: "0.1"
---

# Neutron scattering

Neutron diffraction is used to claim nuclear and magnetic structures and the size and direction of ordered moments; small-angle neutron scattering (SANS) to claim the size, shape and arrangement of nanoscale structures; and inelastic neutron scattering (INS) to claim the dispersion, gaps, widths and spectral weight of phonons and magnetic excitations. Each claim is inferred from intensities measured as a function of momentum transfer Q, and for INS of energy transfer.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | J. R. Stewart, P. P. Deen, K. H. Andersen, H. Schober, J.-F. Barthélémy, J. M. Hillier, A. P. Murani, T. Hayes and B. Lindenau, Disordered materials studied using neutron polarization analysis on the multi-detector spectrometer, D7, J. Appl. Cryst. 42, 69–84 (2009) | doi:10.1107/S0021889808039162 | abstract | Abstract: longitudinal xyz polarisation analysis separates the nuclear, magnetic and nuclear spin-incoherent cross-sections as functions of momentum and energy transfer, including in the scattering between Bragg peaks |
| 2 | I. A. Zaliznyak and J. M. Tranquada, Neutron scattering and its application to strongly correlated systems, in Strongly Correlated Systems: Experimental Techniques, Springer Series in Solid-State Sciences 180, 205–235 (2015); read as preprint arXiv:1304.4214 | doi:10.1007/978-3-662-44133-6_7 | full text | Sec. 0.7, Eq. 29: one-phonon cross-section with a prefactor in the scalar product of Q and the polarisation vector, and the Bose factor. Secs. 0.5 and 0.8, Eqs. 32–33 and 39: only the magnetisation perpendicular to Q scatters; polarised neutrons separate spin-flip and non-spin-flip scattering. Secs. 0.8.4 and 0.8.6: magnetic intensity follows the magnetic form factor. Eq. 56: spin-wave cross-section carries the same Bose factor |
| 3 | A. S. Wills, Symmetry and magnetic structure determination: developments in refinement techniques and examples, Appl. Phys. A 74, S856–S858 (2002); read as preprint arXiv:cond-mat/0109391 | doi:10.1007/s003390101159 | full text | Sec. 1: magnetic structures are generally found by intuition or simple trial-and-error refinement, and published structures are often incorrect or incompletely refined. Sec. 3: by Landau theory a continuous transition involves one irreducible representation, which reduces the trial structures and their variables. Sec. 5: the form factor and sensitivity only to the perpendicular moment make least-squares refinement unstable. Sec. 7: powder data well fitted by a simple model that symmetry does not allow |
| 4 | J. Rodríguez-Carvajal and J. M. Perez-Mato, Magnetic space groups versus representation analysis in the investigation of magnetic structures: the happy end of a strained relationship, Acta Cryst. B80, 370–376 (2024); read through Europe PMC (PMC11457108) | doi:10.1107/S2052520624007479 | full text | Sec. 2: in a reported structure, moment correlations were imposed that its magnetic space group cannot explain, and magnetic space groups were often not stated. Sec. 3.2.2: candidate models refined under each possible magnetic space group; the magCIF format allows exchange and combined analysis. Sec. 4: refining irrep mode amplitudes identifies weakly coupled modes |
| 5 | G. Xu, Z. Xu and J. M. Tranquada, Absolute cross-section normalization of magnetic neutron scattering data, Rev. Sci. Instrum. 84, 083906 (2013); read as preprint arXiv:1305.5521 | doi:10.1063/1.4818323 | full text | Sec. I: absolute units allow comparison with sum rules and bulk susceptibility; extinction in single crystals can strongly affect absolute Bragg intensities; form factor and g-factor enter. Sec. III.1: incoherent scattering from holders and sample environment can lead to an overestimated resolution volume and an underestimated magnetic intensity. Sec. III.2: vanadium normalisation needs sample masses. Sec. III.3: phonon normalisation carries systematic errors of about 20 percent |
| 6 | National Institute of Standards and Technology (NIST) Center for Neutron Research, Neutron scattering lengths and cross sections, web table entered from the special feature in Neutron News 3(3), 29–37 (1992) | https://www.ncnr.nist.gov/resources/n-lengths/list.html | full text | Table of bound coherent and incoherent cross-sections and absorption cross-sections for 2200 m/s neutrons: hydrogen incoherent about 80 barn against deuterium about 2 barn; absorption of natural boron, cadmium, samarium and gadolinium from hundreds to tens of thousands of barn, against a few barn for most elements |
| 7 | J. Trewhella, A. P. Duff, D. Durand, F. Gabel, J. M. Guss, W. A. Hendrickson, G. L. Hura, D. A. Jacques, N. M. Kirby, A. H. Kwan, J. Pérez, L. Pollack, T. M. Ryan, A. Sali, D. Schneidman-Duhovny, T. Schwede, D. I. Svergun, M. Sugiyama, J. A. Tainer, P. Vachette, J. Westbrook and A. E. Whitten, 2017 publication guidelines for structural modelling of small-angle scattering data from biomolecules in solution: an update, Acta Cryst. D73, 710–728 (2017); read through Europe PMC (PMC5586245) | doi:10.1107/S2059798317011597 | full text | Secs. 2.1–2.2 with Tables 1–2: reduction corrects for transmission, incident intensity and solvent subtraction, whose errors affect the high-Q data; intensities on an absolute scale against water or a secondary standard; large hydrogen incoherent scattering complicates SANS subtraction; deuteration levels and transmissions reported. Sec. 2.4 with Table 4: report fit quality and residuals and assess model ambiguity |
| 8 | B. R. Pauw, Everything SAXS: small-angle scattering pattern collection and correction, J. Phys.: Condens. Matter 25, 383201 (2013); read as preprint arXiv:1306.0637 | doi:10.1088/0953-8984/25/38/383201 | full text | Sec. 1.1: shape, polydispersity and packing cannot all be determined from one pattern, so supporting techniques are needed; many of the principles and corrections may also be applied to neutrons. Secs. 3.4.2, 3.4.4 and 3.4.5: transmission, absolute calibration against a standard, background measured with everything but the sample. Sec. 3.4.8: multiple scattering grows for thick, strongly scattering samples and is tested by varying thickness or wavelength |
| 9 | Institut Laue-Langevin (ILL), Spectroscopy group, Useful links: spurions in triple-axis experiments, web page (accessed 2026) | https://www.ill.eu/users/scientific-groups/spectroscopy/useful-links | full text | Spurion list: Bragg peaks from aluminium or copper in the beam; harmonic wavelengths; about 1e-5 of the beam scattered incoherently by the monochromator or analyser and then Bragg diffracted by the sample, recognised by rotating the sample, detuning the monochromator or analyser, or changing the incident or final wavevector; phonons in the monochromator or analyser, independent of temperature and sample rotation |
| 10 | T. Weber, R. Georgii and P. Böni, Takin: an open-source software for experiment planning, visualisation, and data analysis, SoftwareX 5, 121–126 (2016); read as preprint arXiv:1903.02632v1 | doi:10.1016/j.softx.2016.06.002 | abstract | Abstract: the non-trivial resolution function of triple-axis spectrometers means that measurements need care to avoid unwanted spurious artefacts |
