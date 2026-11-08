---
id: CL-ANOMALOUS-THRUST
name: Claims of anomalous thrust
type: claim
field: physics/gravitation-precision
applies_when: the paper claims that a device produces a net force or thrust without expelling propellant, or by a mechanism outside established propulsion physics, measured on a thrust balance, torsion pendulum, weighing scale or other force sensor
version: "0.1"
---

# Claims of anomalous thrust

## 1. Heating of the device and the balance

**Question.** Does the paper show that the apparent force is not produced by heating of the device, its mount or the balance, through thermal expansion that shifts the centre of mass, changes in the zero or stiffness of the balance with temperature, or recoil from uneven thermal emission?

**Why it matters.** A device that dissipates power heats itself and the balance during each on-period, and on a pendulum balance the resulting drift and centre-of-mass shift give a deflection that starts and stops with the power, much as a thrust would. Heat radiated unevenly from a warm body also exerts a real recoil force, which is small but can match the size of the forces claimed.

**Resolved by.** Temperatures of the device, its mount and the balance recorded alongside the force; the rise and decay of the signal compared with the switching times and with the thermal time constants; a balance or mounting that is insensitive to centre-of-mass shifts, or a measured thermal sensitivity applied as a correction; the zero measured before thermal drift builds up; the recoil from thermal emission estimated from the device's temperature distribution.

**Benchmark.** [1], [2], [3], [5]

## 2. Magnetic and electrostatic interaction with the surroundings

**Question.** How does the paper bound forces between the currents and fields of the device and its power circuit and the Earth's field, magnetic parts of the balance or chamber, and dampers or shields, and forces from charge or high voltage on the device and nearby surfaces?

**Why it matters.** Currents of amperes flowing in loops on a balance interact with the Earth's field and with nearby magnetic materials, giving forces that switch on and off with the device. Insulated parts and high-voltage electrodes collect charge and give electrostatic forces on the device and the balance arm that do not depend on the claimed mechanism.

**Resolved by.** Non-magnetic materials near the device, twisted or coaxial current paths, and magnetic and electrostatic shielding described; the magnetic coupling measured by passing the same current through the same path with the claimed mechanism absent, or by applying a deliberately enlarged field, then scaled to operating conditions; the device and balance grounded or discharged; the result unchanged when shielding layers are added or the device is moved relative to magnetic parts.

**Benchmark.** [1], [6], [7]

## 3. Power and signal feeds across the balance

**Question.** How do power and signals reach the device, and does the paper show that cables, waveguides, tubes or liquid-metal contacts crossing the balance do not exert a force that changes when power flows?

**Why it matters.** Every connection that crosses onto the balance adds stiffness, can push or pull as it warms or carries current, and braided conductors can give tares that do not repeat. A change in feed force when the device is energised is indistinguishable from thrust unless it is measured separately.

**Resolved by.** Feeds routed and oriented so that they cannot push along the thrust axis, using liquid-metal contacts or on-board batteries with wireless control where possible, and with any charging done before the measurement; the balance calibrated with all feeds installed; a test in which the same current flows through the feeds into a dummy load, showing no force at the level of the claim.

**Benchmark.** [1], [2], [3], [6]

## 4. Gas, outgassing and tests in air

**Question.** Was the force measured in vacuum, at what residual pressure, and does the paper exclude forces from ion wind, convection, buoyancy, radiometric effects and outgassing?

**Why it matters.** In air, high-voltage devices drive an ion wind and warm devices drive convection, both of which produce real forces that disappear in vacuum. In vacuum, temperature differences in the residual gas still produce radiometric forces that depend on pressure, and heated materials release gas that carries momentum away from the device.

**Resolved by.** Measurements in vacuum with the pressure stated before and during operation; the force shown not to scale with residual pressure; outgassing monitored, for example as a pressure rise during operation, and materials baked or sealed; any result obtained in air repeated in vacuum before it is attributed to the claimed mechanism.

**Benchmark.** [1], [4], [6], [8]

## 5. Calibration and response of the balance under operating conditions

**Question.** Was the balance calibrated in place with a known force applied near the device's line of action, under the same conditions as the measurement (vacuum, feeds connected, device mounted and at operating temperature), and is its response to a step force shown so that a thrust can be told apart from drift?

**Why it matters.** The sensitivity of a balance changes with mass loading and temperature, and a calibration made in a different environment can bias the result. A sudden force makes a pendulum oscillate and its zero can drift slowly, so a signal whose shape differs from the balance's response to a known step is hard to interpret.

**Resolved by.** A calibration force, for example from a voice coil or electrostatic actuator, stepped up and down several times under operating conditions with the residuals of the fit shown; the calibration repeated before and after the runs; the actuator checked against an independent standard such as a mass balance or the radiation pressure of a laser; calibration pulses shown alongside the claimed signal so that their shapes and time constants can be compared; any correction for zero drift stated, bounded by the zero measured before and after each on-period and guided by measured temperatures.

**Benchmark.** [1], [2], [6], [7]

## 6. Moving parts, vibration and torques

**Question.** For devices with moving or oscillating parts, or that vibrate when energised, does the paper show a sustained force on a level, low-friction balance, and exclude friction, vibration coupled into the balance, and torques or tilts read as a linear force?

**Why it matters.** Oscillating masses and gyroscopes can appear to give net thrust through friction that differs between the two halves of a cycle, or because a torque or tilt deflects the sensor. Vibration is often the largest disturbance on a sensitive balance, and a device that vibrates when switched on can shift its reading.

**Resolved by.** A sustained deflection of a level pendulum or balance whose friction is negligible, not motion on a surface or wheels; tilt and rotation of the platform monitored; the vibration of the device measured, the balance isolated from it and from the floor, and the vibration noise compared with the claimed signal; displacement recorded along more than one axis.

**Benchmark.** [1], [6], [9]

## 7. Reversed, sideways and switched-off tests

**Question.** Does the force reverse when the device is reversed on the balance, vanish when it is turned to point across the measured axis, and disappear when the same power flows with the claimed mechanism disabled, with feeds and the rest of the set-up unchanged?

**Why it matters.** Many of the effects above follow the power, the feeds or the balance rather than the orientation of the device, and some, such as thermal and magnetic forces, can also change sign when the device is turned. Comparing orientations, and comparing runs with and without the claimed mechanism at the same power, separates a force tied to the device from one tied to the set-up.

**Resolved by.** Data in forward, reverse and sideways orientations at the same power, and with the polarity of applied voltages reversed where relevant; runs with a dummy load, off resonance or with a symmetric version of the device at the same dissipated power; off-periods before and after each on-period used as the baseline, with many repeated cycles; the claimed force compared with the radiation-pressure force for the same power, which any emitted radiation could supply.

**Benchmark.** [1], [3], [6], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J. E. Polk et al., Recommended practice for thrust measurement in electric propulsion testing, J. Propul. Power 33, 539 (2017); read as the NASA author manuscript in PubMed Central (PMC7839308) | doi:10.2514/1.B35564 |
| 2 | A. D. Kodys et al., An inverted-pendulum thrust stand for high-power electric thrusters, 42nd AIAA/ASME/SAE/ASEE Joint Propulsion Conference, AIAA 2006-4821 (2006) | doi:10.2514/6.2006-4821 |
| 3 | M. Tajmar et al., High-accuracy thrust measurements of the EMDrive and elimination of false-positive effects, CEAS Space J. 14, 31 (2022) | doi:10.1007/s12567-021-00385-1 |
| 4 | L. Carbone et al., Thermal gradient-induced forces on geodetic reference masses for LISA, Phys. Rev. D 76, 102003 (2007); read as arXiv:0706.4402 | doi:10.1103/PhysRevD.76.102003 |
| 5 | S. G. Turyshev et al., Support for the thermal origin of the Pioneer anomaly, Phys. Rev. Lett. 108, 241101 (2012); read as arXiv:1204.2507 | doi:10.1103/PhysRevLett.108.241101 |
| 6 | M. Tajmar et al., In-depth experimental search for a coupling between gravity and electromagnetism with steady fields, Sci. Rep. 14, 19427 (2024); read in PubMed Central (PMC11339412) | doi:10.1038/s41598-024-70286-w |
| 7 | C. Rothleitner and S. Schlamminger, Invited Review Article: Measurements of the Newtonian constant of gravitation, G, Rev. Sci. Instrum. 88, 111101 (2017); read as the NIST author manuscript in PubMed Central (PMC8195032) | doi:10.1063/1.4994619 |
| 8 | F. X. Canning et al., The ISR asymmetrical capacitor thruster: experimental results and improved designs, 40th AIAA/ASME/SAE/ASEE Joint Propulsion Conference (2004), NASA Technical Reports Server record 20040085936 | https://ntrs.nasa.gov/citations/20040085936 |
| 9 | M. G. Millis and N. E. Thomas, Responding to mechanical antigravity, NASA/TM-2006-214390, AIAA 2006-4913 (2006) | https://ntrs.nasa.gov/citations/20070004897 |
