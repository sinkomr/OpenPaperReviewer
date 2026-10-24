---
id: T-FESHBACH-RESONANCES
name: Collisions and Feshbach resonances
type: technique
field: physics/amo
applies_when: the paper locates or characterises a Feshbach resonance in ultracold atoms, reports a scattering length, a two- or three-body loss rate coefficient or an Efimov feature, or bases a claim on atom-loss spectroscopy or on interactions tuned by a magnetic field
version: "0.1"
---

# Collisions and Feshbach resonances

Collision measurements in ultracold gases are used to claim the position and width of magnetically tunable Feshbach resonances, the scattering length a as a function of magnetic field B, and the rate coefficients of two-body and three-body inelastic loss (L2 and L3), including features attributed to few-body physics such as Efimov states. Most of these rest on the number of atoms remaining after a hold time at a field that must itself be calibrated.

## 1. Magnetic field at the atoms

**Question.** How was the field at the position of the atoms calibrated, for example by radio-frequency (RF) or microwave spectroscopy of an atomic transition converted to field with the Breit-Rabi formula, how often was the calibration repeated, and how do the drift, noise and variation of the field across the cloud compare with the width of the features reported?

**Why it matters.** Resonance positions and scattering lengths are only as good as the field scale, and narrow resonances call for field resolution at the milligauss level. Daily drift, field curvature along the cloud and settling after a field ramp each add to the uncertainty and can broaden or shift a narrow feature.

**Resolved by.** A calibration made in situ on the atoms with a stated transition and conversion; the residual uncertainty broken into drift, spatial variation and calibration error; settling times after ramps stated; the field uncertainty compared with the resonance or feature width; field values taken in random order or with repeated calibrations so that drift does not mimic structure.

**Benchmark.** [1], [2], [3]

## 2. Loss maximum and resonance pole

**Question.** When a resonance position is quoted from atom-loss spectroscopy, does the paper say whether it is the field of maximum loss or the pole where the scattering length diverges, and how is the difference between the two estimated?

**Why it matters.** Atom loss is the most common signature of a resonance, but the loss maximum need not coincide with the pole. For broad resonances the loss feature can lie far from the pole, and for narrow ones the thermal spread of collision energies shifts, broadens and skews the loss line, so the maximum moves with temperature. Later determinations of a resonance position have differed from earlier ones by more than the earlier quoted uncertainty.

**Resolved by.** The quantity reported named explicitly; for narrow resonances, loss spectra at several temperatures with the position extrapolated to zero temperature or modelled by thermal averaging; where the pole matters, a determination from binding energies of weakly bound molecules combined with a coupled-channels model; the systematic offset between loss maximum and pole included in the uncertainty.

**Benchmark.** [1], [2], [3]

## 3. Width and character of the resonance

**Question.** Does the paper distinguish the width of the observed loss feature from the resonance width that enters the scattering length (the distance between pole and zero crossing), and does it say whether the resonance is broad or narrow in the sense that sets its universal range?

**Why it matters.** The width of a loss feature reflects temperature, field noise, density and hold time as well as the resonance itself, so a fitted Gaussian or Lorentzian width is not the resonance width. Whether a resonance is dominated by the entrance channel or the closed channel is set by a dimensionless strength parameter, not by its width in gauss alone, and a narrow resonance behaves universally over only a small fraction of its width.

**Resolved by.** The fitted line shape and the meaning of each fitted width stated; the resonance width obtained from a zero crossing, molecular binding energies or a coupled-channels model, not from the loss width; the resonance strength parameter given or cited when claims depend on universal behaviour; the thermal and field contributions to the observed width estimated.

**Benchmark.** [1], [3]

## 4. Scattering length computed from the field

**Question.** When a scattering length is computed from the field, which formula and which resonance parameters (position, width, background scattering length) are used and from what source, and is the field range within the range where that formula holds?

**Why it matters.** The simple dispersive formula holds for a resonance without inelastic two-body channels, and a narrow, closed-channel-dominated resonance follows universal behaviour over only a small part of its width; outside these conditions a coupled-channels model is needed. Near the pole the scattering length changes by a large factor for a small error in position, so an outdated resonance position can be the largest error in a derived quantity.

**Resolved by.** The model and parameters cited from a precise determination, preferably a coupled-channels fit to bound-state and scattering data; the uncertainty in position and width propagated into the scattering length; for fields near the pole or near another resonance, a statement of why the model applies there; the effect of using more recent resonance parameters checked where they exist.

**Benchmark.** [1], [2]

## 5. Scattering length measured from collisions or interaction energy

**Question.** When a scattering length is measured directly, from thermalisation or cross-dimensional relaxation rates, cloud expansion or mean-field shifts, does the paper show that the measurement is in the regime its analysis assumes, and how is the sign of the scattering length determined?

**Why it matters.** The elastic cross section depends on the square of the scattering length, so rate measurements alone do not fix its sign. Analyses that use the zero-energy cross section assume that the collision wavenumber times the scattering length is small; when this fails the cross section reaches the unitarity limit, and in dense samples the gas becomes hydrodynamic, both of which wash out the dependence on scattering length.

**Resolved by.** The product of scattering length and thermal wavenumber stated for the data used; collision rates compared with trap frequencies to rule out the hydrodynamic regime, or the analysis adapted to it; the sign fixed by an independent observable such as a mean-field shift, a zero crossing or the existence of a weakly bound molecular state; energy dependence of the cross section included where the scattering length is large.

**Benchmark.** [1], [4]

## 6. Identifying the loss process

**Question.** Does the paper show which process removes atoms (collisions with background gas, two-body inelastic collisions, three-body recombination or conversion into molecules) and how this was established from the data, not assumed?

**Why it matters.** One-, two- and three-body losses scale differently with density, and assigning a loss curve to the wrong order gives a meaningless rate coefficient. Two-body relaxation is energetically suppressed when the atoms are in the lowest internal state but not otherwise, and atoms converted into weakly bound molecules may simply be missed by atom imaging, so a drop in atom number can reflect molecule formation rather than loss from the trap.

**Resolved by.** Decay curves over a range of densities fitted with the one-, two- and three-body terms, with the dependence on density shown; the internal state stated and two-body decay channels ruled out where possible; a background lifetime measured away from resonance; for loss near resonance, a check for molecules, for example by dissociating them before imaging and recovering the missing atoms.

**Benchmark.** [1], [4], [6]

## 7. Extracting a three-body rate coefficient

**Question.** How was the density entering the three-body rate obtained, were heating and evaporation during the hold included in the fit, and does the quoted coefficient say whether it refers to a thermal or a condensed sample?

**Why it matters.** The three-body coefficient is inferred from the mean square density, which is computed from atom number, temperature and trap frequencies. Because it scales with the square of atom number and the sixth power of the mean trap frequency, modest errors in these can change it by a factor of two. Loss from the dense centre heats the remaining cloud, and residual evaporation removes further atoms, so a fit that holds temperature fixed can misattribute losses. Atoms in a condensate are less bunched than in a thermal gas, so at the same density three-body loss is six times smaller.

**Resolved by.** The density model and the measured trap frequencies stated; temperature measured during the decay and modelled with the atom number, or held constant by a stated method with the evaporation correction given; the systematic uncertainty from atom number and trap frequency calibration quoted separately from the fit uncertainty; the convention for the coefficient and the coherence of the sample stated so that values from different experiments can be compared.

**Benchmark.** [4], [5], [7]

## 8. Temperature, unitarity and few-body features

**Question.** For claims about the scaling of loss with scattering length or about features attributed to few-body states, does the paper compare the scattering length with the thermal wavelength or inverse thermal wavenumber, and restrict the claimed behaviour to the range where finite-temperature effects are small?

**Why it matters.** At zero temperature the three-body rate grows as the fourth power of the scattering length, modulated by log-periodic Efimov structure. At finite temperature it saturates once the scattering length becomes comparable with the thermal wavelength and is then set by temperature, and thermal averaging smears and shifts loss features. A fit that runs into this region can mistake saturation for a change in scaling, or move an apparent feature.

**Resolved by.** The temperature of each data set and the corresponding thermal length given alongside the scattering-length axis; the range used for scaling fits or feature positions limited to scattering lengths well below the thermal length, or a finite-temperature model used; data at more than one temperature showing that the claimed feature does not move with temperature; a feature attributed to a few-body state compared with the loss expected from thermal saturation alone.

**Benchmark.** [4], [5], [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | C. Chin, R. Grimm, P. Julienne and E. Tiesinga, Feshbach resonances in ultracold gases, Rev. Mod. Phys. 82, 1225–1286 (2010); read as arXiv:0812.1496 | doi:10.1103/RevModPhys.82.1225 | full text | Sec. I.2 and footnote 2: dispersive formula for a(B), zero crossing at the pole plus the width, valid for resonances without inelastic two-body channels; narrow resonances universal over a very small fraction of their width. Sec. II.1.2: elastic cross section depends on a squared and reaches a unitarity limit. Sec. II.2.2: the strength parameter s_res, not the width alone, separates entrance- and closed-channel dominated resonances. Sec. II.2.3: coupled-channels models fitted to bound-state and scattering data. Sec. III.1.1: narrow resonances need milligauss field resolution. Sec. III.1.2: loss is the most common signature, density-dependent two- and three-body loss terms. Sec. III.1.3: thermalisation features washed out by hydrodynamic or unitarity limits. Secs. III.1.5 and III.2.1: binding-energy spectroscopy with theory fixes position and width; a loss feature about 150 G below the pole of a broad resonance |
| 2 | G. Zürn, T. Lompe, A. N. Wenz, S. Jochim, P. S. Julienne and J. M. Hutson, Precise characterization of 6Li Feshbach resonances using trap-sideband-resolved RF spectroscopy of weakly bound molecules, Phys. Rev. Lett. 110, 135301 (2013); read as arXiv:1211.1512 | doi:10.1103/PhysRevLett.110.135301 | full text | Main text, measurement procedure: field settling after ramps to an uncertainty of about 11 mG. Supplemental Sec. I.1: field calibrated by an RF atomic transition and the Breit-Rabi formula. Table 2 and discussion: pole positions from binding energies and a coupled-channels fit differ from an earlier determination by more than its quoted uncertainty, and that earlier uncertainty was the largest error in a derived many-body quantity |
| 3 | M. Gerken, B. Tran, S. Häfner, E. Tiemann, B. Zhu and M. Weidemüller, Observation of dipolar splittings in high-resolution atom-loss spectroscopy of 6Li p-wave Feshbach resonances, Phys. Rev. A 100, 050701 (2019); read as arXiv:1909.09831 | doi:10.1103/PhysRevA.100.050701 | full text | Sec. II: field calibrated by RF spectroscopy with the Breit-Rabi formula, uncertainty from daily drift, field curvature along the cloud and calibration, fields taken in random order. Sec. III: thermal averaging makes the loss line asymmetric, shifted and broadened; the loss maximum moves with temperature; positions extrapolated linearly to zero temperature; observed widths exceed the thermal estimate; saturation hides structure at higher temperature |
| 4 | T. Weber, J. Herbig, M. Mark, H.-C. Nägerl and R. Grimm, Three-body recombination at large scattering lengths in an ultracold atomic gas, Phys. Rev. Lett. 91, 123201 (2003); read as arXiv:physics/0304052 | doi:10.1103/PhysRevLett.91.123201 | full text | Rate equations: atom number fitted with a one-body background term and a three-body term, two-body loss excluded by using the lowest internal state; coupled equation for temperature including anti-evaporation and recombination heating, fitted together. Discussion of Fig. 3: density inferred from atom number, temperature and trap frequency, with L3 scaling as atom number squared times trap frequency to the sixth, giving a systematic error up to a factor of two. a^4 law requires the wavenumber times a to be small, with a unitarity cutoff seen at the higher temperature |
| 5 | B. S. Rem, A. T. Grier, I. Ferrier-Barbut, U. Eismann, T. Langen, N. Navon, L. Khaykovich, F. Werner, D. S. Petrov, F. Chevy and C. Salomon, Lifetime of the Bose gas with resonant interactions, Phys. Rev. Lett. 110, 163202 (2013); read as arXiv:1212.5274 | doi:10.1103/PhysRevLett.110.163202 | full text | Introduction and Fig. 3 discussion: three-body loss follows a^4 with log-periodic modulation at zero temperature but saturates once a is comparable with the thermal wavelength, scaling as 1/T^2 at unitarity; thermal smearing moves an Efimov loss maximum. Text around Eqs. 2 and 3: mean square density from a Gaussian profile, temperature held by trap depth, evaporation correction of 30 to 50% applied to L3 |
| 6 | T. Köhler, K. Góral and P. S. Julienne, Production of cold molecules via magnetically tunable Feshbach resonances, Rev. Mod. Phys. 78, 1311–1361 (2006); read as arXiv:cond-mat/0601420 | doi:10.1103/RevModPhys.78.1311 | full text | Sec. I and Fig. 2 caption: field sweeps across a resonance convert atoms into Feshbach molecules, which are missing from atom counts; detection by dissociation, RF photodissociation or loss and recovery of atoms |
| 7 | D. M. Stamper-Kurn and J. H. Thywissen, Experimental methods of ultracold atomic physics, arXiv:1111.6196 (2011), chapter for Ultracold Bosonic and Fermionic Gases (Elsevier) | doi:10.48550/arXiv.1111.6196 | full text | Sec. 5.2: three-body loss is slower in a condensate because the zero-range third-order correlation function is six times smaller than in a thermal gas; sharp increases and decreases of three-body loss near a resonance are attributed to Efimov trimer states |
