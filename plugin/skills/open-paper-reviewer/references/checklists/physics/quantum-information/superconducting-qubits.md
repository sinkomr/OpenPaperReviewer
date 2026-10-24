---
id: T-SUPERCONDUCTING-QUBITS
name: Superconducting qubits
type: technique
field: physics/quantum-information
applies_when: the paper reports T1, Ramsey or echo T2, readout fidelity or spectroscopy of a transmon or other superconducting qubit, or bases a claim about coherence, loss mechanisms, two-level-system defects or device stability on them
version: "0.1"
---

# Superconducting qubits

Measurements on superconducting qubits, most often transmons, are used to claim an energy relaxation time (T1), dephasing times from Ramsey (T2*) and Hahn echo (T2E) experiments, a readout fidelity and the qubit's transition frequencies, and from these to claim better materials or designs, identify loss mechanisms such as two-level-system (TLS) defects, or benchmark a device. Each number comes from a pulse sequence, a readout chain and a fit, and each can change with frequency and over time.

## 1. Energy relaxation time

**Question.** How was T1 measured (pi-pulse calibration, range of delays compared with T1, fit model), at which qubit frequency, and does the paper compare it with the Purcell limit set by the readout resonator and other designed decay channels?

**Why it matters.** T1 is the 1/e time of an exponential fitted to the decay after a pi pulse. When the decay is not a single exponential, as with hot quasiparticles, the fitted value depends on the delay range and the model. Coupling to the readout resonator adds a Purcell decay that can set T1 by design, and T1 can change sharply with frequency, so a value given without its frequency or its designed limit cannot be compared with others.

**Resolved by.** The raw decay curve with its fit over delays reaching several T1; the fit model stated and any departure from a single exponential shown and discussed; the qubit frequency and the readout resonator linewidth, coupling and detuning given, with the estimated Purcell limit and any Purcell filter; the pi-pulse calibration described.

**Benchmark.** [1], [2]

## 2. Dephasing times and their decay model

**Question.** Which dephasing time is quoted (Ramsey T2*, echo T2E or a longer pulse sequence), what Ramsey detuning was used, which decay envelope was fitted, how was any pure dephasing time obtained from T1 and T2, and, for a flux-tunable qubit, at which flux bias was T2 measured?

**Why it matters.** A Ramsey experiment is sensitive to slow noise that changes from one repetition to the next, which an echo pulse largely refocuses, so the two times describe different things and are not interchangeable. Under 1/f noise the dephasing envelope is Gaussian, not exponential, and the familiar sum of rates holds exactly only for white noise. T2 cannot exceed 2T1, and a pure dephasing time derived from T1 and T2 inherits the fluctuations of both. In a flux-tunable qubit, dephasing from flux noise grows with the slope of frequency against flux, so a T2 taken at the flux sweet spot does not describe other operating points.

**Resolved by.** The pulse sequence named with every quoted T2; Ramsey fringes shown with the detuning stated; the envelope model stated (exponential, Gaussian or a product of both) with the fits shown; T2 compared with 2T1; T1 and T2 measured close together in time when a pure dephasing rate is derived from them; for a tunable qubit, the flux bias and the slope of frequency against flux given with each T2.

**Benchmark.** [1], [3]

## 3. Readout fidelity

**Question.** How is readout fidelity defined (formula, threshold, integration time, readout power), and does the paper separate the error into overlap of the state distributions, relaxation during the readout, preparation errors and transitions caused by the measurement, stating any pre-selection of shots?

**Why it matters.** Readout fidelity is limited by the overlap of the two signal distributions, which falls with integration time and drive power, and by relaxation during the readout, which grows with integration time, so the quoted value depends on these choices. Driving the resonator with more photons improves separation, but measurement-induced transitions raise the error, and this can set in well below the critical photon number at which the dispersive approximation fails. Discarding shots flagged as excited before the measurement removes preparation errors from the quoted value.

**Resolved by.** Single-shot histograms or distributions in the IQ plane for each prepared state, with the threshold shown; the fidelity formula stated; integration time and readout photon number given and compared with the critical photon number; an error budget across the separate sources; any pre-selection or heralding stated with the fraction of shots discarded; the amplifier chain described.

**Benchmark.** [1], [4]

## 4. Residual excited-state population and thermal photons

**Question.** Does the paper measure the qubit's residual excited-state population, or effective temperature, and the residual photon population of the readout resonator, and allow for them in the T1, T2 and readout results?

**Why it matters.** Superconducting qubits often hold an excited-state population far above the equilibrium value at the refrigerator temperature, which limits state preparation and offsets relaxation and readout data. Residual thermal photons in the readout resonator dephase the qubit through the dispersive shift, so a short T2 can reflect the wiring, attenuation and filtering, not the qubit itself.

**Resolved by.** The excited-state population measured by a method that does not rest on readout histograms alone, such as comparing Rabi oscillations on the next transition with and without a prior pi pulse, with the implied effective temperature; the attenuation and filtering of the lines described; an estimate or bound on the residual photon number and the dephasing it causes, compared with the measured dephasing rate.

**Benchmark.** [5], [1], [4]

## 5. Qubit spectroscopy and linewidths

**Question.** In spectroscopy used to locate transitions or measure linewidths, are the drive and readout powers stated, is the linewidth followed as a function of drive power before it is related to dephasing, and are splittings in the spectrum assigned with a check against defect coupling?

**Why it matters.** The spectroscopy drive broadens the line, and photons in the readout resonator shift the qubit frequency through the ac Stark effect and broaden the line through measurement-induced dephasing, changing both its width and its shape. A line taken at one power therefore gives only an upper bound on the intrinsic linewidth and a frequency displaced from its bare value. A splitting of the spectral line can come from a strongly coupled TLS defect.

**Resolved by.** Spectra at several drive powers with the width plotted against power and extrapolated to low power; the readout photon number stated or calibrated from the ac Stark shift; the line shape model stated; splittings followed as the qubit is tuned, to distinguish an avoided crossing with a defect from the intended feature.

**Benchmark.** [6], [7]

## 6. Two-level-system defects and frequency dependence

**Question.** When a claim concerns loss mechanisms or a tunable qubit, does the paper show T1 over a range of qubit frequencies, identify sharp dips or avoided crossings from individual TLS defects, and separate them from the background loss?

**Why it matters.** Individual TLS defects near the qubit frequency produce sharp drops in T1 and splittings in spectroscopy, and their frequencies drift over time and can change after thermal cycling. A T1 taken at one frequency may sit on or off such a defect, so it can misstate the typical loss, and an intrinsic loss or a defect density cannot be inferred from it.

**Resolved by.** T1 against frequency, by flux tuning, swap spectroscopy or an ac Stark shift, over a stated range and repeated over time, so that persistent defects can be told from drifting ones; individual defects identified with their coupling strength; data from more than one cooldown where defect densities are discussed.

**Benchmark.** [7], [2], [8]

## 7. Fluctuations of coherence over time

**Question.** Is each quoted T1 and T2 a single measurement, a best value or a statistic over a stated period, and does the paper give the monitoring time, the distribution of values and the change between cooldowns?

**Why it matters.** The T1 of one qubit can change by more than a factor of two over hours, often switching between discrete values as TLS defects move in frequency, and its mean can shift between cooldowns. A single or best value therefore says little about typical performance.

**Resolved by.** Repeated T1 and T2 measurements over hours to days, with the number of measurements, mean or median, spread and histogram given; best values labelled as such; results from repeated cooldowns where available; claims of improvement based on these statistics, not on single values.

**Benchmark.** [3], [8], [7]

## 8. Attributing coherence to a loss mechanism or a fabrication change

**Question.** When a change in T1 or T2 is attributed to a material, surface treatment or design change, does the paper first exclude designed and environmental limits and compare enough qubits whose participation in the lossy regions is known?

**Why it matters.** The measured relaxation rate is a sum of channels, including dielectric loss at surfaces and interfaces, Purcell and radiative decay, and quasiparticles. Once the environment and quasiparticles are controlled, relaxation rates scale with the share of electric-field energy in lossy surfaces, so a change of geometry changes T1 with the same materials. Differences between nominally similar devices, and between cooldowns, can be as large as the improvement claimed.

**Resolved by.** A loss budget with the Purcell and other designed limits computed; surface participation ratios simulated for each geometry compared; several qubits per condition, measured over time and at comparable frequencies; quasiparticle and radiation contributions addressed where they could matter.

**Benchmark.** [9], [1], [3]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | P. Krantz, M. Kjaergaard, F. Yan, T. P. Orlando, S. Gustavsson and W. D. Oliver, A quantum engineer's guide to superconducting qubits, Appl. Phys. Rev. 6, 021318 (2019); read as preprint arXiv:1904.06560 | doi:10.1063/1.5089550 | full text | Sec. III.2.2: T1 from the exponential decay after an X pi pulse over variable delays; hot quasiparticles can make the decay non-exponential; Ramsey is sensitive to quasi-static noise that the echo refocuses; Eq. 42 relates the rates. Sec. III.2.3: 1/f noise gives a Gaussian dephasing envelope, a single exponential is only a practical approximation when the pure dephasing time is at least comparable to T1, and T2 never exceeds 2T1. Sec. III.3.3: residual thermal photons in the readout resonator cause dephasing set by photon number, linewidth and dispersive shift. Secs. III.3.4 and III.5.3: quasiparticles affect T1 and its variation. Secs. III.3.2 and III.4.2: flux noise dephases a split transmon in proportion to the sensitivity of its frequency to flux, with a first-order insensitive sweet spot. Sec. V.1: dispersive readout breaks down above the critical photon number. Sec. V.3: overlap of the noise-broadened state distributions limits discrimination. Sec. V.4: relaxation during the readout limits fidelity, so integration time is a trade-off; Purcell decay through the readout resonator and Purcell filters |
| 2 | P. V. Klimov, J. Kelly, Z. Chen et al., Fluctuations of energy-relaxation times in superconducting qubits, Phys. Rev. Lett. 121, 090502 (2018) | doi:10.1103/PhysRevLett.121.090502 | abstract | Abstract (read on arXiv:1809.01043): energy-relaxation times fluctuate unpredictably in frequency and in time, and individual TLS defects are found to be the dominant source of the largest fluctuations |
| 3 | J. J. Burnett, A. Bengtsson, M. Scigliuzzo, D. Niepce, M. Kudra, P. Delsing and J. Bylander, Decoherence benchmarking of superconducting qubits, npj Quantum Inf. 5, 54 (2019); read as preprint arXiv:1901.04417 | doi:10.1038/s41534-019-0168-5 | full text | Secs. II.2 and II.3: T1 of one qubit varies by more than a factor of two, switching between discrete values with dwell times of hours. Sec. III: the T1 behaviour is attributed to near-resonant TLS; reports of coherence should give statistics from measurements over several hours, so as to show the typical, not the exceptional, value. Secs. II.5 and III: T2* compared with 2T1, and qubit frequency fluctuations bound pure dephasing. Sec. V.1 and Table 3: the mean T1 differs between cooldowns |
| 4 | T. Walter, P. Kurpiers, S. Gasparinetti et al., Rapid high-fidelity single-shot dispersive readout of superconducting qubits, Phys. Rev. Applied 7, 054020 (2017); read as preprint arXiv:1701.06933 | doi:10.1103/PhysRevApplied.7.054020 | full text | Sec. II and Eq. 1: fidelity defined from a threshold on the integrated signal; error split into overlap error and transition errors (failed preparation together with transitions during the readout), with qubit decay the largest part of the excited-state error; fidelity peaks at an intermediate integration time; overlap error falls with drive power while total error has a minimum near 2.5 readout photons and rises above it from measurement-induced mixing. Sec. III.2: the critical photon number is about 13, so the rise sets in well below it. Appendix B: pre-selection discards shots flagged as excited, with the excess attributed to residual thermal population |
| 5 | X. Y. Jin, A. Kamal, A. P. Sears et al., Thermal and residual excited-state population in a 3D transmon qubit, Phys. Rev. Lett. 114, 240501 (2015); read as preprint arXiv:1412.2772 | doi:10.1103/PhysRevLett.114.240501 | full text | Introduction: other devices report excited-state populations of about 1% to 13%, effective temperatures far above base temperature. Measurement protocol and Fig. 1: population measured by comparing excited-to-second-state Rabi amplitudes with and without a prior pi pulse, not from readout histograms. Fig. 3: population saturates below about 35 mK, above the equilibrium value at base temperature; filtering and attenuation reviewed |
| 6 | D. I. Schuster, A. Wallraff, A. Blais, L. Frunzio, R.-S. Huang, J. Majer, S. M. Girvin and R. J. Schoelkopf, ac Stark shift and dephasing of a superconducting qubit strongly coupled to a cavity field, Phys. Rev. Lett. 94, 123602 (2005); read as preprint arXiv:cond-mat/0408367 | doi:10.1103/PhysRevLett.94.123602 | full text | Fig. 4: spectroscopy line broadens with drive power and the unbroadened width is related to T2. Fig. 5a and Eq. 1: readout photons shift the qubit frequency linearly (ac Stark shift), used to calibrate photon number. Eqs. 3 and 4 and Fig. 5b: photon shot noise broadens the line, changing it from Lorentzian to Gaussian as the measurement strengthens |
| 7 | C. Müller, J. H. Cole and J. Lisenfeld, Towards understanding two-level-systems in amorphous solids: insights from quantum circuits, Rep. Prog. Phys. 82, 124501 (2019); read as preprint arXiv:1705.01108 | doi:10.1088/1361-6633/ab3a7e | full text | Sec. IV.3: TLS frequencies diffuse or switch through interactions with thermal fluctuators, so qubit relaxation rates vary by up to about 100% over hours and recalibration is needed. Sec. V.1: a strongly coupled TLS splits the qubit spectroscopy line into an avoided crossing, weaker ones enhance relaxation at resonance, and the pattern of crossings changed after thermal cycling. Secs. V.1 and V.3: swap spectroscopy reveals TLS as the qubit is tuned through them |
| 8 | H. Kim, C. Jünger, A. Morvan, E. S. Barnard, W. P. Livingston, M. V. P. Altoé, Y. Kim, C. Song, L. Chen, J. M. Kreikebaum, D. F. Ogletree, D. I. Santiago and I. Siddiqi, Effects of laser-annealing on fixed-frequency superconducting qubits, Appl. Phys. Lett. 121, 142601 (2022); read as preprint arXiv:2206.03099 | doi:10.1063/5.0102092 | full text | Sec. III and Fig. 2: T1 and T2 of each qubit recorded for about 17 hours before and after laser annealing and compared as box plots of those distributions, with differences judged against their spread. Sec. III and Fig. 3: relaxation rate modelled as a Lorentzian in qubit-TLS detuning on top of a frequency-independent background; TLS spectroscopy of a fixed-frequency transmon by ac Stark shifting it with an off-resonant tone calibrated by Ramsey, using the excited-state population at a fixed delay near T1 as a fast proxy, over 160 hours, shows one persistent and several fluctuating defects, with the detuning and coupling of the persistent one fitted. Sec. III and Supplementary Sec. VII.3 with Fig. S1: spectroscopy repeated over three cooldowns; before annealing one defect persists within 1 MHz, after annealing none persists; telegraphic TLS seen over hours |
| 9 | C. Wang, C. Axline, Y. Y. Gao, T. Brecht, Y. Chu, L. Frunzio, M. H. Devoret and R. J. Schoelkopf, Surface participation and dielectric loss in superconducting qubits, Appl. Phys. Lett. 107, 162601 (2015) | doi:10.1063/1.4934486 | abstract | Abstract (arXiv:1509.01854): with a clean electromagnetic environment and suppressed quasiparticles, transmon relaxation rates are roughly proportional to the simulated surface participation ratio, varied through geometry. Supplementary material (read in full on arXiv; main text not read), Sec. III: 1/T1 fitted against the participation of each interface; Table S1 caption: each T1 uncertainty is one standard deviation of its fluctuation over time |
