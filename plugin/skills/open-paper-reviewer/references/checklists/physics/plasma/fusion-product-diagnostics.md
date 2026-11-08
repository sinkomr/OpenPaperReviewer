---
id: T-FUSION-PRODUCT-DIAGNOSTICS
name: Neutron and fusion-product diagnostics
type: technique
field: physics/plasma
applies_when: the paper reports fusion neutron yield, neutron spectra, neutron time-of-flight, neutron images, activation, or charged-particle or gamma-ray fusion-product data, or infers ion temperature, areal density, fusion power or a thermonuclear origin from them
version: "0.1"
---

# Neutron and fusion-product diagnostics

## 1. Absolute calibration chain

**Question.** How was each yield detector given its absolute calibration (a source of known strength, accelerator neutrons, or cross-calibration with activation or another detector), how was that calibration transferred to the position, extent and spectrum of the plasma source, and which nuclear data, such as cross sections and branching ratios, enter the quoted yield?

**Why it matters.** Detector efficiency depends on neutron energy and on the geometry between source and detector, so a calibration made with a small source at a few positions, or with a different spectrum, holds for the plasma only through a transport calculation of the real geometry. Efficiencies of individual detector types can carry uncertainties from a few to about ten per cent, and a yield or fusion power derived from gamma rays inherits the uncertainty of the gamma-to-neutron branching ratio, which for deuterium-tritium reactions is small and has been measured only to within tens of per cent.

**Resolved by.** The calibration source, its neutron energy and its positions compared with the plasma source; the transfer from calibration to plasma geometry done by in-situ measurement or by a Monte Carlo transport model of the device; the efficiency, solid angle and nuclear-data contributions to the yield uncertainty listed; agreement shown between independent yield diagnostics; for long campaigns, stability tracked with embedded sources or reference discharges; for gamma-based yields, the branching ratio used and its uncertainty given.

**Benchmark.** [1], [2], [3], [4]

## 2. Scattered neutrons and gamma-ray background

**Question.** How large are the contributions of neutrons scattered by the vacuum vessel or target chamber, collimators, shielding and walls, and of gamma rays reaching the detector, to each detector's signal, and how were they determined and removed for each line of sight?

**Why it matters.** Scattered neutrons have lost energy and arrive late, so they fill the spectrum below the primary peak and add a tail to time-of-flight signals that can be mistaken for broadening or for down-scattering in the fuel. Their size and spectral shape differ between lines of sight, attenuation and scattering in the surroundings and in the sample itself can change an activation detector's sensitivity by tens of per cent compared with an ideal geometry, and most neutron detectors also respond to gamma rays, such as those from neutron capture in nearby structures.

**Resolved by.** Collimation and shielding of each line of sight described; the scattered contribution computed with a transport model of the actual surroundings and checked against measurement; the ratio of direct to scattered signal quoted for each detector; threshold reactions or energy cuts chosen to suppress scattered neutrons where possible; neutron and gamma signals separated by pulse shape, timing or kinematic cuts, with the remaining gamma contribution estimated; spectral fits that include the scattered component explicitly.

**Benchmark.** [1], [2], [4], [5], [7]

## 3. Thermonuclear or non-thermal origin

**Question.** Before the yield or spectrum is used to infer an ion temperature or thermonuclear performance, does the paper show that the neutrons come from a thermal ion population, and not from beam-target, beam-thermal or other reactions involving fast ions?

**Why it matters.** Ions accelerated by fields, heating beams or radio-frequency heating produce neutrons with spectra that are not Gaussian, depend on the direction of emission relative to the field or axis and can peak below the thermal peak; they add to the yield and distort the width from which a temperature is read. The spectrum from field-accelerated ions depends on the fields at the time of emission, and magnetized fast ions can emit almost isotropically, so isotropy alone does not show that the emission is thermal.

**Resolved by.** Spectra measured at more than one angle to the field or axis; the measured spectrum compared with forward models of thermal and non-thermal components computed from measured or modelled ion distributions; the thermal fraction of the yield stated with its uncertainty; the yield shown to be consistent with the inferred temperature and density; the claim worded as fusion yield, not thermonuclear yield, until the origin is established.

**Benchmark.** [4], [6]

## 4. Instrument response and spectral fitting

**Question.** How was the response function of each spectrometer or time-of-flight detector measured, including detector, cables and recorder, how was it included in the fit, was it valid at the count rates of the experiment, and does the inferred width depend on the fitting function, the fit range or the unfolding method?

**Why it matters.** A recorded signal is the emission spectrum convolved with the detector response and, for time-of-flight, with the emission history, so an error in the assumed response passes directly into the width and hence the temperature. The temperature obtained from time-of-flight data can depend strongly on the fitting or unfolding method, and the response itself can change with neutron energy, gain, temperature, radiation damage and count rate, where pile-up and random coincidences also distort the spectrum.

**Resolved by.** The response measured with monoenergetic neutrons, calibrated sources or short pulses and supported by simulation; the energy resolution stated and compared with the thermal broadening expected; forward fitting of a modelled spectrum convolved with the response, not deconvolution alone; the result shown to be stable against changes of fit range and model; gain and energy scale monitored during the campaign; count rates stated, with pile-up, random coincidences or gain shifts at those rates shown to be small or corrected.

**Benchmark.** [1], [4], [5], [7], [10]

## 5. From spectral width to ion temperature

**Question.** Is a temperature obtained from the width of a neutron peak presented as an apparent, emission-weighted value, and does the paper assess the broadening from bulk flows, non-thermal ions and averaging along the line of sight and over time before treating it as the thermal ion temperature?

**Why it matters.** The width reflects the spread of centre-of-mass velocities of the reacting ions, and bulk fluid motion of comparable speed broadens the peak further, so the inferred temperature can be too high, and differently so for deuterium-deuterium and deuterium-tritium neutrons from the same plasma. The value is also weighted towards the regions and times of strongest emission, and a single line of sight cannot separate thermal from directed motion.

**Resolved by.** The quantity labelled as an apparent or burn-averaged temperature; widths and peak shifts compared between several lines of sight; deuterium-deuterium and deuterium-tritium temperatures compared where both are measured; the size of flow broadening estimated with synthetic diagnostics from simulations; any claim about the thermal temperature or yield consistency made with this broadening allowed for.

**Benchmark.** [4], [8], [9], [10]

## 6. Areal density from scattered neutrons and activation

**Question.** Which model converts the down-scattered ratio, scattered-neutron spectra or activation measurements around the source into an areal density, what are its assumptions and model uncertainty, and are asymmetry and the velocity of the emitting region accounted for?

**Why it matters.** The conversion from down-scattered ratio to areal density rests on fits to model spectra and on a single-scattering approximation that loses accuracy as areal density grows, and one line of sight samples a cone of scattering angles that can understate a large asymmetry. Motion of the emitting region shifts the neutron energy with viewing angle, which changes activation cross sections and fluence and can produce an apparent areal-density asymmetry where the fuel areal density is negligible.

**Resolved by.** The conversion model and its assumptions stated, with the model contribution to the uncertainty; several lines of sight or activation positions used for asymmetry; a velocity correction, using velocities measured by time-of-flight, applied before activation anisotropy is read as areal-density asymmetry; the method tested on simulated diagnostics or on a calibration shot of low areal density.

**Benchmark.** [9], [10], [11]

## 7. Charged-particle spectra

**Question.** For charged fusion products, how was the detector, for example a CR-39 track detector behind magnets or ranging filters, calibrated for particle type and energy, and how were energy shifts from electric fields around the target separated from energy loss in the target before an areal density or stopping power is inferred?

**Why it matters.** An areal density from charged particles comes from the downshift of their energy through a stopping-power model, but particles emitted while the target is charged can be accelerated by electrostatic fields in the surrounding plasma, so the measured shift mixes gain and loss. A track detector identifies particle type and energy only through a calibrated response.

**Resolved by.** The detector response calibrated with accelerator beams or particles of known energy; the timing of emission relative to the drive stated; several particle species or emission times used to separate acceleration from energy loss; the stopping-power model named and its uncertainty carried into the areal density.

**Benchmark.** [12], [13]

## 8. Neutron images

**Question.** Does the paper give the resolution and response function of the neutron imager (aperture, its alignment, converter and detector), the reconstruction method, how neutrons were separated from x-rays and gamma rays, and which neutron energies each image represents?

**Why it matters.** A neutron image is a line integral of the emission, attenuated by scattering and blurred by the aperture and detector response, so sizes and shapes near the resolution depend on how the response was characterized and the source reconstructed. Images integrated over energy mix primary and scattered neutrons, which carry different information, and x-ray and gamma-ray background on the detector must be removed.

**Resolved by.** Response functions and resolution measured or simulated for the actual aperture and detector; the reconstruction method and its tests described; features compared with the resolution before they are interpreted; energy-gated primary and scattered images separated where the claim needs them; images from more than one line of sight where three-dimensional shape is claimed.

**Benchmark.** [9], [14]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Cecconello et al., Strategy and guidelines for the calibration of the ITER radial neutron camera, arXiv:1810.08582 (2018); read on ar5iv; the arXiv record misspells the first author as Cecconelloa | doi:10.48550/arXiv.1810.08582 |
| 2 | K. D. Hahn et al., Fusion-neutron-yield, activation measurements at the Z accelerator: Design, analysis, and sensitivity, Rev. Sci. Instrum. 85, 043507 (2014); abstract read from the Crossref record | doi:10.1063/1.4870779 |
| 3 | Y. Kim et al., Determination of the deuterium-tritium branching ratio based on inertial confinement fusion implosions, Phys. Rev. C 85, 061601(R) (2012); abstract read on the APS journal page | doi:10.1103/PhysRevC.85.061601 |
| 4 | G. Ericsson, Advanced neutron spectroscopy in fusion research, J. Fusion Energy 38, 330 (2019) | doi:10.1007/s10894-019-00213-9 |
| 5 | Z. Chen et al., The effect of scattered neutrons on the ion temperature measurement with different line-of-sight on the SGIII laser facility, AIP Adv. 9, 015124 (2019); abstract read from the Crossref record | doi:10.1063/1.5064611 |
| 6 | B. Appelbe and J. Chittenden, Neutron spectra from beam-target reactions in dense Z-pinches, Phys. Plasmas 22, 102703 (2015); abstract read from the Crossref record | doi:10.1063/1.4933117 |
| 7 | T. J. Murphy et al., Interpretation of neutron time-of-flight signals from current-mode detectors, Rev. Sci. Instrum. 68, 610 (1997); abstract read from the Crossref record | doi:10.1063/1.1147763 |
| 8 | T. J. Murphy, The effect of turbulent kinetic energy on inferred ion temperature from neutron spectra, Phys. Plasmas 21, 072701 (2014); abstract read from the Crossref record | doi:10.1063/1.4885342 |
| 9 | A. J. Crilly et al., Synthetic nuclear diagnostics for inferring plasma properties of inertial confinement fusion implosions, Phys. Plasmas 25, 122703 (2018); read as preprint arXiv:1807.03087 on ar5iv | doi:10.1063/1.5027462 |
| 10 | R. Hatarik et al., Analysis of the neutron time-of-flight spectra from inertial confinement fusion experiments, J. Appl. Phys. 118, 184502 (2015); abstract read from the Crossref record | doi:10.1063/1.4935455 |
| 11 | H. G. Rinderknecht et al., Velocity correction for neutron activation diagnostics at the NIF, Rev. Sci. Instrum. 89, 10I125 (2018); abstract read from the Crossref record | doi:10.1063/1.5038734 |
| 12 | F. H. Séguin et al., Spectrometry of charged particles from inertial-confinement-fusion plasmas, Rev. Sci. Instrum. 74, 975 (2003); abstract read from the Crossref record | doi:10.1063/1.1518141 |
| 13 | D. G. Hicks et al., Charged-particle acceleration and energy loss in laser-produced plasmas, Phys. Plasmas 7, 5106 (2000); abstract read from the Crossref record | doi:10.1063/1.1320467 |
| 14 | J. D. Vaughan et al., Modeling the one-dimensional imager of neutrons (ODIN) for neutron response functions at the Sandia Z facility, Rev. Sci. Instrum. 89, 10I121 (2018); abstract read from the Crossref record | doi:10.1063/1.5039366 |
