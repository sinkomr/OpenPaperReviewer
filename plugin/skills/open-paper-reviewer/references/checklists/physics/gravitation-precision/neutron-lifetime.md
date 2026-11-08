---
id: T-NEUTRON-LIFETIME
name: Neutron lifetime and neutron interferometry
type: technique
field: physics/gravitation-precision
applies_when: the paper measures the free neutron lifetime with a cold neutron beam or with ultracold neutrons stored in a material, magnetic or gravitational trap, compares lifetimes between methods, or bases a scattering length, gravitational phase or new-interaction limit on a neutron interferometer phase
version: "0.1"
---

# Neutron lifetime and neutron interferometry

## 1. Absolute neutron counting in beam measurements

**Question.** How was the number of neutrons in the decay volume determined: which neutron monitor, with what absorber areal density, cross section, detector solid angle and beam profile, and was the monitor efficiency calibrated absolutely by an independent method?

**Why it matters.** A beam lifetime is a ratio of neutron counts to decay-product counts, so any error in the neutron detection efficiency passes directly into the lifetime. A monitor whose absorption is inversely proportional to neutron velocity (the 1/v law) cancels the beam spectrum only if the law holds for it and it intercepts the whole beam, and the areal density of the absorbing deposit and the tabulated cross section can dominate the systematic uncertainty.

**Resolved by.** The monitor efficiency stated with each contribution (deposit mass and uniformity, cross section, solid angle, absorption and scattering in the deposit and substrates, beam profile over the deposit) and its effect on the lifetime in seconds; the beam halo outside the deposit measured; ideally an absolute calibration of the monitor by an independent technique, with the shift it causes in the lifetime shown.

**Benchmark.** [1], [2]

## 2. Decay-product counting and the decay volume

**Question.** How were the decay products counted and the effective decay volume defined: how was the proton or electron detection efficiency established, how were the ends of the decay region handled, and do decay products from the full width of the beam reach the active detector area?

**Why it matters.** Protons born near the ends of an electrostatic trap may or may not be trapped, so the effective length is uncertain; a fit over several trap lengths removes it only if the end contribution is the same for every length, and field non-uniformity breaks that. Protons that backscatter from the detector or lose energy in its dead layer fall below threshold, a loss that is hard to compute reliably. Gamma rays from neutron capture near the beam give a background that is usually much larger than the decay rate.

**Resolved by.** The decay rate measured against a varied decay-volume length, with the fit and its residuals shown; corrections for non-linearity derived from measured fields and simulated trapping; the detection efficiency measured with different detectors, dead layers and acceleration potentials and extrapolated to zero backscatter; beam images showing that products from the whole beam reach the active detector; beam-off and background rates reported.

**Benchmark.** [1], [2]

## 3. Wall losses and the extrapolation to zero loss

**Question.** In a material bottle, how were losses at the walls separated from beta decay: what was varied (bottle size, surface-to-volume ratio, neutron energy spectrum), how far is the measured storage time from the extrapolated lifetime, and what model links the measurements to the point of zero wall loss?

**Why it matters.** The measured storage time combines decay with upscattering and capture at the walls and escape through gaps or coating defects, and these loss rates depend on neutron velocity while the velocity spectrum changes during storage. The lifetime then rests on an extrapolation whose model and range set much of the uncertainty, and reanalyses of loss corrections in stored-neutron data have moved results by several seconds.

**Resolved by.** All storage times plotted against the varied loss parameter, with the extrapolation and its range stated; a loss model that includes the velocity dependence of the loss per bounce and the evolving spectrum, tested by simulation; a test of coating integrity, for example on a substrate that does not reflect neutrons; the lifetime obtained with alternative loss models reported.

**Benchmark.** [1], [4]

## 4. Marginally trapped neutrons and spectral cleaning

**Question.** How were neutrons with energy above the confining potential of the trap removed before storage, and how does the paper show that none remained, or gained energy during storage, in numbers large enough to bias the lifetime?

**Why it matters.** Neutrons slightly above the wall or trap potential escape only when they strike the wall at a suitable angle, and in smooth, symmetric traps some orbits survive for times comparable to the lifetime, adding a loss that lowers the extracted lifetime. Cleaning the spectrum reduces this population but does not remove it completely, and stored neutrons can also be heated, for example by vibration of the trap.

**Resolved by.** The cleaning procedure, its duration and the cleaning height relative to the trap depth stated; trap shapes or surfaces that randomise trajectories; runs with cleaning disabled or reduced to show the size of the effect; counting at heights above the cleaning level after storage, and the limit this sets on uncleaned and heated neutrons, carried into the uncertainty.

**Benchmark.** [1], [3]

## 5. Other losses, normalisation and counting over storage time

**Question.** Are loss channels other than beta decay bounded, such as depolarisation in magnetic traps and upscattering on residual gas, and how were the initial number of trapped neutrons and the counting efficiency kept comparable between short and long storage times?

**Why it matters.** A magnetic trap holds one spin state, so spin flips where the field is weak or zero let neutrons escape and mimic decay, and residual gas upscatters neutrons at a rate set by its pressure and composition. The number loaded varies with source intensity and spectrum, and if transport to the detector, timing or rate-dependent effects such as dead time and pile-up differ between short and long storage times, the ratio of counts no longer measures decay alone.

**Resolved by.** The holding field and an upper limit on the depolarisation rate; pressure and gas composition measured through the run, with cross sections and their uncertainties; monitor detectors that normalise for source intensity and spectrum, with the normalisation model and its sensitivity stated; detection inside the trap, or losses in transport shown not to depend on storage time; the effective storage time taken from the measured arrival-time distribution; rate-dependent corrections tested on simulated data.

**Benchmark.** [1], [3]

## 6. Comparison between methods

**Question.** When a lifetime is compared or combined with other measurements, does the paper state what each method actually measures, compare with the results of each method separately, and say how the uncertainty is treated when the results are not mutually consistent?

**Why it matters.** Beam measurements count only decays with charged particles in the final state, while storage measurements count surviving neutrons and so measure the total rate of disappearance, and the two face different systematic effects. An average over measurements that are not mutually consistent needs an enlarged uncertainty and can depend on which results are included, and some earlier results have been reanalysed or withdrawn.

**Resolved by.** Comparison with each method's average separately, with the averaging procedure, scale factor or consistency test given; superseded or withdrawn values replaced by their updates; a statement of which systematic effects the new measurement shares with each method; any interpretation in terms of new decay channels accompanied by an account of the systematic effects in both methods that could produce the same difference.

**Benchmark.** [1], [2], [4]

## 7. Interferometer phase stability and the differential measurement

**Question.** How was the phase shift of interest separated from drifts of the interferometer's intrinsic phase: were the configurations compared interleaved in time, what fringe contrast was achieved, and were extra phases from cell walls, windows and holders measured or made equal in both paths?

**Why it matters.** Perfect-crystal interferometers are sensitive to temperature gradients, air flow, vibration and bending, which lower the contrast and make the intrinsic phase drift during the half hour or so needed to record an interferogram. A phase measured before and after a change, instead of interleaved with it, can contain that drift, and small differences in material thickness between the paths, or across the beam, add phase shifts of their own.

**Resolved by.** Interferograms for all settings recorded interleaved with the phase-shifter steps; the contrast stated; equal material in both paths, the sample swapped between paths, and mapped thickness variations corrected with their uncertainty; temperature control and vibration isolation described.

**Benchmark.** [5], [7]

## 8. Interferometer phase model: crystal deformation, dynamical diffraction and wavelength

**Question.** When a measured phase is compared with a prediction, such as the phase from gravity or rotation as the interferometer is tilted, does the analysis account for deformation of the crystal as it moves, for dynamical-diffraction effects, and for the measured wavelength distribution?

**Why it matters.** Rotating a crystal interferometer bends it under its own weight, adding a phase that changes with the rotation as the signal does, and dynamical diffraction in an accelerated frame changes the expected phase by several per cent. Residual differences of order one per cent between measured and predicted gravity-induced phases have been reported with measurement errors much smaller than that, and with grating interferometers an imprecisely measured broad wavelength spectrum limits the comparison.

**Resolved by.** A phase model that includes the dynamical-diffraction and deformation terms, or a method that monitors the deformation directly, such as measuring at two wavelengths in the same setup; the wavelength distribution measured, not assumed; the remaining difference from prediction stated and compared with earlier precision measurements before a new interaction is inferred from it.

**Benchmark.** [5], [6]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | F. E. Wietfeldt, Measurements of the neutron lifetime, Atoms 6, 70 (2018) | doi:10.3390/atoms6040070 |
| 2 | J. S. Nico et al., Measurement of the neutron lifetime by counting trapped protons in a cold neutron beam, Phys. Rev. C 71, 055502 (2005); read as preprint arXiv:nucl-ex/0411041 | doi:10.1103/PhysRevC.71.055502 |
| 3 | F. M. Gonzalez et al. (UCNτ collaboration), Improved neutron lifetime measurement with UCNτ, Phys. Rev. Lett. 127, 162501 (2021); read as preprint arXiv:2106.10375 | doi:10.1103/PhysRevLett.127.162501 |
| 4 | S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110, 030001 (2024); neutron listing read at https://pdg.lbl.gov/2024/listings/rpp2024-list-n.pdf | doi:10.1103/PhysRevD.110.030001 |
| 5 | J. Klepp et al., Fundamental phenomena of quantum mechanics explored with neutron interferometers, Prog. Theor. Exp. Phys. 2014, 082A01 (2014); read as preprint arXiv:1407.2526 | doi:10.1093/ptep/ptu085 |
| 6 | S. Sponar et al., Tests of fundamental quantum mechanics and dark interactions with low-energy neutrons, Nat. Rev. Phys. 3, 309 (2021); read as the extended preprint arXiv:2012.09048 | doi:10.1038/s42254-021-00298-2 |
| 7 | H. Lemmel et al., Neutron interferometry constrains dark energy chameleon fields, Phys. Lett. B 743, 310 (2015); read as preprint arXiv:1502.06023 | doi:10.1016/j.physletb.2015.02.063 |
