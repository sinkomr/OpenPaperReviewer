---
id: T-MAGNETIC-DIAGNOSTICS
name: Magnetic diagnostics and equilibrium reconstruction
type: technique
field: physics/plasma
applies_when: the paper uses magnetic probes, flux loops, Rogowski coils, saddle or diamagnetic loops, motional Stark effect data or an equilibrium reconstruction to report plasma current, position, shape, stored energy, safety factor or current profile, or bases a claim on a reconstructed magnetic geometry
version: "0.1"
---

# Magnetic diagnostics and equilibrium reconstruction

Magnetic diagnostics (inductive pick-up coils, also called magnetic probes or Mirnov coils, flux loops, Rogowski coils and diamagnetic loops) are used to claim the plasma current, position, shape and stored energy of a magnetically confined plasma, and, through an equilibrium reconstruction that solves the Grad-Shafranov equation against the measurements, the flux-surface geometry, the safety factor (q) profile and the current and pressure profiles. Internal measurements such as motional Stark effect (MSE) polarimetry, which gives the magnetic field pitch angle along a neutral beam, are often added to constrain the core.

## 1. Integrator drift and offsets

**Question.** How were the induced voltages integrated (analogue or digital, with what time constant), how were the offset and drift estimated and removed, and does the paper show the residual drift over a pulse of the length used, compared with the signals on which the claims rest?

**Why it matters.** Inductive sensors measure the rate of change of field or flux, so any offset in the voltage is integrated and the error grows with time. Offsets of tens to hundreds of microvolts arise from the electronics, thermoelectric voltages and interference, and they can change during a pulse, so an offset estimated before the pulse may not hold through a long one.

**Resolved by.** The integration scheme and drift correction described; the drift measured over a pulse of the same length without plasma, or from the signal before and after the plasma, and stated in the units of the measurement; a check that slowly varying results such as stored energy or a late-time equilibrium do not depend on the drift correction; for long pulses, a method shown to track offset changes during the pulse.

**Benchmark.** [1], [2], [3]

## 2. Sensor calibration and positions

**Question.** How were the effective area, position and orientation of each sensor determined, was the calibration checked in place with known currents in coils or conductors before plasma operation, and what calibration uncertainty is assigned to each type of sensor?

**Why it matters.** An equilibrium reconstruction fits the plasma to field and flux values at assumed sensor locations. A sensor that is shifted, tilted or has an effective area different from its nominal value gives a systematic error that the fit attributes to the plasma, and calibration uncertainties can differ several-fold between sensor types.

**Resolved by.** In situ calibration with known currents, for example from the poloidal field coils with no plasma or from dedicated calibration coils, with the solved positions compared with metrology; the frequency response of sensors used for fast signals stated; a calibration uncertainty given for each sensor type and used as the measurement weight in the reconstruction; sensors that failed or were excluded listed.

**Benchmark.** [4], [5]

## 3. Eddy currents and pickup from coils

**Question.** How are the direct response of the sensors to the coil currents and the currents induced in the vacuum vessel, wall and other passive conductors treated, both in the raw sensor signals and in the reconstruction, and are the induced currents measured, modelled or fitted as free parameters?

**Why it matters.** Changing coil and plasma currents induce long-lived currents in nearby conductors. These add to the field at the sensors and to the external field acting on the plasma, and a reconstruction that ignores them fits the plasma to the wrong external field. Where the conductors are not axisymmetric, local probes see three-dimensional fields that an axisymmetric model cannot reproduce.

**Resolved by.** The response of each sensor to the coil currents measured in shots without plasma and accounted for; passive currents included in the reconstruction, either measured or as modelled current distributions with fitted amplitudes; the model of the conductors checked against the measured decay of induced currents in shots without plasma; the fit residuals for each sensor group shown with and without the passive-current model; for non-axisymmetric structures, local probes corrected for three-dimensional fields or excluded.

**Benchmark.** [4], [6], [7]

## 4. Diamagnetic flux and plasma current

**Question.** For stored energy from a diamagnetic loop, how was the vacuum toroidal flux removed and how were induced currents in the vessel and coils separated from the plasma signal; for plasma current from a Rogowski coil, does the coil also link currents in the vessel or other structures, and how were they subtracted?

**Why it matters.** The diamagnetic flux of a plasma is a small change on top of a much larger vacuum toroidal flux, so a small error in the compensation, a drift, or currents induced in nearby structures can be comparable with the plasma signal. A Rogowski coil measures all the current it encloses, so a coil outside the vessel includes the vessel current, and induced currents left out of the analysis show up as a mismatch in the plasma current.

**Resolved by.** The compensation scheme for the diamagnetic loop described and set with shots that have toroidal field but no plasma; the residual signal in such shots shown to be small compared with the plasma signal; the stored energy compared with an independent estimate, such as a kinetic stored energy or the reconstruction; the Rogowski coil position relative to the vessel stated, vessel current measured or modelled and subtracted, and the coil calibrated in place with a known current.

**Benchmark.** [3], [4], [6]

## 5. What the external measurements can determine

**Question.** Which quantities does the paper take from the reconstruction, does it state which of them are constrained by the measurements used and which come mainly from the profile parameterisation, regularisation or code, and does it give an uncertainty for each?

**Why it matters.** External magnetic measurements determine the plasma current and boundary well, but in a near-circular plasma they fix only the sum of the poloidal beta and half the internal inductance, and the inverse problem for the internal profiles is ill-posed. Without internal constraints, many current and pressure profiles fit the same data, the uncertainty grows towards the magnetic axis, and different codes or parameterisations can return core q values that disagree.

**Resolved by.** The measurements and constraints used in each reconstruction listed; the profile parameterisation and regularisation stated, with results shown not to change when they are varied within reason; uncertainties on profiles and derived quantities from a stated method, such as Bayesian sampling or a scan over parameterisations; core quantities such as q on axis quoted only when internal constraints are included, or flagged as weakly determined.

**Benchmark.** [8], [7], [9]

## 6. Internal constraints from the motional Stark effect

**Question.** When MSE pitch angles constrain the reconstruction, how was the polarimeter calibrated, was the measurement corrected for the radial electric field, and is the agreement between the reconstruction and the MSE data shown channel by channel?

**Why it matters.** The polarisation angle depends on the radial electric field as well as on the magnetic field, and the correction is significant in plasmas with strong rotation or steep pressure gradients. In situ calibration by firing the beam into a gas-filled torus can be biased by emission from secondary neutrals with different polarisation, and calibration errors pass directly into the q profile.

**Resolved by.** The calibration method and its checks described, including any dependence on fill pressure or beam conditions; the radial electric field correction applied, with its source, or shown to be negligible for the plasma conditions; the measured and reconstructed pitch angles plotted with uncertainties; q profiles compared with independent markers, such as the locations of rational surfaces from magnetohydrodynamic modes, or with polarimetry.

**Benchmark.** [10], [11], [9]

## 7. Model assumptions and independent validation

**Question.** Does the paper state the assumptions built into the reconstruction (axisymmetry, isotropic pressure, edge and scrape-off-layer current, pressure and edge current constraints), show how the geometry used for the claims changes when they are relaxed, and validate the result against measurements that were not used in the fit?

**Why it matters.** Constraints and assumptions that the fit cannot test can move flux surfaces, the separatrix and strike points by up to centimetres while barely changing the goodness of fit. A pressure constraint can even degrade the core reconstruction. Claims that rest on mapping other diagnostics onto flux surfaces inherit these shifts.

**Resolved by.** The model assumptions and constraints listed; reconstructions with and without the uncertain constraints compared for the quantities that matter to the claim, such as separatrix position or q; agreement checked against independent data, such as profile symmetry on both sides of the axis, strike point positions from divertor diagnostics, or rational surfaces; a goodness of fit reported for each sensor group, not only overall.

**Benchmark.** [9], [12], [6]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Amodeo, P. Arpaia and M. Buzio, Integrator drift compensation of magnetic flux transducers by feed-forward correction, Sensors 19, 5455 (2019) | doi:10.3390/s19245455 | full text | Sec. 1: drift comes from offsets and noise in the integrated voltage, thermoelectric voltages and interference; tokamak fields must be known to about 1% through a discharge; offset estimated between discharges cannot track changes during a long discharge; chopping leaves external offsets. Secs. 3.1 to 3.5: offsets of tens to hundreds of microvolts that fluctuate in time, and uncertainty that grows as the offset error accumulates |
| 2 | E. J. Strait, E. D. Fredrickson, J.-M. Moret and M. Takechi, Chapter 2: Magnetic diagnostics, Fusion Sci. Technol. 53, 304–334 (2008) | doi:10.13182/FST08-A1674 | abstract | Abstract (read via the OpenAlex record): magnetic data give plasma current, shape, position and thermal energy, and the equilibrium reconstructions that provide coordinates for other diagnostics; the review covers inductive loops and Hall probes; inductive methods are well understood, but steady-state burning plasmas may need other techniques, and approaches to long-pulse measurement are reviewed |
| 3 | X. Q. Ji, Q. W. Yang, Y. Xu, T. F. Sun, B. S. Yuan, B. B. Feng, Y. Liu, Z. Y. Cui and J. Lu, Diamagnetic measurements by concentric loops in the HL-2A tokamak, Rev. Sci. Instrum. 84, 083507 (2013) | doi:10.1063/1.4816842 | abstract | Abstract (read via Europe PMC): diamagnetic flux of only about 1 to 2 mWb; vacuum toroidal flux compensated by adjusting the integrator; integration drift kept within 5 mV over 10 s by hybrid analogue and digital compensation; stored energy resolved to about 0.2 kJ |
| 4 | D. Shiraki, J. P. Levesque, J. Bialek, P. J. Byrne, B. A. DeBono, M. E. Mauel, D. A. Maurer, G. A. Navratil, T. S. Pedersen and N. Rath, In situ "artificial plasma" calibration of tokamak magnetic sensors, Rev. Sci. Instrum. 84, 063502 (2013) | doi:10.1063/1.4808366 | abstract | Abstract (read via Europe PMC): sensor positions solved from fields of large in situ calibration coils and compared with metrology; sensor time responses compared with the known calibration current to isolate each signal's eddy-current contribution, and the wall model adjusted to match the measured decay; a non-uniformly wound Rogowski coil calibrated with the same coils |
| 5 | D. A. Ryan, R. Martin, L. Appel, N. B. Ayed, L. Kogan, A. Kirk and the MAST Upgrade Team, Initial progress of the magnetic diagnostics of the MAST-U tokamak, Rev. Sci. Instrum. 94, 073501 (2023) | doi:10.1063/5.0156334 | abstract | Abstract (read via Europe PMC): calibration procedures and uncertainty calculations for the magnetic probes; median calibration uncertainty about 1.7% for flux loops and 6.3% for pick-up coils |
| 6 | C. Hansen, D. P. Boyle, J. C. Schmitt and R. Majeski, Equilibrium reconstruction with 3D eddy currents in the Lithium Tokamak eXperiment, Phys. Plasmas 24, 042513 (2017); read as arXiv:1701.05851 | doi:10.1063/1.4981214 | full text | Sec. I: long-lived eddy currents in the shell and vessel distort the vacuum field, and shell breaks give 3D fields at local probes. Sec. III: eddy currents as fixed-shape sources with fitted amplitudes, and local probes corrected for 3D fields. Sec. IV: chi-squared falls sharply for probes, plasma current, diamagnetic flux and Thomson data when the eddy model is added. Sec. V: limits of the model |
| 7 | G. T. von Nessi, M. J. Hole and the MAST Team, Recent developments in Bayesian inference of tokamak plasma equilibria and high-dimensional stochastic quadratures, Plasma Phys. Control. Fusion 56, 114011 (2014); read as arXiv:1403.1321 | doi:10.1088/0741-3335/56/11/114011 | full text | Sec. I: reconstruction solutions are not generally unique. Sec. IV: bias corrections and conducting-surface currents inferred as nuisance parameters in every inference; degeneracy grows away from force balance; core poloidal-current posterior non-Gaussian with the most probable value outside the 95% interval; q from the Bayesian inference with MSE differs from a standard reconstruction by about 0.5 |
| 8 | J. Blum, C. Boulbe and B. Faugeras, Reconstruction of the equilibrium of the plasma in a Tokamak and identification of the current density profile in real time, J. Comput. Phys. 231, 960–980 (2012); read as arXiv:0909.4474 | doi:10.1016/j.jcp.2011.04.005 | full text | Sec. 1: magnetics identify the plasma current and the sum of poloidal beta and half the internal inductance in a near-circular plasma; the profile problem is ill-posed. Secs. 2.3 and 4.1 to 4.2: Tikhonov regularisation, with the parameter chosen from a scanned range; with magnetics only, the two profile functions in the Grad-Shafranov source have larger errors in the inner half of the flux range, while q and the averaged current density are recovered with much smaller errors. Sec. 4.3: interferometry and polarimetry improve the identification |
| 9 | M. Gelfusa, A. Murari, I. Lupelli, N. Hawkes, P. Gaudio, M. Baruzzo, M. Brix, T. Craciunescu, V. Drozdov, A. Meigs, E. Peluso, M. Romanelli, S. Schmuck, B. Sieglin and JET-EFDA Contributors, Influence of plasma diagnostics and constraints on the quality of equilibrium reconstructions on Joint European Torus, Rev. Sci. Instrum. 84, 103508 (2013) | doi:10.1063/1.4824200 | abstract | Abstract (read via Europe PMC and OpenAlex): the reconstruction problem is highly ill-posed, so results depend on the measurements and constraints used; polarimetry and MSE are both needed for reasonable q profiles; an edge current constraint can move strike points and the last closed flux surface by centimetres; a pressure constraint can degrade the core reconstruction; validation against independent measurements is essential |
| 10 | M. C. Zarnstorff, F. M. Levinton, S. H. Batha and E. J. Synakowski, The effect of Er on motional-Stark effect measurements of q, a new technique for measuring Er, and a test of the neoclassical Er, Phys. Plasmas 4, 1097–1102 (1997) | doi:10.1063/1.872197 | abstract | Abstract (read via the OpenAlex record): earlier MSE analyses of q ignored the plasma electric field; MSE angles are sensitive to it and need significant corrections in plasmas with large rotation or pressure gradients, confirmed with measured data |
| 11 | H. Y. Yuh, F. M. Levinton, S. D. Scott and J. Ko, Simulation of the motional Stark effect diagnostic gas-filled torus calibration, Rev. Sci. Instrum. 79, 10F523 (2008) | doi:10.1063/1.2969419 | abstract | Abstract (read via Europe PMC): MSE calibration by firing the beam into a gas-filled torus with known vacuum fields; secondary neutrals emit light with similar Doppler shift but different polarisation angle and contaminate the measured angles; behaviour depends on calibration parameters such as fill pressure |
| 12 | J. R. King, S. E. Kruger, R. J. Groebner, J. D. Hanson, J. D. Hebert, E. D. Held and J. R. Jepson, Effect of scrape-off-layer current on reconstructed tokamak equilibrium, Phys. Plasmas 24, 012504 (2017); read as arXiv:1702.00076 | doi:10.1063/1.4972822 | abstract | Abstract (arXiv:1702.00076): adding scrape-off-layer current to a reconstruction changes the goodness of fit only slightly but moves flux surfaces by up to about 3 cm |
