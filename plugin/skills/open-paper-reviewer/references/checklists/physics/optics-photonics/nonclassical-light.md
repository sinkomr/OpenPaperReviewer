---
id: T-NONCLASSICAL-LIGHT
name: Squeezed and non-classical light
type: technique
field: physics/optics-photonics
applies_when: the paper reports quadrature squeezing or anti-squeezing in dB, balanced homodyne measurements, sub-Poissonian or sub-shot-noise light, a Fano factor or Mandel Q parameter, or a Wigner function or density matrix of an optical mode reconstructed from homodyne or photon-counting data
version: "0.1"
---

# Squeezed and non-classical light

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

**Resolved by.** Noise spectra from the vacuum, squeezed and anti-squeezed traces over the band of interest, with all spectrum analyser settings given; for time-domain data, the detector bandwidth compared with the repetition rate and the correlation between consecutive samples shown to be small or corrected; the spatial and temporal mode of the LO and its overlap with the signal described; for heralded states, trigger dark counts stated and included, with the mode mismatch, in the effective efficiency; for a claimed single-photon Wigner negativity, an effective efficiency above one half shown.

**Benchmark.** [1], [3], [4], [6]

## 6. Sub-Poissonian statistics and the detector response

**Question.** For a claim of sub-Poissonian light from photon counting or photocurrent noise, is the nonclassicality criterion appropriate to the detector actually used (photon-number-resolving, click or multiplexed click detector, or linear photodiode), and are dead time, afterpulsing, saturation and detection efficiency included in the analysis?

**Why it matters.** The Mandel Q parameter computed from the clicks of on-off or multiplexed detectors can be negative even for classical light such as thermal light, because the click statistics are not the photon statistics. Dead time lowers the effective efficiency by an amount that depends on the number of counts, and afterpulses add counts that no photon caused, so the count statistics depend non-linearly on the light and their variance changes. Loss dilutes real sub-Poissonian statistics towards the Poissonian value but cannot create them, whereas a saturated detector can understate the noise.

**Resolved by.** A criterion proved for the detector model used, such as a binomial parameter for click detectors, or a photon-number distribution recovered with the detector's measured response; dead time, afterpulse probability and efficiency stated and included; a coherent or attenuated laser reference of the same mean intensity measured with the same detector and shown to give the value expected for classical light with that detector (binomial click statistics for click detectors, shot noise for a photodiode).

**Benchmark.** [4], [7], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. I. Lvovsky and M. G. Raymer, Continuous-variable optical quantum-state tomography, Rev. Mod. Phys. 81, 299 (2009); read as preprint arXiv:quant-ph/0511044 | doi:10.1103/RevModPhys.81.299 |
| 2 | J. Appel et al., Electronic noise in optical homodyne tomography, Phys. Rev. A 75, 035802 (2007); read as preprint arXiv:quant-ph/0610116 | doi:10.1103/PhysRevA.75.035802 |
| 3 | R. Kumar et al., Versatile wideband balanced detector for quantum optical homodyne tomography, Opt. Commun. 285, 5259 (2012); read as preprint arXiv:1111.4012 | doi:10.1016/j.optcom.2012.07.103 |
| 4 | R. Schnabel, Squeezed states of light and their applications in laser interferometers, Phys. Rep. 684, 1 (2017); read as preprint arXiv:1611.03986 | doi:10.1016/j.physrep.2017.04.001 |
| 5 | U. L. Andersen et al., 30 years of squeezed light generation, Phys. Scr. 91, 053001 (2016); read as preprint arXiv:1511.03250 | doi:10.1088/0031-8949/91/5/053001 |
| 6 | Y. Takeno et al., Observation of −9 dB quadrature squeezing with improvement of phase stability in homodyne measurement, Opt. Express 15, 4321 (2007); read as preprint arXiv:quant-ph/0702139 | doi:10.1364/OE.15.004321 |
| 7 | J. Sperling et al., Sub-binomial light, Phys. Rev. Lett. 109, 093601 (2012); read as preprint arXiv:1205.4669 | doi:10.1103/PhysRevLett.109.093601 |
| 8 | A. A. Semenov et al., Photocounting measurements with dead time and afterpulses in the continuous-wave regime, Phys. Rev. A 109, 013701 (2024); read as preprint arXiv:2303.14246 | doi:10.1103/PhysRevA.109.013701 |
