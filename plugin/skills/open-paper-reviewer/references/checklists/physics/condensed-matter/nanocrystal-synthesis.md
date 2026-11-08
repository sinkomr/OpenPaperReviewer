---
id: T-NANOCRYSTAL-SYNTHESIS
name: Solution synthesis and characterization of nanocrystals
type: technique
field: physics/condensed-matter
applies_when: the paper reports nanocrystals or nanoparticles made by a colloidal, solvothermal or hydrothermal route and makes claims about their phase, composition, purity, shape, size distribution, yield or reproducibility
version: "0.1"
---

# Solution synthesis and characterization of nanocrystals

## 1. Crystallite size versus particle size

**Question.** If a size is derived from diffraction peak widths, is it presented as a crystalline-domain size, is instrumental broadening treated, and is it compared with the particle size from microscopy?

**Why it matters.** Peak width reflects the coherent domain, which is smaller than the particle when particles are polycrystalline. The Scherrer constant depends on domain shape, anisotropic particles give different widths for different reflections, most of the width is instrumental for domains of about 50 nm and above, and peaks from domains below about 5 nm are broad and weak.

**Resolved by.** The reflections and constant used; the treatment of instrumental broadening, or a full-profile fit; and the domain size set against the microscopy size, with any mismatch interpreted (polycrystalline particles, or imaged particles that are a minority of the sample).

**Benchmark.** [1]

## 2. Size, shape and yield

**Question.** Are the size and shape distributions shown as histograms from a stated number of particles taken from separated regions of the grid, and does the paper define yield as the fraction of particles with the claimed shape or as the fraction of starting material recovered as product?

**Why it matters.** Selected micrographs can show a shape or size that is a minority of the batch, and a mean alone hides a bimodal population. Shape yield and overall yield are usually different numbers, and an undefined yield can be read as either.

**Resolved by.** Histograms from several hundred particles (the benchmarks give 200 per region and 300 per sample) from separated regions, with mean, spread and count; "monodisperse" used only where the measured spread supports it; an ensemble size, such as from light scattering, alongside, with how each weights the population; both shape yield and overall yield, with the scale of the preparation; bulk evidence that agrees with the microscopy, such as reflection-dependent peak widths that match the observed dimensions.

**Benchmark.** [1], [2], [4]

## 3. Composition and dopant content

**Question.** Is the composition of the purified product measured directly, rather than taken from the reagent ratio or inferred from lattice constants alone?

**Why it matters.** The amount of an element added to a reaction need not equal the amount incorporated in the particles. Diffraction reports only on the crystalline part of a sample, the linear relation between lattice constant and alloy composition is empirical and often deviates, and lattice constants from broad peaks have limited precision.

**Resolved by.** Element-specific analysis of the product after unreacted reagents have been removed, for example digestion followed by ICP, with EDS or XPS showing which elements the imaged particles contain; measured rather than nominal dopant levels; and lattice-constant trends supported by an internal standard or profile refinement.

**Benchmark.** [1], [2]

## 4. Surface species and purification

**Question.** Is the purification procedure described, and is there evidence for what remains bound to the particle surface and for the removal of unbound reagents?

**Why it matters.** Surfactants, capping agents, ions and solvent adsorb during solution synthesis, so the isolated product is normally an inorganic core with a ligand shell, and a statement that the surface is bare needs its own evidence. Unreacted reagents can be hard to separate and are then counted with the product in composition and concentration measurements, and precipitation with a non-solvent can itself change the ligand shell.

**Resolved by.** Washing steps and solvents given; surface analysis by XPS, EDS or vibrational spectroscopy; for organic ligands, a measurement that separates bound from free species, such as line broadening or diffusion filtering in solution NMR; and quantified ligand amounts where a surface coverage is claimed.

**Benchmark.** [2], [5]

## 5. Reagents, reaction vessel and batch-to-batch variation

**Question.** Are reagent suppliers and purities given, are the vessel and heating conditions specified, and does the paper report how the product varied between repeated batches?

**Why it matters.** Size, shape and dispersity can depend on trace impurities that differ between suppliers and lots, and on water quality, pH and storage. For sealed-vessel reactions the liner and fill volumes, the heating method, whether the stated temperature is internal or external, and when timing starts are often unreported, although they set the pressure and thermal history. A result obtained under unrecorded conditions may not be repeatable elsewhere.

**Resolved by.** An experimental section that lists source, purity and handling of each reagent and solvent and describes observable cues during the reaction; for autoclave work, the vessel, internal and liner volumes, fill volume, heating and stirring arrangement, point of temperature measurement, heating rate and pressure; and results from more than one batch, with the variation between them.

**Benchmark.** [3], [6], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | C. F. Holder and R. E. Schaak, Tutorial on Powder X-ray Diffraction for Characterizing Nanoscale Materials, ACS Nano 13, 7359 (2019) | doi:10.1021/acsnano.9b05157 |
| 2 | C. J. Murphy and J. M. Buriak, Best Practices for the Reporting of Colloidal Inorganic Nanomaterials, Chem. Mater. 27, 4911 (2015) | doi:10.1021/acs.chemmater.5b02323 |
| 3 | L. M. Liz-Marzán et al., Reproducibility in Nanocrystal Synthesis? Watch Out for Impurities!, ACS Nano 14, 6359 (2020) | doi:10.1021/acsnano.0c04709 |
| 4 | J. E. Bonevich and W. K. Haller, Measuring the Size of Nanoparticles Using Transmission Electron Microscopy (TEM), NIST–NCL Joint Assay Protocol PCC-7, version 1.1 (2010) | doi:10.17917/C7N7-N938 |
| 5 | J. De Roo, The Surface Chemistry of Colloidal Nanocrystals Capped by Organic Ligands, Chem. Mater. 35, 3781 (2023) | doi:10.1021/acs.chemmater.3c00638 |
| 6 | A. Roy et al., The Huge Role of Tiny Impurities in Nanoscale Synthesis, ACS Nanosci. Au 4, 176 (2024) | doi:10.1021/acsnanoscienceau.3c00056 |
| 7 | R. McGonigle et al., Autoclave reactor synthesis of upconversion nanoparticles, unreported variables, and safety considerations, Commun. Chem. 8, 36 (2025) | doi:10.1038/s42004-025-01415-3 |
