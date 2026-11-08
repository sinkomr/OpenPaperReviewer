---
id: CL-MOLECULAR-DETECTIONS
name: Claims of molecular detections in space and planetary atmospheres
type: claim
field: physics/astrophysics
applies_when: the paper claims that a molecule is detected, tentatively detected or newly identified in an interstellar, circumstellar, cometary, planetary or exoplanet spectrum, or bases such a claim on line assignments, stacked or cross-correlated lines, or comparison of models with and without the molecule
version: "0.1"
---

# Claims of molecular detections in space and planetary atmospheres

## 1. Rest frequencies and laboratory data

**Question.** Which laboratory measurements or line lists give the rest frequencies or wavelengths of the assigned lines, are those values measured or predicted, and, if predicted, are the stated uncertainties small compared with the line width and the spacing of nearby lines?

**Why it matters.** An assignment is only as good as the rest frequency it is matched to. Predictions extrapolated beyond the measured range of a molecule's spectrum are unreliable, especially for molecules with internal rotation, and older catalogue predictions can fit observed spectra clearly worse than newer ones. At high spectral resolution, small errors in line positions in a template can remove a real match or create a false one.

**Resolved by.** The catalogue or line list named for each molecule, with its version; the assigned lines shown to lie within the measured range or to have predicted uncertainties well below the line width; where the laboratory data are uncertain, new laboratory measurements or a stated allowance in the assignment; for cross-correlation templates, the line list and its known accuracy at the relevant temperature stated.

**Benchmark.** [1], [2], [5]

## 2. Velocity and line width shared by all lines

**Question.** Do all the assigned lines give the same velocity and line width within their uncertainties, and are these consistent with other molecules in the same target?

**Why it matters.** A line from the claimed molecule must appear at the target's velocity. Velocity differences between lines should follow the target's kinematics, not scatter randomly with frequency or energy, which is what chance coincidences produce.

**Resolved by.** A table of the fitted velocity and width for each assigned line, compared with each other and with well-established molecules in the same target; any outlying lines discussed, not silently dropped.

**Benchmark.** [1], [2]

## 3. Signal from the target, not the instrument, the Earth's atmosphere or the star

**Question.** Could the assigned features come from the instrument (lines from the image sideband, spurious spikes or other artefacts), from residual lines of the Earth's atmosphere, or from the host star, and for a planet, does the signal appear at the planet's expected orbital velocity and not at a velocity tied to the Earth or the star?

**Why it matters.** A receiver passes a small fraction of its image band, so a strong line there can appear as a weak feature in the observed band, and spectrometers can produce spikes at fixed channels. Lines from the Earth's atmosphere are stationary while a planet's lines move with its orbit, so a signal at an offset velocity may not come from the planet. In transmission spectra, unocculted starspots and faculae can add or hide features that may be taken for absorption in the planet's atmosphere.

**Resolved by.** The image-band frequency of each assigned line checked for strong lines, and channels with known instrumental artefacts flagged; telluric and stellar lines removed, with the residuals shown; for planets, a map of signal against orbital and systemic velocity showing the peak at the expected values, with any offset explained; for transmission spectra, the stellar contribution from spots and faculae modelled or bounded.

**Benchmark.** [3], [5], [12]

## 4. Blending, line confusion and spectral resolution

**Question.** Are the assigned lines resolved from their neighbours at the spectral resolution used, and was the whole spectrum modelled with all known molecules (including isotopologues and vibrationally excited states) so that blends with other species are accounted for?

**Why it matters.** In line-rich spectra lines fill most channels, so a feature at the right frequency is often a coincidence or a blend with a line of a more common molecule. Modelling lines one at a time hides such blends. At low resolution, the bands of different molecules overlap, so a feature attributed to one molecule may come wholly or partly from another.

**Resolved by.** The spectral resolution and channel spacing stated and compared with the line widths; a synthetic spectrum including all identified species overlaid on the data around each assigned line; lines that are blended marked and either excluded or modelled; the fraction of channels free of emission reported for line-rich sources; at low resolution, the overlapping species named and included in the models compared.

**Benchmark.** [1], [2], [3], [5], [7]

## 5. Every predicted line present

**Question.** Using the column density and excitation the paper derives, which other lines of the molecule are predicted within the observed range, are all lines predicted above the noise actually seen, and how many lines that are not blended support the claim?

**Why it matters.** One or two lines at the right frequencies do not identify a molecule when the spectrum is dense. A model that predicts detectable lines that are absent counts strongly against the assignment. The number of independent, well-isolated lines needed for a secure identification grows with the density of lines in the spectrum.

**Resolved by.** A figure showing every transition predicted above a stated level, detected or not, with the model overlaid; no predicted line missing without an explanation such as a blend or a known artefact; the number of clean lines that support the detection stated; for a first detection, several transitions that are well separated in frequency and energy.

**Benchmark.** [1], [2], [3]

## 6. Relative intensities and excitation

**Question.** Are the relative strengths of the assigned lines consistent with a single physically reasonable excitation model, with the source size relative to the beam, optical depth, continuum opacity and background radiation taken into account?

**Why it matters.** The line ratios of a molecule are fixed by its line strengths, energies and excitation, so assignments whose intensities do not follow a plausible model are unlikely to be correct. A rotational temperature diagram can produce a convincing straight line from misassigned features, so it does not by itself confirm an identification. Beam dilution, optically thick lines and continuum absorption change the intensities and the column density derived.

**Resolved by.** The excitation model stated (local thermodynamic equilibrium or not, temperature, column density, source size and beam), with its predicted intensities compared line by line with the data; optical depths estimated, using rarer isotopologues where the main lines are thick; any population diagram used to derive quantities after the identification has been established, not to establish it.

**Benchmark.** [1], [2]

## 7. Continuum, baseline and detrending

**Question.** How were the continuum, the spectral baseline or the time-varying stellar and telluric signal removed (which line-free channels, what order of fit, how many detrending components), and does the claimed feature survive reasonable changes to these choices?

**Why it matters.** Baseline ripples left after a fit can rise above the noise and look like lines, while a fit that takes the wings of broad lines as baseline creates negative bowls and cuts flux. In line-rich spectra few channels are free of lines, so the continuum level is hard to set and errors pass into line strengths. In high-resolution planetary spectra, tuning the detrending to maximise the signal at the expected velocity can create detections from noise.

**Resolved by.** The line-free channels, fitting order and method stated, with low orders preferred unless justified; the spectrum shown before and after baseline or continuum removal over a range wide enough to judge ripples; the feature's strength reported for several reasonable baseline or detrending choices; detrending parameters chosen without reference to the signal at the expected velocity, for example by optimising the recovery of an injected signal.

**Benchmark.** [3], [4], [8], [9], [10], [11]

## 8. Significance of weak, stacked or model-compared detections

**Question.** For a detection that rests on stacked lines, a matched filter, cross-correlation or comparison of models with and without the molecule, how was the significance computed, over what range of velocities, frequencies or alternative models was the noise or the comparison taken, and what tests show that the signal is not produced by a few lines, by interlopers or by the choice of alternatives?

**Why it matters.** Stacking and cross-correlation can raise a signal to formal significance when no single line is detected, so the result depends on how the noise is estimated and which lines are included. Estimating noise over a narrow velocity range can inflate significance, and peaks of about three standard deviations appear elsewhere in such maps by chance. A Bayes factor converted to standard deviations depends on the priors and on which alternative models were compared, and overlapping features of other molecules can absorb or mimic the signal.

**Resolved by.** The significance method stated, with the noise taken from a wide region away from the signal; the full map or response shown, not only the peak; tests in which subsets of lines are used separately, or the catalogue frequencies are perturbed, and the signal behaves as expected; interloping lines removed before stacking; for model comparison, the alternatives listed, including other molecules with overlapping features, the priors stated, and the conversion to standard deviations explained; significance shown to be robust to oversampling of the velocity grid and confirmed with more than one detrending choice or night.

**Benchmark.** [5], [6], [7], [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | L. E. Snyder et al., A rigorous attempt to verify interstellar glycine, Astrophys. J. 619, 914 (2005); read as arXiv:astro-ph/0410335 | doi:10.1086/426677 |
| 2 | J. K. Jørgensen et al., Astrochemistry during the formation of stars, Annu. Rev. Astron. Astrophys. 58, 727 (2020); read as arXiv:2006.07071 | doi:10.1146/annurev-astro-032620-021927 |
| 3 | A. Belloche et al., Complex organic molecules in the interstellar medium: IRAM 30 m line survey of Sagittarius B2(N) and (M), Astron. Astrophys. 559, A47 (2013); read as arXiv:1308.5062 | doi:10.1051/0004-6361/201321096 |
| 4 | Á. Sánchez-Monge et al., STATCONT: a statistical continuum level determination method for line-rich sources, Astron. Astrophys. 609, A101 (2018); read as arXiv:1710.02419 | doi:10.1051/0004-6361/201730425 |
| 5 | J. L. Birkby, Exoplanet atmospheres at high spectral resolution, review chapter, arXiv:1806.04617 (2018) | doi:10.48550/arXiv.1806.04617 |
| 6 | R. A. Loomis et al., An investigation of spectral line stacking techniques and application to the detection of HC11N, Nat. Astron. 5, 188 (2021); read as arXiv:2009.11900 | doi:10.1038/s41550-020-01261-4 |
| 7 | B. Benneke and S. Seager, How to distinguish between cloudy mini-Neptunes and water/volatile-dominated super-Earths, Astrophys. J. 778, 153 (2013); read as arXiv:1306.6325 | doi:10.1088/0004-637X/778/2/153 |
| 8 | CASA Team, CASA documentation, UV manipulation: continuum subtraction with uvcontsub, NRAO (accessed 2026) | https://casadocs.readthedocs.io/en/stable/notebooks/uv_manipulation.html |
| 9 | C. R. Purcell et al., The H2O Southern Galactic Plane Survey: NH3 (1,1) and (2,2) catalogues, Mon. Not. R. Astron. Soc. 426, 1972 (2012); read as arXiv:1207.6159 | doi:10.1111/j.1365-2966.2012.21800.x |
| 10 | C. J. Cheverall et al., Robustness measures for molecular detections using high-resolution transmission spectroscopy of exoplanets, Mon. Not. R. Astron. Soc. 522, 661 (2023); read as arXiv:2303.01496 | doi:10.1093/mnras/stad648 |
| 11 | S. H. C. Cabot et al., On the robustness of analysis techniques for molecular detections using high resolution exoplanet spectroscopy, Mon. Not. R. Astron. Soc. 482, 4422 (2019; online 2018) | doi:10.1093/mnras/sty2994 |
| 12 | B. V. Rackham et al., The transit light source effect: false spectral features and incorrect densities for M-dwarf transiting planets, Astrophys. J. 853, 122 (2018); read as arXiv:1711.05691 | doi:10.3847/1538-4357/aaa08c |
