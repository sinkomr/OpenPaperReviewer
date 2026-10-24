---
id: T-METASURFACES
name: Metamaterials and metasurfaces
type: technique
field: physics/optics-photonics
applies_when: the paper reports a metamaterial or metasurface device such as a metalens, beam deflector or hologram, quotes its efficiency, bandwidth or field of view, or assigns an effective permittivity, permeability or refractive index, including a negative index, to a structured medium
version: "0.1"
---

# Metamaterials and metasurfaces

Metamaterials are structured media, and metasurfaces structured layers thinner than the wavelength, built from sub-wavelength elements (meta-atoms) designed to set the amplitude, phase or polarisation of light. They are used to claim flat devices such as metalenses (metasurface lenses), deflectors and holograms with a stated efficiency, bandwidth and field of view, and media with designed effective permittivity, permeability or refractive index, including a negative index.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | S. Li, H.-C. Lin and C. W. Hsu, High-efficiency high-numerical-aperture metalens designed by maximizing the efficiency limit, Optica 11, 454–459 (2024); read as preprint arXiv:2311.13592 | doi:10.1364/OPTICA.514907 | full text | Sec. II: transmission efficiency (transmitted over incident power) and Strehl ratio (normalised to transmitted power) defined separately. Sec. IV: focusing efficiency (power within three spot widths over incident power) is not optimised because it can rise when the spot widens. Supplementary Table 1: literature values mix definitions, averaging conventions (ranges, averages, maxima), and simulated with measured results |
| 2 | A. Arbabi, E. Arbabi, M. Mansouree, S. Han, S. M. Kamali, Y. Horie and A. Faraon, Increasing efficiency of high numerical aperture metasurfaces using the grating averaging technique, Sci. Rep. 10, 7124 (2020) | doi:10.1038/s41598-020-64198-8 | full text | Introduction: the usual design assumes locally periodic meta-atoms with isotropic radiation patterns, which weakens at high NA; meta-atom response changes with incident and scattered angle and efficiency falls with NA. Performance verification: focusing efficiency measured as power through an aperture over incident power taken with a reference lens; measured deflection efficiencies about 7% below simulation, attributed to fabrication dimension errors |
| 3 | R. Pestourie, C. Pérez-Arancibia, Z. Lin, W. Shin, F. Capasso and S. G. Johnson, Inverse design of large-area metasurfaces, Opt. Express 26, 33732–33747 (2018); read as preprint arXiv:1808.04215 | doi:10.1364/OE.26.033732 | full text | Sec. 2: the locally periodic approximation treats each region as an equivalent periodic surface, valid when unit cells vary slowly, and can break down for very rapid variation such as diffraction to near-glancing angles. Sec. 3.1: checked against a brute-force Maxwell solver, with agreement worse close to the surface, which is attributed to abrupt changes in pillar width and neglected evanescent fields |
| 4 | N. Mohammadi Estakhri and A. Alù, Wave-front transformation with gradient metasurfaces, Phys. Rev. X 6, 041008 (2016) | doi:10.1103/PhysRevX.6.041008 | full text | Abstract: local phase compensation is insufficient for arbitrary wave manipulation, and full-wave design is needed. Sec. I and the section after it: impedance mismatch grows for steeper angles, earlier gradient-metasurface studies found coupling efficiency degrading as the steering angle grows, and the linear phase approximation deviates from the rigorous solution at large deflection angles |
| 5 | K. Shastri and F. Monticone, Bandwidth bounds for wide-field-of-view dispersion-engineered achromatic metalenses, EPJ Appl. Metamat. 9, 16 (2022); read as preprint arXiv:2204.09154 | doi:10.1051/epjam/2022012 | full text | Introduction and Results: the aberration-free phase profile works only at its design incidence, and a local metasurface gives an aberrated image at other angles; a wider field of view and larger NA both lower the achievable bandwidth; the worst-case angle is not always the largest |
| 6 | F. Presutti and F. Monticone, Focusing on bandwidth: achromatic metalens limits, Optica 7, 624–631 (2020); read as preprint arXiv:2001.10899 | doi:10.1364/OPTICA.389404 | full text | Sec. 2, Eqs. 6 to 12: time-bandwidth bounds on achromatic bandwidth in terms of focal length, NA, thickness and index contrast. Table 1 and Fig. 2: published designs compared with the bounds; exceeding the ideal bound signals reduced focal quality, and many papers do not report focal-plane profiles, so aberrations are hard to assess |
| 7 | J. Engelberg and U. Levy, The advantages of metalenses over diffractive lenses, Nat. Commun. 11, 1991 (2020) | doi:10.1038/s41467-020-15972-9 | full text | Section on chromatic correction: color correction by dispersion-engineered nanoantennas is limited to small optical powers and/or wavelength ranges; all achromatic metalenses demonstrated to date are small, and good correction at 10 to 100 micrometres does not show that it carries over to 1 to 10 millimetres |
| 8 | C. Simovski and S. Tretyakov, On effective electromagnetic parameters of artificial nanostructured magnetic materials, Photonics Nanostruct. Fundam. Appl. 8, 254–263 (2010); read as preprint arXiv:1003.3309 | doi:10.1016/j.photonics.2010.04.005 | full text | Sec. 1: local parameters must not depend on sample size, shape or excitation; samples of one or a few layers and patterned surfaces need surface or grid impedance; retrieved parameters can show non-physical signs of imaginary parts, violate the Foster theorem in low-loss regions or depend on incidence angle; fishnet permeability does not hold across the whole backward-wave band. Sec. 2: local parameters fail as the wavelength in the medium approaches the period |
| 9 | D. R. Smith, D. C. Vier, Th. Koschny and C. M. Soukoulis, Electromagnetic parameter retrieval from inhomogeneous metamaterials, Phys. Rev. E 71, 036617 (2005) | doi:10.1103/PhysRevE.71.036617 | abstract | Abstract: in nearly all metamaterials the phase varies noticeably across a unit cell, so they do not rigorously reach an effective-medium limit; the index can be established but the impedance only approximately; unit cells asymmetric along the propagation axis need a modified retrieval |
| 10 | J. Zhou, Th. Koschny, M. Kafesaki and C. M. Soukoulis, Size dependence and convergence of the retrieval parameters of metamaterials, Photonics Nanostruct. Fundam. Appl. 6, 96–101 (2008); read as preprint arXiv:0710.0822 | doi:10.1016/j.photonics.2007.10.003 | full text | Sec. II: retrieved parameters converge only after several cells and differ from the single-cell result; a negative index below resonance, where only the permittivity is negative, carries higher loss; the figure of merit peaks away from the loss maximum at resonance. Sec. III: convergence depends on the wavelength-to-cell ratio and is slow for fishnets |
| 11 | J. Zhou, Th. Koschny, M. Kafesaki and C. M. Soukoulis, Negative refractive index response of weakly and strongly coupled optical metamaterials, Phys. Rev. B 80, 035109 (2009); read as preprint arXiv:0907.1119 | doi:10.1103/PhysRevB.80.035109 | full text | Sec. II: figure of merit defined as the magnitude of real over imaginary index; unit-cell size along propagation is undefined for one measured layer. Sec. III: figure of merit low near resonance and, for strongly coupled stacks, rising with layer number. Introduction: ten-layer fishnets about half a wavelength thick are described as not bulk; strongly coupled stacks converge slowly and differ from a single layer. Appendix A: the index branch is chosen by overlap across sample lengths |
