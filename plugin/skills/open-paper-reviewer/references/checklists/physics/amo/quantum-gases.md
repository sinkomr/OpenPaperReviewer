---
id: T-QUANTUM-GASES
name: Bose-Einstein condensates and degenerate Fermi gases
type: technique
field: physics/amo
applies_when: the paper reports a Bose-Einstein condensate, a degenerate Fermi gas or a pair condensate of ultracold atoms, or bases a claim about condensate fraction, temperature, degeneracy, atom number, scattering length or superfluidity on absorption or time-of-flight images
version: "0.1"
---

# Bose-Einstein condensates and degenerate Fermi gases

Experiments on ultracold atomic gases claim Bose-Einstein condensation (BEC), Fermi degeneracy (a temperature T well below the Fermi temperature T_F), condensation of fermion pairs and superfluidity. They also report condensate fractions, temperatures, atom numbers and interaction strengths set by Feshbach resonances. Nearly all of these are inferred from absorption images of the cloud, usually after a time of flight (TOF) in which the cloud expands freely.

## 1. Evidence of condensation

**Question.** Does the claim of condensation rest on more than one signature, such as a bimodal density profile, an aspect ratio after expansion that differs from that of the thermal cloud, and a dense component that appears at a threshold and grows as cooling continues, and is that threshold compared with the critical temperature expected from the atom number and trap frequencies?

**Why it matters.** Each signature has ordinary look-alikes. Collisions in a dense thermal cloud can make its expansion anisotropic, and a strongly interacting normal gas inverts its aspect ratio during expansion, so aspect-ratio inversion alone shows strong interactions rather than condensation. In the Thomas-Fermi regime the condensate and thermal cloud have the same aspect ratio in the trap, so in-situ shape alone does not reveal the onset.

**Resolved by.** A series of images or profiles across the threshold showing the dense component appearing and growing while the thermal wings shrink; the aspect ratio after expansion shown together with the bimodal profile; the atom number at the observed onset compared with the ideal-gas critical number for the measured trap frequencies, with interaction shifts of the critical temperature taken into account.

**Benchmark.** [1], [2], [7]

## 2. Condensate fraction and temperature from bimodal fits

**Question.** Which functions were fitted to the thermal and condensed parts of the profile, which region was excluded from the thermal fit and how was it chosen, and does the paper show that the resulting condensate fraction and temperature do not depend on these choices?

**Why it matters.** A Gaussian thermal component ignores Bose enhancement near the critical temperature, and fitting the thermal part too close to the condensate can bias the temperature by about 20 per cent. The condensate number depends strongly on the assumed bimodal shape, and the size of the excluded region is often chosen by hand. Interactions between the condensate and the thermal cloud distort the overlap region and lower the condensate fraction below the ideal-gas curve.

**Resolved by.** The fit functions stated, with a Bose-enhanced thermal component near the transition; the excluded region given and the results shown to be stable as it is varied; temperature taken from the outer wings; a residual plot or fitted profile overlaid on the data; condensate fraction against reduced temperature compared with an interacting model, not only the ideal-gas curve; a separate method, such as spatially separating the two components, where condensed fractions are high.

**Benchmark.** [1], [6], [7]

## 3. Atom number from absorption imaging

**Question.** How was the optical density converted to atom number: which absorption cross-section, probe polarisation, detuning and intensity were used, how was the probe intensity calibrated against the effective saturation intensity, and was the peak optical density low enough to be measured?

**Why it matters.** The atom number scales inversely with the absorption cross-section, which depends on the probe polarisation, the excited-state structure and the populations of the ground-state sublevels; birefringent windows and stray fields make the effective saturation intensity hard to predict. At high probe intensity the result also depends on the absolute intensity at the atoms. At low probe intensity, optical densities above about 3 or 4 cannot be measured reliably, dense clouds imaged off resonance refract light like a lens, and for light atoms the recoil from the probe pulse shifts them out of resonance during the exposure.

**Resolved by.** The cross-section and any correction factor stated with how it was measured, for example by requiring the optical density to be independent of probe intensity or by measuring the momentum the probe transfers to the atoms; the resonance frequency found by a method insensitive to lensing; the peak optical density reported and kept within the measurable range, for example by imaging after expansion or with high intensity; the atom number cross-checked against an independent route such as the atom number at the critical temperature.

**Benchmark.** [1], [4], [5]

## 4. Time-of-flight mapping and trap parameters

**Question.** Which expansion model converts the measured sizes after time of flight into temperature, chemical potential or momentum, are the trap frequencies and imaging magnification measured and reported, and does the paper show that the expansion is ballistic, or model it if it is not?

**Why it matters.** The standard scaling of a thermal cloud's width assumes collisionless expansion from a harmonic trap with known frequencies, and a condensate's mean-field energy changes how it expands. Collisions soon after release, hydrodynamic flow in strongly interacting gases and mean-field repulsion all break the ballistic assumption and can bias the inferred temperature by an estimated 10 to 20 per cent. Typical expansion times may not reach the asymptotic aspect ratio of a condensate.

**Resolved by.** Trap frequencies measured, for example from centre-of-mass or breathing oscillations, with their uncertainty; magnification and pixel size calibrated; the expansion time and model given; for interacting or dense clouds, evidence that the expansion is ballistic, such as sizes measured at several expansion times or temperatures from different axes that agree, or else a hydrodynamic or interacting expansion model.

**Benchmark.** [1], [2], [7]

## 5. Degeneracy of Fermi gases

**Question.** How was T/T_F determined: from which fit function, over which region of the profile, with which atom number and trap frequencies entering T_F, and is the method valid for the interaction regime of the sample?

**Why it matters.** At low T/T_F the profile of a Fermi gas changes only in its wings beyond the Fermi radius, so the fitted temperature is limited by the signal-to-noise ratio there, and imaging effects can make a cloud look colder than it is. T_F itself depends on the atom number and trap frequencies, which carry their own calibration errors. Fitting an ideal Fermi profile to a strongly interacting cloud gives only an empirical temperature, and such clouds can be superfluid while their profiles look smooth.

**Resolved by.** The fit function and the fugacity or T/T_F it returns, with the uncertainty from atom number and trap frequencies included in T_F; full two-dimensional fits or fits to the wings with their signal-to-noise stated, and imaging resolution shown not to distort the wings; for strongly interacting gases, a thermometer suited to that regime, such as the ideal-gas wings of an imbalanced mixture or an entropy determined after an adiabatic sweep to a weakly interacting regime, rather than an ideal-gas fit labelled as a temperature.

**Benchmark.** [2]

## 6. Interaction strength and Feshbach resonances

**Question.** How was the scattering length obtained: which resonance position, width and background scattering length were used and from where, how was the magnetic field at the atoms calibrated, and how do its stability and spread compare with the width of the resonance?

**Why it matters.** Near a Feshbach resonance the scattering length diverges at the resonance position, so a small field error near the pole, or near a narrow resonance, changes the interaction strength by a large factor. Loss features can sit far from the true pole, and different ways of locating the same resonance have given positions that differ by more than ten gauss. Narrow resonances behave universally over only a small fraction of their width.

**Resolved by.** The resonance parameters cited from a precise determination, such as radio-frequency spectroscopy of molecular binding energies combined with theoretical modelling; the field calibrated at the atoms, for example by radio-frequency or microwave spectroscopy of atomic transitions, with its uncertainty and stability; the resulting uncertainty in scattering length or in the interaction parameter propagated into the claim; the field width compared with the resonance width where a narrow resonance is used.

**Benchmark.** [2], [3]

## 7. Pair condensates detected after a magnetic field ramp

**Question.** When fermion pair condensation is detected by sweeping the field to convert pairs into molecules before imaging, does the paper show that the sweep is fast enough to preserve the pairs' momentum distribution and slow enough to convert them, and that the condensate it reports existed before the sweep?

**Why it matters.** The method relies on a window of sweep rates, and the many-body timescales that set this window are uncertain. Whether a condensate measured after the sweep reflects the state before it cannot be settled by theory alone and needs experimental tests. Condensate fractions from bimodal fits to molecular clouds also depend on the fit form.

**Resolved by.** The sweep rate and the timescales it is compared with stated; the measured condensate fraction shown to be independent of sweep rate and of the time spent near resonance over a stated range; conversion efficiency reported; the fit form for the molecular profile given and its effect on the fraction assessed.

**Benchmark.** [2]

## 8. Claims of superfluidity

**Question.** Does a claim of superfluidity rest on a property specific to superfluid flow, such as quantised vortices, rather than only on a bimodal profile, hydrodynamic expansion, collective modes, spectroscopic pairing or sharp peaks in the momentum distribution of atoms released from an optical lattice?

**Why it matters.** Hydrodynamic excitations and anisotropic expansion occur in collisional normal gases as well as in superfluids, and radio-frequency spectra of pairs can look the same in the superfluid and normal states. An ideal Bose gas in an optical lattice just above the critical temperature already shows sharp interference peaks, so peak sharpness judged by eye is not a test of superfluidity.

**Resolved by.** A signature specific to superfluid flow, such as a vortex lattice under rotation; for lattice gases, a quantitative coherence measure such as the visibility of interference peaks compared with a non-reciprocal-lattice reference, together with an estimate of the temperature in the lattice.

**Benchmark.** [2], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | W. Ketterle, D. S. Durfee and D. M. Stamper-Kurn, Making, probing and understanding Bose-Einstein condensates, contribution to the proceedings of the 1998 Enrico Fermi summer school on Bose-Einstein condensation, Varenna (1999); read as arXiv:cond-mat/9904034 | doi:10.48550/arXiv.cond-mat/9904034 | full text | Sec. 3.1: saturation modifies near-resonant absorption. Sec. 3.5.3: atoms pumped to a cycling transition for probing. Sec. 3.2: resonant optical density of trapped condensates far too high to image; off-resonant clouds refract light like a lens and bias densities. Sec. 4.1 and 4.2: scaling of thermal and Thomas-Fermi clouds in expansion; asymptotic aspect ratio not reached at typical times. Sec. 4.5: number from the cross-section, which depends on probe and atomic polarisation; temperature from the outer wings, with errors of about 20% if the fit comes too close to the condensate; condensate number depends strongly on the assumed shape; atom number at the critical temperature as a systematic check. Sec. 4.7: anisotropic expansion as the obvious signature; in-situ aspect ratios equal in the Thomas-Fermi regime; collisions can make thermal expansion anisotropic. Sec. 5: dense core appearing as the final evaporation frequency is lowered. Sec. 6.3: trap frequencies from centre-of-mass oscillations |
| 2 | W. Ketterle and M. W. Zwierlein, Making, probing and understanding ultracold Fermi gases, in Ultracold Fermi Gases, Proceedings of the International School of Physics Enrico Fermi, Course CLXIV, Varenna 2006 (IOS Press, 2008); read as arXiv:0801.2500 | doi:10.48550/arXiv.0801.2500 | full text | Secs. 1.2 and 1.3.3: quantised vortices as the strongest evidence of superfluidity; hydrodynamic excitations can reflect classical or superfluid hydrodynamics; the RF spectrum does not distinguish superfluid and normal states. Sec. 2.4.3: resonance positions from different methods differ by more than ten gauss, with molecular RF spectroscopy the most precise. Sec. 2.4.5: rapid ramp works in a window of sweep rates; survival of a pre-existing condensate must be tested experimentally. Sec. 3.2: collisional and superfluid hydrodynamic expansion; aspect-ratio inversion shows strong interactions, not condensation. Sec. 3.3: polylogarithm fits; at low T only the wings beyond the Fermi radius carry temperature information, so signal-to-noise there limits thermometry, and imaging effects can mimic a low T/T_F; ideal-gas fits to resonant clouds give an empirical temperature, and smooth-looking clouds can be superfluid; bimodal fits to molecular clouds are model dependent; alternative thermometers for unitary gases |
| 3 | C. Chin, R. Grimm, P. Julienne and E. Tiesinga, Feshbach resonances in ultracold gases, Rev. Mod. Phys. 82, 1225–1286 (2010); read as arXiv:0812.1496 | doi:10.1103/RevModPhys.82.1225 | full text | Sec. I.2 and II.1.3: the scattering length diverges at the resonance position, with width and background scattering length as parameters. Sec. II.2.2: narrow resonances are universal over only a small fraction of their width. Sec. III.1.2 and III.2.1: losses are the usual signature, and a loss feature was first seen about 150 G below the true pole of a broad resonance. Sec. III.1.5: binding energies measured by RF spectroscopy and combined with theoretical modelling fix position and width |
| 4 | G. Reinaudi, T. Lahaye, Z. Wang and D. Guéry-Odelin, Strong saturation absorption imaging of dense clouds of ultracold atoms, Opt. Lett. 32, 3143–3145 (2007); read as arXiv:0707.2930 | doi:10.1364/OL.32.003143 | full text | Eqs. 1 to 3 and following paragraphs: optical depth with saturation needs a correction factor to the saturation intensity, set by probe polarisation, excited-state structure and sublevel populations, and hard to predict because of window birefringence and stray fields. Calibration paragraphs and Fig. 1: factor chosen so the peak optical depth is independent of probe intensity. Introduction and Fig. 2: low-intensity imaging fails above an optical depth of about 3 to 4 |
| 5 | K. Hueck, N. Luick, L. Sobirey, J. Siegl, T. Lompe, H. Moritz, L. W. Clark and C. Chin, Calibrating high intensity absorption imaging of ultracold atoms, Opt. Express 25, 8670–8679 (2017); read as arXiv:1702.01943 | doi:10.1364/OE.25.008670 | full text | Sec. 2: at high intensity the column density depends on the absolute intensity in units of the effective saturation intensity. Sec. 4.2: calibration from the momentum the probe transfers to the atoms. Sec. 4.3: finding resonance by maximising apparent atom number is affected by lensing. Sec. 4.4: recoil Doppler shift of light atoms during the pulse. Sec. 4.6 and 4.7: polarisation purity checked; calibrated atom number independent of intensity |
| 6 | J. Szczepkowski, R. Gartman, M. Witkowski, Ł. Tracewski, M. Zawada and W. Gawlik, Analysis and calibration of absorptive images of Bose–Einstein condensate at nonzero temperatures, Rev. Sci. Instrum. 80, 053103 (2009); read as arXiv:0811.4034 | doi:10.1063/1.3125051 | full text | Sec. I and II.1: a Gaussian plus Thomas-Fermi fit biases results; Bose enhancement and interactions distort the overlap region; the excluded central region is somewhat arbitrary. Sec. II.2: excluded region calibrated against the temperature dependence of the condensate fraction. Sec. III and IV: simple sum fits give a notably low temperature and deviate from theory |
| 7 | F. Gerbier, J. H. Thywissen, S. Richard, M. Hugbart, P. Bouyer and A. Aspect, Experimental study of the thermodynamics of an interacting trapped Bose-Einstein condensed gas, Phys. Rev. A 70, 013607 (2004); read as preprint arXiv:cond-mat/0401585, which carries a different title | doi:10.1103/PhysRevA.70.013607 | full text | Sec. II.2 and II.3: temperature from the thermal wings with the centre excluded; the axial value depends on the excluded region; the standard fit fails at high condensed fractions, and Bragg separation of the components is used instead. Sec. III: condensed fraction below the ideal-gas curve, better described by a Hartree-Fock model. Sec. V.1: estimated temperature errors of about 10 to 20% from hydrodynamic and mean-field effects in expansion; measured aspect ratios show expansion not fully ballistic. Appendix A.3: interactions lower the critical temperature |
| 8 | R. B. Diener, Q. Zhou, H. Zhai and T.-L. Ho, Criterion for bosonic superfluidity in an optical lattice, Phys. Rev. Lett. 98, 180404 (2007); read as arXiv:cond-mat/0609685 | doi:10.1103/PhysRevLett.98.180404 | full text | Introduction and Sec. A with Fig. 1: an ideal Bose gas in a lattice at 1.1 times the critical temperature gives visibly sharp momentum peaks, so narrow peaks alone do not prove condensation. Sec. C: visibility against a non-reciprocal-lattice reference as a quantitative criterion. Closing paragraph after Sec. E: calls for ways to determine the temperature of lattice gases |
