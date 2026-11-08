---
id: T-QUANTUM-GASES
name: Bose-Einstein condensates and degenerate Fermi gases
type: technique
field: physics/amo
applies_when: the paper reports a Bose-Einstein condensate, a degenerate Fermi gas or a pair condensate of ultracold atoms, or bases a claim about condensate fraction, temperature, degeneracy, atom number, scattering length or superfluidity on absorption or time-of-flight images
version: "0.1"
---

# Bose-Einstein condensates and degenerate Fermi gases

## 1. Evidence of condensation

**Question.** Does the claim of condensation rest on more than one signature, such as a bimodal density profile, an aspect ratio after expansion that differs from that of the thermal cloud, and a dense component that appears at a threshold and grows as cooling continues, and is that threshold compared with the critical temperature expected from the atom number and trap frequencies?

**Why it matters.** Each signature has ordinary look-alikes. Collisions in a dense thermal cloud can make its expansion anisotropic, and a strongly interacting normal gas inverts its aspect ratio during expansion, so aspect-ratio inversion alone shows strong interactions rather than condensation. In the Thomas-Fermi regime the condensate and thermal cloud have the same aspect ratio in the trap, so in-situ shape alone does not reveal the onset.

**Resolved by.** A series of images or profiles across the threshold showing the dense component appearing and growing while the thermal wings shrink; the aspect ratio after expansion shown together with the bimodal profile; the atom number at the observed onset compared with the ideal-gas critical number for the measured trap frequencies, with interaction shifts of the critical temperature taken into account.

**Benchmark.** [1], [2], [4]

## 2. Condensate fraction and temperature from bimodal fits

**Question.** Which functions were fitted to the thermal and condensed parts of the profile, which region was excluded from the thermal fit and how was it chosen, and does the paper show that the resulting condensate fraction and temperature do not depend on these choices?

**Why it matters.** A Gaussian thermal component ignores Bose enhancement near the critical temperature, and fitting the thermal part too close to the condensate can bias the temperature by about 20 per cent. The condensate number depends strongly on the assumed bimodal shape, and the size of the excluded region is often chosen by hand. Interactions between the condensate and the thermal cloud distort the overlap region and lower the condensate fraction below the ideal-gas curve.

**Resolved by.** The fit functions stated, with a Bose-enhanced thermal component near the transition; the excluded region given and the results shown to be stable as it is varied; temperature taken from the outer wings; a residual plot or fitted profile overlaid on the data; condensate fraction against reduced temperature compared with an interacting model, not only the ideal-gas curve; a separate method, such as spatially separating the two components, where condensed fractions are high.

**Benchmark.** [1], [3], [4]

## 3. Time-of-flight mapping and trap parameters

**Question.** Which expansion model converts the measured sizes after time of flight into temperature, chemical potential or momentum, are the trap frequencies and imaging magnification measured and reported, and does the paper show that the expansion is ballistic, or model it if it is not?

**Why it matters.** The standard scaling of a thermal cloud's width assumes collisionless expansion from a harmonic trap with known frequencies, and a condensate's mean-field energy changes how it expands. Collisions soon after release, hydrodynamic flow in strongly interacting gases and mean-field repulsion all break the ballistic assumption and can bias the inferred temperature by an estimated 10 to 20 per cent. Typical expansion times may not reach the asymptotic aspect ratio of a condensate.

**Resolved by.** Trap frequencies measured, for example from centre-of-mass or breathing oscillations, with their uncertainty; magnification and pixel size calibrated; the expansion time and model given; for interacting or dense clouds, evidence that the expansion is ballistic, such as sizes measured at several expansion times or temperatures from different axes that agree, or else a hydrodynamic or interacting expansion model.

**Benchmark.** [1], [2], [4]

## 4. Degeneracy of Fermi gases

**Question.** How was T/T_F determined: from which fit function, over which region of the profile, with which atom number and trap frequencies entering T_F, and is the method valid for the interaction regime of the sample?

**Why it matters.** At low T/T_F the profile of a Fermi gas changes only in its wings beyond the Fermi radius, so the fitted temperature is limited by the signal-to-noise ratio there, and imaging effects can make a cloud look colder than it is. T_F itself depends on the atom number and trap frequencies, which carry their own calibration errors. Fitting an ideal Fermi profile to a strongly interacting cloud gives only an empirical temperature, and such clouds can be superfluid while their profiles look smooth.

**Resolved by.** The fit function and the fugacity or T/T_F it returns, with the uncertainty from atom number and trap frequencies included in T_F; full two-dimensional fits or fits to the wings with their signal-to-noise stated, and imaging resolution shown not to distort the wings; for strongly interacting gases, a thermometer suited to that regime, such as the ideal-gas wings of an imbalanced mixture or an entropy determined after an adiabatic sweep to a weakly interacting regime, rather than an ideal-gas fit labelled as a temperature.

**Benchmark.** [2]

## 5. Pair condensates detected after a magnetic field ramp

**Question.** When fermion pair condensation is detected by sweeping the field to convert pairs into molecules before imaging, does the paper show that the sweep is fast enough to preserve the pairs' momentum distribution and slow enough to convert them, and that the condensate it reports existed before the sweep?

**Why it matters.** The method relies on a window of sweep rates, and the many-body timescales that set this window are uncertain. Whether a condensate measured after the sweep reflects the state before it cannot be settled by theory alone and needs experimental tests. Condensate fractions from bimodal fits to molecular clouds also depend on the fit form.

**Resolved by.** The sweep rate and the timescales it is compared with stated; the measured condensate fraction shown to be independent of sweep rate and of the time spent near resonance over a stated range; conversion efficiency reported; the fit form for the molecular profile given and its effect on the fraction assessed.

**Benchmark.** [2]

## 6. Claims of superfluidity

**Question.** Does a claim of superfluidity rest on a property specific to superfluid flow, such as quantised vortices, rather than only on a bimodal profile, hydrodynamic expansion, collective modes, spectroscopic pairing or sharp peaks in the momentum distribution of atoms released from an optical lattice?

**Why it matters.** Hydrodynamic excitations and anisotropic expansion occur in collisional normal gases as well as in superfluids, and radio-frequency spectra of pairs can look the same in the superfluid and normal states. An ideal Bose gas in an optical lattice just above the critical temperature already shows sharp interference peaks, so peak sharpness judged by eye is not a test of superfluidity.

**Resolved by.** A signature specific to superfluid flow, such as a vortex lattice under rotation; for lattice gases, a quantitative coherence measure such as the visibility of interference peaks compared with a non-reciprocal-lattice reference, together with an estimate of the temperature in the lattice.

**Benchmark.** [2], [5]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | W. Ketterle et al., Making, probing and understanding Bose-Einstein condensates, contribution to the proceedings of the 1998 Enrico Fermi summer school on Bose-Einstein condensation, Varenna (1999); read as arXiv:cond-mat/9904034 | doi:10.48550/arXiv.cond-mat/9904034 |
| 2 | W. Ketterle and M. W. Zwierlein, Making, probing and understanding ultracold Fermi gases, in Ultracold Fermi Gases, Proceedings of the International School of Physics Enrico Fermi, Course CLXIV, Varenna 2006 (IOS Press, 2008); read as arXiv:0801.2500 | doi:10.48550/arXiv.0801.2500 |
| 3 | J. Szczepkowski et al., Ł. Tracewski, M. Zawada and W. Gawlik, Analysis and calibration of absorptive images of Bose–Einstein condensate at nonzero temperatures, Rev. Sci. Instrum. 80, 053103 (2009); read as arXiv:0811.4034 | doi:10.1063/1.3125051 |
| 4 | F. Gerbier et al., Experimental study of the thermodynamics of an interacting trapped Bose-Einstein condensed gas, Phys. Rev. A 70, 013607 (2004); read as preprint arXiv:cond-mat/0401585, which carries a different title | doi:10.1103/PhysRevA.70.013607 |
| 5 | R. B. Diener et al., Criterion for bosonic superfluidity in an optical lattice, Phys. Rev. Lett. 98, 180404 (2007); read as arXiv:cond-mat/0609685 | doi:10.1103/PhysRevLett.98.180404 |
