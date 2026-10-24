---
id: T-DETECTOR-DEVELOPMENT
name: Detector development and performance
type: technique
field: physics/particle
applies_when: the paper presents a new or prototype particle detector, sensor or readout chip and reports its detection efficiency, spatial, time or energy resolution, rate capability, radiation tolerance or ageing from test-beam, source, laser or irradiation measurements
version: "0.1"
---

# Detector development and performance

Detector development papers claim that a new sensor, detector or readout chip reaches a stated detection efficiency, spatial, time or energy resolution, rate capability or radiation tolerance. The numbers usually come from a particle beam at a test-beam facility, with a beam telescope (a set of reference tracking planes) predicting where each particle crossed, and from measurements before and after irradiation to a stated fluence (often expressed as a 1 MeV neutron equivalent fluence, n_eq/cm²) or total ionising dose (TID).

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | H. Jansen, S. Spannagel, J. Behr et al., Performance of the EUDET-type beam telescopes, EPJ Tech. Instrum. 3, 7 (2016); read as arXiv:1603.09669 | doi:10.1140/epjti/s40485-016-0033-2 | full text | Sec. 3.1: threshold set in multiples of the noise, noise occupancy at the working point; integration time of 115 µs and a maximum particle rate of about 1 MHz. Sec. 4: trigger rate limited by the slowest device. Secs. 6.2 to 6.4: biased and unbiased residual widths combine intrinsic and track resolution differently (Eqs. 3, 4); width from a fit to the central 95.5% of the distribution; efficiency and resolution change with threshold, optimum at five to six times the noise. Secs. 6.2 and 6.5: track resolution at the device worsens at low beam energy and with more material in the device under test, and depends on the plane spacing and the position of the device |
| 2 | M. Garcia-Sciveres and N. Wermes, A review of advances in pixel detectors for experiments with high rate and radiation, Rep. Prog. Phys. 81, 066101 (2018); read as arXiv:1705.10150 | doi:10.1088/1361-6633/aab064 | full text | Sec. 2.2: resolution of pitch divided by √12 for single-pixel clusters and strong dependence on incidence angle and charge sharing. Sec. 3.1: required bias rises with fluence, above 500 V near 10^15 n_eq/cm². Sec. 4.1: efficiency lost to in-pixel pile-up unless hits are spaced well beyond the recovery time. Sec. 4.4: ionising damage occurs mainly in powered devices, depends on temperature and annealing, and high-dose-rate protocols no longer transfer simply to small-feature technologies. Sec. 4.1: many chips guarantee stable operation only up to a design occupancy. Sec. 4.6: noise occupancy set by the threshold in units of noise; time walk and its correction. Sec. 4.7: hits lost when buffers are insufficient |
| 3 | D. Dannheim, K. Dort, L. Huth et al., Corryvreckan: a modular 4D track reconstruction and analysis software for test beam data, JINST 16, P03008 (2021); read as arXiv:2011.12730 | doi:10.1088/1748-0221/16/03/P03008 | full text | Sec. 1: test beams operate prototypes in conditions as close as possible to the final deployment to characterise efficiency, resolution and timing. Sec. 4.2 (offline event building): hits near event-time window borders need selection using each detector's time resolution to keep the efficiency measurement unbiased. Secs. 5.2 and 5.3: masked pixels shown in the efficiency map; residual width taken as the root mean square of the central 96% of entries |
| 4 | H. F.-W. Sadrozinski, A. Seiden and N. Cartiglia, 4D tracking with ultra-fast silicon detectors, Rep. Prog. Phys. 81, 026101 (2018); read as arXiv:1704.08666 | doi:10.1088/1361-6633/aa94d3 | full text | Sec. 3 introduction and Sec. 3.6: time resolution sums time walk, fluctuations in the deposited charge, signal distortion, jitter and TDC binning. Secs. 3.2 and 3.4: a non-uniform weighting field adds a time spread from drift between the impact point and the high-field region. Sec. 4.6: finely segmented electrodes make the electric and weighting fields non-uniform, against the parallel-plate geometry timing needs. Sec. 5.3: radiation lowers charge collection efficiency and changes the doping, compensated by higher bias after irradiation. Sec. 6.4.1: time-walk correction by constant fraction, time over threshold or multiple sampling. Sec. 8.2.4: gain changes with temperature, more so near breakdown. Sec. 8.3.1: single-device resolutions obtained from time differences between pairs of sensors and a reference counter |
| 5 | R. Wigmans, New developments in calorimetric particle detection, Prog. Part. Nucl. Phys. 103, 109–161 (2018); read as arXiv:1807.03853 | doi:10.1016/j.ppnp.2018.07.003 | full text | Sec. 8 (Energy resolution): a truncated rms90 is about 21% smaller than the true width for a Gaussian and should not be called the energy resolution; sensor saturation narrows the distribution; non-linearity invalidates the width as a resolution; event selection should rely on external detectors, not on the calorimeter's own signals |
| 6 | I. Dawson, F. Faccio, M. Moll and A. Weidberg, Overview of radiation effects on detector systems, in Radiation effects in the LHC experiments: impact on detector performance and operation, CERN Yellow Reports: Monographs CERN-2021-001 (2021) | doi:10.23731/CYRM-2021-001.3 | full text | Sec. 2.1.1: 1 MeV neutron equivalent defined via NIEL; the NIEL hypothesis and its shortcomings. Sec. 2.1.3: leakage current scales with fluence independent of material, with strong temperature dependence and annealing; effective doping has beneficial, stable and reverse annealing components and depends on material and particle type, a weakness of the NIEL hypothesis; trapping limits signal at high fluence. Secs. 2.2 and 2.2.1: ionising-dose response depends on particle type, dose rate, temperature and bias; non-monotonic leakage current with dose, so step-by-step irradiation with monitoring is recommended. Sec. 2.2.1.1: test dose rates far above those in operation, low-dose-rate effects and rebound annealing tests |
| 7 | M. Titov, Radiation damage and long-term aging in gas detectors, in Innovative Detectors for Supercolliders, World Scientific (2004); read as arXiv:physics/0403055 | doi:10.1142/9789812702951_0014 | full text | Abstract and Sec. 6: initial laboratory radiation tests may not give what is needed to extrapolate to long-term performance of full-size detectors; ageing rate depends on current density. Sec. 6.3: lifetime depends on the size of the irradiated area and on gas flow, which is most critical when extrapolating laboratory tests to large detectors |
