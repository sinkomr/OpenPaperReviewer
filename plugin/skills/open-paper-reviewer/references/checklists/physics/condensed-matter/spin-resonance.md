---
id: T-SPIN-RESONANCE
name: Electron spin and ferromagnetic resonance
type: technique
field: physics/condensed-matter
applies_when: the paper reports electron spin or paramagnetic resonance g-factors, linewidths or spin counts, ferromagnetic resonance damping, anisotropy or g-factor, or spin pumping and inverse spin Hall voltages, or bases a claim about spin-mixing conductance or spin Hall angle on them
version: "0.1"
---

# Electron spin and ferromagnetic resonance

## 1. Field and frequency behind a g-factor

**Question.** How were the microwave frequency and the magnetic field at the sample position determined, which g-factor standard was used and how (measured with the sample or just before it), and at which point of the line was the g-factor read?

**Why it matters.** A g-factor is the ratio of frequency to resonance field, so both must be determined precisely; the field axis of a spectrometer can be offset from the field at the sample, which is why g-factors are usually measured against a standard of known g at nearly the same field. The standard's own g carries an uncertainty, and small claimed g-shifts can lie within the combined uncertainty of standard, field and frequency.

**Resolved by.** The frequency measured for each spectrum; the standard named, with its g-factor and how it was placed; any correction to the field axis stated; the point on the line where g is read marked on the spectrum; a g-factor uncertainty that includes the standard, the field calibration and field homogeneity.

**Benchmark.** [1], [2]

## 2. Microwave power, modulation and passage

**Question.** Are the microwave power, modulation amplitude and modulation frequency stated for each spectrum, and does the paper show that the linewidths and intensities it uses were measured without saturation and with modulation small compared with the linewidth?

**Why it matters.** Above a power set by the spin relaxation times, the signal no longer grows in proportion to the microwave field, and slowly relaxing spins saturate at low power. A modulation amplitude comparable with the linewidth raises the signal but broadens and changes the line, and a modulation period short compared with the relaxation time causes passage effects. Linewidths, lineshapes and intensities taken under these conditions do not describe the spins.

**Resolved by.** A power-saturation curve, integrated intensity against microwave field, with the power used shown to lie in the linear range; a modulation amplitude that is a fraction of the peak-to-peak linewidth, or modulation broadening included in the fit; modulation frequency, time constant and sweep settings stated.

**Benchmark.** [2], [3]

## 3. Spin counting

**Question.** When a number or concentration of spins is quoted, how was it obtained: double integration with what baseline, against which reference sample of known spin number, under which matched conditions (resonator quality factor, sample size and position, temperature, spin quantum number), and with what uncertainty?

**Why it matters.** The doubly integrated signal depends on the resonator quality factor, the distribution of microwave and modulation fields over the sample, the population difference set by temperature and the spin quantum number, as well as on the number of spins. Any of these that differs between sample and reference passes directly into the count. The choice of baseline alone can change the integral by 10 to 20%, and even careful work can carry uncertainties of about 30% in the spin number.

**Resolved by.** The reference named with its calibration; quality factor measured or shown to match; the same tube, filling height and position for sample and reference; both spectra in the linear power range; corrections for temperature and spin quantum number stated; the baseline procedure shown; an uncertainty that reflects these contributions.

**Benchmark.** [2], [3]

## 4. Lineshape model and linewidth definition

**Question.** Which lineshape was fitted to obtain resonance field, linewidth and intensity, is it appropriate for the sample (for example a Dysonian shape for a conducting sample), and is the linewidth defined (peak-to-peak or half width, field-swept or frequency-swept) and converted when values are compared?

**Why it matters.** Lines from conducting samples have a Dysonian shape, and for broad lines both rotating components of the microwave field must be included; how they are included changes the fit, and so the resonance fields and widths taken from it. Field-swept and frequency-swept linewidths have different frequency dependences, so comparing them without conversion gives wrong damping and relaxation values.

**Resolved by.** The lineshape stated and justified by whether the sample conducts; fits shown with residuals; for broad lines, a model with both rotating components; the linewidth definition stated, and conversions given when field-swept and frequency-swept values are compared.

**Benchmark.** [4], [6]

## 5. Resonance field analysis in ferromagnetic resonance

**Question.** Over what frequency and field range was the Kittel relation fitted, in which field geometry, with which parameters free, and are the g-factor, effective magnetisation and anisotropy fields shown not to depend on the fitting range?

**Why it matters.** At laboratory frequencies the resonance frequency is not proportional to the field, so a fitted g-factor is correlated with the effective magnetisation and anisotropy fields fitted with it, and fits over a limited frequency range can give large errors in g. The Kittel relation can also be incomplete because of unmodelled anisotropies, or field misalignment that leaves the sample unsaturated near the resonance field. The effective magnetisation combines saturation magnetisation and perpendicular anisotropy, so an anisotropy derived from it is only as good as an independent saturation magnetisation.

**Resolved by.** Broadband data over a wide frequency range; the g-factor shown to be stable as the upper end of the fitting range is changed, or obtained by an asymptotic analysis at high frequency; in-plane and out-of-plane geometries compared; field calibration in the uncertainty; the sample saturated at every resonance field; saturation magnetisation measured independently and a thickness series used where interface anisotropy is claimed.

**Benchmark.** [5], [7], [8]

## 6. Damping from linewidth

**Question.** Is the damping constant taken from the slope of linewidth against frequency over a broad frequency range, in which magnetisation geometry, and are inhomogeneous broadening, two-magnon scattering, and radiative and eddy-current damping separated from the intrinsic damping?

**Why it matters.** Gilbert damping gives a linewidth proportional to frequency; inhomogeneity adds a frequency-independent intercept, and two-magnon scattering, common when the magnetisation lies in the film plane, adds a term that is not linear in frequency. A linewidth at one frequency, or in-plane data over a narrow range, therefore does not give the Gilbert damping. In waveguide measurements inductive coupling adds a radiative damping that grows with sample thickness and length, and eddy currents add damping in thicker metal films; together they can be a large part of the measured value.

**Resolved by.** Linewidth plotted against frequency with the fitted slope and intercept; measurements with the magnetisation perpendicular to the film, where two-magnon scattering is suppressed, or an in-plane analysis that includes it; radiative and eddy-current contributions estimated for the sample and waveguide geometry.

**Benchmark.** [6], [7], [8], [9]

## 7. From damping and voltage to spin-mixing conductance and spin Hall angle

**Question.** When a spin-mixing conductance, spin diffusion length or spin Hall angle is derived, does the paper show the thickness dependences the spin pumping model requires, account for interface effects other than spin pumping, and state how the microwave field amplitude and precession cone angle were determined?

**Why it matters.** Damping added by spin pumping scales inversely with the ferromagnet thickness and depends on how well the adjacent layer absorbs spin current. In thin bilayers much of the extra damping can come from two-magnon scattering and spin memory loss at the interface, which gives an unphysically large apparent mixing conductance and underestimates the spin Hall angle. The pumped spin current scales with the square of the sine of the precession cone angle, which is often poorly known in cavity measurements. Reported spin Hall angles for the same material still spread widely, and begin to agree only where such systematic errors are corrected.

**Resolved by.** Damping against inverse ferromagnet thickness, preferably with the magnetisation perpendicular to the film; a control with a poor spin sink or a spacer layer; the dependence on the normal-metal thickness; the microwave field calibrated and the cone angle obtained from the measured susceptibility in a known waveguide geometry; the spin diffusion length measured, not assumed; comparison with values from other methods.

**Benchmark.** [9], [10], [11]

## 8. Rectification and heating voltages

**Question.** How does the paper separate the inverse spin Hall voltage from rectification of induced microwave currents through magnetoresistance and the anomalous Hall effect, and from thermoelectric voltages caused by microwave heating?

**Why it matters.** Microwave currents in a conducting ferromagnet combine with its oscillating resistance to give a dc voltage at resonance. Its lineshape can be symmetric, antisymmetric or both, depending on the phase between microwave current and field, and its symmetric part can share the angular symmetry of the spin pumping voltage, so splitting the line into symmetric and antisymmetric parts does not isolate the spin pumping signal. Absorbed power heats the sample and produces Seebeck, anomalous Nernst and spin Seebeck voltages, some of which reverse with the magnetisation just as the spin pumping voltage does, so field reversal alone is not a sufficient test.

**Resolved by.** A sample design that limits rectification, such as an insulating ferromagnet or a low-magnetoresistance metal in a symmetric layout; a control in which a thin insulating spacer blocks spin current but passes heat; thickness dependences of both layers; in-plane and out-of-plane angular dependences with the microwave field components known; a frequency dependence to separate heating; raw voltage spectra for both field polarities.

**Benchmark.** [11], [12], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | K. Herb et al., Double resonance calibration of g factor standards: carbon fibers as a high precision standard, J. Magn. Reson. 289, 100 (2018) | doi:10.1016/j.jmr.2018.02.006 |
| 2 | G. R. Eaton et al., Quantitative EPR, Springer, Vienna (2010); read as the publisher's book page and the preview abstract of chapter 10 | doi:10.1007/978-3-211-92948-3 |
| 3 | J. Möser et al., Using rapid-scan EPR to improve the detection limit of quantitative EPR by more than one order of magnitude, J. Magn. Reson. 281, 17 (2017); read as the author manuscript in PubMed Central (PMC5556260) | doi:10.1016/j.jmr.2017.04.003 |
| 4 | J. P. Joshi and S. V. Bhat, On the analysis of broad Dysonian electron paramagnetic resonance spectra, J. Magn. Reson. 168, 284 (2004) | doi:10.1016/j.jmr.2004.03.018 |
| 5 | J. M. Shaw et al., Precise determination of the spectroscopic g-factor by use of broadband ferromagnetic resonance spectroscopy, J. Appl. Phys. 114, 243906 (2013); read as the arXiv abstract page of preprint arXiv:1310.7515 | doi:10.1063/1.4852415 |
| 6 | S. S. Kalarickal et al., Ferromagnetic resonance linewidth in metallic thin films: comparison of measurement methods, J. Appl. Phys. 99, 093909 (2006); read as the abstract on the NIST publication page | doi:10.1063/1.2197087 |
| 7 | W. K. Peria et al., Interplay of large two-magnon ferromagnetic resonance linewidths and low Gilbert damping in Heusler thin films, Phys. Rev. B 101, 134430 (2020); read as preprint arXiv:1909.02738 | doi:10.1103/PhysRevB.101.134430 |
| 8 | M. A. W. Schoen et al., Radiative damping in waveguide-based ferromagnetic resonance measured via analysis of perpendicular standing spin waves in sputtered permalloy films, Phys. Rev. B 92, 184417 (2015); read as preprint arXiv:1508.05265 | doi:10.1103/PhysRevB.92.184417 |
| 9 | Y. Tserkovnyak et al., Nonlocal magnetization dynamics in ferromagnetic heterostructures, Rev. Mod. Phys. 77, 1375 (2005); read as preprint arXiv:cond-mat/0409242 | doi:10.1103/RevModPhys.77.1375 |
| 10 | L. Zhu et al., Effective spin-mixing conductance of heavy-metal–ferromagnet interfaces, Phys. Rev. Lett. 123, 057203 (2019) | doi:10.1103/PhysRevLett.123.057203 |
| 11 | J. Sinova et al., Spin Hall effects, Rev. Mod. Phys. 87, 1213 (2015); read as preprint arXiv:1411.3249 | doi:10.1103/RevModPhys.87.1213 |
| 12 | R. Iguchi and E. Saitoh, Measurement of spin pumping voltage separated from extrinsic microwave effects, J. Phys. Soc. Jpn. 86, 011003 (2017); read as preprint arXiv:1607.04716 | doi:10.7566/JPSJ.86.011003 |
| 13 | M. Harder et al., Electrical detection of magnetization dynamics via spin rectification effects, Phys. Rep. 661, 1 (2016); read as preprint arXiv:1605.00710 | doi:10.1016/j.physrep.2016.10.002 |
