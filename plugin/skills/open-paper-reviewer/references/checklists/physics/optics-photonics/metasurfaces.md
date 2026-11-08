---
id: T-METASURFACES
name: Metamaterials and metasurfaces
type: technique
field: physics/optics-photonics
applies_when: the paper reports a metamaterial or metasurface device such as a metalens, beam deflector or hologram, quotes its efficiency, bandwidth or field of view, or assigns an effective permittivity, permeability or refractive index, including a negative index, to a structured medium
version: "0.1"
---

# Metamaterials and metasurfaces

## 1. Definition of efficiency

**Question.** For each efficiency quoted, does the paper state what is counted in the numerator (the power in the focal spot inside what window, in one diffraction order, or in one polarisation) and in the denominator (the power incident on the device aperture, or the power the device transmits), and is the same definition used for simulated and measured values and for every comparison with other work?

**Why it matters.** Normalising to the transmitted power instead of the incident power leaves out reflection and absorption, so it gives a higher number for the same device. A focusing efficiency counted inside a window scaled to the spot width rises when the spot broadens, so it can improve while focusing gets worse, and published comparison tables often mix definitions and averaging conventions.

**Resolved by.** Each efficiency named as absolute (relative to incident power) or relative (relative to transmitted power), with its formula; the collection window given in absolute units or in multiples of the measured spot width; the incident power measured through the same aperture, for example with a reference lens of known transmission or with the device removed; transmission efficiency and a measure of focal quality, such as the Strehl ratio or the measured point-spread function, reported alongside; comparisons with other work made only between matching definitions.

**Benchmark.** [1], [2]

## 2. Simulation compared with measurement

**Question.** What exactly was simulated (a library of periodic unit cells assembled under a local periodic approximation, or a full-wave model of the whole device), with which dimensions and optical constants, and are simulated and measured results labelled as such and compared for the same quantity, definition and device?

**Why it matters.** Unit-cell libraries assume that each meta-atom behaves as it would in a periodic array of identical neighbours with a simple radiation pattern; this holds when the structure varies slowly and becomes less accurate near abrupt changes, at high numerical aperture (NA) and for large deflection angles. Fabricated dimensions differ from the design, and measured efficiencies can fall below simulated ones for that reason. A simulated value placed next to measured ones can make a device look better than the measurement shows.

**Resolved by.** A full-wave simulation of the whole device, or a stated check of the approximation against one; the measured feature sizes and the optical constants used, with their origin; simulated and measured values for the same quantity shown together, with any gap stated and its cause tested, for example by simulating the measured dimensions; simulated-only values marked as such wherever they appear in tables or comparisons.

**Benchmark.** [1], [2], [3], [4]

## 3. Angular response and field of view

**Question.** Is the device characterised over the range of incidence angles, and for deflectors the range of output angles, on which the claim rests, and is any field of view stated together with the criterion that defines it?

**Why it matters.** A phase profile designed for one angle of incidence focuses without aberration only at that angle, and a single local metasurface gives an aberrated image at other angles. The response of each meta-atom also changes with the incident and scattered angles, and the efficiency of designs based on a local phase gradient falls for large deflection angles, so performance measured at one angle does not carry over to others.

**Resolved by.** Efficiency, spot size or Strehl ratio, and point-spread functions measured at several angles across the claimed field of view, including its edge; the field-of-view criterion stated, such as a threshold on Strehl ratio or efficiency; for deflectors, efficiency against deflection angle together with the power in unwanted orders; the angular range covered by the unit-cell simulations stated.

**Benchmark.** [2], [4], [5]

## 4. Bandwidth and achromatic claims

**Question.** Over what wavelength range does the claimed behaviour hold, by what criterion (focal shift, efficiency, spot size or Strehl ratio), and how does the claimed bandwidth compare with published bounds for a device of the stated aperture, NA, thickness and field of view?

**Why it matters.** Achromatic focusing needs a range of group delays that grows with aperture and NA, and time-bandwidth bounds limit what a device of given thickness and index contrast can provide; a wider field of view lowers the bound further. A bandwidth beyond the bound for ideal focusing usually means reduced focal quality, which cannot be judged when focal-plane profiles across the band are not shown. Dispersion engineering of meta-atoms is limited to small optical power or narrow wavelength ranges, and correction shown on a small device does not establish it for a larger one.

**Resolved by.** Focal length, efficiency and the focal-spot profile or Strehl ratio measured at several wavelengths across the band, edges included; the bandwidth stated with its criterion; the claimed bandwidth placed against a published bound for the device's aperture, NA and thickness; the device diameter stated, and claims for larger apertures backed by measurements on larger devices.

**Benchmark.** [5], [6], [7]

## 5. Conditions for an effective-medium description

**Question.** When an effective permittivity, permeability or refractive index is assigned, does the paper show that the structure is in a regime where local bulk parameters are meaningful: a unit cell small compared with the wavelength in the medium, parameters that do not change with sample thickness or number of layers, and the same parameters describing other angles of incidence and other samples?

**Why it matters.** Bulk effective parameters are meaningful only if they do not depend on the size and shape of the sample or on the wave used to probe it. In most metamaterials the phase changes noticeably across one unit cell, retrieved values change with the number of layers and can converge slowly, and a single layer or patterned surface can behave differently from the bulk; for such samples a sheet description, such as a surface impedance, is more appropriate. Parameters fitted to one plane wave can reproduce its reflection and transmission and still fail for other excitations.

**Resolved by.** The ratio of wavelength to period stated; the retrieval repeated for several thicknesses or numbers of layers, showing convergence; the parameters tested on a second configuration, such as oblique incidence or a sample of different thickness; for a single layer, sheet parameters in place of bulk ones, or bulk values presented as a fit to one measurement and not as material properties.

**Benchmark.** [8], [9], [10], [11]

## 6. Retrieval procedure and physical checks

**Question.** How were the effective parameters extracted (from measured or simulated complex reflection and transmission coefficients, with which reference planes and assumed thickness, and which branch of the refractive index), and do the results pass the checks of passivity and causality?

**Why it matters.** The inversion from reflection and transmission to a refractive index has several branches, and it needs a thickness that is not defined for a single functional layer; unit cells that are not symmetric along the propagation direction need a modified procedure. Retrieved parameters with the wrong sign of the imaginary part, a frequency dependence in low-loss regions that violates the Foster theorem or other causality-based conditions, or a strong dependence on incidence angle show that the description is not a material property.

**Resolved by.** The retrieval method cited and its inputs stated, including the reference planes and effective thickness; the choice of branch justified, for example by agreement between samples of different length; the imaginary parts of permittivity and permeability shown, with signs consistent with a passive medium, or any inconsistency discussed; unit-cell asymmetry addressed.

**Benchmark.** [8], [9], [11]

## 7. Negative-index claims

**Question.** For a claimed negative refractive index, does the paper give the real and imaginary parts of the index across the band, the figure of merit (the magnitude of the real part divided by the imaginary part) at the quoted wavelength, the signs of the effective permittivity and permeability there, and the number of functional layers and total thickness compared with the wavelength?

**Why it matters.** Loss peaks near the resonance that produces the negative index, so the figure of merit depends strongly on where in the band the index is quoted, and a negative index can also appear where only the permittivity is negative, at higher loss. Fabricated optical samples are often a few layers and less than a wavelength thick; their retrieved index depends on the number of layers and coupling between them and may not describe a bulk material, and an effective permeability can fail over part of the backward-wave band.

**Resolved by.** The real and imaginary parts of the index plotted across the band, with the figure of merit at the quoted wavelength; the signs of the real parts of permittivity and permeability shown; retrievals for several numbers of layers showing convergence; thickness compared with wavelength, and the claim worded for a thin film when the sample is not bulk; the retrieved index checked against a second configuration, such as a sample of different thickness.

**Benchmark.** [8], [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. Li et al., High-efficiency high-numerical-aperture metalens designed by maximizing the efficiency limit, Optica 11, 454 (2024); read as preprint arXiv:2311.13592 | doi:10.1364/OPTICA.514907 |
| 2 | A. Arbabi et al., Increasing efficiency of high numerical aperture metasurfaces using the grating averaging technique, Sci. Rep. 10, 7124 (2020) | doi:10.1038/s41598-020-64198-8 |
| 3 | R. Pestourie et al., Inverse design of large-area metasurfaces, Opt. Express 26, 33732 (2018); read as preprint arXiv:1808.04215 | doi:10.1364/OE.26.033732 |
| 4 | N. Mohammadi Estakhri and A. Alù, Wave-front transformation with gradient metasurfaces, Phys. Rev. X 6, 041008 (2016) | doi:10.1103/PhysRevX.6.041008 |
| 5 | K. Shastri and F. Monticone, Bandwidth bounds for wide-field-of-view dispersion-engineered achromatic metalenses, EPJ Appl. Metamat. 9, 16 (2022); read as preprint arXiv:2204.09154 | doi:10.1051/epjam/2022012 |
| 6 | F. Presutti and F. Monticone, Focusing on bandwidth: achromatic metalens limits, Optica 7, 624 (2020); read as preprint arXiv:2001.10899 | doi:10.1364/OPTICA.389404 |
| 7 | J. Engelberg and U. Levy, The advantages of metalenses over diffractive lenses, Nat. Commun. 11, 1991 (2020) | doi:10.1038/s41467-020-15972-9 |
| 8 | C. Simovski and S. Tretyakov, On effective electromagnetic parameters of artificial nanostructured magnetic materials, Photonics Nanostruct. Fundam. Appl. 8, 254 (2010); read as preprint arXiv:1003.3309 | doi:10.1016/j.photonics.2010.04.005 |
| 9 | D. R. Smith et al., Electromagnetic parameter retrieval from inhomogeneous metamaterials, Phys. Rev. E 71, 036617 (2005) | doi:10.1103/PhysRevE.71.036617 |
| 10 | J. Zhou et al., Size dependence and convergence of the retrieval parameters of metamaterials, Photonics Nanostruct. Fundam. Appl. 6, 96 (2008); read as preprint arXiv:0710.0822 | doi:10.1016/j.photonics.2007.10.003 |
| 11 | J. Zhou et al., Negative refractive index response of weakly and strongly coupled optical metamaterials, Phys. Rev. B 80, 035109 (2009); read as preprint arXiv:0907.1119 | doi:10.1103/PhysRevB.80.035109 |
