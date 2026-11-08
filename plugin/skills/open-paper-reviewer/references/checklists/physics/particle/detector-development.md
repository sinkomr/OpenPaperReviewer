---
id: T-DETECTOR-DEVELOPMENT
name: Detector development and performance
type: technique
field: physics/particle
applies_when: the paper presents a new or prototype particle detector, sensor or readout chip and reports its detection efficiency, spatial, time or energy resolution, rate capability, radiation tolerance or ageing from test-beam, source, laser or irradiation measurements
version: "0.1"
---

# Detector development and performance

## 1. Test-beam conditions and the reference system

**Question.** Does the paper state the beam particle and momentum, the angle of incidence, the temperature, the bias and threshold, any magnetic field, and the precision with which the reference system predicts the particle position at the device, and does it say how these conditions compare with those of the intended application?

**Why it matters.** The precision of the reference tracks at the device depends on the beam momentum, the material in the beam and the spacing of the telescope planes; at low momentum, multiple scattering can make it comparable to the resolution being measured. A test beam is meant to reproduce the final operating conditions as closely as possible, and a result obtained at one angle, momentum or temperature does not carry over automatically to another.

**Resolved by.** Beam, momentum, incidence angle, temperature, bias and threshold given for each data set; the track resolution at the device stated, with how it was calculated or measured; any conditions that differ from the application named, and either their effect estimated or the measurement repeated over the relevant range.

**Benchmark.** [1], [3]

## 2. Definition of detection efficiency and its working point

**Question.** How is the efficiency defined: which reference tracks form the denominator, which part of the device is included and which channels, edges or gaps are excluded, what spatial and time window counts as a matched hit, and at what threshold and noise or fake-hit rate is the efficiency quoted?

**Why it matters.** The quoted efficiency depends on each of these choices. Excluding masked channels, edges or inter-pad gaps, or widening the matching window, raises it, and so does lowering the threshold, which at the same time admits more noise hits. An efficiency given without the noise occupancy at the same threshold does not fix a working point, and hits assigned across the edges of readout time windows can bias the count unless the time resolution of each device is taken into account.

**Resolved by.** The definition written out, with the denominator, the region included and the matching criteria; efficiency shown as a function of threshold together with the noise or fake-hit rate, and the chosen working point named; an efficiency map, or the losses at edges, gaps and masked channels stated together with the fraction of the area excluded from the quoted value.

**Benchmark.** [1], [2], [3]

## 3. Spatial resolution: from residuals to intrinsic resolution

**Question.** Is the quoted spatial resolution the intrinsic resolution of the device, with the reference-track contribution removed, and does the paper state whether the residuals are biased (the device included in the track fit) or unbiased, how the width was estimated (a fit to the core, the full root mean square or a truncated one) and at which incidence angle, threshold and cluster size?

**Why it matters.** The width of the residual distribution combines the device resolution with the track resolution, and the two combine differently for biased and unbiased residuals. A fit to the core or a truncated root mean square gives a smaller number than the full distribution. Resolution also depends strongly on incidence angle, charge sharing and threshold, so a value obtained at one setting can differ widely from another, and for single-channel hits the binary limit of pitch divided by √12 is the natural comparison.

**Resolved by.** Residual distributions shown with their tails; the track resolution, its uncertainty and the way it was removed stated; the width estimator named, with the fraction of entries used if truncated; resolution given as a function of incidence angle and threshold; comparison with the binary resolution for the pitch.

**Benchmark.** [1], [2], [3]

## 4. Time resolution and the reference device

**Question.** How was the time resolution obtained: against which reference device, with what resolution of that reference and how it was removed, which correction for time walk was applied, and at what gain, bias, threshold and temperature, and over which part of the active area?

**Why it matters.** A measured time difference contains the resolution of both devices, so the single-device value depends on how the reference contribution was determined, for example from time differences between pairs or triplets of devices. Time resolution combines jitter, time walk, signal distortion and fluctuations in the deposited charge; without a pulse-by-pulse amplitude correction, time walk enters directly, and gain, and hence resolution, change with bias and temperature. If the signal shape depends on where the particle crosses, the resolution is not the same across the device.

**Resolved by.** The reference device and its resolution stated, with the reference contribution removed using combinations of several devices or an independently measured reference; the time-walk correction named, such as constant fraction discrimination, time over threshold or multiple sampling; resolution shown against bias or gain and at the stated temperature; resolution reported across the active area, including near pad edges.

**Benchmark.** [2], [4]

## 5. Energy resolution and response of calorimeter prototypes

**Question.** For energy measurements, how was the resolution defined (full root mean square of the signal distribution, a Gaussian fit, or a truncated measure such as the root mean square of the central 90 per cent), how were electrons, hadrons and muons separated in the event sample, and is the response shown to be linear over the energy range?

**Why it matters.** A truncated width gives a smaller value than the full root mean square, by about a fifth even for a Gaussian distribution, so it cannot be compared directly with resolutions defined in the usual way. Saturation in the sensors narrows the signal distribution and makes the resolution look better than it is, non-linearity means the width no longer describes the precision of the energy, and selecting events with the prototype's own signals biases the sample towards well-measured events.

**Resolved by.** Signal distributions shown with their tails and the estimator stated, with the full root mean square given where tails are present; event selection based on detectors outside the prototype, such as upstream Cherenkov counters, preshower detectors and downstream leakage or muon counters; mean response plotted against beam energy to show linearity; saturation discussed for the sensors used.

**Benchmark.** [5]

## 6. Rate capability and occupancy

**Question.** Was the device tested at particle rates and occupancies comparable with those of the intended application, and if not, does the paper show or estimate how efficiency, resolution and timing change with rate?

**Why it matters.** Test beams and their reference telescopes often deliver rates far below those of the target experiment, and the slowest device can limit the trigger rate. At high rate, efficiency is lost when hits arrive faster than the front end recovers or than buffers and readout can drain, and some chips are stable only up to a design occupancy, so performance measured at test-beam rates can overstate performance in operation.

**Resolved by.** The particle rate and occupancy during each measurement stated and compared with the target environment; efficiency shown against rate, or hit losses from dead time and buffer overflow measured or simulated for the readout architecture at the target rate.

**Benchmark.** [1], [2]

## 7. Radiation tolerance: fluence, annealing and operating point

**Question.** Does the paper state the fluence or dose with its units, the particle type and energy used for the irradiation and how the fluence was determined, the annealing history after irradiation, and the temperature and bias at which the irradiated device was measured?

**Why it matters.** Converting damage from different particles to a 1 MeV neutron equivalent fluence assumes that damage scales with non-ionising energy loss; this holds well for leakage current, but changes in effective doping and in the electric field depend on the particle type and on the impurity content of the material. Leakage current, effective doping and trapping change with time and temperature after irradiation through beneficial and reverse annealing, and leakage current depends strongly on the measurement temperature. Irradiated sensors often need much higher bias to recover their signal, and performance at a bias or temperature the application cannot provide does not show that the device will work there.

**Resolved by.** Irradiation facility, particle, energy, fluence and its uncertainty given, with the hardness factor used for the conversion; annealing time and temperature stated; measurement temperature given and leakage currents scaled to a reference temperature; efficiency and other performance shown against bias up to a stated maximum, with the leakage current or power dissipation at the operating point; an unirradiated device measured in the same setup for comparison.

**Benchmark.** [2], [4], [6]

## 8. Irradiation and ageing tests compared with the application

**Question.** Were the irradiation or ageing tests carried out under conditions that represent the application, in dose rate, temperature and bias during irradiation, size of the irradiated area and, for gaseous detectors, gas flow, current density and accumulated charge, and was performance followed during the irradiation and not only before and after it?

**Why it matters.** Laboratory tests deliver the lifetime dose or charge much faster than the experiment will. Ionising damage in electronics can depend on dose rate, temperature and bias and can vary non-monotonically with dose, so a test with only end points can miss a temporary degradation. In gaseous detectors, ageing depends on current density, the size of the irradiated area and gas flow, so small-area accelerated tests may not predict the lifetime of full-size detectors.

**Resolved by.** Dose rate, temperature and bias during irradiation stated; performance measured in steps through the irradiation; any annealing procedure used to emulate low dose rates described; for gaseous detectors, accumulated charge, current density, irradiated area and gas flow given; an argument, or tests at more than one dose rate or irradiated area, relating the test to the conditions of the application.

**Benchmark.** [2], [6], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | H. Jansen et al., Performance of the EUDET-type beam telescopes, EPJ Tech. Instrum. 3, 7 (2016); read as arXiv:1603.09669 | doi:10.1140/epjti/s40485-016-0033-2 |
| 2 | M. Garcia-Sciveres and N. Wermes, A review of advances in pixel detectors for experiments with high rate and radiation, Rep. Prog. Phys. 81, 066101 (2018); read as arXiv:1705.10150 | doi:10.1088/1361-6633/aab064 |
| 3 | D. Dannheim et al., Corryvreckan: a modular 4D track reconstruction and analysis software for test beam data, JINST 16, P03008 (2021); read as arXiv:2011.12730 | doi:10.1088/1748-0221/16/03/P03008 |
| 4 | H. F.-W. Sadrozinski et al., 4D tracking with ultra-fast silicon detectors, Rep. Prog. Phys. 81, 026101 (2018); read as arXiv:1704.08666 | doi:10.1088/1361-6633/aa94d3 |
| 5 | R. Wigmans, New developments in calorimetric particle detection, Prog. Part. Nucl. Phys. 103, 109 (2018); read as arXiv:1807.03853 | doi:10.1016/j.ppnp.2018.07.003 |
| 6 | I. Dawson et al., Overview of radiation effects on detector systems, in Radiation effects in the LHC experiments: impact on detector performance and operation, CERN Yellow Reports: Monographs CERN-2021-001 (2021) | doi:10.23731/CYRM-2021-001.3 |
| 7 | M. Titov, Radiation damage and long-term aging in gas detectors, in Innovative Detectors for Supercolliders, World Scientific (2004); read as arXiv:physics/0403055 | doi:10.1142/9789812702951_0014 |
