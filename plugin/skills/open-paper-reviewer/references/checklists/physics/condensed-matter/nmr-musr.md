---
id: T-NMR-MUSR
name: NMR, NQR and muon spin rotation
type: technique
field: physics/condensed-matter
applies_when: the paper reports NMR or NQR spectra, Knight shifts or nuclear relaxation rates, or zero-, longitudinal- or transverse-field muon spin rotation or relaxation data, and bases a claim about magnetic order, its volume fraction, spin dynamics, superconducting pairing or superfluid density on them
version: "0.1"
---

# NMR, NQR and muon spin rotation

Nuclear magnetic resonance (NMR), nuclear quadrupole resonance (NQR) and muon spin rotation, relaxation and resonance (μSR) are local probes. They are used to claim a local spin susceptibility from the Knight shift, spin dynamics and superconducting gap structure from the nuclear spin-lattice relaxation rate 1/T1, static magnetic order and the fraction of the sample that orders, broken time-reversal symmetry, and the superfluid density from the field distribution of the vortex lattice. Each of these is inferred from the resonance or precession of a probe spin whose coupling to the electrons, and for muons whose position, has to be known or assumed.

## 1. Shift reference and hyperfine coupling

**Question.** Does the paper state the reference against which shifts are measured, and does it show how the measured shift was separated into spin and orbital parts and converted into a spin susceptibility, for example with a plot of shift against bulk susceptibility?

**Why it matters.** The Knight shift equals a hyperfine coupling times the spin susceptibility, plus a temperature-independent orbital term, so a spin susceptibility follows from it only when the coupling and the orbital term are known. Shift and bulk susceptibility are linked through such plots, but in many materials the shift stops tracking the bulk susceptibility below a crossover temperature, so a single coupling constant does not hold at all temperatures.

**Resolved by.** The reference frequency or compound stated; a plot of shift against bulk susceptibility, with temperature as the implicit parameter, giving the hyperfine coupling and orbital shift with uncertainties; the temperature range over which the linear relation holds stated, and any departure from it discussed, not absorbed into a fixed coupling.

**Benchmark.** [1], [2]

## 2. Knight shift in the superconducting state

**Question.** When a change, or the absence of a change, in the Knight shift below the superconducting transition is used to infer the spin state of the pairs, does the paper correct for the diamagnetic and demagnetising fields of the superconductor, and show that the radio-frequency pulses did not heat the sample out of the superconducting state?

**Why it matters.** In the superconducting state the field at the nucleus is changed by the screening currents, the vortex lattice and demagnetisation, which depends on sample shape, and these alone can move the resonance a long way. Radio-frequency pulses can briefly heat the electrons above the transition temperature, so the spectrum looks like the normal state and an unchanged shift is recorded although the spin susceptibility has fallen. A finite shift at low temperature can also come from spin-orbit coupling or from field-induced quasiparticles.

**Resolved by.** The diamagnetic and demagnetisation corrections estimated for the actual sample shape, field and penetration depth; spectra recorded at several pulse energies, with the shift shown not to depend on them, or a direct check that the sample stayed superconducting during the pulse sequence; measurements at more than one field, so that field-induced contributions can be separated.

**Benchmark.** [1], [3]

## 3. Spin-lattice relaxation and its recovery law

**Question.** Which recovery function was fitted to obtain 1/T1, is it the one appropriate to the nuclear spin, the transition irradiated and the relaxation mechanism, and are the raw recovery curves shown, including any stretched or multi-component fits and the fitted exponents?

**Why it matters.** For a nucleus with spin greater than one half the recovery is a sum of exponentials whose weights depend on which transition was saturated or inverted and on whether the relaxation is magnetic or quadrupolar, and a single fitted time can hide a slow component. A stretched exponential describes a distribution of relaxation rates; its characteristic rate is close to the median, not the average, of that distribution, and the same data can often also be fitted by a discrete sum of exponentials. Gap structure inferred from 1/T1 is also open to other readings: the coherence peak below the transition is hard to see in most materials and its absence alone does not show unconventional pairing, and in a field, vortex motion and states in the vortex cores add to the relaxation.

**Resolved by.** The recovery function written out with the nuclear spin, the irradiated transition and the assumed mechanism; representative recovery curves with fits; the stretching exponent reported with its temperature dependence, and conclusions not drawn from a characteristic rate alone when the exponent changes; power laws or activated behaviour fitted over a stated temperature range well below the transition; zero-field NQR or measurements at several fields where vortex contributions could matter.

**Benchmark.** [1], [4], [5]

## 4. Spectra, line assignment and static magnetism

**Question.** How was each line assigned to a nucleus and site (from quadrupole frequencies, asymmetry parameter, isotope ratios or orientation dependence), and when magnetic order is claimed from the spectrum, does the paper distinguish a static internal field, which splits or broadens the lines, from fluctuations, and convert the internal field to a moment with a stated coupling?

**Why it matters.** The quadrupolar lines are set by the electric field gradient, characterised by a frequency and an asymmetry parameter, and a wrong assignment passes into every derived quantity. A static internal field appears in the spectrum, but a field that fluctuates faster than the measurement is averaged out, and inhomogeneous broadening from disorder can mimic an ordered state. Near a transition both the spectrum and the relaxation change strongly.

**Resolved by.** Full spectra over the range where lines are expected, with each line assigned and the quadrupole parameters given; for claims of order, the spectrum shown above and below the transition, a splitting or broadening that matches the internal field expected for the proposed structure, and the hyperfine coupling used to convert field to moment; relaxation data across the transition consistent with the claimed onset.

**Benchmark.** [1]

## 5. Static or dynamic fields in zero-field μSR

**Question.** In zero-field μSR, does the paper separate the relaxation due to nuclear moments from that due to electronic moments, and show with longitudinal-field measurements whether the electronic fields are static or fluctuating, in particular when a small increase in relaxation is used to claim broken time-reversal symmetry or a frozen state?

**Why it matters.** Oscillations in zero field show a well-defined static internal field, while relaxation without oscillations can come from disordered static fields, from fluctuating fields or from randomly oriented nuclear dipoles. A longitudinal field affects static and fluctuating contributions differently, so it is the usual way to tell them apart. Claims of broken time-reversal symmetry in superconductors rest on a small increase in relaxation below the transition on top of a temperature-independent nuclear part, which leaves room for extrinsic origins such as defects or impurities.

**Resolved by.** Raw asymmetry spectra above and below the temperature of interest; the fitting function stated and the nuclear contribution fixed from data above the transition or from calculation; longitudinal-field scans showing decoupling of the additional relaxation, with the field needed compared with the size of the internal field; for small effects, the change shown on more than one sample or stoichiometry, and the residual field at the sample and how it was compensated stated.

**Benchmark.** [2], [6], [7], [8]

## 6. Magnetic volume fraction and background

**Question.** How was the magnetic or superconducting volume fraction obtained, and how was the signal from muons that stopped outside the sample (holder, cryostat, pressure cell) measured and subtracted?

**Why it matters.** Muons stop throughout the sample, so each signal component has an amplitude proportional to the volume it occupies, which is what makes a volume fraction possible. That number is only as good as the separation of the sample signal from the background of muons stopping in the holder or cryostat, or in the walls of a pressure cell, which can take a large share of the muons. For a powder that orders fully, the asymmetry should fall to one third of its value, and a smoother fall indicates a distribution of transition temperatures.

**Resolved by.** The background fraction measured, for example with a reference sample or from a calibration with the same holder, and stated; for small samples, veto counters or a sample area compared with the beam spot; for pressure cells, the share of muons stopping in the sample stated and the cell contribution kept separate from the sample signal, with a cell material whose response is small and does not change with field or temperature; volume fractions given with uncertainties and the method stated, such as the amplitudes of the separate signal components or the size of the non-relaxing one-third tail in a zero-field powder measurement.

**Benchmark.** [2], [6], [8], [9]

## 7. Superfluid density from transverse-field μSR

**Question.** How was the penetration depth or superfluid density obtained from the transverse-field spectra (which field distribution model, how many components, how the nuclear contribution was removed), at what field or fields, and was the field applied in a way that produces an ordered vortex lattice?

**Why it matters.** The simple relation between the Gaussian relaxation rate and the inverse square of the penetration depth gives the right trends, but a single Gaussian does not describe the asymmetric vortex-lattice field distribution and the fitted value depends on the model. The fitted penetration depth can vary with field because of the vortex cores, nonlocal and nonlinear effects and multiple gaps, so a value at one field can mislead about the gap structure. Pinning and disorder of the vortex lattice add broadening, and neglecting it biases the result.

**Resolved by.** The model of the field distribution stated with its assumptions and validity range; the nuclear contribution fixed from data above the transition; measurements at several fields and, where the claim depends on it, a value extrapolated to low field; field cooling or a stated procedure that produces an ordered vortex lattice; any correction for vortex-lattice disorder stated.

**Benchmark.** [6], [10], [11]

## 8. Muon site and perturbation of the host

**Question.** When a local field is converted into an ordered moment or used to choose between magnetic structures, does the paper identify the muon stopping site or sites, state how they were determined, and consider whether the muon changes its surroundings?

**Why it matters.** The field at the muon depends on where it sits, so a moment or structure derived from a precession frequency rests on the assumed site, and calculations often give several candidate sites without showing which are occupied. The positive muon can distort the lattice and change the local crystal field around it, and in some materials this alters the property being measured.

**Resolved by.** The muon sites determined by calculation (such as density functional theory with the muon included) or by experiment, and the moment derived from each candidate site with the spread reported; checks that the predicted frequencies and their number match the data; a discussion of muon-induced distortion; where possible, the site tested against the angle dependence of the muon Knight shift.

**Benchmark.** [2], [6], [12]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | N. J. Curro, Nuclear magnetic resonance in the heavy fermion superconductors, Rep. Prog. Phys. 72, 026502 (2009); read as preprint arXiv:0812.1031 | doi:10.1088/0034-4885/72/2/026502 | full text | Sec. 2.1: quadrupolar resonances set by the electric field gradient, its frequency and asymmetry parameter; NQR in zero field. Secs. 2.5 and 2.6: a static internal field shows in the spectrum, a fast-fluctuating one is averaged out; spectra and T1 change strongly near a magnetic transition. Sec. 2.1: orbital (chemical) shift term. Sec. 3.2: shift as hyperfine coupling times susceptibility. Sec. 4.1: diamagnetic, vortex and demagnetisation fields can move the resonance a long way below Tc and must all be considered; spin-orbit coupling leaves a finite shift. Sec. 4.2: Hebel-Slichter peak hard to see and its absence not proof of unconventional pairing; T^3 and T^5 laws for line and point nodes. Sec. 5.1: vortex motion contributes to 1/T1, so zero-field measurement is advantageous. Sec. 6.1 and Fig. 10: shift against susceptibility with temperature as implicit parameter; shift fails to track susceptibility below a crossover |
| 2 | P. Dalmas de Réotier and A. Yaouanc, Muon spin rotation and relaxation in magnetic materials, J. Phys.: Condens. Matter 9, 9113–9166 (1997); read as preprint arXiv:cond-mat/9710235 | doi:10.1088/0953-8984/9/43/002 | full text | Sec. 2: background from muons stopping in the holder or cryostat, usually a silver plate with a time-independent signal, corrected for in the asymmetry; in a fully ordered powder the asymmetry falls to a third, and a smoother fall indicates a spread of ordering temperatures. Secs. 2.2 and 3.4: longitudinal fields separate static from dynamic relaxation. Sec. 2.3: local fields linked to moments through Knight shift and Clogston-Jaccarino plots; muon sites cannot be predicted reliably; the muon's positive charge can distort the lattice locally |
| 3 | K. Ishida, M. Manago, K. Kinjo and Y. Maeno, Reduction of the 17O Knight shift in the superconducting state and the heat-up effect by NMR pulses on Sr2RuO4, J. Phys. Soc. Jpn. 89, 034712 (2020); read as preprint arXiv:1907.12236 | doi:10.7566/JPSJ.89.034712 | full text | Sec. 3: above a threshold pulse energy the spectra match the normal state because the pulses briefly destroy superconductivity; low-energy pulses reveal the reduced shift. Appendices A and B: heating checked with the tank-circuit phase and avoided with longer, weaker pulses. Sec. 4: residual shift attributed to field-induced quasiparticles |
| 4 | A. Suter, M. Mali, J. Roos and D. Brinkmann, Separation of quadrupolar and magnetic contributions to spin-lattice relaxation in the case of a single isotope, J. Magn. Reson. 143, 266–273 (2000); read as preprint arXiv:cond-mat/9906216 | doi:10.1006/jmre.1999.1990 | full text | Secs. I and II: recovery for spin greater than one half is multi-exponential, with amplitudes set by the initial populations and rates by magnetic and quadrupolar transitions; mixed relaxation can look like a single time constant. Sec. IV: an inversion-recovery time reflected only the fast decay while full saturation took much longer, revealing a slow quadrupolar channel |
| 5 | D. C. Johnston, Stretched exponential relaxation arising from a continuous sum of exponential decays, Phys. Rev. B 74, 184430 (2006); read as preprint arXiv:cond-mat/0609331 | doi:10.1103/PhysRevB.74.184430 | full text | Sec. I: stretched exponential as a sum of exponentials over a distribution of rates, motivated by NMR spin-lattice relaxation. Sec. II.3: the characteristic rate is close to the median, not the average, which is infinite without a cutoff. Sec. III: relaxation data can often be fitted by either a stretched exponential or a discrete sum of exponentials |
| 6 | S. J. Blundell, Spin-polarized muons in condensed matter physics, Contemp. Phys. 40, 175–192 (1999); read as preprint arXiv:cond-mat/0207699 | doi:10.1080/001075199181521 | full text | Sec. 4: oscillations reflect a static internal field and vanish above the ordering temperature. Sec. 6: Kubo-Toyabe relaxation from randomly oriented nuclear dipoles; a longitudinal field separates static broadening from fluctuations; the muon site must be known for quantitative information; each signal's amplitude is proportional to its volume fraction. Sec. 7: vortex-lattice field distribution is asymmetric; relaxation rate related to the inverse square of the penetration depth. Sec. 8: the muon is often, but not always, a passive probe |
| 7 | S. K. Ghosh, M. Smidman, T. Shang, J. F. Annett, A. D. Hillier, J. Quintanilla and H. Yuan, Recent progress on superconductors with time-reversal symmetry breaking, J. Phys.: Condens. Matter 33, 033001 (2020); read as preprint arXiv:2003.04357 | doi:10.1088/1361-648X/abaa06 | full text | Sec. II.1: fields of order 0.1 mT or below detected; static nuclear moments give a temperature-independent relaxation and the extra relaxation appears below Tc; a small longitudinal field decouples it, showing quasi-static fields not from paramagnetic impurities. Sec. III.1: stoichiometry used to exclude impurity-induced magnetism, and an earlier finding later attributed to defects or impurities |
| 8 | A. Amato, H. Luetkens, K. Sedlak, A. Stoykov, R. Scheuermann, M. Elender, A. Raselli and D. Graf, The new versatile general purpose surface-muon instrument (GPS) based on silicon photomultipliers for μSR measurements on a continuous-wave beam, Rev. Sci. Instrum. 88, 093301 (2017); read as preprint arXiv:1705.10687 | doi:10.1063/1.4986045 | full text | Sec. II.1 and Table 1: veto detectors reject muons that miss the sample, with a separate veto mode for samples smaller than the beam, whose diameter is about 10.5 mm at the sample. Sec. IV.2: stray fields of order 0.2 mT disturb measurements, so the field at the sample is actively compensated to about 1 μT |
| 9 | R. Khasanov, Perspective on muon-spin rotation/relaxation under hydrostatic pressure, J. Appl. Phys. 132, 190903 (2022); read as preprint arXiv:2208.11320 | doi:10.1063/5.0119840 | full text | Discussion of pressure cells: a substantial share of muons stops in the cell walls, so the sample volume must be large, and the cell material should be non-magnetic with a small, field- and temperature-independent response; signal amplitudes of coexisting phases give their volume fractions |
| 10 | A. Maisuradze, R. Khasanov, A. Shengelaya and H. Keller, Comparison of different methods for analyzing μSR line shapes in the vortex state of type-II superconductors, J. Phys.: Condens. Matter 21, 075701 (2009); read as preprint arXiv:0805.3646 | doi:10.1088/0953-8984/21/7/075701 | full text | Secs. II and V.1: a single Gaussian is unreliable and the number of components needed depends on field; the nuclear contribution is fixed above Tc; vortex disorder adds broadening, and neglecting it gives a lower limit for the penetration depth. Secs. V.2 and VI: penetration depth and coherence length are strongly correlated at high fields; fits at several fields recommended |
| 11 | J. E. Sonier, Muon spin rotation studies of electronic excitations and magnetism in the vortex cores of superconductors, Rep. Prog. Phys. 70, 1717–1755 (2007); read as preprint arXiv:0802.2942 | doi:10.1088/0034-4885/70/11/R01 | full text | Sec. III: the Gaussian relation between relaxation rate and penetration depth gives qualitative trends only. Sec. IV: the model is the largest source of uncertainty; the fitted penetration depth is field dependent and the true value is the low-field limit. Sec. IV.2: pinning broadens the field distribution. Secs. V.3.2 and V.4: field cooling gives a well-ordered vortex lattice; field dependence of the fitted value linked to gap anisotropy and multiple gaps |
| 12 | S. J. Blundell and T. Lancaster, DFT+μ: density functional theory for muon site determination, Appl. Phys. Rev. 10, 021316 (2023); read as preprint arXiv:2307.10076 | doi:10.1063/5.0149080 | full text | Sec. I: the field depends on the unknown muon position, and muon perturbation raises the question whether intrinsic behaviour is measured. Sec. II.3: the site fixes the angle dependence of the dipolar field, which can be tested against Knight shift data. Sec. IV.2: the site identifies which fields cause precession and allows quantitative moments; an energy-ordered list of candidate sites does not show which is occupied. Sec. IV.5: muon-induced change of the local crystal field can dominate the response in some materials |
