---
id: T-PULSE-CHARACTERIZATION
name: Ultrafast pulse characterization
type: technique
field: physics/optics-photonics
applies_when: the paper reports an ultrashort pulse duration, chirp, spectral phase or temporal shape, measures pulses by autocorrelation, frequency-resolved optical gating, spectral interferometry, SPIDER or a related method, or bases a claim on pulse compression or a pulse-derived peak intensity
version: "0.1"
---

# Ultrafast pulse characterization

Ultrafast pulse characterization is used to claim the duration, temporal shape, chirp and spectral phase of pulses from picoseconds down to a few optical cycles, and from them compression towards the transform limit (the shortest duration the measured spectrum allows), peak power and the time resolution of experiments. The common methods are intensity and interferometric autocorrelation, frequency-resolved optical gating (FROG), spectral interferometry (SI) and spectral phase interferometry for direct electric-field reconstruction (SPIDER), and only some of them recover the full field.

## 1. Autocorrelation and the assumed pulse shape

**Question.** When a duration is derived from an autocorrelation, does the paper show the full trace including any wings or pedestal, state the pulse shape assumed and the deconvolution factor used, justify that shape, and compare the result with the transform-limited duration of the measured spectrum?

**Why it matters.** An intensity autocorrelation does not determine the pulse intensity: quite different pulses give nearly the same trace, and the conversion to a duration rests on a shape, such as a Gaussian or a squared hyperbolic secant, that is assumed rather than measured, with factors that differ markedly between shapes. The trace is symmetric and carries no phase, so it cannot distinguish chirp or the direction of time; adding the measured spectrum still does not determine the pulse, the spectrum alone fixes only the shortest possible duration, and an interferometric autocorrelation still has to be fitted to a guessed field.

**Resolved by.** The raw trace over a delay range wide enough to show the baseline on both sides; the assumed shape and factor stated, with the duration presented as an estimate under that assumption; the measured spectrum and its transform-limited duration given for comparison; where the shape, chirp or pedestal matters to the claim, a method that recovers intensity and phase.

**Benchmark.** [1], [2]

## 2. Coherent artefact and pulse-train stability

**Question.** Was the measurement averaged over many pulses, and does the paper show that the pulse train is stable in shape, so that a narrow central feature or a stable component is not taken for the pulse?

**Why it matters.** Averaging over a train of pulses whose shape varies, or measuring a single complicated pulse, gives an autocorrelation with a narrow coherence spike on a broader pedestal, and the pulse length corresponds to the pedestal, not the spike. When the spike is only about twice as narrow as the base the two blend into what looks like a clean trace, and the duration can be underestimated by a factor of two or more. Interferometric methods such as SPIDER and SI return only the stable component of an unstable train, which can give a much shorter average duration; in FROG the instability shows up as disagreement between measured and retrieved traces.

**Resolved by.** Raw traces shown over their full delay range, with any pedestal visible; for multi-shot measurements, a method that reveals instability, such as FROG with measured and retrieved traces compared, or single-shot measurements; for interferometric methods, a reference whose stability was established by such a method and fringe visibility consistent with a stable train; sources prone to instability, such as overpumped lasers, sources at the edge of current technology, semiconductor lasers and passively mode-locked combs, tested rather than assumed stable.

**Benchmark.** [1], [3]

## 3. Agreement between measured and retrieved traces

**Question.** For FROG and other methods that retrieve the pulse iteratively, does the paper show the measured and retrieved traces side by side, give the retrieval error together with the grid size, show that the whole trace was recorded, and compare the trace marginal or the retrieved spectrum with an independently measured spectrum?

**Why it matters.** A FROG trace has many more data points than the pulse has unknowns, so close agreement between measured and retrieved traces is the main evidence that the data are free of systematic error, and poor agreement points to systematic error, an unstable train or a cropped trace. The size of the retrieval error depends on the grid size and on the complexity of the pulse, so a value without its grid cannot be judged. The result is reliable only if the measured trace contains all of its non-zero values in delay and frequency, and a cropped trace is a common cause of poor retrieval.

**Resolved by.** Measured and retrieved traces shown on the same scale; the root-mean-square retrieval error stated with the grid size; a trace that falls to zero at its edges in delay and frequency; the frequency marginal or retrieved spectrum agreeing with a separately measured spectrum; any correction applied to the trace stated.

**Benchmark.** [1], [2]

## 4. Bandwidth and geometry of the measuring device

**Question.** Is the nonlinear crystal or medium thin enough to convert the whole spectrum of the pulse, is the spectral response of the device corrected where it matters, and, for pulses of a few optical cycles, does the beam geometry avoid geometrical smearing and dispersion in optics before the nonlinear medium?

**Why it matters.** A crystal whose phase-matching bandwidth is narrower than the pulse spectrum filters the signal; in a FROG trace this narrows the spectral axis, and autocorrelators carry the same requirement but have no internal check that shows when it is violated. Crossing the beams at an angle while scanning the delay samples a range of delays on each shot and lengthens the measured pulse by at least a fraction of a cycle, and glass before the nonlinear medium disperses and distorts a very broadband pulse.

**Resolved by.** Crystal material and thickness stated and shown to be adequate for the pulse bandwidth; the treatment of the spectral response of the nonlinear process described; beam geometry, crossing angle and the optics in the beam before the nonlinear medium given; for pulses of a few cycles, a collinear or single-shot geometry free of smearing, with reflective focusing and thin beam splitters.

**Benchmark.** [1], [2]

## 5. Direction of time, sign of chirp and separated pulses

**Question.** When the paper reports the sign of chirp or of higher-order phase, or whether a satellite pulse leads or trails, does the method determine the direction of time, and if not, how was the ambiguity removed?

**Why it matters.** An intensity autocorrelation and a second-harmonic FROG trace are symmetric in delay, so a pulse and its time-reversed copy give the same data and the sign of chirp and the order of satellite pulses are not determined. Second-harmonic FROG also cannot distinguish relative phases differing by π between well-separated pulses, and adding the spectrum does not remove this; when the gate is an independent pulse, the relative phase of well-separated pulses is left entirely undetermined.

**Resolved by.** A method without the time-direction ambiguity, or a second measurement after adding known dispersion, such as glass placed before the beam splitter, with only one direction of time consistent with both; or a stated and justified prior about the pulse; any relative phase between separated pulses reported together with the ambiguity of the method used.

**Benchmark.** [1], [2]

## 6. Reference pulse and calibration in interferometric methods

**Question.** For SI, is the reference pulse fully measured, does its spectrum cover that of the unknown pulse, and are the delay and spectrometer resolution suitable; for SPIDER and its variants, how were the spectral shear and the delay calibrated?

**Why it matters.** SI returns only the phase difference between the test and reference pulses, so an error in the reference phase passes directly into the result, and the phase is defined only where both spectra are non-zero. The delay must be long enough to separate the components of the interferogram in the Fourier domain and short enough for the spectrometer to resolve the fringes, and the filtering step costs spectral resolution. In SPIDER the retrieved phase depends on the spectral shear and on removal of the delay term, and without a calibration measurement the analysis does not give meaningful results.

**Resolved by.** How the reference pulse was measured; its spectrum shown together with the unknown spectrum; the delay and spectrometer resolution stated; for SPIDER, the shear value and how it was measured, and a calibration trace recorded with the same beam-splitting arrangement.

**Benchmark.** [1]

## 7. Spatial variation of the pulse and where it was measured

**Question.** Does the paper say where in the beam and at which plane the pulse was measured (on axis or integrated over the beam, at focus or in the collimated beam), and, where a claim concerns the pulse at a focus or across a large beam, does it test for spatio-temporal couplings such as pulse-front tilt, spatial chirp or pulse-front curvature?

**Why it matters.** Standard temporal methods average over an aperture or sample one point, so they report a local field. When the field does not separate into a spatial and a temporal part, the local duration differs from that of the whole beam, and couplings such as pulse-front curvature lengthen the pulse on axis at focus and lower the peak intensity. Scanning a temporal method across the beam does not detect couplings that only shift the arrival time, such as pulse-front tilt.

**Resolved by.** The measurement plane, position in the beam and aperture stated; the pulse measured at, or imaged from, the plane where it is used, or propagation from the measurement plane accounted for; for focused or large beams, a spatially resolved measurement or at least simple checks, such as comparing the focal spot with the full spectrum and through a narrow band-pass filter; peak intensities computed from the duration that applies at the relevant location.

**Benchmark.** [1], [4]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | R. Trebino, R. Jafari, S. A. Akturk, P. Bowlan, Z. Guang, P. Zhu, E. Escoto and G. Steinmeyer, Highly reliable measurement of ultrashort laser pulses, J. Appl. Phys. 128, 171103 (2020); read as the copy hosted on the authors' FROG website | doi:10.1063/5.0022552 | full text | Sec. II.A: the spectrum alone does not fix the pulse; a Gaussian spectrum can carry any linear chirp and so any duration. Sec. III.A: autocorrelation is a one-dimensional phase-retrieval problem with ambiguities, and users divide the trace width by a factor for an assumed shape with little justification. Sec. III.B: complicated pulses or averaging over unstable trains give a coherence spike on a pedestal; the pulse length relates to the pedestal; a spike only about twice narrower blends in, giving errors of a factor of two or more. Sec. III.C: autocorrelation and spectrum together still leave ambiguities, including the direction of time. Sec. III.D: interferometric autocorrelation must be fitted to a guessed field. Secs. IV.B and IV.C: the time-direction ambiguity remains in SHG FROG and is removed by a second trace after inserting glass; some versions have relative-phase ambiguities for well-separated pulses. Secs. IV.D and IV.D.2: over-determined trace gives feedback on systematic error; thin crystals, correctable variation of SHG efficiency across the spectrum, transverse geometrical smearing of at least a fraction of a cycle, glass to be avoided for near-single-cycle pulses. Sec. IV.E: unstable trains give discrepancies between measured and retrieved FROG traces. Sec. IV.I: overpowered pump lasers, near-single-cycle sources, semiconductor lasers and passive combs are prone to instability and need a stability check. Sec. V: SI requires a fully characterized reference whose spectrum contains that of the unknown; Eq. (16) gives the phase difference weighted by both spectra; Fig. 37, the delay must separate the interferogram components; Fig. 45, spectral resolution limits how long the pulses can interfere. Sec. V.A: under fluctuations SI measures only the coherent artifact; reference stability should be established, e.g. by FROG, with fringe visibility then confirming stability; spectral filtering costs resolution. Sec. VI: SPIDER needs a calibration measurement with the same beam-splitting scheme; the shear is the remaining error source; Fig. 51, SPIDER gives only a lower bound on pulse length for unstable trains. Sec. VII: spatially averaged temporal measurements are not always useful because of spatio-temporal couplings |
| 2 | R. Trebino, K. W. DeLong, D. N. Fittinghoff, J. N. Sweetser, M. A. Krumbügel, B. A. Richman and D. J. Kane, Measuring ultrashort laser pulses in the time-frequency domain using frequency-resolved optical gating, Rev. Sci. Instrum. 68, 3277–3295 (1997); read as the copy hosted on the authors' FROG website | doi:10.1063/1.1148286 | full text | Sec. I: an autocorrelation smears out the intensity, satellites show only as enlarged wings, the duration needs a guessed shape whose factor varies significantly between shapes, and adding the spectrum does not determine the pulse. Sec. V: the result is rigorous only if the measured trace contains all of its non-zero values; agreement of measured and retrieved traces as feedback on systematic error; autocorrelations have only weak constraints, including even symmetry; marginals compared with the independently measured spectrum reveal insufficient phase-matching bandwidth. Sec. VI.A: geometrical smearing can artificially broaden the pulse. Sec. VI.D: SHG FROG has a time-direction ambiguity, removed by a second trace after glass before the beam splitter or by prior knowledge; relative phase of well-separated pulses ambiguous by π, not removed by the spectrum, and fully undetermined for spectrograms with an independent gate; crystal must be thin enough, and autocorrelators carry the same requirement without an independent check. Sec. VI.F: the entire trace must be measured, cropping being the most common cause of poor retrieval for new users. Sec. VII: the FROG error is the rms difference between traces and depends on time-bandwidth product and grid size |
| 3 | J. Ratner, G. Steinmeyer, T. C. Wong, R. Bartels and R. Trebino, Coherent artifact in modern pulse measurements, Opt. Lett. 37, 2874–2876 (2012) | doi:10.1364/OL.37.002874 | abstract | Abstract: in simulated multi-shot measurements of unstable trains of complex pulses, neither SHG FROG nor SPIDER revealed the instability; FROG gave the correct average duration and indicated the problem through poor agreement of measured and retrieved traces, while SPIDER substantially underestimated the duration and measured only the coherent artifact |
| 4 | S. W. Jolly, O. Gobert and F. Quéré, Spatio-temporal characterization of ultrashort laser beams: a tutorial, J. Opt. 22, 103501 (2020); read as preprint arXiv:2007.04135 | doi:10.1088/2040-8986/abad08 | full text | Sec. 1: FROG, SPIDER and similar methods average over an aperture or sample one point and give only the local temporal field; couplings often increase duration and reduce focal intensity. Secs. 2.1 and 2.3: with couplings the local duration differs from the global one; pulse-front curvature lengthens the on-axis pulse at focus. Sec. 2.5: comparing the focal spot with the full spectrum and through a narrow band-pass filter reveals chromatic couplings. Sec. 3: scanning a temporal device across the beam is blind to phase terms linear in frequency, so pulse-front tilt is not detected |
