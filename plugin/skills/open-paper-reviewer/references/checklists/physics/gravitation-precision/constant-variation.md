---
id: T-CONSTANT-VARIATION
name: Variation of fundamental constants
type: technique
field: physics/gravitation-precision
applies_when: the paper reports a drift, oscillation or spatial variation of the fine-structure constant, the proton-to-electron mass ratio or related constants, or a limit on one, from atomic clock comparisons, quasar or radio absorption spectra, the Oklo reactor or a combination of probes
version: "0.1"
---

# Variation of fundamental constants

## 1. The quantity constrained and the sensitivity coefficients

**Question.** Which dimensionless constant or combination of constants does the measurement constrain, which sensitivity coefficient was used for each transition (with its source and uncertainty), and how large is the difference in sensitivity between the transitions compared?

**Why it matters.** Only dimensionless quantities, such as ratios of frequencies, can be measured, and a frequency ratio is sensitive to a change in the constants only through the difference of the sensitivity coefficients of the two transitions. Microwave and radio lines usually depend on a combination of α, μ and g_p rather than on one constant. Sensitivity coefficients come from atomic or molecular structure calculations, and different calculations can disagree; an error in a coefficient rescales the inferred change or limit, though it cannot by itself create a non-zero result.

**Resolved by.** The measured quantity written as a dimensionless ratio, with the combination of constants it depends on; a table of sensitivity coefficients with references, a stated uncertainty based on comparing calculation methods, and the resulting sensitivity difference; a check that the conclusion does not change within the spread of the coefficients.

**Benchmark.** [1], [2], [4]

## 2. Laboratory reference frequencies and isotopic structure

**Question.** For astronomical spectra, how precisely are the laboratory rest frequencies of the transitions used known, and how does the analysis treat unresolved isotopic and hyperfine structure and the isotopic abundances of the absorbing gas?

**Why it matters.** The shift sought corresponds to velocities of tens of metres per second to a few hundred, so laboratory frequencies must be known to better than that, or they limit the result. Isotopic components of some ions are separated by a large fraction of a kilometre per second; if the abundances in the absorbing gas differ from terrestrial values, the line centroids move and can imitate a change in α.

**Resolved by.** The source and uncertainty of every laboratory frequency, each well below the velocity precision of the astronomical measurement; isotopic and hyperfine components included in the line model; the result recalculated with plausible non-terrestrial isotopic abundances, or transitions that are most affected by isotopic structure shown to be excluded or to make no difference.

**Benchmark.** [4], [6]

## 3. Wavelength calibration of astronomical spectra

**Question.** How was the wavelength scale of each spectrum calibrated (lamp exposures taken when and through which light path, laser frequency comb, iodine cell), and was it checked for distortions over long wavelength ranges and within echelle orders, for example by comparing spectra of solar-type objects with a reference solar spectrum?

**Why it matters.** Transitions with different sensitivities to α or μ fall at different wavelengths, so a distortion of the wavelength scale that grows with wavelength shifts them in a way that mimics a change in the constant. Calibration lamp light can follow a different path through the spectrograph from the light of a point-like target, and distortions of a few hundred metres per second over a thousand ångström have been found in archival spectra from high-resolution spectrographs. Such distortions differ between instruments and observing epochs.

**Resolved by.** Calibration exposures taken with each science exposure without moving the instrument; a measurement of long-range and intra-order distortions for the same instrument and epoch, such as a comparison of asteroid or solar-twin spectra with a reference solar spectrum, or calibration with a laser frequency comb; the result corrected for the measured distortion, or the distortion included in the uncertainty, with the size of the correction stated.

**Benchmark.** [3], [6], [7]

## 4. Line-profile modelling and co-location of the transitions

**Question.** How was the velocity structure of the absorption modelled (number of components, how components were added, whether all transitions share the same component redshifts), how were blends with unrelated lines treated, and what is the evidence that the transitions compared arise in the same gas?

**Why it matters.** Most methods assume that the different transitions or species trace gas with the same velocity structure. Species that sit in different parts of a cloud, or have different ionisation, can have velocity offsets of up to about ten kilometres per second, which act as a random noise or a spurious signal in the inferred constant. Unresolved velocity components, saturated lines and blends with forest or other foreground lines all shift fitted line centres.

**Resolved by.** A stated procedure for choosing the number of components, applied in the same way to all systems; fits with and without the parameter for the varying constant, and residuals shown for each transition; blended regions identified and excluded or modelled; transitions chosen from one ion or species, or from species with similar ionisation potentials, or an estimate of the velocity offset between species included in the uncertainty.

**Benchmark.** [1], [6], [8]

## 5. Interpreting clock comparisons as a drift

**Question.** For atomic clock comparisons, which frequency ratios were measured over what span of time, what time dependence was fitted (linear drift, annual modulation with the solar gravitational potential, oscillation), and how were constraints on separate constants obtained from them?

**Why it matters.** A clock comparison gives the time dependence of a frequency ratio over the measurement period only, and the constraint on any one constant depends on the sensitivity difference of the pair. A single ratio constrains one combination of constants, so separating α from μ or from nuclear quantities needs several ratios with different sensitivities fitted together. Microwave hyperfine clocks depend on nuclear magnetic moments, and translating them into quark masses or other parameters needs a nuclear model whose choice changes the result substantially.

**Resolved by.** The time series of each ratio shown with the fitted model and the span of the data; the model for the time dependence and, for a search for a coupling to the gravitational potential, the variation in potential over the data set stated; a joint fit of several ratios with the matrix of sensitivities shown; any nuclear model used to interpret hyperfine clocks named, and its effect on the result stated.

**Benchmark.** [1], [2]

## 6. Reactor modelling for the Oklo and similar natural records

**Question.** For constraints from the Oklo natural reactor, which neutron spectrum, temperature and reactor geometry were assumed when converting the measured isotope ratios into an effective cross section, how were they constrained by independent data, and how does the analysis deal with more than one solution for the resonance shift?

**Why it matters.** The constraint rests on how much the energy of a low-lying neutron resonance could have shifted, which is inferred from an effective capture cross section that depends strongly on the assumed neutron spectrum and temperature. Analyses with different spectra, for example with and without an epithermal tail, have given different results. The relation between cross section and resonance shift usually has two solutions, and one of them corresponds to a non-zero shift.

**Resolved by.** A reactor model whose spectrum is checked against measured spectral indices or other isotope data, with temperature and composition stated; the cross section and the resonance shift given across the plausible temperature range; both solutions reported and any argument for excluding one shown with the data it uses; samples whose contamination and history are described.

**Benchmark.** [1], [5]

## 7. Assumptions behind a result for a single constant

**Question.** When a result is quoted for α alone, or for μ alone, what assumption about the other constants was made (that only one varies, or a relation from a unification model), and how would the result change under other assumptions?

**Why it matters.** Many probes are sensitive to several constants at once, including nuclear quantities whose dependence on α and quark masses is poorly known. Translating a measured shift into a value for one constant requires holding the others fixed or relating them through a model, and the coefficients relating changes in α and μ differ widely between models. A bound that is tight under one assumption can be much weaker under another.

**Resolved by.** The assumption stated explicitly next to the quoted value; the result given for the combination actually measured as well as for any single constant derived from it; for model-dependent conversions, the model and its coefficients named and results shown for more than one choice.

**Benchmark.** [1], [5], [7]

## 8. Combining probes and testing for spatial variation

**Question.** When results from different probes, instruments or epochs are combined, or a dependence on redshift or a dipole across the sky is fitted, what model of the time and space dependence links them, how are instrument-dependent systematic errors handled, and how well does the sample cover redshift and sky?

**Why it matters.** Clocks, the Oklo reactor, quasar spectra and the cosmic microwave background probe different epochs and environments, so a single constraint from all of them needs a model for how the constants evolve. Calibration distortions differ between spectrographs and epochs and could correlate with sky position through observing practice, and a sample that covers a narrow band of sky cannot fix the direction of a dipole. When the precision and the redshift coverage are limited, a pure spatial dipole and a dipole with an added redshift dependence can fit the data about equally well.

**Resolved by.** The model used to connect the probes stated, with results shown for each probe separately; instrument-specific calibration errors corrected or included for each data set, with a test of whether the fit changes when one instrument is left out; a map of the sky and redshift coverage; comparison of alternative models for the spatial and redshift dependence, with the significance reported for each.

**Benchmark.** [3], [6], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J.-P. Uzan, Varying constants, gravitation and cosmology, Living Rev. Relativ. 14, 2 (2011); read as arXiv:1009.5514 | doi:10.12942/lrr-2011-2 |
| 2 | M. S. Safronova et al., Search for new physics with atoms and molecules, Rev. Mod. Phys. 90, 025008 (2018); read as arXiv:1710.01833 | doi:10.1103/RevModPhys.90.025008 |
| 3 | J. B. Whitmore and M. T. Murphy, Impact of instrumental systematic errors on fine-structure constant measurements with quasar spectra, Mon. Not. R. Astron. Soc. 447, 446 (2015, published online 2014); read as arXiv:1409.4467 | doi:10.1093/mnras/stu2420 |
| 4 | M. T. Murphy and J. C. Berengut, Laboratory atomic transition data for precise optical quasar absorption spectroscopy, Mon. Not. R. Astron. Soc. 438, 388 (2014, published online 2013); read as arXiv:1311.2949 | doi:10.1093/mnras/stt2204 |
| 5 | C. R. Gould et al., Time-variability of alpha from realistic models of Oklo reactors, Phys. Rev. C 74, 024607 (2006); read as arXiv:nucl-ex/0701019 | doi:10.1103/PhysRevC.74.024607 |
| 6 | W. Ubachs et al., Colloquium: Search for a drifting proton-electron mass ratio from H2, Rev. Mod. Phys. 88, 021003 (2016); read as arXiv:1511.04476 | doi:10.1103/RevModPhys.88.021003 |
| 7 | C. J. A. P. Martins, The status of varying constants: a review of the physics, searches and implications, Rep. Prog. Phys. 80, 126902 (2017); read as arXiv:1709.02923 | doi:10.1088/1361-6633/aa860e |
| 8 | S. A. Levshakov et al., A new approach for testing variations of fundamental constants over cosmic epochs using FIR fine-structure lines, Astron. Astrophys. 479, 719 (2008); read as arXiv:0712.2890 | doi:10.1051/0004-6361:20079116 |
