---
id: T-LARGE-FACILITIES
name: Measurements at large facilities
type: technique
field: physics/methods
applies_when: the paper reports data taken at a synchrotron, neutron source or X-ray free-electron laser (XFEL), such as scattering, diffraction or absorption spectroscopy, and bases a claim on them
version: "0.1"
---

# Measurements at large facilities

## 1. Beam damage and dose

**Question.** Does the paper state the dose or exposure the sample received, and does it show that the features a claim rests on do not change with accumulated exposure?

**Why it matters.** Intense X-ray beams change the samples they measure. The damage follows the absorbed dose, not the exposure time, and changes at particular sites, such as metal and heavy-atom sites, can set in at much lower dose than any visible loss of overall signal. A spectrum or structure taken late in an exposure may then describe a sample that the beam has already altered.

**Resolved by.** The dose estimated from flux, beam size, photon energy and sample composition, for example with a dose calculator, and compared with known damage thresholds for that kind of sample; successive exposures or frames compared and shown to agree, or early and late data analysed separately; any measures taken to limit damage, such as shorter exposures, moving the beam to fresh regions or crystals, or radical scavengers, reported.

**Benchmark.** [1], [2]

## 2. The sample and the region the beam sees

**Question.** What part of the sample did the beam illuminate (spot size, footprint, penetration depth, number of grains or crystals), was the measured specimen characterised by independent means, and did it stay the same during the measurement?

**Why it matters.** A facility measurement reports an average over the illuminated volume, which may be a small spot, a near-surface layer or a few grains, and it carries no information about the parts of the sample the beam did not reach. A measurement on one specimen in a short allocation can therefore stand for less of the material than the claim implies, and a sample that moves, settles or degrades during the measurement changes the quantity being averaged.

**Resolved by.** Beam size at the sample, footprint and probing depth stated and compared with the sample size and with the scale of the structure claimed; the specimen characterised by methods independent of the facility measurement, such as purity, composition or monodispersity checks, and identified as the same batch or piece; transmission or flux monitored throughout and repeated measurements in sequence shown to agree; more than one spot, specimen or orientation measured where the claim concerns the material as a whole.

**Benchmark.** [2], [3]

## 3. Instrument resolution

**Question.** Is the instrument resolution stated, and compared with the widths, line shapes and absent features on which claims rest?

**Why it matters.** Every measured profile is smeared by the resolution, significantly so with broad wavelength bands and large beams, and desmearing the data amplifies noise and can create artefacts.

**Resolved by.** The resolution stated for the configuration used; widths, line shapes and claims resting on an absent feature compared with it; the model smeared with the measured resolution rather than the data desmeared, or the desmearing method stated and the original data kept.

**Benchmark.** [2], [3]

## 4. Background and unwanted beam components

**Question.** How was the background measured and subtracted: was it taken with the same sample environment, container, geometry and corrections as the sample, how large was it compared with the signal, and was the beam free of unwanted radiation accompanying the intended beam?

**Why it matters.** At large facilities the sample usually sits in a container or sample environment, such as a capillary, cryostat, pressure cell or magnet, that scatters or absorbs as much as the sample, and the background also includes detector dark current and natural background. A background measured in a different configuration, or a subtraction that is large compared with the signal, can create or remove features. Unwanted radiation accompanying the intended beam distorts measured amplitudes in a way that depends on sample thickness.

**Resolved by.** An empty-container or solvent-only measurement made in the same geometry and with the same corrections, repeated whenever the geometry, container or solvent changed; dark-current measurements stated; the size of the background and of any ad hoc correction to it reported, with the raw sample and background curves shown together; sample thickness chosen to avoid amplitude distortion, and the measures used to suppress unwanted radiation in the beam stated.

**Benchmark.** [2], [3], [4]

## 5. Normalization to beam intensity

**Question.** To what were the data normalized: which monitor measured the incident intensity, how was transmission measured, and, where absolute intensities are claimed, against which standard were they calibrated?

**Why it matters.** The incident flux at a facility changes during and between measurements, and XFEL pulses vary from one pulse to the next in beam position and size, in ways that averages over a pulse train underestimate. Intensities compared between samples, temperatures or runs are only as good as the normalization, and absolute scales rest on a calibration standard and its own uncertainty.

**Resolved by.** The monitor type and position stated, with normalization by monitor counts or time named; transmission measured for each sample and the method given; absolute calibration against a named standard with the calibration factor reported; for XFELs, per-pulse beam diagnostics used where pulse-to-pulse variation could affect the result.

**Benchmark.** [2], [3], [5]

## 6. Facility software and corrections

**Question.** Which reduction software and version produced the reduced data, which corrections did it apply with which parameters, and was the reduction checked by the authors rather than taken as given?

**Why it matters.** Converting raw detector counts into physical units at a facility relies on instrument-specific knowledge built into facility software: instrument geometry, detector efficiency, and corrections such as flat field, dead time, polarization and solid angle. Users often run this reduction as supplied, so its choices and defaults enter the result without appearing in the paper, and the software changes from one release to the next.

**Resolved by.** The reduction software and version named, with each correction and its parameters listed, for example as a recorded processing history or script; the instrument definition or calibration files identified; analysis and modelling software and versions named; reduced data checked against a reference sample or a known result measured in the same session.

**Benchmark.** [2], [3], [6], [7]

## 7. Instrument configuration reported

**Question.** Does the paper give the facility, instrument and configuration used for each data set: source type, wavelength or energy and its spread, collimation, beam size, detector and sample-to-detector distance, measured range, counting or exposure times, and sample environment conditions?

**Why it matters.** Facility instruments are reconfigured between experiments and between runs within one experiment, and each configuration changes resolution, range, background and corrections. Without it a reader cannot judge which artefacts could be present, and the measurement cannot be repeated, often on a different instrument.

**Resolved by.** A table of instrument settings for each data set, of the kind community reporting guidelines set out; sample environment conditions such as temperature, pressure, field and cell type stated; raw data and metadata kept in a self-describing facility format that records the instrument state with each measurement.

**Benchmark.** [2], [3], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J. M. Holton, A beginner's guide to radiation damage, J. Synchrotron Rad. 16, 133 (2009) | doi:10.1107/S0909049509004361 |
| 2 | J. Trewhella et al., 2017 publication guidelines for structural modelling of small-angle scattering data from biomolecules in solution: an update, Acta Cryst. D 73, 710 (2017) | doi:10.1107/S2059798317011597 |
| 3 | B. R. Pauw, Everything SAXS: small-angle scattering pattern collection and correction, J. Phys.: Condens. Matter 25, 383201 (2013); read as preprint arXiv:1306.0637 | doi:10.1088/0953-8984/25/38/383201 |
| 4 | E. A. Stern and K. Kim, Thickness effect on the extended-x-ray-absorption-fine-structure amplitude, Phys. Rev. B 23, 3781 (1981) | doi:10.1103/PhysRevB.23.3781 |
| 5 | T. W. Guest et al., Shot-to-shot two-dimensional photon intensity diagnostics within megahertz pulse-trains at the European XFEL, J. Synchrotron Rad. 29, 939 (2022) | doi:10.1107/S1600577522005720 |
| 6 | O. Arnold and others, Mantid: data analysis and visualization package for neutron scattering and μSR experiments, Nucl. Instrum. Methods Phys. Res. A 764, 156 (2014); read as preprint arXiv:1407.5860 | doi:10.1016/j.nima.2014.07.029 |
| 7 | M. Könnecke et al., The NeXus data format, J. Appl. Cryst. 48, 301 (2015) | doi:10.1107/S1600576714027575 |
