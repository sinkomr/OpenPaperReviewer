---
id: T-INELASTIC-X-RAY
name: Resonant and inelastic X-ray scattering
type: technique
field: physics/condensed-matter
applies_when: the paper reports resonant inelastic X-ray scattering (RIXS), non-resonant inelastic X-ray scattering (IXS) or resonant elastic X-ray scattering, or bases a claim about magnons, paramagnons, orbital or charge excitations, phonons, electron-phonon coupling or charge order on them
version: "0.1"
---

# Resonant and inelastic X-ray scattering

## 1. Energy resolution, zero of energy loss and the elastic line

**Question.** Does the paper state the measured energy resolution and its line shape, say how the elastic line and the zero of energy loss were determined, and show that the features it interprets are separated from the elastic line by more than the resolution and its tails?

**Why it matters.** Where the elastic line is strong, its tails rather than the resolution width decide whether a low-energy feature can be seen, and the roughly Lorentzian resolution of meV-resolution IXS spectrometers makes the intensity at one energy respond to features far away. Low-energy phonons and other modes below the resolution merge into the elastic line, and when the resolution is comparable with the width of an excitation, the fitted parameters depend on how the elastic line and background are modelled.

**Resolved by.** The combined resolution measured on an elastic reference under the same conditions, with its line shape used in the fits; the zero of energy loss and how it was found stated; the elastic line fitted with stated constraints and shown not to account for the claimed feature; no excitation claimed at an energy comparable with the resolution without a resolution-convolved fit that supports it.

**Benchmark.** [1], [5], [6]

## 2. Incident-energy dependence

**Question.** Were spectra measured at more than one incident energy across the edge, and does the paper show whether each interpreted feature stays at constant energy loss (Raman-like) or at constant emitted energy (fluorescence-like)?

**Why it matters.** Features at constant energy loss come from excitations left in the sample, while features at constant emitted energy come from fluorescence and shift one for one with the incident energy; a spectrum at a single incident energy cannot tell them apart. The intensity and even the presence of a feature depend on which intermediate state is reached, and approximate cross-sections that ignore the intermediate state do not reproduce how spectra change with incident energy.

**Resolved by.** An incident-energy map or spectra at several energies through the resonance, with each feature classified as Raman-like or fluorescence-like; the incident energy for each data set stated relative to the absorption spectrum of the same sample; where intensities are compared with theory, a calculation that includes the intermediate state at the energies used.

**Benchmark.** [1], [2], [4]

## 3. Assignment of spectral features

**Question.** On what evidence is each feature assigned to a magnon, paramagnon, multimagnon, orbital (dd) excitation, charge excitation or phonon: the selection rules of the edge used, the dependence on incident and scattered polarisation, the momentum dependence, a calculated cross-section, or the energy scale alone?

**Why it matters.** Which excitations appear depends on the edge: single spin flips are allowed at transition-metal L and M edges but not at K edges, where only spin-conserving excitations such as bimagnons appear. Phonon, magnetic and charge features can overlap in energy, especially near zero momentum, and without analysis of the scattered polarisation the spin and charge channels are mixed. A polarisation dependence like that of a known magnon is an empirical argument for a magnetic origin, not a proof. In non-resonant IXS the phonon intensity depends on the eigenvector projected on the total momentum transfer, so which branch is seen depends on where in reciprocal space the spectrum was taken.

**Resolved by.** The edge and its selection rules stated for each assignment; incident polarisation varied and, where possible, scattered polarisation analysed, with the expected behaviour of each candidate excitation shown; the momentum ranges where features overlap identified and excluded or treated separately; a calculated RIXS cross-section, or for IXS a lattice-dynamics calculation of intensities, compared with the measured spectra at the momenta used.

**Benchmark.** [1], [2], [3], [4], [6], [7]

## 4. Self-absorption, geometry and normalisation

**Question.** When intensities from different momenta, geometries, polarisations or samples are compared, does the paper say how self-absorption was corrected and how the spectra were normalised?

**Why it matters.** Changing the momentum transfer in RIXS usually means rotating the sample, which changes the incidence and exit angles, the path of the X-rays in the sample and the illuminated volume. Absorption of the incident and scattered beams near the resonance depends strongly on this geometry, so an uncorrected change of intensity with momentum may reflect geometry rather than the excitation. The correction depends on the absorption spectrum near the edge.

**Resolved by.** Incidence and exit angles given for each momentum; a self-absorption correction stated with the absorption coefficients used, measured on the same sample, or a geometry chosen to reduce it with an estimate of what remains; the normalisation of spectra stated and kept the same for all spectra compared; intensity trends shown to survive the correction.

**Benchmark.** [1], [7]

## 5. Momentum coverage and projection

**Question.** Which part of the Brillouin zone could be reached at the edge and geometry used, how were the in-plane and out-of-plane components of the momentum transfer handled, and does the claim depend on momenta that were not measured?

**Why it matters.** The momentum transfer is fixed by the photon energy and the scattering angle, so at soft X-ray L and M edges only part of the first Brillouin zone is reachable and some characteristic wavevectors cannot be measured at all. Changing the in-plane momentum by rotating the sample also changes the out-of-plane component, which is often assumed not to matter. Treating data along one accessible direction as representative of the whole zone, for example in a material without long-range magnetic order, is an assumption that needs support.

**Resolved by.** The edge, scattering angle and accessible momentum range stated; momenta given with both in-plane and out-of-plane components, or evidence that out-of-plane dispersion is negligible for the claim; conclusions confined to the momenta measured, or extrapolations stated as such; where wider coverage matters, data at a harder edge or from another probe.

**Benchmark.** [1], [2], [3], [8]

## 6. From spectral weight to response functions and coupling constants

**Question.** When the paper compares RIXS intensities with a dynamical structure factor, with neutron data or with theory, or derives a coupling constant from them, does it state the approximation that links the RIXS cross-section to that quantity and test whether it holds?

**Why it matters.** Whether and when RIXS intensity is proportional to a spin or charge dynamical structure factor is an open question in general; in model calculations the cross-polarised channel only approximates the shape of the spin structure factor, its weight does not match, and the parallel channel does not reduce to a simple charge response. Electron-phonon coupling constants from RIXS rest on a model that assumes a localised intermediate state and local phonons, and the ratio of overtone to fundamental intensity is often impossible to measure in doped materials where features broaden.

**Resolved by.** The relation between RIXS intensity and the compared quantity stated with its assumptions; comparisons made on line shape where weights are not expected to match, or with a full cross-section calculation; for coupling constants, the model, the parameters taken from elsewhere (phonon energy, core-hole lifetime) and the method (overtone ratio or incident-energy detuning) stated, with uncertainties that include these inputs.

**Benchmark.** [1], [3], [4], [7]

## 7. Line-shape model for broad excitations

**Question.** For broad excitations such as paramagnons, which line-shape model, background and elastic-line treatment were used, were the parameters free or fixed, and does the conclusion survive a model that also allows overdamped behaviour?

**Why it matters.** Broad features sit on sloping backgrounds and the tails of higher-energy excitations, and the fitted energy and damping depend strongly on the background model, especially at coarse resolution. A damped-oscillator form that cannot describe overdamped motion pushes the fit away from that regime and gives error bars that are too small. The temperature factor relating intensity to the response function shifts the peak to higher energy, so a peak in the intensity is not the same as a propagating mode, and resolution tails do not obey detailed balance.

**Resolved by.** The fit function, background form, elastic-line treatment and constraints stated; fits repeated with a general oscillator model that permits overdamping and with alternative backgrounds, with the spread reported; propagating-mode claims based on the response function after removing the temperature factor, not on the intensity peak alone; resolution convolved before any detailed-balance correction.

**Benchmark.** [3], [5], [6]

## 8. Resonant elastic scattering for charge order

**Question.** For a claim of charge order from a resonant superlattice peak, does the paper show the energy dependence of the peak across the edge, say how the fluorescence background was removed, and separate a modulation of valence from a lattice distortion or a structural superlattice?

**Why it matters.** A superlattice peak at a resonance can come from a modulation of valence, from a strain wave or lattice displacement that scatters at all energies, or from a shift of transition energies, and these give different line shapes across the edge. Energy-integrated soft X-ray scattering sits on a strong fluorescence background, and finite energy resolution means the peak measures order that is static only on a timescale set by that resolution. Peak widths give a correlation length only after the resolution is accounted for.

**Resolved by.** The peak intensity measured against incident energy and compared with the absorption spectrum and with model line shapes for valence, displacement and energy-shift contributions; polarisation dependence shown; background removed with the procedure stated, or a spectrometer used to reject fluorescence; a non-resonant measurement, or its absence, discussed for the lattice component; the energy resolution stated when the order is called static; correlation lengths derived with the resolution stated.

**Benchmark.** [2], [8], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | L. J. P. Ament et al., Resonant inelastic x-ray scattering studies of elementary excitations, Rev. Mod. Phys. 83, 705 (2011); read as preprint arXiv:1009.3630 | doi:10.1103/RevModPhys.83.705 |
| 2 | M. Mitrano et al., Exploring quantum materials with resonant inelastic x-ray scattering, Phys. Rev. X 14, 040501 (2024); read as preprint arXiv:2410.13062v1 | doi:10.1103/PhysRevX.14.040501 |
| 3 | M. P. M. Dean, Insights into the high temperature superconducting cuprates from resonant inelastic X-ray scattering, J. Magn. Magn. Mater. 376, 3 (2015); read as preprint arXiv:1402.5423 | doi:10.1016/j.jmmm.2014.03.057 |
| 4 | C. Jia et al., Using RIXS to uncover elementary charge and spin excitations, Phys. Rev. X 6, 021020 (2016); read as preprint arXiv:1510.05068 | doi:10.1103/PhysRevX.6.021020 |
| 5 | J. Lamsal and W. Montfrooij, Extracting paramagnon excitations from resonant inelastic x-ray scattering experiments, Phys. Rev. B 93, 214513 (2016); read as preprint arXiv:1603.08805, which carries a different title | doi:10.1103/PhysRevB.93.214513 |
| 6 | A. Q. R. Baron, Introduction to high-resolution inelastic x-ray scattering, arXiv:1504.01098v7 (2015, revised 2020), a revised version of the chapters on high-resolution inelastic X-ray scattering in Synchrotron Light Sources and Free-Electron Lasers (Springer) | doi:10.48550/arXiv.1504.01098 |
| 7 | L. Braicovich et al., Determining the electron-phonon coupling in superconducting cuprates by resonant inelastic x-ray scattering: methods and results on Nd1+xBa2−xCu3O7−δ, Phys. Rev. Res. 2, 023231 (2020) | doi:10.1103/PhysRevResearch.2.023231 |
| 8 | R. Comin and A. Damascelli, Resonant x-ray scattering studies of charge order in cuprates, Annu. Rev. Condens. Matter Phys. 7, 369 (2016); read as preprint arXiv:1509.03313 | doi:10.1146/annurev-conmatphys-031115-011401 |
| 9 | P. Abbamonte, Charge modulations versus strain waves in resonant x-ray scattering, Phys. Rev. B 74, 195113 (2006); read as preprint arXiv:cond-mat/0608236 | doi:10.1103/PhysRevB.74.195113 |
