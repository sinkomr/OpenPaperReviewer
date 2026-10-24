---
id: T-OPTICAL-LATTICES
name: Optical lattices and quantum-gas microscopy
type: technique
field: physics/amo
applies_when: the paper holds ultracold atoms in an optical lattice or images them site by site, and bases a claim on lattice depth, a superfluid or Mott-insulating state, lattice temperature or entropy, spin or density correlations, or simulation of a Hubbard-type model
version: "0.1"
---

# Optical lattices and quantum-gas microscopy

Ultracold atoms in optical lattices (periodic potentials formed by interfering laser beams) are used to claim realisations of Bose- and Fermi-Hubbard models, transitions between superfluid and Mott-insulating states, and correlated phases such as antiferromagnets. Quantum-gas microscopes, which image the lattice by fluorescence with single-site resolution, are used to claim local densities, spin and density correlations, temperatures and entropies, all inferred through a model that links the laser intensity and the detected photons to the Hubbard parameters and site occupations.

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

**Why it matters.** Temperatures in a lattice are usually inferred by fitting data to a model, such as an atomic-limit expression, a series expansion or quantum Monte Carlo calculations, and inherit its assumptions about equilibrium and the trap. Entropy, not temperature, is conserved in adiabatic loading, while spontaneous emission, laser noise and finite ramp times add heat, and the resulting error in temperature can grow substantially in deeper lattices.

**Resolved by.** The thermometry method and model stated, with the range of validity of the model shown to cover the data; temperature quoted relative to the tunnelling, interaction or superexchange energy that matters for the claim, with its uncertainty; entropy before and after loading compared, or temperatures from two independent methods agreeing; measured heating rates and ramp times, with the heating they cause estimated and corrected for; how entropy is distributed across the trap, where the claim concerns the central region.

**Benchmark.** [4], [6], [7], [9]

## 8. Claims of simulating a Hubbard-type model

**Question.** When the paper claims to simulate a Hubbard-type model or to observe one of its phases, does it validate the experiment against reliable calculations in a regime where they exist, and does it show that the temperature, system size and imperfections are small enough for the conclusion to refer to the model and not to the apparatus?

**Why it matters.** Agreement in a regime that classical methods can check is the main evidence that a lattice experiment realises the intended model, but it does not guarantee correctness where no check is possible. Disorder, residual trap potentials and heating can shift an apparent transition point or change fitted exponents, and at strong coupling the magnetic ordering temperature lies far below the temperature at which a Mott insulator forms, so reaching a Mott insulator does not imply reaching an ordered phase.

**Resolved by.** Comparison with numerical results, such as quantum Monte Carlo or series expansions, for the actual trap and temperature without free parameters, at least in a regime where those results are reliable; the measured temperature compared with the relevant ordering scale, such as the Néel temperature or the superexchange energy; estimates of disorder, residual potential gradients and finite-size effects, and how they would alter the observed signal; claims beyond the validated regime stated as such.

**Benchmark.** [4], [6], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | I. Bloch, J. Dalibard and W. Zwerger, Many-body physics with ultracold gases, Rev. Mod. Phys. 80, 885–964 (2008); read as preprint arXiv:0704.3011 | doi:10.1103/RevModPhys.80.885 | full text | Preprint Sec. II.2, Eq. 38 and Table 1: tunnelling falls exponentially with the square root of the depth in recoil units, and the asymptotic formula is accurate to about 10% only above 15 recoil energies. Secs. II.4 and IV.1: single-band model needs thermal and interaction energies well below the band gap and nearest-neighbour hopping; it can fail near Feshbach resonances. Sec. IV.2: in a trap, Mott shells alternate with superfluid regions in the local density approximation; interference peaks persist in the Mott phase while coherence extends over several sites, visibility changes smoothly, and peaks do not by themselves probe superfluidity; the Mott gap measured by modulation spectroscopy or a potential gradient |
| 2 | B. Gadway, D. Pertot, R. Reimann, M. G. Cohen and D. Schneble, Analysis of Kapitza-Dirac diffraction patterns beyond the Raman-Nath regime, Opt. Express 17, 19173 (2009); read as preprint arXiv:0907.3507 | doi:10.1364/OE.17.019173 | full text | Sec. 4: for weak pulses outside the Raman-Nath regime, a fit with the Raman-Nath formula returns a depth reduced by a sinc factor in the pulse length. Sec. 6: tunnelling depends exponentially on depth and pulses deep in the Raman-Nath regime are hard to realise; with numerical modelling, calibrations at three pulse lengths agree within 4% and agree with an independent adiabatic-loading method within 10% |
| 3 | O. Dutta, M. Gajda, P. Hauke, M. Lewenstein, D.-S. Lühmann, B. A. Malomed, T. Sowiński and J. Zakrzewski, Non-standard Hubbard models in optical lattices: a review, Rep. Prog. Phys. 78, 066001 (2015); read as preprint arXiv:1406.0181 | doi:10.1088/0034-4885/78/6/066001 | full text | Abstract and Sec. I.4: experiments show effects outside the standard Hubbard model, including density-induced tunnelling and higher-band effects, the latter important at strong interactions even in deep lattices. Sec. II.2: the standard nearest-neighbour approximation may be poor in shallow lattices. Sec. III.2.1: at depths of about ten recoil energies and above, density-induced tunnelling is considerably larger than the other neglected terms |
| 4 | L. Tarruell and L. Sanchez-Palencia, Quantum simulation of the Hubbard model with ultracold fermions in optical lattices, C. R. Physique 19, 365–393 (2018); read as preprint arXiv:1809.00571 | doi:10.1016/j.crhy.2018.10.013 | full text | Sec. 2.2: tunnelling and interaction energies from depth and scattering length; single-band validity requires interaction, temperature and chemical potential below the first excited band; Gaussian beams and the trap give a position-dependent potential and a wedding-cake profile in the local density approximation. Sec. 2.3: the Néel temperature lies well below the Mott temperature at strong coupling. Secs. 4.1 to 5.2: temperatures inferred by comparison with series expansions, linked-cluster expansions, dynamical mean-field theory and quantum Monte Carlo; light-assisted collisions make empty and doubly occupied sites look alike, so the detected signal equals the local moment; spin resolution by removing one spin state, and doublon detection with a pinning lattice; entropy concentrates in metallic shells and is redistributed to cool the centre |
| 5 | R. B. Diener, Q. Zhou, H. Zhai and T.-L. Ho, Criterion for bosonic superfluidity in an optical lattice, Phys. Rev. Lett. 98, 180404 (2007); read as preprint arXiv:cond-mat/0609685 | doi:10.1103/PhysRevLett.98.180404 | full text | Abstract and Fig. 1: a normal Bose gas above the critical temperature can show a similarly sharp momentum distribution, so narrow peaks do not establish condensation; sharpness is judged by eye with no quantitative definition. Sec. C: visibility proposed as a quantitative criterion. Sec. D: in a trap, superfluid and Mott shells alternate, and measured visibilities point to heating of the superfluid regions |
| 6 | S. Trotzky, L. Pollet, F. Gerbier, U. Schnorrberger, I. Bloch, N. V. Prokof'ev, B. Svistunov and M. Troyer, Suppression of the critical temperature for superfluidity near the Mott transition, Nat. Phys. 6, 998–1004 (2010); read as preprint arXiv:0905.4882, subtitled validating a quantum simulator | doi:10.1038/nphys1799 | full text | Comparison of time-of-flight images with quantum Monte Carlo for the actual trap, including expansion and imaging resolution, without free parameters; broad interference peaks also appear in the normal phase at strong interactions; the temperature found by matching to simulations agrees with that from assumed entropy conservation in a shallow lattice but is up to about 30% higher in a deeper one, attributed to heating from spontaneous scattering, laser noise and finite ramp times |
| 7 | J. F. Sherson, C. Weitenberg, M. Endres, M. Cheneau, I. Bloch and S. Kuhr, Single-atom-resolved fluorescence imaging of an atomic Mott insulator, Nature 467, 68–72 (2010); read as preprint arXiv:1006.3799 | doi:10.1038/nature09378 | full text | Main text and Methods: light-assisted collisions remove pairs, so only occupation modulo two is recorded and shells of two atoms per site appear empty; about 1% loss and 0.5% hopping during imaging, hopping measured from consecutive images; reconstruction by deconvolution with a measured point-spread function and fidelity about 99.5% from simulated images; temperature and entropy from fits to an atomic-limit model assuming equilibrium and the local density approximation |
| 8 | C. Gross and W. S. Bakr, Quantum gas microscopy for single atom and spin detection, Nat. Phys. 17, 1316–1323 (2021); read as preprint arXiv:2010.15407 | doi:10.1038/s41567-021-01370-5 | full text | Section on optical lattices: reconstruction uses the known lattice geometry, with zero-or-one fidelity well above 99% at typical signal-to-noise. Section on quantum gas microscopy: atoms scatter many photons during imaging; photoassociation makes microscopes detect the parity of the site occupation; pinning lattices and superlattices with magnetic fields recover number and spin. Section on new directions: bilayer readout avoids parity projection |
| 9 | D. McKay and B. DeMarco, Cooling in strongly correlated optical lattices: prospects and challenges, Rep. Prog. Phys. 74, 054401 (2011) | doi:10.1088/0034-4885/74/5/054401 | abstract | Abstract: reaching temperatures where Hubbard physics beyond current theory appears is difficult, progress needs better thermometry as well as cooling, and the review covers thermometry methods and the main sources of heating in lattice experiments |
| 10 | P. Hauke, F. M. Cucchietti, L. Tagliacozzo, I. Deutsch and M. Lewenstein, Can one trust quantum simulators?, Rep. Prog. Phys. 75, 082401 (2012); read as preprint arXiv:1109.6457 | doi:10.1088/0034-4885/75/8/082401 | full text | Sec. II: reliability within a stated error, checked in regimes classical methods can treat. Sec. IV.2: validation in tractable regimes does not guarantee robustness beyond them; Hubbard models in optical lattices as a main example, with numerics used to correct inferred temperatures by up to 30%. Secs. VI and VII: in the model studied (a transverse-field Ising chain), disorder of a few percent shifts the apparent critical point and changes fitted exponents |
