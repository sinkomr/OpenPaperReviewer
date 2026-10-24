---
id: T-MICRORESONATOR-COMBS
name: Microresonators and frequency combs
type: technique
field: physics/optics-photonics
applies_when: the paper reports the quality factor or linewidth of an optical microresonator, or generates a Kerr frequency comb or soliton microcomb and claims a soliton state, coherence, low noise, stabilisation, self-referencing, conversion efficiency, parametric threshold or thermal behaviour
version: "0.1"
---

# Microresonators and frequency combs

Optical microresonators are used to claim intrinsic and loaded quality factors (Q) and linewidths, and, when pumped by a continuous-wave laser, Kerr frequency combs ("microcombs") that form dissipative Kerr soliton (DKS) states with a stated repetition rate, carrier-envelope offset frequency (f_CEO), coherence, frequency stability and efficiency. These claims rest on transmission scans, optical and radio-frequency (RF) spectra and beat notes, each of which is shaped by the coupling to the bus waveguide, the laser and the resonator's own heating.

## 1. Coupling regime and intrinsic quality factor

**Question.** Does the paper state whether each resonance is under-coupled, critically coupled or over-coupled, how that was established, and how the intrinsic Q was separated from the loaded Q?

**Why it matters.** A transmission dip of a given depth and width fits both an under-coupled and an over-coupled resonance, and the two give different intrinsic Q from the same loaded linewidth. Assuming a regime without measuring it can change the claimed intrinsic Q by a large factor, and the coupling ratio also sets the threshold and efficiency that follow from it.

**Resolved by.** The loaded linewidth, extinction and the coupling regime given for each resonance quoted; the regime determined by a measurement that carries phase or time information, such as a phase-sensitive or vector network analyser scan or a ring-down; where the regime is assumed from design, the assumption stated and its effect on the intrinsic Q shown.

**Benchmark.** [1], [2], [3]

## 2. Linewidth measurement conditions

**Question.** How was the frequency axis of the linewidth scan calibrated, what were the laser linewidth, scan direction, scan speed and optical power, and how were split resonances treated?

**Why it matters.** A linewidth read from a laser scan is only as good as the frequency calibration and needs a laser narrower than the resonance. Absorbed power heats the resonator and shifts it during the scan, so the dip is broadened in one scan direction and narrowed in the other. Backscattering splits many high-Q resonances into doublets, and fitting a doublet as a single Lorentzian, or choosing only unsplit resonances, changes the reported Q.

**Resolved by.** A calibrated frequency axis, for example an interferometer whose free spectral range is itself calibrated with modulation sidebands, and its uncertainty carried into Q; the laser linewidth stated; scans in both directions or at reduced power showing no thermal distortion; a ring-down cross-check for the highest Q values; doublets fitted with a coupled-mode model, and the rule for choosing the resonances reported stated together with the spread across many resonances.

**Benchmark.** [1], [2], [4]

## 3. Pump power, threshold and efficiency

**Question.** For each quoted pump power, parametric threshold or conversion efficiency, does the paper say where the power is referenced (in the bus waveguide, in the fibre, or from the wall plug) and how the comb power and efficiency were defined?

**Why it matters.** Coupling losses between fibre and chip mean that a power quoted in the bus waveguide and one quoted at the laser are not the same number. Efficiency definitions differ in whether the residual pump is counted and in whether amplifier and electrical power are included, and the threshold of a Kerr comb scales with the inverse square of Q, so an error in Q or in the coupling ratio passes directly into these numbers.

**Resolved by.** Each power stated at a named reference plane with the coupling loss measured and given; the efficiency defined in words (which lines are counted, whether the pump is excluded) and the loading factor or coupling ratio stated; a threshold derived from Q checked against a measured threshold; wall-plug or system efficiency reported separately where a practical advantage is claimed.

**Benchmark.** [3], [11]

## 4. Dispersion and mode spectrum

**Question.** Was the dispersion of the pumped mode family measured over the comb bandwidth, and does the paper show the mode spectrum, including avoided mode crossings, near the pump and where the comb spectrum has features?

**Why it matters.** Soliton formation needs overall anomalous dispersion in the pumped family, and higher-order dispersion and coupling to other mode families reshape the comb. Avoided crossings near the pump can prevent solitons altogether, and crossings further away produce local peaks and dips in the spectrum that can be mistaken for other effects.

**Resolved by.** Measured resonance frequencies against mode number, from a laser scan calibrated with a reference comb or interferometer, with the fitted dispersion coefficients and their uncertainties; avoided crossings located and related to features in the comb spectrum; dispersive waves and spectral asymmetries explained by the measured higher-order terms.

**Benchmark.** [5]

## 5. Identifying the soliton state

**Question.** Which measurements show that the comb is in a single-soliton or a stated multi-soliton state, and not in a chaotic modulation-instability state, a breathing soliton or a non-soliton comb?

**Why it matters.** Steps in the transmitted power, a smooth spectral envelope and a narrow beat note each point to a soliton but do not alone fix the number of solitons or show that the state is stationary. Breathing solitons, whose amplitude and duration oscillate, change the averaged spectrum and add sidebands to the beat note, and autocorrelation traces can show pulse-like features where there are no pulses.

**Resolved by.** The optical spectrum compared with the expected sech-squared envelope given the measured dispersion; the step structure in transmitted power with the soliton number read from step heights or spectral interference; the effective detuning measured, for example by the response to a weak phase modulation; the RF spectrum of the transmitted light over a wide range showing no breathing tones; temporal characterisation by frequency-resolved optical gating or time-resolved detection where pulse shape is claimed.

**Benchmark.** [6], [7], [8]

## 6. Coherence and noise across the comb

**Question.** Which measurements support the claimed coherence and low noise of the comb: the repetition-rate beat note with its resolution bandwidth and span, heterodyne beats of individual lines against a reference, and the RF amplitude noise of the whole comb or of filtered parts of it?

**Why it matters.** A Kerr comb can consist of interleaved sub-combs with slightly different offsets, which give multiple or broad beat notes even when the optical spectrum looks smooth. A single narrow beat note measured at one span and resolution bandwidth, or only in one part of the spectrum, does not show that every line shares the same spacing and phase relation.

**Resolved by.** The repetition-rate beat note shown with its resolution bandwidth and over a span wide enough to reveal sidebands; RF amplitude noise of the full comb and of filtered spectral slices; heterodyne beats of several lines against a reference laser or comb, or counted line spacings showing equal spacing to a stated precision; the soliton or comb state in which each noise measurement was made.

**Benchmark.** [6], [8], [9], [10]

## 7. Stabilisation and frequency accuracy

**Question.** Which degrees of freedom (pump frequency, repetition rate, f_CEO) were detected and locked, by what scheme and to what reference, and is frequency stability or accuracy shown by an out-of-loop comparison and not only by in-loop signals?

**Why it matters.** A locked in-loop beat note shows that the servo is working, not that the comb lines have the claimed frequencies. Self-referencing needs a spectrum wide enough for the chosen interferometer, often reached with external broadening that the claim should acknowledge. Allan deviations depend on the counter type and gate times, which change the slope from which the noise type is inferred.

**Resolved by.** A diagram of the locks with actuators and references named; the spectral coverage used for self-referencing and any external broadening stated; an independent comparison, for example comb line frequencies computed from counted f_CEO and repetition rate compared with a separate reference comb; Allan deviations with counter type and gate times stated, and a check that the instruments do not limit them.

**Benchmark.** [10], [11]

## 8. Thermal effects and thermal noise

**Question.** How were thermal shifts handled in reaching and holding the reported comb state, and does the paper compare its noise or stability claims with the thermorefractive noise expected for its resonator?

**Why it matters.** Absorbed power shifts the resonance, so the transmission becomes a triangle and states on the red-detuned side, where solitons live, are thermally unstable unless the laser is tuned at a suitable speed or the heating is otherwise compensated. The heating depends on the number of solitons, so thermal effects also govern which soliton states are reached and how one switches between them. Thermorefractive noise sets a floor on resonance frequency fluctuations that grows as the mode volume shrinks, and it can limit comb noise and stability.

**Resolved by.** The method used to reach the soliton state, such as tuning speed, power modulation or an auxiliary laser, stated with how reproducibly it works and how long the state is held without feedback; the thermal time constants or shifts relevant to the claim given; measured noise and stability compared with an estimate of thermorefractive noise for the stated geometry.

**Benchmark.** [4], [6], [7], [11], [12]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | Z. Abdallah, Y. G. Boucher, A. Fernandez, S. Balac and O. Llopis, Radio frequency spectral characterization and model parameters extraction of high Q optical resonators, Sci. Rep. 6, 27208 (2016) | doi:10.1038/srep27208 | full text | Results, analytical study: the same intensity profile arises in under- and over-coupling, and the phase profile tells them apart; loaded and intrinsic Q defined. Introduction: self-heating makes the resonance shape depend on scan direction; a semiconductor laser can be broader than a resonance at Q near 10^9; ring-down reveals the coupling regime but needs high Q and fitting of amplitude and phase |
| 2 | M. W. Puckett, K. Liu, N. Chauhan, Q. Zhao, N. Jin, H. Cheng, J. Wu, R. O. Behunin, P. T. Rakich, K. D. Nelson and D. J. Blumenthal, 422 Million intrinsic quality factor planar integrated all-waveguide resonator with sub-MHz linewidth, Nat. Commun. 12, 934 (2021) | doi:10.1038/s41467-021-21205-4 | full text | Results, "Q-factor, linewidth, and resonance splitting": Lorentzian fits give loaded and intrinsic linewidths; coupling regime inferred from design and extinction, critical coupling assumed to convert ring-down Q; interferometer free spectral range calibrated with phase-modulation sidebands and its uncertainty propagated; ring-down agrees with the spectral Q; resonance splitting attributed to scattering from defects or sidewall roughness, and the plotted Q values taken from non-split resonances. Results, "Loss reduction": photothermal shift can be comparable to the linewidth |
| 3 | Q.-F. Yang, Y. Hu, V. Torres-Company and K. Vahala, Efficient microresonator frequency combs, eLight 4, 18 (2024) | doi:10.1186/s43593-024-00075-5 | full text | "Principles of microcomb efficiency" and Box 1: efficiency defined as comb-line power over pump power excluding residual pump, and set by the loading factor, the ratio of coupling to total loss; red detuning of bright solitons prevents critical coupling; threshold inversely proportional to Q squared. Summary and outlook: the wall-plug efficiency of the pump components has to be quantified to judge total electrical power, and laser-to-resonator interface loss is named as a further loss |
| 4 | X. Jiang and L. Yang, Optothermal dynamics in whispering-gallery microresonators, Light Sci. Appl. 9, 24 (2020) | doi:10.1038/s41377-019-0239-6 | full text | Sections on thermal broadening and bistability: scanning up in wavelength gives a broadened triangular dip and scanning down a narrowed one; thermal self-locking works only on the blue-detuned slope; thermal tuning steps into soliton states; temperature fluctuations shift resonances and degrade stability |
| 5 | T. Herr, V. Brasch, J. D. Jost, I. Mirgorodskiy, G. Lihachev, M. L. Gorodetsky and T. J. Kippenberg, Mode spectrum and temporal soliton formation in optical microresonators, Phys. Rev. Lett. 113, 123901 (2014); read as arXiv:1311.1716 | doi:10.1103/PhysRevLett.113.123901 | full text | Fig. 2 and text: mode spectrum over more than 600 free spectral ranges from comb-calibrated diode laser spectroscopy, with dispersion and crossings read against an equidistant grid. Fig. 3: a family with anomalous dispersion but crossings near the pump did not form solitons. Fig. 4: crossings produce up-down spectral features; higher-order dispersion tolerated if the quadratic term dominates |
| 6 | T. Herr, V. Brasch, J. D. Jost, C. Y. Wang, N. M. Kondratiev, M. L. Gorodetsky and T. J. Kippenberg, Temporal solitons in optical microresonators, Nat. Photonics 8, 145–152 (2014); read as arXiv:1211.0733 | doi:10.1038/nphoton.2013.343 | full text | Main text: transmission steps linked to changes in soliton number; first step coincides with a change from a broad, noisy RF signal to a narrow beat note; sech-squared single-soliton spectrum; multi-soliton spectra structured; solitons on the effectively red-detuned branch, normally thermally unstable. Supplementary Sec. VI: soliton states reached only with an intermediate laser tuning speed. Supplementary Sec. VIII: autocorrelation can show spikes without pulses, so FROG was used |
| 7 | H. Guo, M. Karpov, E. Lucas, A. Kordts, M. H. P. Pfeiffer, V. Brasch, G. Lihachev, V. E. Lobanov, M. L. Gorodetsky and T. J. Kippenberg, Universal dynamics and deterministic switching of dissipative Kerr solitons in optical microresonators, Nat. Phys. 13, 94–102 (2017); read as arXiv:1601.05036, which carries a different title and author order | doi:10.1038/nphys3893 | full text | Results: forward tuning mostly gives multi-soliton states and backward tuning removes solitons one at a time, with soliton number from step heights; a phase-modulation probe read by a network analyser shows a double resonance in the soliton state and distinguishes blue-detuned, chaotic modulation-instability and soliton stages; thermal shift depends on soliton number and enables the switching |
| 8 | E. Lucas, M. Karpov, H. Guo, M. L. Gorodetsky and T. J. Kippenberg, Breathing dissipative solitons in optical microresonators, Nat. Commun. 8, 736 (2017); read as arXiv:1611.06567 | doi:10.1038/s41467-017-00719-w | full text | Results, experimental identification: breathers give a triangular averaged spectral envelope instead of sech-squared, sharp RF peaks at the breathing frequency and its harmonics, and sidebands on the repetition-rate beat note. Results, breathing region: breathing near the low-detuning edge of soliton existence. Discussion: breathing degrades stability and is to be avoided for low-noise combs |
| 9 | T. Herr, K. Hartinger, J. Riemensberger, C. Y. Wang, E. Gavartin, R. Holzwarth, M. L. Gorodetsky and T. J. Kippenberg, Universal formation dynamics and noise of Kerr-frequency combs in microresonators, Nat. Photonics 6, 480–487 (2012); read as arXiv:1111.3071, which carries a different title | doi:10.1038/nphoton.2012.127 | full text | Secs. III and IV: when primary lines are not spaced by an integer number of free spectral ranges, offset sub-combs form and give multiple and broad RF beat notes; noise characterised by beat notes, heterodyne with a reference comb, spectrally filtered beat notes and line-by-line frequency reconstruction |
| 10 | P. Del'Haye, A. Schliesser, O. Arcizet, T. Wilken, R. Holzwarth and T. J. Kippenberg, Optical frequency comb generation from a monolithic microresonator, Nature 450, 1214–1217 (2007); read as arXiv:0708.0611 | doi:10.1038/nature06401 | full text | Main text: equal mode spacing tested by beating lines against a reference fibre comb and by synchronous counting referenced to a hydrogen maser, the counting giving uniformity at the 10^-18 level relative to the optical carrier; synchronous counting needed because the spacing itself fluctuated |
| 11 | V. Brasch, E. Lucas, J. D. Jost, M. Geiselmann and T. J. Kippenberg, Self-referenced photonic chip soliton Kerr frequency comb, Light Sci. Appl. 6, e16202 (2017; the Crossref record is dated 2016) | doi:10.1038/lsa.2016.202 | full text | Results and discussion: f_CEO detected by 2f-3f interferometry from a spectrum of two-thirds of an octave without external broadening; repetition rate locked through pump power; counters referenced to an atomic clock; Allan deviation slope affected by counter type; instruments checked not to limit; out-of-loop comparison of the pump frequency with an independent fibre comb; soliton state reached by power kicking. Materials and methods: threshold quoted in the bus waveguide |
| 12 | G. Huang, E. Lucas, J. Liu, A. S. Raja, G. Lihachev, M. L. Gorodetsky, N. J. Engelsen and T. J. Kippenberg, Thermorefractive noise in silicon-nitride microresonators, Phys. Rev. A 99, 061801 (2019); read as arXiv:1901.07112, which carries a hyphenated title | doi:10.1103/PhysRevA.99.061801 | full text | Introduction: thermal noise limits microcomb offset-frequency noise and soliton applications. Sec. II: thermorefractive noise scales inversely with ring radius, and for a typical device with a 1 THz free spectral range the frequency fluctuation exceeds 1% of the linewidth. Sec. III: homodyne measurement with an absolute calibration tone and a power sweep to exclude photothermal effects |
