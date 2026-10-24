---
id: T-BLIND-ANALYSIS
name: Blind analysis
type: technique
field: physics/particle
applies_when: the paper states that its analysis was blind or blinded, hid a signal region, the result, the event count or part of the data until unblinding, used a hidden offset or added or removed events, or reports changes made after unblinding
version: "0.1"
---

# Blind analysis

A blind analysis hides some aspect of the data or the result from the analysts, such as a signal region, the numerical answer behind a hidden offset, the true event count or most of the data set, until the analysis is fixed. A paper that calls its analysis blind claims that its selections, corrections and uncertainties were chosen without knowing how they moved the result, so that the result is free of experimenter's bias.

## 1. What was hidden, and whether it stayed hidden

**Question.** Does the paper say which quantity was hidden during the analysis (a signal region, the result through an offset, the event count, or most of the data), and does it show that the answer could not be read from the distributions and intermediate numbers the analysts examined while blind?

**Why it matters.** A blinding scheme protects only what it hides. When the result shows in a distribution that has to be inspected, such as a decay-time shape or an asymmetry between two samples, or when a fitted model is overlaid on the blinded data, the analysts can see the answer although the final number is hidden. A shift applied only to the printed result is a thin cover that is easily lifted by accident.

**Resolved by.** The blinding method named and matched to the kind of measurement; a description of how the plots used while blind were masked, flipped or combined so that they did not show the result; fit quality judged from residuals, not from a model drawn over blinded data; the stage of the analysis at which the blinding was applied stated.

**Benchmark.** [1], [2], [3]

## 2. Construction of a hidden offset or blinding transformation

**Question.** Where a hidden offset or a transformation of the data was used, how was it generated (distribution, width, hidden sign), was it large enough to move the result across the range of earlier measurements and predictions, and, where the transformation was applied to the data before the fit, does the paper show that it left the validation tests and goodness of fit unchanged?

**Why it matters.** An offset that is small compared with the spread of earlier results does not stop the analysts knowing whether they agree with them, and without a hidden sign they can still see which way each change moves the result. A transformation that distorts the internal consistency of the data can make validation tests pass or fail for reasons that have nothing to do with the analysis.

**Resolved by.** The offset distribution and width stated and compared with the spread of earlier results and predictions; a hidden sign, or an equivalent way of hiding the direction of changes; separate offsets for parallel analyses of the same data until they are compared; a test, for example on simulated data, showing that blinding leaves the goodness of fit and the null tests essentially unchanged; any part of the blinding lifted early, for instance to evaluate systematic uncertainties, stated with the stage at which it was lifted.

**Benchmark.** [1], [3]

## 3. Signal region and background estimate fixed while blind

**Question.** For a hidden signal region, was the expected background in that region predicted from sidebands or control samples before it was opened, without using any event inside it, and was the hidden region chosen larger than the final signal region?

**Why it matters.** A hidden signal region works only when the signal's location is known in advance and the background inside it can be estimated independently. The final signal region can be made smaller than the hidden one but not larger, so a hidden region drawn too tightly leaves no room to optimise the selection without looking. Control samples examined while blind often reveal unexpected backgrounds or miscalibrations, and these need to be dealt with before the region is opened.

**Resolved by.** The hidden region and the final signal region both defined, with the hidden one the larger; the background prediction and its uncertainty stated as fixed before opening, with the sidebands or control samples it came from; the extrapolation from control to signal region checked while blind; problems found in control samples reported together with how they were handled.

**Benchmark.** [1], [4]

## 4. What was frozen before unblinding, and who decided to unblind

**Question.** Does the paper say which elements were fixed before unblinding (selection, efficiencies, background model, systematic uncertainties, the statistical procedure including how a limit or an interval would be reported), which tests had to pass before unblinding, and who approved it?

**Why it matters.** Blinding protects only the choices made while blind. Continuing to look for mistakes until the result agrees with expectation, and then stopping, may be the most common form of experimenter's bias, and it is prevented only if the criteria for finishing are agreed before the answer is seen. A decision to unblind taken through internal review, and not by the analysts alone, makes the review before unblinding more effective.

**Resolved by.** A list of the elements frozen before unblinding; the validation tests used as unblinding criteria and their outcomes; the decision to unblind taken by a review body or wider group; a statement that the frozen procedure was applied unchanged to the unblinded data, or a pointer to the changes reported under item 5.

**Benchmark.** [1], [2], [3], [4]

## 5. Changes made after unblinding

**Question.** Were any selections, corrections, uncertainties or fit choices changed after unblinding, and if so does the paper say so explicitly, give the reason, report the result obtained before the change, and assess how the change affected the result and its significance?

**Why it matters.** Blinding does not require the analysis to stop at unblinding, nor does it make a result correct, and a known error should be fixed. But a change made after seeing the answer can reintroduce the bias that blinding was meant to remove, most of all when a selection is adjusted to reject or keep particular events in the signal region. An analysis changed after unblinding is no longer fully blind, and readers can weigh the change only if they are told about it.

**Resolved by.** The result before and after each post-unblinding change; each change listed with its reason; the statistical effect of the change on the result assessed; for outcomes that could be foreseen, such as events in the signal region that are clearly background, the treatment decided before unblinding; no selection aimed at individual events.

**Benchmark.** [1], [4]

## 6. Data examined openly to develop the analysis

**Question.** If part of the data was examined openly to develop or tune the analysis (a prescaled sample or an early run), how was that part chosen, does it span the running conditions of the full data set, and was it left out of the final result or its influence assessed?

**Why it matters.** Tuning on a subsample protects the rest of the data only if the subsample is chosen without reference to the data and samples the changes in detector, beam or background conditions over time. A large tuned subsample that is kept in the final result carries any statistical bias from the tuning into it, and a fully blind result requires that the data used to define the analysis be left out.

**Resolved by.** The fraction of the data examined openly and how it was selected, at random and in time blocks where events are correlated in time; evidence that it spans the conditions of the full run; a statement of whether it was included in the final result and, if it was, how much it contributes.

**Benchmark.** [1], [4]

## 7. Events added to or removed from the data

**Question.** Where the event count was blinded by adding an unknown number of tagged signal-like events or by removing an unknown fraction of the data, does the paper show that the added events resemble the signal, that they were all removed at unblinding, and that the removed data were restored before the final fit?

**Why it matters.** Added events that differ from real signal can be recognised and counted, which reveals the answer. Adding events alone still bounds the true count from above and so leaks some information, which removing an unknown fraction of events as well avoids. For time-correlated data, removing single events instead of blocks can distort the sample.

**Resolved by.** The source of the added events and a comparison of their distributions with the expected signal; the tag used to remove them and confirmation that they were removed; the fraction removed and whether events or time blocks were removed; the final fit repeated on the complete data after unblinding.

**Benchmark.** [1]

## 8. What the blinding does not cover

**Question.** Does the paper still evaluate instrumental and method biases as corrections or systematic uncertainties, and does it say which steps were not blind, such as event-by-event inspection, cross-checks possible only after unblinding, or a search in which the signal location was not known in advance?

**Why it matters.** Blinding addresses one problem, the influence of the analysts' expectations, and does nothing about biases from the apparatus or the method. It cannot be applied where backgrounds are removed or signals identified by inspecting events one at a time, and a hidden signal region cannot be used when the signal location is unknown, as in searches for new particles at unknown mass. A statement that an analysis was blind can then cover less of it than a reader might assume.

**Resolved by.** Systematic uncertainties evaluated in the same way as for an analysis that is not blind; the steps done openly, and the checks done only after unblinding, identified; for searches over an unknown signal location, the blinding method used, such as tuning on a separate data subset, stated.

**Benchmark.** [1], [2]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | J. R. Klein and A. Roodman, Blind analysis in nuclear and particle physics, Annu. Rev. Nucl. Part. Sci. 55, 141–163 (2005); read as preprint SLAC-PUB-12051 | doi:10.1146/annurev.nucl.55.090704.151521 | full text | Sec. 2: biased cut choice, cuts tuned to include or exclude individual events, and stopping once the result matches expectation (called probably the most common bias); unblinding decided through internal review; selections added after unblinding to be stated explicitly; blinding does not ensure correctness, does not remove instrumental biases, and cannot cover event-by-event human inspection. Sec. 3.1: hidden box needs known signal location and a background estimate independent of events in the box, should be larger than the final region, and ambiguous outcomes should be planned for. Secs. 3.2.2 and 3.2.3: offset drawn from a wide Gaussian covering earlier results, hidden sign, separate seeds for parallel analyses, sign lifted early for systematics; distributions that reveal an asymmetry hidden and fit curves not overlaid, residuals used instead. Sec. 3.3: added events must mimic signal; adding alone leaks information, so an unknown fraction is also removed, in blocks for time-correlated data. Sec. 3.4: prescaled samples chosen randomly and spanning time variations, discarded if large; hidden box unusable when the mass is unknown |
| 2 | A. Roodman, Blind analysis in particle physics, in Proceedings of PHYSTAT2003, eConf C030908, TUIT001 (2003), SLAC-PUB-10281 | https://arxiv.org/abs/physics/0312102 | full text | Sec. 2: bias from cut choice can be of the order of the statistical uncertainty, agreement with earlier results says nothing about the correctness of a measurement, and this bias cannot be estimated numerically. Sec. 3.3: the hidden variable for decay-time plots, with the fitted curve not overlaid and residuals used. Sec. 3.4: branching fractions and searches for bumps at unknown location are hard to blind. Sec. 4: review and changes made while still blind; unblinding once a wider group or review committee is satisfied |
| 3 | J. Muir, G. M. Bernstein, D. Huterer et al. (DES Collaboration), Blinding multiprobe cosmological experiments, Mon. Not. R. Astron. Soc. 494, 4454–4470 (2020); read as preprint arXiv:1911.05929 | doi:10.1093/mnras/staa965 | full text | Secs. 1 and 2.3: shifting only the final parameters is a thin cover with a high risk of accidental unblinding and can be compromised by plotting a model over the data, so blinding earlier in the pipeline is preferred. Sec. 2.1: the transformation must be able to move the result into or out of the region the analysts expect. Sec. 2.2: it must not change the outcome of validation tests or the maximum likelihood. Sec. 3.1: unblind only after the validation tests pass. Sec. 4: blinding tested on simulated data by the change in goodness of fit; unblinding criteria such as a fit-quality threshold |
| 4 | T. R. Junk and L. Lyons, Reproducibility and replication of experimental particle physics results, Harvard Data Sci. Rev. 2(4) (2020); read as preprint arXiv:2009.06864 | doi:10.1162/99608f92.250f995b | full text | Sec. 6.6: selection tuned on the data gives p values too small and signals too large; the data selection, classification and statistical procedures are fixed before unblinding and the result accepted without change, or the analysis is not fully blind; control samples examined first can reveal unexpected backgrounds or miscalibrations; early data used to tune the analysis must be left out of the final result for it to be called fully blind |
