---
id: T-OPTICAL-LATTICES
name: Optical lattices and quantum-gas microscopy
type: technique
field: physics/amo
applies_when: the paper holds ultracold atoms in an optical lattice or images them site by site, and bases a claim on lattice depth, a superfluid or Mott-insulating state, lattice temperature or entropy, spin or density correlations, or simulation of a Hubbard-type model
version: "0.1"
---

# Optical lattices and quantum-gas microscopy

## 1. Lattice depth calibration

**Question.** How was the lattice depth measured, in units of the recoil energy, which method was used and in which regime of that method, and what uncertainty in depth is carried into the quoted tunnelling and interaction energies?

**Why it matters.** The tunnelling energy falls roughly exponentially with the square root of the depth, so a modest error in depth becomes a large error in the tunnelling energy and in the ratio of interaction to tunnelling that locates a claimed transition. Pulsed-diffraction calibrations rely on a short-pulse approximation; outside it, a fit with the simple formula can underestimate the depth unless the pulse duration is modelled.

**Resolved by.** The calibration method named for each lattice axis (for example diffraction from a pulsed lattice, or amplitude-modulation spectroscopy of band transitions) with the pulse length or modulation range and the model used to analyse it; agreement between two methods or between pulse lengths; the depth uncertainty stated and propagated into the tunnelling energy, the interaction energy and their ratio; the calibration repeated or checked over the period of the measurements.

**Benchmark.** [1], [2], [4]

## 2. From lattice parameters to a Hubbard model

**Question.** How were the Hubbard tunnelling and interaction energies obtained from the lattice depth and the scattering length, and does the paper show that the conditions for a single-band model with nearest-neighbour tunnelling hold, or account for the terms that the standard model leaves out?

**Why it matters.** The single-band Hubbard description assumes that interaction energy, temperature and chemical potential are small compared with the gap to the first excited band, and that tunnelling beyond nearest neighbours is negligible. In shallow lattices, near a Feshbach resonance or at strong interactions, higher bands, density-induced tunnelling and other non-standard terms can matter, and the Gaussian profile of the lattice beams adds a position-dependent potential that the model may not include.

**Resolved by.** Tunnelling and interaction energies computed from band-structure or Wannier-function calculations at the calibrated depth, not only from deep-lattice approximations outside their range of accuracy; the band gap compared with interaction energy and temperature; an estimate of the size of next-neighbour, density-induced and higher-band terms where interactions are strong or the lattice is shallow; the confining potential from beam profiles and any additional trap included in the model used for comparison.

**Benchmark.** [1], [3], [4]

## 3. Evidence for superfluid and Mott-insulating states

**Question.** When the paper claims a superfluid, a Mott insulator or the transition between them, what does it use beyond the presence, sharpness or visibility of interference peaks in time-of-flight images?

**Why it matters.** Sharp peaks in the time-of-flight momentum distribution reflect phase coherence, which can persist over several sites in a Mott insulator and in a normal gas above the critical temperature. Peak width judged by eye has no fixed threshold, and visibility changes smoothly across the transition, so peaks alone do not establish superfluidity, and their loss alone does not establish a Mott insulator.

**Resolved by.** A quantitative criterion stated in advance, such as visibility or peak fraction compared with a calculation at the stated temperature and trap; independent signatures of the insulating state, such as a measured excitation gap from modulation spectroscopy or a potential gradient, or in-situ density plateaus of an incompressible region; for superfluid claims, a probe of superfluid response, not only coherence; comparison of time-of-flight data with simulations that include the trap, expansion and imaging resolution.

**Benchmark.** [1], [5], [6]

## 4. Trap inhomogeneity and local versus averaged quantities

**Question.** Does the paper account for the variation of density across the trap, and is each claimed phase or correlation attributed to a region of known local density, not to an average over the whole cloud?

**Why it matters.** In a trapped gas the local chemical potential changes with position, so a single sample contains Mott shells at integer filling alternating with superfluid or metallic regions, and these respond differently to temperature. A signal averaged over the cloud mixes these regions and can be read as a property of a phase that occupies only part of it. Results stated for a homogeneous system then rely on the local density approximation.

**Resolved by.** In-situ density profiles, or site-resolved images, showing where each phase sits; correlations and structure factors evaluated within a stated density window or in a flattened potential; comparison with calculations that include the actual trap, or a stated justification for the local density approximation; the number of atoms and the trap frequencies given so that the shell structure can be estimated.

**Benchmark.** [1], [4], [5]

## 5. Single-site detection fidelity

**Question.** What is the detection fidelity of the microscope: the probability of atom loss and of hopping to another site during imaging, and the rates of false and missed detections from the reconstruction, and how do these enter the reported densities and correlations?

**Why it matters.** Fluorescence imaging heats atoms while they scatter many photons, so atoms can be lost or move to neighbouring sites before they are recorded. Site occupations are assigned by a reconstruction algorithm that uses a point-spread function, a lattice geometry and an intensity threshold, and errors in any of them propagate into the reported occupations and correlations.

**Resolved by.** Loss and hopping fractions measured, for example by comparing consecutive images of the same sample; the reconstruction method, point-spread function and threshold described, with a fidelity estimate from simulated or repeated images; the effect of the stated detection errors on correlation functions estimated or corrected for; the imaging fidelity reported for the same settings as the data.

**Benchmark.** [7], [8]

## 6. Parity projection and what the detected signal measures

**Question.** If light-assisted collisions during imaging remove atom pairs, does the paper treat the detected occupation as the occupation modulo two, and does it state how spin or full number resolution was obtained where a claim needs them?

**Why it matters.** With parity projection, doubly occupied sites look empty, so the detected density saturates and a shell with two atoms per site appears as a ring of empty sites. In two-component Fermi gases the detected signal is a combination of occupations equal to the local moment, not the density, and doublons and holes cannot be distinguished, which changes what a measured correlation means.

**Resolved by.** The detected observable written down in terms of site occupations and compared with theory in that form; a stated method, such as a pinning lattice, bilayer separation or selective removal of one spin state, whenever the claim requires spin resolution, double occupancy or full counting; the efficiency of any spin-removal or separation step measured and included in the analysis.

**Benchmark.** [4], [7], [8]

## 7. Temperature, entropy and adiabatic loading

**Question.** How were the temperature and entropy in the lattice determined, which model and numerical method did the thermometry rely on, and does the paper show that loading and holding were close enough to adiabatic for the inferred values to apply?

**Why it matters.** Temperatures in a lattice are usually inferred by fitting data to a model, such as an atomic-limit expression, a series expansion or quantum Monte Carlo calculations, and inherit its assumptions about equilibrium and the trap. Entropy, not temperature, is conserved in adiabatic loading, while spontaneous emission, laser noise and finite ramp times add heat, and the resulting error in temperature can grow substantially in deeper lattices. At strong coupling the Néel temperature lies far below the temperature at which a Mott insulator forms, so a Mott insulator does not imply magnetic order.

**Resolved by.** The thermometry method and model stated, with the range of validity of the model shown to cover the data; temperature quoted relative to the scale that matters for the claim, such as the tunnelling, interaction or superexchange energy or the Néel temperature, with its uncertainty; entropy before and after loading compared, or temperatures from two independent methods agreeing; measured heating rates and ramp times, with the heating they cause estimated and corrected for; how entropy is distributed across the trap, where the claim concerns the central region.

**Benchmark.** [4], [6], [7], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | I. Bloch et al., Many-body physics with ultracold gases, Rev. Mod. Phys. 80, 885 (2008); read as preprint arXiv:0704.3011 | doi:10.1103/RevModPhys.80.885 |
| 2 | B. Gadway et al., Analysis of Kapitza-Dirac diffraction patterns beyond the Raman-Nath regime, Opt. Express 17, 19173 (2009); read as preprint arXiv:0907.3507 | doi:10.1364/OE.17.019173 |
| 3 | O. Dutta et al., Non-standard Hubbard models in optical lattices: a review, Rep. Prog. Phys. 78, 066001 (2015); read as preprint arXiv:1406.0181 | doi:10.1088/0034-4885/78/6/066001 |
| 4 | L. Tarruell and L. Sanchez-Palencia, Quantum simulation of the Hubbard model with ultracold fermions in optical lattices, C. R. Physique 19, 365 (2018); read as preprint arXiv:1809.00571 | doi:10.1016/j.crhy.2018.10.013 |
| 5 | R. B. Diener et al., Criterion for bosonic superfluidity in an optical lattice, Phys. Rev. Lett. 98, 180404 (2007); read as preprint arXiv:cond-mat/0609685 | doi:10.1103/PhysRevLett.98.180404 |
| 6 | S. Trotzky et al., Suppression of the critical temperature for superfluidity near the Mott transition, Nat. Phys. 6, 998 (2010); read as preprint arXiv:0905.4882, subtitled validating a quantum simulator | doi:10.1038/nphys1799 |
| 7 | J. F. Sherson et al., Single-atom-resolved fluorescence imaging of an atomic Mott insulator, Nature 467, 68 (2010); read as preprint arXiv:1006.3799 | doi:10.1038/nature09378 |
| 8 | C. Gross and W. S. Bakr, Quantum gas microscopy for single atom and spin detection, Nat. Phys. 17, 1316 (2021); read as preprint arXiv:2010.15407 | doi:10.1038/s41567-021-01370-5 |
| 9 | D. McKay and B. DeMarco, Cooling in strongly correlated optical lattices: prospects and challenges, Rep. Prog. Phys. 74, 054401 (2011) | doi:10.1088/0034-4885/74/5/054401 |
