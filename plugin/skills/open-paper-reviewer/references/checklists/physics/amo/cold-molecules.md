---
id: T-COLD-MOLECULES
name: Cold and ultracold molecules
type: technique
field: physics/amo
applies_when: the paper laser-cools molecules or holds them in a magneto-optical, magnetic, optical or tweezer trap, forms them from ultracold atoms by magnetoassociation or stimulated Raman adiabatic passage, or reports the number, temperature, degeneracy, internal-state purity, trap lifetime or collisional loss of cold molecules
version: "0.1"
---

# Cold and ultracold molecules

## 1. Optical cycling and photon budget

**Question.** For laser cooling or slowing, does the paper state the cycling transition, the repump lasers and the branching ratios they close, and does it measure the scattering rate and the number of photons scattered before molecules leave the cycle?

**Why it matters.** Molecules have no closed transition, so cooling needs the leak to other vibrational and rotational states kept to around one part in a hundred thousand or less, and calculated branching ratios for weak decays can be wrong by orders of magnitude. A trap lifetime or a velocity change that is short of what the claimed photon number implies points to an unclosed leak or to a force other than the one claimed.

**Resolved by.** The level scheme with each repump and the leak it closes; branching ratios measured, not only calculated; a scattering rate measured directly, for example from the decay of fluorescence when one repump is switched off; trap loss compared with the measured scattering rate and the stated residual leak; for a MOT, trapping shown to depend on the field gradient, with cloud size, oscillation frequency and damping measured and compared with a model.

**Benchmark.** [1], [2]

## 2. Molecule number and detection calibration

**Question.** How was the number of molecules, or the occupation of single-molecule traps, obtained from the detected signal, which conversion factors entered (scattering rate, detection efficiency, absorption cross-section, back-transfer efficiency), and are their uncertainties carried into the number and into densities derived from it?

**Why it matters.** Fluorescence counts become a number only through a scattering rate and a collection efficiency, each with an uncertainty of ten per cent or more and sometimes in disagreement with models by a factor of about two. Ground-state molecules are often counted only after reverse transfer and dissociation into atoms, and weakly bound molecules imaged directly absorb differently from free atoms, so each step scales the reported number.

**Resolved by.** Each conversion factor stated with its source and uncertainty; background from trapping or imaging light subtracted using images without molecules; reported numbers corrected explicitly for reverse-transfer and imaging efficiency, with the correction stated; the full uncertainty of the number, not only the shot-to-shot scatter, propagated into densities and rate coefficients; for single molecules in tweezers, the detection fidelity and the loss caused by imaging stated.

**Benchmark.** [1], [2], [3], [4]

## 3. Magnetoassociation and separation from atoms

**Question.** Does the paper state the magnetic-field sweep across the Feshbach resonance and the resulting atom-to-molecule conversion efficiency, and how were the molecules distinguished and separated from the unassociated atoms before they were counted or used?

**Why it matters.** Conversion follows a Landau-Zener-type dependence on sweep rate and is limited by the phase-space density of the atoms, so a stated efficiency means little without the conditions. Unassociated atoms usually outnumber the molecules, and unless they are removed or separated they appear in the images and collide with the molecules, changing both the count and any measured loss.

**Resolved by.** The resonance, the sweep and the conversion efficiency given with the atomic temperature and density; the molecular signal shown to vanish when association is skipped or the field is swept the wrong way; the method for removing each atomic species described, with a check that removal leaves the molecule number and temperature unchanged.

**Benchmark.** [4], [5]

## 4. STIRAP transfer efficiency

**Question.** How was the efficiency of transfer to the target deeply bound state measured, and if a one-way efficiency is quoted from a round-trip measurement, is the assumption of equal efficiency in both directions stated and tested?

**Why it matters.** Molecules in the target state are usually counted only after transfer back, so the measured quantity is the round-trip efficiency and the one-way value is commonly taken as its square root, which holds only if the two transfers are equally efficient. Transfer is complete only when the pulses are adiabatic and the relative phase of the two lasers is stable during the transfer; fast phase noise cannot be overcome with more laser power, and population left in the intermediate state decays and is lost or heats the sample.

**Resolved by.** Round-trip efficiency reported as measured, with any one-way value marked as derived and its assumption stated; the dependence of efficiency on pulse delay, two-photon detuning and Rabi frequencies shown; the laser locking scheme and relative linewidth stated; molecules remaining in the initial state after the forward pulse measured, or an independent check of the one-way efficiency where possible.

**Benchmark.** [3], [6], [7]

## 5. Identification and purity of the internal state

**Question.** How was the claimed vibrational, rotational and hyperfine state identified, and what fraction of the molecules is in it, with the fractions in other states measured, not assumed?

**Why it matters.** Several nearby levels can be reached by a given set of laser frequencies, so an assignment rests on comparison of measured binding energies, rotational constants and selection rules with predictions. Optical pumping into a single state typically leaves a sizeable fraction elsewhere, and molecules in unintended states change measured collision rates, coherence times and spectroscopic shifts.

**Resolved by.** The assignment supported by measured binding energy, rotational constant or Stark and Zeeman shifts compared with calculation; the population of the target state and of neighbouring states measured, for example by state-selective microwave transfer and detection; any step that removes molecules in other states described, with the resulting purity stated.

**Benchmark.** [1], [3], [7]

## 6. Temperature, phase-space density and degeneracy

**Question.** How was the temperature obtained (which expansion model, which fit function, over what range of expansion times), and if degeneracy or a phase-space density is claimed, does it rest on a fit that distinguishes a degenerate distribution from a classical one?

**Why it matters.** A non-thermal velocity distribution can expand ballistically in a way that resembles a thermal one, and position-dependent light scattering during imaging distorts the expansion, so the choice of fit model can shift the temperature by around ten per cent. A Gaussian fit to a degenerate Fermi gas overestimates the temperature over the whole cloud and misjudges the central density if fitted to the wings, and molecules formed from atoms may not have reached equilibrium.

**Resolved by.** The expansion model and fit function stated with residuals shown; expansion long enough for the cloud to grow well beyond its initial size; any extra terms in the fit justified and their effect quantified; for degeneracy claims, fits to both degenerate and classical distributions compared, with residuals, and trap frequencies given so that the Fermi temperature can be recomputed; evidence that the sample is near equilibrium, or a statement that it may not be.

**Benchmark.** [1], [2], [4]

## 7. Collisional loss rate coefficients

**Question.** How was a two-body loss rate coefficient extracted from the decay of molecule number, which density, temperature and trap frequencies entered it, and were one-body loss, heating and collisions with residual atoms included in the fit?

**Why it matters.** The coefficient is inversely proportional to the density assumed, which depends on the calibrated number, temperature and trap frequencies and is often the least certain input. Heating during the hold changes the density over time, and inhomogeneous density, one-body loss and evaporation all change the shape of the decay curve. The universal loss rate is a useful reference, but a measured rate above or below it is meaningful only within the combined uncertainty of these inputs.

**Resolved by.** The rate equation fitted, with one-body loss and heating included or shown to be negligible; temperature measured at several hold times; the density and its uncertainty stated, with the number calibration behind it; residual atoms shown to be removed; comparison with the universal rate stated with the uncertainty of the density.

**Benchmark.** [4], [8], [9]

## 8. Trap light and trap lifetime

**Question.** Does the paper identify what limits the lifetime of the trapped molecules (background gas, blackbody radiation, scattering of trap light, light-induced loss of collision complexes) and show how the trapping light affects loss, coherence and state-resolved measurements?

**Why it matters.** Trapping light can excite long-lived collision complexes and cause loss that is attributed to the molecules themselves, and chopping or turning off the trap light to test this can itself cause loss. Rotational states have different polarisabilities, so the trap shifts transition frequencies and limits coherence. In room-temperature apparatus, blackbody radiation can pump molecules to other vibrational states on timescales of seconds.

**Resolved by.** Lifetime measured as a function of trap intensity or with the light modulated, with a control for loss caused by the modulation itself; background-gas pressure and blackbody limit estimated and compared with the observed lifetime; trap polarisation and intensity stated, and differential light shifts estimated or measured for any coherence or spectroscopic claim.

**Benchmark.** [1], [7], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | N. J. Fitch and M. R. Tarbutt, Laser-cooled molecules, Adv. At. Mol. Opt. Phys. 70, 157 (2021); read as arXiv:2103.00968 | doi:10.1016/bs.aamop.2021.04.003 |
| 2 | H. J. Williams et al., Characteristics of a magneto-optical trap of molecules, New J. Phys. 19, 113035 (2017); read as arXiv:1706.07848 | doi:10.1088/1367-2630/aa8e52 |
| 3 | K.-K. Ni et al., A high phase-space-density gas of polar molecules, Science 322, 231 (2008); read as arXiv:0808.2963 | doi:10.1126/science.1163861 |
| 4 | L. De Marco et al., A degenerate Fermi gas of polar molecules, Science 363, 853 (2019); read as arXiv:1808.00028 | doi:10.1126/science.aau7230 |
| 5 | C. Chin et al., Feshbach resonances in ultracold gases, Rev. Mod. Phys. 82, 1225 (2010); read as arXiv:0812.1496 | doi:10.1103/RevModPhys.82.1225 |
| 6 | N. V. Vitanov et al., Stimulated Raman adiabatic passage in physics, chemistry, and beyond, Rev. Mod. Phys. 89, 015006 (2017); read as arXiv:1605.00224 | doi:10.1103/RevModPhys.89.015006 |
| 7 | T. Langen et al., Quantum state manipulation and cooling of ultracold molecules, Nat. Phys. 20, 702 (2024); read as arXiv:2305.13445 | doi:10.1038/s41567-024-02423-1 |
| 8 | R. Bause et al., Ultracold sticky collisions: theoretical and experimental status, J. Phys. Chem. A 127, 729 (2023); read as PMC9884084 | doi:10.1021/acs.jpca.2c08095 |
| 9 | Z. Idziaszek and P. S. Julienne, Universal rate constants for reactive collisions of ultracold molecules, Phys. Rev. Lett. 104, 113202 (2010) | doi:10.1103/PhysRevLett.104.113202 |
