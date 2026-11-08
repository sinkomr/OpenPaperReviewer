---
id: T-MACHINE-LEARNING-ANALYSIS
name: Machine learning in data analysis
type: technique
field: physics/methods
applies_when: the paper uses a trained machine-learning model, such as a neural network, boosted decision trees or a random forest, to classify, select, denoise, reconstruct or infer from data, or bases a claim on its scores, predictions, reconstructions or on what it has learned
version: "0.1"
---

# Machine learning in data analysis

## 1. Separation of training and test data

**Question.** How were the training, validation and test sets formed, are samples that share a source (the same specimen, run, image, simulation seed, or a near-duplicate structure or composition) kept on the same side of the split, and were preprocessing, feature selection and hyperparameter tuning done without the test set?

**Why it matters.** Information that leaks from the test set into training makes performance look better than it will be on new data, and leakage of this kind is common across fields that use ML. Randomly splitting data that contain correlated or clustered samples tests interpolation between close neighbours, while a discovery claim usually needs extrapolation to unlike cases, so the usual metrics then overstate performance.

**Resolved by.** The split procedure stated, with related samples grouped on one side, for example by specimen, run or time, or by holding out whole clusters of similar materials; preprocessing and feature selection fitted on training data only; the test set used once, after model selection; a check for duplicates across the split; each input feature shown to be available at prediction time and not a proxy for the label.

**Benchmark.** [1], [2], [3]

## 2. Origin and quality of the labels

**Question.** Where do the training and test labels come from (simulation truth, expert annotation, the output of another algorithm, an earlier measurement), how accurate are they, and how closely do they match the physical quantity the claim is about?

**Why it matters.** Deep networks can fit training labels exactly even when many are wrong, which degrades their performance on new data. Errors in test labels can change which of two models appears better. A label produced by another procedure is only a stand-in for the quantity of interest, so a model that reproduces it inherits its errors and does not by that alone show agreement with the physical truth.

**Resolved by.** The source of the labels described for each data set; an estimate of the label error rate, for example from repeated or independent annotation or from a subset labelled by a better method; test labels checked or corrected; any difference between the label and the quantity the claim concerns stated; the sensitivity of the result to label errors shown.

**Benchmark.** [2], [4], [5]

## 3. Simulated training data and real measurements

**Question.** If the model was trained on simulated or synthetic data and applied to measured data, does the paper show that the inputs the model relies on are well modelled, test the model on real data whose answer is known, and include the effect of imperfect simulation in the uncertainty of the result?

**Why it matters.** Simulations rest on approximate physics, imperfect instrument response and uncertain parameter values, so a model trained on them is not guaranteed to perform as well on real data, and its output can depend on those nuisance parameters. Both accuracy and the quality of uncertainty estimates fall as the data move away from the training distribution, so good performance on held-out simulation does not show good performance on the measurement.

**Resolved by.** Distributions of the inputs and of the model output compared between simulation and data in control samples where the answer is known; performance measured on real calibration or control data; systematic variations of the simulation passed through the trained model to the final result; a check that the measured data lie within the range covered by training, or an explicit test on data outside it.

**Benchmark.** [6], [7]

## 4. Baselines and ablations

**Question.** Is the model compared, on the same data and the same split, with the established analysis that does not use ML and with simple models tuned with comparable effort, and do ablations show which inputs or components produce the gain?

**Why it matters.** Reported advantages of complex models have shrunk or disappeared when simple baselines were tuned on an equal footing, or when leakage was corrected. Without ablations the source of a gain is unknown, and changes that do not matter appear to be necessary.

**Resolved by.** Results for the conventional analysis and for a simple model, such as a linear or logistic regression, a nearest-neighbour predictor or a cut-based selection, on the same test set; the tuning effort for each stated; an ablation table that removes inputs or components one at a time; the gain over the baseline shown to exceed the variation between training runs.

**Benchmark.** [1], [3], [8]

## 5. Variation between training runs and choice of metric

**Question.** Does the reported performance include its variation across random initialisations, data splits and hyperparameter choices, and is the performance metric suited to the class balance and to the working point that the claim needs?

**Why it matters.** Trained models vary noticeably with data sampling, initialisation and hyperparameters, so one training run can overstate a difference between methods. When the class of interest is rare, the receiver operating characteristic (ROC) curve and its area can look good while most positive predictions are false, and a precision-recall view is more informative.

**Resolved by.** Several training runs with the spread of the metric reported, and the rule for choosing the reported model stated; the metric justified for the task; for rare signals, purity or precision at the stated selection efficiency or threshold; the working point chosen on validation data, not on the test set.

**Benchmark.** [2], [9], [10]

## 6. Calibration of scores and uncertainties

**Question.** Where a classifier score is read as a probability, or a model reports uncertainties or intervals, does the paper test their calibration on held-out data, and on data like those to which the claim applies?

**Why it matters.** Modern deep networks are often overconfident, with average confidence above their accuracy, and regression intervals from a model may not contain the true value at the stated rate. Calibration on validation data from the training distribution does not guarantee calibration on shifted data, where post-hoc recalibration can fall short.

**Resolved by.** A reliability diagram or a calibration error measured on held-out test data; for intervals, the observed coverage compared with the nominal level; any recalibration fitted on validation data and evaluated separately; calibration checked on real or shifted data where the model is applied; methods that capture model uncertainty, such as ensembles, where a shift is expected.

**Benchmark.** [7], [11], [12]

## 7. Claims about what the model has learned

**Question.** When saliency maps, feature importances or internal representations are taken to show which physics the model uses, does the paper test that the explanation depends on the trained model and on the data, and does it exclude unintended cues that could give the same performance?

**Why it matters.** Some saliency methods produce similar maps for a trained network, a randomly initialised one and one trained on random labels, so a plausible-looking map does not by itself show what the model uses. Models can reach high test scores through shortcuts: cues that happen to correlate with the labels, such as an artefact of the instrument or the acquisition settings, which fail on data from other conditions. Words that suggest understanding can claim more than the tests show.

**Resolved by.** Explanations shown to change when the model weights or training labels are randomised; tests that remove or alter suspected cues; performance on data from different conditions, instruments or samples; any claim of a learned physical relationship checked against a known quantity or a prediction confirmed on new data; descriptions of the model limited to what was tested.

**Benchmark.** [8], [13], [14]

## 8. Features supplied by learned reconstruction or denoising

**Question.** When a network denoises, upsamples or reconstructs an image or signal, does the paper show that the features on which the claims rest are supported by the measured data and not supplied by what the network learned from its training set?

**Why it matters.** A learned reconstruction can add false structures in parts of the object that the measurement does not determine, and can miss small features unlike those seen in training. Small perturbations of the input can produce artefacts, and image quality does not always improve when more data are supplied.

**Resolved by.** Raw or conventionally processed data shown next to the network output; the consistency of the reconstruction with the measurement checked, for example through residuals; tests with known features inserted into the input; stability to small perturbations of the input shown; performance on test objects unlike the training set; no claim resting on a feature that appears only in the network output.

**Benchmark.** [15], [16]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. Kapoor and A. Narayanan, Leakage and the reproducibility crisis in machine-learning-based science, Patterns 4, 100804 (2023); read as preprint arXiv:2207.07048 | doi:10.1016/j.patter.2023.100804 |
| 2 | S. Kapoor et al., REFORMS: consensus-based recommendations for machine-learning-based science, Sci. Adv. 10, eadk3452 (2024); read as preprint arXiv:2308.07832 | doi:10.1126/sciadv.adk3452 |
| 3 | B. Meredig et al., Can machine learning identify the next high-temperature superconductor? Examining extrapolation performance for materials discovery, Mol. Syst. Des. Eng. 3, 819 (2018) | doi:10.1039/C8ME00012C |
| 4 | H. Song et al., Learning from noisy labels with deep neural networks: a survey, arXiv:2007.08199 (2020), final version published in IEEE Trans. Neural Netw. Learn. Syst. (2022) | doi:10.48550/arXiv.2007.08199 |
| 5 | C. G. Northcutt et al., Pervasive label errors in test sets destabilize machine learning benchmarks, NeurIPS 2021 Datasets and Benchmarks Track; arXiv:2103.14749 (2021) | doi:10.48550/arXiv.2103.14749 |
| 6 | T. Dorigo and P. de Castro, Dealing with nuisance parameters using machine learning in high energy physics: a review, arXiv:2007.09121 (2020) | doi:10.48550/arXiv.2007.09121 |
| 7 | Y. Ovadia et al., Can you trust your model's uncertainty? Evaluating predictive uncertainty under dataset shift, NeurIPS 2019; arXiv:1906.02530 (2019) | doi:10.48550/arXiv.1906.02530 |
| 8 | Z. C. Lipton and J. Steinhardt, Troubling trends in machine learning scholarship, arXiv:1807.03341 (2018) | doi:10.48550/arXiv.1807.03341 |
| 9 | X. Bouthillier et al., Accounting for variance in machine learning benchmarks, arXiv:2103.03098 (2021) | doi:10.48550/arXiv.2103.03098 |
| 10 | T. Saito and M. Rehmsmeier, The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets, PLoS ONE 10, e0118432 (2015) | doi:10.1371/journal.pone.0118432 |
| 11 | C. Guo et al., On calibration of modern neural networks, ICML 2017; arXiv:1706.04599 (2017) | doi:10.48550/arXiv.1706.04599 |
| 12 | V. Kuleshov et al., Accurate uncertainties for deep learning using calibrated regression, ICML 2018; arXiv:1807.00263 (2018) | doi:10.48550/arXiv.1807.00263 |
| 13 | J. Adebayo et al., Sanity checks for saliency maps, arXiv:1810.03292 (2018) | doi:10.48550/arXiv.1810.03292 |
| 14 | R. Geirhos et al., Shortcut learning in deep neural networks, Nat. Mach. Intell. 2, 665 (2020); read as preprint arXiv:2004.07780 | doi:10.1038/s42256-020-00257-z |
| 15 | V. Antun et al., On instabilities of deep learning in image reconstruction and the potential costs of AI, Proc. Natl. Acad. Sci. USA 117, 30088 (2020); read as preprint arXiv:1902.05300 | doi:10.1073/pnas.1907377117 |
| 16 | S. Bhadra et al., On hallucinations in tomographic image reconstruction, IEEE Trans. Med. Imaging 40, 3249 (2021); read as the version on PubMed Central, PMC8673588 | doi:10.1109/TMI.2021.3077857 |
