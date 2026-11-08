---
id: T-DARK-MATTER-DIRECT
name: Dark matter direct detection
type: technique
field: physics/particle
applies_when: the paper searches for dark matter scattering off nuclei or electrons in a low-background detector, reporting a recoil spectrum, threshold, quenching factor or background model, or claims an excess, an annual modulation or a cross-section exclusion limit from such a search
version: "0.1"
---

# Dark matter direct detection

## 1. Energy threshold, efficiency and calibration near threshold

**Question.** How is the energy threshold defined, how was the detection and selection efficiency measured as a function of energy down to and below that threshold, and what is the lowest energy at which the energy scale was calibrated directly?

**Why it matters.** The expected recoil spectrum falls steeply with energy, so the result, especially for light dark matter, is set by the few events just above threshold. Efficiency, resolution and energy scale are least well known there, and a response extrapolated below the lowest calibration point can change a limit or the interpretation of a small number of events substantially.

**Resolved by.** The threshold stated in both the measured quantity and in recoil energy; an efficiency curve measured with calibration sources or injected signals, with its uncertainty, down to and through threshold; the calibration points and their energies shown, and any extrapolation below them stated, justified and propagated, or the result shown with and without it.

**Benchmark.** [2], [3], [4]

## 2. Nuclear-recoil energy scale and quenching

**Question.** How was the measured signal converted from electron-equivalent to nuclear-recoil energy, which quenching factor or light and charge yield model was used, over what energy range was it measured in this or a comparable target, and how does its uncertainty enter the result?

**Why it matters.** Nuclear recoils produce less light or charge than electron recoils of the same energy, and the ratio depends on energy and target. Measured yields have disagreed between experiments, simple theory does not hold for every target, and an assumed yield at energies where none has been measured shifts the energy scale and with it the claimed sensitivity to low masses.

**Resolved by.** The quenching or yield model named, with the measurements behind it and their energy range; dedicated nuclear-recoil calibrations, for example with neutron sources, in the same detector or the same material and conditions; the yield uncertainty carried into the limit or the signal fit; where possible, an energy scale built from more than one channel (light and charge, or heat and ionisation) as a cross-check.

**Benchmark.** [2], [3], [4]

## 3. Discrimination between electron and nuclear recoils

**Question.** If the analysis separates nuclear recoils from electron recoils, how were the rejection power and the nuclear-recoil acceptance measured, at which energies, and how is the leakage of electron-recoil and surface events into the signal region estimated?

**Why it matters.** Discrimination parameters such as the ratio of two signals or a pulse shape can lose power at low energy, where the two populations overlap. Rare classes of events, such as surface events that lose part of their signal or alpha decays with energy lost in dead regions, can sit in the nuclear-recoil region and are not described by a model of the electron-recoil band alone.

**Resolved by.** Rejection and acceptance measured with high-statistics electron-recoil and nuclear-recoil calibration data as a function of energy; the leakage estimate based on measured calibration distributions, including their tails, and not only on a fitted band; separate estimates for surface and degraded-energy events, with the cuts against them and their efficiencies.

**Benchmark.** [2]

## 4. Backgrounds and fiducial volume

**Question.** Which background sources does the background model include (radiogenic gammas and betas, radon and its daughters, cosmogenic activation, radiogenic and muon-induced neutrons, surface contamination, neutrino scattering), how was each rate determined, and how were the fiducial volume and its mass and uncertainty fixed?

**Why it matters.** The signal is expected to be far smaller than the raw background, so the claim rests on a model of what remains after shielding, vetoes and fiducial cuts. Neutrons give nuclear recoils like the signal, external and surface backgrounds are concentrated near the detector boundaries, and coherent neutrino scattering produces nuclear recoils that cannot be rejected event by event and whose spectrum can closely match that of a dark matter particle of a particular mass.

**Resolved by.** Each background predicted independently, from material screening, radon and activation measurements, simulations or side-bands, and compared with what was observed; the fiducial cut and its position resolution described, with the background rate shown against position; neutron backgrounds constrained, for example by multiple-scatter events or a veto; neutrino fluxes and their uncertainties taken from stated recommendations; goodness-of-fit tests of the background and detector-response model with pass criteria set in advance.

**Benchmark.** [1], [2], [3], [8]

## 5. Rising event rates near threshold

**Question.** Is there a rise in the event rate towards the threshold that the background model does not describe, and if a dark matter interpretation is offered for low-energy events, how are detector effects ruled out?

**Why it matters.** Many low-threshold detectors of different types see event rates rising sharply below a few hundred eV whose origin is not established. The spectra differ in shape and rate between detectors and targets, which points to several instrumental sources, such as stress in holders or sensors, luminescence or noise, rather than a common physical signal.

**Resolved by.** The low-energy spectrum shown down to threshold with the background model over it; tests of the rate against time since cool-down, warm-up cycles and the way the detector is held, and comparisons between detectors in the same run; a comparison with spectra seen in other low-threshold detectors; a dark matter interpretation offered only for features that these tests leave unexplained.

**Benchmark.** [3], [5]

## 6. Signal model: halo and interaction assumptions

**Question.** Which astrophysical parameters (local dark matter density, circular speed, escape speed, Earth velocity) and which interaction model (spin-independent, spin-dependent, effective operators, proton and neutron couplings, nuclear form factors, or for light dark matter electron scattering or the Migdal effect) were used to compute the expected signal, and are they the conventional ones or, if not, are the consequences shown?

**Why it matters.** A limit or a preferred region on a cross-section is only defined relative to these assumptions. The local density scales a limit directly; light dark matter and high thresholds probe only the high-speed tail of the velocity distribution, so the escape speed and the shape of that tail change the result strongly; results from different targets can be compared only for a stated interaction, for example with equal couplings to protons and neutrons; and for masses where nuclear recoils fall below threshold, the expected rate rests on the additional model for electron scattering or the Migdal effect.

**Resolved by.** The halo parameters and interaction model stated with their sources, using recommended standard values for the main result; the effect of different halo parameters or a halo-independent comparison shown where the conclusion depends on low masses or on comparison with another target; nuclear structure inputs for spin-dependent results, and the model behind any electron-scattering or Migdal signal, named.

**Benchmark.** [1], [2], [3], [7]

## 7. Annual modulation

**Question.** For a claimed annual modulation, were the period and phase fitted freely and found consistent with the expected values, how does the modulation depend on energy, and how were seasonal variations in background rates and detector conditions excluded?

**Why it matters.** The expected modulation is a few per cent of the signal, so its detection needs a large number of events and a stable detector over several years. Backgrounds and detector parameters can also vary with the seasons, and the phase and amplitude of a true signal depend on the velocity distribution, so a modulation alone does not identify its origin.

**Resolved by.** Fits with free period and phase alongside the fit with fixed values, with the phase compared with the expectation near early June; the modulation amplitude shown in energy bins; time series of environmental and detector parameters (temperature, radon, muon flux, gain, noise rate) with their own phases and an estimate of the modulation they could induce; tests with the same target material at a different site or with different backgrounds.

**Benchmark.** [2], [3], [6], [7]

## 8. Reporting conventions of the field

**Question.** Does the paper follow the recommended conventions for direct-detection results (limits at 90% confidence level, any power constraint and its threshold stated, the median expected limit with its bands, an excess called evidence only at a global significance of at least three standard deviations), or say where it departs from them?

**Why it matters.** Direct detection results are compared directly across experiments, so a limit or an excess reported under other conventions is hard to compare with the rest of the field.

**Resolved by.** The recommended conventions used for the main result, or each departure stated with its effect, so that the result can be compared with those of other experiments.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | D. Baxter et al., Recommended conventions for reporting results from direct dark matter searches, Eur. Phys. J. C 81, 907 (2021); read as arXiv:2105.00599v3 | doi:10.1140/epjc/s10052-021-09655-y |
| 2 | M. Schumann, Direct detection of WIMP dark matter: concepts and status, J. Phys. G 46, 103003 (2019); read as arXiv:1903.03026 | doi:10.1088/1361-6471/ab2ea5 |
| 3 | J. Billard et al., Direct detection of dark matter: APPEC committee report, Rep. Prog. Phys. 85, 056201 (2022); read as arXiv:2104.07634 | doi:10.1088/1361-6633/ac5754 |
| 4 | P. Sorensen and C. E. Dahl, Nuclear recoil energy scale in liquid xenon with application to the direct detection of dark matter, Phys. Rev. D 83, 063501 (2011); read as arXiv:1101.6080 | doi:10.1103/PhysRevD.83.063501 |
| 5 | P. Adari et al., EXCESS workshop: descriptions of rising low-energy spectra, SciPost Phys. Proc. 9, 001 (2022); read as arXiv:2202.05097 | doi:10.21468/SciPostPhysProc.9.001 |
| 6 | K. Freese et al., Colloquium: Annual modulation of dark matter, Rev. Mod. Phys. 85, 1561 (2013); read as arXiv:1209.3339 | doi:10.1103/RevModPhys.85.1561 |
| 7 | A. M. Green, Astrophysical uncertainties on the local dark matter distribution and direct detection experiments, J. Phys. G 44, 084001 (2017); read as arXiv:1703.10102 | doi:10.1088/1361-6471/aa7819 |
| 8 | C. A. J. O'Hare, New definition of the neutrino floor for direct dark matter searches, Phys. Rev. Lett. 127, 251802 (2021); read as arXiv:2109.03116, which carries a different title | doi:10.1103/PhysRevLett.127.251802 |
