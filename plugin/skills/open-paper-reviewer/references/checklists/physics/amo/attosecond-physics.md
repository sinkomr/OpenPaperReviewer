---
id: T-ATTOSECOND-PHYSICS
name: Attosecond physics and high-harmonic generation
type: technique
field: physics/amo
applies_when: the paper reports high-harmonic spectra, cut-offs, photon flux or conversion efficiency, characterises attosecond pulses or pulse trains by RABBITT, streaking or related retrieval, measures photoemission time delays, or depends on carrier-envelope phase stabilisation or CEP-dependent signals
version: "0.1"
---

# Attosecond physics and high-harmonic generation

High-harmonic generation (HHG) in gases is used to claim extreme-ultraviolet (XUV) spectra, cut-off energies, photon fluxes and conversion efficiencies, and to produce attosecond pulse trains or isolated attosecond pulses. These pulses are characterised by RABBITT (reconstruction of attosecond beating by interference of two-photon transitions) or by attosecond streaking with FROG-CRAB (frequency-resolved optical gating for complete reconstruction of attosecond bursts) or related retrievals, and are used to measure time delays in photoemission. Isolated pulses and many strong-field results also depend on control of the carrier-envelope phase (CEP) of the driving laser.

## 1. Photon flux and conversion efficiency

**Question.** How were detector counts converted into photon numbers, pulse energy or conversion efficiency: which detector, spectrometer and filter efficiencies were used, were they measured or taken from tabulated or manufacturer values, and what fraction of the harmonic beam reached the detector?

**Why it matters.** An absolute XUV flux rests on a chain of factors (grating and mirror efficiency, filter transmission, detector response, beam clipping), and each can be off by a large factor if assumed rather than measured; thin metal filters, for example, can transmit much less than tabulated values once oxidised. Conversion efficiencies quoted without the spatial properties of the beam are hard to compare, because similar efficiencies can come with very different divergence and beam quality.

**Resolved by.** A spectrometer and detector sensitivity calibrated against a reference, such as a calibrated photodiode or a synchrotron measurement; filter transmission and mirror reflectivity measured in the set-up; clipping and collection angle accounted for; the definition of conversion efficiency stated (per harmonic or integrated, over which band, relative to which driving energy) with its uncertainty; divergence or beam profile reported alongside the efficiency.

**Benchmark.** [1], [2], [3]

## 2. Driving-field intensity

**Question.** How was the peak intensity of the driving laser in the generation or interaction region determined, what uncertainty is given, and does any intensity inferred from the harmonic cut-off or from ionisation yields account for focal-volume averaging and propagation in the medium?

**Why it matters.** Intensity estimated from pulse energy, duration and focal spot is uncertain by about ten per cent even when measured carefully, mainly from the spot size, and strong-field observables can change markedly with a few per cent change in intensity. In situ calibrations rely on a theoretical model and on focal-volume averaging, both of which can introduce systematic errors. In a partly ionised medium, plasma defocusing lowers the peak intensity below its vacuum value, so the cut-off law applied to an observed cut-off need not give the intensity at the atoms.

**Resolved by.** The method of intensity determination stated with its uncertainty; spot size measured at the focus; where an in situ calibration is used, the reference process, the theory it is compared with, and the focal-volume and target-geometry treatment described; for dense or long media, an estimate of ionisation and defocusing showing whether the vacuum intensity applies.

**Benchmark.** [3], [4], [6]

## 3. Macroscopic generation conditions

**Question.** Does the paper give the gas, pressure, medium length and position relative to the focus, and the estimated ionisation degree, and does it consider whether phase matching, reabsorption and the selection of short or long electron trajectories, rather than the single-atom response, explain the features it interprets?

**Why it matters.** The measured harmonic signal is a macroscopic response shaped by neutral and plasma dispersion, the focusing (Gouy) phase, the intensity-dependent dipole phase and reabsorption in the medium. Above a critical ionisation degree, on-axis phase matching is no longer possible, and moving the medium relative to the focus changes which trajectories are phase matched. Changes in spectra, cut-offs or efficiency attributed to the atom or molecule can therefore come from changed propagation conditions.

**Resolved by.** All target parameters reported; the ionisation degree compared with the critical value for the harmonics studied; pressure, length and focus-position scans, or propagation calculations, showing that the interpreted feature does not follow phase matching or absorption; spatial or divergence data used to identify short and long trajectory contributions.

**Benchmark.** [3]

## 4. Isolated pulse or pulse train

**Question.** When a single isolated attosecond pulse is claimed, what gating method was used, over which part of the spectrum is the pulse isolated, and what evidence (a continuous spectrum, its dependence on CEP, the measured streaking trace) excludes satellite pulses from neighbouring half-cycles?

**Why it matters.** With spectral selection of the cut-off, only the highest photon energies come from a single half-cycle; lower energies come from several half-cycles and form more than one pulse. With polarisation gating, one or two pulses can fall in the gate depending on the CEP. An apparently continuous spectrum can also come from a spectrometer that cannot resolve closely spaced harmonics, as with long-wavelength drivers. A pulse that is isolated only in part of the spectrum, or only for some laser shots, does not support claims made for the whole bandwidth.

**Resolved by.** The gating scheme and the spectral window used for the experiment stated; a spectrum free of harmonic modulation across that window, recorded with a resolution shown to be sufficient to resolve the harmonic spacing; the dependence of the spectrum on CEP shown; a retrieved temporal profile with any satellite pulses and their relative intensity quantified.

**Benchmark.** [5]

## 5. Pulse retrieval and its assumptions

**Question.** Which retrieval method gives the quoted pulse duration or spectral phase, which approximations does it make (identical pulses in a train, a weak probe, the central momentum approximation, a flat or included dipole phase), and are these approximations valid for the measured bandwidth and probe intensity?

**Why it matters.** RABBITT assumes a periodic train of identical pulses and a weak probe; a real train has a finite length and can vary from pulse to pulse, so the result is an average pulse. FROG-CRAB relies on the central momentum approximation, which holds only when the bandwidth is small compared with the central photoelectron energy; for broad spectra it can return a pulse that is too short. Ignoring the phase of the photoionisation dipole adds a target-dependent error to the retrieved phase.

**Resolved by.** The retrieval algorithm named with its approximations; the ratio of bandwidth to central energy given and, for broad spectra, a method that does not rely on the narrow-band approximation; the retrieval tested on simulated traces with realistic noise; measured and reconstructed spectrograms shown side by side with the residual; the retrieved spectrum compared with the independently measured XUV spectrum; RABBITT results described as an average over the train.

**Benchmark.** [5], [6], [7]

## 6. What a measured photoemission delay contains

**Question.** When a photoemission time delay is reported, does the paper separate the atomic or Wigner delay from the contributions of the measurement (the continuum-continuum or Coulomb-laser coupling term, any dipole-laser coupling of the initial state, and the group delay or chirp of the XUV pulse), and is the delay measured relative to a reference channel or atom?

**Why it matters.** The delay read from a RABBITT or streaking measurement is the sum of the XUV group delay, the single-photon delay and a probe-induced term that depends on the photoelectron energy and the probe wavelength. An absolute delay is not directly observable, so delays are meaningful only relative to a reference, and relative measurements remove several sources of error. Within the broad XUV bandwidth, unresolved shake-up satellites can overlap a main line and shift the delay attributed to it.

**Resolved by.** Delays reported as differences between channels or atoms measured simultaneously, or referenced to a calculable system; the probe-induced correction stated with its source and validity range, which is narrower for slow electrons; the XUV chirp characterised or shown to cancel in the difference; the energy resolution compared with the separation of nearby satellite or overlapping lines; dependence on probe intensity and wavelength checked.

**Benchmark.** [6], [8]

## 7. Delay stability and delay axis

**Question.** How stable was the delay between the XUV and the probe pulses over the acquisition, how was this measured, and how was the delay axis calibrated?

**Why it matters.** Attosecond resolution requires path-length stability better than a few tens of nanometres between two arms that are often metres long; about three nanometres corresponds to ten attoseconds. Thermal expansion of mirrors under laser load causes slow drifts that can exceed a sideband period within about ten minutes, and a stabilisation reference that does not travel on the main optics can miss them. Drift during a scan smears the phase and biases the extracted delays.

**Resolved by.** The interferometer stability quantified over the acquisition time, for example as an RMS delay, with the method stated; active or passive stabilisation described, including whether the reference shares the main optics; repeated or interleaved scans showing that the extracted phases are reproducible; the calibration of the delay axis stated.

**Benchmark.** [8], [9]

## 8. Carrier-envelope phase stability and CEP-dependent signals

**Question.** How was the CEP measured and stabilised, is the quoted residual CEP noise from an in-loop or out-of-loop measurement and from single shots or averages over many shots, and for CEP-dependent results, how was the CEP of each shot known?

**Why it matters.** CEP noise values obtained from spectrometers that average over tens to hundreds of shots are systematically smaller than those from single-shot statistics, and an in-loop value is not an independent check of the stability. CEP noise reduces the amplitude of CEP-dependent signals and can wash out higher harmonics of the CEP dependence. Isolated-pulse generation depends on the CEP, so drifts change the pulse structure during a measurement.

**Resolved by.** The CEP detection method, its bandwidth and the number of shots per value stated; residual noise reported from an out-of-loop or single-shot measurement over the acquisition time; for CEP-resolved results, shot-by-shot CEP tagging or a measured CEP distribution used in the analysis; the effect of the residual noise on the observed CEP modulation estimated.

**Benchmark.** [4], [5], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | S. Fuchs, C. Rödel, M. Krebs, S. Hädrich, J. Bierbach, A. E. Paz, S. Kuschel, M. Wünsche, V. Hilbert, U. Zastrau, E. Förster, J. Limpert and G. G. Paulus, Sensitivity calibration of an imaging extreme ultraviolet spectrometer-detector system for determining the efficiency of broadband extreme ultraviolet sources, Rev. Sci. Instrum. 84, 023101 (2013) | doi:10.1063/1.4788732 | abstract | Abstract: an XUV spectrometer (toroidal mirror and transmission grating) was calibrated at a synchrotron for the ratio of detected to incident photons from 15.5 to 99 eV, which allows absolute photon numbers from laser-driven harmonic sources |
| 2 | A. Comby, D. Descamps, S. Beauvarlet, A. Gonzalez, F. Guichard, S. Petit, Y. Zaouter and Y. Mairesse, Cascaded harmonic generation from a fiber laser: a milliwatt XUV source, Opt. Express 27, 20383 (2019); read as arXiv:1811.05178, which carries a different title | doi:10.1364/OE.27.020383 | full text | Flux measurement section and Fig. 4: flux from a calibrated XUV photodiode behind an aluminium filter whose transmission was measured in situ; measured transmission about 45% against about 70% tabulated, attributed to oxidation; filter transmission, mirror reflectivity and beam clipping corrected, with a stated uncertainty of about 20% |
| 3 | R. Weissenbilder, S. Carlström, L. Rego, C. Guo, C. M. Heyl, P. Smorenburg, E. Constant, C. L. Arnold and A. L'Huillier, How to optimize high-order harmonic generation in gases, Nat. Rev. Phys. 4, 713–722 (2022); read as arXiv:2202.08202, which carries a different title | doi:10.1038/s42254-022-00522-7 | full text | Sec. 3.3: four contributions to phase mismatch (neutral, free-electron, focusing, dipole phase). Sec. 3.4: above a critical ionisation degree on-axis phase matching is impossible; with the medium after the focus only the short trajectory can be phase matched. Sec. 3.5 and Table 1: intensity window bounded by the cut-off intensity and the critical ionisation. Sec. 4.5 and Fig. 10: moving the medium relative to the focus changes the efficiency of short- and long-trajectory contributions. Sec. 3.7: reabsorption limits yield; plasma defocusing lowers the effective peak intensity below the vacuum value. Secs. 5.1 and 5.2: similar conversion efficiencies with divergence below 1 mrad or about 6 mrad |
| 4 | D. Kielpinski, R. T. Sang and I. V. Litvinyuk, Benchmarking strong-field ionization with atomic hydrogen, J. Phys. B 47, 204003 (2014); read as arXiv:1403.6548 | doi:10.1088/0953-4075/47/20/204003 | full text | Sec. III.4: intensity from power, duration and spot size uncertain by about 10%, mainly from spot size; intensity changes of a few per cent can strongly alter strong-field ionisation; approximate theories give systematic intensity errors. Sec. III.2 and Sec. V.5: focal-volume averaging changes predicted yields strongly and must be modelled. Sec. V.4: CEP noise reduces measured asymmetry amplitudes, suppressing higher-order terms most |
| 5 | M. Chini, K. Zhao and Z. Chang, The generation, characterization and applications of broadband isolated attosecond pulses, Nat. Photon. 8, 178–186 (2014); read as arXiv:1312.1679, which carries a different title | doi:10.1038/nphoton.2013.362 | full text | Section on gating and Fig. 1: with amplitude or ionisation gating only cut-off photons come from a single half-cycle, lower energies from several pulses; isolated-pulse generation needs the CEP set; with polarisation gating one or two pulses fall in the gate depending on CEP; an isolated pulse is indicated by a spectrum continuous over its whole bandwidth and by its CEP dependence. Paragraph on mid-infrared drivers: an apparent continuum can result from a grating spectrometer unable to resolve the narrow harmonic spacing. Section on characterisation: FROG-CRAB assumes narrow bandwidth (central momentum approximation) and is not suited to ultrabroadband pulses, motivating other methods |
| 6 | J. M. Dahlström, A. L'Huillier and A. Maquet, Introduction to attosecond delays in photoionization, J. Phys. B 45, 183001 (2012); read as arXiv:1205.6624 | doi:10.1088/0953-4075/45/18/183001 | full text | Sec. 1.1, Eqs. (1)–(2): cut-off law in terms of ionisation potential and ponderomotive energy. Sec. 1.2.3: RABBITT assumes a train of identical pulses and a weak probe. Sec. 2.1.2: real trains are finite and can vary pulse to pulse, so RABBITT gives an average pulse. Sec. 2.1.3: harmonics carry a positive intrinsic chirp. Sec. 3.3: no absolute Coulomb delay, only relative ones. Sec. 5.1: the continuum-continuum phase depends on electron momentum and probe photon energy, and its asymptotic form fails below about 10 eV. Sec. 5.2: measured delay is the sum of XUV group delay, Wigner delay and continuum-continuum delay; ionising two states simultaneously with the same pulse gives their delay difference without knowing the pulse |
| 7 | P. D. Keathley, S. Bhardwaj, J. Moses, G. Laurent and F. X. Kärtner, Volkov transform generalized projection algorithm for attosecond pulse characterization, New J. Phys. 18, 073009 (2016) | doi:10.1088/1367-2630/18/7/073009 | full text | Sec. 1: the central momentum approximation needs bandwidth small compared with the central momentum and cannot describe the induced phase or a dispersive dipole for broad pulses. Numerical comparison (Fig. 4): the least-squares generalized projections algorithm used for FROG-CRAB returned a near transform-limited pulse about half the true duration; the dipole matrix element included in the retrieval; tests on simulated traces with noise |
| 8 | R. Pazourek, S. Nagele and J. Burgdörfer, Attosecond chronoscopy of photoemission, Rev. Mod. Phys. 87, 765–802 (2015); read as the accepted manuscript made available via CHORUS | doi:10.1103/RevModPhys.87.765 | full text | Sec. II: XUV chirp produces apparent spectral phase variations that mask the delay, so chirp control is essential. Sec. IV: streaking delay is the Wigner delay plus a Coulomb-laser coupling term and, for polarisable initial states, a dipole-laser coupling term. Sec. V: relative-delay measurements remove several error sources tied to absolute phase; unresolved shake-up satellites within the XUV bandwidth can contaminate a main-line streaking trace |
| 9 | M. Luttmann, D. Bresteau, J.-F. Hergott, O. Tcherbakoff and T. Ruchon, In situ sub-50-attosecond active stabilization of the delay between infrared and extreme-ultraviolet light pulses, Phys. Rev. Applied 15, 034036 (2021); read as arXiv:2012.09528 | doi:10.1103/PhysRevApplied.15.034036 | full text | Sec. I: attosecond pump-probe needs path stability of a few tens of nanometres or better, 3 nm being about 10 as; thermal expansion of mirrors causes drift; references on separate optics miss expansion of the main mirrors. Sec. III: open-loop drift of several femtoseconds per hour, a sideband period in about 10 minutes; drift during an open-loop RABBITT scan distorts the sideband oscillation (Fig. 6); stabilised long scans improve spectral phase precision (Fig. 8) |
| 10 | D. Hoff, F. J. Furch, T. Witting, K. Rühle, D. Adolph, A. M. Sayler, M. J. J. Vrakking, G. G. Paulus and C. P. Schulz, Continuous every-single-shot carrier-envelope phase measurement and control at 100 kHz, Opt. Lett. 43, 3850 (2018); read as arXiv:1805.12399 | doi:10.1364/OL.43.003850 | full text | Introduction: stereo above-threshold ionisation allows CEP tagging of individual shots. Conclusion: fast CEP control facilitates the generation of isolated attosecond XUV pulses. Discussion of Figs. 3 and 4: f-2f values averaged over tens to hundreds of shots give noise values always smaller than single-shot statistics; in-loop and out-of-loop measurements distinguished, with the stereo-ATI-locked data noted as in-loop |
