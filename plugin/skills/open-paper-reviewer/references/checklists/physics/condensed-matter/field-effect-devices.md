---
id: T-FIELD-EFFECT-DEVICES
name: Field-effect and gated devices
type: technique
field: physics/condensed-matter
applies_when: the paper reports transistor transfer or output curves, extracts field-effect mobility, threshold voltage, subthreshold swing, on/off ratio or contact resistance, or tunes carrier density with a solid, ionic-liquid or electrolyte gate
version: "0.1"
---

# Field-effect and gated devices

Field-effect transistors (FETs) and other gated devices are used to claim a mobility, a threshold voltage, an on/off ratio or subthreshold swing, a contact resistance, and a carrier density set by the gate, up to the very high densities reached with ionic-liquid and electrolyte gates in electric double-layer transistors (EDLTs). All of these are inferred from drain and gate currents through a device model whose assumptions may not hold.

## 1. Extraction model and bias regime

**Question.** For each quoted mobility and threshold voltage, does the paper state the equation used (linear or saturation regime), the drain bias and gate-voltage range of the fit, the gate capacitance entered and the method of threshold extraction, and does it show the transfer curves on linear and logarithmic scales together with the output curves?

**Why it matters.** Field-effect mobility can come out too low or too high relative to the drift mobility of the channel, depending on the bias, the contact resistance, the channel length and the gate capacitance assumed. There is no single standard way to extract the threshold voltage, and its value depends on the drain bias and on the kind of sweep used, so the carrier density inferred from it inherits that uncertainty.

**Resolved by.** Transfer and output curves shown in full; the regime and bias of every extraction stated; mobility plotted against gate voltage or carrier density, not only a peak value; the threshold method named and applied at the drain bias it belongs to; a high mobility cross-checked by a second method, such as a conductivity mobility from four-probe sheet resistance.

**Benchmark.** [1]

## 2. Contact resistance and gated contacts

**Question.** Does the paper separate the contact resistance from the channel, show how it varies with gate voltage, and check whether a steep turn-on or a kink in the transfer curve comes from the contacts and not from the channel?

**Why it matters.** The usual transistor equations, and the usual corrections for contact resistance, treat the contacts as an ohmic resistor in series with the channel. When the contact resistance falls with gate voltage, the drain current rises faster than the channel alone would allow, and applying the ideal model to that region can overestimate mobility by an order of magnitude or more. A contact resistance from a transfer-length series is unreliable unless the series includes devices in which the contacts dominate and the sheet resistance varies little between devices.

**Resolved by.** Contact resistance reported as a function of carrier density; a transfer-length series with at least four channel lengths, including both contact-dominated and channel-dominated devices, taken at low drain bias; or gated four-probe or impedance measurements that isolate the channel; output curves at low drain bias shown to be linear before linear-regime formulas are applied.

**Benchmark.** [1], [2]

## 3. Hysteresis, sweep conditions and bias stress

**Question.** Are forward and backward gate sweeps shown, with the sweep rate, hold time and maximum bias stated, and is the threshold shift between them carried into the uncertainty of the threshold voltage and of every quantity that depends on it?

**Why it matters.** Traps in the gate insulator near the channel capture and release charge with a wide spread of time constants, so the threshold voltage shifts during a sweep and drifts under sustained bias. The size of the hysteresis depends on sweep rate, bias range and hold time, and stress at high drain and gate bias can shift the threshold between one measurement and the next. A single sweep therefore gives a threshold and a subthreshold swing that may not describe the device in steady state.

**Resolved by.** Both sweep directions plotted, with sweep conditions listed; the hysteresis width reported and, where claims depend on it, measured at more than one sweep rate; the subthreshold swing given for both sweep directions; the order of measurements stated so that stress from one does not pass unnoticed into the next.

**Benchmark.** [1], [3]

## 4. Gate leakage

**Question.** Is the gate current plotted against gate voltage on the same logarithmic axes as the drain current, and is it small compared with the drain current at every bias used to extract the off current, the subthreshold swing, the mobility or the carrier density?

**Why it matters.** Current that leaks through the gate insulator, by direct, field-assisted or trap-assisted tunnelling, adds to or dominates the measured off current, which then sets the on/off ratio. In electrolyte gating, a gate current that overshoots and decays slowly when the gate is switched, and reverses when it is removed, points to a chemical reaction and not to charging alone.

**Resolved by.** The gate current shown for every transfer curve used in the analysis, well below the drain current where parameters are extracted; the off current compared with both the gate current and the instrument noise floor; for electrolyte gates, the time trace of gate current on switching, showing a fast displacement current.

**Benchmark.** [1], [3], [4], [6]

## 5. Carrier density from capacitance and from Hall measurements

**Question.** How was the carrier density obtained: from a measured or an assumed gate capacitance multiplied by the gate voltage above threshold, or from Hall measurements, and where both are available, do they agree?

**Why it matters.** The permittivity of a thin or high-permittivity insulator is hard to know in advance, and in channels with a low density of states the quantum capacitance acts in series with the insulator, so the charge per volt is lower than the insulator capacitance alone predicts. In electrolyte gating, a carrier change far larger than the double-layer capacitance can supply shows that something other than electrostatic charging is changing the transport.

**Resolved by.** The gate capacitance measured by capacitance-voltage or capacitance-frequency methods, not taken from a nominal permittivity; the quantum capacitance considered where the density of states is low; the threshold uncertainty carried into the density; Hall densities compared with the density expected from the capacitance over the same gate range, and any disagreement discussed.

**Benchmark.** [1], [5]

## 6. Electrostatic or electrochemical gating

**Question.** For ionic-liquid, ion-gel or electrolyte gating, does the paper establish whether the change it reports is electrostatic accumulation of carriers or an electrochemical change in the material, such as vacancy formation, ion insertion or surface redox?

**Why it matters.** The large interfacial fields that make these gates attractive can also drive ions or vacancies into or out of the channel or oxidize and reduce its surface, and which mechanism dominates differs between materials and with the gate voltage applied. Electrochemical changes can extend far deeper than the electrostatic screening length and can still be reversible, so reversibility under a reverse gate bias does not by itself show that the gating was electrostatic.

**Resolved by.** The state recovered when the gate voltage is returned to zero, without a reverse bias; the voltage window of purely electrostatic behaviour identified, with the gate current monitored; a carrier density consistent with the double-layer capacitance; direct probes of the channel under gate bias, such as X-ray absorption or other spectroscopy, and measurements under a controlled atmosphere, where an electrochemical route is plausible.

**Benchmark.** [4], [5]

## 7. Potential at the channel and charging time in electrolyte gating

**Question.** In electrolyte-gated devices, does the paper measure the potential at the channel with a reference electrode, and does it show that the double layer had finished forming at each gate step before the data were taken?

**Why it matters.** The applied gate voltage divides between the gate-electrolyte and electrolyte-channel interfaces in a way that is not linear in the gate voltage and can drift or show hysteresis. Ion layers can take from tens of seconds to tens of minutes to form, so a fast sweep gives large hysteresis and a gate-voltage axis that does not represent the potential at the channel.

**Resolved by.** A reference electrode in the electrolyte and the channel data plotted against its potential; the time evolution of the channel current after a gate step shown; sweep rates and waiting times stated and slow enough for the current to settle; the gate current recorded throughout.

**Benchmark.** [6]

## 8. Figures of merit compared on equal terms

**Question.** When the paper compares on/off ratio, subthreshold swing, on current or mobility with other devices, does it state the drain and gate biases, the operating regime, the carrier density and the channel dimensions at which each value was taken?

**Why it matters.** These figures of merit depend on channel length, insulator thickness and permittivity, gating geometry and bias, so values taken at the same drain voltage can represent different regimes in different devices. The minimum current is often limited by the instrument or by leakage, and the on current depends on the carrier density at which it is read, so comparisons that omit these conditions can mislead.

**Resolved by.** Each figure of merit given with its bias, regime and carrier density; the maximum and minimum currents reported with the biases at which they were read; the subthreshold swing plotted against drain current over several decades; channel length and width measured, with electron microscopy for very short dimensions; comparisons made at matched carrier density or field.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | Z. Cheng, C.-S. Pang, P. Wang, S. T. Le, Y. Wu, D. Shahrjerdi, I. Radu, M. C. Lemme, L.-M. Peng, X. Duan, Z. Chen, J. Appenzeller, S. J. Koester, E. Pop, A. D. Franklin and C. A. Richter, How to report and benchmark emerging field-effect transistors, Nat. Electron. 5, 416–423 (2022); read as preprint arXiv:2203.16759 with supplementary notes | doi:10.1038/s41928-022-00798-8 | full text | Fig. 1 and text: subthreshold curves on log scale with gate leakage plotted; forward and backward sweeps, with sweep rate, hold time and maximum bias listed, and hysteresis accounted for in threshold uncertainty. Mobility paragraph: field-effect mobility can be under- or overestimated relative to drift mobility depending on drain and gate bias, contact resistance, channel length and gate capacitance; state how a high mobility was obtained and cross-check, for example with four-probe data. Carrier-density paragraph: Hall is the ideal route. Electric-field paragraph: gate field and insulator permittivity are hard to measure accurately; quantum capacitance in series for low density of states. Table 1: measured insulator capacitance preferred over estimated permittivity, especially for high-k insulators; transfer-length series of at least four channels including contact- and channel-dominated devices at small drain bias; mobility plotted against carrier density; gate current plotted; microscopy for sub-20 nm dimensions. Table 2: carrier density specified for maximum current and contact resistance; SS plotted against drain current. Note S1: maximum/minimum current ratio depends on regime and on the drain and gate biases, minimum often set by the instrument and by leakage. Note S2: no standard threshold method; threshold shift between sweep types attributed to hot-carrier stress. Note S3: transfer-length contact resistance needs short contact-dominated devices and small sheet-resistance spread |
| 2 | E. G. Bittle, J. I. Basham, T. N. Jackson, O. D. Jurchescu and D. J. Gundlach, Mobility overestimation due to gated contacts in organic field-effect transistors, Nat. Commun. 7, 10908 (2016) | doi:10.1038/ncomms10908 | full text | Abstract: gate-bias-dependent contact resistance makes mobility from dc current-voltage curves overestimated by one order of magnitude or more; impedance spectroscopy separates channel from contacts. Results, current-voltage characterization: a kink separating high-slope and low-slope regions of the characteristics. Discussion: contact-correction methods suit devices with ohmic contacts that can be modelled as a series resistor |
| 3 | Y. Y. Illarionov, T. Knobloch, M. Jech, M. Lanza, D. Akinwande, M. I. Vexler, T. Mueller, M. C. Lemme, G. Fiori, F. Schwierz and T. Grasser, Insulators for 2D nanoelectronics: the gap to bridge, Nat. Commun. 11, 3385 (2020) | doi:10.1038/s41467-020-16640-8 | full text | "Gate leakage current" subsection: direct, Fowler-Nordheim and trap-assisted tunnelling through thin insulators. "Border traps and device stability" subsection and Fig. 5: border traps with widely distributed capture and emission times cause hysteresis and bias-temperature instability; text notes hysteresis width falls with slower sweeps |
| 4 | K. Ueno, H. Shimotani, Y. Iwasa and M. Kawasaki, Electrostatic charge accumulation versus electrochemical doping in SrTiO3 electric double layer transistors, Appl. Phys. Lett. 96, 252107 (2010); read as preprint arXiv:1006.3847 | doi:10.1063/1.3457785 | full text | Text on Fig. 1(b): below a threshold gate voltage the conductance switches reversibly and the gate current is a fast displacement current; above it the gate current overshoots with slow decay and turns negative on removal, a sign of electrochemical reaction, and conduction persists after the gate is removed. Fig. 2: a distinct gate-voltage window of electrostatic accumulation. Fig. 3 and Fig. 4 text: the conductive region is about 10 µm thick, against about 10 nm for the accumulation layer |
| 5 | T. A. Petach, M. Lee, R. C. Davis, A. Mehta and D. Goldhaber-Gordon, Mechanism for the large conductance modulation in electrolyte-gated thin gold films, Phys. Rev. B 90, 081108 (2014); read as preprint arXiv:1603.08286 | doi:10.1103/PhysRevB.90.081108 | full text | Introduction: reported electrolyte-gated carrier densities exceed typical double-layer capacitance by more than an order of magnitude. Impedance section and Fig. 3: double-layer capacitance measured by electrochemical impedance spectroscopy implies a carrier change 35 times smaller than the change in Hall coefficient. Fig. 1 and Fig. 4: measurements in controlled atmosphere; X-ray absorption shows reversible surface oxidation and reduction |
| 6 | D. Vaquero, V. Clericò, J. Salvador-Sánchez, J. Quereda, E. Diez and A. M. Pérez-Muñoz, Ionic-liquid gating in two-dimensional TMDs: the operation principles and spectroscopic capabilities, Micromachines 12, 1576 (2021) | doi:10.3390/mi12121576 | full text | Sec. 2.2: channel current after a gate step follows two time constants, about 30 s and 23 min. Sec. 2.3: gate voltage divides between the two interfaces non-linearly, with drift or hysteresis, so a reference electrode is needed. Sec. 2.4: large hysteresis against gate voltage from slow ion diffusion shrinks when plotted against reference potential. Sec. 2.5: gate leakage current measured |
