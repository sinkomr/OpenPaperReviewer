---
id: T-NEURAL-IMAGING
name: Optical recording of neural activity
type: technique
field: physics/biological
applies_when: the paper records neural activity by calcium or voltage imaging with genetically encoded or synthetic indicators, and bases a claim on fluorescence changes, inferred spikes or events, response properties, correlations between cells, or the activity of identified cells or cell types
version: "0.1"
---

# Optical recording of neural activity

Calcium imaging and voltage imaging use fluorescent indicators, genetically encoded calcium indicators (GECIs) such as GCaMP, genetically encoded voltage indicators (GEVIs) or synthetic dyes, to claim when and how strongly identified neurons were active, how they respond to stimuli or behaviour, and how their activity is correlated. These claims are inferred from fluorescence changes (often expressed as ΔF/F, the change in fluorescence relative to a baseline F0) in regions of interest (ROIs) drawn on images recorded by one-photon or two-photon microscopy.

## 1. Indicator kinetics and what the signal can resolve

**Question.** Does the paper state the indicator, its rise and decay times and its response to a single action potential under the conditions used, together with the frame rate, and are the claims about spike timing, firing rate or single spikes within what that indicator and sampling can resolve?

**Why it matters.** A calcium signal is a slow, filtered version of spiking: sensitive GECIs decay over hundreds of milliseconds, so spikes closer together than roughly the rise time merge, timing is imprecise, and single spikes may be missed. Voltage signals from action potentials last only milliseconds and need frame rates of several hundred hertz or more. The response to one spike also varies widely between neurons, even with the same indicator.

**Resolved by.** The indicator, its kinetics and the frame rate stated; claims about timing, rates or isolated spikes matched to those values; where single spikes or precise timing matter, a calibration against simultaneous electrophysiology in the same preparation, or a citation to one under comparable conditions, with the spread across neurons shown.

**Benchmark.** [1], [2], [3]

## 2. Spike inference and event detection

**Question.** If spikes, events or rates are inferred from fluorescence, which algorithm and parameters were used, how was the detection threshold chosen, and was the method validated against ground-truth electrophysiology recorded with the same indicator and imaging conditions?

**Why it matters.** Even the best spike inference methods recover only part of the spike train, their performance changes between data sets and indicators, and without tuning on ground truth most single spikes can go undetected. Non-negative deconvolution produces false events, and the event threshold changes derived measures such as the fraction of responsive cells and their selectivity. Methods that assume activity only rises above baseline misread decreases in activity and can report spurious spikes when the signal returns to baseline.

**Resolved by.** The inference method, its parameters and the event threshold stated relative to each cell's noise; validation against simultaneous electrophysiology, held out by neuron, or a citation to a benchmark using the same indicator; key results shown to hold on the fluorescence traces or across reasonable thresholds; claims about suppressed activity based on traces, not on non-negative event estimates.

**Benchmark.** [3], [4], [5], [6]

## 3. Motion correction and motion-related artefacts

**Question.** How was brain motion corrected (rigid or non-rigid registration), how was the residual motion assessed, and does the paper rule out that fluorescence changes locked to movement, licking or running come from motion that registration cannot remove, such as movement out of the focal plane?

**Why it matters.** Raster scanning and deformation of the brain produce motion that varies across the field of view, and rigid registration can leave large residual displacements. Movement and deformation can change a cell's measured fluorescence even when its activity is constant, and when that motion is correlated with behaviour it produces apparent behaviour-related activity.

**Resolved by.** The registration method stated, with a measure of registration quality such as correlation of frames with a template or residual displacement; motion traces shown alongside the behaviour; an activity-independent reference, such as a co-expressed red fluorophore or animals expressing a calcium-insensitive fluorescent protein, showing that the behaviour-related signal is absent when the fluorescence does not report activity; frames or periods with large motion handled by a stated rule.

**Benchmark.** [7], [8]

## 4. Neuropil and overlapping sources

**Question.** How was fluorescence from surrounding neuropil, from neighbouring cells and from processes passing through each ROI removed or modelled (for example a subtraction coefficient or a demixing method), with what parameters, and do the main results survive changes to that correction?

**Why it matters.** Neuropil fluorescence is highly correlated with activity over long distances, so an uncorrected soma trace inherits tuning and correlations from its surroundings. Fixed subtraction coefficients and demixing methods both leave contamination from unidentified cells and processes, which creates transients a cell did not produce. This can add apparent response fields and inflate correlations between nearby cells, especially in one-photon imaging.

**Resolved by.** The neuropil model and coefficient stated, and how it was estimated; results shown with and without, or with different strengths of, the correction; checks that individual transients match the spatial footprint of their ROI; correlations between nearby cells compared with distance between them; where available, soma-targeted or nuclear-localised indicators, which reduce crosstalk from processes.

**Benchmark.** [9], [10], [11], [12]

## 5. Baseline fluorescence and normalisation

**Question.** How was the baseline F0 defined (fixed period, percentile, running window), was background or neuropil subtracted before dividing by it, and are amplitudes compared between cells, conditions or sessions on a scale that does not depend on that choice?

**Why it matters.** ΔF/F depends on what is taken as baseline. A running baseline can turn a decrease in fluorescence into an apparent increase afterwards, and photobleaching makes the baseline drift over long recordings. A small or poorly estimated F0, as in dim cells whose resting fluorescence is close to autofluorescence or background, inflates ΔF/F, and summed event amplitudes weight bursts much more than isolated spikes.

**Resolved by.** The baseline definition, window and percentile stated, with the order of background subtraction and division; raw or z-scored traces shown alongside ΔF/F for key results; the result checked with a second baseline definition; dim cells excluded by a stated brightness criterion; comparisons of amplitude between groups that differ in expression or brightness argued explicitly.

**Benchmark.** [2], [5], [6], [12]

## 6. Effects of the indicator on the cells

**Question.** What was the expression method, level and duration, does the paper exclude cells with abnormal expression such as indicator filling the nucleus, and for transgenic lines, does it check for activity that the indicator or the line itself introduces?

**Why it matters.** After long, strong expression some neurons accumulate indicator in the nucleus and then respond abnormally. Some transgenic lines expressing calcium indicators show large, widespread interictal-like events in cortex that a small field of view can miss. Voltage indicators add charge movement to the membrane and can change the electrical properties being measured.

**Resolved by.** The expression method, promoter, line and time since expression stated; nuclear-filled cells identified and excluded by a stated rule; for transgenic lines, a check for widespread synchronous events over a large field of view or a line known not to show them; key results confirmed with another indicator, expression method or recording technique.

**Benchmark.** [1], [13], [15]

## 7. Photobleaching, heating and phototoxicity

**Question.** What excitation wavelength, power at the sample, scan area, duty cycle and session length were used, how was photobleaching measured and corrected, and does the paper show that illumination did not change the activity being reported?

**Why it matters.** Photobleaching lowers the signal over a session and, if uncorrected, appears as a trend in activity; high frame rates for voltage imaging need high intensities that bleach faster. Two-photon illumination heats tissue roughly in proportion to the average power, and at high continuous power produces glial activation and cell damage, with effects on neural activity expected at lower temperature rises. Light can also damage membranes through reactive oxygen species.

**Resolved by.** Power at the sample, wavelength, scan area and duty cycle reported, with an estimate of heating; bleaching shown as raw fluorescence over the session and its correction stated; responses compared between early and late parts of a session, or across powers; for long or high-power protocols, a check of tissue health or of activity with lower illumination.

**Benchmark.** [2], [12], [14], [15]

## 8. Attributing activity to identified cells

**Question.** How were ROIs selected as cell bodies (manual, automatic, with what criteria and curation), how were cells matched across sessions, and how was the cell type or projection target of each imaged cell established?

**Why it matters.** Human annotators disagree on which ROIs are cells, and automatic classifiers return probabilities, so ROIs that are dendrites or neuropil can enter the analysis. Matching cells across sessions has false and missed matches that bias measures of stability, and changes in focal plane between sessions add to them. Expression in a genetically defined population does not guarantee that every labelled cell is of that type.

**Resolved by.** The segmentation method, its thresholds and the curation rule stated, with the number of ROIs kept and rejected; a check that results do not depend on low-confidence ROIs; cross-session matching with a stated confidence and estimated error rate, and the field of view shown to be stable; cell identity confirmed by a second marker, such as post hoc histology or a co-expressed label, with the specificity of the expression stated.

**Benchmark.** [2], [9], [12], [16]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | T.-W. Chen, T. J. Wardill, Y. Sun, S. R. Pulver, S. L. Renninger, A. Baohan, E. R. Schreiter, R. A. Kerr, M. B. Orger, V. Jayaraman, L. L. Looger, K. Svoboda and D. S. Kim, Ultrasensitive fluorescent proteins for imaging neuronal activity, Nature 499, 295–300 (2013) | doi:10.1038/nature12354 | full text | Sec. "Imaging neuronal populations in the mouse visual cortex" and Fig. 3: single-spike detection calibrated with simultaneous loose-seal recordings; spikes in a burst give separate steps only when spaced by about the sensor rise time, tens to over a hundred milliseconds depending on variant. Same section and Supplementary Fig. 7: after months of expression a small fraction of strongly expressing neurons showed nuclear fluorescence and later aberrant responses. Methods "Image analysis": only cells identifiable in every session analysed |
| 2 | M. Z. Lin and M. J. Schnitzer, Genetically encoded indicators of neuronal activity, Nat. Neurosci. 19, 1142–1153 (2016); read as the author manuscript in PubMed Central | doi:10.1038/nn.4359 | full text | Calcium indicator sections: fast GECIs give about 20% response to one spike with a decay of over 100 ms, making spike timing imprecise and spike inference only partly accurate; voltage signals from spikes last about 2 ms and need sampling above 300 Hz. Expression sections: at low expression baseline fluorescence is hard to separate from autofluorescence, and transgenic lines may express in unintended cell types. Voltage indicator sections: high frame rates need high intensity, which speeds photobleaching |
| 3 | L. Huang, P. Ledochowitsch, U. Knoblich, J. Lecoq, G. J. Murphy, R. C. Reid, S. E. J. de Vries, C. Koch, H. Zeng, M. A. Buice, J. Waters and L. Li, Relationship between simultaneously recorded spiking activity and fluorescence signal in GCaMP6 transgenic mice, eLife 10, e51675 (2021) | doi:10.7554/eLife.51675 | full text | Abstract: under population-imaging conditions only a minority of single-spike events were detected. Results "Calcium transients differ across mouse lines": single-spike detection probability spanned a wide range across neurons, and trial-to-trial variability exceeded photon shot noise in most neurons. Results on field of view and blind inference, and Discussion: with blind inference most single-spike events went undetected; caution in interpreting inferred spike rates; the spike-to-fluorescence relation may differ for each neuron |
| 4 | P. Berens, J. Freeman, T. Deneux, N. Chenkov, T. McColgan, A. Speiser, J. H. Macke, S. C. Turaga, P. Mineault, P. Rupprecht, S. Gerhard, R. W. Friedrich, J. Friedrich, L. Paninski, M. Pachitariu, K. D. Harris, B. Bolte, T. A. Machado, D. Ringach, J. Stone, L. E. Rogerson, N. J. Sofroniew, J. Reimer, E. Froudarakis, T. Euler, M. Román Rosón, L. Theis, A. S. Tolias and M. Bethge, Community-based benchmarking improves spike rate inference from two-photon calcium imaging data, PLoS Comput. Biol. 14, e1006157 (2018) | doi:10.1371/journal.pcbi.1006157 | full text | Results and Fig. 1: the best algorithms reached a mean correlation with ground-truth spike rates of about 0.44, and performance differed substantially between data sets and indicators. Discussion and Methods: evaluation against simultaneous electrophysiology, test data held out by neuron, overfitting and dataset-specific adaptation noted |
| 5 | J. H. Siegle, P. Ledochowitsch, X. Jia, D. J. Millman, G. K. Ocker, S. Caldejon, L. Casal, A. Cho, D. J. Denman, S. Durand, P. A. Groblewski, G. Heller, I. Kato, S. Kivikas, J. Lecoq, C. Nayan, K. Ngo, P. R. Nicovich, K. North, T. K. Ramirez, J. Swapp, X. Waughman, A. Williford, S. R. Olsen, C. Koch, M. A. Buice and S. E. J. de Vries, Reconciling functional differences in populations of neurons recorded with two-photon imaging and electrophysiology, eLife 10, e69068 (2021) | doi:10.7554/eLife.69068 | full text | Results on response magnitudes: summed event amplitudes make bursts count far more than isolated spikes. Results on event detection: unpenalized non-negative deconvolution gives more false events, and the event threshold shifts responsiveness and selectivity; derived functional classes inherit these shifts |
| 6 | G. Vanwalleghem, L. Constantin and E. K. Scott, Calcium imaging and the curse of negativity, Front. Neural Circuits 14, 607391 (2021) | doi:10.3389/fncir.2020.607391 | full text | Results on ΔF/F: a moving baseline produces positive artefacts after a decrease below baseline, while z-scoring preserves the raw trace. Results on spike inference: all methods tested performed poorly on inhibited neurons and inferred spurious spikes when the signal returned to baseline. Discussion: avoid analyses that assume non-negativity before checking for decreases |
| 7 | E. A. Pnevmatikakis and A. Giovannucci, NoRMCorre: An online algorithm for piecewise rigid motion correction of calcium imaging data, J. Neurosci. Methods 291, 83–94 (2017); read as bioRxiv preprint 108514 v2 | doi:10.1016/j.jneumeth.2017.07.031 | full text | Abstract and Introduction: motion can be non-rigid from raster scanning and brain deformation, and rigid alignment can be inadequate. Sec. 3 and Table 1: rigid correction leaves the largest residual motion. Sec. 2.2: registration quality measured by correlation with the mean image, crispness of summary images and residual optical flow |
| 8 | M. S. Creamer, K. S. Chen, A. M. Leifer and J. W. Pillow, Correcting motion induced fluorescence artifacts in two-channel neural imaging, PLoS Comput. Biol. 18, e1010421 (2022) | doi:10.1371/journal.pcbi.1010421 | full text | Introduction: movement and deformation change measured fluorescence unrelated to activity, beyond what registration corrects; an activity-independent second fluorophore captures the shared artefact and simple ratios do not handle independent noise. Results "Decoding Behavior": control animals expressing a calcium-insensitive protein test whether behaviour is decodable from artefacts alone |
| 9 | M. Pachitariu, C. Stringer, M. Dipoppa, S. Schröder, L. F. Rossi, H. Dalgleish, M. Carandini and K. D. Harris, Suite2p: beyond 10,000 neurons with standard two-photon microscopy, bioRxiv 061507 (2016) | doi:10.1101/061507 | full text | Results Fig. 3 and Discussion: neuropil signal is highly correlated with the soma signal over long distances, and failing to remove it biases tuning. Stage 4: per-cell neuropil coefficients instead of a fixed value. Stage 3 and Methods: ROIs classified as somata with a probability, and results holding only for low-probability ROIs may reflect non-somatic compartments |
| 10 | J. L. Gauthier, S. A. Koay, E. H. Nieh, D. W. Tank, J. W. Pillow and A. S. Charles, Detecting and correcting false transients in calcium imaging, Nat. Methods 19, 470–478 (2022); read as bioRxiv preprint 473470 v1 | doi:10.1038/s41592-022-01422-5 | full text | Abstract and Sec. 2.1: fluorescence from unidentified or poorly outlined overlapping sources is assigned to the wrong cell, giving false transients in a sizeable fraction of transients and most sources in one data set; examples of a spurious second place field and a spurious correlation between two cells. Sec. 2.2: diagnostic comparing each transient's spatial profile with the profile of its source |
| 11 | O. A. Shemesh, C. Linghu, K. D. Piatkevich et al., Precision calcium imaging of dense neural populations via a cell-body-targeted calcium indicator, Neuron 107, 470–486 (2020) | doi:10.1016/j.neuron.2020.05.029 | full text | Introduction: signals from nearby axons and dendrites contaminate soma readouts in one-photon imaging. Results on brain slices: untargeted GCaMP gave many fluorescence events without a recorded spike, far fewer with soma targeting. Results in zebrafish and mice: pairwise correlations between nearby neurons were higher with untargeted indicators; in zebrafish, post hoc demixing (CNMF) lowered but did not remove the difference |
| 12 | A. Giovannucci, J. Friedrich, P. Gunn et al., CaImAn an open source tool for scalable calcium imaging data analysis, eLife 8, e38173 (2019) | doi:10.7554/eLife.38173 | full text | Methods "Mathematical model of the CNMF framework": neuropil and background modelled explicitly so overlapping sources can be demixed. Text on deconvolution: traces are detrended to remove non-stationary effects such as photobleaching. Results on benchmarking: human annotators agreed with consensus only with F1 scores of 0.69 to 0.94; components accepted by stated footprint, signal-to-noise and classifier criteria; cross-session registration of components described |
| 13 | N. A. Steinmetz, C. Buetfering, J. Lecoq, C. R. Lee, A. J. Peters, E. A. K. Jacobs, P. Coen, D. R. Ollerenshaw, M. T. Valley, S. E. J. de Vries et al., Aberrant cortical activity in multiple GCaMP6-expressing transgenic mouse lines, eNeuro 4, ENEURO.0207-17.2017 (2017) | doi:10.1523/ENEURO.0207-17.2017 | full text | Abstract and Results: large, widespread events resembling interictal spikes in several GCaMP6 transgenic genotypes, detected by field potentials and widefield imaging; Results and Discussion: two-photon imaging of small fields can miss them. Discussion "Notes of caution": account for germline recombination in breeding or check for it, and confirm observations with several techniques and with wild-type controls |
| 14 | K. Podgorski and G. Ranganathan, Brain heating induced by near-infrared lasers during multiphoton microscopy, J. Neurophysiol. 116, 1012–1023 (2016) | doi:10.1152/jn.00275.2016 | full text | Abstract and Results "Brain heating during two-photon imaging": about 1.8 °C rise per 100 mW for continuous scanning at 920 nm, roughly linear in power. Results "Tissue damage produced by laser heating": glial activation and damage markers at 300 mW and above continuous, less with lower duty cycle. Introduction and Discussion: temperature changes affect neural activity, so these are upper bounds |
| 15 | R. U. Kulkarni and E. W. Miller, Voltage imaging: pitfalls and potential, Biochemistry 56, 5171–5177 (2017); read as the author manuscript in PubMed Central | doi:10.1021/acs.biochem.7b00490 | full text | Section on universal challenges: action potentials need sampling near 1 kHz with far fewer photons per frame than calcium imaging; illumination can compromise membranes through reactive oxygen species; indicator charge movement in the membrane can add capacitance and change neuronal properties; mislocalised indicator adds voltage-insensitive background |
| 16 | L. Sheintuch, A. Rubin, N. Brande-Eilat, N. Geva, N. Sadeh, O. Pinchasof and Y. Ziv, Tracking the same neurons across multiple days in Ca2+ imaging data, Cell Rep. 21, 1102–1115 (2017) | doi:10.1016/j.celrep.2017.10.013 | full text | Introduction and Results: false and missed matches across sessions can lead to wrong conclusions about activity dynamics, and registration errors lower the measured fraction of stable cells. Discussion: the method gives a confidence for each match and estimated false-positive and false-negative rates for judging whether data suit longitudinal analysis, and its metrics can detect changes in the focal plane over time |
