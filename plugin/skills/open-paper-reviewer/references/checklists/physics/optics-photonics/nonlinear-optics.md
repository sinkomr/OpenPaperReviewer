---
id: T-NONLINEAR-OPTICS
name: Nonlinear optics and frequency conversion
type: technique
field: physics/optics-photonics
applies_when: the paper reports harmonic generation, sum- or difference-frequency generation, parametric amplification or oscillation, or a measured nonlinear coefficient such as d, χ(2), χ(3), n2 or two-photon absorption, or bases a claim on conversion efficiency, phase matching or power handling
version: "0.1"
---

# Nonlinear optics and frequency conversion

Nonlinear optical measurements are used to claim a material's second- or third-order nonlinear coefficient (d or χ(2), χ(3), the nonlinear refractive index n2, the two-photon absorption coefficient) and the performance of a frequency converter: second- and third-harmonic generation (SHG, THG), sum- and difference-frequency generation, and optical parametric amplification and oscillation (OPA, OPO). These claims rest on the measured powers of the pump and the generated light, on how well the pump is characterised, and on phase matching, including quasi-phase matching (QPM) in periodically poled media.

## 1. Definition of conversion efficiency

**Question.** Which formula gives the quoted conversion efficiency: power or pulse energy, peak or average, incident or coupled into the device, measured outside or estimated inside the sample, and at what pump power; and if a normalised efficiency is quoted, is it used only in the regime where it applies?

**Why it matters.** The same experiment can be reported with efficiencies that differ by orders of magnitude depending on these choices, so figures from different papers are often not comparable. A normalised efficiency, such as SHG power divided by the square of pump power and length in %/W·cm², assumes an undepleted pump and ideal length scaling, and it does not predict the absolute efficiency at high power, where pump depletion sets in.

**Resolved by.** The efficiency formula stated, with the plane at which each power was measured; coupling, filter and collection losses given separately, so that external and internal values can both be recovered; absolute efficiency plotted against pump power together with any normalised figure; the pump depletion regime identified; for parametric oscillators, the measured threshold compared with the threshold calculated from the stated coefficient.

**Benchmark.** [1], [5], [6]

## 2. Nonlinear coefficient: definition, convention and reference

**Question.** Which definition, convention and units does the paper use for the nonlinear coefficient (d or χ(2), SI or Gaussian units, a sheet or a bulk-like value for a two-dimensional material), is the value an effective coefficient for a given direction and polarisation or a tensor component, and is it absolute or relative to a reference material whose value is stated?

**Why it matters.** Definitions differ by numerical factors between texts, and values reported for the same crystal have spread widely, through these factors and through differing absolute scales. Relative methods such as Maker fringes inherit any error in the reference value, and several long-accepted reference values were later found to be too high because multiple reflections in plane-parallel samples were neglected. For two-dimensional materials, a bulk-like value depends on the thickness assumed.

**Resolved by.** The defining equation for the coefficient; the measured quantity identified as an effective coefficient with its propagation direction and polarisations, or as a tensor component with crystal orientation confirmed; for relative measurements, the reference material, its value, wavelength and source; corrections for reflections, walk-off and absorption described; wavelength scaling method stated where values are compared at different wavelengths; for thin layers, the thickness used and whether the value is a sheet quantity.

**Benchmark.** [1], [2], [5]

## 3. Phase matching

**Question.** Does the paper show that the interaction is phase matched or quasi-phase matched as claimed, with measured tuning curves (against temperature, angle or wavelength) compared with curves calculated from dispersion, and for periodically poled media, with the poling period, duty cycle and uniformity characterised; and for short pulses, is the effect of group-velocity mismatch on the interaction length taken into account?

**Why it matters.** Converting an efficiency into a coefficient, or comparing a device with theory, assumes phase matching that is uniform along the whole length. Non-uniform phase matching shortens the effective length and broadens or distorts the tuning curve. In QPM the first-order effective coefficient is reduced by 2/π, and duty-cycle errors, domains of the wrong orientation and accumulated period errors reduce it further. With short pulses, once the pump and generated pulses separate within the crystal, the efficiency falls below the value calculated for continuous or long-pulse operation.

**Resolved by.** Measured tuning curves overlaid on calculated ones, with the acceptance bandwidth compared with that expected for the interaction length; poling quality shown, for example by second-harmonic microscopy or selective etching, with the duty cycle stated; for short pulses, the group-velocity mismatch and the corresponding walk-off length compared with the crystal length; where phase matching is not needed, as in films much thinner than the coherence length, this stated and the coherence length given.

**Benchmark.** [1], [3], [5], [6]

## 4. Pump characterisation at the sample

**Question.** How were the beam size and profile, the pulse duration and shape, the repetition rate and the spectrum of the pump measured at the sample position, and how was the quoted intensity calculated: peak on axis or averaged, inside or outside the sample, with which width convention?

**Why it matters.** A coefficient extracted from harmonic power or from a Z-scan depends on the pump intensity, so errors in beam size or pulse duration pass directly, or squared, into the result; in careful absolute measurements the beam size can be the largest single source of error. Microscope objectives and other optics change the pulse at the sample, and standard Z-scan analysis assumes a Gaussian beam.

**Resolved by.** Beam profile measured at or near the sample, for example by knife edge or camera, with the width convention (full width at half maximum or 1/e² radius) stated; pulse duration measured after the focusing optics; the intensity formula given; spectral purity of the pump checked; where the beam parameters are uncertain, a calibration against a reference material of known nonlinearity measured in the same set-up.

**Benchmark.** [1], [4], [5]

## 5. Mechanism and time scale of a third-order response

**Question.** For a measured n2, χ(3) or two-photon absorption coefficient, does the paper separate the fast electronic response from slower contributions (thermal lensing, molecular reorientation, free carriers, cascaded second-order effects), and separate nonlinear refraction from nonlinear absorption?

**Why it matters.** With long pulses or high repetition rates, heating builds up over a pulse or many pulses and produces a thermal lens that can mask or mimic the electronic nonlinearity. Values measured with different pulse durations can therefore describe different physical processes. A closed-aperture Z-scan alone mixes nonlinear refraction with nonlinear absorption.

**Resolved by.** Open- and closed-aperture data, or another way of separating refraction and absorption; the dependence on irradiance, pulse duration, repetition rate or wavelength shown, or time-resolved data; the result labelled as an effective coefficient for the stated pulse duration, repetition rate and wavelength where the mechanisms are not separated.

**Benchmark.** [4], [5]

## 6. Origin of the detected signal

**Question.** Is the detected signal shown to come from the claimed process in the claimed material: at the expected wavelength and spectral width, with the expected power-law dependence on pump power over the range used, with a polarisation dependence consistent with the symmetry, and with the substrate, solvent or surrounding material measured on its own?

**Why it matters.** Two-photon-excited fluorescence or luminescence, harmonic generation in the substrate or at surfaces, and scattered pump light can all add to the measured signal. A slope below the expected order on a logarithmic plot can indicate saturation, pump depletion or damage, and the dependence on pump power is one of the main ways to separate contributions from different processes.

**Resolved by.** Spectra showing the generated peak and any broad background; signal plotted against pump power on logarithmic axes with the fitted slope; a substrate-only or solvent-only measurement under the same conditions and a description of how its contribution was removed; polarisation-resolved data compared with the expected tensor symmetry; filter transmission at the pump and signal wavelengths stated.

**Benchmark.** [1], [5], [7]

## 7. Optical damage, photo-induced and thermal effects

**Question.** At the power used for the headline result, does the paper show that the device or sample is stable and undamaged over the measurement time, and does it report the damage threshold, photorefractive or photochromic effects, and heating under its own pulse duration, repetition rate and spot size?

**Why it matters.** Photorefractive index changes, photochromic absorption and the formation of colour centres distort the beam and cause the output to drift, and their onset depends on intensity, repetition rate, spot size, material composition and temperature. Nanostructures, especially absorbing ones, can melt or change at moderate power, so a peak efficiency may not be repeatable. Damage thresholds depend on the pulse duration and conditions of the test.

**Resolved by.** The output recorded against time at the operating power; images or linear measurements of the sample before and after high-power exposure; repeated cycles giving the same result; operating temperature and material composition stated; any damage threshold quoted with the pulse duration, repetition rate, wavelength and spot size of the test.

**Benchmark.** [3], [5], [6], [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | R. C. Eckardt and R. L. Byer, Measurement of nonlinear optical coefficients by phase-matched harmonic generation, Proc. SPIE 1561, Inorganic Crystals for Optics, Electro-Optics, and Frequency Conversion, 119–127 (1991); read as the copy hosted by the Byer group at Stanford | doi:10.1117/12.50759 | full text | Sec. 1: a calculated parametric oscillator threshold disagreed with the observed one, prompting the measurements; Table I: reported values for the same KDP coefficient differ through differing definitions and absolute scales. Sec. 2: oscillator thresholds and other applications serve as checks of coefficient values; Maker-fringe and wedge methods are normally relative to a standard; phase-matched measurements give effective coefficients that depend on direction and polarisation; absolute measurements need careful spatial, temporal and spectral pump characterisation. Sec. 3: the coefficient is defined explicitly because notations differ; omitting walk-off changes the effective coefficient by up to 10%; plane-wave, focused-beam, pulsed and pump-depletion expressions for efficiency; the pulsed analysis requires group-velocity walk-off to be small. Sec. 4: knife-edge beam measurements, with beam-size uncertainty as large as all other errors combined; measured tuning curves compared with curves calculated from dispersion; intensity dependence checked for depletion and two-photon absorption; optics transmissions measured. Sec. 5: surface damage limit and efficiency against power compared with the depletion model |
| 2 | I. Shoji, T. Kondo, A. Kitamoto, M. Shirane and R. Ito, Absolute scale of second-order nonlinear-optical coefficients, J. Opt. Soc. Am. B 14, 2268–2294 (1997) | doi:10.1364/JOSAB.14.002268 | abstract | Abstract: absolute coefficients of many crystals redetermined by SHG, parametric fluorescence and difference-frequency generation; many accepted standard values are too high because multiple reflections in near plane-parallel samples were neglected; Miller's rule is a poorer wavelength-scaling method than others |
| 3 | D. S. Hum and M. M. Fejer, Quasi-phasematching, C. R. Physique 8, 180–198 (2007; published online 2006) | doi:10.1016/j.crhy.2006.10.022 | full text | Sec. 2.2: the QPM coefficient is the effective coefficient times 2 sin(πD)/mπ, so first order is reduced by 2/π, and the tuning curve keeps the sinc² shape. Sec. 2.3: wrong-orientation domains, duty-cycle errors and accumulating period errors reduce peak efficiency, with strict tolerance on period errors. Secs. 3.1.2 and 3.1.3: photorefractive and photochromic effects, including green-induced infrared absorption, distort beams in lithium niobate and tantalate, often requiring elevated temperature unless doped or stoichiometric material is used; gray tracking in KTP depends on intensity, repetition rate, spot size and growth method. Sec. 4.1.2: with ultrafast pulses, group-velocity mismatch reduces the gain below the quasi-stationary value once the group delay over the crystal approaches the pulse duration |
| 4 | M. Sheik-Bahae, A. A. Said, T.-H. Wei, D. J. Hagan and E. W. Van Stryland, Sensitive measurement of optical nonlinearities using a single beam, IEEE J. Quantum Electron. 26, 760–769 (1990); read as the copy hosted by CREOL, University of Central Florida | doi:10.1109/3.53394 | full text | Abstract, Secs. II and III: Z-scan analysis assumes a focused Gaussian beam; averaging factors differ for instantaneous and cumulative nonlinearities. Sec. IV: with 300 ns pulses the response of CS2 is thermal self-defocusing, while with picosecond pulses reorientational Kerr response dominates; Z-scan values are absolute, but the set-up can be calibrated with a standard such as CS2 if beam parameters are not well known. Abstract and Sec. V: a second scan with the aperture removed separates nonlinear absorption from refraction |
| 5 | N. Vermeulen, D. Espinosa, A. Ball, J. Ballato, P. Boucaud, G. Boudebs et al., Post-2000 nonlinear optical materials and measurements: data tables and best practices, J. Phys. Photonics 5, 035001 (2023); read as arXiv:2301.06138 | doi:10.1088/2515-7647/ac9e2f | full text | Sec. 2.1: report pump wavelength, peak power or irradiance, beam size and pulse width with their width conventions, repetition rate and polarisation relative to crystal axes; consider substrate influence and sample damage; state the formulas used for efficiencies and bandwidths; long pulses or high repetition rates give thermal effects that can mask the nonlinearity, so report an effective coefficient or separate contributions by power, wavelength and time dependence; long and short pulses can trigger different processes and give different damage thresholds. Sec. 2.2.1: verify phase matching and its parameters, define efficiency, check that SHG is not masked by two-photon-excited fluorescence; objectives modify pulses in SHG imaging. Sec. 2.2.2.4: Z-scan analysis assumes Gaussian beams, closed aperture alone gives a mixed effective coefficient. Sec. 3 introduction: free carriers from two-photon absorption act as an effective higher-order nonlinearity, and cascaded second-order effects can closely mimic bound-electronic third-order ones. Secs. 3.1.1.3, 3.3.1.3 and 3.4.1.4: report the substrate-only response; sheet and bulk-like susceptibilities of 2D materials differ by an assumed thickness; fragile metamaterials can melt, so guard against damage |
| 6 | D. Zhu, L. Shao, M. Yu, R. Cheng, B. Desiatov, C. J. Xin et al., Integrated photonics on thin-film lithium niobate, Adv. Opt. Photon. 13, 242 (2021); read as arXiv:2102.11956 | doi:10.1364/AOP.411024 | full text | Sec. 4.3.1: absolute SHG efficiency in waveguides scales with pump power and length squared, so the figure of merit is a normalised efficiency in %/W·cm²; phase-matching bandwidth is inversely proportional to interaction length; lower normalised efficiency in longer devices attributed to non-optimal duty cycle and non-uniform poling. Sec. 4.2.3: poling quality assessed by second-harmonic microscopy and by monitoring during poling. Sec. 7.1: photorefraction and other charge-carrier effects cause drift and limit power handling, more strongly in thin films and at visible wavelengths |
| 7 | B. Sain, C. Meier and T. Zentgraf, Nonlinear optics in all-dielectric nanoantennas and metasurfaces: a review, Adv. Photonics 1, 024002 (2019); read as arXiv:2002.03571 | doi:10.1117/1.AP.1.2.024002 | full text | Sec. 3: a THG efficiency limited by free carriers from two-photon absorption in the silicon substrate. Sec. 4 and Fig. 5: SHG departs from the quadratic power dependence at higher intensity because of resonator damage; two-photon-absorption photoluminescence appears in the spectrum alongside the harmonics. Secs. 1 and 6: heating and low damage thresholds limit absorbing plasmonic structures |
