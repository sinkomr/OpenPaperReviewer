---
id: T-ATOMIC-MAGNETOMETRY
name: Atomic magnetometers
type: technique
field: physics/amo
applies_when: the paper measures magnetic fields with an optically pumped or spin-exchange-relaxation-free alkali or helium vapour magnetometer, or reports such a sensor's sensitivity, noise floor, bandwidth, calibration, heading error or a comparison with other magnetic sensors
version: "0.1"
---

# Atomic magnetometers

Optically pumped magnetometers (OPMs) detect a magnetic field through its effect on the spin precession of optically polarised atoms in a vapour cell; spin-exchange-relaxation-free (SERF) magnetometers are OPMs run at high vapour density near zero field. They are used to claim a field sensitivity, usually as a noise spectral density in T/√Hz, a bandwidth and dynamic range, and measurements of biomagnetic, geophysical or laboratory fields.

## 1. Measured noise floor or projected sensitivity

**Question.** Is the quoted sensitivity a field-noise spectral density measured with the sensor operating, converted to field units with a response calibrated by a known applied field, and stated at a given frequency or band, and is it kept separate from limits projected from photon shot noise or spin-projection noise?

**Why it matters.** Atomic magnetometers have well-defined fundamental limits, and estimates of those limits are often several times lower than what the same apparatus achieves, because excess noise from the shield, the lasers or the cell adds to them. A projected value, or an optical noise level divided by an assumed response, can then be read as a demonstrated sensitivity. Noise also varies strongly with frequency, so a single number without its frequency can mislead.

**Resolved by.** A measured noise spectrum in field units over the frequency range of interest, with the conversion fixed by the response to a calibrated applied field; the frequency or band at which the headline value is taken stated; any projected limit labelled as such and compared with the measured value, with the excess noise discussed.

**Benchmark.** [1], [2]

## 2. Magnetic noise from the shield and surroundings

**Question.** Does the paper estimate the magnetic noise produced at the cell by the magnetic shield, conducting parts and heaters, and compare it with the reported noise floor?

**Why it matters.** Thermal currents and magnetisation fluctuations in high-permeability or conducting shields produce field noise of a few fT/√Hz inside a mu-metal shield of about 0.2 m radius, which often exceeds the intrinsic noise of a high-density alkali magnetometer. A single-sensor floor well below the noise expected from the shield in use calls for low-noise shield materials or differential detection, and a floor near it may be set by the environment rather than the sensor.

**Resolved by.** The shield materials and dimensions given, with an estimate of their thermal magnetic noise at the cell; low-noise materials such as ferrite, or a differential measurement, where the claimed floor is below that estimate; the frequency dependence of the measured noise compared with that expected from the shield.

**Benchmark.** [2], [3]

## 3. Gradiometric and single-sensor figures

**Question.** When the noise floor comes from the difference of two channels, does the paper state the baseline, say whether the difference was divided by √2 to give a per-channel figure, and show the single-channel noise alongside it?

**Why it matters.** Subtracting two nearby channels removes noise common to both, such as shield noise and drifts in the applied field, so a gradiometric noise floor can be far below what either channel achieves alone. The difference also removes much of the signal from distant sources, by a factor set by the baseline, so a gradiometric figure is not the sensitivity to an arbitrary field.

**Resolved by.** Single-channel and gradiometric noise spectra shown together; the baseline and the scaling used to give a per-channel figure stated; the reduction in response to the signal of interest, given its distance and the baseline, estimated or measured, for example with a calibrated gradient.

**Benchmark.** [2], [3]

## 4. Bandwidth and frequency response

**Question.** Is the frequency response of the sensor measured and shown, is the bandwidth stated, and does the sensitivity apply across the band where the claimed signals lie?

**Why it matters.** A passive atomic magnetometer responds like a low-pass filter with a corner set by its spin relaxation rate, and longer relaxation times that improve sensitivity also narrow the bandwidth. Signals above the corner are attenuated, and widening the bandwidth by feedback raises the output noise by the same factor, so a sensitivity quoted near the peak of the response may not hold at the frequencies used.

**Resolved by.** A measured amplitude and phase response against frequency with the bandwidth defined, for example at 3 dB; the noise spectrum and the response given over the same band as the signals of interest; for closed-loop operation, the loop bandwidth and the noise at the widened bandwidth.

**Benchmark.** [1], [4]

## 5. Operating field, dynamic range and residual fields

**Question.** For SERF and other zero-field sensors, does the paper state the residual static field at the cell in all three axes, how it was nulled and kept stable, and the linear range of the sensor, and does it show that the signals of interest stay inside that range?

**Why it matters.** The SERF regime needs a field of order 10 nT or less, and the response is linear only over about a nanotesla. A residual field of a few nanotesla rotates the sensitive axis by a few degrees per nanotesla and lets components along other axes leak into the output with amplitude and phase errors, and drifting ambient fields change the gain during a measurement. Results recorded outside the linear range are distorted.

**Resolved by.** The residual field components after nulling and their drift during the measurement; nulling coils or active compensation described; the linear range measured and the signal amplitudes shown to lie within it; where residual fields are not negligible, an estimate of the resulting gain and axis errors, or closed-loop operation.

**Benchmark.** [1], [4], [5]

## 6. Gain and sensitive-axis calibration of vector sensors

**Question.** Were the gain and the direction of the sensitive axis of each vector sensor measured in place, under the conditions of the measurement, rather than taken from nominal values?

**Why it matters.** The gain of a zero-field OPM depends on residual fields, and in arrays on the modulation fields of neighbouring sensors, which can change it by several per cent. The sensitive axis is set by the beam, the cell and the on-sensor coils and is hard to predict from the geometry, and two axes of one sensor need not be orthogonal. Source localisation and field maps inherit these errors.

**Resolved by.** Gain and axis directions measured for each sensor with known applied fields, for example from calibrated coils, after the array is assembled; recalibration after the array geometry changes; the calibration accuracy stated, ideally checked with a reference sensor; residual fields during calibration kept small enough that cross-axis errors are negligible.

**Benchmark.** [4], [5], [6]

## 7. Heading error and dead zones in scalar sensors

**Question.** For scalar sensors operated in finite fields such as the Earth's, does the paper report how the reading changes with the orientation of the sensor relative to the field, and the orientations at which the signal is lost?

**Why it matters.** Nonlinear Zeeman splitting and orientation-dependent light shifts make the reading depend on the angle between the light and the field; for alkali atoms in a 50 µT field the uncorrected shift can be of order ten nanotesla. Measuring at one fixed orientation hides this. Pumping and detection schemes also have dead zones, orientations where the signal goes to zero.

**Resolved by.** The reading measured while the sensor is rotated in a stable, known field, or the field direction is varied, over the range of orientations met in use; the heading error given in field units against angle; any correction scheme described and its residual error stated; the dead-zone orientations stated, or a scheme that avoids them.

**Benchmark.** [7], [8], [9]

## 8. Comparison with other magnetic sensors

**Question.** When the paper compares its sensitivity with other magnetometers, does it account for sensor volume, the distance to the source and the measurement bandwidth, for example through the energy resolution per bandwidth?

**Why it matters.** The fundamental sensitivity of a vapour magnetometer improves with the number of atoms, and so with the cell volume, and with the coherence time at the cost of bandwidth. A small, close sensor can see a weaker source than a larger, more sensitive one further away. Comparing noise floors alone favours large, slow sensors, and a combined figure such as energy resolution near or below the reduced Planck constant calls for a check of the volume and time used.

**Resolved by.** The active volume and its definition, the standoff from the source and the bandwidth stated alongside the noise floor; comparisons made at matched volume, distance and bandwidth, or through a combined figure such as energy resolution, with how the volume was counted.

**Benchmark.** [1], [4], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | D. Budker and M. V. Romalis, Optical magnetometry, Nat. Phys. 3, 227–234 (2007); read as preprint arXiv:physics/0611246 | doi:10.1038/nphys566 | full text | Sec. II, Eqs. 1–2: sensitivity limits from spin-projection noise (scaling with atom number and coherence time) and photon shot noise; SERF regime needs fields below about 10 nT; fundamental potassium SERF limit scales with the inverse square root of cell volume. Sec. III: passive sensor acts as a first-order low-pass filter with natural bandwidth set by the relaxation time, shorter relaxation costs sensitivity, feedback-widened bandwidth raises output noise by the same factor. Secs. II and IV.3: projected or estimated fundamental limits well below demonstrated sensitivities |
| 2 | H. B. Dang, A. C. Maloof and M. V. Romalis, Ultrahigh sensitivity magnetic field and magnetization measurements with an atomic magnetometer, Appl. Phys. Lett. 97, 151110 (2010); read as preprint arXiv:0910.2206 | doi:10.1063/1.3491215 | full text | Fig. 2: response to a 10 pT applied field measured and compared with a model. Fig. 3: single-channel and gradiometer noise spectra shown, difference scaled to give the sensitivity of each channel; baseline determined with a calibrated field gradient. Text: photon-shot-noise projection about three times below the measured floor, excess probably from imperfect cancellation of ferrite noise; ferrite inner shield used because its low conductivity removes Johnson-current noise |
| 3 | S.-K. Lee and M. V. Romalis, Calculation of magnetic field noise from high-permeability magnetic shields and conducting objects with simple geometry, J. Appl. Phys. 103, 084904 (2008); read as preprint arXiv:0709.2543 | doi:10.1063/1.2885711 | full text | Sec. I: shield noise often exceeds the intrinsic noise of high-density alkali magnetometers. Sec. VII and Table 4: a few fT/√Hz from a mu-metal shield of 0.2 m radius. Sec. V and Table 2: frequency dependence of the noise. Sec. VI and Table 3: differential detection with a short baseline reduces shield noise by about the baseline over the distance to the material. Sec. VII: the most sensitive experiments need low-loss non-conducting materials or short-baseline differential measurements |
| 4 | T. M. Tierney, N. Holmes, S. Mellor, J. D. López, G. Roberts, R. M. Hill, E. Boto, J. Leggett, V. Shah, M. J. Brookes, R. Bowtell and G. R. Barnes, Optically pumped magnetometers: From quantum origins to multi-channel magnetoencephalography, NeuroImage 199, 598–608 (2019) | doi:10.1016/j.neuroimage.2019.05.063 | full text | Sec. 3.5: spin-exchange relaxation suppressed below about 10 nT; cell offset from the sensor walls. Secs. 4.1 and 4.3: ambient fields nulled with coils, response linear only near zero field, within about ±1.5 nT (Fig. 5). Sec. 4.4: longer relaxation time improves sensitivity but narrows the bandwidth. Secs. 4.5–4.6: modulation fields of neighbouring sensors change the gain, about 3% in the example given; recalibration advised after array geometry changes. Sec. 5: drifting ambient fields change the gain; larger vapour volume gives higher sensitivity |
| 5 | A. Borna, J. Iivanainen, T. R. Carter, J. McKay, S. Taulu, J. Stephen and P. D. D. Schwindt, Cross-Axis projection error in optically pumped magnetometers and its implication for magnetoencephalography systems, NeuroImage 247, 118818 (2022) | doi:10.1016/j.neuroimage.2021.118818 | full text | Abstract and Sec. 2: a remnant field within SERF limits lets off-axis signal components leak into the output (cross-axis projection error). Sec. 4.2: sensitive axis rotates by about 3° per nT; amplitude errors up to about 30% for signals near 90° to the nominal axis. Sec. 5: null remnant fields, measure each sensor's gain and axis, closed-loop operation would remove the error |
| 6 | J. Iivanainen, A. Borna, R. Zetter, T. R. Carter, J. M. Stephen, J. McKay, L. Parkkonen, S. Taulu and P. D. D. Schwindt, Calibration and localization of optically pumped magnetometers using electromagnetic coils, Sensors 22, 3059 (2022) | doi:10.3390/s22083059 | full text | Introduction: OPM orientations are hard to obtain from geometric models, depending on beam shape, optical depth and on-sensor coils. Secs. 2–3: gain, orientation and position estimated from the response to coil fields mapped with a reference sensor. Sec. 4.3: estimated sensitive axes of one sensor are not orthogonal. Sec. 5.2: fields kept within the roughly ±1 nT linear range; cross-axis projection error may limit accuracy |
| 7 | G. Oelsner, V. Schultze, R. IJsselsteijn, F. Wittkämper and R. Stolz, Sources of heading errors in optically pumped magnetometers operated in the Earth's magnetic field, Phys. Rev. A 99, 013420 (2019); read as preprint arXiv:1809.00627, which carries a slightly different title | doi:10.1103/PhysRevA.99.013420 | full text | Abstract and Sec. II: heading error arises from changing the angle between the beam and the field; Secs. IV–V: main sources are nonlinear Zeeman splitting and an orientation-dependent light shift. Sec. III: measured by rotating the sensor in a fixed, well-defined field inside a shield and coil system. Abstract and conclusion: combining both circular polarisations can compensate both sources |
| 8 | W. Lee, V. G. Lucivero, M. V. Romalis, M. E. Limes, E. L. Foley and T. W. Kornack, Heading errors in all-optical alkali-vapor magnetometers in geomagnetic fields, Phys. Rev. A 103, 063103 (2021); read as preprint arXiv:2103.01358 | doi:10.1103/PhysRevA.103.063103 | full text | Introduction and Sec. II: orientation-dependent shifts of order 15 nT for rubidium at 50 µT from nonlinear Zeeman splitting; heading errors limit accuracy, especially for navigation. Sec. IV: measured by rotating the sensor relative to the field over about ±65°, with the pump polarisation reversed to separate offsets from sensor magnetisation. Secs. I and VII: corrected accuracy about 0.1 nT |
| 9 | A. Ben-Kish and M. V. Romalis, Dead-zone-free atomic magnetometry with simultaneous excitation of orientation and alignment resonances, Phys. Rev. Lett. 105, 193601 (2010); read as preprint arXiv:1001.0345, which carries a different title | doi:10.1103/PhysRevLett.105.193601 | full text | Introduction: for some field orientations relative to the device the signal goes to zero (dead zones), an inherent feature of the vector and tensor interactions used for pumping, a serious challenge for space magnetometers; heading errors in alkali magnetometers arise from nonlinear Zeeman splitting |
| 10 | M. W. Mitchell and S. Palacios Alvarez, Colloquium: Quantum limits to the energy resolution of magnetic field sensors, Rev. Mod. Phys. 92, 021001 (2020); read as preprint arXiv:1905.00618 | doi:10.1103/RevModPhys.92.021001 | full text | Secs. I and III, Eqs. 5–6: energy resolution combines field noise, sensing volume and measurement time. Sec. IV and Fig. 2: sensitivity plotted against sensor size; SERF magnetometers and other leading sensors approach the reduced Planck constant; the survey counts only measured results with known sensing dimensions. Sec. VIII: best reported sensors do not go below it |
