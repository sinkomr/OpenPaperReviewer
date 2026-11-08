---
id: CL-PERSISTENT-CURRENTS
name: Persistent currents
type: claim
field: physics/condensed-matter
applies_when: the paper claims a persistent or circulating current, quantized trapped flux or quantized circulation in a superconducting, normal-metal or semiconductor ring or a ring-shaped quantum gas, or bases such a claim on flux-periodic signals from SQUID, cantilever torque or Hall-probe measurements
version: "0.1"
---

# Persistent currents

## 1. Flux period and the ring's area

**Question.** Is the signal shown to be periodic in the flux through the ring, over enough periods to fix the period, and does the measured period agree with the flux quantum claimed (h/e or h/2e) for the ring's measured inner and outer radii?

**Why it matters.** A field-dependent signal is evidence of a ring current only if its period corresponds to flux through the ring. In a ring of finite width the expected period spans the values set by the inner and outer radii, so a period that matches a different area points to an incomplete background removal or another source. With only a few oscillations in the field range, the period and the background cannot be separated reliably.

**Resolved by.** The raw signal against flux over many periods; a Fourier transform or autocorrelation with the band expected from the inner and outer radii marked; the fitted period with its uncertainty compared with the expected one; any rings or data sets with a different period reported, not dropped.

**Benchmark.** [1], [2]

## 2. Separating the ring from the background

**Question.** How was the ring's contribution separated from the background of the sensor, the substrate and paramagnetic spins, and is the separation tested, for example by a background measured away from the ring or by the expected dependence on ring size and coupling?

**Why it matters.** The persistent-current signal is often much smaller than the raw sensor signal, which is dominated by sensor non-linearities and by a linear paramagnetic response from spins in or near the metal. Spins can also give non-linear features near zero field that mask or mimic a periodic current, and a smooth background fitted and removed over a narrow field range can leave artefacts with a period close to the expected one.

**Resolved by.** A background measured in place, away from the ring, and subtracted; the processing shown step by step from the raw signal; features that scale with the ring-sensor coupling and with ring size as a current would; a spin contribution identified by its temperature or frequency dependence; differences between rings or symmetric measurement positions used to cancel common backgrounds.

**Benchmark.** [1], [2]

## 3. Equilibrium current or driven current

**Question.** Does the paper show that the measured current is the equilibrium persistent current, not a current driven or heated by the sensor, electrical noise or radiation, and does it state the electron temperature of the rings and how it was established?

**Why it matters.** Noise or radiation reaching a ring can drive a direct current around it with the same flux periodicity, and such noise-driven currents have been proposed as an explanation for currents larger than theory predicts. The high-frequency Josephson oscillations of a nearby SQUID can drive non-equilibrium currents and heat the electrons, so the electron temperature can stay well above the bath temperature.

**Resolved by.** Filtering and shielding described; the result shown not to depend on excitation amplitude, frequency or sensor operating point; the electron temperature determined, for example from the temperature dependence of a calibrated response, from rings with and without a heat sink, or from an independent thermometer on the same chip; a detection method with low back-action, or a comparison between methods.

**Benchmark.** [1], [2], [3]

## 4. Magnitude, sign and the statistic compared with theory

**Question.** How was the measured signal converted to a current (coupling, mutual inductance or moment per unit current), and is the magnitude compared with theory using the right statistic for the claim: the typical current of a single ring, with random sign, or the average current of an ensemble?

**Why it matters.** In disordered metal rings the h/e current has a sign and size that vary from ring to ring, so its ensemble average vanishes and an array signal grows only as the square root of the number of rings, while an average current grows in proportion to it. Comparing a single ring with an ensemble prediction, or the reverse, can misstate the agreement with theory by large factors; reported amplitudes have at times exceeded theory by a few times up to two orders of magnitude. The conversion from sensor signal to current usually rests on a modelled inductance or geometry, not a direct calibration.

**Resolved by.** The conversion factor stated with how it was obtained, for example from a model of the ring-sensor mutual inductance; the number of rings and the scaling of the signal with that number shown; the theory evaluated with parameters measured on the same material, such as a diffusion constant from a co-deposited wire; the sign of the current and its zero-field reference stated; rings without a detectable signal included when a typical current is computed over rings.

**Benchmark.** [1], [2]

## 5. Temperature and size dependence

**Question.** Does the amplitude fall with temperature on the energy scale set by the ring (the correlation or Thouless energy, from the measured diffusion constant and circumference), and with ring size and harmonic number as predicted, and are these dependences compared quantitatively with theory?

**Why it matters.** A persistent current in a diffusive metal ring is suppressed exponentially once the temperature exceeds the correlation energy, which falls with the square of the circumference, and higher harmonics are suppressed faster. Spin contributions and many backgrounds follow different laws, such as an inverse dependence on temperature, so the temperature and size dependence are independent tests of the attribution.

**Resolved by.** Amplitude against temperature for rings of more than one size, compared with a theoretical curve whose parameters are measured independently or, if fitted, checked against an independent measurement such as the diffusion constant of a co-deposited wire; the period shown not to change with temperature; harmonics treated separately; any saturation at low temperature linked to a stated electron temperature.

**Benchmark.** [1], [2]

## 6. Superconducting rings: quantized flux and its origin

**Question.** For a superconducting ring, does the trapped flux or circulating current change in steps that correspond to h/2e through the ring's area as the cooling field is varied, and does the paper show that the signal comes from a current around the ring and not from flux pinned in the material or from a magnetic remanence?

**Why it matters.** Flux quantization in a ring is shown by steps in the trapped flux as the field during cooling is varied, with a step size fixed by the flux quantum and the ring's area. A superconducting film or bulk sample also holds a non-equilibrium magnetisation from pinned flux lines, which is not a ring current and which relaxes by thermally activated or tunnelling escape of flux from pinning sites.

**Resolved by.** Trapped flux or moment plotted against cooling field with the steps resolved and the step size compared with h/2e for the measured area; the contribution of flux pinned in the film estimated, for example from a sample of the same film without the hole; a ferromagnetic remanence excluded by showing that the moment vanishes when the ring is warmed through its transition.

**Benchmark.** [4], [5]

## 7. How persistent: monitoring time and decay

**Question.** Over what time was the current or trapped flux monitored, with what resolution, what lower bound on the lifetime (or upper bound on the decay rate) does this give, and is the observed decay compared with the expected mechanism, such as flux creep or phase slips?

**Why it matters.** "Persistent" is a statement about decay over time, so it is supported only to the extent of the monitoring time and the resolution of the measurement. Flux trapped by pinning relaxes over time, and a circulating superflow in a ring decays by stochastic phase slips, either in discrete steps or rapidly above a critical velocity; the observed lifetime can also be limited by drift, atom loss or trap lifetime rather than by the current itself.

**Resolved by.** The signal plotted against time over the full monitoring period with its noise level; the resulting bound on the decay rate stated; the decay law fitted and compared with the expected mechanism; for gases, the circulation lifetime compared with the atom-number and trap lifetimes.

**Benchmark.** [5], [6], [7]

## 8. Ring quantum gases: reading out the circulation

**Question.** How were the magnitude and direction of the circulation (the winding number) determined, can the read-out resolve neighbouring quantized states in single images, and is the flow shown to need the ring geometry?

**Why it matters.** In time-of-flight images a circulating ring condensate shows a central hole whose radius changes in discrete steps, but the hole size gives only the magnitude and also depends on atom number. Interference with a concentric reference cloud gives a spiral whose number of arms and handedness depend on the circulation and its direction, and whose dislocations reveal phase slips. A quantized circulation is stable only in a multiply connected trap; in a simply connected trap it breaks into separate vortices.

**Resolved by.** An interferometric or other direction-sensitive read-out alongside time-of-flight images; a histogram of the read-out showing well-separated states and the fidelity of assignment; the dependence of the read-out on atom number checked; a control in which the trap is made simply connected or no circulation is imprinted.

**Benchmark.** [6], [7], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. C. Bleszynski-Jayich et al., Persistent currents in normal metal rings, Science 326, 272 (2009); read as preprint arXiv:0906.4780, which carries a longer title | doi:10.1126/science.1178139 |
| 2 | H. Bluhm et al., Persistent currents in normal metal rings, Phys. Rev. Lett. 102, 136802 (2009); read as preprint arXiv:0810.4384 | doi:10.1103/PhysRevLett.102.136802 |
| 3 | V. E. Kravtsov and B. L. Altshuler, Relationship between the noise-induced persistent current and the dephasing rate, Phys. Rev. Lett. 84, 3394 (2000) | doi:10.1103/PhysRevLett.84.3394 |
| 4 | D. Lindley, Landmarks—Superconductor quantizes magnetic field, Physics 8, 102 (2015) | doi:10.1103/Physics.8.102 |
| 5 | Y. Yeshurun et al., Magnetic relaxation in high-temperature superconductors, Rev. Mod. Phys. 68, 911 (1996) | doi:10.1103/RevModPhys.68.911 |
| 6 | C. Ryu et al., Observation of persistent flow of a Bose-Einstein condensate in a toroidal trap, Phys. Rev. Lett. 99, 260401 (2007); read as preprint arXiv:0709.0012 | doi:10.1103/PhysRevLett.99.260401 |
| 7 | S. Moulder et al., Quantized supercurrent decay in an annular Bose-Einstein condensate, Phys. Rev. A 86, 013629 (2012); read as preprint arXiv:1112.0334 | doi:10.1103/PhysRevA.86.013629 |
| 8 | L. Amico et al., Colloquium: Atomtronic circuits: From many-body physics to quantum technologies, Rev. Mod. Phys. 94, 041001 (2022); read as preprint arXiv:2107.08561 | doi:10.1103/RevModPhys.94.041001 |
