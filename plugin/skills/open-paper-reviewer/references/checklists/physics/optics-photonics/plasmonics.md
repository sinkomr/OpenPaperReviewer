---
id: T-PLASMONICS
name: Plasmonics and nanophotonics
type: technique
field: physics/optics-photonics
applies_when: the paper reports surface-enhanced Raman or other near-field enhancement factors, simulated plasmonic field enhancement, single-molecule detection by enhanced spectroscopy, plasmonic heating or hot-carrier effects, single-nanoparticle optical spectra, or near-field optical microscopy images or spectra
version: "0.1"
---

# Plasmonics and nanophotonics

## 1. Definition and calculation of the enhancement factor

**Question.** Which definition of the SERS enhancement factor does the paper use, how were the number of molecules contributing to the SERS and to the reference signal estimated, and was the reference (non-enhanced) Raman signal measured for the same molecule, vibrational mode and instrument settings?

**Why it matters.** Several definitions of the enhancement factor are in use, and they measure different things, so values quoted under different definitions cannot be compared. The substrate enhancement factor needs the number of molecules in each measurement, which depends on surface coverage, orientation and the active area, and these are hard to know for colloids and rough films. A reference spectrum taken from a concentrated solution or solid, for another mode or with different collection settings, changes the result.

**Resolved by.** The definition stated with its formula; the surface coverage, active area and probe volume given with how each was found; the reference Raman cross-section measured for the same mode, excitation wavelength and instrument settings; for comparisons between substrates, the same probe and conditions, or a relative enhancement against a stated standard.

**Benchmark.** [1], [2]

## 2. Hot spots and the spread of enhancement

**Question.** Does the paper say whether a quoted enhancement is an average over the substrate or the value at the best sites, and does it show how the signal varies across the substrate and between batches?

**Why it matters.** SERS signals come mostly from a small fraction of sites with the highest fields, and the distribution of site enhancements can span many orders of magnitude, so an average and a maximum describe different things. A spectrum from one chosen spot, or a figure built from the brightest pixels, does not show what the substrate gives in general. Electron microscopy images alone predict the enhancement poorly.

**Resolved by.** The enhancement labelled as average or local, with the area over which it was measured; maps or histograms of signal over many spots and over several batches, with the spread stated; correlative measurements (electron microscopy, dark-field and SERS on the same structures) where specific hot spots are claimed.

**Benchmark.** [1], [3]

## 3. Single-molecule claims

**Question.** When the paper claims single-molecule sensitivity, what evidence shows that each event comes from one molecule, rather than relying only on a low bulk concentration?

**Why it matters.** At very low concentration, the number of molecules actually present at the hot spots in the probed volume is uncertain, so dilution alone does not show that a signal comes from one molecule. The enhancement needed for single-molecule detection is often quoted far higher than measurements support, which can inflate claims built on it.

**Resolved by.** A statistical test designed for the purpose, such as two distinguishable analytes or isotopologues at comparable concentration, with the counts of events showing one species, the other, or both; the statistics of events reported over many spectra; any single-molecule enhancement factor derived from such data rather than from concentration estimates.

**Benchmark.** [2], [4], [5]

## 4. Choice of analyte and non-electromagnetic contributions

**Question.** Is the probe molecule resonant with the excitation light or strongly absorbing, does it bind to the metal, and does the paper consider contributions other than field enhancement, such as molecular resonance, chemical enhancement, shifted absorption on adsorption or light-driven reactions?

**Why it matters.** Resonant dyes give very strong signals because of their own resonance Raman cross-section, and that cross-section can change when they adsorb, so the apparent enhancement mixes molecular and plasmonic effects. Chemical enhancement through charge transfer adds a further factor that depends on the molecule and the metal. Light can also drive reactions at the metal surface that create new species and new bands.

**Resolved by.** A non-resonant, strongly binding probe for quoted enhancement factors, or a correction for molecular resonance; comparison of probes that bind strongly and weakly; the absorption of the adsorbed molecule considered; spectra checked over time and power for new bands or changes that indicate photochemistry.

**Benchmark.** [1], [5]

## 5. Calculated field enhancement and material data

**Question.** For field enhancements or spectra obtained by simulation, does the paper state the dielectric function used and whether it matches the deposited metal, the gap size and the rounding of edges in the model, and whether effects beyond the classical local model matter at the smallest gaps?

**Why it matters.** The fourth-power estimate of SERS enhancement from the local field is only good to about an order of magnitude. Classical local models predict enhancement that grows without limit as a gap narrows, while nonlocal screening and electron tunnelling reduce it in gaps of about a nanometre or less, and the result depends on gap shape, which is hard to measure. The losses of a real film depend on grain size, roughness and deposition conditions and can differ strongly from tabulated optical constants.

**Resolved by.** The dielectric data stated, measured on the paper's own films (for example by ellipsometry) or justified for them; deposition conditions, roughness and grain structure reported; geometry in the model taken from microscopy of the measured structures, with the sensitivity of the result to gap size and edge rounding shown; nonlocal or quantum corrections considered for gaps of about a nanometre or less; calculated and measured spectra compared before calculated enhancement is used.

**Benchmark.** [5], [6], [7]

## 6. Heating and hot-carrier claims

**Question.** When the paper attributes an effect to hot carriers or another non-thermal plasmonic mechanism, how was the local temperature measured or bounded, and which experiments separate a thermal from a non-thermal origin?

**Why it matters.** Absorbed light heats plasmonic structures, and the temperature rise of an illuminated sample is often far larger than single-particle estimates suggest, because heat from many particles adds up. A thermocouple away from the illuminated area can greatly underestimate the temperature. Over a narrow range of light power, an exponential (Arrhenius) thermal rate can look linear, so a linear dependence alone does not exclude heating.

**Resolved by.** The temperature at the reacting or measured region measured, for example by calibrated thermometry close to the illuminated area or temperature microscopy, not inferred from a single-particle formula; power dependence over a wide range; tests that vary beam size, wavelength at matched absorption, or time response; a comparison with the same system heated in the dark to the measured temperature.

**Benchmark.** [8]

## 7. Single-particle optical spectroscopy

**Question.** For spectra attributed to single nanoparticles, does the paper show that each spot is one particle of the stated shape, and how were the spectra corrected for lamp, background and substrate?

**Why it matters.** Particles and small clusters closer together than the diffraction limit look the same in an optical image, so a bright spot is not proof of a single particle, and an aggregate changes the spectrum. Dark-field spectra need background subtraction and division by a white-light reference, and electron-beam imaging before the optical measurement can alter the particle. Ensemble spectra are broadened by the spread of sizes and shapes and do not give the intrinsic linewidth.

**Resolved by.** Correlated electron or probe microscopy of the same particles, with optical measurements taken first or with low electron dose; the spectral correction procedure and substrate stated; linewidths from single particles fitted and compared with ensemble spectra; for small particles, absorption-based methods where scattering is too weak.

**Benchmark.** [9]

## 8. Artefacts in near-field optical microscopy

**Question.** How does the paper show that near-field optical contrast reflects the sample's optical properties and not the probe's path over topography, background scattering, or reflections from the surrounding sample?

**Why it matters.** When the tip-sample distance is held by a feedback loop, the optical image can mainly record the probe's trajectory over topography rather than the optical response. In s-SNOM, light scattered from the tip shaft and sample adds a background that is reduced by demodulating at higher harmonics of the tip oscillation and by interferometric detection, and reflections from nearby surfaces can still change amplitude and phase. Normalising to a reference such as gold or silicon removes far-field terms only when sample and reference reflect similarly.

**Resolved by.** Topography shown next to every optical image, with contrast that does not simply follow height; the detection scheme, demodulation order and tapping amplitude stated; contrast compared between harmonic orders, or harmonic ratios used; the reference material and its suitability for the sample stated; edges and nearby structures considered as sources of interference fringes.

**Benchmark.** [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. E. J. Bell et al., Towards reliable and quantitative surface-enhanced Raman scattering (SERS): from key parameters to good analytical practice, Angew. Chem. Int. Ed. 59, 5454 (2020) | doi:10.1002/anie.201908154 |
| 2 | E. C. Le Ru et al., Surface enhanced Raman scattering enhancement factors: a comprehensive study, J. Phys. Chem. C 111, 13794 (2007) | doi:10.1021/jp0687908 |
| 3 | Y. Fang et al., Measurement of the distribution of site enhancements in surface-enhanced Raman scattering, Science 321, 388 (2008) | doi:10.1126/science.1159499 |
| 4 | E. C. Le Ru et al., Proof of single-molecule sensitivity in surface enhanced Raman scattering (SERS) by means of a two-analyte technique, J. Phys. Chem. B 110, 1944 (2006) | doi:10.1021/jp054732v |
| 5 | J. Langer et al., Present and future of surface-enhanced Raman scattering, ACS Nano 14, 28 (2020) | doi:10.1021/acsnano.9b04224 |
| 6 | W. Zhu et al., Quantum mechanical effects in plasmonic structures with subnanometre gaps, Nat. Commun. 7, 11495 (2016) | doi:10.1038/ncomms11495 |
| 7 | K. M. McPeak et al., Plasmonic films can easily be better: rules and recipes, ACS Photonics 2, 326 (2015) | doi:10.1021/ph5004237 |
| 8 | G. Baffou et al., Simple experimental procedures to distinguish photothermal from hot-carrier processes in plasmonics, Light Sci. Appl. 9, 108 (2020) | doi:10.1038/s41377-020-00345-0 |
| 9 | J. Olson et al., Optical characterization of single plasmonic nanoparticles, Chem. Soc. Rev. 44, 40 (2015) | doi:10.1039/c4cs00131a |
| 10 | B. Hecht et al., Facts and artifacts in near-field optical microscopy, J. Appl. Phys. 81, 2492 (1997) | doi:10.1063/1.363956 |
| 11 | L. Mester et al., High-fidelity nano-FTIR spectroscopy by on-pixel normalization of signal harmonics, Nanophotonics 11, 377 (2022) | doi:10.1515/nanoph-2021-0565 |
