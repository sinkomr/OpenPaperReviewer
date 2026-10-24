---
id: T-PLASMA-SPECTROSCOPY
name: Spectroscopic plasma diagnostics
type: technique
field: physics/plasma
applies_when: the paper infers electron or ion temperature, electron density, flow velocity or impurity content of a plasma from emission, absorption or charge-exchange spectra, using line intensities or ratios, line widths, Doppler shifts, Stark broadening or collisional-radiative modelling
version: "0.1"
---

# Spectroscopic plasma diagnostics

Optical emission spectroscopy (OES), absorption spectroscopy and charge-exchange recombination spectroscopy (CXRS) are used to claim electron and ion temperatures, electron density, flow velocities and impurity densities. Each of these is inferred through a model: of level populations, either local thermodynamic equilibrium (LTE) or a collisional-radiative (CR) model, of line shapes, of radiation transport, and of the path along which the light was collected.

## 1. Equilibrium assumed behind a temperature or density

**Question.** When a temperature or density comes from Boltzmann plots, Saha-Boltzmann relations or line ratios that assume LTE or partial LTE, does the paper show that the plasma meets that assumption at the times and places measured, and not only that it passes a minimum-density criterion?

**Why it matters.** Boltzmann and Saha relations hold only if collisions dominate radiative processes. The usual minimum-density criterion was derived for homogeneous, optically thin plasmas and is necessary but not sufficient in transient or inhomogeneous ones. Even where upper levels follow the Saha-Boltzmann relation, lower levels may not, and the level above which they do differs between ionising and recombining plasmas.

**Resolved by.** The equilibrium assumed stated for each quantity; an argument for it that covers the rate of change and the gradients of the plasma, not only its density; time- and space-resolved data at the conditions where the claim is made; temperatures from different species or ionisation stages compared; a CR model used instead where the assumption is in doubt, or the effect of departures from equilibrium estimated.

**Benchmark.** [1], [2]

## 2. Collisional-radiative model and its atomic data

**Question.** Which population model (coronal, CR, or LTE) and which atomic data set convert line intensities or ratios into temperature, density or impurity content, and does the paper show how sensitive the result is to that choice?

**Why it matters.** In plasmas of finite density that change in time, ionisation state and level populations depend on metastable states and on how fast the plasma changes, not only on local temperature and density. Calculated atomic data are a main input to these models and their uncertainties need to be estimated and carried through, and independent CR codes given the same plasma conditions predict different populations and spectra because of differences in level structure, completeness, density effects and rates.

**Resolved by.** The model, code and atomic data source named, with versions; the assumptions about metastables, ionisation balance and transport stated; the sensitivity of the inferred quantity to the rate coefficients or to an alternative model or data set shown, and carried into the stated uncertainty; where possible, the diagnostic ratio checked against an independent measurement.

**Benchmark.** [3], [4], [5]

## 3. Line broadening and Stark density

**Question.** When electron density comes from a Stark width, or temperature from a Doppler width, does the paper separate the instrumental, Doppler, Stark, van der Waals and resonance contributions, state the line and the source of its broadening parameters, and show that the line is within their range of validity?

**Why it matters.** The measured profile is a convolution of several broadening mechanisms and the instrument function, and the contribution of each depends on density, temperature and background gas pressure. The inferred density is no more accurate than the reference Stark parameters, densities from different lines of the same plasma can disagree, and Stark widths become too small to measure at low densities.

**Resolved by.** The measured instrument function and its deconvolution stated; the Doppler and pressure contributions estimated and shown to be small or removed; the Stark parameters cited with their stated accuracy and density range; densities from two or more lines, or from a hydrogen line and a non-hydrogenic line, compared; a line chosen that is isolated from its neighbours and optically thin.

**Benchmark.** [1], [6]

## 4. Opacity and self-absorption

**Question.** Does the paper show that the lines used for intensities, ratios or widths are optically thin under the conditions measured, or correct for self-absorption?

**Why it matters.** Self-absorption is strongest at line centre, so it lowers peak intensity, broadens the line and distorts intensity ratios, and it is hard to detect from line shape alone. In an inhomogeneous plasma, absorption in cooler outer layers can produce a central dip. Opacity also changes the conditions under which level populations follow equilibrium relations.

**Resolved by.** An estimate of optical depth for each line used, or a test such as comparing ratios within a multiplet with their optically thin values; resonance lines and strong lines avoided or corrected; self-absorption corrections applied before widths or intensities are used, and their size stated.

**Benchmark.** [1], [2]

## 5. Line-of-sight integration and inversion

**Question.** Is each quantity a local value or an average along the line of sight and over the exposure, and if local values come from an inversion, does the paper state the method, its assumptions such as symmetry, and how the inversion affects the uncertainty and the spatial resolution?

**Why it matters.** Light collected along a chord, or over a gate longer than the time the plasma takes to change, mixes regions of different temperature and density, so a fit returns a weighted average that can differ from every local value and between species. An absorption measurement gives a column density, and the density follows only through an assumed absorption path length. Inversion of line-integrated data is ill-posed, particularly with few chords, and the result depends on the symmetry assumed and on the regularisation and prior information used.

**Resolved by.** The viewing geometry and the gate or exposure times stated; the result labelled as chord-integrated or local; for absorption, the path length used to convert column density to density stated and justified; for inversions, the method, symmetry assumption and regularisation given, with a test on synthetic data or a comparison of chord-integrated and inverted results; the time resolution shown to be short compared with the evolution of the plasma.

**Benchmark.** [1], [7]

## 6. Line selection, transition data and relative calibration

**Question.** For temperatures from line ratios or Boltzmann plots, does the paper list the lines used with their upper-level energies, transition probabilities and the accuracy of those values, and describe how the relative spectral response of the system was calibrated across the lines?

**Why it matters.** A Boltzmann temperature comes from the slope of intensities against upper-level energy, so lines close in energy give a poorly constrained slope. Tabulated transition probabilities carry uncertainties from below one per cent to more than fifty per cent, and errors in the relative response between wavelengths change the ratios directly.

**Resolved by.** A table of lines with wavelengths, upper-level energies, statistical weights, transition probabilities, their source and accuracy grade; lines spanning a wide range of upper-level energy; the Boltzmann plot shown with its scatter and fit uncertainty; the relative intensity calibration described with the reference source; line identifications checked for blends with lines of other species.

**Benchmark.** [1], [8]

## 7. Charge-exchange spectra: active signal, passive background and cross-section effects

**Question.** For ion temperature, flow or impurity density from charge-exchange spectra, does the paper describe how the active signal was separated from passive and edge emission, and whether the measured width, shift and intensity were corrected for the energy dependence of the charge-exchange cross-section?

**Why it matters.** Passive charge-exchange emission, from background neutrals that enter from the wall, adds to the active signal along the same line of sight, and for helium an additional plume emission can, under some conditions, be comparable to the active signal and has a non-Gaussian shape. The energy dependence of the emission rate shifts and usually narrows the observed line, giving an apparent velocity and temperature, and changes the effective emission rate used for impurity density.

**Resolved by.** The background subtraction method stated, for example beam modulation or dedicated passive views, with a check that the background is stable over the subtraction; edge and plume contributions modelled or shown to be small; cross-section corrections to temperature, velocity and intensity applied and their size given; the beam neutral density and effective emission rates used for impurity density stated with their source and uncertainty.

**Benchmark.** [9], [10], [11]

## 8. Doppler width and shift: Zeeman splitting, fine structure and the wavelength reference

**Question.** When an ion or neutral temperature comes from a Doppler width, or a flow from a line shift, does the paper account for Zeeman splitting and fine structure in the line, and state how the unshifted reference wavelength was established and kept stable?

**Why it matters.** In a magnetic field a line is a superposition of Zeeman and fine-structure components, so its profile need not be Gaussian, and fitting a single Doppler profile assigns the extra width to temperature; the same components can also move the line centre by an amount that depends on temperature. A flow is a small shift measured against a reference wavelength, so an error in the rest wavelength or a drift of the wavelength scale appears directly as an apparent velocity.

**Resolved by.** The magnetic field at the emitting region and the Zeeman and fine-structure pattern of the line included in the fitted model, or shown to be small compared with the Doppler width; the rest wavelength and its source given; the wavelength scale calibrated against reference lines near the measured line and checked for drift over the measurements; for flows, the angle between the line of sight and the flow stated.

**Benchmark.** [12]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | S. S. Harilal, M. C. Phillips, D. H. Froula, K. K. Anoop, R. C. Issac and F. N. Beg, Optical diagnostics of laser-produced plasmas, Rev. Mod. Phys. 94, 035002 (2022); read as preprint arXiv:2201.08783v4 | doi:10.1103/RevModPhys.94.035002 | full text | Preprint Sec. II.1.1: Lorentzian (Stark, resonance, van der Waals) and Gaussian (Doppler) contributions combine with the instrument profile and must be deconvolved; self-absorption is strongest at line centre, broadens lines, can cause self-reversal in inhomogeneous plasmas, and must be corrected before line-shape diagnostics; space- or time-integrated data give only weighted averages. Sec. II.1.2: choose strong, optically thin lines well separated from neighbours; density accuracy limited by the reference Stark parameters, and densities from lines of several elements scattered; Stark broadening becomes negligible at low density. Sec. II.1.3: several lines with a large upper-energy spread for Boltzmann plots; line-of-sight measurements can introduce systematic error, and integrated temperatures of two species differed while Abel-inverted local values agreed. Sec. II.2: absorbance depends on the product of density and absorption path length. Sec. II.4: the minimum-density criterion, derived for homogeneous, optically thin plasma, is necessary but not sufficient for transient, inhomogeneous plasmas; integrated measurements may depart from LTE; CR models describe non-LTE plasmas |
| 2 | T. Fujimoto and R. W. P. McWhirter, Validity criteria for local thermodynamic equilibrium in plasma spectroscopy, Phys. Rev. A 42, 6588 (1990) | doi:10.1103/PhysRevA.42.6588 | abstract | Abstract: CR calculations show that only levels above a certain principal quantum number follow Saha-Boltzmann populations (partial LTE); separate criteria for ionising, recombining and balanced plasmas; extension to complete LTE; effect of opacity on the criteria considered |
| 3 | H. P. Summers, W. J. Dickson, M. G. O'Mullane, N. R. Badnell, A. D. Whiteford, D. H. Brooks, J. Lang, S. D. Loch and D. C. Griffin, Ionization state, excited populations and emission of impurities in dynamic finite density plasmas: I. The generalized collisional-radiative model for light elements, Plasma Phys. Control. Fusion 48, 263–293 (2006); abstract read through its OpenAlex record | doi:10.1088/0741-3335/48/2/007 | abstract | Abstract: ionisation state in dynamic plasmas of finite density is tied to population structure; metastable states treated explicitly in the generalised CR framework; derived coefficients for experimental analysis supplied through the ADAS project |
| 4 | H.-K. Chung, B. J. Braams, K. Bartschat, A. G. Császár, G. W. F. Drake, T. Kirchner, V. Kokoouline and J. Tennyson, Uncertainty estimates for theoretical atomic and molecular data, J. Phys. D: Appl. Phys. 49, 363002 (2016); read as preprint arXiv:1603.05923 | doi:10.1088/0022-3727/49/36/363002 | full text | Sec. I: calculated data are the main input to plasma modelling codes and should carry uncertainty estimates, to be tracked as they propagate through simulations. Sec. II: compare independent methods to expose systematic errors; use sensitivity tests where propagation is not feasible. Sec. IV: uncertainty from the choice of scattering model should be quantified. Sec. V: run model variants and monitor the spread of results for charge transfer |
| 5 | S. B. Hansen, H.-K. Chung, C. J. Fontes, Yu. Ralchenko, H. A. Scott and E. Stambulchik, Review of the 10th Non-LTE code comparison workshop, High Energy Density Phys. 35, 100693 (2020); read as preprint arXiv:1903.09605 | doi:10.1016/j.hedp.2019.06.001 | abstract | Abstract: fifteen CR codes compared on common cases; differences in predictions arise from internal structure, completeness, density effects and rate fidelity, with consequences for diagnostics of hot, dense plasmas |
| 6 | N. Konjević, A. Lesage, J. R. Fuhr and W. L. Wiese, Experimental Stark widths and shifts for spectral lines of neutral and ionized atoms (a critical review of selected data for the period 1989 through 2000), J. Phys. Chem. Ref. Data 31, 819–927 (2002); abstract read through its OpenAlex record | doi:10.1063/1.1486456 | abstract | Abstract: critically evaluated experimental Stark widths and shifts tabulated with an estimated accuracy for each, guidelines for accuracy estimates, and comparison with semiclassical calculations where possible |
| 7 | J. Mlynar, V. Weinzettl, G. Bonheure, A. Murari and JET-EFDA contributors, Inversion techniques in the soft-X-ray tomography of fusion plasmas: toward real-time applications, Fusion Sci. Technol. 58, 733–741 (2010); abstract read through its OpenAlex record | doi:10.13182/FST58-733 | abstract | Abstract: recovering local emissivity from line-integrated plasma measurements is an ill-posed, often underdetermined problem; few lines of sight and fast plasma changes; inversion methods accept lower resolution and use prior information and constraints |
| 8 | National Institute of Standards and Technology (NIST), Atomic Spectra Database, Spectral Lines Help File, web page describing ASD version 5.11 and later (undated; accessed 2026) | https://physics.nist.gov/PhysRefData/ASD/Html/lineshelp.html | full text | Section "Accuracy": each transition probability carries a letter grade, from AAA (at most 0.3 %) to E (more than 50 %), reflecting mainly systematic effects; values split from multiplets assuming LS coupling may be less accurate |
| 9 | M. von Hellermann, P. Breger, J. Frieling, R. König, W. Mandl, A. Maas and H. P. Summers, Analytical approximation of cross-section effects on charge exchange spectra observed in hot fusion plasmas, Plasma Phys. Control. Fusion 37, 71–94 (1995); abstract read through its OpenAlex record | doi:10.1088/0741-3335/37/2/002 | abstract | Abstract: the energy-dependent charge-exchange emission rate produces a line shift (apparent velocity), usually a narrowing (apparent temperature) and a change in the effective emission rate; an algebraic deconvolution recovers true temperature, rotation and intensities; representative correction factors given |
| 10 | M. Tunklev, P. Breger, K. Günther, M. von Hellermann, R. König, M. G. O'Mullane and K.-D. Zastrow, Modelling of passive charge exchange emission and neutral background density deduction in JET, Plasma Phys. Control. Fusion 41, 985–1004 (1999); abstract read through its OpenAlex record | doi:10.1088/0741-3335/41/8/305 | abstract | Abstract: passive charge-exchange emission between wall neutrals and fully ionised impurities contaminates the active spectra used for ion temperature, impurity density and rotation; modelling it reduces errors in ion temperature |
| 11 | A. Kappatou, R. M. McDermott, T. Pütterich, R. Dux, B. Geiger, R. J. E. Jaspers, A. J. H. Donné, E. Viezzer, M. Cavedon and the ASDEX Upgrade Team, A forward model for the helium plume effect and the interpretation of helium charge exchange measurements at ASDEX Upgrade, Plasma Phys. Control. Fusion 60, 055006 (2018); abstract read through its OpenAlex record | doi:10.1088/1361-6587/aab25a | abstract | Abstract: an additional plume emission cannot be separated from the active helium signal by standard analysis, can be of the same order of magnitude, and if ignored overestimates helium density; its non-Gaussian shape biases ion temperature and flow |
| 12 | A. Blom and C. Jupén, Parametrization of the Zeeman effect for hydrogen-like spectra in high-temperature plasmas, Plasma Phys. Control. Fusion 44, 1229–1241 (2002); abstract read through its OpenAlex record | doi:10.1088/0741-3335/44/7/312 | abstract | Abstract: the Zeeman pattern of hydrogen-like lines with unresolved fine structure is parametrised for inclusion in ion temperature diagnostics, valid where the total line shape is no longer Gaussian; non-statistical upper-sublevel populations and a temperature-dependent shift of line centres discussed |
