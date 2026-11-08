---
id: T-ATOMIC-CLOCKS
name: Atomic clocks and frequency metrology
type: technique
field: physics/amo
applies_when: the paper reports the frequency, systematic uncertainty or instability of an optical or microwave atomic clock, a comparison between clocks or a frequency ratio, or bases a claim about fundamental constants, relativity or geodesy on clock measurements
version: "0.1"
---

# Atomic clocks and frequency metrology

## 1. Completeness of the systematic uncertainty budget

**Question.** Does the paper give a table of every systematic shift with its correction and uncertainty, and say for each one whether it was measured on this apparatus (and how) or calculated from atomic data and a model?

**Why it matters.** The stated accuracy of a clock is only as good as its budget: a shift that is left out, or estimated from a model with an optimistic coefficient, leads directly to an understated uncertainty. Some of the effects that matter are specific to the apparatus, such as charge on in-vacuum optics, phase chirps from optical or microwave switches, servo errors and microwave leakage, and these are easy to leave out.

**Resolved by.** A full budget table with the sum of corrections and the combined uncertainty; each shift measured where possible by interleaving operation at two settings of the relevant parameter, with the extrapolation and its uncertainty stated; the source of every calculated coefficient cited; tests for apparatus-specific effects reported, for example frequency changes with switches or microwaves toggled and checks for perturbations synchronous with the clock cycle.

**Benchmark.** [1], [2]

## 2. Blackbody radiation shift

**Question.** How was the effective temperature of the thermal radiation at the atoms determined (number, calibration and placement of sensors, temperature differences across the chamber, heated parts), and which polarisability and dynamic correction values were used, with what uncertainties?

**Why it matters.** At room temperature the blackbody shift is of order 10⁻¹⁵ for neutral-atom lattice clocks, so a 1 K error in the effective temperature gives a frequency error of several parts in 10¹⁷. Radio-frequency heating of ion traps and differences in emissivity between materials matter: temperature differences of up to about 25 K have been seen between parts of one trap. The atomic coefficient carries its own uncertainty, which is separate from that of the temperature.

**Resolved by.** A thermal model of the chamber backed by calibrated sensors at several positions, ideally inside the vacuum; the spread of temperatures, viewports and hot components included in the uncertainty; the static polarisability and dynamic correction stated with their sources and uncertainties; where the claimed uncertainty demands it, a cryogenic or temperature-uniform enclosure, or a direct measurement of the shift against temperature.

**Benchmark.** [1], [2]

## 3. Shifts from magnetic, electric and light fields

**Question.** How were the first-order Zeeman shift and, for ions, the electric quadrupole shift cancelled (which transitions or field orientations were averaged), how was the field at the atoms calibrated for the quadratic Zeeman correction, and how were light shifts from the trapping or lattice light and from the probe laser measured?

**Why it matters.** The quadratic Zeeman correction is often the largest single correction in the budget, so the field calibration controls it. Averaging opposite Zeeman components or orthogonal field orientations cancels a shift only if the averaging is symmetric and the field orientations are accurate, to about a degree for a hundredfold suppression of the quadrupole shift. Lattice light shifts depend on the lattice frequency relative to the magic wavelength and include terms that are not linear in trap depth, so a model that is linear in trap depth can leave a residual shift.

**Resolved by.** The field determined from the splitting of the clock transition or of a field-sensitive transition, and monitored during the run; the averaging scheme stated, with checks that it is balanced; the lattice frequency stated relative to the measured magic wavelength, and the light shift measured over a range of trap depths with a model that includes the non-linear terms; probe light shifts measured against probe intensity or suppressed by a stated pulse scheme.

**Benchmark.** [1], [2]

## 4. Motion of the atoms: Doppler and time-dilation shifts

**Question.** How were the residual motion of the atoms and the shifts it causes evaluated: for ions, excess micromotion and secular motion; for lattice clocks, relative motion of lattice and probe; for fountains, the distributed cavity phase and microwave lensing?

**Why it matters.** Excess micromotion comes from stray electric fields that drift, so a compensation made once may not hold for the whole run, and in some ion clocks motional time dilation dominates the uncertainty. Vibration between the trap and the probe that is synchronised with the clock cycle produces a first-order Doppler shift that does not average away. In fountains a spatial phase variation of the cavity field acts as a residual first-order Doppler shift that depends on the launch tilt.

**Resolved by.** For ions, micromotion measured along three non-coplanar directions and repeated during the run, and the motional temperature measured; for lattice clocks, probe phase stabilised to the lattice or probing from opposite directions; for fountains, the distributed cavity phase shift evaluated by measurements of tilt sensitivity combined with calculation, and the lensing shift calculated with the apertures included.

**Benchmark.** [1], [2]

## 5. Density and collision shifts

**Question.** How was the shift from collisions between cold atoms measured (over what range of atom number or density, how the density ratio was determined, how it was extrapolated to zero density), and how were collisions with background gas bounded?

**Why it matters.** Cold-collision shifts are evaluated by measurement on the apparatus, because they depend on the density distribution and on details of the atomic interactions. Shifts have been seen even with fermions prepared in one spin state, where s-wave collisions are suppressed. An extrapolation to zero density is only as good as the knowledge of the density ratio between the settings and the assumption that the shift is linear in density.

**Resolved by.** Interleaved operation at high and low density with the density ratio measured, for example by a method that sets the ratio precisely; the coefficient and its uncertainty stated and scaled to the operating density; if a pre-measured coefficient is used, periodic checks that it still holds; the background-gas collision shift included in the budget, with the method used to bound it.

**Benchmark.** [1], [2]

## 6. Gravitational redshift

**Question.** For a comparison between clocks at different heights or sites, or a frequency referred to the SI second, does the paper state the gravity potential or height of each clock, the geodetic method and reference surface used, the resulting uncertainty, and whether tidal and other time-varying contributions were included?

**Why it matters.** A height difference of 1 m changes the frequency by about 10⁻¹⁶, so a 10⁻¹⁸ comparison needs heights to about a centimetre. Levelling errors grow with distance, national height systems differ by more than half a metre, and solid Earth tides change the frequency difference between distant clocks by up to about 10⁻¹⁶.

**Resolved by.** The gravity potential at each clock with its uncertainty, from levelling for nearby clocks or from GNSS (global navigation satellite system) positions combined with a gravimetric geoid model for distant ones; the reference potential stated; tides and other time-varying effects modelled where they matter; the redshift uncertainty smaller than, or included in, the comparison uncertainty.

**Benchmark.** [1], [2], [3]

## 7. Instability and the statistical uncertainty

**Question.** Which estimator was used for the instability (for example overlapping or modified Allan deviation), how were the frequency data taken (counter type and its averaging, drift removal), what error bars are given at long averaging times, and how is the statistical uncertainty of the final result derived from the instability?

**Why it matters.** Many high-resolution frequency counters average overlapping measurements, so applying the Allan variance formula to their output gives the modified Allan variance instead. At long averaging times few degrees of freedom remain, so the confidence interval is wide and hard to estimate. A comparison of two clocks gives only the sum of their variances, and extrapolating an inverse-square-root trend beyond the measured averaging time assumes white frequency noise without a floor or drift. In clocks with dead time between interrogations, local-oscillator noise is aliased into the result (the Dick effect).

**Resolved by.** The estimator and the counter's averaging method stated; the Allan deviation plotted with error bars based on the degrees of freedom for the identified noise type; any drift removal described; the instability of a single clock obtained from three or more clocks, for example by a three-cornered hat, or the assumption used stated; the statistical uncertainty taken from the instability at the total measurement time, with any extrapolation justified by the data; statistical and systematic uncertainties kept separate.

**Benchmark.** [1], [4], [5]

## 8. Clock comparisons and frequency ratios

**Question.** For a comparison or a frequency ratio, does the paper give the uncertainty of the link (fibre, satellite or transportable clock) and of the frequency comb, state which uncertainties are shared with other clocks or earlier measurements, and test its result against independent measurements of the same ratio or the recommended values?

**Why it matters.** A comparison validates the stated clock uncertainties only if the link contributes less, and satellite links are several orders of magnitude less precise than phase-coherent fibre links. Correlations from shared clocks, overlapping measurement periods or shared corrections are often not published; leaving them out gives some measurements too much weight and understates the uncertainty of combined values. Measurements of a ratio of unperturbed transitions should agree within their combined uncertainties, and disagreement points to an unrecognised systematic shift.

**Resolved by.** A link and comb uncertainty budget alongside the clock budgets; for an absolute frequency, the comb mode number and the signs of the offset and beat frequencies fixed by a stated test; correlations with other measurements stated or the covariances provided; the result compared with earlier independent measurements and with recommended values, with normalised deviations or a goodness-of-fit test; for clocks of the same species, the measured frequency difference consistent with zero within the combined uncertainty, and any disagreement reported and discussed.

**Benchmark.** [1], [2], [3], [6], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. D. Ludlow et al., Optical atomic clocks, Rev. Mod. Phys. 87, 637 (2015); read as preprint arXiv:1407.3493 | doi:10.1103/RevModPhys.87.637 |
| 2 | J. Guéna et al., Progress in atomic fountains at LNE-SYRTE, IEEE Trans. Ultrason. Ferroelectr. Freq. Control 59, 391 (2012); read as preprint arXiv:1204.3621 | doi:10.1109/TUFFC.2012.2208 |
| 3 | P. Delva et al., Chronometric geodesy: methods and applications, in Relativistic Geodesy, Fundamental Theories of Physics 196, Springer, pp. 25–85 (2019); read as preprint arXiv:1804.09506 | doi:10.1007/978-3-030-11500-5_2 |
| 4 | E. Rubiola, On the measurement of frequency and of its sample variance with high-resolution counters, Rev. Sci. Instrum. 76, 054703 (2005); read as preprint arXiv:physics/0411227 | doi:10.1063/1.1898203 |
| 5 | E. Lantz et al., KLTS: A rigorous method to compute the confidence intervals for the Three-Cornered Hat and for Groslambert Covariance, IEEE Trans. Ultrason. Ferroelectr. Freq. Control 66, 1942 (2019); read as preprint arXiv:1904.05849 | doi:10.1109/TUFFC.2019.2931911 |
| 6 | H. S. Margolis and P. Gill, Least-squares analysis of clock frequency comparison data to deduce optimized frequency and frequency ratio values, Metrologia 52, 628 (2015); read as preprint arXiv:1504.01633 | doi:10.1088/0026-1394/52/5/628 |
| 7 | A. L. Wolf et al., Frequency metrology on the 4s 2S1/2 - 4p 2P1/2 transition in the calcium ion for a comparison with quasar data, Phys. Rev. A 78, 032511 (2008); read as arXiv:0804.4130 | doi:10.1103/PhysRevA.78.032511 |
