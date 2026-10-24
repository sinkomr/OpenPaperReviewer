---
id: T-DARK-MATTER-DIRECT
name: Dark matter direct detection
type: technique
field: physics/particle
applies_when: the paper searches for dark matter scattering off nuclei or electrons in a low-background detector, reporting a recoil spectrum, threshold, quenching factor or background model, or claims an excess, an annual modulation or a cross-section exclusion limit from such a search
version: "0.1"
---

# Dark matter direct detection

Direct detection experiments look for the small energy deposited when a dark matter particle, such as a weakly interacting massive particle (WIMP), scatters off a nucleus or an electron in a low-background detector. They are used to claim an excess of events, an annual modulation of the rate, or an upper limit on the interaction cross-section as a function of dark matter mass, and every such claim depends on the energy scale in nuclear-recoil (keVnr) or electron-equivalent (keVee) units, on the background model and on an assumed signal model.

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

## 8. Statistical conventions for excesses and limits

**Question.** For a claimed excess, does the paper give the local and, where needed, global significance with the test statistic used, and for a limit, does it state the confidence level, the treatment of downward fluctuations of the background and the expected sensitivity band?

**Why it matters.** Direct detection results are compared directly across experiments, so differences in confidence level, test statistic, power constraint or an unchecked asymptotic approximation make limits hard to compare and can misstate their coverage. Community recommendations ask for a global significance of at least three standard deviations before an excess is called evidence, and for the expected limit to be shown so that a limit well below sensitivity is visible.

**Resolved by.** A profile likelihood or other stated method with its nuisance parameters; asymptotic distributions checked against pseudo-experiments; limits at 90% confidence level with any power constraint and its threshold stated; the median expected limit with its one and two standard deviation bands; local and global p-values against mass for any excess.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | D. Baxter et al., Recommended conventions for reporting results from direct dark matter searches, Eur. Phys. J. C 81, 907 (2021); read as arXiv:2105.00599v3 | doi:10.1140/epjc/s10052-021-09655-y | full text | Sec. 2 and 4.1: profile likelihood with nuisance parameters, asymptotic formulas only after validation with pseudo-experiments, 90% CL limits, power constraint at a critical power of 0.32 (the minus one sigma sensitivity in the asymptotic case), publication of the unconstrained limit left optional, median expected limit with 68% and 95% bands, local and global p-values, evidence only at a global 3 sigma, choices fixed before unblinding. Sec. 2.5: background and detector-response models tested for goodness of fit with criteria set in advance. Sec. 3.1: recommended halo parameters fixed for comparability, local density only rescales a limit. Sec. 3.2: recommended neutrino fluxes and uncertainties; boron-8 neutrinos mimic a WIMP of about 6 GeV |
| 2 | M. Schumann, Direct detection of WIMP dark matter: concepts and status, J. Phys. G 46, 103003 (2019); read as arXiv:1903.03026 | doi:10.1088/1361-6471/ab2ea5 | full text | Sec. 2.1: steeply falling spectrum makes the low threshold decisive; annual modulation is about 5% of the signal, needs of order ten thousand events, peaks near early June, some backgrounds also modulate; spin-independent comparisons across targets assume equal proton and neutron couplings, spin-dependent results quoted for proton-only or neutron-only coupling. Sec. 1.2: halo parameters and their uncertainty. Sec. 2.2: quenching factor depends on energy, Lindhard theory fits germanium and silicon but not liquid noble gases. Secs. 2.4.1 and 2.4.2: background classes, neutrons and multiple scatters, fiducialisation, discrimination in cryogenic detectors breaking down at low energy where the populations overlap, surface events with partial signal loss leaking into the nuclear-recoil region |
| 3 | J. Billard et al., Direct detection of dark matter: APPEC committee report, Rep. Prog. Phys. 85, 056201 (2022); read as arXiv:2104.07634 | doi:10.1088/1361-6633/ac5754 | full text | Sec. 4.1: threshold matters more than the upper energy limit; keVnr and keVee differ through quenching; modulation needs of order ten thousand signal events and is more sensitive to halo assumptions; MeV-scale dark matter searched for through electron scattering. Sec. 4.2: spin-dependent results depend on nuclear-model calculations; effective operators for comparisons; Migdal effect proposed to extend the reach to low masses. Sec. 4.4: cosmogenic activation, neutron and surface backgrounds, radon plate-out, coherent neutrino scattering as the ultimate background, indistinguishable event by event. Secs. 4.5 and 4.6.4: tests of an annual modulation with the same target material. Sec. 4.6.1: nuclear-recoil quenching factors between 0 and 0.3 below 20 keV, heat-and-ionisation readout as a direct energy measurement, low-energy excesses under study in cryogenic experiments |
| 4 | P. Sorensen and C. E. Dahl, Nuclear recoil energy scale in liquid xenon with application to the direct detection of dark matter, Phys. Rev. D 83, 063501 (2011); read as arXiv:1101.6080 | doi:10.1103/PhysRevD.83.063501 | full text | Introduction: measured scintillation yields disagree between experiments by about a factor of two. Sec. III: low-energy efficiency and resolution depend almost entirely on the light signal. Summary: no direct calibration below about 4 keV; an assumed flat yield below the lowest measurement is incompatible with theory and the more aggressive exclusion limit is hard to support; combined light-and-charge energy scale recommended, with a measurement of the nuclear-recoil band as a cross-check |
| 5 | P. Adari et al., EXCESS workshop: descriptions of rising low-energy spectra, SciPost Phys. Proc. 9, 001 (2022); read as arXiv:2202.05097 | doi:10.21468/SciPostPhysProc.9.001 | full text | Abstract and Sec. 1: sharply rising rates below a few hundred eV in many low-threshold experiments, of unknown origin; differing shapes and rates make a dark matter explanation unlikely and point to several origins. Sec. 2.1 (cryogenic detectors): hypotheses including stress in crystals and from holders, cracking of sensor glue, luminescence and noise; rate decreasing with time and rising after warm-ups; holding strategies tested; comparisons between detectors in the same run |
| 6 | K. Freese, M. Lisanti and C. Savage, Colloquium: Annual modulation of dark matter, Rev. Mod. Phys. 85, 1561 (2013); read as arXiv:1209.3339 | doi:10.1103/RevModPhys.85.1561 | full text | Sec. III: modulation with a one-year period and maximum near early June in the standard halo, of order 1 to 10% of the rate, phase reversal at low energy, phase and shape changed by streams and anisotropy; Sec. III.3: higher harmonics in a power-spectrum analysis. Sec. IV.1: radon, neutrons and muon flux discussed as conventional explanations of an observed modulation; fitted phase and period compared with expectation; energy dependence of the amplitude. Sec. IV.2: a same-target detector at a site with different environmental backgrounds; recoil energy-scale calibration as a systematic in interpreting results |
| 7 | A. M. Green, Astrophysical uncertainties on the local dark matter distribution and direct detection experiments, J. Phys. G 44, 084001 (2017); read as arXiv:1703.10102 | doi:10.1088/1361-6471/aa7819 | full text | Sec. III: ranges of estimates for local density, circular speed and escape speed. Sec. V: limits for light WIMPs or high thresholds depend strongly on the escape speed and the high-speed tail; annual modulation phase and amplitude far more sensitive to the velocity distribution than the mean rate. Sec. VI.1: experiments with different targets and thresholds probe different speeds; halo-independent comparison methods |
| 8 | C. A. J. O'Hare, New definition of the neutrino floor for direct dark matter searches, Phys. Rev. Lett. 127, 251802 (2021); read as arXiv:2109.03116, which carries a different title | doi:10.1103/PhysRevLett.127.251802 | full text | Introduction and "The neutrino fog": neutrino-induced nuclear recoils are an irreducible background whose spectra can resemble dark matter signals of particular masses, boron-8 neutrinos on xenon mimicking about 6 GeV; flux normalisation uncertainties set how far a search can go before neutrinos limit discovery |
