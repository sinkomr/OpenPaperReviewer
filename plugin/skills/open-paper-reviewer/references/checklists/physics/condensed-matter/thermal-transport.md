---
id: T-THERMAL-TRANSPORT
name: Thermal and thermoelectric transport
type: technique
field: physics/condensed-matter
applies_when: the paper measures thermal conductivity or diffusivity by steady-state, 3-omega or laser flash methods, measures Seebeck, Nernst or thermal Hall coefficients, or claims a thermoelectric figure of merit, a lattice thermal conductivity or a transverse thermal signal from particular excitations
version: "0.1"
---

# Thermal and thermoelectric transport

Thermal and thermoelectric measurements are used to claim a thermal conductivity and its electronic and lattice parts, a Seebeck coefficient (thermopower), a Nernst coefficient or thermal Hall conductivity (κxy), and the thermoelectric figure of merit zT = S²T/(ρκ), where S is the Seebeck coefficient, ρ the electrical resistivity, κ the thermal conductivity and T the temperature. Each rests on a small temperature difference measured on a sample and, for thermal conductivity, on knowing how much heat flows through it, whether from steady-state heat flow, the 3-omega (3ω) electrothermal method or laser flash diffusivity.

## 1. Heat-flow accounting in steady-state methods

**Question.** In a steady-state or slow transient measurement, how was the heat flowing through the sample determined, and how large were the losses by radiation, by conduction along wires and by residual gas compared with that heat, at each temperature reported?

**Why it matters.** The thermal conductivity follows from the heat conducted through the sample divided by the temperature gradient, so any heat lost on the way is counted as conducted. Radiation loss grows roughly with the cube of temperature, and corrections that depend on an assumed emissivity and surface area can under- or over-correct, giving errors that grow with temperature.

**Resolved by.** Measurement in vacuum with radiation shielding; thin, low-conductivity thermometer wires or a differential thermocouple; parasitic losses estimated and shown to be a small fraction of the conducted heat, or a stated correction with the emissivity and area used and the raw and corrected curves both shown; at high temperature, agreement with a method less sensitive to radiation, such as laser flash or 3ω, or with a reference sample.

**Benchmark.** [1], [2]

## 2. Seebeck coefficient: temperature and voltage at the same place

**Question.** Which probe geometry was used, were the temperature difference and the voltage measured at the same points and at the same time, was the Seebeck coefficient taken from the slope of voltage against temperature difference, and does the paper show checks of thermal contact?

**Why it matters.** Thermocouples that draw heat from the sample (the cold-finger effect) or make poor thermal contact misread the temperature difference at the sample; in the common off-axis four-probe geometry this overestimates the Seebeck coefficient by an amount that grows with temperature. Offset voltages of up to several hundred microvolts arise from dissimilar thermocouple wires, reactive samples and the cold-finger effect, and a single reading of voltage over temperature difference cannot separate them from the thermoelectric voltage.

**Resolved by.** The geometry stated; the slope of several voltage and temperature-difference points used, with voltages and temperatures read simultaneously or corrected for drift; the size of the temperature difference stated; heating and cooling runs that agree, and no dependence on the size, sign or rate of the temperature difference or on gas pressure; a check against a reference material where one exists for the temperature range, or against a second geometry.

**Benchmark.** [1], [3]

## 3. 3ω and thin-film thermal conductivity

**Question.** For 3ω measurements, does the paper give the heater width, the film thickness and the frequency range, show that the assumptions of the analysis model hold, and state which component of the thermal conductivity, in-plane or cross-plane, was measured?

**Why it matters.** The simple slope analysis assumes a thermal penetration depth much larger than the heater half-width, and the film value is obtained by subtracting the substrate response, so errors in the substrate conductivity or an unaccounted insulating layer pass into the result. The heater width relative to the film thickness decides whether the measurement is sensitive to cross-plane conduction alone or also to in-plane spreading, and thin-film conductivity is often anisotropic and thickness dependent.

**Resolved by.** Heater dimensions, film thickness and frequency range given, with the penetration depth compared with the heater half-width; the substrate measured by the same method or a reference sample without the film measured alongside; the electrical insulation layer included in the model; heaters of different widths, or a model with anisotropy, where in-plane and cross-plane values are claimed; the direction stated whenever a film value is compared with bulk values.

**Benchmark.** [2]

## 4. Laser flash: diffusivity, heat capacity and density

**Question.** For laser flash data, which model and which heat-loss and finite-pulse corrections were used to obtain the diffusivity, how were the sample thickness and surface coating controlled, and how were the heat capacity and density that convert diffusivity into conductivity measured and checked?

**Why it matters.** The original half-rise-time formula assumes one-dimensional heat flow without losses and a pulse much shorter than the rise time; much of the spread in diffusivity between laboratories comes from errors in thickness, and a coating that is too thick or poorly adherent distorts results for thin samples. Heat capacity estimated by comparison inside a flash instrument is often inaccurate and has led to underestimated conductivity, and immersion density can be overestimated when liquid enters pores.

**Resolved by.** The correction named (for example Cowan or Clark and Taylor, or a fit to the whole transient) with a raw transient and its fit shown; the thickness measured with its uncertainty and the coating described; heat capacity measured by differential scanning calorimetry or drop calorimetry and compared with the Dulong–Petit value above the Debye temperature; the density method and relative density stated; any thermal-expansion correction applied consistently to all affected quantities.

**Benchmark.** [1], [2]

## 5. Electronic and lattice contributions

**Question.** Where the total thermal conductivity is split into electronic and lattice parts, which Lorenz number was used, how was it justified for the carrier density and band structure of the material, and is a bipolar contribution considered?

**Why it matters.** The electronic part is usually estimated from the electrical conductivity with the Wiedemann–Franz law, and using the degenerate-limit Lorenz number for a material that is not strongly degenerate can be off by up to about 40%. This passes directly into the lattice value, which can then be misleading or even negative, and the Wiedemann–Franz law does not include the bipolar contribution of narrow-gap materials at high temperature.

**Resolved by.** The Lorenz number stated with its source; for semiconductors, a value estimated from the measured Seebeck coefficient or from a band model rather than the degenerate limit; the sensitivity of the lattice value to this choice shown; the bipolar contribution discussed where the gap is small; lattice values that remain physically sensible.

**Benchmark.** [4]

## 6. Thermal Hall: transverse temperature difference

**Question.** For thermal Hall data, how was the transverse temperature difference separated from the longitudinal gradient picked up by misaligned thermometers, how large is the residual uncertainty after antisymmetrising in field, and are the sample shape and the way heat enters and leaves the sample accounted for?

**Why it matters.** Misaligned transverse thermometers pick up part of the longitudinal gradient, and even after antisymmetrisation in field this can leave errors of roughly 20 to 50% in κxy, which limits the measurement of small signals. The thermal boundary conditions at the heater and the heat sink change the measured transverse response by factors of order unity for samples of similar length and width, so differences between nominally similar samples can exceed the statistical spread.

**Resolved by.** The raw transverse temperature difference shown for both field polarities, with the antisymmetrisation and the remaining residual quantified; the misalignment estimated; sample dimensions and the attachment of heater and heat sink described; elongated rectangular samples or simulations used to correct for geometry when the size of κxy matters; agreement between samples discussed.

**Benchmark.** [5]

## 7. Attributing a transverse signal to a particular excitation

**Question.** When a Nernst or thermal Hall signal is attributed to a particular source, such as vortices, superconducting fluctuations, magnons or other magnetic excitations, does the paper estimate and exclude the contributions of other carriers, in particular ordinary quasiparticles and phonons?

**Why it matters.** A Nernst signal can come from mobile quasiparticles, whose contribution scales with the ratio of mobility to Fermi energy and can be large, from short-lived Cooper pairs far above the critical temperature, and from mobile vortices. Phonons can also contribute to the thermal Hall signal through coupling to other degrees of freedom, so a transverse thermal signal in a magnetic insulator does not by itself identify magnetic excitations.

**Resolved by.** The quasiparticle contribution estimated from measured mobility and carrier properties and compared with the signal; the temperature and field dependence compared with what each candidate source predicts; the longitudinal thermal conductivity reported alongside the transverse one, so that the role of phonons can be judged; the phonon contribution to a thermal Hall signal estimated or bounded before a magnetic or topological origin is claimed.

**Benchmark.** [6], [7]

## 8. Figure-of-merit claims

**Question.** Were the Seebeck coefficient, electrical resistivity and thermal conductivity that enter zT measured on the same sample, along the same direction and over the same temperature range, and does the paper show heating and cooling data and the uncertainty carried into zT at each temperature?

**Why it matters.** Inhomogeneity and anisotropy cause large errors in zT when the properties are measured on different samples or along different directions. Measurements of one material in several laboratories scatter by about 12% in zT at 300 K and more at higher temperature, with a temperature-averaged standard uncertainty of about 19% from 300 to 700 K, so a modest improvement in zT can lie within the measurement uncertainty.

**Resolved by.** The sample and direction for each property stated, with direction-resolved measurements for anisotropic materials; the relative density given; heating and cooling curves that agree; the uncertainty of each property combined into an uncertainty on zT that grows with temperature; exceptional values confirmed on further samples or by a second method.

**Benchmark.** [1], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | K. A. Borup, J. de Boor, H. Wang, F. Drymiotis, F. Gascoin, X. Shi, L. Chen, M. I. Fedorov, E. Müller, B. B. Iversen and G. J. Snyder, Measuring thermoelectric transport properties of materials, Energy Environ. Sci. 8, 423–435 (2015); read as the published PDF in the Caltech authors repository | doi:10.1039/C4EE01320D | full text | "Measurement guide for authors and reviewers" box: zT confirmation on the same sample and direction, heating and cooling data, several samples. "General considerations": round-robin scatter in zT of 12% at 300 K and 21% at 475 K. "Sample homogeneity": inhomogeneity gives large zT errors when properties come from different samples or directions. "Seebeck coefficient": slope method removes offset voltages of several hundred microvolts; cold-finger effect in the off-axis four-point geometry overestimates thermopower; hysteresis, dependence on the temperature difference and on gas pressure indicate bad thermal contact; reference material only up to 390 K. "Direct measurements": heat-flow corrections for wires and radiation, radiation loss scales with T³, an assumed emissivity and area can overestimate the correction. "Flash diffusivity", "Heat capacity", "Density and thermal expansion": half-rise-time assumptions, Cowan and Clark–Taylor corrections, thickness dominates interlaboratory scatter, graphite coating errors, heat capacity from the flash instrument often inaccurate, Dulong–Petit check, Archimedes density in porous samples, consistent thermal-expansion corrections |
| 2 | D. Zhao, X. Qian, X. Gu, S. A. Jajja and R. Yang, Measurement techniques for thermal conductivity and interfacial thermal conductance of bulk and thin film materials, J. Electron. Packag. 138, 040802 (2016); read as preprint arXiv:1605.08469 | doi:10.1115/1.4034605 | full text | Sec. 2.1.1: parasitic losses by convection, radiation and conduction through thermocouple wires should be kept below about 2% of the heat flow; vacuum, radiation shields, fine low-conductivity wires and differential thermocouples. Sec. 2.2.4: laser flash assumes one-dimensional flow without lateral loss and uses a graphite coating as absorber and emitter. Sec. 3.2.1: the 3ω line-source analysis needs a penetration depth much larger than the heater half-width; the film value relies on a known substrate conductivity; heater width relative to film thickness sets cross-plane or in-plane sensitivity, with a stated width condition; an insulating layer is needed on conducting films and reduces sensitivity; the radiation error of 3ω is small, under 2% even at 1000 K. Sec. 1: thin-film conductivity is often anisotropic and thickness dependent |
| 3 | J. Martin, Protocols for the high temperature measurement of the Seebeck coefficient in thermoelectric materials, Meas. Sci. Technol. 24, 085601 (2013); read as the NIST publication record | doi:10.1088/0957-0233/24/8/085601 | abstract | Abstract: surface temperature errors come from a parasitic heat flux set by the temperature difference to the surroundings and by thermal resistances; the off-axis four-probe arrangement has larger contact resistance and temperature error than the two-probe arrangement, growing with temperature and leading to an overestimated Seebeck coefficient |
| 4 | H.-S. Kim, Z. M. Gibbs, Y. Tang, H. Wang and G. J. Snyder, Characterization of Lorenz number with Seebeck coefficient measurement, APL Mater. 3, 041506 (2015) | doi:10.1063/1.4908244 | full text | Abstract and introduction: the electronic part is commonly estimated with the Wiedemann–Franz law and the degenerate-limit Lorenz number, which can be off by about 40% for non-degenerate materials; a poor choice can make the lattice value negative; an estimate of the Lorenz number from the measured Seebeck coefficient is proposed. Closing discussion: the Wiedemann–Franz law omits bipolar thermal conductivity, important in lightly doped narrow-gap materials at high temperature |
| 5 | S. Mumford, T. Paul, E. Kountz and A. Kapitulnik, Sample shape and boundary dependence of measured transverse thermal properties, J. Appl. Phys. 128, 175105 (2020); read as preprint arXiv:2007.10413 | doi:10.1063/5.0024253 | full text | Abstract and Sec. I: misaligned transverse contacts let the longitudinal gradient pollute κxy, leaving about 20 to 50% error after field antisymmetrisation and limiting small signals; differences between similar samples exceed the statistical spread; heat-flow and temperature-anchoring boundary conditions change the measured transverse response by factors of order unity for samples of similar width and length; simulation or rectangular samples recommended. Conclusion: contact method and sample shape matter in thermal Hall measurements |
| 6 | K. Behnia and H. Aubin, Nernst effect in metals and superconductors: a review of concepts and experiments, Rep. Prog. Phys. 79, 046502 (2016); read as preprint arXiv:1601.06647 | doi:10.1088/0034-4885/79/4/046502 | full text | Abstract: experiments document several sources of a Nernst signal, namely mobile quasiparticles, fluctuating Cooper pairs and mobile vortices. Sec. 5: the quasiparticle Nernst coefficient scales with mobility over Fermi energy and is large in dilute, high-mobility metals. Abstract: earlier analyses that assumed a negligible quasiparticle contribution and no fluctuation signal well above the critical temperature were contradicted by later experiments. Sec. 6: in Ginzburg–Landau theory, Cooper-pair fluctuations have no upper temperature limit and survive far above the critical temperature |
| 7 | X.-T. Zhang, Y. H. Gao and G. Chen, Thermal Hall effects in quantum magnets, Phys. Rep. 1070, 1–59 (2024); read as preprint arXiv:2305.04830 | doi:10.1016/j.physrep.2024.03.004 | full text | Sec. I (Introduction): phonons interact with magnetic excitations and complicate the longitudinal thermal conductivity; the thermal Hall conductivity is more selective, but phonons can still contribute to it through coupling to other degrees of freedom |
| 8 | E. Alleno, D. Bérardan, C. Byl, C. Candolfi, R. Daou and others, Invited Article: A round robin test of the uncertainty on the measurement of the thermoelectric dimensionless figure of merit of Co0.97Ni0.03Sb3, Rev. Sci. Instrum. 86, 011301 (2015) | doi:10.1063/1.4905250 | abstract | Abstract: one material measured in several laboratories; uncertainties rise with temperature; sample dimensions dominate the uncertainty in resistivity and diffusivity; temperature-averaged standard uncertainties of 6%, 8%, 11% and 19% for Seebeck coefficient, resistivity, thermal conductivity and zT between 300 and 700 K |
