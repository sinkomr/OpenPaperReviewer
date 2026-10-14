---
id: T-EELS
name: Electron energy-loss spectroscopy (EELS) in the (scanning) transmission electron microscope
type: technique
field: physics
applies_when: the paper bases a claim on electron energy-loss spectra or spectrum images recorded in a TEM or STEM, such as composition, valence or bonding, a band gap or optical response, or the location of a spectral signal
version: "0.1"
---

# Electron energy-loss spectroscopy (EELS) in the (scanning) transmission electron microscope

EELS spectra and spectrum images are used to claim local composition, valence and bonding, band gaps and optical or plasmonic response, and where in a specimen a given signal originates, down to the atomic scale.

## 1. Specimen thickness and plural scattering

**Question.** Is the relative thickness (t/λ) of the analysed region reported, and was plural scattering shown to be negligible or removed before edges or onsets were interpreted?

**Why it matters.** Plural inelastic scattering changes the shape of the background under an edge and distorts onsets in the low-loss region, and the background grows strongly with thickness, so an apparent elemental signal or onset energy can vary with thickness alone. Converting t/λ to an absolute thickness needs an inelastic mean free path, and a parameterised value can differ from a measured one by roughly 20 %.

**Resolved by.** A t/λ value or map obtained from the low-loss spectrum of the same area; analysis restricted to thin regions, or spectra deconvolved to the single-scattering distribution with the remaining uncertainty acknowledged; the mean free path and its source stated wherever an absolute thickness or areal density is quoted.

**Benchmark.** [3], [4], [5], [8]

## 2. Background subtraction

**Question.** Are the background model, the fitting window and the signal integration window stated, and is a background-subtracted spectrum shown so that the fit can be judged?

**Why it matters.** Core-loss edges sit on a large background, so an error in extrapolating it passes directly into the extracted signal and grows with distance from the fitting window. At low counts per channel, as in fast or atomic-resolution maps, the usual power-law fit can become biased or unstable. Overlapping edges and thickness-dependent background shapes are not described by one extrapolated power law, and spatial averaging of the background can produce rings at abrupt boundaries.

**Resolved by.** Representative raw and background-subtracted spectra from the regions on which the claim rests, with the pre-edge residual scattering about zero; fitting and integration windows given; reference-spectrum or full-model fitting where edges overlap; a statement of how the result changes for reasonable alternative windows.

**Benchmark.** [1], [2], [3]

## 3. Elemental quantification and detection limits

**Question.** Where compositions, areal densities or the absence of an element are reported, are the cross-sections, the beam energy, the convergence and collection angles and the integration windows given, together with an uncertainty or a detection limit?

**Why it matters.** Edge intensity converts to a number of atoms only through a partial cross-section defined for the collection angle and energy window used, and the accuracy of a calculated cross-section is established only by comparison with a standard of known composition. Overlapping edges or changing fine structure bias simple window integration. Whether an element can be detected depends on the dose, the background under its edge and the cross-section, so a missing edge does not by itself show that the element is absent.

**Resolved by.** Acquisition geometry and cross-section model stated; the quantification checked on a standard of known composition measured in the same way; overlapping edges handled by reference-spectrum or model fitting; an uncertainty that covers more than counting noise; for trace or absence claims, an estimated minimum detectable amount for the dose and thickness used.

**Benchmark.** [1], [3], [5]

## 4. Near-edge fine structure and valence assignments

**Question.** Where valence, coordination or bonding is inferred from the shape or position of an edge, is the assignment tied to reference spectra or calculations for that edge, and are other causes of the same spectral change considered?

**Why it matters.** Near-edge structure responds to the charge on the ion and also to site symmetry and lattice distortion, so a change in edge shape is not a unique signature of valence. The shifts and splittings involved can be below 1 eV, comparable to energy instabilities during acquisition and to shifts that denoising can introduce. The beam can also change the valence that is being measured.

**Resolved by.** Reference spectra from compounds of known valence and coordination, or calculated spectra, compared with the data for the same edge; energy drift during acquisition corrected or bounded, for example by aligning many short exposures; unprocessed spectra shown alongside any filtered ones; a check that the feature is stable under the beam (item 5).

**Benchmark.** [1], [2], [4]

## 5. Radiation damage

**Question.** Is the electron fluence (dose) on the analysed area reported, and is there a check that the spectral feature of interest did not change during acquisition?

**Why it matters.** The beam can remove material, alter composition and change bonding or valence, and fine structure can change at fluences where images still show an intact structure. The focused probes and long exposures needed for weak signals deliver the highest fluences. The dominant damage mechanism and its threshold depend on the material and on the beam energy.

**Resolved by.** Beam energy, probe current, exposure and the resulting fluence stated; a time or fluence series for the feature used in the claim, or a measured critical fluence, with the reported data taken below it; spectra from the start and the end of the acquisition compared; low-dose, lower-voltage or cryogenic conditions where the material requires them.

**Benchmark.** [1], [3], [4]

## 6. Spatial origin of the signal

**Question.** When a spectral feature is assigned to a particular layer, interface, particle or atomic column, does the paper distinguish the probe size from the region that contributes to the signal?

**Why it matters.** Inelastic scattering is delocalised, increasingly so at low energy loss, so a low-loss signal can come from a region several nanometres wide even with an atomic-sized probe. In layered or nanostructured specimens the layers respond together, and the response of a thin layer can be dominated by its neighbours. In thicker regions the probe also spreads as it passes through the specimen.

**Resolved by.** An estimate of the delocalisation length for the energy loss and collection geometry used; specimen thickness reported; a simulation of the response expected from the actual geometry, including neighbouring layers; where localisation is essential, an acquisition geometry chosen to favour localised scattering, or confirmation from a core-loss signal.

**Benchmark.** [1], [8]

## 7. Low-loss spectra: band gaps and optical properties

**Question.** Where a band gap, dielectric function or other optical property is extracted from the low-loss region, is it stated how the zero-loss peak was removed and how retardation and surface losses were excluded for the beam energy and thickness used?

**Why it matters.** The gap onset lies on the tail of the zero-loss peak, and the value obtained depends on how that tail is modelled and on the onset-fitting procedure. In materials of high refractive index, Cherenkov radiation and guided light modes add intensity near and below the gap that varies with thickness and beam energy, and surface losses modulate the bulk signal. Each of these can shift the apparent gap or distort a Kramers–Kronig analysis.

**Resolved by.** The zero-loss model and fitting ranges stated, with spectra shown before and after subtraction; beam energy and thickness reported with an assessment of whether retardation losses are expected for the material, tested by lower beam energy, a thinner specimen or a changed collection angle; results at more than one thickness; an uncertainty on the gap that includes the choice of method.

**Benchmark.** [1], [6], [7], [8]

## 8. Denoising and multivariate analysis

**Question.** If spectra or maps were denoised or decomposed, for example by principal component analysis, is the feature on which the claim rests also visible in unprocessed or simply summed data, and is the number of retained components justified?

**Why it matters.** Because EELS edges are weak relative to the background, variance-based filtering of raw spectra can discard small local signals, shift fine-structure peaks and produce map contrast that follows a neighbouring edge. The components returned are mathematical abstractions, not the spectra of physical constituents, and the outcome depends on how many are kept.

**Resolved by.** Raw or summed spectra from the relevant pixels shown next to the processed result; the number of components and the criterion for choosing it stated, with a check that the conclusion survives a different choice; residuals examined for spatial structure; the background removed before any decomposition.

**Benchmark.** [1], [2]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | C. Colliex, From early to present and future achievements of EELS in the TEM, Eur. Phys. J. Appl. Phys. 97, 38 (2022) | doi:10.1051/epjap/2022220012 | full text | §2.2 (Denoising): PCA can lose information held in low-variance components and create artefacts; the number of components is a sensitive choice and components are abstract. §3.1: edge signal converts to atoms per area through a cross-section defined for the collection angle and energy window; overlapping edges or variable fine structure need reference-spectrum or model fitting; fine structure depends on cation charge and on site symmetry and distortion, and is interpreted against reference spectra and calculations. §3.2.1: a gap measurement needs a good model of the zero-loss tail, and Cherenkov and guided-mode losses bias it, more so in thicker specimens. §2.1.1 and §3.2.2.1: probe size sets the resolution only while the specimen does not broaden the beam, and neighbouring layers add a delocalised response. §4.2: an intense probe converted an oxide to metal during acquisition; instabilities limit energy resolution unless short exposures are realigned. |
| 2 | P. Cueva, R. Hovden, J. A. Mundy, H. L. Xin, D. A. Muller, Data processing for atomic resolution electron energy loss spectroscopy, Microsc. Microanal. 18, 667–675 (2012) | doi:10.1017/S1431927612000244 | full text | Read as the preprint, arXiv:1112.3059. Sections Least Squares Estimation and Linear Combination of Power Laws: background-extrapolation error passes directly into the signal and grows away from the fit window; low-count spectra bias power-law fits; the pre-edge residual should fluctuate about zero. Section Local Background Averaging: averaging can produce ringing at particle edges. Section Extracting EELS Core-loss Edge: PCA filtering of raw spectra can create false map contrast, shift fine-structure peaks and remove interface signals, so the background should be removed first. |
| 3 | M. A. Aronova, R. D. Leapman, Development of electron energy-loss spectroscopy in the biological sciences, MRS Bull. 37, 53–62 (2012) | doi:10.1557/mrs.2011.329 | full text | Read as the author manuscript in PubMed Central (PMC3465455). Section on high-sensitivity elemental mapping: plural scattering changes the background shape under an edge and is corrected using t/λ from unfiltered and zero-loss intensities. Section Detection Limits: the minimum detectable number of atoms depends on dose, edge and background cross-sections, collection angle and energy window; near-single-atom detection needs doses at which knock-on damage removes mass. |
| 4 | M. Ilett, M. S'ari, H. Freeman, Z. Aslam, N. Koniuch, M. Afzali, J. Cattle, R. Hooley, T. Roncal-Herrero, S. M. Collins, N. Hondow, A. Brown, R. Brydson, Analysis of complex, beam-sensitive materials by transmission electron microscopy and associated techniques, Phil. Trans. R. Soc. A 378, 20190601 (2020) | doi:10.1098/rsta.2019.0601 | full text | §2: knock-on and radiolysis mechanisms; critical fluence measured from the decay of a diffraction, image or spectral feature. §4 and §11: analysis has to fit within a fluence budget. §8: damage can change composition and bonding; fine structure in oxides can change at fluences where imaging shows no structural change; the EELS background rises steeply with thickness. |
| 5 | A. J. Craven, J. Bobynko, B. Sala, I. MacLaren, Accurate measurement of absolute experimental inelastic mean free paths and EELS differential cross-sections, Ultramicroscopy 170, 113–127 (2016) | doi:10.1016/j.ultramic.2016.08.012 | abstract | Abstract: states beam energy, probe and collection angles; calculated cross-sections matched edges from compounds of known composition to within a few percent; a measured inelastic mean free path was about 18 % below the value from a widely used parameterisation. |
| 6 | M. Stöger-Pollach, Optical properties and bandgaps from low loss EELS: Pitfalls and solutions, Micron 39, 1092–1110 (2008) | doi:10.1016/j.micron.2008.01.023 | abstract | Abstract: band-gap determination needs accurate removal of the zero-loss peak and treatment of retardation losses, and the same holds before Kramers–Kronig analysis for optical properties. |
| 7 | R. Erni, N. D. Browning, The impact of surface and retardation losses on valence electron energy-loss spectroscopy, Ultramicroscopy 108, 84–99 (2008) | doi:10.1016/j.ultramic.2007.03.005 | abstract | Abstract: surface and retardation losses give a thickness-dependent modulation of the volume loss that can hamper identification of band-gap and interband energies and of bulk dielectric data; guided light modes in thin foils and Cherenkov losses in thicker ones for materials such as Si and GaAs. |
| 8 | H. J. Jung, Local bandgap and optoelectronic measurement using monochromated STEM-VEELS: fundamentals, challenges, and recent advances, Appl. Microsc. 56, 22 (2026) | doi:10.1186/s42649-026-00143-9 | full text | Section Spatial delocalization: probe size is not the spatial resolution of a low-loss measurement, and delocalisation grows as the energy loss falls. Section Sources of uncertainty (Table 7): Cherenkov and guided-mode losses, plural scattering, zero-loss subtraction and the onset-fitting method each shift the extracted gap, and a reproducible value is not necessarily accurate. Section Specimen preparation and thickness effects: plural scattering distorts the onset, deconvolution leaves residual uncertainty, and t/λ below about 1 is recommended. |
