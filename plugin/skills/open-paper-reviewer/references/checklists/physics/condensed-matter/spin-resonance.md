---
id: T-SPIN-RESONANCE
name: Electron spin and ferromagnetic resonance
type: technique
field: physics/condensed-matter
applies_when: the paper reports electron spin or paramagnetic resonance g-factors, linewidths or spin counts, ferromagnetic resonance damping, anisotropy or g-factor, or spin pumping and inverse spin Hall voltages, or bases a claim about spin-mixing conductance or spin Hall angle on them
version: "0.1"
---

# Electron spin and ferromagnetic resonance

Electron spin resonance (ESR), also called electron paramagnetic resonance (EPR), and ferromagnetic resonance (FMR) are used to claim g-factors, linewidths, numbers of unpaired spins, magnetic damping and anisotropy. Combined with spin pumping and the inverse spin Hall effect (ISHE), they are also used to claim spin-mixing conductances and spin Hall angles, inferred from small dc voltages measured at resonance.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | K. Herb, R. Tschaggelar, G. Denninger and G. Jeschke, Double resonance calibration of g factor standards: carbon fibers as a high precision standard, J. Magn. Reson. 289, 100–106 (2018) | doi:10.1016/j.jmr.2018.02.006 | abstract | Abstract: the g-factor of defects in carbon fibres, a proposed high-precision g standard, is calibrated by a double-resonance method with a relative uncertainty of 15 ppm, showing that a standard's own g must be calibrated and carries an uncertainty |
| 2 | G. R. Eaton, S. S. Eaton, D. P. Barr and R. T. Weber, Quantitative EPR, Springer, Vienna (2010); read as the publisher's book page and the preview abstract of chapter 10 | doi:10.1007/978-3-211-92948-3 | abstract | Book description: accurate spin concentrations depend on the reference standard, resonator quality factor, microwave and modulation field distributions, sample positioning and power saturation; field and frequency determine g-values. Chapter list: resonator Q, filling factor, temperature, magnetic field and microwave frequency, standard samples. Ch. 10 abstract: g-factors need precisely determined frequency and field, or a standard close enough in field that the field offset adds little error |
| 3 | J. Möser, K. Lips, M. Tseytlin, G. R. Eaton, S. S. Eaton and A. Schnegg, Using rapid-scan EPR to improve the detection limit of quantitative EPR by more than one order of magnitude, J. Magn. Reson. 281, 17–25 (2017); read as the author manuscript in PubMed Central (PMC5556260) | doi:10.1016/j.jmr.2017.04.003 | full text | Sec. 1: slowly relaxing spins saturate and limit the usable power. Sec. 2.4: power-saturation curve, highest microwave field still in the linear range used. Sec. 2.5: intensity equation with gain, power, modulation amplitude, quality factor, Boltzmann population, spin quantum number, field-distribution correction and a reference-standard calibration; double integration after baseline subtraction; modulation amplitude about 30% of the linewidth; modulation period chosen against relaxation time to avoid passage effects. Sec. 3.4: baseline choice gives 10–20% error. Table 1: spin numbers uncertain by about 30%. Sec. 4: overmodulation raises intensity |
| 4 | J. P. Joshi and S. V. Bhat, On the analysis of broad Dysonian electron paramagnetic resonance spectra, J. Magn. Reson. 168, 284–287 (2004) | doi:10.1016/j.jmr.2004.03.018 | abstract | Abstract: broad lines from conducting samples (Dysonian lineshapes) must be simulated with both the clockwise and counterclockwise rotating components of the microwave field; a modified lineshape equation fits better than the one commonly used |
| 5 | J. M. Shaw, H. T. Nembach, T. J. Silva and C. T. Boone, Precise determination of the spectroscopic g-factor by use of broadband ferromagnetic resonance spectroscopy, J. Appl. Phys. 114, 243906 (2013); read as the arXiv abstract page of preprint arXiv:1310.7515 | doi:10.1063/1.4852415 | abstract | Abstract: because broadband measurements cover a finite frequency range, simple fits can give large errors in g; an asymptotic analysis keeps the error below 1% even when the exact Kittel equation is not known, tested on simulated data with an unmodelled anisotropy; deviations from the Kittel equation depend on film thickness and interface structure |
| 6 | S. S. Kalarickal, P. Krivosik, M. Wu, C. E. Patton, M. L. Schneider, P. Kabos, T. J. Silva and J. P. Nibarger, Ferromagnetic resonance linewidth in metallic thin films: comparison of measurement methods, J. Appl. Phys. 99, 093909 (2006); read as the abstract on the NIST publication page | doi:10.1063/1.2197087 | abstract | Abstract: field-swept linewidths increase linearly with frequency, the slope giving the damping parameter; frequency-swept linewidths instead curve upward at low frequency and level off at high frequency; the three methods compared give consistent linewidths once the two kinds are related |
| 7 | W. K. Peria, T. A. Peterson, A. P. McFadden, T. Qu, C. Liu, C. J. Palmstrøm and P. A. Crowell, Interplay of large two-magnon ferromagnetic resonance linewidths and low Gilbert damping in Heusler thin films, Phys. Rev. B 101, 134430 (2020); read as preprint arXiv:1909.02738 | doi:10.1103/PhysRevB.101.134430 | full text | Abstract and Sec. I, Eq. (1): linewidth is a Gilbert term, a frequency-independent inhomogeneous term and a two-magnon term that is in general not linear in frequency; two-magnon linewidths are pervasive in the in-plane geometry, so the perpendicular geometry, where two-magnon scattering is suppressed, or sufficiently broadband data are needed to extract the Gilbert damping. Sec. III and Sec. IV.1: resonance fields fitted against frequency for g and effective magnetisation in both geometries; misalignment in the perpendicular geometry causes field dragging near saturation, so low-frequency data are excluded |
| 8 | M. A. W. Schoen, J. M. Shaw, H. T. Nembach, M. Weiler and T. J. Silva, Radiative damping in waveguide-based ferromagnetic resonance measured via analysis of perpendicular standing spin waves in sputtered permalloy films, Phys. Rev. B 92, 184417 (2015); read as preprint arXiv:1508.05265 | doi:10.1103/PhysRevB.92.184417 | full text | Sec. II, Eqs. (1) and (6): inductive coupling to the waveguide adds radiative damping that depends on sample length and grows linearly with thickness; eddy currents add damping in conducting films. Sec. III: effective magnetisation is saturation magnetisation minus the perpendicular anisotropy field. Sec. IV, Eq. (11): zero-frequency linewidth as inhomogeneous broadening. Sec. VI: radiative damping is up to 40% of the total in the thickest films and is inherent to the measurement, so it must be separated to obtain the intrinsic damping |
| 9 | Y. Tserkovnyak, A. Brataas, G. E. W. Bauer and B. I. Halperin, Nonlocal magnetization dynamics in ferromagnetic heterostructures, Rev. Mod. Phys. 77, 1375–1421 (2005); read as preprint arXiv:cond-mat/0409242 | doi:10.1103/RevModPhys.77.1375 | full text | Sec. I, subsection on Landau-Lifshitz-Gilbert phenomenology: Gilbert damping gives a linewidth strictly linear in frequency, while inhomogeneous broadening gives a weaker frequency dependence and a zero-frequency part. Sec. IV, subsection on ideal spin sinks, Eqs. (60) and (63): spin pumping adds damping inversely proportional to the ferromagnet volume, so to its thickness at fixed interface area. Sec. IV, subsection on diffuse systems: the added damping depends on the spin-sink quality of the normal metal and is reduced by spins flowing back into the ferromagnet; Cu is a poor sink, Pt a very good one |
| 10 | L. Zhu, D. C. Ralph and R. A. Buhrman, Effective spin-mixing conductance of heavy-metal–ferromagnet interfaces, Phys. Rev. Lett. 123, 057203 (2019) | doi:10.1103/PhysRevLett.123.057203 | abstract | Abstract: the mixing conductance is usually taken from damping against inverse ferromagnet thickness assuming spin pumping dominates; in many in-plane magnetised bilayers at nanometre thickness most of that damping is from interfacial two-magnon scattering, with spin memory loss also significant, giving an unphysically large apparent conductance and underestimated spin Hall ratios |
| 11 | J. Sinova, S. O. Valenzuela, J. Wunderlich, C. H. Back and T. Jungwirth, Spin Hall effects, Rev. Mod. Phys. 87, 1213–1260 (2015); read as preprint arXiv:1411.3249 | doi:10.1103/RevModPhys.87.1213 | full text | Sec. III.D: pumped spin current scales with the square of the sine of the precession cone angle; spin backflow reduces it when the normal metal is thin. Sec. IV.D.1: backflow and spin memory loss at the interface reduce the effective mixing conductance; in cavity experiments the excitation field amplitude, and so the cone angle, is usually not well known, and stray microwave electric fields add anomalous Hall contributions; waveguides give known field amplitudes and the cone angle from the measured susceptibility; parasitic magnetoresistance voltages must be analysed. Sec. IV.E and Table III: spin Hall angles from different methods; measurements begin to converge for several materials as systematic errors are understood and corrected, but values for one material still spread widely |
| 12 | R. Iguchi and E. Saitoh, Measurement of spin pumping voltage separated from extrinsic microwave effects, J. Phys. Soc. Jpn. 86, 011003 (2017); read as preprint arXiv:1607.04716 | doi:10.7566/JPSJ.86.011003 | full text | Sec. 2.4: rectification through anisotropic magnetoresistance, the anomalous Hall effect and spin Hall magnetoresistance gives symmetric and antisymmetric Lorentzian voltages. Sec. 2.5: microwave heating gives Seebeck, anomalous Nernst and spin Seebeck voltages, some with the symmetry of the spin pumping signal. Sec. 3.1: low-magnetoresistance or insulating injectors, symmetric layouts, insulating spacer control. Sec. 3.2: symmetric rectification shares the spin pumping symmetry and magnetisation reversal is not sufficient. Secs. 3.3 to 3.5: thickness, angular and frequency dependences as separation methods, frequency mainly for heating |
| 13 | M. Harder, Y. Gui and C.-M. Hu, Electrical detection of magnetization dynamics via spin rectification effects, Phys. Rep. 661, 1–59 (2016); read as preprint arXiv:1605.00710 | doi:10.1016/j.physrep.2016.10.002 | full text | Sec. 1: the relative phase of the microwave electric and magnetic fields shapes the electrically detected line. Sec. 2.3.1: the line splits into Lorentzian and dispersive parts whose ratio is set by that phase; angular dependences of the magnetoresistance and Hall rectification terms. Abstract: the review covers how to distinguish rectification from spin pumping and inverse spin Hall voltages |
