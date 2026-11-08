---
id: T-PHOTODETECTORS
name: Photodetectors
type: technique
field: physics/optics-photonics
applies_when: the paper reports responsivity, external quantum efficiency, gain, noise-equivalent power, specific detectivity, response time, bandwidth or linear dynamic range of a light detector, or bases a claim of high sensitivity, broadband or fast detection on them
version: "0.1"
---

# Photodetectors

## 1. Incident power and illuminated area

**Question.** How was the optical power reaching the active area found: was the source measured with a calibrated reference detector, what area was taken as illuminated for the device and for the reference, and was the beam smaller than, matched to or larger than the active area?

**Why it matters.** Responsivity and EQE are only as good as the incident power, and power estimated from a laser spot size and a nominal power density can carry large errors. A beam larger than the active area without an aperture can collect photocurrent from light absorbed outside it and overstate responsivity, while a small spot samples only part of a device whose response varies across its surface. Antennas, electrode edges and lateral collection can make the effective optical area differ from the drawn area.

**Resolved by.** The incident power measured, and monitored during the measurement, with a calibrated reference detector at the same wavelength; an aperture or mask defining an illuminated area close to the active area, with uniform irradiance; the area used for normalisation stated and justified for the device geometry; where the effective area is uncertain, a scanning photocurrent map showing where the signal is collected.

**Benchmark.** [1], [2], [6]

## 2. External quantum efficiency above unity and gain

**Question.** When EQE exceeds 100% or responsivity exceeds what one carrier per photon allows at that wavelength, does the paper name the gain mechanism (photoconductive gain, photogating by trapped charge, photomultiplication, avalanche), show evidence for it, and keep EQE and gain apart?

**Why it matters.** EQE counts collected carriers per incident photon, while gain counts collected carriers per photogenerated electron-hole pair, so the two are not interchangeable. In a photoconductor the gain is the ratio of carrier lifetime to transit time, and trapped charge that gates the channel can raise it by orders of magnitude. A large apparent EQE in a device with injecting contacts therefore does not by itself show better detection, because the same mechanism raises noise and slows the response.

**Resolved by.** The mechanism identified with supporting measurements, such as the dependence on bias, light level and modulation frequency, transfer curves under illumination for photogating, or internal quantum efficiency from the measured absorption; gain reported together with its effect on noise and speed, not as a stand-alone figure; no comparison of a gain device with a gain-free device on EQE alone.

**Benchmark.** [1], [2], [4]

## 3. Detection mechanism and thermal signals

**Question.** Does the paper show whether the photoresponse is photoelectric (photovoltaic or photoconductive) or thermal (bolometric or photothermoelectric), for example from its sign, bias dependence, spatial map and spectral response?

**Why it matters.** Heating by absorbed light changes the conductance of a biased sample (bolometric effect) or drives a current across a junction of materials with different Seebeck coefficients (photothermoelectric effect), and either can be mistaken for photocarrier generation. The mechanisms differ in their current-voltage behaviour, spatial pattern and wavelength dependence, and each changes how responsivity, speed and broadband response should be read.

**Resolved by.** Photocurrent against bias, including zero bias, with the sign and its origin explained; scanning photocurrent maps locating the signal at junctions, contacts or the channel; spectral response compared with the absorption and the band gap; a time or frequency response consistent with the proposed mechanism.

**Benchmark.** [2], [4]

## 4. Responsivity against light level and linear dynamic range

**Question.** At what incident power is each responsivity or EQE quoted, is the photocurrent shown against power over the range used, and is the linear dynamic range found from measured deviation from a unit slope, with that slope reported?

**Why it matters.** In devices with trap-assisted gain the photocurrent often grows sublinearly with power, so responsivity is highest at the lowest light level and a value taken there does not hold at working intensities. A straight line on a log-log plot with a slope other than one is a power law, not linear response. Taking the limits of the linear range as the dark current, the noise floor or the smallest and largest currents measured, instead of measuring where linearity is lost, misstates the range.

**Resolved by.** Photocurrent against incident power on log-log axes with the fitted slope; the power at which each quoted responsivity applies; LDR limits set where the local slope departs from one by a stated tolerance, with the formula given; a range limited by the apparatus labelled as a lower bound; for non-linear detectors, no LDR quoted.

**Benchmark.** [1], [2], [4], [5]

## 5. Noise measured, not assumed

**Question.** Is the noise used for NEP and D* a measured noise current or noise spectral density at the operating bias and frequency, with the instrument noise floor shown, or is it calculated from the dark current as shot noise?

**Why it matters.** Shot noise from the dark current is rarely the dominant noise in emerging detectors. Flicker (1/f) noise and generation-recombination noise, which grows with photoconductive gain, can be far larger, so a shot-noise estimate can overstate detectivity by orders of magnitude. Turning a noise spectral density into a root-mean-square current by multiplying by the bandwidth is valid only where the noise is white.

**Resolved by.** The noise spectral density plotted against frequency for the device and for the measurement system, at the bias used for the responsivity; the noise at the frequency and over the bandwidth of the quoted figure; the gain included where it raises the noise; any calculated noise labelled as theoretical and not used to compare with measured values from other work.

**Benchmark.** [1], [2], [3]

## 6. NEP and specific detectivity: frequency, bandwidth and area

**Question.** Are NEP and D* computed from responsivity and noise taken at the same modulation frequency, bias and bandwidth, with responsivity measured near the NEP level, and does the paper show that the noise scales with the square root of area and bandwidth before quoting an area-normalised D*?

**Why it matters.** NEP depends on the frequency and bandwidth at which signal and noise are taken, and combining a low-frequency responsivity with high-frequency noise mixes two operating points. D* removes area and bandwidth only if the noise current scales with the square root of both: the area scaling holds for shot-noise-limited vertical photodiodes without gain but not in general, and the bandwidth scaling holds only for white noise. A wrong effective area enters D* directly.

**Resolved by.** The frequency, bandwidth and bias stated for every NEP and D*; responsivity and noise measured at matched conditions, with responsivity checked at low power; a test of the area scaling, for example on devices of different size, or else detectivity or NEP quoted at a stated bandwidth instead of D*; values that rest on assumptions labelled as apparent.

**Benchmark.** [1], [2]

## 7. Response time and bandwidth

**Question.** How were rise and fall times or the 3 dB bandwidth measured, does the transient reach a steady plateau that agrees with the continuous-wave responsivity, and are speed and gain reported for the same device and conditions?

**Why it matters.** Rise and fall times read from a signal that never settles, or from a modulation too fast for the slow part of the response, understate the response time. Speed depends on bias, load, background light and wavelength, and the textbook link between rise time and bandwidth holds only for a first-order system. In photoconductive detectors gain and speed are both set by the carrier lifetime, so high gain usually comes with slow, sometimes persistent, response.

**Resolved by.** Full periodic transients with a stable plateau, rise and fall times defined (10 to 90%), and the load, bias and light level given; frequency response with a flat low-frequency region before the 3 dB point, and modulated responsivity or EQE taken at a frequency within that flat region; speed measured at several light levels within the linear range; the gain-bandwidth product, not gain alone, used as the benchmark for gain devices.

**Benchmark.** [1], [2], [3]

## 8. One operating point for all figures of merit

**Question.** Are responsivity, EQE, dark current, noise, detectivity, speed and dynamic range reported at one stated bias, wavelength, temperature and modulation frequency, or is each best value taken under different conditions?

**Why it matters.** Responsivity, noise and speed all change with bias, light level, wavelength and temperature, and a gain mechanism that raises responsivity also raises noise and slows the response. Combining the best responsivity from one condition with the lowest noise or fastest response from another describes no real operating point and overstates the device.

**Resolved by.** A table of all figures of merit at a common bias, with wavelength, temperature, modulation frequency and bandwidth stated for each; dark current and responsivity checked before and after noise and transient measurements; comparisons with other work made at matched conditions and for the same kind of measured, not calculated, value.

**Benchmark.** [1], [3]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | V. Pecunia et al., Guidelines for accurate evaluation of photodetectors based on emerging semiconductor technologies, Nat. Photon. 19, 1178 (2025) | doi:10.1038/s41566-025-01759-1 |
| 2 | F. Wang et al., How to characterize figures of merit of two-dimensional photodetectors, Nat. Commun. 14, 2224 (2023) | doi:10.1038/s41467-023-37635-1 |
| 3 | G. Konstantatos, Current status and technological prospect of photodetectors based on two-dimensional materials, Nat. Commun. 9, 5266 (2018) | doi:10.1038/s41467-018-07643-7 |
| 4 | M. Buscema et al., Photocurrent generation with two-dimensional van der Waals semiconductors, Chem. Soc. Rev. 44, 3691 (2015) | doi:10.1039/C5CS00106D |
| 5 | H. T. Chandran et al., Deriving the linear dynamic range of next-generation thin-film photodiodes: pitfalls and guidelines, Appl. Phys. Lett. 124, 101113 (2024) | doi:10.1063/5.0184847 |
| 6 | T. C. Larason and S. S. Bruce, Spatial uniformity of responsivity for silicon, gallium nitride, germanium, and indium gallium arsenide photodiodes, Metrologia 35, 491 (1998) | doi:10.1088/0026-1394/35/4/48 |
