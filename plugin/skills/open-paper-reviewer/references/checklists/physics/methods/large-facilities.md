---
id: T-LARGE-FACILITIES
name: Measurements at large facilities
type: technique
field: physics/methods
applies_when: the paper reports data taken at a synchrotron, neutron source, X-ray free-electron laser (XFEL) or high-field magnet laboratory, such as scattering, diffraction, absorption spectroscopy or pulsed-field measurements, and bases a claim on them
version: "0.1"
---

# Measurements at large facilities

Measurements at synchrotrons, neutron sources (reactors and spallation sources), X-ray free-electron lasers (XFELs) and high-field magnet laboratories are used to claim structures, spectra, excitations and field-induced states that laboratory instruments cannot reach. The data come from short allocations of beamtime or magnet time on instruments run by the facility, with intense probes, facility-built corrections and reduction software, and little room to repeat a measurement.

## 1. Beam damage and dose

**Question.** Does the paper state the dose or exposure the sample received, and does it show that the features a claim rests on do not change with accumulated exposure?

**Why it matters.** Intense X-ray beams change the samples they measure. The damage follows the absorbed dose, not the exposure time, and changes at particular sites, such as metal and heavy-atom sites, can set in at much lower dose than any visible loss of overall signal. A spectrum or structure taken late in an exposure may then describe a sample that the beam has already altered.

**Resolved by.** The dose estimated from flux, beam size, photon energy and sample composition, for example with a dose calculator, and compared with known damage thresholds for that kind of sample; successive exposures or frames compared and shown to agree, or early and late data analysed separately; any measures taken to limit damage, such as shorter exposures, moving the beam to fresh regions or crystals, or radical scavengers, reported.

**Benchmark.** [1], [2]

## 2. Sample temperature and field in pulsed magnets

**Question.** For measurements in pulsed magnetic fields, how was the field at the sample calibrated, and does the paper show that the sample temperature during the pulse is the temperature it quotes?

**Why it matters.** The quoted temperature is usually the one recorded before the pulse. In a conducting sample the rapidly changing field drives eddy currents whose heating grows with the square of the sweep rate and with the sample's cross-section and conductivity, so the sample can be warmer during the pulse than the quoted value. The field itself is inferred from the voltage induced in a pick-up coil, whose calibration has a limited range of validity.

**Resolved by.** The method used to calibrate the field, such as a pick-up coil checked against a reference coil or an optical standard such as Faraday rotation, with its range of validity; an estimate of eddy-current heating from the sweep rate, sample size and conductivity, or a measurement of the temperature near the sample; rising and falling parts of the pulse compared, so that heating or relaxation shows as a difference between them; sample geometry chosen to reduce the cross-section normal to the field.

**Benchmark.** [3]

## 3. The sample and the region the beam sees

**Question.** What part of the sample did the beam illuminate (spot size, footprint, penetration depth, number of grains or crystals), was the measured specimen characterised by independent means, and did it stay the same during the measurement?

**Why it matters.** A facility measurement reports an average over the illuminated volume, which may be a small spot, a near-surface layer or a few grains, and it carries no information about the parts of the sample the beam did not reach. A measurement on one specimen in a short allocation can therefore stand for less of the material than the claim implies, and a sample that moves, settles or degrades during the measurement changes the quantity being averaged.

**Resolved by.** Beam size at the sample, footprint and probing depth stated and compared with the sample size and with the scale of the structure claimed; the specimen characterised by methods independent of the facility measurement, such as purity, composition or monodispersity checks, and identified as the same batch or piece; transmission or flux monitored throughout and repeated measurements in sequence shown to agree; more than one spot, specimen or orientation measured where the claim concerns the material as a whole.

**Benchmark.** [2], [4]

## 4. Instrument resolution

**Question.** Does the paper state the instrument resolution (in momentum, energy or wavelength, and the beam divergence and size), and is it included in the analysis wherever the width or shape of a feature carries the claim?

**Why it matters.** Every measured profile is the true signal convolved with the instrument resolution. Broad wavelength bands and large beams, as in many neutron instruments, smear the data significantly, and removing that smearing from the data amplifies noise and can create artefacts. A width, a lineshape or the absence of a feature means little without the resolution beside it.

**Resolved by.** The resolution stated for the configuration used, with how it was determined (calculated or measured on a reference sample); models smeared with the measured resolution and fitted to the data, rather than the data desmeared; where data were desmeared, the method stated and the original data made available; claimed widths compared with the resolution.

**Benchmark.** [2], [4]

## 5. Background and unwanted beam components

**Question.** How was the background measured and subtracted: was it taken with the same sample environment, container, geometry and corrections as the sample, how large was it compared with the signal, and was the beam free of unwanted radiation accompanying the intended beam?

**Why it matters.** At large facilities the sample usually sits in a container or sample environment, such as a capillary, cryostat, pressure cell or magnet, that scatters or absorbs as much as the sample, and the background also includes detector dark current and natural background. A background measured in a different configuration, or a subtraction that is large compared with the signal, can create or remove features. Unwanted radiation accompanying the intended beam distorts measured amplitudes in a way that depends on sample thickness.

**Resolved by.** An empty-container or solvent-only measurement made in the same geometry and with the same corrections, repeated whenever the geometry, container or solvent changed; dark-current measurements stated; the size of the background and of any ad hoc correction to it reported, with the raw sample and background curves shown together; sample thickness chosen to avoid amplitude distortion, and the measures used to suppress unwanted radiation in the beam stated.

**Benchmark.** [2], [4], [5]

## 6. Normalization to beam intensity

**Question.** To what were the data normalized: which monitor measured the incident intensity, how was transmission measured, and, where absolute intensities are claimed, against which standard were they calibrated?

**Why it matters.** The incident flux at a facility changes during and between measurements, and XFEL pulses vary from one pulse to the next in beam position and size, in ways that averages over a pulse train underestimate. Intensities compared between samples, temperatures or runs are only as good as the normalization, and absolute scales rest on a calibration standard and its own uncertainty.

**Resolved by.** The monitor type and position stated, with normalization by monitor counts or time named; transmission measured for each sample and the method given; absolute calibration against a named standard with the calibration factor reported; for XFELs, per-pulse beam diagnostics used where pulse-to-pulse variation could affect the result.

**Benchmark.** [2], [4], [6]

## 7. Facility software and corrections

**Question.** Which reduction software and version produced the reduced data, which corrections did it apply with which parameters, and was the reduction checked by the authors rather than taken as given?

**Why it matters.** Converting raw detector counts into physical units at a facility relies on instrument-specific knowledge built into facility software: instrument geometry, detector efficiency, and corrections such as flat field, dead time, polarization and solid angle. Users often run this reduction as supplied, so its choices and defaults enter the result without appearing in the paper, and the software changes from one release to the next.

**Resolved by.** The reduction software and version named, with each correction and its parameters listed, for example as a recorded processing history or script; the instrument definition or calibration files identified; analysis and modelling software and versions named; reduced data checked against a reference sample or a known result measured in the same session.

**Benchmark.** [2], [4], [7], [8]

## 8. Instrument configuration reported

**Question.** Does the paper give the facility, instrument and configuration used for each data set: source type, wavelength or energy and its spread, collimation, beam size, detector and sample-to-detector distance, measured range, counting or exposure times, and sample environment conditions?

**Why it matters.** Facility instruments are reconfigured between experiments and between runs within one experiment, and each configuration changes resolution, range, background and corrections. Without it a reader cannot judge which artefacts could be present, and the measurement cannot be repeated, often on a different instrument.

**Resolved by.** A table of instrument settings for each data set, of the kind community reporting guidelines set out; sample environment conditions such as temperature, pressure, field and cell type stated; raw data and metadata kept in a self-describing facility format that records the instrument state with each measurement.

**Benchmark.** [2], [4], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | J. M. Holton, A beginner's guide to radiation damage, J. Synchrotron Rad. 16, 133–142 (2009) | doi:10.1107/S0909049509004361 | full text | Sec. 3: dose is absorbed energy per mass, not incident energy, and damage follows it. Sec. 4: global damage (fading high-angle diffraction) and specific chemical damage, which can proceed up to about 60 times faster and affects active, ligand and heavy-atom sites; a general limit of 30 MGy from earlier work, and much lower doses reported for specific damage. Sec. 10: metal sites can break down far faster than spot intensities decay. Secs. 3, 6 and 11: dose estimated with RADDOSE. Secs. 4 and 11: rising scaling B factor as a sign of damage. Sec. 11: falling anomalous signal, limited exposure time, early and late data treated separately. Secs. 10 and 11: dose spread over fresh regions or several crystals. Sec. 8: radical scavengers |
| 2 | J. Trewhella, A. P. Duff, D. Durand, F. Gabel, J. M. Guss, W. A. Hendrickson, G. L. Hura, D. A. Jacques, N. M. Kirby, A. H. Kwan, J. Pérez, L. Pollack, T. M. Ryan, A. Sali, D. Schneidman-Duhovny, T. Schwede, D. I. Svergun, M. Sugiyama, J. A. Tainer, P. Vachette, J. Westbrook and A. E. Whitten, 2017 publication guidelines for structural modelling of small-angle scattering data from biomolecules in solution: an update, Acta Cryst. D 73, 710–728 (2017) | doi:10.1107/S2059798317011597 | full text | Table 1 (Sec. 2.1): sample source, purity, composition, concentration method, solvent blank and monodispersity checks independent of scattering. Table 2 (Sec. 2.2): report how radiation damage was monitored, exposures and times, normalization (time or monitor counts), transmission method, absolute-scale standards, instrument and source type, collimation, beam size, wavelength resolution, detector, measured range, sample environment, and reduction software with version. Sec. 2.2: neutron wavelength spread and large beams smear the data; smear the model with the measured beam profile. Sec. 2.4: successive frames compared to detect subtle damage. Table 3: report the size of any solvent-subtraction correction; desmearing method stated and smeared data kept; analysis software and versions |
| 3 | S. Takeyama, Bridging the gap between extreme environments and precision measurements: recent progress in megagauss physics, AppliedPhys 2, 6 (2026); read as preprint arXiv:2605.11379 | doi:10.3390/appliedphys2020006 | full text | Sec. 4.4: the quoted temperature is the one recorded just before the pulse; it holds for insulators, while in conductors eddy-current heating, scaling with the conductivity, the cross-section normal to the field, the square of the sweep rate and the volume, raises it; reducing the cross-section is essential; a thermocouple placed next to the sample. Sec. 3.1: pick-up coils calibrated against a reference coil. Sec. 3.2: that calibration holds only up to a limited field, and Faraday rotation is the more reliable field determination at the highest fields. Sec. 2.1: up- and down-sweeps recorded in one pulse, with the fast sweep helping to detect relaxation and hysteresis. Sec. 5.1: data from the rising and falling parts of the pulse compared for validity |
| 4 | B. R. Pauw, Everything SAXS: small-angle scattering pattern collection and correction, J. Phys.: Condens. Matter 25, 383201 (2013); read as preprint arXiv:1306.0637 | doi:10.1088/0953-8984/25/38/383201 | full text | Sec. 1.1: the information is an average over the irradiated volume. Secs. 2.2.2 and 3.4.9: slit smearing; desmearing amplifies noise and creates artefacts, so smear the model instead. Secs. 3.3 and 3.4.1 to 3.4.6: detector and geometric corrections (flat field, dead time, dark current and natural background, polarization, spherical angle), flux and transmission normalization (3.4.2), absolute calibration against secondary standards (3.4.4); the background measured with as many variables as possible identical to the sample measurement and given the same corrections (3.4.5). Secs. 3.3.1 and 3.6: NeXus and HDF5 formats, metadata kept with reduced data. Sec. 7: checklist of geometry and correction inputs to record, transmission and flux monitored throughout, background repeated for each change of geometry or container, repeated measurements in sequence to detect instability |
| 5 | E. A. Stern and K. Kim, Thickness effect on the extended-x-ray-absorption-fine-structure amplitude, Phys. Rev. B 23, 3781 (1981) | doi:10.1103/PhysRevB.23.3781 | abstract | Abstract: leakage radiation accompanying the intended beam reduces the measured absorption fine-structure amplitude in samples that are too thick, with significant distortion once the absorption step times thickness reaches about 1.5 |
| 6 | T. W. Guest, R. Bean, J. Bielecki, S. Birnsteinova, G. Geloni, M. Guetg, R. Kammering, H. J. Kirkwood, A. Koch, D. M. Paganin, G. van Riessen, P. Vagovič, R. de Wijn, A. P. Mancuso and B. Abbey, Shot-to-shot two-dimensional photon intensity diagnostics within megahertz pulse-trains at the European XFEL, J. Synchrotron Rad. 29, 939–946 (2022) | doi:10.1107/S1600577522005720 | full text | Sec. 3: beam position and size vary with position in the pulse train, with a slow drift and a rapid change. Sec. 4: perturbing the electron-beam trajectory increased the photon-beam displacement and size variance. Sec. 5: diagnostics integrated over a train understate pulse-to-pulse variance, and pulses should not be treated as independent or stationary |
| 7 | O. Arnold and others, Mantid: data analysis and visualization package for neutron scattering and μSR experiments, Nucl. Instrum. Methods Phys. Res. A 764, 156–166 (2014); read as preprint arXiv:1407.5860 | doi:10.1016/j.nima.2014.07.029 | full text | Sec. 1: reduction transforms instrument data into physical units and requires detailed knowledge of the instrument. Sec. 2: shared, professionally maintained software in place of bespoke instrument routines. Sec. 6.1: instrument geometry held in definition files. Sec. 6.3: each workspace records the history of algorithms that produced it, so the processing can be shown and regenerated. Sec. 5: formal releases about every three months, with release notes |
| 8 | M. Könnecke, F. A. Akeroyd, H. J. Bernstein, A. S. Brewster, S. I. Campbell, B. Clausen, S. Cottrell, J. U. Hoffmann, P. R. Jemian, D. Männicke, R. Osborn, P. F. Peterson, T. Richter, J. Suzuki, B. Watts, E. Wintersberger and J. Wuttke, The NeXus data format, J. Appl. Cryst. 48, 301–305 (2015) | doi:10.1107/S1600576714027575 | full text | Introduction: facilities have stored data in many home-grown formats, which burdens analysis software and undermines open access and scientific integrity. Sec. 2: one self-describing file per measurement holding detector and monitor data, beamline state and logs. Sec. 3.2: processed data record the program, version, date and parameters used |
