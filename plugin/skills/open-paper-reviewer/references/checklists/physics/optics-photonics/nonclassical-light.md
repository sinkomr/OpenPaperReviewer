---
id: T-NONCLASSICAL-LIGHT
name: Squeezed and non-classical light
type: technique
field: physics/optics-photonics
applies_when: the paper reports quadrature squeezing or anti-squeezing in dB, balanced homodyne measurements, sub-Poissonian or sub-shot-noise light, a Fano factor or Mandel Q parameter, or a Wigner function or density matrix of an optical mode reconstructed from homodyne or photon-counting data
version: "0.1"
---

# Squeezed and non-classical light

These measurements are used to claim that light has less noise than the shot-noise (vacuum) level in one quadrature, that its photon-number fluctuations are sub-Poissonian, or that an optical mode is in a particular quantum state with a given Wigner function or density matrix. Most of these claims rest on balanced homodyne detection (BHD), in which the signal is mixed with a bright local oscillator (LO) and the difference photocurrent gives a quadrature, or on photon counting, and all are stated relative to a noise reference that the experiment itself has to establish.

## 1. The shot-noise reference

**Question.** How was the vacuum or shot-noise level that the squeezing or noise reduction is quoted against measured (signal blocked, same LO power, same analysis frequency and settings), and does the paper show that this level scales linearly with LO power, or with optical power for direct detection?

**Why it matters.** Every squeezing figure is a ratio to the shot-noise level, and that level depends on the LO power and the electronic gain, so it has to be measured, not assumed. Classical LO noise that is not cancelled by the balanced subtraction grows with the square of the power and raises the apparent reference, while saturation of the detector makes noise grow too slowly; either one changes the ratio that is reported as squeezing.

**Resolved by.** A trace of the vacuum level taken under the same conditions as the squeezed trace; noise power plotted against LO power (or total optical power) over the range used, showing linear growth; the common-mode rejection of the balanced detector stated; for direct detection, an attenuation test showing that the noise falls in proportion to the power.

**Benchmark.** [1], [3], [4]

## 2. Electronic noise and its treatment

**Question.** What is the clearance of the shot-noise level above the detector's electronic (dark) noise at the analysis frequency, and was the electronic noise subtracted from the traces before the squeezing was quoted?

**Why it matters.** Electronic noise adds to every quadrature and acts on the measured state like an extra optical loss whose size is set by the clearance; a 6 dB clearance is equivalent to an efficiency of about 75%. Subtracting it changes the quoted squeezing, often by a few tenths of a dB at high squeezing levels, so a figure with the subtraction is a different quantity from one without it.

**Resolved by.** The clearance stated in dB at the analysis frequency and LO power used; the electronic noise trace shown; squeezing given both before and after any subtraction, with the subtraction labelled; where the result feeds a reconstruction, the electronic noise included as an equivalent loss.

**Benchmark.** [2], [3], [4], [6]

## 3. Directly measured versus loss-corrected values

**Question.** Is the headline squeezing or noise reduction the directly observed value, and if a value corrected for detection loss is also given, does the paper list each loss that was corrected (escape efficiency of the source, propagation loss, homodyne visibility, photodiode quantum efficiency) with how it was measured?

**Why it matters.** Loss mixes vacuum into the squeezed mode and reduces the observed squeezing, so a value inferred by dividing out losses can be many dB larger than what was measured. The inferred value is only as good as the efficiencies used: the homodyne visibility enters squared, and errors in any measured efficiency pass straight into the corrected figure.

**Resolved by.** The directly observed squeezing in the abstract and main text, with any corrected value labelled as inferred; a loss budget giving each efficiency, its measurement and its uncertainty; the total detection efficiency stated; agreement between the loss implied by the squeezing and anti-squeezing data and the loss budget measured separately.

**Benchmark.** [4], [5], [6]

## 4. Anti-squeezing and phase noise

**Question.** Does the paper report the anti-squeezed variance together with the squeezed one, at each pump power or setting, and does it state the phase fluctuation between the squeezed field and the LO, with a model that accounts for both?

**Why it matters.** Fluctuations of the measured quadrature angle mix part of the large anti-squeezed noise into the squeezed quadrature, so squeezing can fall as the pump power rises even when loss is unchanged. Reporting the squeezed variance alone hides how pure the state is and whether loss or phase noise limits it. The anti-squeezing in dB cannot be smaller than the squeezing, so a pair of values that breaks this relation indicates a problem with the noise reference or the data.

**Resolved by.** Squeezing and anti-squeezing plotted against pump power, fitted with a model that includes total efficiency and phase fluctuation, with the fitted values stated; the phase locking scheme and its residual phase noise described; any squeezing corrected for phase noise labelled as inferred.

**Benchmark.** [4], [6]

## 5. Analysis frequency, bandwidth and detected mode

**Question.** At which sideband frequency, resolution bandwidth and video bandwidth was the squeezing measured, is it shown over a frequency range and not only at its best point, and for pulsed or time-domain measurements, does the paper state the detector bandwidth, the temporal mode defined by the LO and how correlations between adjacent pulses were handled?

**Why it matters.** Squeezing from a cavity source varies with sideband frequency, falling beyond the cavity linewidth, and low frequencies carry technical noise from the laser and from back-scattered light, so a single best-frequency value does not describe the source. In pulsed BHD a detector response that spills into neighbouring pulses adds correlated noise and lowers the effective efficiency. Homodyne detection measures only the mode that matches the LO, so the detected mode is set by the LO, not by the signal.

**Resolved by.** Noise spectra from the vacuum, squeezed and anti-squeezed traces over the band of interest, with all spectrum analyser settings given; for time-domain data, the detector bandwidth compared with the repetition rate and the correlation between consecutive samples shown to be small or corrected; the spatial and temporal mode of the LO and its overlap with the signal described.

**Benchmark.** [1], [3], [4], [6]

## 6. Sub-Poissonian statistics and the detector response

**Question.** For a claim of sub-Poissonian light from photon counting or photocurrent noise, is the nonclassicality criterion appropriate to the detector actually used (photon-number-resolving, click or multiplexed click detector, or linear photodiode), and are dead time, afterpulsing, saturation and detection efficiency included in the analysis?

**Why it matters.** The Mandel Q parameter computed from the clicks of on-off or multiplexed detectors can be negative even for classical light such as thermal light, because the click statistics are not the photon statistics. Dead time lowers the effective efficiency by an amount that depends on the number of counts, and afterpulses add counts that no photon caused, so the count statistics depend non-linearly on the light and their variance changes. Loss dilutes real sub-Poissonian statistics towards the Poissonian value but cannot create them, whereas a saturated detector can understate the noise.

**Resolved by.** A criterion proved for the detector model used, such as a binomial parameter for click detectors, or a photon-number distribution recovered with the detector's measured response; dead time, afterpulse probability and efficiency stated and included; a coherent or attenuated laser reference of the same mean intensity measured with the same detector and shown to give the value expected for classical light with that detector (binomial click statistics for click detectors, shot noise for a photodiode).

**Benchmark.** [4], [8], [9]

## 7. Reconstruction of the quantum state

**Question.** For a reconstructed Wigner function or density matrix, does the paper state how the quadrature phase was known for each data point, which estimator was used, where the photon-number space was truncated, and whether the detection efficiency was built into the reconstruction or corrected afterwards, and is the state reconstructed without efficiency correction also shown?

**Why it matters.** Features such as Wigner negativity are reduced by every source of inefficiency, including mode mismatch and electronic noise, and for a single photon they vanish below an effective efficiency of one half, so negativity that appears only after correction rests on the assumed efficiency. Inverting the loss after reconstruction can produce unphysical large elements at high photon number, and inverse Radon methods can give negative populations, while a truncated maximum-likelihood estimate assumes the state has no weight above the cut-off.

**Resolved by.** The phase reference and how each quadrature value was assigned its phase; the estimator, the truncation and a check that the result does not change when the truncation is raised; the efficiency value used, how it was measured and whether it entered the measurement operators; reconstructions with and without efficiency correction side by side; for heralded states, the heralding rate, trigger dark counts and LO mode matching given.

**Benchmark.** [1], [2], [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | A. I. Lvovsky and M. G. Raymer, Continuous-variable optical quantum-state tomography, Rev. Mod. Phys. 81, 299–332 (2009); read as preprint arXiv:quant-ph/0511044 | doi:10.1103/RevModPhys.81.299 | full text | Sec. II.A: the LO pulse defines the detected spatiotemporal mode. Sec. III.B: efficiency built into the maximum-likelihood measurement operators; inverse Bernoulli correction can give unphysical high-number elements; truncation equivalent to assuming the signal intensity is limited. Sec. IV.A: shot noise distinguished from classical LO noise and electronic noise by its scaling with LO power; balancing needed to cancel classical LO noise; electronic noise equivalent to loss; bandwidth requirement for pulsed detection. Sec. IV.B and V.A: mode mismatch and trigger dark counts reduce effective efficiency; single-photon Wigner negativity needs effective efficiency above 0.5 |
| 2 | J. Appel, D. Hoffman, E. Figueroa and A. I. Lvovsky, Electronic noise in optical homodyne tomography, Phys. Rev. A 75, 035802 (2007); read as preprint arXiv:quant-ph/0610116 | doi:10.1103/PhysRevA.75.035802 | full text | Eqs. 4 to 14: with the vacuum calibration taken including electronic noise, the noise acts as an optical attenuator with equivalent efficiency (S−1)/S set by the shot-to-electronic noise ratio S; about 75% for 6 dB of clearance |
| 3 | R. Kumar, E. Barrios, A. MacRae, E. Cairns, E. H. Huntington and A. I. Lvovsky, Versatile wideband balanced detector for quantum optical homodyne tomography, Opt. Commun. 285, 5259–5267 (2012); read as preprint arXiv:1111.4012 | doi:10.1016/j.optcom.2012.07.103 | full text | Sec. I: shot-to-electronic noise ratio and common-mode rejection ratio among the main detector criteria; the common-mode rejection ratio measures rejection of classical LO noise and is bounded by blocking one photodiode. Sec. II.A: electronic noise equivalent to optical loss; clearance of shot noise over electronic noise a primary detector characteristic. Sec. II.B: in time-domain detection the response spilling into neighbouring pulses lowers effective efficiency and shows up as correlations between consecutive samples, which can be corrected. Sec. IV: shot noise verified by detector output power growing linearly with LO power; spectra taken with and without LO |
| 4 | R. Schnabel, Squeezed states of light and their applications in laser interferometers, Phys. Rep. 684, 1–51 (2017); read as preprint arXiv:1611.03986 | doi:10.1016/j.physrep.2017.04.001 | full text | Sec. 2.2: the vacuum level depends on power and electronic gain and must be measured; attenuation test separates shot noise from classical noise and saturation. Sec. 2.3: vacuum reference measured by blocking the squeezed signal; squeezing falls at high frequency from the cavity linewidth and at low frequency from technical noise and back-scattered light; dark noise subtracted in shown traces; anti-squeezing always above the magnitude of squeezing, from the uncertainty relation and loss. Sec. 2.5: lost photons and dark counts wash out photon-number features; arrays of single-photon detectors used to resolve photon number. Sec. 3.1: loss mixes vacuum into the squeezed mode; list of loss sources. Secs. 4.4 and 4.4.1: back-scattered light limits low-frequency squeezing; phase noise mixes the squeezed mode with itself at a fluctuating squeeze angle; dark noise 28 dB below shot noise still cost 0.3 dB |
| 5 | U. L. Andersen, T. Gehring, C. Marquardt and G. Leuchs, 30 years of squeezed light generation, Phys. Scr. 91, 053001 (2016); read as preprint arXiv:1511.03250 | doi:10.1088/0031-8949/91/5/053001 | full text | Sec. II (parametric down-conversion): intra-cavity loss, detection loss and phase noise named as the limits on squeezing; escape efficiency of the source defined; detection loss mainly from photodiode quantum efficiency and homodyne visibility, both needed close to 100% to measure high squeezing |
| 6 | Y. Takeno, M. Yukawa, H. Yonezawa and A. Furusawa, Observation of −9 dB quadrature squeezing with improvement of phase stability in homodyne measurement, Opt. Express 15, 4321–4327 (2007); read as preprint arXiv:quant-ph/0702139 | doi:10.1364/OE.15.004321 | full text | Experiment section, Eqs. 1 and 2: observed squeezing and anti-squeezing modelled with escape, propagation, visibility (squared) and quantum efficiencies and a phase fluctuation that mixes anti-squeezing into the squeezed quadrature. Results and discussions section and Fig. 3: raw value reported separately from values with circuit noise subtracted and with phase noise removed; analysis frequency, resolution and video bandwidths stated; loss from the fit compared with the measured loss budget; squeezing and anti-squeezing against pump power, with observed squeezing degrading at high pump through phase fluctuation |
| 7 | A. I. Lvovsky, Iterative maximum-likelihood reconstruction in quantum homodyne tomography, J. Opt. B: Quantum Semiclass. Opt. 6, S556–S559 (2004); read as preprint arXiv:quant-ph/0311097 | doi:10.1088/1464-4266/6/6/014 | full text | Efficiency modelled as a beam splitter and included in the measurement operators, avoiding the unphysical elements of a later inverse correction; Fock-space truncation justified by bounded intensity; inverse Radon reconstruction gave negative diagonal elements in the example |
| 8 | J. Sperling, W. Vogel and G. S. Agarwal, Sub-binomial light, Phys. Rev. Lett. 109, 093601 (2012); read as preprint arXiv:1205.4669 | doi:10.1103/PhysRevLett.109.093601 | full text | Sec. I and III: the Mandel Q parameter from click detectors can be negative for classical light, shown for thermal light. Sec. II: coherent light gives binomial click statistics; a binomial parameter that is non-negative for all classical light certifies nonclassicality |
| 9 | A. A. Semenov, J. Samelin, Ch. Boldt, M. Schünemann, C. Reiher, W. Vogel and B. Hage, Photocounting measurements with dead time and afterpulses in the continuous-wave regime, Phys. Rev. A 109, 013701 (2024); read as preprint arXiv:2303.14246 | doi:10.1103/PhysRevA.109.013701 | full text | Abstract and Sec. I: dead time and afterpulses make pulse statistics non-linear in the quantum state; click statistics of split detectors can be sub-Poissonian for classical light. Sec. II: dead time lowers the effective efficiency in a way that depends on the count number |
