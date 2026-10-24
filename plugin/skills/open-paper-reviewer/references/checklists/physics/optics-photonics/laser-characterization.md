---
id: T-LASER-CHARACTERIZATION
name: Laser characterization
type: technique
field: physics/optics-photonics
applies_when: the paper claims lasing, or reports a laser's threshold, output power or efficiency, linewidth, frequency or phase noise, beam quality or M², or power or frequency stability, including claims of lasing from new gain materials, microcavities or nanolasers
version: "0.1"
---

# Laser characterization

Laser characterization is used to claim that a device lases and to report its threshold, output power and efficiency, spectral linewidth and frequency or phase noise, beam quality (usually as the beam propagation ratio M²) and stability. A claim of lasing must also be separated from amplified spontaneous emission (ASE), superluminescence and cavity-enhanced spontaneous emission, which share some of its signatures.

## 1. Threshold and the input-output curve

**Question.** Does the paper show output power against pump power over a wide range, on logarithmic as well as linear axes, state how the threshold was defined and extracted, and give the threshold as a density with the pumped area, pulse duration and absorbed fraction stated?

**Why it matters.** Several methods are in use for extracting a threshold, such as the onset of spectral narrowing or a change of slope in the output, and for amplified spontaneous emission thresholds they have been shown to give systematically different values from the same data, so a threshold without its method cannot be compared with others. A threshold given as a pulse energy or power, without the pumped area or the fraction absorbed, cannot be compared either. In small cavities that channel most spontaneous emission into the lasing mode (a spontaneous emission factor β near one), the kink in the input-output curve weakens or disappears.

**Resolved by.** An input-output curve that runs from well below to well above threshold on log-log axes; the threshold definition and fitting range stated; pump spot size, pulse duration, repetition rate and absorbed fraction given, with the threshold as a power or energy density; a gain and loss estimate showing that the measured threshold is physically reasonable.

**Benchmark.** [1], [2], [3]

## 2. Lasing against amplified spontaneous emission and cavity-modified emission

**Question.** Which alternative explanations for the spectral narrowing and the rise in output does the paper exclude, such as ASE or superluminescence from single-pass gain, directional scattering, or spontaneous emission reshaped by the cavity, and by which measurements?

**Why it matters.** Single-pass gain in a film or waveguide produces spectral narrowing and a superlinear rise above a pump threshold with no resonator at all, and a scattering gain medium can show strong narrowing above threshold without discrete modes. A cavity also narrows and redirects spontaneous emission below threshold. Narrowing and a kink together therefore do not show that feedback-driven oscillation has started.

**Resolved by.** Spectra below, near and above threshold on the same axes; discrete modes whose spacing and position match the cavity design and that narrow and grow above threshold; comparison with the same gain medium without the cavity, or with the feedback spoiled; the dependence of the emission on gain length or cavity size; an explicit statement of which alternatives were ruled out and how.

**Benchmark.** [1], [2], [3], [4]

## 3. Coherence and photon statistics

**Question.** Does the paper measure coherence beyond the spectrum, for example the second-order intensity correlation g(2)(0) as a function of pump, the coherence time or the polarization of the emission, and for correlation data is the detector timing resolution compared with the coherence time?

**Why it matters.** When the input-output curve is smooth, the change from thermal light (g(2)(0) = 2) to coherent light (g(2)(0) = 1) and the growth of the coherence time are what locate the onset of lasing. A correlation setup records the true correlation smeared by the detector response, so emission with a coherence time far below the timing resolution gives g(2)(0) near one even when it is thermal. A value near one above a supposed threshold is therefore not enough on its own.

**Resolved by.** g(2)(0) over a pump range that spans the transition, with the timing resolution stated and the response deconvolved or modelled; the coherence time or interference visibility against pump; the polarization of the emission below and above threshold.

**Benchmark.** [1], [3], [5]

## 4. Spectral linewidth and frequency noise

**Question.** How was the linewidth measured (grating spectrometer, beat note with a reference laser, delayed self-heterodyne interferometer or frequency-noise spectrum), is the instrument resolution stated and well below the quoted width, and is the quoted value identified as an intrinsic (Lorentzian) linewidth or as a width over a stated observation time?

**Why it matters.** A width close to the instrument resolution is an upper limit, not a measurement. Only white frequency noise gives a Lorentzian line; with flicker (1/f) frequency noise the linewidth grows with observation time, so a linewidth without that time is not well defined. Self-heterodyne data must be corrected for the response of the interferometer, and detector noise in that correction can create spurious features in the frequency-noise spectrum or hide the plateau from which the intrinsic linewidth is read.

**Resolved by.** The method, resolution, delay length and observation or integration time stated; the frequency-noise power spectral density shown over the relevant range of Fourier frequencies, with the white-noise level marked; intrinsic and integrated linewidths both given with their definitions; for spectrometer data, the resolution shown alongside the narrowest spectrum.

**Benchmark.** [1], [6], [7]

## 5. Beam quality and spatial mode

**Question.** For claims about beam quality, divergence or single-transverse-mode output, was M² obtained from second-moment beam widths measured at several planes through and beyond a focus, or was it inferred from a single profile, another width definition or a Gaussian fit?

**Why it matters.** M² is defined from the second-moment widths at the waist and in the far field. For beams that are not Gaussian, other width definitions, such as the 1/e² width, give different numbers. The waist position is rarely known in advance, which is why the standard method measures widths in about ten planes, half within one Rayleigh range of the waist and half beyond two, partly to make the result robust to background and measurement errors.

**Resolved by.** The width definition stated; the measured widths against position through the focus with the fit shown; background subtraction and the analysis region described; values for both transverse axes when the beam is not round; near-field and far-field images showing a well-defined beam above threshold.

**Benchmark.** [1], [8], [9]

## 6. Output power, efficiency and operating conditions

**Question.** Does the paper say which output power is quoted (peak or average, from one output or all of them, after which filters), which efficiency (slope efficiency, optical-to-optical, power-conversion or wall-plug efficiency, against incident or absorbed pump), and under which operating conditions (continuous-wave or pulsed, pulse duration and repetition rate, temperature)?

**Why it matters.** These quantities can differ by large factors for the same device, and a figure is only comparable with others when its definition is clear. Pulsed operation at low duty cycle avoids the heating that limits continuous-wave output, so the operating mode bears directly on the claim. Residual pump light or broadband spontaneous emission reaching the power meter adds to the apparent laser output.

**Resolved by.** The operating mode, temperature and pump conditions stated; power or pulse energy measured with a method suited to continuous-wave or pulsed beams, with pulse duration and repetition rate given when peak power is derived; the efficiency definition stated together with the pump power it uses; residual pump and spontaneous background removed or measured, for example by filtering and spectrally resolved power; a model estimate showing that the efficiency is physically reasonable.

**Benchmark.** [1], [10]

## 7. Stability, drift and operating lifetime

**Question.** For claims about power or frequency stability or about operating lifetime, does the paper state the record length, the averaging times and the statistic used, describe drift removal and the environment, and show how the output changed over the operating time?

**Why it matters.** For many noise types found in oscillators the ordinary standard deviation does not settle as the record grows, and any stability figure depends on the averaging time, so a single number without it cannot be compared. Deterministic drift and sensitivity to temperature or other conditions need to be separated from noise. Gain materials that degrade under pumping can lase for only a short time, which a short record does not reveal.

**Resolved by.** Power or frequency recorded over a stated duration and sampling interval; an Allan deviation, or a related variance, against averaging time with confidence intervals, or a phase-noise spectrum with its integration bandwidth; drift removal and environmental conditions described; output against operating time or number of pump pulses under stated conditions, with the time to a defined drop in output.

**Benchmark.** [1], [10], [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | Nature Research, Lasing Reporting Summary, reporting checklist for papers that claim lasing, version of March 2018 (2018); the official file is an interactive form, so the template text was read from the form data embedded in it | https://www.nature.com/documents/nr-lasing-reporting.pdf | full text | Item 1: output power against pump power over a wide range showing a clear threshold. Item 2: spectra below, around and above threshold showing narrowing, with spectrometer resolution stated. Item 3: coherence and/or polarization of the emission. Item 4: image or measurement of a well-defined beam above threshold. Item 5: continuous-wave or pulsed operation and temperature; threshold given as a density using the device area. Item 6: reasons why ASE, directional scattering or cavity-modified fluorescence are ruled out. Item 7: theoretical check that threshold, linewidth, gain-loss and efficiency are realistic. Item 8 (Statistics): number of devices tested, and statistical analysis of device performance and lifetime (time to failure) |
| 2 | S. Milanese, M. L. De Giorgi, L. Cerdán, M.-G. La-Placa, N. F. Jamaludin, A. Bruno, H. J. Bolink, M. V. Kovalenko and M. Anni, Amplified spontaneous emission threshold dependence on determination method in dye-doped polymer and lead halide perovskite waveguides, Molecules 27, 4261 (2022) | doi:10.3390/molecules27134261 | full text | Abstract and Introduction: ASE is characterized in thin films without any resonator providing feedback, and several different threshold definitions are in use, which hinders comparison. Conclusions: the seven most common methods give systematically different thresholds for every material tested, and the authors propose a standard procedure |
| 3 | W. W. Chow, F. Jahnke and C. Gies, Emission properties of nanolasers during the transition to lasing, Light Sci. Appl. 3, e201 (2014) | doi:10.1038/lsa.2014.82 | full text | "From conventional to nanolasers": as β approaches one the jump in output intensity vanishes. "Lasing criteria": debate over criteria without an intensity jump, and photon statistics must be examined. "Emission and coherence of nanolasers": g(2)(0) falls from about 2 to 1 at the transition, coherence time grows, and laser, cavity-enhanced LED and LED cases are compared. Conclusions: coherence time and g(2)(0) locate the threshold when the intensity curve is smooth |
| 4 | H. Cao, J. Y. Xu, S.-H. Chang and S. T. Ho, Transition from amplified spontaneous emission to laser action in strongly scattering media, Phys. Rev. E 61, 1985–1989 (2000); read as the author copy on the Cao laboratory website | doi:10.1103/PhysRevE.61.1985 | full text | Abstract and opening paragraphs: distinguishing ASE from lasing is crucial but sometimes difficult; in weakly scattering gain media a dramatic spectral narrowing occurs above a pump threshold while discrete lasing modes are missing, which is amplification of spontaneous emission without coherent feedback |
| 5 | S. T. Jagsch, N. Vico Triviño, F. Lohof, G. Callsen, S. Kalinowski, I. M. Rousseau, R. Barzel, J.-F. Carlin, F. Jahnke, R. Butté, C. Gies, A. Hoffmann, N. Grandjean and S. Reitzenstein, A quantum optical study of thresholdless lasing features in high-β nitride nanobeam cavities, Nat. Commun. 9, 564 (2018); read as the published version in Europe PMC, PMC5805739 | doi:10.1038/s41467-018-02999-2 | full text | Introduction: a correlation setup measures the correlation convolved with the detector response, so thermal bunching is resolved only when the coherence time approaches the detector resolution; measuring g(2)(0) = 1 above a supposed threshold is not sufficient proof of lasing, and the pump-dependent change from thermal to coherent emission is what matters. Results: measured traces fitted with the detector response and the timing resolution of the setup included |
| 6 | G. Di Domenico, S. Schilt and P. Thomann, Simple approach to the relation between laser frequency noise and laser line shape, Appl. Opt. 49, 4801–4807 (2010); read as the author copy in the University of Neuchâtel repository | doi:10.1364/AO.49.004801 | full text | Sec. 1: the frequency-noise spectral density carries more information than the linewidth; only white frequency noise gives a Lorentzian line; with 1/f noise the linewidth diverges with observation time. Secs. 3 and 4: the linewidth formula has a lower cut-off set by the measurement time, which matters for flicker noise |
| 7 | M. Kantner and L. Mertenskötter, Accurate evaluation of self-heterodyne laser linewidth measurements using Wiener filters, Opt. Express 31, 15994–16009 (2023); read as preprint arXiv:2301.10645 | doi:10.1364/OE.485866 | full text | Abstract and Sec. I: because of flicker noise the linewidth must be specified for a given measurement time; delayed self-heterodyne data must be corrected for the transfer function of the setup, and the standard correction, which ignores detector noise, creates spurious spikes in the frequency-noise spectrum and can hide the intrinsic linewidth plateau |
| 8 | International Organization for Standardization, ISO 11146-1:2021, Lasers and laser-related equipment, Test methods for laser beam widths, divergence angles and beam propagation ratios, Part 1: Stigmatic and simple astigmatic beams (2021); abstract read on the Standard Norge catalogue page | https://online.standard.no/en/iso-11146-1-2021 | abstract | Abstract: the standard specifies test methods for beam widths, divergence angles and beam propagation ratios, for stigmatic and simple astigmatic beams, with ISO 11146-2 for general astigmatic beams or beams of unknown type |
| 9 | M. H. Griessmann, A. C. Martinez-Becerril and J. S. Lundeen, A method to determine the M² beam quality from the electric field in a single plane, Opt. Continuum 2, 1833–1848 (2023); read as preprint arXiv:2305.07724 | doi:10.1364/OPTCON.494610 | full text | Sec. 1: ISO 11146 calls for intensity profiles at ten distances, partly to make the procedure robust to background and other measurement errors, and at prescribed distances from the waist. Sec. 2.1: widths are second-moment widths, which differ from the 1/e² width except for Gaussian beams. Sec. 2.2: the waist position is seldom known accurately, so the standard measures five planes on each side of the waist, half within one Rayleigh range and the rest beyond two |
| 10 | International Organization for Standardization, ISO 11554:2025, Optics and photonics, Lasers and laser-related equipment, Test methods for laser beam radiant power, radiant energy and temporal characteristics (2025); abstract read on the Standard Norge catalogue page | https://online.standard.no/en/iso-11554-2025 | abstract | Abstract: test methods for the radiant power and energy of continuous-wave and pulsed laser beams and their pulse shape, duration and repetition rate, and test and evaluation methods for power stability of continuous-wave lasers, energy stability of pulsed lasers and pulse duration stability |
| 11 | W. J. Riley, Handbook of Frequency Stability Analysis, NIST Special Publication 1065 (2008) | https://tf.nist.gov/general/pdf/2220.pdf | full text | Sec. 5: for many divergent noise types the standard variance does not converge, and the dependence of the variance on averaging time shows the noise type; Allan and related variances converge. Sec. 5.2.19: integrated phase jitter is stated over a bandwidth. Sec. 5.25: deterministic environmental effects must be separated from stochastic noise. Sec. 10.15: describe the setup and preprocessing and document analysis choices so results can be reproduced |
