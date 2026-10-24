---
id: CL-OPTOELECTRONIC-EFFICIENCY
name: Claims of optoelectronic device efficiency
type: claim
field: physics/optics-photonics
applies_when: the paper claims a record, certified or high power conversion efficiency (PCE) for a solar cell, or a high external quantum efficiency (EQE) or efficacy for a light-emitting diode (LED), or ranks such efficiencies against reported values
version: "0.1"
---

# Claims of optoelectronic device efficiency

A claim of this kind asserts that a solar cell converts light to electrical power, or that a light-emitting diode (LED) converts injected charge to emitted photons, with a record or unusually high efficiency. For solar cells the figure is the power conversion efficiency (PCE) from current density-voltage (J-V) measurements under simulated sunlight; for LEDs it is the external quantum efficiency (EQE), the ratio of photons that leave the device to electrons in the circuit, or a photometric efficacy derived from it.

## 1. Independent certification

**Question.** For a claim of record or near-record efficiency, was the device measured by an independent, recognised test centre, and does the paper give the certified value, the area definition and area, and the measurement protocol next to its in-house value?

**Why it matters.** In-house measurements of new device types are prone to errors in area, spectrum and scan protocol that an accredited laboratory is set up to avoid. The consolidated record tables accept only results measured independently by a recognised test centre, on an eligible area definition and above a minimum area, and journal reporting guidelines ask authors to state whether performance was certified.

**Resolved by.** The certification report included, with the test centre named and its value compared with the in-house value; the device area and category consistent with the record being claimed (for one-sun cell records, an area of at least 1 cm², smaller cells only as notable exceptions); where certification was not possible, the claim worded as an in-house measurement, the full procedure described and the spread over devices shown alongside the best device.

**Benchmark.** [1], [2], [3]

## 2. Device area and masking

**Question.** On which area is the efficiency based (total, aperture or designated illumination area), how was that area measured, and was the device covered during the measurement by an opaque mask with a single simple opening that defines the illuminated area?

**Why it matters.** Current density is current divided by area, so any error in area passes directly into the efficiency. Small cells on larger glass substrates collect light that is scattered or guided through the glass from outside the defined area unless a mask blocks it, which overestimates the short-circuit current density. The record tables do not accept efficiencies based on an "active area" or measured through masks with multiple openings.

**Resolved by.** The area definition named; the area or mask opening measured with a calibrated microscope or imaging system, with repeated measurements and an uncertainty; the mask geometry, its alignment and its size relative to the device described; the short-circuit current density consistent with the integrated EQE (item 5).

**Benchmark.** [1], [3]

## 3. Hysteresis and stabilised output

**Question.** Does the paper state the J-V scan direction, rate, step, delay and any preconditioning, show forward and reverse scans, and report as its headline a steady-state efficiency from maximum power point tracking or from stabilised current at fixed bias, with the tracking data shown?

**Why it matters.** For many emerging absorbers the J-V curve depends on scan direction, scan rate and measurement history, so a fast scan can give a higher efficiency than the device delivers in operation. Across nearly 200 emerging cells submitted to an accredited laboratory, fast-scan efficiencies differed from steady-state values, in either direction, by up to about 20% relative, and up to 40% for some devices. Averaging forward and reverse scans, or quoting a hysteresis index, does not give a representative operating efficiency.

**Resolved by.** The steady-state efficiency reported as the headline value, with the current or power plotted against time until it has settled under a stated criterion (for example, tracking for at least a minute or until the change rate falls below a set threshold); fast scans in both directions shown for comparison; scans repeated after tracking to check for light soaking or degradation during the measurement.

**Benchmark.** [3], [4]

## 4. Simulator spectrum, irradiance and spectral mismatch

**Question.** How was the simulator irradiance set (which reference cell, calibrated by whom, with what spectral response), was a spectral mismatch factor calculated from the measured simulator spectrum and the device's spectral response and applied, and does the paper state the simulator class, its spatial uniformity over the device and the device temperature?

**Why it matters.** The simulator spectrum differs from the standard reference spectrum and the reference cell responds to different wavelengths from the device, so the measured current is in error unless a mismatch correction is applied. A large spectral deviation in a range where the device is sensitive, non-uniform irradiance over the device and reference cell, unstable lamp output and a device temperature away from the standard 25 °C each add further error.

**Resolved by.** A reference cell with a traceable calibration and a spectral response close to that of the device, keeping the correction small (an accredited laboratory keeps the mismatch factor within about 3% of unity); the mismatch factor computed and applied; the simulator spectrum, class and uniformity stated; the reference cell and device of similar size placed at the same position; the device temperature measured and controlled.

**Benchmark.** [3]

## 5. Agreement with integrated external quantum efficiency

**Question.** Does the paper show the EQE spectrum of the solar cell and compare the current density obtained by integrating it over the standard reference spectrum with the short-circuit current density from the J-V measurement, and were the EQE light bias and chopping frequency suited to the device?

**Why it matters.** A J-V current density well above the integrated EQE most often points to a poorly defined area or light guided in from outside it, though agreement does not by itself prove a correct measurement because absolute EQE calibration is itself uncertain. Devices that respond slowly or depend on light intensity give a distorted EQE spectrum when measured without light bias or at too high a chopping frequency, which also corrupts the spectral mismatch correction.

**Resolved by.** The EQE spectrum shown with its integrated current density; agreement with the J-V value within a stated margin (a margin of about 10% is common), or the J-V value below the upper limit set by the normalised EQE, with any discrepancy explained; the light bias and chopping frequency stated and shown to give a steady response.

**Benchmark.** [3], [4]

## 6. Collection geometry for LED emission

**Question.** How were the emitted photons collected (integrating sphere, large photodetector close to the device, or photodetector at a distance or on a goniometer), does the paper give the geometry, distances and calibration, and was the angular emission profile measured or only assumed to be Lambertian?

**Why it matters.** A detector that subtends a small solid angle gives the EQE only if the angular profile of the emission is known. With a detector on the device axis, assuming a Lambertian profile overestimates the EQE when the emission is more forward-directed than Lambertian and underestimates it when the emission is spread to wider angles, departures that are common with scattering layers or new architectures. Light guided to the substrate edges or scattered from outside the pixel can be counted as emission from the pixel, a detector touching the device alters the outcoupling, and errors in detector distance or in its spectral calibration enter the result directly.

**Resolved by.** The set-up described with device and detector dimensions and distances, and calibration files provided; the angular emission profile measured where a far detector is used; an aligned aperture mask that excludes edge and scattered light; the detector responsivity weighted by the measured electroluminescence spectrum; the EQE cross-checked by a second method, such as a photodetector and a calibrated spectroradiometer.

**Benchmark.** [5], [6]

## 7. Light outcoupling and the plausibility of LED efficiency

**Question.** Does the paper relate the claimed EQE to the internal efficiency and the light-extraction efficiency expected for its device structure, and where the EQE exceeds what a planar device of that kind usually extracts, does it identify the reason and measure it?

**Why it matters.** In planar thin-film LEDs most internally generated photons are trapped in substrate, waveguide and surface plasmon modes; in flat organic LEDs without outcoupling structures only about a fifth typically reach air, and the fraction for other emitter classes depends on their layer structure and the refractive indices of its materials. An EQE well above the level expected for the stack therefore implies a specific mechanism, such as an outcoupling structure, preferential emitter orientation or photon recycling, or else a measurement that collects more than the forward emission of the pixel.

**Resolved by.** The photoluminescence quantum efficiency of the emitter in a film or full device stack reported; an optical model or measurement of the extraction efficiency for the actual layer stack; any emitter orientation or photon recycling invoked supported by measurement; the EQE stated as forward-hemisphere or total emission, with consistency shown between EQE, photoluminescence efficiency and extraction efficiency.

**Benchmark.** [5], [6]

## 8. LED efficiency under operating conditions

**Question.** Is the LED EQE reported against current density over several orders of magnitude, with the luminance or radiance at which the peak occurs, and does the paper show that current, light output and emission spectrum were stable while each point was recorded?

**Why it matters.** A peak EQE reached only at low current density and luminance may fall sharply at the luminance an application needs, so a single peak value overstates the device. Emerging LEDs often change during a voltage sweep, unsynchronised readings of current and light output distort the EQE, and a spectrum that shifts during operation towards wavelengths where the detector is more sensitive can inflate it.

**Resolved by.** EQE plotted against current density and luminance, and current density and luminance against voltage; the luminance at peak EQE stated and compared with practical levels (at least about 100 cd m⁻² for displays); forward and backward sweeps at two rates showing no drift; the electroluminescence spectrum given at peak EQE and at maximum brightness, and before and after operation.

**Benchmark.** [5]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. A. Green, E. D. Dunlop, M. Yoshita, N. Kopidakis, K. Bothe, G. Siefer, X. Hao and J. Y. Jiang, Solar cell efficiency tables (Version 66), Prog. Photovolt. Res. Appl. 33, 795–810 (2025); read as the accepted manuscript hosted by OSTI (record 2573889) | doi:10.1002/pip.3919 | full text | Sec. 1 (Introduction): the main criterion for inclusion is independent measurement by a recognised test centre; three eligible area definitions (total, aperture, designated illumination area); masks must have a simple single aperture, masks with multiple openings are ineligible, and "active area" efficiencies are excluded; minimum areas of 1 cm² for a one-sun cell and 0.05 cm² for a one-sun notable exception; EQE and current-voltage curves are included with tabled results |
| 2 | Editorial, A checklist for photovoltaic research, Nat. Mater. 14, 1073 (2015) | doi:10.1038/nmat4473 | full text | Whole editorial: the checklist asks for scan conditions, cell size and number of samples, and whether performance was confirmed by an independent certification laboratory; several groups favour mandatory certification for record claims; without certification, extra care in describing the procedure and statistical evidence of reproducibility, with average values reported alongside the best device; hysteresis may need a tuned protocol |
| 3 | T. Song, D. J. Friedman and N. Kopidakis, Comprehensive performance calibration guidance for perovskites and other emerging solar cells, Adv. Energy Mater. 11, 2100728 (2021); read as the accepted manuscript hosted by OSTI (record 1787554) | doi:10.1002/aenm.202100728 | full text | Sec. 2 opening: standard test conditions include a device temperature of 25 °C. Secs. 1 and 2.1: poorly defined area is among the most common errors; light piping through unmasked glass overestimates short-circuit current; area measured with a calibrated microscope and repeated to estimate uncertainty. Sec. 2.2: spectral mismatch factor from simulator spectrum and spectral responses of reference cell and device, kept within 0.97 to 1.03; EQE without light bias distorts the spectrum and inflates current by about 1.5%; integrated EQE current within about 10% of the J-V value, or measured current below 98% of the normalised-EQE limit for glass-encapsulated cells, with failures usually traced to area or light piping; simulator spectral match, uniformity and stability. Secs. 2.3 and 4: accredited laboratories use steady-state protocols; fast-scan efficiencies of nearly 200 submitted cells deviated by about 20% relative and up to 40% from steady-state values; scans repeated after the steady-state measurement to check degradation |
| 4 | E. Zimmermann, K. K. Wong, M. Müller, H. Hu, P. Ehrenreich, M. Kohlstädt, U. Würfel, S. Mastroianni, G. Mathiazhagan, A. Hinsch, T. P. Gujar, M. Thelakkat, T. Pfadler and L. Schmidt-Mende, Characterization of perovskite solar cells: Towards a reliable measurement protocol, APL Mater. 4, 091901 (2016) | doi:10.1063/1.4960759 | full text | Abstract and opening section: hysteresis depends on scan rate, device and measurement history, so standard J-V measurements are not reproducible; scan direction and speed can change results by up to 50%; averaging scan directions and hysteresis indices are not representative; comparing short-circuit current with integrated EQE depends on light bias and chopping frequency; maximum power point tracking for at least 60 s as the first measurement. Concluding section: only stabilised results represent operating efficiency |
| 5 | M. Anaya, B. P. Rand, R. J. Holmes, D. Credgington, H. J. Bolink, R. H. Friend, J. Wang, N. C. Greenham and S. D. Stranks, Best practices for measuring emerging light-emitting diode technologies, Nat. Photonics 13, 818–821 (2019); read as the copy in the NSF Public Access Repository (record 10174170) | doi:10.1038/s41566-019-0543-y | full text | "Quantum efficiencies": three collection geometries; detector not in contact with the device; a small-solid-angle detector with the Lambertian assumption misses wide-angle emission or overestimates EQE for forward-directed emission, so measure the angular profile; aperture masks against waveguided edge and scattered light; spectral calibration weighted by the emission spectrum; cross-check by two methods; distance errors; EQE across orders of magnitude of current density; extraction efficiency affected by photon recycling and dipole orientation; comparison with photoluminescence efficiency. "Device emission colour and intensity": EQE meaningful only at practical luminance, at least 100 cd m⁻² for displays. "Stability and device lifetime": sweeps at two rates in both directions, asynchronous readout errors, spectra at peak EQE and maximum brightness, with allowance for the change in photodetector response when the spectrum shifts. Table 1: reporting checklist |
| 6 | S. Reineke, M. Thomschke, B. Lüssem and K. Leo, White organic light-emitting diodes: Status and perspective, Rev. Mod. Phys. 85, 1245–1293 (2013); read as preprint arXiv:1302.3435 | doi:10.1103/RevModPhys.85.1245 | full text | Abstract and Sec. I A 6: about 80% of generated photons are trapped in the layer structure; the light modes are set mainly by the thin-film structure and its refractive indices and absorption; the fraction reaching the far field is typically about 20%, and waveguide and surface plasmon modes cannot be extracted by external techniques. Sec. I B 1: EQE is correct only if the angular distribution is measured with an integrating sphere or goniometer, and the Lambertian assumption has been shown not to hold. Sec. II D: rule-of-thumb limit of about 20% EQE for flat devices without outcoupling improvement. Sec. IV: outcoupling structures |
