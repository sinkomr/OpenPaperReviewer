---
id: T-MICROFLUIDICS
name: Microfluidics
type: technique
field: physics/soft-matter
applies_when: the paper reports flows, transport, droplets, particles, cells or reactions in microfluidic or nanofluidic channels, including polydimethylsiloxane or other polymer devices, pressure- or electrokinetically driven flow, or bases a claim on slip, surface charge or behaviour that depends on channel size
version: "0.1"
---

# Microfluidics

Microfluidic and nanofluidic experiments are used to claim flow fields, transport rates, droplet and particle behaviour, slip at walls, electrokinetic effects and the response of cells or chemicals in confined liquid. These claims rest on the channel dimensions, the delivered flow or field, and the state of the walls, often in devices of polydimethylsiloxane (PDMS), a soft, gas-permeable silicone elastomer.

## 1. Channel geometry as built and under pressure

**Question.** Are the channel height and width measured on the devices or moulds actually used, not only taken from the design, and for soft-walled devices is the change in cross-section at the operating pressure measured or estimated?

**Why it matters.** In a shallow channel the flow rate at a given pressure drop scales with the cube of the height, so a small error in height becomes a large error in flow rate, shear rate or an inferred viscosity. PDMS walls bulge under pressure, so the cross-section varies along the channel, the pressure-flow relation becomes nonlinear, and the size of the effect depends on wall thickness and elastic modulus.

**Resolved by.** Height and width measured, for example by profilometry or cross-section imaging, with their spread across devices; wall thickness and elastic modulus stated; the deformation measured under flow, for example by fluorescence or confocal imaging, or estimated with a model and shown to be small over the pressures used; the pressure-flow relation shown to be linear over the operating range, or its nonlinearity included in the analysis.

**Benchmark.** [1], [2]

## 2. Flow rate and pressure as delivered

**Question.** Does the paper state how the flow was driven, whether the flow rate in the device was measured or the pump calibrated rather than taken from the set point, how long the system was left to settle, and how steady the flow was?

**Why it matters.** The pump set point is not the flow in the channel. Calibrations of syringe pumps show errors from the set value that grow at low flow rates, and oscillations of the pump motor cause flow fluctuations that become pressure fluctuations in elastic channels. The compliance of channels and tubing both damps these fluctuations and sets the time for inflating channels to reach a steady state, and droplet size, interface position and shear rate follow the actual flow.

**Resolved by.** The driving method, syringe size and tubing stated; flow rate measured in the device or at its outlet (flow sensor, weighing, velocimetry) or the pump calibrated at the flow rates used, with an uncertainty; the size of flow or pressure fluctuations reported; the waiting time before data were taken and evidence of a steady state; the result unchanged when the drive or tubing is changed.

**Benchmark.** [2], [3], [4], [5]

## 3. Boundary condition at the wall

**Question.** When a claim rests on slip, flow enhancement or velocity close to a wall, does the paper fix the wall position independently, characterise roughness, wettability, dissolved gas and contamination, and compare the slip length with the channel size and the resolution of the measurement?

**Why it matters.** Reported slip lengths range from nanometres to micrometres and often disagree for similar systems. Apparent slip can arise from roughness, surface-attached gas, impurities, error in locating the wall and charged tracer particles. Slip changes the flow by an amount of order the slip length over the channel size, so it is likely to matter little in channels wider than tens of micrometres.

**Resolved by.** Slip obtained from a local velocity profile near the wall, with the wall position found by an independent method; roughness and contact angle reported; measurements repeated with degassed liquid and cleaned surfaces; the uncertainty in channel size carried into the inferred slip; the value compared with what is expected for the surface, which is close to zero for water on hydrophilic walls and tens of nanometres on smooth hydrophobic ones.

**Benchmark.** [6], [7]

## 4. Surface charge, wettability and their stability

**Question.** Are the wall material, surface treatment and liquid composition stated, and is the surface property the result depends on, such as zeta potential, electro-osmotic mobility or contact angle, measured under the conditions of the experiment and at the time of use?

**Why it matters.** The zeta potential of a wall depends on ionic strength, pH, counter-ion valency and temperature, and data for polymer substrates are sparse and for at least one common polymer poorly repeatable, so values taken from the literature may not fit the device. Treated PDMS recovers its hydrophobicity over time, which changes wetting, adsorption and electro-osmotic flow. In nanochannels and at low salt, conduction through the surface charge can exceed that of the bulk liquid, so the surface state controls the result.

**Resolved by.** Buffer composition, pH and ionic strength stated; zeta potential or electro-osmotic mobility measured in the device material under the experimental conditions; contact angle measured, with the time between surface treatment and use stated and controlled; for nanofluidic claims, surface conduction considered by comparing the channel size with the Dukhin length, the ratio of surface charge to bulk salt concentration.

**Benchmark.** [7], [8], [9], [10]

## 5. Absorption into and leaching from the device material

**Question.** When small molecules such as drugs, hormones, dyes or other hydrophobic solutes are used in PDMS or other polymer devices, does the paper measure or bound their loss into the walls and the release of uncured material into the liquid?

**Why it matters.** PDMS takes up hydrophobic small molecules, so their concentration in solution can fall substantially; the loss can be most of the solute and is not necessarily prevented by pre-soaking the device in it. Uncured oligomers leach into the liquid, can enter cell membranes and remain after solvent extraction of the device. Dyes that enter the walls also distort fluorescence-based measurements of concentration or temperature.

**Resolved by.** Solute concentration measured in the channel or at the outlet over the duration of the experiment; the same experiment run in a device of a material that does not absorb, such as glass or polystyrene, or in a well plate; any coating, extraction or pre-treatment described and shown to work; fluorescence measurements corrected for dye uptake or made with the dye kept out of contact with the walls.

**Benchmark.** [11], [12], [13]

## 6. Exchange through permeable walls and bubbles

**Question.** Over the duration of the experiment, does the paper account for the exchange of water and gas through permeable walls and open reservoirs, and say how bubbles were prevented or detected?

**Why it matters.** Water permeating into dry PDMS drives flows of more than ten micrometres per second in shallow channels, concentrates solutes over an hour and can persist for hours, so a liquid meant to be stagnant or slowly flowing may not be. Bubbles nucleate on surface defects and from gas-supersaturated liquid, especially where pressure or temperature changes, and change the flow resistance and the flow.

**Resolved by.** PDMS pre-soaked or coated, temperature and humidity stated and reservoir levels maintained; residual flow measured under nominally stagnant conditions; liquids degassed or bubble traps used; images showing the region of interest free of bubbles during the measurement.

**Benchmark.** [14], [15]

## 7. Temperature and Joule heating

**Question.** Where electric fields, heaters, strong illumination or high shear are present, is the temperature of the liquid in the channel measured or estimated, and are temperature-dependent properties taken into account?

**Why it matters.** Joule heating in electrokinetic flow raises the liquid temperature and makes it non-uniform, and because viscosity, conductivity and other properties depend on temperature it disturbs the flow, electric and concentration fields. The low thermal conductivity of PDMS impedes heat loss through the substrate, so an all-PDMS chip can reach a much higher temperature than one bonded to glass, with a marked change in flow rate.

**Resolved by.** The current and dissipated power reported; the temperature measured in the channel, for example by calibrated fluorescence thermometry, with its precision and spatial resolution; chip materials and thermal contact with the stage stated; properties such as viscosity and conductivity evaluated at the measured temperature.

**Benchmark.** [16], [17], [18]

## 8. From one device to others

**Question.** Does the paper state the dimensionless groups that govern the result, such as the Reynolds, Péclet, capillary and Weissenberg numbers and the ratios of slip, Debye or Dukhin lengths to the channel size, test more than one device or geometry, and limit its general claims to the range covered?

**Why it matters.** Which physical effects dominate at this scale depends on these groups, and boundaries have a strong influence. Slip, surface conduction and wall deformation each enter through a ratio to the channel size or wall thickness, so the same experiment in a device of another size, material or surface state can give a different answer.

**Resolved by.** The relevant dimensionless numbers given for each data set; results from more than one device and fabrication batch, with the spread between devices shown; dependence on channel size or wall material tested where a claim is meant to be general; general statements expressed in dimensionless terms, with the range covered.

**Benchmark.** [1], [6], [7], [19]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | I. C. Christov, V. Cognet, T. C. Shidhore and H. A. Stone, Flow rate–pressure drop relation for deformable shallow microfluidic channels, J. Fluid Mech. 841, 267–286 (2018); read as preprint arXiv:1712.02687 | doi:10.1017/jfm.2018.30 | full text | Introduction: PDMS channels depart from their moulded cross-section under flow, and because flow rate scales with height cubed modest deformation has large effects, giving a nonlinear pressure-flow relation. Fig. 5 caption and Sec. 6, Eq. 27: rigid result with flow rate proportional to height cubed; correction grows with the cube of width over wall thickness and with pressure over Young's modulus; earlier models needed a fitted parameter for each channel |
| 2 | I. C. Christov, Soft hydraulics: from Newtonian to complex fluid flows through compliant conduits, J. Phys.: Condens. Matter 34, 063001 (2022); read as preprint arXiv:2106.07164 | doi:10.1088/1361-648X/ac327d | full text | Secs. 2 and 3: in a soft conduit the hydraulic resistance depends on pressure, and measured channel heights rise with pressure drop by up to about 12% in cited experiments; deformation measured by calibrated fluorescence imaging. Sec. 5.2: for compliant channels it is important to quantify the time scale of inflation and deflation |
| 3 | E. Batista, R. F. Martins, V. Silverio and I. Godinho, Advancing calibration techniques for accurate micro and nanoflow measurements, Front. Nanotechnol. 7, 1600426 (2025) | doi:10.3389/fnano.2025.1600426 | full text | Introduction: micro- and nanoflow instruments lack established calibration protocols and traceability. Results, Table 5: syringe-pump errors within about 2% from 10 to 1000 µL/h, rising to about 8% by gravimetry and interferometry at 1 µL/h. Sec. 2.5: syringe inner diameter is critical to the delivered flow and was measured gravimetrically |
| 4 | W. Zeng, I. Jacobi, D. J. Beck, S. Li and H. A. Stone, Characterization of syringe-pump-driven induced pressure fluctuations in elastic microchannels, Lab Chip 15, 1110–1115 (2015) | doi:10.1039/c4lc01347f | abstract | Abstract (Princeton research portal record): pressure fluctuations in syringe-pump-driven microchannels come from flow-rate fluctuations caused by mechanical oscillations of the pump motor; their normalised amplitude depends on pump frequency, channel geometry and wall elasticity, through one dimensionless parameter |
| 5 | A. Kalantarifard, E. Alizadeh Haghighi and Ç. Elbüken, Damping hydrodynamic fluctuations in microfluidic systems, Chem. Eng. Sci. 178, 238–247 (2018) | doi:10.1016/j.ces.2017.12.045 | abstract | Abstract (Bilkent repository record): flow sources introduce fluctuations; elastomeric off-chip tubing damps them, and off-chip compliance matters most for displacement-pump systems; modelled with electrical circuit analogies |
| 6 | E. Lauga, M. P. Brenner and H. A. Stone, Microfluidics: the no-slip boundary condition, chapter 19 in Springer Handbook of Experimental Fluid Mechanics, eds. C. Tropea, A. L. Yarin and J. F. Foss (2007); read as arXiv:cond-mat/0501557 (2005) | doi:10.48550/arXiv.cond-mat/0501557 | full text | Sec. 2.4 and Tables 1–4: reported slip lengths from about a nanometre to micrometres, with conflicting results for similar systems. Secs. 5.1, 5.2 and 5.5: roughness (which also makes the surface position ambiguous), dissolved gas and nanobubbles, contamination and charged tracers can each produce apparent slip. Sec. 3.1, Eq. 4: the flow increase varies with slip length over system size. Sec. 6: impact likely limited above tens of microns; reproducing experiments in degassed, clean conditions suggested |
| 7 | L. Bocquet and E. Charlaix, Nanofluidics, from bulk to interfaces, Chem. Soc. Rev. 39, 1073–1095 (2010); read as preprint arXiv:0909.0628 | doi:10.1039/B909366B | full text | Sec. III, slip: water does not slip on hydrophilic surfaces and slips by up to about 20–30 nm on hydrophobic ones; particle velocimetry is biased by errors in locating the wall. Sec. IV.3, surface versus bulk conductance: Dukhin length defined as surface charge over bulk salt concentration; surface conduction dominates in channels narrower than it, and it reaches micrometres at low salt. Sec. II.3: Debye, Dukhin and slip lengths lie in the nanometre to tens-of-nanometres range, so surface effects offer most room |
| 8 | B. J. Kirby and E. F. Hasselbrink, Zeta potential of microfluidic substrates: 1. Theory, experimental techniques, and effects on separations, Electrophoresis 25, 187–202 (2004) | doi:10.1002/elps.200305754 | abstract | Abstract (Europe PMC record, PMID 14743473): zeta potential depends on cation concentration, buffer and cation type, pH, cation valency and temperature; the Debye-Hückel approximation can lead to serious errors when extended to counter-ion concentration dependence |
| 9 | B. J. Kirby and E. F. Hasselbrink, Zeta potential of microfluidic substrates: 2. Data for polymers, Electrophoresis 25, 203–213 (2004) | doi:10.1002/elps.200305755 | abstract | Abstract (Europe PMC record, PMID 14743474): zeta potential data for polymer substrates are sparse; normalising by counter-ion concentration brings studies together, with encouraging repeatability except for PMMA |
| 10 | J. Zhou, A. V. Ellis and N. H. Voelcker, Recent developments in PDMS surface modification for microfluidic devices, Electrophoresis 31, 2–16 (2010) | doi:10.1002/elps.200900475 | abstract | Abstract (Europe PMC record): PDMS is hydrophobic and recovers its hydrophobicity quickly after surface treatment, which degrades device performance; longer-lasting modifications are reviewed |
| 11 | M. W. Toepke and D. J. Beebe, PDMS absorption of small molecules and consequences in microfluidic applications, Lab Chip 6, 1484–1486 (2006) | doi:10.1039/b612140c | abstract | Abstract (Europe PMC record, PMID 17203151): partitioning of hydrophobic small molecules into PDMS can change solution concentrations significantly and could alter experimental outcomes |
| 12 | K. J. Regehr, M. Domenech, J. T. Koepsel, K. C. Carver, S. J. Ellison-Zelski, W. L. Murphy, L. A. Schuler, E. T. Alarid and D. J. Beebe, Biological implications of polydimethylsiloxane-based microfluidic cell culture, Lab Chip 9, 2132–2139 (2009) | doi:10.1039/b903043c | abstract | Abstract (Europe PMC record, PMID 19606288): estrogen in microchannel media partitioned rapidly into the PDMS, at about a 9:1 ratio, and serum blocking or 24 h pre-absorption did not change the loss; uncured oligomers found in channel media before and after Soxhlet extraction and in plasma membranes of cells cultured in the channels |
| 13 | R. Samy, T. Glawdel and C. L. Ren, Method for microfluidic whole-chip temperature measurement using thin-film poly(dimethylsiloxane)/rhodamine B, Anal. Chem. 80, 369–375 (2008) | doi:10.1021/ac071268c | abstract | Abstract (Europe PMC record): rhodamine B adsorbing into or absorbing into PDMS channels gives false intensity readings in temperature measurement; a separate dye film avoids this |
| 14 | G. C. Randall and P. S. Doyle, Permeation-driven flow in poly(dimethylsiloxane) microfluidic devices, Proc. Natl. Acad. Sci. USA 102, 10813–10818 (2005); read through PubMed Central (PMC1182434) | doi:10.1073/pnas.0503287102 | full text | Abstract and Results: water permeating into PDMS drives flows above 10 µm/s, faster in shallower channels, and can give steady velocities for several hours. Applications: fluorescein concentrated about 15-fold in 60 min. Discussion: soaking the PDMS in water suppressed the flow for up to about 2 h; reservoirs refilled about every 2 h |
| 15 | I. Pereiro, A. Fomitcheva Khartchenko, L. Petrini and G. V. Kaigala, Nip the bubble in the bud: a guide to avoid gas nucleation in microfluidics, Lab Chip 19, 2296–2314 (2019) | doi:10.1039/c9lc00211a | abstract | Abstract (Europe PMC record): bubbles are a common obstacle in microfluidics, nucleating from surface nuclei and gas supersaturation; prevention by design, bubble traps and control of gas saturation under pressure and temperature gradients |
| 16 | X. Xuan, Joule heating in electrokinetic flow, Electrophoresis 29, 33–43 (2008) | doi:10.1002/elps.200700302 | abstract | Abstract (Europe PMC record): Joule heating is unavoidable in electrokinetic flow; because material properties depend on temperature, the resulting temperature variations disturb electric, flow and concentration fields |
| 17 | D. Erickson, D. Sinton and D. Li, Joule heating and heat transfer in poly(dimethylsiloxane) microfluidic systems, Lab Chip 3, 141–149 (2003) | doi:10.1039/b306158b | abstract | Abstract (Europe PMC record, PMID 15100765): microscale thermometry and a whole-chip model show a nearly fivefold higher maximum buffer temperature in PDMS/PDMS than PDMS/glass chips at high field, because a PDMS substrate impedes heat loss through it; the higher temperature nearly doubled the flow rate |
| 18 | D. Ross, M. Gaitan and L. E. Locascio, Temperature measurement in microfluidic systems using a temperature-dependent fluorescent dye, Anal. Chem. 73, 4117–4123 (2001) | doi:10.1021/ac010370l | abstract | Abstract (Europe PMC record): fluorescence thermometry maps Joule heating in electrokinetically pumped channels with micrometre spatial and millisecond time resolution, temperatures up to 90 °C and precision of 0.03 to 3.5 °C depending on averaging |
| 19 | T. M. Squires and S. R. Quake, Microfluidics: fluid physics at the nanoliter scale, Rev. Mod. Phys. 77, 977–1026 (2005) | doi:10.1103/RevModPhys.77.977 | abstract | Abstract (Caltech repository record): the physics is organised by dimensionless numbers, including Re, Pe, Ca and Wi, expressing the relative importance of physical effects; because viscous flows act over long range and devices are small, the influence of boundaries is typically significant |
