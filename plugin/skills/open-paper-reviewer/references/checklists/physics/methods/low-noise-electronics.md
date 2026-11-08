---
id: T-LOW-NOISE-ELECTRONICS
name: Low-noise electronics and lock-in detection
type: technique
field: physics/methods
applies_when: the paper measures small voltages, currents or noise with lock-in amplifiers, preamplifiers or digitizers, or bases a claim on a lock-in signal, its phase or harmonics, a noise spectrum, or a signal close to the noise floor of the electronics
version: "0.1"
---

# Low-noise electronics and lock-in detection

## 1. Grounding and ground loops

**Question.** Does the paper describe how the source, sample, amplifiers and lock-in or digitizer are grounded, whether the inputs are differential or single-ended, and how cable shields are connected?

**Why it matters.** When instruments are grounded at different points, the potential difference between the grounds drives currents around the loop, and the resulting voltage adds to the reading as an offset or as noise at the mains frequency. A single-ended input reads this difference directly, and a shield grounded at both ends carries ground current next to the signal.

**Resolved by.** A wiring diagram, or a description, showing the ground points, the input configuration and where each shield is connected; differential inputs or isolation for grounded sources; the lock-in's own oscillator, or an isolated source, used for the excitation where possible; evidence that the background does not change when the grounding is changed.

**Benchmark.** [1], [2], [4]

## 2. Pickup, crosstalk and background at the reference frequency

**Question.** Does the paper show the signal recorded with the sample's response removed (excitation off, the sample replaced by a short or by a resistor of similar impedance, or the modulated stimulus blocked), and does it say why the reference frequency was chosen?

**Why it matters.** Capacitive and magnetic coupling from mains wiring, the excitation lines or the reference cable can put a signal into the input at the measurement frequency. Unlike random noise, a coherent pickup at the reference frequency adds directly to the signal and does not average away, so a background that is not measured is read as part of the result. A reference frequency at or near a mains harmonic or another technical line makes this more likely.

**Resolved by.** A background measurement under the same settings with the sample's response removed, shown to be small compared with the reported signal; the signal shown to scale as expected with the excitation; a noise spectrum or a statement showing that the reference frequency avoids mains harmonics and other interference peaks; twisted or shielded leads and reduced loop areas where magnetic pickup is possible.

**Benchmark.** [1], [2], [3]

## 3. Input impedance, loading and bandwidth

**Question.** Are the input impedance of the measuring instrument, the capacitance of the cables and filters, the coupling (ac or dc) and the bandwidth of each amplifier stated, and are they compared with the source impedance and the measurement frequency?

**Why it matters.** A voltage input of finite resistance draws current from a high-impedance sample and reduces the measured voltage, and the cable and filter capacitance forms a low-pass filter with the source that attenuates the signal and shifts its phase as the frequency rises. At a current-preamplifier input the same capacitance narrows the bandwidth. Ac coupling removes signals below its cut-off, so a low reference frequency can be attenuated by the input itself.

**Resolved by.** Input impedance, cable and filter capacitance, coupling and amplifier bandwidth stated; source impedance shown to be well below the input impedance, or a high-impedance buffer or preamplifier placed near the sample; the measurement frequency shown to lie well inside the bandwidth of every stage; for high-impedance samples, the result shown not to depend on frequency over the range used.

**Benchmark.** [1], [4], [5], [6]

## 4. Amplifier noise and the noise floor

**Question.** Does the paper state the noise floor of the measurement chain at the measurement frequency, with the source impedance in place, and compare it with the reported signal or noise?

**Why it matters.** A preamplifier contributes voltage noise, current noise and the thermal noise of its feedback resistor, and which one dominates depends on the source impedance and the input capacitance; voltage noise acting on a large input capacitance is easily overlooked. A noise spectrum is a property of the sample only where the background of the chain is well below it. Cross-correlation of two amplifier channels can reach below the background of one channel, but only after enough averaging.

**Resolved by.** The background measured with the inputs shorted and with a resistor or dummy load of matching impedance, plotted alongside the reported spectrum or signal; the amplifier, its gain and its specified noise named; for noise spectra, the background shown to be well below the reported noise over the full frequency range, and for cross-correlation the number of averages and the residual background stated.

**Benchmark.** [1], [5], [7], [8], [13]

## 5. Phase, in-phase and quadrature

**Question.** Does the paper say which lock-in output is plotted (X, Y, R or phase), how the reference phase was set, and what the out-of-phase component was?

**Why it matters.** A lock-in measures the input relative to its reference as two components, X in phase and Y in quadrature. Capacitive paths and amplifier bandwidth add phase shifts, so a signal that is plotted as X after an arbitrary phase adjustment, or as R alone, can mix a resistive response with a capacitive one or with pickup. Setting the phase to put all of the signal in X can hide such a contribution.

**Resolved by.** The plotted output named for each data set; the method of setting the reference phase stated, for example on a known resistive load; both X and Y, or R and phase, shown or reported, with the out-of-phase part small or explained; the phase shown to be stable over the parameter range of the claim.

**Benchmark.** [3], [5]

## 6. Filter settings, sampling and noise bandwidth

**Question.** Are the lock-in time constant, filter order and wait time or sweep rate stated, and for digitized records the sampling rate and anti-aliasing filter, and is the sweep slow enough for the filter to settle at each point?

**Why it matters.** The lock-in's low-pass filter needs several time constants to settle, more for higher filter orders, so a fast sweep distorts and shifts features and depends on the sweep direction; the same settings fix the noise bandwidth needed to turn a noise reading into a spectral density, and noise read from the magnitude R is biased because R has a nonzero mean even for pure noise. A digitizer sampling at less than twice the highest frequency reaching its input folds pickup and noise from above that frequency into the measured band, where they appear as low-frequency signal.

**Resolved by.** Time constant, filter order and wait time per point, or sweep rate, stated for each data set; the same features obtained in both sweep directions or at a slower rate; noise given as a spectral density computed from X and Y, with the noise bandwidth used for the conversion; for digitized data, the sampling rate and the anti-aliasing filter stated, with the input band-limited below half the sampling rate.

**Benchmark.** [3], [4], [12], [13]

## 7. Harmonics, nonlinearity and overload

**Question.** For signals detected at a harmonic of the reference, or claimed to come from a nonlinear response, does the paper show that the harmonic is not produced by heating, by distortion in the source or amplifiers, by overload of the input, or by the reference waveform?

**Why it matters.** A lock-in with a square-wave reference also responds to odd harmonics of the input. An ac current that heats the sample produces temperature changes at twice the excitation frequency, and the resulting thermoelectric voltages can be similar in size and symmetry to the effect being sought. An input driven near the limit of its range distorts the signal and creates harmonics of its own.

**Resolved by.** The harmonic signal shown to scale with excitation as the claimed mechanism predicts; the input range and the margin to overload stated; the harmonic content of the source measured on a linear reference load; thermal contributions estimated or separated, for example by their dependence on field, angle or sample structure.

**Benchmark.** [3], [4], [9]

## 8. Calibration of the gain chain

**Question.** Where an absolute signal level is quoted, was the overall gain of the preamplifiers, filters and lock-in or digitizer measured at the frequency used, and is it stated whether values are root mean square, amplitude or peak-to-peak?

**Why it matters.** The gain of a preamplifier depends on frequency near its bandwidth and on the source capacitance, and the accuracy of a lock-in's gain is specified only loosely by manufacturers, far less tightly than a calibrated reference source can check it. Unchecked factors from gain settings, filter roll-off or the convention for amplitude pass directly into the reported signal and into anything derived from it.

**Resolved by.** The gain of the whole chain measured by injecting a known signal at the sample position at the measurement frequency, or each stage's gain at that frequency stated with its source; the amplitude convention stated; the calibration uncertainty included in the quoted values.

**Benchmark.** [5], [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | National Instruments (NI), Field Wiring and Noise Considerations for Analog Signals, Measurement Fundamentals tutorial (web page, undated; accessed 2026) | https://www.ni.com/en/shop/data-acquisition/measurement-fundamentals/field-wiring-and-noise-considerations-for-analog-signals.html |
| 2 | Keysight Technologies, Tip 7: Making Low-Level AC Measurements, training material (web page, undated; accessed 2026) | https://www.keysight.com/ca/en/lib/resources/training-materials/tip-7-making-lowlevel-ac-measurements-489748.html |
| 3 | Zurich Instruments, Principles of Lock-in Detection, white paper (web page, undated; accessed 2026) | https://www.zhinst.com/en/resources/principles-of-lock-in-detection |
| 4 | G. Ciardi, Top 10 Tips for Your Lock-in Measurement, Zurich Instruments blog (20 August 2024) | https://www.zhinst.com/en/blogs/top-10-tips-for-your-lock-in-measurement/ |
| 5 | A. V. Kretinin and Y. Chung, Wide-band current preamplifier for conductance measurements with large input capacitance, Rev. Sci. Instrum. 83, 084704 (2012); read as preprint arXiv:1204.2239 | doi:10.1063/1.4740521 |
| 6 | Z. Pan et al., Tackling Challenges in Seebeck Coefficient Measurement of Ultra-High Resistance Samples with an AC Technique, Adv. Electron. Mater. 6, 1901340 (2020); read as preprint arXiv:1910.14205 | doi:10.1002/aelm.201901340 |
| 7 | G. Scandurra et al., A review of design approaches for the implementation of low-frequency noise measurement systems, Rev. Sci. Instrum. 93, 111101 (2022) | doi:10.1063/5.0116589 |
| 8 | E. Rubiola and F. Vernotte, The cross-spectrum experimental method, arXiv:1003.0113 (2010) | doi:10.48550/arXiv.1003.0113 |
| 9 | C. O. Avci et al., Interplay of spin-orbit torque and thermoelectric effects in ferromagnet/normal metal bilayers, Phys. Rev. B 90, 224427 (2014); read as preprint arXiv:1412.0865 | doi:10.1103/PhysRevB.90.224427 |
| 10 | EURAMET Technical Committee for Electricity and Magnetism, Project 1466, Calibration of lock-in amplifiers (project page, 2019 to 2021) | https://www.euramet.org/technical-committees/tc-projects/details/project/calibration-of-lock-in-amplifiers |
| 11 | A. Cultrera et al., A new calibration setup for lock-in amplifiers in the low frequency range and its validation in a bilateral comparison, Metrologia 58, 025001 (2021) | doi:10.1088/1681-7575/abdae0 |
| 12 | Spectrum Instrumentation, Common Digitizer Setup Problems to Avoid, application note (web page, undated; accessed 2026) | https://spectrum-instrumentation.com/applications/application_notes/Common_Digitizer_Setup_Problems_avoid.php |
| 13 | M. Alem, Noise Spectral Density Measured with Lock-in Amplifiers, Zurich Instruments blog (15 August 2021) | https://www.zhinst.com/en/blogs/noise-spectral-density-measured-lock-amplifiers |
