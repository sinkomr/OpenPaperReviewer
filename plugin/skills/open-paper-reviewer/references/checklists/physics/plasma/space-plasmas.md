---
id: T-SPACE-PLASMAS
name: Space plasmas measured in situ
type: technique
field: physics/plasma
applies_when: the paper bases a claim on particle distributions, plasma moments, or magnetic or electric fields measured on board one or several spacecraft, including boundary orientations and speeds, current densities, wave properties, or statistics of events drawn from mission data
version: "0.1"
---

# Space plasmas measured in situ

In-situ measurements from spacecraft, made with particle instruments such as electrostatic analysers (ESA) and with magnetometers and electric field instruments, are used to claim the density, velocity, temperature and velocity distribution of space plasmas, the orientation, speed and thickness of boundaries, current densities, wave properties and the occurrence of events. Each of these is inferred from instruments on a charged, moving platform that samples a changing plasma at one or a few points, and is usually expressed in a named coordinate system such as geocentric solar ecliptic (GSE) or boundary-normal (LMN) coordinates.

## 1. Spacecraft potential and photoelectrons

**Question.** Does the paper state the spacecraft potential during the measurements and how it was obtained, say how particle energies were corrected for it, and show how photoelectrons from the spacecraft were removed from the low-energy electron data?

**Why it matters.** A sunlit spacecraft in the solar wind usually floats at around ten volts positive, which shifts the energies of arriving electrons and lets the spacecraft's own photoelectrons enter the electron detector; in dense plasma or in shadow it can charge negative and repel electrons whose energy is below the potential. If these effects are not corrected, electron density, temperature and velocity moments are biased, most strongly where the plasma is cold, and density errors of tens of per cent have been estimated.

**Resolved by.** The spacecraft potential given as a time series or a range, with its source (for example a probe-to-spacecraft potential or a break in the electron spectrum) and any active potential control named; measured energies shifted by the potential before moments are computed; the energy below which photoelectrons dominate stated and those data excluded or modelled; electron density compared with an independent density, such as ion density or a density from a wave cutoff.

**Benchmark.** [1], [2], [3]

## 2. Energy range, field of view and moments

**Question.** Does the paper give the energy range, angular coverage and resolution of each particle instrument as operated, show that the populations behind the claim fall inside them, and say how moments or distribution features were computed when part of the distribution was outside the field of view or below the lowest energy?

**Why it matters.** Moments are integrals over the full distribution, so a population that lies partly below the lowest energy step, or behind a heat shield, is under-counted, and a cold beam can appear hotter than it is. An electrostatic analyser cannot by itself separate species with the same energy per charge, and reduced sampling modes may rely on assumptions such as gyrotropy that a feature of interest can violate.

**Resolved by.** Energy range, angular coverage, resolution and sampling mode stated for the intervals used; the fraction of the distribution inside the instrument's coverage estimated, or the moments described as partial moments over a stated range; cold or narrow populations checked against the energy and angular resolution; species separation by time-of-flight or a stated method where heavy ions matter; assumptions of the sampling mode named and shown to hold.

**Benchmark.** [1], [2], [3]

## 3. Particle instrument calibration over the mission

**Question.** For the period analysed, how were the geometric factor and detector efficiency of the particle instruments calibrated in flight, and are densities and fluxes cross-checked against another instrument or another spacecraft?

**Why it matters.** The geometric factor depends on particle energy and arrival direction, and the efficiency of the detectors changes during a mission through radiation exposure, high fluxes and ageing. A ground calibration applied years later, or fluxes compared between spacecraft without intercalibration, can produce apparent changes or differences that are instrumental.

**Resolved by.** The calibration version of the data stated; in-flight efficiency corrections for the period described; densities compared with an independent density, for example from a plasma wave cutoff or a sounder, and agreement between instruments or spacecraft shown for the intervals used; any remaining calibration uncertainty carried into the claimed differences or trends.

**Benchmark.** [1], [3], [4], [5]

## 4. Magnetometer offsets and spacecraft fields

**Question.** How were the magnetometer offsets determined for the period analysed, how large is their uncertainty compared with the field magnitudes, differences or gradients on which the claim rests, and how were fields generated by the spacecraft handled?

**Why it matters.** Fluxgate offsets and spacecraft-generated fields add a constant or slowly drifting error to each field component, and ground calibration alone does not remove them. Because the solar wind field is usually below 10 nT, offset errors of a few tenths of a nanotesla matter; reaching that accuracy needs tens of hours of suitable data, and differences between spacecraft used for gradients and currents are limited by the offset accuracy.

**Resolved by.** The method used to determine offsets in flight (for example from Alfvénic or compressional fluctuations) and the length of data it used; the offset uncertainty stated and compared with the field values, differences or gradients that carry the claim; the handling of spacecraft fields described; intervals of possible offset drift identified.

**Benchmark.** [6], [7]

## 5. Space or time with one spacecraft

**Question.** When a single-spacecraft time series is interpreted as a spatial structure, a boundary crossing or a wavenumber spectrum, what assumption converts time into space, and does the paper show that the assumption holds for the structures and waves involved?

**Why it matters.** A single spacecraft cannot by itself tell whether a change is a structure moving past or a change in time. Converting time into distance with the flow speed (the Taylor hypothesis) fails when wave phase speeds are not small compared with the flow, as for dispersive whistler waves or slow flow near the Sun, and boundaries move with speeds that change from one crossing to the next.

**Resolved by.** The assumed structure or flow speed stated with its source; a check that wave phase speeds are small compared with the flow, or a frame transformation that does not rely on the Taylor hypothesis; boundary speed estimated for each crossing rather than assumed constant; where available, comparison with multi-spacecraft timing or other independent estimates.

**Benchmark.** [8], [9]

## 6. Multi-spacecraft gradients and timing

**Question.** When gradients, currents, boundary normals or speeds are computed from several spacecraft, does the paper give the spacecraft separation and configuration compared with the scale of the structure, state the assumptions of the method, and report a quality measure?

**Why it matters.** Timing methods assume a planar structure moving at constant velocity across the spacecraft, and gradient methods such as the curlometer assume a field that varies linearly across the configuration. When the structure is smaller than the separation, curved or changing in time, the estimated normal, speed or current can be in error.

**Resolved by.** Separation, configuration and structure scale stated together; the method's assumptions (planarity, steadiness, linear variation) named and tested; a quality indicator such as the ratio of the divergence to the curl of the field reported for current estimates; results compared between methods, such as timing and single-spacecraft variance analysis, with the spread given.

**Benchmark.** [7], [9]

## 7. Coordinate systems and reference frames

**Question.** Does the paper name and define the coordinate system and frame for each vector and distribution, say how transformations and spacecraft positions were obtained (software, version, field model), and justify any boundary-normal or field-aligned system determined from the data?

**Why it matters.** Systems with the same name are defined and implemented differently, and spacecraft positions and transformations from different sources can differ by amounts that matter for closely spaced spacecraft. A boundary-normal system found from the data rests on assumptions about the structure's dimensionality, and a frame velocity estimated with a method outside its range of validity changes which components appear in the plasma frame.

**Resolved by.** Each vector labelled with its coordinate system and each distribution with its frame; the definition, software and version, and any magnetic field model used for transformations stated, with positions given in units of kilometres or with the Earth radius defined; for data-derived systems, the method and the evidence that its assumptions hold, such as variance ratios or agreement between methods, and the uncertainty of the axes.

**Benchmark.** [3], [7], [10]

## 8. Event selection and orbital sampling

**Question.** How were the events or intervals selected (criteria, catalogue or algorithm, and who or what chose them), how do the orbits and data modes sample the regions and conditions involved, and how were occurrence rates normalised by the time spent in each region?

**Why it matters.** A spacecraft samples only the regions its orbit covers, and for limited times, so the distribution of observed events reflects the coverage as well as the physics. High-resolution data are often downlinked only for a small fraction of intervals chosen by people or automated systems with stated priorities, so a set built from such data is not a complete sample. In superposed epoch analyses, the choice of epoch and the spread of event durations shape the composite.

**Resolved by.** Selection criteria stated before the results, with the source of the event list and any data-mode restriction named; dwell time per region or condition shown and used to normalise rates; a test of whether the coverage could produce the observed distribution; for superposed epoch analyses, the epoch definition and the handling of different event durations stated, with the number of events in each bin.

**Benchmark.** [11], [12], [13]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | D. Verscharen, In-situ measurements of space plasma: recent progress and future challenges, Plasma Phys. Control. Fusion 68, 093001 (2026); read as preprint arXiv:2608.16734v2 | doi:10.1088/1361-6587/ae9ac7 | full text | Sec. 2: spacecraft floating potentials of about +10 V in the solar wind, negative in dense plasma or in shadow; positive charging shifts electron energies and negative charging repels electrons below the potential; photoelectrons contaminate low-energy electron data; mitigation by active potential control; geometric factor to be calibrated as a function of speed and arrival direction; an analyser cannot separate species of equal energy per charge. Sec. 3.1: burst mode sampling assumes gyrotropy. Sec. 3.2: a heat shield often reduces the field of view |
| 2 | V. Génot and S. J. Schwartz, Spacecraft potential effects on electron moments derived from a perfect plasma detector, Ann. Geophys. 22, 2073–2080 (2004) | doi:10.5194/angeo-22-2073-2004 | abstract | Abstract: the spacecraft potential and the lower energy cutoff bias electron density, velocity and temperature moments; the solar wind, where electrons are cold, is the region where moments are most compromised; density overestimated by up to 40% in the magnetosheath under typical operation |
| 3 | L. B. Wilson III et al., Electron energy partition across interplanetary shocks. I. Methodology and data product, Astrophys. J. Suppl. Ser. 243, 8 (2019); read as preprint arXiv:1902.01476v4 | doi:10.3847/1538-4365/ab22bd | full text | Sec. II: low-energy electron data contaminated by spacecraft photoelectrons; energies corrected for the spacecraft potential before transformation; distributions transformed to the ion rest frame with components relative to the field. Sec. III.2: distributions colder than the lowest energy step appear artificially hot; detector problems at very low and high densities; electron density constrained by ion density and the upper hybrid line from the radio receiver. Sec. III.3: detector calibration issues limit fit quality |
| 4 | A. Blagau, I. Dandouras, A. Barthe, S. Brunato, G. Facskó and V. Constantinescu, In-flight calibration of the Hot Ion Analyser on board Cluster, Geosci. Instrum. Method. Data Syst. 3, 49–58 (2014) | doi:10.5194/gi-3-49-2014 | abstract | Abstract: detection efficiency changes over time through radiation, detector ageing and changes in operating parameters, so continuous in-flight calibration is needed; calibration by comparison with densities from a sounder in the magnetosheath and solar wind |
| 5 | N. Doss, A. N. Fazakerley, B. Mihaljčić, A. D. Lahiff, R. J. Wilson, D. Kataria, I. Rozum, G. Watson and Y. Bogdanova, In-flight calibration of the Cluster PEACE sensors, Geosci. Instrum. Method. Data Syst. 3, 59–70 (2014) | doi:10.5194/gi-3-59-2014 | abstract | Abstract: electron detector efficiency declined during the mission, possibly through radiation, high fluxes and thruster firings; continuous in-flight calibration of the time-varying parameters is described as essential |
| 6 | F. Plaschke, How many solar wind data are sufficient for accurate fluxgate magnetometer offset determinations?, Geosci. Instrum. Method. Data Syst. 8, 285–291 (2019) | doi:10.5194/gi-8-285-2019 | full text | Sec. 1: offsets must be determined in flight because calibration parameters change and spacecraft fields affect them; methods based on Alfvénic and mirror-mode fluctuations; spin-axis offsets likely to drift by about 0.2 nT. Abstract and Sec. 3: about 40 h of solar wind data for 0.2 nT accuracy; drift limits accuracy whatever the amount of data. Sec. 2: solar wind intervals selected by a field magnitude below 10 nT |
| 7 | H. Hasegawa et al., Advanced methods for analyzing in-situ observations of magnetic reconnection, Space Sci. Rev. 220, 68 (2024); read as the Europe PMC full text PMC11369046 | doi:10.1007/s11214-024-01095-w | full text | Table 2 and Sec. 2.2: variance analysis for the boundary normal assumes a one-dimensional structure; de Hoffmann–Teller frame not valid inside diffusion regions; four-spacecraft timing assumes a one-dimensional, steady structure at constant velocity; gradient methods assume separation smaller than the structure scale. Sec. 2.3.2: curlometer errors arise mainly from the linear approximation; the divergence-to-curl ratio as a quality indicator. Sec. 2.2.2: a 0.1 nT magnetometer calibration error used as the minimum accuracy of field gradients |
| 8 | G. G. Howes, K. G. Klein and J. M. TenBarge, Validity of the Taylor hypothesis for linear kinetic waves in the weakly collisional solar wind, Astrophys. J. 789, 106 (2014); read as preprint arXiv:1405.5460 | doi:10.1088/0004-637X/789/2/106 | full text | Secs. II.1 to II.4: the hypothesis drops the plasma-frame frequency and holds when the flow speed along the wavevector greatly exceeds the wave phase speed; it can fail for slow flow and for dispersive waves. Secs. III.1.2 and III.2.2: kinetic Alfvén waves do not violate it, whistler waves likely do at small scales |
| 9 | S. E. Haaland et al., Four-spacecraft determination of magnetopause orientation, motion and thickness: comparison with results from single-spacecraft methods, Ann. Geophys. 22, 1347–1365 (2004) | doi:10.5194/angeo-22-1347-2004 | abstract | Abstract: four-spacecraft timing gives boundary speed, normal and thickness; properly chosen single-spacecraft methods agree on orientation but less well on speed; the boundary speed and thickness changed substantially from one crossing to the next within one event |
| 10 | R. S. Weigel, A. Y. Shih, R. Ringuette, I. Christopher, S. M. Petrinec, S. Turner, R. M. Candey, G. K. Stephens and B. Cecconi, Coordinate systems and transforms in space physics: terms, definitions, implementations, and recommendations for reproducibility, arXiv:2601.07605v6 (2026) | doi:10.48550/arXiv.2601.07605 | full text | Sec. 3: same-named systems defined differently. Sec. 4: spacecraft positions from different providers differ by up to about 1 degree, and software transforms by amounts not negligible for multi-spacecraft separations. Sec. 6: recommends stating software and version, avoiding Earth-radius units, and documenting position sources |
| 11 | A. W. Smith, C. M. Jackman, C. M. Frohmaier, J. C. Coxon, J. A. Slavin and R. C. Fear, Evaluating single-spacecraft observations of planetary magnetotails with simple Monte Carlo simulations: 1. Spatial distributions of the neutral line, J. Geophys. Res. Space Phys. 123, 10109–10123 (2018); read as the Europe PMC full text PMC6472645 | doi:10.1029/2018JA025958 | full text | Sec. 1: surveys from one spacecraft are limited by orbital coverage. Secs. 3.3 and 6: uneven orbital sampling recovers spatial distributions of structures less well, and uniform sampling recovers them best. Secs. 3.1 and 3.2: the number of orbits needed depends on the structures' extent and rate of occurrence |
| 12 | M. R. Argall et al., MMS SITL ground loop: automating the burst data selection process, Front. Astron. Space Sci. 7, 54 (2020) | doi:10.3389/fspas.2020.00054 | full text | Sec. 1: only about 4% of high-resolution data can be downlinked. Secs. 2.1 and 2.2: intervals chosen by scientists in the loop and by automated systems, with assigned priorities. Fig. 4 caption and Sec. 6.2: selectors differ in what they choose, and an automated system was trained toward particular event types |
| 13 | S. D. Walton and K. R. Murphy, Superposed epoch analysis using time-normalization: a Python tool for statistical event analysis, Front. Astron. Space Sci. 9, 1000145 (2022) | doi:10.3389/fspas.2022.1000145 | full text | Abstract and Secs. 1 and 2: superposed epoch results depend on the epoch definition; event durations vary widely, and absolute-time composites can hide patterns that time normalisation reveals; bin counts reported with the statistics |
