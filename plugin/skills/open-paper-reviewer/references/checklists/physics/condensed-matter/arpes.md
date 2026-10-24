---
id: T-ARPES
name: Angle-resolved photoemission spectroscopy
type: technique
field: physics/condensed-matter
applies_when: the paper reports angle-resolved photoemission data, or bases a claim about band dispersion, Fermi surface, energy gaps, surface or bulk states, orbital character or quasiparticle self-energy on them
version: "0.1"
---

# Angle-resolved photoemission spectroscopy

ARPES is used to claim band dispersions, Fermi surfaces, energy gaps, the surface, bulk or orbital character of states, and quasiparticle self-energies, from the kinetic energy and emission angle of photoelectrons. The measured intensity is the spectral function weighted by a matrix element and the Fermi function and broadened by resolution, and at ultraviolet photon energies it comes mostly from the top few atomic layers.

## 1. Energy reference and resolution

**Question.** How was the Fermi level determined, what are the stated energy and angular resolutions, and how do they compare with the size of the gap, splitting or shift that is claimed?

**Why it matters.** The measured Fermi-edge position varies between set-ups, from day to day and with photon energy, so a reference that is nominal or was taken at another time shifts the whole energy axis. When a gap or splitting is comparable to the resolution or to the uncertainty of the reference, noise and broadening can produce or hide it.

**Resolved by.** A Fermi edge measured on a metal in electrical contact with the sample under the same conditions, before and after the data; resolution obtained from a fit to that edge at the measurement temperature; and error bars on extracted quantities that combine counting statistics, resolution and energy stability.

**Benchmark.** [1], [2]

## 2. Surface or bulk origin

**Question.** For each band on which a conclusion rests, what shows whether it is a surface state or a bulk state, and whether the measured surface is representative of the bulk?

**Why it matters.** With ultraviolet photons most of the signal comes from the top few atomic layers. Reduced coordination, structural or chemical change at the surface, and coexisting surface and bulk states mean that spectra need not reflect the bulk electronic structure.

**Resolved by.** Photon-energy dependence showing whether the band disperses with out-of-plane momentum; structural and chemical characterization of the measured surface, for example low-energy electron diffraction and core-level spectra; and, where bulk properties are at issue, data at more bulk-sensitive photon energies.

**Benchmark.** [2], [3]

## 3. Out-of-plane momentum

**Question.** How was the out-of-plane momentum assigned (inner potential, photon-energy range), and is its intrinsic broadening taken into account when bulk bands, Fermi crossings or line widths are interpreted?

**Why it matters.** Out-of-plane momentum is not conserved at the surface and is reconstructed by assuming a free-electron final state with a fitted inner potential, an approximation that can fail, particularly at low photon energy. The short escape depth averages over a sizeable fraction of the Brillouin zone along that direction, which can shift peaks, leave intensity at the Fermi level away from true crossings, and add width that resembles a self-energy effect.

**Resolved by.** Photon-energy scans wide enough to show the periodicity along the out-of-plane direction, with the inner potential and the way it was fixed stated; an estimate of the out-of-plane broadening relative to the zone size; and conclusions about line widths or Fermi surfaces of three-dimensional bands that allow for it.

**Benchmark.** [1], [2], [4]

## 4. Matrix-element effects

**Question.** Where a claim rests on intensity (a band being absent, a change in spectral weight, orbital character, dichroism), has the feature been examined with different photon energies, polarizations, geometries or Brillouin zones?

**Why it matters.** The photoemission intensity is the spectral function multiplied by a matrix element that depends on photon energy, polarization and geometry and can suppress a band completely. Dichroism signals can arise from the experimental geometry or from final-state effects as well as from the initial state.

**Resolved by.** Photon energy, polarization and geometry stated for each data set; the same feature shown under more than one of these conditions; sample alignment to a mirror plane documented where selection rules or dichroism are used; and a symmetry analysis or calculation of the matrix element where intensities are interpreted quantitatively.

**Benchmark.** [1], [2], [3]

## 5. Charging and space charge

**Question.** Has it been shown that peak positions and widths do not change with photon flux?

**Why it matters.** A sample that cannot drain the photocurrent charges, which shifts and broadens the spectra. With pulsed or high-flux sources, Coulomb interaction among the emitted electrons does the same, by amounts that can reach the energy scale of the features studied and that can differ between the sample and the reference metal, so the Fermi-level reference itself becomes uncertain.

**Resolved by.** Spectra at more than one flux showing no shift or broadening, or a flux scan identifying the regime used; for pulsed sources, the repetition rate and flux used and the residual shift and broadening; and an account of how the energy reference was protected, for example an internal reference or flux monitoring.

**Benchmark.** [1], [2], [6]

## 6. Image enhancement

**Question.** If second-derivative, curvature or similarly filtered images are shown, are the unprocessed intensity maps and energy or momentum distribution curves also shown, and are quantitative values taken from fits to the unprocessed curves?

**Why it matters.** Derivative-based filters sharpen features for display but do not preserve line shapes or intensities. For asymmetric peaks the second-derivative maximum is displaced from the true peak, the Fermi cut-off can itself appear as a feature, and the curvature method adds free parameters, so band positions, gaps or kinks read from filtered images can differ from those in the data.

**Resolved by.** Raw maps and distribution curves next to any filtered image; the filter and its parameters stated; and dispersions, gaps and widths extracted by fitting the raw curves.

**Benchmark.** [1], [2], [5]

## 7. Gaps and self-energies from line shapes

**Question.** Which procedure was used to extract a gap, dispersion or self-energy (symmetrization, leading-edge position, model fit, energy or momentum distribution curve fitting, assumed bare band), and are its assumptions stated and tested?

**Why it matters.** Symmetrizing about the Fermi level imposes particle–hole symmetry, leading-edge shifts are sensitive to momentum misalignment, and for gaps near the resolution or spectra without sharp quasiparticle peaks, noise, resolution and scattering can mimic the closing of a gap. Energy and momentum distribution curve fits generally give different dispersions, and a self-energy depends on a bare band that is not known independently, on the assumed background and on assumptions about unoccupied states.

**Resolved by.** The method and its assumptions named; fits that include resolution, Fermi function and background, shown against raw curves corrected for detector non-linearity; a check that the conclusion survives reasonable changes of bare band, background or method; and uncertainties on the extracted values.

**Benchmark.** [1], [2], [3]

## 8. Surface ageing, reproducibility and reporting

**Question.** Are the surface preparation, vacuum, temperature and time since preparation given, was the surface checked for change during the measurement, and was the result reproduced on another cleave or sample?

**Why it matters.** Even in ultrahigh vacuum, residual gas covers a fresh surface within about a day, and adsorption, temperature cycling and beam exposure can shift and broaden peaks. A feature seen on one surface at one time may reflect the history of that surface.

**Resolved by.** Preparation method and vacuum conditions; spectra repeated at the start and end of long acquisitions; results from more than one sample or cleave; and the conditions needed to repeat the measurement reported with the data: energy resolution, photon energy and polarization, geometry and sample orientation, sample temperature and facility.

**Benchmark.** [1], [2]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | H. Zhang, T. Pincelli, C. Jozwiak, T. Kondo, R. Ernstorfer, T. Sato and S. Zhou, Angle-resolved photoemission spectroscopy, Nat. Rev. Methods Primers 2, 54 (2022); read as preprint arXiv:2207.06942 | doi:10.1038/s43586-022-00133-7 | full text | Preprint sections "Sample" (vary flux to test for charging), "Fermi energy calibration" (reference before and after), "Energy, momentum and time resolution", "Angle-to-momentum conversion" (inner potential is a fitted parameter), "Important band parameters and self-energy analysis" (bare velocity hard to determine), "Dipole matrix element effect" (band suppression; vary photon energy, polarization, zone), "Statistical analysis and errors", "Issues with reproducibility", "Repositories and data deposition" (distribution curves needed for gap claims), "Minimum reporting standards", "kz broadening" and "Space charge" |
| 2 | J. A. Sobota, Y. He and Z.-X. Shen, Angle-resolved photoemission studies of quantum materials, Rev. Mod. Phys. 93, 025006 (2021); read as preprint arXiv:2008.02378, which carries a different title | doi:10.1103/RevModPhys.93.025006 | full text | Sec. II, subsections on final states and out-of-plane momentum (photon-energy dependence separates surface from bulk states; free-electron final state can fail), on surface sensitivity and resolution (signal from the top few layers; out-of-plane broadening; space charge) and on matrix elements (dichroism caveats). Sec. III, subsections on data analysis (Fermi reference, detector non-linearity, gap extraction and symmetrization, unknown bare band, filtered images not quantitative) and on sample environment (monolayer coverage in about a day) |
| 3 | A. Damascelli, Probing the Electronic Structure of Complex Systems by ARPES, Phys. Scr. T109, 61–74 (2004); read as preprint arXiv:cond-mat/0307085, which carries a slightly different title | doi:10.1238/Physica.Topical.109a00061 | full text | Sec. V: the matrix element depends on photon energy and geometry and can suppress intensity completely; resolution and background must enter quantitative analysis. Sec. VI: surface sensitivity means spectra may not represent the bulk, and the surface should be characterized structurally and chemically |
| 4 | V. N. Strocov, Intrinsic accuracy in 3-dimensional photoemission band mapping, J. Electron Spectrosc. Relat. Phenom. 130, 65–78 (2003); read as preprint arXiv:cond-mat/0210404 | doi:10.1016/S0368-2048(03)00054-9 | full text | Secs. I and V: final-state damping gives an intrinsic out-of-plane broadening, so peaks are averages that can be shifted from the true dispersion. Sec. III, subsections on ghost peaks at the Fermi level and on line widths near it |
| 5 | P. Zhang, P. Richard, T. Qian, Y.-M. Xu, X. Dai and H. Ding, A precise method for visualizing dispersive features in image plots, Rev. Sci. Instrum. 82, 043712 (2011); read as preprint arXiv:1104.1524 | doi:10.1063/1.3585113 | full text | Secs. I and II with Fig. 1: second-derivative maxima are displaced from true peak positions for asymmetric line shapes, and the Fermi cut-off appears as a feature. Sec. IV: these methods serve visualization only, line-shape information is lost, and the curvature method has free parameters |
| 6 | X. J. Zhou, B. Wannberg, W. L. Yang, V. Brouet, Z. Sun, J. F. Douglas, D. Dessau, Z. Hussain and Z.-X. Shen, Space charge effect and mirror charge effect in photoemission spectroscopy, J. Electron Spectrosc. Relat. Phenom. 142, 27–38 (2005); read as preprint arXiv:cond-mat/0410006 | doi:10.1016/j.elspec.2004.08.004 | full text | Abstract and Sec. V: Coulomb effects shift and broaden spectra by about 10 meV at a third-generation synchrotron, scale with photon flux, and differ between sample and reference metal, which undermines the Fermi-level reference |
