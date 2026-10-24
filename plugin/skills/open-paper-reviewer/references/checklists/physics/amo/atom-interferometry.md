---
id: T-ATOM-INTERFEROMETRY
name: Atom interferometry
type: technique
field: physics/amo
applies_when: the paper measures gravity, a gravity gradient, rotation, acceleration, photon recoil or a fundamental constant with a light-pulse, Raman, Bragg or guided atom interferometer, or bases an equivalence-principle or new-physics test on atom-interferometer phases
version: "0.1"
---

# Atom interferometry

Atom interferometry is used to claim absolute values of the gravitational acceleration g, gravity gradients and rotation rates, the photon recoil of an atom (and from it h/m and the fine-structure constant), and limits on violations of the equivalence principle. Light pulses that drive stimulated Raman or Bragg transitions, sometimes with Bloch oscillations for large momentum transfer (LMT), or guiding potentials for trapped atoms and Bose-Einstein condensates (BECs), split and recombine atomic wave packets; the claimed quantity is inferred from the interferometer phase through a scale factor set by the effective wavevector k_eff and the pulse separation T, and is shifted by systematic effects that depend on the atoms' trajectories through imperfect light fields.

## 1. Scale factor

**Question.** How was the scale factor that turns the interferometer phase into the reported quantity determined (effective wavevector, pulse separation time and, for rotation, the enclosed area and beam orientation), and was it checked, for example by changing T or by measuring a known signal?

**Why it matters.** The ideal phase is k_eff·a·T² for an acceleration and k_eff·(2Ω×v)T² for a rotation, so the result is only as accurate as the knowledge of the laser frequencies, the pulse timing and the beam geometry. In a real Gaussian or distorted beam the local photon momentum differs from the plane-wave value through the Gouy phase and intensity variations, a correction of parts per billion that is among the largest terms in recoil measurements. A gyroscope's response also depends on the launch velocity, the beam tilt and g.

**Resolved by.** Laser frequencies measured against a frequency reference such as an optical frequency comb and the timing against a clock; the wavevector correction for the beam waist and intensity profile evaluated and tested by changing the beam size; for gyroscopes, each input to the predicted Sagnac phase measured separately and the scale factor tested against Earth's rotation in repeated runs with different parameters such as T; the scale-factor uncertainty stated.

**Benchmark.** [1], [10], [11], [12]

## 2. Reading the phase from the fringe

**Question.** How was the phase obtained from the measured populations (fit to a scanned fringe, operation at mid-fringe, ellipse fitting or another correlation method), how was the 2π ambiguity resolved, and are the raw fringes shown with their contrast and offset?

**Why it matters.** The transition probability depends on the phase as P₀ + (C/2)cos Φ, so a phase read at mid-fringe assumes a linear response, stable contrast and offset, and excursions of only a few tens of degrees, and the phase is known only modulo 2π unless the fringe order is fixed independently. Ellipse fitting of two coupled interferometers requires equal scale factors and returns a biased phase when offset or differential-phase noise is present, more so as the differential phase moves away from π/2.

**Resolved by.** Raw fringes or ellipses shown with the fitted contrast and offset; the fringe order fixed independently, for example by a scan that unwraps the phase, such as a full turn of a gyroscope; for differential measurements, the estimator named, its bias evaluated by simulation or by comparison with a second estimator, and the differential phase set near π/2 or an estimator without that bias used.

**Benchmark.** [1], [3], [4], [5], [10]

## 3. Vibration of the inertial reference

**Question.** How were vibrations of the retroreflecting mirror, which serves as the inertial reference, isolated, measured or rejected, and where a classical sensor was used to correct the phase, how well did its signal correlate with the interferometer phase?

**Why it matters.** Once the interrogation time exceeds a few milliseconds, ground vibration usually limits the sensitivity of a single interferometer. Correction from a seismometer or accelerometer is limited by that sensor's own noise, its frequency response and cross-axis coupling, and in practice can fall well short of the predicted rejection. Gradiometers and dual-species sensors reject vibration only to the extent that both interferometers share it.

**Resolved by.** The isolation platform or correction method described, with the sensor's position relative to the mirror and its transfer function; the measured correlation or rejection factor; sensitivity quoted for the conditions under which the main data were taken; for differential sensors, the common-mode rejection measured, and a method suited to the noise level when vibration scrambles the fringes.

**Benchmark.** [1], [3], [5]

## 4. Phase shifts not caused by the inertial signal

**Question.** Which phase shifts that do not come from the measured acceleration or rotation (light shifts, magnetic field gradients and Zeeman shifts, electronic phase delays, the two-photon light shift, diffraction phases of Bragg pulses) were considered, and how was each cancelled or measured, for example by reversing the effective wavevector?

**Why it matters.** Reversing k_eff reverses the inertial phase but not shifts that are independent of k_eff, so averaging the two directions removes the latter. Shifts that do follow k_eff survive: the two-photon light shift from off-resonant Raman pairs in a retroreflected beam scales with the Raman intensity and has been measured at about 8×10⁻⁸ g in a gravimeter with dropped atoms, and Bragg pulses add a diffraction phase that has to be suppressed or extrapolated.

**Resolved by.** Interleaved measurements with reversed wavevector, with the size of the rejected shifts reported; the two-photon light shift measured by alternating Raman intensity or Rabi frequency and extrapolated to zero; diffraction phases reduced by design and checked by varying T, with a simulation of the residual; each term listed in the error budget with how it was obtained.

**Benchmark.** [1], [3], [6], [11]

## 5. Wavefront aberrations and atom temperature

**Question.** How was the bias from imperfect wavefronts of the beam-splitter light estimated, and was it measured as a function of atom temperature or of the selected trajectories, not only inferred from an optical characterisation of the beam?

**Why it matters.** The equiphase surfaces of the light act as the ruler that locates the atoms at each pulse. Because the cloud expands, atoms sample different parts of a distorted wavefront at each pulse and the averaged phase is biased; a distortion of 0.1 nm corresponds to about 1 mrad, and this term has led the accuracy budgets of the most accurate gravimeters. Its size depends on cloud temperature, beam waist and detection field of view, and extrapolating from laser-cooled temperatures alone can be inaccurate because the dependence becomes steep at low temperature.

**Resolved by.** g measured over a range of temperatures, preferably extending to ultracold sources, or with truncated detection or beam size, and the bias extrapolated with a stated wavefront model; the dependence of the result on that model shown, for example on the number of wavefront terms; large, retroreflected beams; the evaluation uncertainty carried into the budget.

**Benchmark.** [1], [7]

## 6. Rotation and Coriolis effects

**Question.** How were Earth's rotation and the atoms' transverse velocities accounted for: by measurements at opposite orientations of the instrument, by counter-rotating the retroreflecting mirror, or by measuring the transverse velocity distribution of the atoms actually detected?

**Why it matters.** At microkelvin temperatures, transverse velocities of order cm/s give Coriolis accelerations up to about 10⁻⁶ m s⁻²; the mean bias cancels only if the velocity distribution of the detected atoms is symmetric and centred, and the detection response and beam inhomogeneities can break that symmetry. Rotation also stops the two wave packets from overlapping at the final pulse, which lowers contrast in long or LMT interferometers, and in gyroscopes mirror misalignment combined with the launch direction adds a bias that can drift.

**Resolved by.** Data at opposite orientations, or mirror counter-rotation at the local Earth rate with the residual quantified; the effective velocity distribution of detected atoms measured, not assumed; launch and beam alignment stated and monitored during the measurement.

**Benchmark.** [1], [8], [9], [10]

## 7. Gravity gradients, measurement height and initial kinematics

**Question.** At what height, or effective height, is an absolute result reported, how was the local gravity gradient measured, and in differential tests between two species or clouds, how closely were their initial positions and velocities matched or the gradient coupling suppressed?

**Why it matters.** Gravity changes with height, so an absolute value has meaning only at a stated height, and comparisons between gravimeters transfer each result to a common height with a measured gradient after common corrections for tides, air pressure and polar motion. In tests of the universality of free fall, gravity gradients couple to differences in the initial positions and velocities of the two species and produce a differential phase that can mimic a violation, and they also reduce contrast; in recoil measurements an acceleration gradient enters the budget at the part-per-billion level.

**Resolved by.** The reference height, the gradient measured on site (for example with a relative gravimeter at several heights) and the tidal, pressure and polar-motion corrections stated; agreement with an independent absolute gravimeter or a result from a key comparison; for differential tests, the initial kinematic differences measured and a gradient-compensation scheme used, such as a frequency shift of the mirror pulse, with the residual coupling quantified.

**Benchmark.** [1], [11], [13], [14], [15]

## 8. Contrast and coherence

**Question.** Does the paper report the contrast and how it changes with interrogation time, atom number or density, and does it identify what limits it, in particular for interferometers with trapped or guided atoms or BECs?

**Why it matters.** The phase is read from a fringe whose amplitude is the contrast, so falling contrast lowers sensitivity and makes mid-fringe readings depend on contrast stability. In trapped and guided interferometers, interactions between atoms cause phase diffusion that limits the coherence time, to below about 50 ms for a typical condensate of a million atoms, and contrast in guided interferometers can fall from near 100% to about a fifth within ten milliseconds; interactions also shift the phase through mean-field energy. Rotation and gravity gradients reduce contrast further in long interferometers.

**Resolved by.** Contrast plotted against interrogation time and its dependence on atom number or density shown; the limiting mechanism, such as interactions, rotation, gradients or velocity selection, identified and tested by changing it; any claimed coherence time defined by the measurement that gives it; mean-field or density shifts evaluated in the error budget.

**Benchmark.** [2], [8], [13]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | R. Geiger, A. Landragin, S. Merlet and F. Pereira Dos Santos, High-accuracy inertial measurements with cold-atom sensors, AVS Quantum Sci. 2, 024702 (2020); read as preprint arXiv:2003.12516 | doi:10.1116/5.0009093 | full text | Sec. II: transition probability P0 + (C/2)cos of the phase, and phase terms k_eff·a·T² and k_eff·(2Ω×v)T². Sec. III.E and IV.C: vibrations limit sensitivity beyond a few ms of interrogation; isolation platforms and correlation with a seismometer or accelerometer; vibration is common mode in gradiometers. Sec. IV.A: atom gravimeters in CIPM key comparisons since 2009. Sec. IV.D: scale factor tied to time and frequency; k_eff reversal removes light-shift, magnetic-gradient and electronic-delay shifts; remaining two-photon light shift, Coriolis bias (cm/s velocities, up to 10⁻⁶ m s⁻², cancels only for symmetric detected distribution; rotate instrument or counter-rotate mirror) and wavefront aberrations (0.1 nm gives about 1 mrad; leading term of the best gravimeters; evaluated by varying temperature or truncating trajectories). Sec. V.A.1: Sagnac phase and area depend on T, k_eff and launch velocity |
| 2 | A. D. Cronin, J. Schmiedmayer and D. E. Pritchard, Optics and interferometry with atoms and molecules, Rev. Mod. Phys. 81, 1051–1129 (2009); read as preprint arXiv:0712.3703 | doi:10.1103/RevModPhys.81.1051 | full text | Sec. III.F (opening) and III.F.1: in a split condensate, mean-field interactions cause dephasing that limits coherence to under about 50 ms for a typical million-atom BEC; in a guided-atom interferometer contrast fell from about 100% at 1 ms to 20% at 10 ms, mainly from interactions. Sec. V.E: mean-field shifts, ac Stark shifts, beam misalignment and wavefront curvature listed among systematic errors of h/m measurements |
| 3 | J. Le Gouët, T. E. Mehlstäubler, J. Kim, S. Merlet, A. Clairon, A. Landragin and F. Pereira Dos Santos, Limits to the sensitivity of a low noise compact atomic gravimeter, Appl. Phys. B 92, 133–144 (2008); read as preprint arXiv:0801.1270 | doi:10.1007/s00340-008-3088-1 | full text | Sections on the sensitivity function and vibration correction: phase noise filtered by the sensitivity function; seismometer under the mirror; post-correction assumes mid-fringe operation with excursions of tens of degrees and stable contrast; rejection limited to about a factor of 3 by seismometer response, noise and cross-axis coupling. Also: reversing k_eff rejects a magnetic-gradient phase by about 300; alternating Rabi frequency isolates the two-photon light shift |
| 4 | G. T. Foster, J. B. Fixler, J. M. McGuirk and M. A. Kasevich, Method of phase extraction between coupled atom interferometers using ellipse-specific fitting, Opt. Lett. 27, 951–953 (2002) | doi:10.1364/OL.27.000951 | abstract | Abstract: fitting ellipses to the coupled outputs of two gravimeters in a gradiometer extracts the differential phase despite common vibration noise |
| 5 | B. Barrett, L. Antoni-Micollier, L. Chichet, B. Battelier, P.-A. Gominet, A. Bertoldi, P. Bouyer and A. Landragin, Correlative methods for dual-species quantum tests of the weak equivalence principle, New J. Phys. 17, 085010 (2015); read as preprint arXiv:1503.08423 | doi:10.1088/1367-2630/17/8/085010 | full text | Sec. 3.1: ellipse fitting needs equal scale factors and is biased with offset, amplitude or differential-phase noise; Appendix A: the bias of the direct ellipse fit grows away from π/2. Sec. 3.2 and 6: Bayesian estimation needs prior knowledge of the noise. Sec. 3.3 and 5.1: when vibration scrambles the fringes, accelerometer-based fringe reconstruction gives unbiased estimates, and common vibration was rejected by a factor of 730, depending on the temporal overlap of the two interferometers |
| 6 | A. Gauguet, T. E. Mehlstäubler, T. Lévèque, J. Le Gouët, W. Chaibi, B. Canuel, A. Clairon, F. Pereira Dos Santos and A. Landragin, Off-resonant Raman transition impact in an atom interferometer, Phys. Rev. A 78, 043615 (2008); read as preprint arXiv:0809.0149 | doi:10.1103/PhysRevA.78.043615 | full text | Sections on the two-photon light shift: off-resonant Raman couplings in retroreflected beams shift the resonance; the phase shift scales with Raman power and is larger for dropped than launched atoms; measured by alternating Rabi frequency with constant pulse area; Sec. III: in a gravimeter with dropped atoms, a calculated shift of about 8×10⁻⁸ g and a measured 32 mrad |
| 7 | R. Karcher, A. Imanaliev, S. Merlet and F. Pereira Dos Santos, Improving the accuracy of atom interferometers with ultracold sources, New J. Phys. 20, 113041 (2018); read as preprint arXiv:1804.04909 | doi:10.1088/1367-2630/aaf07d | full text | Introduction and model sections: atoms expanding through the beam sample different wavefront defects; bias depends on temperature, beam waist and detection area. Results: g measured from about 50 nK to 7 µK and extrapolated to zero temperature with Zernike terms; result depends on the number of terms; linear extrapolation from laser-cooled data would be inaccurate because the dependence is steep below about 2 µK |
| 8 | S.-Y. Lan, P.-C. Kuan, B. Estey, P. Haslinger and H. Müller, Influence of the Coriolis force in atom interferometry, Phys. Rev. Lett. 108, 090402 (2012); read as preprint arXiv:1110.6910 | doi:10.1103/PhysRevLett.108.090402 | full text | Paragraphs after Eq. 2 and on apparatus: Earth's rotation displaces the wave packets at the final pulse and reduces contrast in LMT interferometers with long T; a tip-tilt mirror counter-rotates at the Earth rate and restores contrast; systematics paragraph: rotation with residual horizontal launch velocity gives a gravity offset, removed by the compensation |
| 9 | T. Farah, P. Gillot, B. Cheng, A. Landragin, S. Merlet and F. Pereira Dos Santos, Effective velocity distribution in an atom gravimeter: effect of the convolution with the response of the detection, Phys. Rev. A 90, 023606 (2014) | doi:10.1103/PhysRevA.90.023606 | abstract | Abstract (read on arXiv:1406.5998): the transverse velocity distribution of detected atoms is distorted by the detection response, depending on molasses balance and cloud position, and this strongly affects how the Coriolis bias averages |
| 10 | R. Gautier, M. Guessoum, L. A. Sidorenkov, Q. Bouton, A. Landragin and R. Geiger, Accurate measurement of the Sagnac effect for matter waves, Sci. Adv. 8, eabn8009 (2022) | doi:10.1126/sciadv.abn8009 | full text | Read on PubMed Central (PMC9187224). Results and methods: scale factor tested against Earth's rotation by full-turn rotation of the apparatus in six data sets with different parameters, including T, agreeing to within 25 ppm; each input (T, k_eff, beam tilt, latitude) measured separately; alternating ±k_eff removes k_eff-independent bias; full-turn scan unwraps the roughly 200 rad phase; mirror misalignment with launch direction gives a drifting bias |
| 11 | R. H. Parker, C. Yu, W. Zhong, B. Estey and H. Müller, Measurement of the fine-structure constant as a test of the Standard Model, Science 360, 191–195 (2018); read as preprint arXiv:1812.04130 with supplementary text | doi:10.1126/science.aap7706 | full text | Main text: laser frequency monitored with a frequency comb; diffraction phase from Bragg pulses suppressed and extrapolated by alternating pulse separation times, with Monte Carlo simulation. Table 1: Gouy phase (−2.60 ppb) and acceleration gradient (−1.79 ppb) among the largest corrections. Supplementary Sec. 3: Gaussian-beam wavevector differs from a plane wave; check with two beam waists |
| 12 | S. Bade, L. Djadaojee, M. Andia, P. Cladé and S. Guellati-Khelifa, Observation of extra photon recoil in a distorted optical field, Phys. Rev. Lett. 121, 073603 (2018); read as preprint arXiv:1712.04023 | doi:10.1103/PhysRevLett.121.073603 | full text | Paragraphs after Eqs. 1 and 2: local photon momentum depends on amplitude and phase variations of the beam; the Gaussian-beam (Gouy) correction varies across the beam; intensity variations give effects of order 100 ppb, larger than the resolution of recoil measurements |
| 13 | A. Roura, Circumventing Heisenberg's uncertainty principle in atom interferometry tests of the equivalence principle, Phys. Rev. Lett. 118, 160401 (2017) | doi:10.1103/PhysRevLett.118.160401 | abstract | Abstract (read on arXiv:1509.08098): gravity gradients require tightly matched initial positions and velocities of the two species and cause strong contrast loss in sensitive interferometers; a scheme relaxes the co-location requirement by orders of magnitude |
| 14 | C. Overstreet, P. Asenbaum, T. Kovachy, R. Notermans, J. M. Hogan and M. A. Kasevich, Effective inertial frame in an atom interferometric test of the equivalence principle, Phys. Rev. Lett. 120, 183604 (2018) | doi:10.1103/PhysRevLett.120.183604 | abstract | Abstract (read on arXiv:1711.09986): gravity gradients couple to initial kinematic differences between species and cause systematic errors; a frequency shift of the mirror pulse reduces this coupling about a hundredfold and allows the differences to be measured |
| 15 | D. Newell, D. van Westrum and the participants, Final report of the CCM.G-K2.2023 key comparison and additional comparison of absolute gravimeters, Table Mountain Geophysical Observatory, pilot laboratory NIST; report published by BIPM (comparison held in 2023) | https://www.bipm.org/documents/d/guest/ccm-g-k2-2023 | full text | Participants section: 30 absolute gravimeters including 2 atom gravimeters. Gravity gradient measurements section: relative gravimeter readings at three heights above each pier. Text before Table 5: results reported at each instrument's effective height, corrected in common for tides, pressure, polar motion and instrumental effects, and transferred to 125 cm with each pier's gradient |
