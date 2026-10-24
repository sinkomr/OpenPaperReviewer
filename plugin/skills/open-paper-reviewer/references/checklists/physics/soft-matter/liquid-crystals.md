---
id: T-LIQUID-CRYSTALS
name: Liquid crystals
type: technique
field: physics/soft-matter
applies_when: the paper studies nematic, smectic, cholesteric or other liquid-crystal phases, identifies a mesophase by polarised microscopy, X-ray scattering or calorimetry, prepares aligned cells, measures anchoring, elastic constants, viscosities or field-induced switching, characterises a phase transition, or interprets defect textures
version: "0.1"
---

# Liquid crystals

Experiments on liquid crystals are used to claim that a material forms a given mesophase (nematic, smectic, cholesteric, columnar or a new phase), to locate and characterise its phase transitions, and to measure its anchoring, elastic, viscous and dielectric properties and the defects it supports. Most of these claims rest on polarised optical microscopy (POM), X-ray scattering, differential scanning calorimetry (DSC) and the response of thin aligned cells to electric or magnetic fields, such as the Fréedericksz transition.

## 1. Phase identification

**Question.** How was each phase identified: is the polarised-microscopy texture supported by X-ray scattering and calorimetry and, where relevant, by conoscopy or miscibility with a material whose phase is known?

**Why it matters.** A texture shows the pattern of the director seen through crossed polarisers; it does not measure the positional order that separates nematic, smectic and columnar phases. X-ray scattering resolves layering and tilt, but some phase structures give no conventional Bragg reflections and are only revealed by resonant scattering.

**Resolved by.** Textures shown on both heating and cooling, with the cell thickness and surface treatment stated; X-ray patterns, preferably from aligned samples, with layer spacings against temperature and peak widths compared with the instrumental resolution; transition temperatures and enthalpies from calorimetry; for a phase claimed to be new, agreement between several independent techniques, such as X-ray scattering, calorimetry, conoscopy and miscibility studies.

**Benchmark.** [1], [2], [3]

## 2. Character of phase transitions

**Question.** When the paper states that a transition is first order or continuous, quotes a latent heat or fits critical exponents, what are the temperature resolution, the scan rate and the range of reduced temperature used, and is an upper limit given for any latent heat that was not detected?

**Why it matters.** Some liquid-crystal transitions have latent heats so small that whether they look continuous or weakly first order depends on the resolution of the measurement, and the nematic-to-smectic-A transition can appear continuous to within a stated limit. Effective critical exponents at such transitions vary systematically from one material to another, in trends compared with a predicted crossover between different kinds of critical behaviour, so a single fitted exponent depends on the material and the fitting range and is not by itself a universal value.

**Resolved by.** High-resolution calorimetry or X-ray data with the scan rate and temperature stability stated; latent heats or upper limits on them; heating and cooling runs with any hysteresis reported; temperatures given relative to the transition temperature measured in the same sample; the fitted range of reduced temperature stated and the exponents compared with those of related materials.

**Benchmark.** [4], [5]

## 3. Cell preparation and surface anchoring

**Question.** Does the paper state the alignment layer and how it was prepared, the cell gap as measured for each cell, the pretilt, and the anchoring strength, or show that the anchoring is strong enough for the analysis it uses?

**Why it matters.** The alignment layer fixes the director at the walls and enters every analysis that assumes a boundary orientation. Measured anchoring energies depend on the method and its assumptions: the standard optical method needs the twist elastic constant and the cell gap and overestimates anchoring on birefringent alignment layers, high-field methods can be distorted by an in-plane inhomogeneous director, even to the wrong sign, and ions adsorbed at the surfaces make the effective anchoring depend on cell thickness.

**Resolved by.** The alignment material and processing (rubbing conditions, exposure dose, baking) stated; the gap of each cell measured, for example by interferometry, and not taken from the spacer size; uniform alignment shown over the area measured; the anchoring strength measured by a method whose assumptions are checked for that cell, or an argument that the result does not depend on it; results compared across more than one cell thickness.

**Benchmark.** [6], [7], [8]

## 4. Elastic constants from field-induced deformation

**Question.** When elastic constants are extracted from a Fréedericksz threshold or from field-dependent deformation, which field (magnetic or electric), geometry and model were used, and were the dielectric or diamagnetic anisotropy, the anchoring and the capacitance of the alignment layers measured or accounted for?

**Why it matters.** The threshold formula gives an elastic constant from the field, the anisotropy and the thickness only under strong anchoring; when anchoring is weak the threshold also depends on the anchoring strength and carries a large error. An electric field becomes non-uniform once the director distorts, so in some geometries, including bend with positive dielectric anisotropy, the threshold is well above the value given by the magnetic analogy, and the analogy formula cannot then be used to extract an elastic constant. Electric fields also couple to conductivity and flexoelectric polarisation, which magnetic fields avoid.

**Resolved by.** The anisotropy measured on the same material at the same reduced temperature; a magnetic-field measurement, or a cross-check against one; an electric-field analysis that allows for field non-uniformity and treats the alignment layers as series capacitors; the drive frequency chosen and stated to suppress ionic effects; the anchoring strength known, or the result shown to be independent of cell thickness.

**Benchmark.** [8], [9], [10]

## 5. Viscosities from director dynamics

**Question.** When a viscosity is reported, which coefficient is it (the rotational viscosity, a flow viscosity, or an effective combination), from which method and geometry, and are the elastic constant, the cell gap and any coupling to flow used in the analysis stated?

**Why it matters.** A nematic has several independent viscosity coefficients, and methods differ in which coefficient or combination they measure and in their accuracy. The relaxation time of a distortion gives a viscosity only through the elastic constant and the square of the cell thickness, so errors in either carry directly into it, and in splay or bend geometries the rotating director drives a backflow, so the relaxation gives an effective viscosity that differs from the rotational viscosity.

**Resolved by.** The coefficient and geometry named; the elastic constant and cell gap used in the analysis measured on the same material and cell at the same temperature; backflow included in the model, or the result reported as an effective viscosity, or a twist geometry used in which there is no flow; a comparison with a second method or with published values for a reference material.

**Benchmark.** [11], [12]

## 6. Ions and electric-field effects

**Question.** For results that depend on an applied electric field, does the paper characterise the ionic content of the filled cells, such as their conductivity or ion density, and show that the response does not come from ionic screening, for example by its dependence on drive frequency?

**Why it matters.** Even small ion concentrations screen an applied field and change the response of the cell. Purified materials pick up ions during preparation and handling, alignment layers both release and trap ions, and the ion concentrations reported for the same compound by different groups vary widely. Ions adsorbed at the surfaces also change the effective anchoring.

**Resolved by.** Conductivity or ion density measured in the cells actually used, for example by impedance or dielectric spectroscopy; the drive waveform and frequency stated and the response checked over a range of frequencies; the alignment layer and filling procedure the same for all cells compared; repeat cells showing the same response.

**Benchmark.** [8], [10], [13]

## 7. Identification of defects

**Question.** How were the sign, strength and structure of the defects determined: from counting brushes alone, or from how the brushes rotate when the sample or the polarisers are rotated, and, for three-dimensional structures, from depth-resolved imaging?

**Why it matters.** The number of dark brushes around a defect fixes the magnitude of its strength (a quarter of the number of brushes) but not its sign, which follows from the sense in which the brushes rotate, and published interpretations of schlieren textures are often incomplete or incorrect. In three dimensions the planar classification does not carry over directly, since half-integer lines of opposite sign can be turned into each other, and the anchoring on surfaces and inclusions constrains which defects must form; claims about three-dimensional structure therefore need the director mapped through the depth of the sample.

**Resolved by.** Images at several orientations of the sample or the polarisers, with the sense of brush rotation reported and the sign and strength assigned from it; the anchoring and thickness of the cell stated; for claims about three-dimensional structure, fluorescence confocal polarising microscopy or another method that maps the director through the depth of the sample.

**Benchmark.** [14], [15], [16], [17]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | P. S. Clegg, X-ray studies of the phases and phase transitions of liquid crystals, Acta Cryst. A 61, 112–121 (2005); read as preprint arXiv:cond-mat/0501011 | doi:10.1107/S0108767304025991 | full text | Sec. I: X-ray diffraction established the layer structure of the smectic-A phase and identified the tilt transition to smectic C. Sec. II: oriented samples on rubbed surfaces and long correlation lengths are needed to resolve block structures. Sec. IV: finite smectic correlation lengths from peak widths; magnetically aligned samples behave like single crystals |
| 2 | P. Barois, H. Gleeson, C. C. Huang and R. Pindak, Application of X-ray resonant diffraction to structural studies of liquid crystals, Eur. Phys. J. Spec. Top. 208, 333–350 (2012) | doi:10.1140/epjst/e2012-01628-9 | abstract | Abstract: X-ray scattering generally characterises liquid-crystal structure, but special symmetries forbid some Bragg reflections so that some phase structures are out of reach of conventional experiments; resonant scattering restores them and its polarisation analysis can discriminate between structural models |
| 3 | R. J. Mandle, A ten-year perspective on twist-bend nematic materials, Molecules 27, 2689 (2022); read in Europe PMC (PMC9102178) | doi:10.3390/molecules27092689 | full text | Sec. 1: a newly reported phase was characterised by conoscopy, calorimetry of the transition and resonant X-ray scattering of its periodicity. Sec. 2: freeze-fracture electron microscopy as a further independent probe. Sec. 3: miscibility of one material with a compound showing the same phase is reported |
| 4 | J. Thoen, H. Marynissen and W. Van Dael, Temperature dependence of the enthalpy and the heat capacity of the liquid-crystal octylcyanobiphenyl (8CB), Phys. Rev. A 26, 2886 (1982) | doi:10.1103/PhysRevA.26.2886 | abstract | Abstract: adiabatic scanning calorimetry measured enthalpy, latent heats and heat capacity through three transitions; the nematic-isotropic latent heat is small (about 0.6 kJ/mol) and the smectic-A-nematic transition appears continuous with only an upper limit on its latent heat; the fitted exponent differs from the simple model prediction |
| 5 | C. W. Garland and G. Nounesis, Critical behavior at nematic–smectic-A phase transitions, Phys. Rev. E 49, 2964 (1994) | doi:10.1103/PhysRevE.49.2964 | abstract | Abstract: effective critical exponents from high-resolution heat capacity and X-ray studies show complex, systematic trends with the ratio of the nematic-smectic-A to nematic-isotropic transition temperatures, compared with the predicted crossover between different kinds of critical behaviour |
| 6 | A. Muravsky and A. Murauski, Q&A of liquid crystal alignment: theory and practice, Front. Soft Matter 4, 1382925 (2024) | doi:10.3389/frsfm.2024.1382925 | full text | Sec. 2.2: anchoring energy in the Rapini-Papoular form with polar and azimuthal parts. Sec. 3.1: rubbing conditions and the rubbing cloth are critical. Sec. 3.6: the standard optical method in a twisted cell needs the twist elastic constant and the cell gap and assumes waveguiding, which fails for optically anisotropic alignment layers and overestimates the anchoring |
| 7 | Yu. A. Nastishin, R. D. Polak, S. V. Shiyanovskii, V. H. Bodnar and O. D. Lavrentovich, Nematic polar anchoring strength measured by electric field techniques, J. Appl. Phys. 86, 4199–4213 (1999) | doi:10.1063/1.371347 | abstract | Abstract: in high-field methods for polar anchoring, real cells often deviate from theory because the director is inhomogeneous in the plane of the plates, which can distort the fitted inverse anchoring strength, even changing its sign; a protocol is proposed to check whether a cell is suitable, and results are compared with threshold-field data |
| 8 | V. S. U. Fazio, F. Nannelli and L. Komitov, Sensitive methods for estimating the anchoring strength of nematic liquid crystals on Langmuir-Blodgett monolayers of fatty acids, Phys. Rev. E 63, 061712 (2001); read as preprint arXiv:cond-mat/0010484 | doi:10.1103/PhysRevE.63.061712 | full text | Sec. 1 and Sec. 2.3 with Fig. 9: the Fréedericksz threshold method, the most widely used, has an error too large to resolve small differences when anchoring is weak; threshold defined at 20% of saturated transmission. Sec. 2.2: ions selectively adsorbed at the surfaces form a double layer, so the effective anchoring depends on cell thickness |
| 9 | E. C. Gartland Jr, Anomalous behavior of electric-field Fréedericksz transitions, Liq. Cryst. Rev. 12, 105–127 (2024); read as preprint arXiv:2409.07654 | doi:10.1080/21680396.2024.2431745 | full text | Abstract, Introduction and Secs. 4 and 5: an electric field becomes non-uniform when the director distorts, unlike a magnetic field; for bend with positive and splay with negative dielectric anisotropy the threshold is higher than the magnetic analogy predicts (Sec. 5: about 63% higher for bend in a common cyanobiphenyl nematic) |
| 10 | E. E. Zavvou, A. Jarosik, H. Nádasi, C. A. Krontiras, P. K. Karahaliou, R. P. Tuffin, M. Klasen-Memmer and A. Eremin, Signatures of polar order in a ferroelectric nematic liquid crystal: splay stiffening and twist softening, Soft Matter 21, 7508–7518 (2025); read as preprint arXiv:2505.15714, which carries a different title | doi:10.1039/d5sm00670h | full text | Sec. 2: electric Fréedericksz analysis models the polyimide alignment layers as series capacitors and uses a drive frequency chosen to minimise ionic effects; the dielectric or diamagnetic anisotropy is needed. Sec. 3.4: magnetic measurements avoid the influence of conductivity and flexoelectric polarisation; the analysis assumes strong anchoring; flexoelectric coupling distorts electric-field fits |
| 11 | V. V. Belyaev, Physical methods for measuring the viscosity coefficients of nematic liquid crystals, Phys. Usp. 44, 255–284 (2001) | doi:10.1070/PU2001v044n03ABEH000831 | abstract | Abstract: hydrodynamic theory gives five independent viscosity coefficients, of which the rotational viscosity is the distinctive one; shear-flow, ultrasonic, rotating-magnetic-field, Fréedericksz-dynamics and light-scattering methods are described and compared for accuracy, complexity and the amount of material needed |
| 12 | S. DasGupta, P. Chattopadhyay and S. K. Roy, Effect of a rigid nonpolar solute on the splay, bend elastic constants, and on rotational viscosity coefficient of 4,4′-n-octyl-cyanobiphenyl, Phys. Rev. E 63, 041703 (2001); read as preprint arXiv:cond-mat/0011452 | doi:10.1103/PhysRevE.63.041703 | full text | Sec. 2: the relaxation time after the field is removed gives an effective rotational viscosity through the cell thickness squared and the splay elastic constant; splay reorientation drives a backflow, the effective value is about 10% below the rotational viscosity, and pure twist involves no flow. Sec. 3: the relaxation is measured from the capacitance decay and analysed with the splay constant from static measurements |
| 13 | Y. A. Garbovskiy, Evaluating the concentration of ions in liquid crystal cells: hidden factors and useful techniques, Proceedings 62, 10 (2021), paper of the 2nd International Online Conference on Crystals held in 2020 | doi:10.3390/proceedings2020062010 | abstract | Abstract: small amounts of ions screen applied fields; purified materials pick up ions during processing and handling; ion concentrations reported for the same liquid crystal by different groups vary widely; alignment layers both generate and trap ions and so set the actual concentration in a cell |
| 14 | J. E. Lydon, H. Gleeson and E. I. L. Jull, The identification of the sign and strength of disclinations in the schlieren (nucleated domain) texture of the nematic phase, by optical microscopy, Liq. Cryst. 44, 1775–1786 (2017); read as the White Rose Research Online record, whose listed DOI 10.1080/02678292.2017.1336580 did not resolve when checked | https://eprints.whiterose.ac.uk/id/eprint/117213/ | abstract | Abstract: the sign and strength of each point singularity can be determined from how the dark brushes change when the sample or the polarisers are rotated; these rules have been largely overlooked and much of the literature is incomplete, confusing or incorrect |
| 15 | G. P. Alexander, B. G. Chen, E. A. Matsumoto and R. D. Kamien, Colloquium: Disclination loops, point defects, and all that in nematic liquid crystals, Rev. Mod. Phys. 84, 497 (2012); read as preprint arXiv:1107.1169 | doi:10.1103/RevModPhys.84.497 | full text | Sec. I: defects form at phase transitions and can be induced by boundary conditions such as anchoring on inclusions. Sec. II.1: the strength is plus or minus one quarter of the number of brushes, so counting fixes the magnitude but not the sign. Sec. II.3: in three dimensions planar textures of strength plus and minus one half can be converted into each other by a uniform rotation. Sec. IV: radial anchoring on a colloidal inclusion makes it carry a topological charge that must be balanced by a companion point defect or a disclination loop |
| 16 | S. Fumeron and B. Berche, Introduction to topological defects: from liquid crystals to particle physics, Eur. Phys. J. Spec. Top. 232, 1813–1833 (2023); read as preprint arXiv:2209.07743 | doi:10.1140/epjs/s11734-023-00803-x | full text | Sec. III.1 (footnote on the typology of disclinations): polarising microscopy shows schlieren patterns with four times the absolute strength in dark brushes; the sign follows from whether the brushes rotate with or against crossed polarisers that are rotated |
| 17 | I. I. Smalyukh, B. I. Senyuk, P. Palffy-Muhoray, O. D. Lavrentovich, H. Huang, E. C. Gartland Jr., V. H. Bodnar, T. Kosa and B. Taheri, Electric-field-induced nematic-cholesteric transition and three-dimensional director structures in homeotropic cells, Phys. Rev. E 72, 061707 (2005); read as preprint arXiv:cond-mat/0512365 | doi:10.1103/PhysRevE.72.061707 | abstract | Abstract: fluorescence confocal polarising microscopy determines three-dimensional director structures in confined cholesteric cells directly and unambiguously, mapped against the ratio of thickness to pitch and the applied voltage |
