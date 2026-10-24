---
id: T-ELECTROPHYSIOLOGY
name: Membranes and electrophysiology
type: technique
field: physics/biological
applies_when: the paper reports patch-clamp, whole-cell, planar lipid bilayer or other electrical recordings from cells, membranes or ion channels, or bases a claim about channel gating, conductance, selectivity, pharmacology, single-channel events or the identity of a channel on them
version: "0.1"
---

# Membranes and electrophysiology

Patch-clamp recording (cell-attached, whole-cell, inside-out and outside-out patches) and planar lipid bilayer recording are used to claim the size, voltage dependence and kinetics of ionic currents, single-channel conductance and open probability, ion selectivity, the action of drugs, and that a particular protein forms or carries a channel. All of these are inferred from picoampere to nanoampere currents measured through a glass pipette or across an artificial membrane, at a membrane voltage that is set by the amplifier only as well as the recording allows.

## 1. Seal resistance and leak

**Question.** Does the paper state the seal resistance (or, for bilayers, the membrane resistance) for the recordings used, the minimum it accepted, and how leak current was measured and subtracted?

**Why it matters.** The seal between pipette and membrane sets both the background noise and the leak current that flows alongside the current of interest. A low seal resistance adds noise that hides small events and a leak that is easily mistaken for, or subtracted into, a genuine conductance, and leak subtraction itself rests on assumptions, such as that no channel current flows during the step used to estimate the leak.

**Resolved by.** Seal or membrane resistance reported for the recordings, with the acceptance threshold (typically in the gigaohm range); the leak protocol and subtraction method stated, with raw and leak-subtracted traces available for comparison; recordings whose leak changed during the experiment excluded by a stated rule.

**Benchmark.** [1], [2], [3], [4]

## 2. Series resistance and voltage control

**Question.** For whole-cell recordings, does the paper report the series (access) resistance, the fraction compensated, the membrane capacitance and the size of the largest currents, so that the voltage error can be estimated?

**Why it matters.** Current flowing through the uncompensated series resistance makes the membrane voltage differ from the command voltage by the product of the two, which reaches several millivolts or more for nanoampere currents. This shifts and flattens activation and inactivation curves, slows apparent kinetics and distorts dose-response curves, and much of the apparent cell-to-cell variability in kinetics can come from these artefacts rather than from the channels.

**Resolved by.** Series resistance before and after compensation, and the compensation percentage, stated for each data set; peak current amplitudes kept below a limit at which the voltage error is small, or the voltage error estimated; voltage-dependence parameters shown not to depend on current amplitude; acceptance limits on series resistance stated and applied.

**Benchmark.** [3], [4]

## 3. Liquid junction potentials and voltage offsets

**Question.** Does the paper state whether membrane voltages were corrected for liquid junction potentials between pipette, bath and reference solutions, how the correction was obtained, and whether further corrections were made when solutions were changed during a recording?

**Why it matters.** Junction potentials between solutions of different composition are often 5 to 10 mV or more, and together with electrode and amplifier offsets they shift every voltage in the paper. Uncorrected or wrongly signed offsets change reported activation voltages and reversal potentials, and so the permeability ratios and selectivity conclusions drawn from them.

**Resolved by.** The junction potential stated with its sign, calculated from the solution compositions or measured, and the paper saying whether voltages were corrected; additional corrections described for experiments in which the bath solution was exchanged, as in ion-substitution measurements of selectivity.

**Benchmark.** [5], [6], [3]

## 4. Space clamp

**Question.** When currents are recorded from cells that are not compact, such as neurons with dendrites and axons, or coupled cells, does the paper show that the voltage was uniform over the membrane carrying the current, or limit its claims accordingly?

**Why it matters.** A single electrode controls the voltage only near its tip. In extended cells the distant membrane is not at the command voltage, so voltage-gated currents and remote synaptic currents are distorted in amplitude, kinetics, voltage dependence and reversal potential, even in cells with short processes. Passive cable arguments do not remove the problem once voltage-gated channels open.

**Resolved by.** Recordings from compact cells, isolated patches or reduced preparations when voltage dependence or kinetics are claimed; reversal potentials checked against those expected for the ions involved; where a remote input is studied, an estimate of the voltage error, for example from a second electrode or a model of the cell; claims about remote currents stated as approximate.

**Benchmark.** [7], [8]

## 5. Washout and stability over time

**Question.** Does the paper show that the currents studied were stable over the duration of each recording, and does it consider whether dialysis of the cell by the pipette solution changed them?

**Why it matters.** In conventional whole-cell recording the pipette solution exchanges with the cytoplasm, and cytoplasmic factors that a current or a signalling response depends on can be washed out within minutes. A current that runs down, or a response that fades with time, can then be mistaken for the effect of a drug or a condition applied later in the recording.

**Resolved by.** Current amplitude and recording parameters plotted against time in the recording; time-matched recordings without the treatment showing the extent of rundown; the order of conditions varied or reversed where possible; perforated-patch or cell-attached recordings used when an intact cytoplasm matters.

**Benchmark.** [9], [2]

## 6. Bilayer stability, incorporation and contamination

**Question.** For planar bilayer recordings, does the paper show that the bilayer was stable and free of channel-like activity before the protein was added, describe how the protein was incorporated, and exclude conductances from lipids, solvents, detergents or contaminating proteins?

**Why it matters.** Planar bilayers are mechanically fragile and can break or reform during solution exchange, and incorporating a channel without contamination is a recognised difficulty of the method. Protein-free lipid vesicles and membranes near a lipid phase transition can produce step-like, gating, selective events that cannot be told apart from protein channels by inspecting the traces.

**Resolved by.** Bilayer capacitance and resistance reported before insertion, with a period of recording showing no events; vesicle, buffer and detergent additions without the protein showing no events; protein purity shown and the source of the protein stated; conductance and selectivity of the events consistent across insertions; stated rules for discarding membranes that broke or changed.

**Benchmark.** [10], [11], [12]

## 7. Detection of single-channel events

**Question.** For single-channel claims, does the paper state the recording bandwidth and filter, the detection method and threshold, the shortest event that could be resolved, and how missed and false events were handled in dwell-time and open-probability estimates?

**Why it matters.** Filtering needed to reduce noise prevents brief openings and closings from reaching the detection threshold, so they are missed and neighbouring intervals merge into longer ones, which lengthens apparent dwell times and biases rate constants. Noise can also create false brief events that shorten them. When a patch holds more than one active channel, the number of channels has to be estimated before open probability and dwell times can be assigned to one channel, and no single way of estimating it is reliable in every case.

**Resolved by.** Filter type and cut-off, sampling rate and detection method stated; a time resolution imposed and stated, with missed events corrected for in kinetic fitting or the results limited to events longer than that resolution; amplitude histograms showing the closed and open levels and any subconductance levels; the number of active channels in the patch shown or estimated.

**Benchmark.** [2], [13], [15]

## 8. Which channel carries the current

**Question.** What evidence shows that the recorded current comes from the channel the paper names, and not from endogenous channels of the expression system, other channels in the preparation, or the membrane itself?

**Why it matters.** Cells used for expression, such as HEK cells, carry endogenous channels whose currents can be substantial and can be mistaken for, or added to, the expressed current, especially when the expressed current is small. Voltage protocols designed for one current can be contaminated by endogenous currents, and channel-like events in reconstituted membranes do not by themselves identify a protein.

**Resolved by.** Untransfected or mock-transfected cells recorded under the same protocol, with their current amplitude stated; currents well above that background; identification based on several properties together, such as unitary conductance, reversal potential and permeability sequence, and block by drugs at stated concentrations; for reconstituted protein, controls without the protein and agreement with properties measured in cells.

**Benchmark.** [2], [14], [4], [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | O. P. Hamill, A. Marty, E. Neher, B. Sakmann and F. J. Sigworth, Improved patch-clamp techniques for high-resolution current recording from cells and cell-free membrane patches, Pflügers Arch. 391, 85–100 (1981) | doi:10.1007/BF00656997 | abstract | Abstract: pipette-membrane seals of 10^9 to 10^11 ohm (giga-seals) are the basis of improved current resolution; describes the whole-cell, inside-out and outside-out configurations and the limits on single-channel recording |
| 2 | L. Catacuzzeno and F. Franciolini, Celebrating 50 years of single-channel recording with the patch clamp, J. Membr. Biol. 258, 429–445 (2025) | doi:10.1007/s00232-025-00362-3 | full text | Prologue and "Gigaseal Formation": early seals were 50–100 MΩ; seal resistance sets the thermal noise from ions leaking through the seal (about 0.4 pA rms at 100 MΩ against 0.04 pA at 10 GΩ), and gigaseals cut background noise by more than an order of magnitude. "The 'Whole-cell' Configuration": the pipette solution replaces the cytoplasm and washes out cellular factors. "Idealization of Single-channel Records and the Problem of Missed Events": the half-amplitude threshold with heavy filtering misses brief events and lengthens dwell times, noise creates false events, correction methods and hidden Markov analysis. "Constructing Amplitude Histograms": one closed and one open peak, extra open peaks as subconductance states, peak areas giving open probability, and unitary amplitudes measured across ionic conditions and voltages helping to characterise or identify a channel. Introduction: block by TEA and TTX used as evidence for separate sodium and potassium pathways |
| 3 | C. L. Lei, M. Clerx, D. G. Whittaker, D. J. Gavaghan, T. P. de Boer and G. R. Mirams, Accounting for variability in ion current recordings using a mathematical model of artefacts in voltage-clamp experiments, Phil. Trans. R. Soc. A 378, 20190348 (2020); read as the open-access version in PubMed Central (PMC7287334) | doi:10.1098/rsta.2019.0348 | full text | Secs. 1 and 2 with Table 1: series resistance (typically 5–20 MΩ) makes membrane voltage differ from command voltage, compensation typically 70–85%; seal resistance 0.5–10 GΩ and leak estimated on a step and subtracted; voltage offset from amplifier, electrode and junction potentials, of order 10 mV. Sec. 4 and Abstract: most cell-to-cell variability in the recordings is explained by artefacts rather than by different channel kinetics |
| 4 | J. Montnach, M. Lorenzini, A. Lesage, I. Simon, S. Nicolas, E. Moreau, C. Marionneau, I. Baró, M. De Waard and G. Loussouarn, Computer modeling of whole-cell voltage-clamp analyses to delineate guidelines for good practice of manual and automated patch-clamp, Sci. Rep. 11, 3282 (2021) | doi:10.1038/s41598-021-82077-8 | full text | Introduction and Results: the voltage error equals series resistance times current and reaches tens of millivolts for 10 nA currents; it shifts half-activation voltages by several millivolts, changes slope factors, delays time to peak and raises the apparent IC50. Discussion: plot half-activation and slope against peak current, compensate series resistance, keep currents below channel-specific limits. Methods: seal above 0.5 GΩ and series resistance below 10 MΩ as inclusion criteria on the automated platform. Results: in HEK293 cells on that platform, activation parameters of currents below 500 pA were poorly determined, which the authors tentatively attribute to endogenous currents |
| 5 | P. H. Barry, T. M. Lewis and A. J. Moorhouse, An optimised 3 M KCl salt-bridge technique used to measure and validate theoretical liquid junction potential values in patch-clamping and electrophysiology, Eur. Biophys. J. 42, 631–646 (2013) | doi:10.1007/s00249-013-0911-3 | abstract | Abstract: potential measurements need correction for liquid junction potentials, which in patch-clamping can often be about 5–10 mV or more; a salt-bridge method measures them and confirms values calculated from the Henderson equation |
| 6 | A. Amtmann and D. Sanders, A unified procedure for the correction of liquid junction potentials in patch clamp experiments on endo- and plasma membranes, J. Exp. Bot. 48, 361–364 (1997) | doi:10.1093/jxb/48.Special_Issue.361 | abstract | Abstract: correct values and polarities of junction potentials between bath, pipette and reference salt bridge are essential for estimating ionic selectivities and activation voltages of channels; the procedure covers all patch configurations |
| 7 | D. Bar-Yehuda and A. Korngreen, Space-clamp problems when voltage clamping neurons expressing voltage-gated conductances, J. Neurophysiol. 99, 1127–1136 (2008) | doi:10.1152/jn.01232.2007 | abstract | Abstract: voltage clamp works properly only for compact cells; in neurons the recorded current mixes local and axial currents; simulations and recordings show substantial distortion of potassium and calcium currents even with short dendrites, and passive cable theory does not justify the clamp because of shunting when channels open |
| 8 | S. R. Williams and S. J. Mitchell, Direct measurement of somatic voltage clamp errors in central neurons, Nat. Neurosci. 11, 790–798 (2008) | doi:10.1038/nn.2137 | abstract | Abstract: simultaneous somatic and dendritic recordings show that a somatic clamp does not control dendritic voltage; errors in the amplitude, kinetics, slope conductance and reversal potential of synaptic currents depend on distance from the soma |
| 9 | R. Horn and A. Marty, Muscarinic activation of ionic currents measured by a new whole-cell recording method, J. Gen. Physiol. 92, 145–159 (1988) | doi:10.1085/jgp.92.2.145 | abstract | Abstract: in conventional whole-cell recording, washout of cytoplasmic constituents makes a receptor-activated response fade within about 5 minutes; with a nystatin-perforated patch the response was intact after an hour |
| 10 | D. J. Woodbury, Pure lipid vesicles can induce channel-like conductances in planar bilayers, J. Membr. Biol. 109, 145–150 (1989) | doi:10.1007/BF01870853 | abstract | Abstract: protein-free lipid vesicles ejected near a planar bilayer produced step changes, flickering, ion selectivity and inactivation usually taken as evidence of reconstituted channels, so such conductance changes need cautious interpretation |
| 11 | A. Blicher and T. Heimburg, Voltage-gated lipid ion channels, PLoS ONE 8, e65707 (2013) | doi:10.1371/journal.pone.0065707 | full text | Introduction: protein-free lipid membranes show channel-like events, most likely near melting transitions, with conductances of several tens to about 100 pS; such events are strikingly similar to protein channels in the traces, and some events in the literature may be misattributed; protein channels keep a consistent unitary conductance whereas lipid conductance varies between experiments. Results and Discussion: voltage-dependent open probability and non-exponential dwell times |
| 12 | M. El Khoury, T. Winterstein, W. Weber, V. Stein, H. F. Schlaak and G. Thiel, Photolithographic fabrication of micro apertures in dry film polymer sheets for channel recordings in planar lipid bilayers, J. Membr. Biol. 252, 173–182 (2019) | doi:10.1007/s00232-019-00062-9 | full text | Introduction: incorporation of channels without contamination and the mechanical instability of the bilayer are inherent problems of the method; large apertures raise capacitance and noise. Results and Discussion: removing solution from a conventional chamber usually destroys the bilayer, which reforms without the channel; capacitance and resistance measured with voltage ramps |
| 13 | Y. Geng and K. L. Magleby, Single-channel kinetics of BK (Slo1) channels, Front. Physiol. 5, 532 (2015) | doi:10.3389/fphys.2014.00532 | full text | Section "Estimating parameters and ranking kinetic gating mechanisms": low-pass filtering can attenuate very brief intervals so they go undetected; a missed closing merges two openings into one longer opening and a missed opening merges two closings; corrections for missed events and limited time resolution are applied when fitting |
| 14 | A. Varghese, E. M. Tenbroek, J. Coles and D. C. Sigg, Endogenous channels in HEK cells and potential roles in HCN ionic current measurements, Prog. Biophys. Mol. Biol. 90, 26–37 (2006) | doi:10.1016/j.pbiomolbio.2005.05.002 | abstract | Abstract: endogenous voltage-gated potassium channels in HEK cells, untransfected and HCN-transfected, give substantial outward current at positive potentials, so pulse protocols with positive tail pulses give inaccurate measurements of the expressed HCN current in some HEK cells |
| 15 | R. Horn, Estimating the number of channels in patch recordings, Biophys. J. 60, 433–439 (1991) | doi:10.1016/S0006-3495(91)82069-0 | abstract | Abstract: estimating the number of channels in a patch is treated as estimating a binomial parameter; of seven estimators tested on simulated single-channel data none was best for all parameters; all were accurate for one channel, the maximum number of simultaneously open channels was best for up to four, and Bayesian estimators for more |
