---
id: T-SINGLE-PHOTON
name: Single-photon sources
type: technique
field: physics/quantum-information
applies_when: the paper reports a second-order correlation g(2), Hong-Ou-Mandel interference or photon indistinguishability, or the brightness or efficiency of a single-photon or heralded source
version: "0.1"
---

# Single-photon sources

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

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | R. E. K. Fishman et al., Photon-emission-correlation spectroscopy as an analytical tool for solid-state quantum defects, PRX Quantum 4, 010202 (2023); read as arXiv:2111.01252 | doi:10.1103/PRXQuantum.4.010202 |
| 2 | R. Brouri et al., Photon antibunching in the fluorescence of individual color centers in diamond, Opt. Lett. 25, 1294 (2000); read as arXiv:quant-ph/0007032 | doi:10.1364/OL.25.001294 |
| 3 | P. Senellart et al., High-performance semiconductor quantum-dot single-photon sources, Nat. Nanotechnol. 12, 1026 (2017); read as the copy hosted by NIST | doi:10.1038/nnano.2017.218 |
| 4 | H. Ollivier et al., Hong-Ou-Mandel interference with imperfect single photon sources, Phys. Rev. Lett. 126, 063602 (2021); read as arXiv:2005.01743 | doi:10.1103/PhysRevLett.126.063602 |
| 5 | T. Heindel et al., Quantum dots for photonic quantum information technology, Adv. Opt. Photon. 15, 613 (2023); read as arXiv:2309.04229 | doi:10.1364/AOP.490091 |
| 6 | M. D. Eisaman et al., Invited Review Article: Single-photon sources and detectors, Rev. Sci. Instrum. 82, 071101 (2011); read as the copy hosted by NIST | doi:10.1063/1.3610677 |
| 7 | C. Kurtsiefer et al., The breakdown flash of silicon avalanche photodiodes: back door for eavesdropper attacks?, J. Mod. Opt. 48, 2039 (2001); read as arXiv:quant-ph/0104103 | doi:10.1080/09500340108240905 |
| 8 | C. M. Natarajan et al., Superconducting nanowire single-photon detectors: physics and applications, Supercond. Sci. Technol. 25, 063001 (2012); read as arXiv:1204.5560 | doi:10.1088/0953-2048/25/6/063001 |
| 9 | ETSI Industry Specification Group on Quantum Key Distribution, ETSI GS QKD 011 V1.1.1, Quantum Key Distribution (QKD); Component characterization: characterizing optical components for QKD systems (2016) | https://www.etsi.org/deliver/etsi_gs/QKD/001_099/011/01.01.01_60/gs_qkd011v010101p.pdf |
