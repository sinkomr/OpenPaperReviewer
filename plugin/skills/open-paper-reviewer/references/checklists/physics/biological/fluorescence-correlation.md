---
id: T-FLUORESCENCE-CORRELATION
name: Fluorescence correlation spectroscopy and diffusion
type: technique
field: physics/biological
applies_when: the paper reports diffusion coefficients, mobilities, concentrations or binding from fluorescence correlation or cross-correlation spectroscopy or fluorescence recovery after photobleaching, or attributes slow or anomalous diffusion in cells to binding or crowding; single-particle tracking has its own card
version: "0.1"
---

# Fluorescence correlation spectroscopy and diffusion

## 1. Calibration of the observation volume

**Question.** How were the size and shape of the observation volume determined (reference dye and the diffusion coefficient and temperature assumed for it, bead scans, or a calibration-free method), and were the calibration and the sample measured under the same optical conditions: coverslip, refractive index of the medium, depth, pinhole and alignment?

**Why it matters.** Single-focus FCS returns a diffusion time, and converting it to a diffusion coefficient or a concentration needs the size of the observation volume, so most measurements are relative to a reference. The volume often departs from the assumed three-dimensional Gaussian and changes with coverslip thickness, refractive-index mismatch, pinhole size, aberrations and saturation, which shifts diffusion times and can add apparent components. A calibration in water does not automatically carry over to a cell or a gel.

**Resolved by.** The reference dye, the literature value of its diffusion coefficient and the temperature stated; the beam waist and structure parameter reported; the calibration repeated on the day under matching conditions (same coverslip, correction collar and depth); where absolute values matter, a check by an independent route such as a dilution series, bead scans, dual-focus or scanning FCS.

**Benchmark.** [1], [2], [3], [4], [5], [6]

## 2. Excitation power, saturation, photobleaching and background

**Question.** Does the paper give the excitation power at the sample and show that the diffusion time, the number of molecules and the molecular brightness do not change with power over the range used, does it check for photobleaching during the measurement, and does it correct the correlation amplitude for uncorrelated background before deriving concentrations?

**Why it matters.** Optical saturation changes the effective observation volume and the amplitude and shape of the correlation curve, so FCS results depend on excitation power and accurate diffusion coefficients become hard to obtain. Photobleaching distorts the intensity trace and the correlation amplitude, and in a small compartment it depletes the pool of fluorophores. Uncorrelated background such as autofluorescence lowers the correlation amplitude and so inflates the apparent number of molecules.

**Resolved by.** The power at the sample stated for calibration and sample alike; a power series showing that diffusion time and molecule number are independent of power at the level used, or a saturation correction calibrated from count rate against power; intensity traces shown stable over each measurement; bleaching corrected or shown to be negligible; background measured on unlabelled samples and corrected for in concentrations and brightness.

**Benchmark.** [3], [6], [7], [8], [9]

## 3. Photophysics in the correlation curve

**Question.** Which terms besides translational diffusion does the fit model contain (triplet, blinking, protonation), how were their amplitudes and relaxation times constrained, and are they shown to be separated in time from the diffusion component?

**Why it matters.** Triplet transitions and other dark states make fluorophores blink and add fast relaxation terms to the correlation curve; in fluorescent proteins, protonation of the chromophore adds pH-dependent blinking on tens to hundreds of microseconds with a large dark fraction at low pH. Left out of the model, or absorbed into a free anomalous exponent or an extra diffusion component, these terms bias the diffusion time and the concentration.

**Resolved by.** The full fit function written out; blinking terms included, with their relaxation times compared with the diffusion time; their dependence on excitation power or pH checked; residuals shown across the full range of lag times.

**Benchmark.** [8], [10], [11]

## 4. Normal, anomalous or multi-component models in FCS

**Question.** When a correlation curve is fitted with an anomalous exponent or with several diffusing components, does the paper compare the alternative models, show that the lag-time range is wide enough to tell them apart, and test the choice independently, for example by varying the size of the observation volume?

**Why it matters.** An apparent exponent below one can also come from a mixture of species with different diffusion coefficients, from an observation volume that is not Gaussian, or from drift and other artefacts, and different models can fit the same curve about equally well while giving very different parameters. Slow anomalous transport can be measured reliably only from data that span several decades of time.

**Resolved by.** Fits and residuals for normal, two-component and anomalous models shown side by side; the lag-time range stated; measurements at several beam waists giving a diffusion law (diffusion time against the area of the observation volume) consistent with the claimed mode of motion; the exponent not used to absorb drift or photophysics.

**Benchmark.** [1], [11], [12], [13]

## 5. Bleach geometry, timing and the recovery model in FRAP

**Question.** For diffusion or binding parameters from FRAP, does the paper report the bleach region and its measured profile, the bleach and imaging durations, the correction for bleaching during acquisition and the model fitted, and does it show that the system is in the regime the model assumes?

**Why it matters.** Finite bleach and scan times let molecules move during the bleach, and analyses that ignore this can substantially underestimate diffusion coefficients. FRAP models rest on different assumptions: diffusion contributes to many recoveries and can hide binding kinetics, and an incomplete recovery is easily confused with slow anomalous recovery unless the measurement runs long enough.

**Resolved by.** Bleach region size and shape with the measured post-bleach profile; normalisation and acquisition-bleaching corrections described; recovery followed to a plateau; the dependence on bleach-spot size tested to separate diffusion from binding; the model's assumptions stated and checked for self-consistency.

**Benchmark.** [11], [13], [14], [15], [16]

## 6. Binding and crowding as explanations for slow diffusion

**Question.** When slower or anomalous diffusion is attributed to binding, complex formation or crowding, does the paper measure a matched inert tracer or a binding-deficient variant, and are bound fractions and residence times checked with another technique or kinetic model?

**Why it matters.** Different kinetic models can fit the same FRAP or FCS data equally well while giving residence times that differ by an order of magnitude or more, and estimates for the same protein have differed between studies for technical reasons. Anomalous diffusion is not found everywhere in cells, and where it is attributed to crowding its degree depends on the tracer size and the protein concentration; in cross-correlation binding assays, spectral cross-talk, incomplete labelling and background change the apparent bound fraction.

**Resolved by.** Inert tracers of several sizes or a binding-deficient variant measured in the same cells; the kinetic model supported by independent data such as single-molecule residence times; bound fraction and residence time compared across techniques; for cross-correlation, cross-talk, degree of labelling and background measured and corrected.

**Benchmark.** [9], [13], [17], [18], [19]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. T. Hess and W. W. Webb, Focal volume optics and experimental artifacts in confocal fluorescence correlation spectroscopy, Biophys. J. 83, 2300 (2002) | doi:10.1016/S0006-3495(02)73990-8 |
| 2 | J. Enderlein et al., Performance of fluorescence correlation spectroscopy for measuring diffusion and concentration, ChemPhysChem 6, 2324 (2005) | doi:10.1002/cphc.200500414 |
| 3 | S. Rüttinger et al., Comparison and accuracy of methods to determine the confocal volume for quantitative fluorescence correlation spectroscopy, J. Microsc. 232, 343 (2008) | doi:10.1111/j.1365-2818.2008.02105.x |
| 4 | T. Dertinger et al., Two-focus fluorescence correlation spectroscopy: a new tool for accurate and absolute diffusion measurements, ChemPhysChem 8, 433 (2007) | doi:10.1002/cphc.200600638 |
| 5 | Z. Petrášek and P. Schwille, Precise measurement of diffusion coefficients using scanning fluorescence correlation spectroscopy, Biophys. J. 94, 1437 (2008) | doi:10.1529/biophysj.107.108811 |
| 6 | L. Yu et al., A comprehensive review of fluorescence correlation spectroscopy, Front. Phys. 9, 644450 (2021) | doi:10.3389/fphy.2021.644450 |
| 7 | I. Gregor et al., Optical saturation in fluorescence correlation spectroscopy under continuous-wave and pulsed excitation, ChemPhysChem 6, 164 (2005) | doi:10.1002/cphc.200400319 |
| 8 | L. M. Davis and G. Shen, Accounting for triplet and saturation effects in FCS measurements, Curr. Pharm. Biotechnol. 7, 287 (2006) | doi:10.2174/138920106777950843 |
| 9 | J. Ries et al., A comprehensive framework for fluorescence cross-correlation spectroscopy, New J. Phys. 12, 113009 (2010) | doi:10.1088/1367-2630/12/11/113009 |
| 10 | U. Haupts et al., Dynamics of fluorescence fluctuations in green fluorescent protein observed by fluorescence correlation spectroscopy, Proc. Natl. Acad. Sci. USA 95, 13573 (1998) | doi:10.1073/pnas.95.23.13573 |
| 11 | F. Höfling and T. Franosch, Anomalous transport in the crowded world of biological cells, Rep. Prog. Phys. 76, 046602 (2013); read as arXiv:1301.6990 | doi:10.1088/0034-4885/76/4/046602 |
| 12 | L. Wawrezinieck et al., Fluorescence correlation spectroscopy diffusion laws to probe the submicron cell membrane organization, Biophys. J. 89, 4029 (2005) | doi:10.1529/biophysj.105.067959 |
| 13 | D. Mazza et al., A benchmark for chromatin binding measurements in live cells, Nucleic Acids Res. 40, e119 (2012) | doi:10.1093/nar/gks701 |
| 14 | M. Weiss, Challenges and artifacts in quantitative photobleaching experiments, Traffic 5, 662 (2004) | doi:10.1111/j.1600-0854.2004.00215.x |
| 15 | B. L. Sprague et al., Analysis of binding reactions by fluorescence recovery after photobleaching, Biophys. J. 86, 3473 (2004) | doi:10.1529/biophysj.103.026765 |
| 16 | N. Lorén et al., Fluorescence recovery after photobleaching in material and life sciences: putting theory into practice, Q. Rev. Biophys. 48, 323 (2015) | doi:10.1017/S0033583515000013 |
| 17 | F. Mueller et al., FRAP and kinetic modeling in the analysis of nuclear protein dynamics: what do we really know?, Curr. Opin. Cell Biol. 22, 403 (2010) | doi:10.1016/j.ceb.2010.03.002 |
| 18 | J. A. Dix and A. S. Verkman, Crowding effects on diffusion in solutions and cells, Annu. Rev. Biophys. 37, 247 (2008) | doi:10.1146/annurev.biophys.37.032807.125824 |
| 19 | M. Weiss et al., Anomalous subdiffusion is a measure for cytoplasmic crowding in living cells, Biophys. J. 87, 3518 (2004) | doi:10.1529/biophysj.104.044263 |
