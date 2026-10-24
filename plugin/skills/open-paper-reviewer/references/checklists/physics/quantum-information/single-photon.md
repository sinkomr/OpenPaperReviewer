---
id: T-SINGLE-PHOTON
name: Single-photon sources and detectors
type: technique
field: physics/quantum-information
applies_when: the paper reports a second-order correlation g(2), Hong-Ou-Mandel interference or photon indistinguishability, the brightness or efficiency of a single-photon or heralded source, or the efficiency, dark counts, afterpulsing, dead time or timing jitter of a single-photon detector
version: "0.1"
---

# Single-photon sources and detectors

Single-photon measurements are used to claim that a source emits one photon at a time, through the second-order intensity correlation g(2) measured in a Hanbury Brown and Twiss (HBT) set-up; that its photons are indistinguishable, through Hong-Ou-Mandel (HOM) two-photon interference; and that the source is bright or efficient. The same experiments rest on single-photon detectors, such as single-photon avalanche diodes (SPADs) and superconducting nanowire single-photon detectors (SNSPDs), whose detection efficiency, dark counts, afterpulsing, dead time and timing jitter are themselves often claimed or relied on.

## 1. How g(2)(0) was extracted

**Question.** How was the quoted g(2)(0) obtained (the area of the zero-delay peak relative to the side peaks for pulsed excitation, or the depth of the antibunching dip for continuous excitation), what sets the normalisation, and is the raw value given beside any value corrected for background, with the background fraction stated and the way it was measured?

**Why it matters.** Uncorrelated background light and dark counts push the measured g(2) towards one, and the usual correction divides by the square of the signal fraction, so a small error in that fraction gives a large change in the corrected value. A g(2)(0) below 0.5 is often taken to show a single emitter, but several emitters of unequal brightness can also give a value below 0.5, so the threshold alone does not count emitters.

**Resolved by.** The full correlation histogram shown out to delays long enough to include any bunching, with its normalisation stated (from the count rates, acquisition time and bin width, or from the long-delay level); the integration window for pulsed data stated and covering the whole peak; the raw g(2)(0) with its uncertainty reported first, and any corrected value labelled, with the signal-to-background ratio and how it was measured, for example off the emitter or from the power dependence; claims about the number of emitters supported by more than the 0.5 threshold.

**Benchmark.** [1], [2], [3]

## 2. Timing resolution and the instrument response

**Question.** Is the timing response of the detection system (detector jitter together with the timing electronics) measured and stated, and when the features of the correlation or lifetime trace are comparable to it, is that response included in the fit?

**Why it matters.** The measured correlation is the true one convolved with the instrument response, so a finite timing resolution fills in the antibunching dip and sets a floor on the g(2)(0) that can be measured even from an ideal source. Deconvolving the data amplifies noise, and a jitter quoted as a single width, often the full width at half maximum of a fitted Gaussian, does not describe the shape of the response away from its peak.

**Resolved by.** The instrument response measured with optical pulses much shorter than the jitter, shown or characterised by its full width and its tails; the bin width stated and the same for response and data; fits that convolve the model with the measured response, not deconvolved data; the shortest time constants in the fit compared with the response width.

**Benchmark.** [1], [6], [8], [9]

## 3. Coincidences created by the set-up

**Question.** Does the paper exclude coincidences that the apparatus itself can create: scattered excitation laser light, re-excitation of the emitter within one pulse, afterpulses, and light emitted by one detector during its breakdown reaching the other detector?

**Why it matters.** Laser light that leaks through the filters and re-excitation during a long pulse both add photons to the zero-delay peak, and because these extra photons overlap with the single photons to different degrees, the same g(2)(0) can lower the HOM visibility by different amounts. SPADs emit light when they fire, which can register in the other detector of an HBT or HOM set-up and produce spurious correlation peaks, and afterpulses add correlated false counts in a single detector.

**Resolved by.** The method of laser rejection stated (spectral, polarisation or spatial) with the residual laser contribution measured, for example with the collection placed off the emitter; the excitation pulse length compared with the emitter lifetime; two separate detectors used for cross-correlation, so that afterpulses and dead time of one detector do not shape the histogram near zero delay, with filtering or isolation between them and a check for crosstalk peaks.

**Benchmark.** [1], [3], [4], [7]

## 4. HOM visibility: reference, post-selection and corrections

**Question.** How was the HOM visibility defined and measured (which reference was used for distinguishable photons, such as crossed polarisation or added delay), were coincidences integrated over the whole photon wavepacket or within a narrow time window, and which corrections, for beam-splitter ratio, interferometer imperfection or non-zero g(2)(0), were applied and with what assumptions?

**Why it matters.** Restricting coincidences to a time window narrower than the wavepacket raises the visibility artificially, and the gap can be very large when the detector resolution is comparable to the coherence time. Correcting the visibility for multi-photon events assumes how the extra photons overlap with the single photons, and different assumptions give different indistinguishabilities, while the uncorrected value is the one that matters for applications.

**Resolved by.** The raw visibility from coincidences integrated over the full wavepacket, with the reference measurement described; any post-selected value labelled as such, with the window stated; the beam-splitter reflectivity and transmissivity measured and used explicitly; any value corrected for g(2)(0) labelled, given beside the uncorrected one, with the formula and its assumption about the noise photons stated.

**Benchmark.** [3], [4], [5]

## 5. Which photons were interfered

**Question.** Which photons does the quoted indistinguishability refer to: photons emitted a few nanoseconds apart by the same emitter, photons separated by longer delays, or photons from separate sources, and under what spectral filtering and excitation conditions?

**Why it matters.** Slow fluctuations of the emitter's environment make the emission energy wander from one photon to the next, so the indistinguishability depends on the delay between the interfering photons, and photons from separate emitters also suffer from uncorrelated noise. Visibility measured for consecutive photons therefore does not establish indistinguishability over the longer delays or between the separate sources that many applications need, and narrow spectral filtering can raise visibility at the cost of efficiency.

**Resolved by.** The delay between the interfering photons stated, with visibility measured at the delays relevant to the claim, or as a function of delay; for claims about separate sources, interference between those sources shown directly; the spectral filter width and its transmission stated alongside the visibility; excitation scheme and power the same as for the quoted purity and brightness.

**Benchmark.** [3], [5]

## 6. Brightness and efficiency definitions

**Question.** Where in the optical path is the quoted brightness or efficiency defined (at the first lens, in a single-mode fibre, at the detector or end to end), is it a probability per excitation pulse or a count rate, and which losses, including the detector efficiency, were divided out and how were they measured?

**Why it matters.** The efficiency of a single-photon source is not defined uniformly across the field, and figures quoted at the first lens, into a fibre or on a detector can differ greatly for the same device. An extraction efficiency depends on the numerical aperture of the collection optics and may or may not include the emitter's internal quantum efficiency and occupation probability. For heralded sources, brightness and multi-photon probability rise together with pump power, so purity and brightness quoted at different powers do not describe one operating point.

**Resolved by.** The measurement point named, with the numerical aperture and every transmission and detector efficiency used to infer it listed and measured, and the raw detected rate also given; the figure expressed as a probability per pulse at a stated repetition rate and excitation power; any correction for multi-photon emission or for detector dead time stated; brightness, g(2)(0) and visibility reported for the same operating conditions; for heralded sources, the heralding efficiency and the dependence of g(2)(0) on pump power.

**Benchmark.** [3], [5], [6]

## 7. Detector efficiency: definition and calibration

**Question.** Is the quoted detection efficiency a system efficiency, including coupling into the detector, or a device efficiency, and how was it calibrated (the reference detector or source, the attenuators and their calibration), with dark counts, afterpulses, polarisation and count rate taken into account?

**Why it matters.** System and device efficiency are equal only for perfect coupling, and the literature does not consistently report one or the other. A calibration with an attenuated laser depends on traceable power and attenuation measurements and on subtracting dark counts and afterpulses, and the efficiency can depend on the input polarisation, on the fibre connection and on the count rate.

**Resolved by.** The efficiency named as system or device efficiency, at a stated wavelength, bias and count rate; the calibration method stated, such as substitution against a calibrated power meter with calibrated attenuation or a correlated-photon method, with its uncertainty; dark counts and afterpulses subtracted; the polarisation dependence given, or the polarisation used stated; the dependence on count rate checked.

**Benchmark.** [8], [9], [10]

## 8. Dark counts, afterpulsing and dead time

**Question.** Are the dark count rate, afterpulse probability and dead time stated for the operating conditions actually used (bias, gating, temperature and optical shielding), and are they measured in a way that separates intrinsic dark counts from stray light and from afterpulses?

**Why it matters.** Dark counts include stray light reaching the detector as well as intrinsic events, and for SNSPDs the dark count rate rises steeply as the bias approaches the critical current, so efficiency and dark counts quoted at different biases do not describe one operating point. Afterpulses are correlated false counts that a simple count with the input blocked cannot separate from dark counts, and dead times, which for SPADs range from tens of nanoseconds to microseconds, reduce efficiency at high rates.

**Resolved by.** Dark count rate given at the same bias and temperature as the efficiency, with the input blocked under the operating optical conditions; afterpulse probability measured, for example from the distribution of times between events or with a double-pulse method; dead time and recovery time stated and compared with the count rates in the experiment.

**Benchmark.** [6], [8], [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | R. E. K. Fishman, R. N. Patel, D. A. Hopper, T.-Y. Huang and L. C. Bassett, Photon-emission-correlation spectroscopy as an analytical tool for solid-state quantum defects, PRX Quantum 4, 010202 (2023); read as arXiv:2111.01252 | doi:10.1103/PRXQuantum.4.010202 | full text | Sec. III.5: the g(2)(0) below 0.5 test can be met by several emitters of unequal brightness. Sec. IV.2: each bin normalised by the expected coincidences from the two count rates, acquisition time and bin width, with shot-noise uncertainty. Sec. V: bunching from non-radiative states, with the model returning to one at long delay. Sec. IV.3, Eqs. 20 and 21: background pushes g(2) towards one; the signal fraction is estimated off the emitter, from a spatial fit or from the power dependence. Sec. IV.4: the instrument response convolves with the true correlation; deconvolution amplifies noise, so fitting with the convolved response is preferred, with equal bin widths. Sec. IV.1: two detectors are used to see dynamics within the dead time |
| 2 | R. Brouri, A. Beveratos, J.-P. Poizat and P. Grangier, Photon antibunching in the fluorescence of individual color centers in diamond, Opt. Lett. 25, 1294–1296 (2000); read as arXiv:quant-ph/0007032 | doi:10.1364/OL.25.001294 | full text | Eq. 2 and following text: the background correction subtracts uncorrelated coincidences using the signal fraction rho = S/(S+B), dividing by its square; rho was measured separately in each run from a fit to a line scan across the emitter |
| 3 | P. Senellart, G. Solomon and A. White, High-performance semiconductor quantum-dot single-photon sources, Nat. Nanotechnol. 12, 1026–1039 (2017); read as the copy hosted by NIST | doi:10.1038/nnano.2017.218 | full text | Box 1: pulsed g(2)(0) from the zero-delay peak area; HOM visibility from parallel and distinguishable coincidences integrated over the whole pulse, as temporal post-selection artificially raises it; correction for beam-splitter R and T; the g(2)-corrected indistinguishability is common but the uncorrected one remains the relevant figure of merit. Section on brightness: efficiency is not defined uniformly, with count rates, collected photons per second and first-lens brightness in use; probability per pulse proposed; first-lens brightness as extraction times occupation times quantum efficiency. SPDC section: g(2)(0) rises with brightness. Indistinguishability section: spectral diffusion makes indistinguishability depend on the photon delay; laser rejection by spatial or polarisation separation; near-unity values obtained with zero-phonon-line filtering. Fig. 4b: fibre-output count rate shown with and without correction for detector dead time |
| 4 | H. Ollivier, S. E. Thomas, S. C. Wein, I. Maillette de Buy Wenniger, N. Coste, J. C. Loredo, N. Somaschi, A. Harouri, A. Lemaitre, I. Sagnes, L. Lanco, C. Simon, C. Anton, O. Krebs and P. Senellart, Hong-Ou-Mandel interference with imperfect single photon sources, Phys. Rev. Lett. 126, 063602 (2021); read as arXiv:2005.01743 | doi:10.1103/PhysRevLett.126.063602 | full text | Eqs. 1 and 2: HOM visibility depends on g(2)(0) and on the overlap between the single photons and the noise photons; the common correction assumes identical noise and gives a lower bound. Appendix A: general formula with beam-splitter R and T. Fig. 3 and text: laser leakage and re-excitation as sources of multi-photon noise with different overlap |
| 5 | T. Heindel, J.-H. Kim, N. Gregersen, A. Rastelli and S. Reitzenstein, Quantum dots for photonic quantum information technology, Adv. Opt. Photon. 15, 613–738 (2023); read as arXiv:2309.04229 | doi:10.1364/AOP.490091 | full text | Sec. 3.3: extraction efficiency defined for a lens of finite numerical aperture. Sec. 6.2: an extraction efficiency quoted into a stated numerical aperture of 0.4. Sec. 6.3: experimental extraction efficiencies often include the internal quantum efficiency; post-selected HOM visibilities are often quoted, limited by the set-up's timing resolution relative to the coherence time and not relevant for applications, with an example of 0.97 post-selected against 0.18 without post-selection. Sec. 8.2: separate emitters suffer uncorrelated charge noise and blinking |
| 6 | M. D. Eisaman, J. Fan, A. Migdall and S. V. Polyakov, Invited Review Article: Single-photon sources and detectors, Rev. Sci. Instrum. 82, 071101 (2011); read as the copy hosted by NIST | doi:10.1063/1.3610677 | full text | Sec. II.A: the detector time response sets the minimum g(2)(0) measurable even for an ideal source. Table I note: emission efficiency includes filtering and excludes the detector; for pair sources g(2)(0) increases with generation rate. Sec. II.C: heralded-path losses, false heralds from dark counts and stray light. Sec. III.A: definitions of detection efficiency, dark-count rate, dead time and timing jitter. Sec. III.B: SPAD afterpulsing from trapped carriers and dead times from tens of nanoseconds to 10 microseconds |
| 7 | C. Kurtsiefer, P. Zarda, S. Mayer and H. Weinfurter, The breakdown flash of silicon avalanche photodiodes: back door for eavesdropper attacks?, J. Mod. Opt. 48, 2039–2047 (2001); read as arXiv:quant-ph/0104103 | doi:10.1080/09500340108240905 | full text | Sec. 1: in HBT configurations the breakdown flash of one detector must not cause artificial events in the second. Sec. 3: coincidence histogram of two facing detectors shows crosstalk peaks from the flash |
| 8 | C. M. Natarajan, M. G. Tanner and R. H. Hadfield, Superconducting nanowire single-photon detectors: physics and applications, Supercond. Sci. Technol. 25, 063001 (2012); read as arXiv:1204.5560 | doi:10.1088/0953-2048/25/6/063001 | full text | Sec. 1.2: system detection efficiency includes coupling, device efficiency does not, and the literature has no consensus on which to report; dark counts include stray light and electrical noise. Fig. 3 caption and Sec. 2.3.1: jitter quoted as the FWHM of a Gaussian fitted to the instrument response measured with a femtosecond laser. Sec. 2.3.8: dark count rate rises exponentially as the bias approaches the critical current; non-uniform wires broaden the jitter |
| 9 | ETSI Industry Specification Group on Quantum Key Distribution, ETSI GS QKD 011 V1.1.1, Quantum Key Distribution (QKD); Component characterization: characterizing optical components for QKD systems (2016) | https://www.etsi.org/deliver/etsi_gs/QKD/001_099/011/01.01.01_60/gs_qkd011v010101p.pdf | full text | Clause 4.7, Table 4.3: row 2, dark counts measured without illumination, and a simple count cannot separate dark counts from afterpulses, while the distribution of times between events can; row 3, afterpulse probability by a double-pulse method; row 4, detection efficiency by substitution with a calibrated power meter and calibrated attenuator, correcting for dark counts and afterpulses, or by heralded photons; rows 5 and 6, linearity and polarisation dependence; rows 7 and 8, dead and recovery time; row 10, jitter from the instrument response measured with pulses much narrower than the jitter |
| 10 | T. Gerrits, A. Migdall, J. C. Bienfang, J. Lehman, S. W. Nam, J. Splett, I. Vayshenker and J. Wang, Calibration of free-space and fiber-coupled single-photon detectors, Metrologia 57, 015002 (2020) | doi:10.1088/1681-7575/ab4533 | abstract | Abstract: detection-efficiency calibration corrected for afterpulsing, dark counts and count-rate effects and interpolated to the operating count rate; fusion-spliced and connectorised fibre coupling compared; expanded uncertainties of about 0.7 to 1.8 percent |
