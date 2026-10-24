---
id: T-FORCE-SPECTROSCOPY
name: Single-molecule force spectroscopy
type: technique
field: physics/biological
applies_when: the paper pulls on single molecules or molecular complexes with optical tweezers, magnetic tweezers or an atomic force microscope, or bases a claim about unfolding or rupture forces, bond lifetimes, kinetic rates, transition-state distances or energy landscapes on force-extension or force-time traces
version: "0.1"
---

# Single-molecule force spectroscopy

Single-molecule force spectroscopy (SMFS) with optical tweezers (OT), magnetic tweezers (MT) or the atomic force microscope (AFM) is used to claim the forces at which molecules unfold or bonds rupture, the lengths released in each step, force-dependent rates and lifetimes, and parameters of the underlying energy landscape such as the distance to the transition state and the barrier height. All of these rest on a calibrated probe stiffness, a calibrated displacement, and the assumption that each trace records one specific molecule.

## 1. Stiffness and force calibration

**Question.** How was the force scale calibrated for each probe (trap or cantilever stiffness, or force against magnet position), by which method, under what conditions, and with what uncertainty?

**Why it matters.** Every force, loading rate and energy in the paper scales with the calibrated stiffness. Each method has its own conditions: the power-spectrum method needs the drag coefficient, which rises near a surface, and enough detector bandwidth; the variance method needs a calibrated detector; camera-based MT calibration underestimates the bead's fluctuations and so overestimates force when the corner frequency approaches the camera rate. Common AFM cantilever methods carry systematic uncertainties of about 10 % or more, and cantilevers from the same batch can differ markedly.

**Resolved by.** The method named for each probe, with the drag, bead size, height above the surface, laser power or magnet position at which it was done; each bead or cantilever calibrated, not a nominal or batch value; for MT, the camera rate and any correction for blurring and aliasing, with the force range checked against it; where possible, agreement between two independent methods; the calibration uncertainty stated and carried into forces and derived parameters.

**Benchmark.** [1], [2], [3], [4]

## 2. Displacement calibration and linear range

**Question.** How were bead or tip displacements converted from detector signal to distance, and do the reported forces and extensions stay within the range where the detector response and the restoring force are linear?

**Why it matters.** An optical trap behaves as a linear spring only for displacements of the order of 100 nm, and the position detector gives a single-valued, near-linear response only over a limited range, with a sensitivity that varies from bead to bead and with height above the surface. In AFM, the deflection sensitivity taken from contact force curves enters both the force and the cantilever stiffness from thermal calibration, and much of the spread between laboratories in a calibration comparison has been attributed to it. AFM extension is the piezo displacement corrected for cantilever deflection, so an error here alters contour lengths as well as forces.

**Resolved by.** The detector calibrated for each bead in the plane where it is used, or the AFM deflection sensitivity measured on a hard surface with the slope and data range stated; the displacement range of the data compared with the calibrated linear range; extensions corrected for probe deflection; a known length or force signature, such as a reference molecule, used as a check.

**Benchmark.** [1], [2], [4]

## 3. Drift and low-frequency noise

**Question.** How large was the instrumental drift over the duration of a trace or a calibration, how was it measured and corrected, and is it small compared with the length and force changes the claims rest on?

**Why it matters.** Temperature gradients of the order of one kelvin can move the sample by micrometres over minutes, far more than molecular length changes. Slow drift often does not show in a time series or power spectrum, but it limits how long a calibration or a constant-force measurement remains valid, and it can shift the force baseline or the zero of extension during slow pulls.

**Resolved by.** Temperature control and isolation described; drift measured, for example with a reference bead fixed to the surface or an Allan variance analysis, and its size stated; calibration and measurement times chosen within the stable interval; force and extension baselines checked before and after each event, with any correction stated.

**Benchmark.** [1], [2], [5], [7]

## 4. One specific tether

**Question.** What evidence shows that each analysed trace comes from a single molecule attached through the intended chemistry, and not from several molecules in parallel or from nonspecific adhesion?

**Why it matters.** The probe is much larger than the molecule, so several molecules can attach at once, and surfaces and tips bind nonspecifically. Several bonds in parallel can raise the apparent rupture force and shrink the apparent transition-state distance, and nonspecific adhesion produces events that resemble specific ones. Keeping the binding frequency low lowers, but does not remove, the fraction of multiple attachments.

**Resolved by.** Specific attachment chemistry, ideally site-specific and covalent at the anchors; surfaces passivated, with negative controls such as blocked binding sites or missing partners giving few events; the fraction of approach cycles that give an attachment reported and kept low, with the expected share of multiple attachments estimated; a single-molecule signature in each trace, such as the expected elasticity of the tether, a known overstretching or fingerprint transition, the expected contour-length increments, or in MT a fitted persistence length that excludes beads held by more than one tether.

**Benchmark.** [1], [6], [7], [9], [11]

## 5. Trace selection and event assignment

**Question.** How many traces were recorded, how many were analysed, by what rule were traces kept or rejected and events assigned to states or domains, and was that rule fixed independently of the forces being measured?

**Why it matters.** In AFM experiments the share of usable traces can be well below one per cent, so the rule that picks them shapes the result. Rejecting traces with the highest forces, or keeping only the last rupture, can remove a real strong state or retain multiple-bond events; filtering on multiple ruptures fails when the ruptures lie close together. Fingerprint domains that unfold at forces close to the event of interest can bias which events are counted.

**Resolved by.** The numbers of recorded, analysed and rejected traces for each condition; selection criteria stated in terms of tether length, contour-length increments or fingerprint pattern, not of the force of the event studied; fingerprint domains chosen to unfold well below the force of interest; force distributions shown for all selected events, with the number of events behind each.

**Benchmark.** [6], [7]

## 6. Loading rate

**Question.** How was the loading rate at rupture or unfolding determined, over what range was it varied, and does the paper show the full force distributions at each rate rather than only the most probable force?

**Why it matters.** Rupture and unfolding forces depend on how fast the force is applied, so a force without its loading rate is not a property of the molecule. Flexible linkers and handles make the loading rate depend on force, so pulling speed times probe stiffness can misstate it, and ignoring this has shifted fitted lifetimes by about an order of magnitude. A narrow range of rates cannot show the curvature in force spectra that arises from rebinding near equilibrium or from several bonds.

**Resolved by.** The loading rate taken from the measured slope of force against time just before each event, or calculated with the linker compliance included; rates spanning as wide a range as the instrument allows, ideally several decades; complete rupture-force histograms at each rate; a check that histograms at different rates map onto one force-dependent lifetime, which tests the assumed single-step kinetics.

**Benchmark.** [8], [9]

## 7. Kinetic and energy-landscape parameters

**Question.** Which model was used to extract zero-force rates, transition-state distances, barrier heights or full energy landscapes, are its assumptions shown to hold for the data, and how sensitive are the parameters to the model choice and to the compliance of the probe and handles?

**Why it matters.** The Bell and Bell–Evans models assume a barrier that does not move with force, which cannot hold over a wide force range, so extrapolated zero-force rates are often unreliable and transition-state distances depend on the pulling geometry. Rebinding or multiple bonds analysed with an irreversible single-bond model give misleading parameters, and curvature in force spectra is not by itself evidence for two barriers. Landscapes reconstructed from extension are broadened by handle and probe compliance and must be deconvolved, equilibrium reconstructions need a constant load over the folding bandwidth, and nonequilibrium estimators need more data as dissipation grows.

**Resolved by.** The model and its assumptions stated, with parameters compared across models of different barrier shape; extrapolations to zero force flagged as such, with their range; agreement between independent routes, such as constant-force and force-ramp data giving the same force-dependent rates; for landscape reconstruction, the point-spread function of probe and handles measured and deconvolved, convergence of nonequilibrium estimators shown, and the adequacy of extension as a reaction coordinate discussed.

**Benchmark.** [8], [9], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | K. C. Neuman and A. Nagy, Single-molecule force spectroscopy: optical tweezers, magnetic tweezers and atomic force microscopy, Nat. Methods 5, 491–505 (2008); read as the author manuscript in PubMed Central (PMC3397402) | doi:10.1038/nmeth.1218 | full text | Optical tweezers calibration: power-spectrum, variance and drag methods and their requirements, each bead calibrated, stiffness constant only over about 150 nm. Magnetic tweezers: force from transverse fluctuations, video detection limits bandwidth; drift reduced with a reference bead stuck to the surface. AFM: thermal calibration accuracy of 10 to 20 %, cantilevers from one lot differ; several molecules may attach because the tip is large; nonspecific binding introduces artefacts; extension must be corrected for cantilever deflection; DNA transition at about 65 pN and titin fingerprints confirm single molecules. Temperature stability named as the largest single concern |
| 2 | K. C. Neuman and S. M. Block, Optical trapping, Rev. Sci. Instrum. 75, 2787–2809 (2004); read as the author manuscript in PubMed Central (PMC1523313) | doi:10.1063/1.1785844 | full text | Sec. II: linear spring only for small displacements of about 150 nm. Sec. III.G and IV.A: detector working range about 0.3 µm, calibration restricted to the single-valued region, lateral sensitivity varies with axial position. Sec. III.E.5: silicon detectors are bandwidth limited in the near infrared. Sec. III.H: a 1 K gradient can drift the sample by micrometres in minutes. Sec. IV.A: detector calibrated per bead, bead diameters vary by up to 5 %, axial position and crosstalk matter. Sec. IV.A.1 and IV.B.1: drag rises near the coverslip (Faxén's law); the power-spectrum method needs enough detector bandwidth and is biased by filtering |
| 3 | A. J. W. te Velthuis, J. W. J. Kerssemakers, J. Lipfert and N. H. Dekker, Quantitative guidelines for force calibration through spectral analysis of magnetic tweezers data, Biophys. J. 99, 1292–1302 (2010); read in PubMed Central (PMC2920648) | doi:10.1016/j.bpj.2010.06.008 | full text | Introduction and Results: camera integration lowers the measured variance, so force is overestimated without correction; aliasing changes the spectral shape; force error grows as the corner frequency nears the Nyquist frequency, reaching 10 % at about 14 pN for a 2.7 µm tether; guidelines on tether length, camera rate, viscosity and bead size; drag changes near the surface |
| 4 | R. S. Gates, M. G. Reitsma, J. A. Kramar and J. R. Pratt, Atomic force microscope cantilever flexural stiffness calibration: toward a standard traceable method, J. Res. Natl. Inst. Stand. Technol. 116, 703–727 (2011); read in PubMed Central (PMC4550330) | doi:10.6028/jres.116.015 | full text | Sec. 4: chip-to-chip variation in stiffness within one set; leaving unstated whether approach or retract slopes were used called a dangerous omission. Sec. 6 and 8: optical lever sensitivity from a force curve on a rigid surface enters thermal and reference methods; thermal methods judged accurate to within about 10 %; the authors believe much of the variation in precision and accuracy came from the optical lever sensitivity |
| 5 | F. Czerwinski, A. C. Richardson, C. Selhuber-Unkel and L. B. Oddershede, Allan variance analysis as useful tool to determine noise in various single-molecule setups, arXiv:0908.4484 (2009), preprint of Proc. SPIE 7400, 740004 (2009); read on ar5iv | doi:10.48550/arXiv.0908.4484 | full text | Introduction and Results: low-frequency drift not visible in the time series, histogram or power spectrum is revealed by the Allan variance; its minimum (about 1 to 10 s for trapped spheres) gives the optimal calibration time, beyond which drift dominates and more data do not improve accuracy |
| 6 | K. C. Johnson and W. E. Thomas, How do we know when single-molecule force spectroscopy really tests single bonds?, Biophys. J. 114, 2032–2039 (2018); read in PubMed Central (PMC5961468) | doi:10.1016/j.bpj.2018.04.002 | full text | Poisson analysis: adhesion probabilities of 20 to 35 % give roughly 80 to 90 % single bonds, and adhesion probability should be reported; nonspecific adhesion must be blocked and shown absent with negative controls; rupture-length and marker signatures, polymer linkers; discarding the highest-force ruptures or keeping only the last rupture is unreliable, and filtering multiple ruptures fails when they lie close together; in a survey of one receptor-ligand pair, studies with high adhesion probability reported some of the highest forces, and results agreed only where low adhesion was reported |
| 7 | B. Yang, Z. Liu, H. Liu and M. A. Nash, Next generation methods for single-molecule force spectroscopy on polyproteins and receptor-ligand complexes, Front. Mol. Biosci. 7, 85 (2020) | doi:10.3389/fmolb.2020.00085 | full text | Nonspecific adsorption gives yields of usable curves sometimes well below 1 %; fingerprint domains with known unfolding forces and contour-length increments screen for single specific events and should unfold well below the force of interest; site-specific covalent attachment raises yield and reduces nonspecific events; cantilever coatings and instrumental drift limit low-frequency stability |
| 8 | O. K. Dudko, G. Hummer and A. Szabo, Theory, analysis, and interpretation of single-molecule force spectroscopy experiments, Proc. Natl. Acad. Sci. USA 105, 15755–15760 (2008); read in PubMed Central (PMC2572921) | doi:10.1073/pnas.0806085105 | full text | Bell's formula assumes a force-independent transition-state distance that cannot hold at all forces, and deviations are observed; rupture-force histograms at different loading rates should collapse onto one force-dependent lifetime, and failure to collapse indicates more complex kinetics; with flexible linkers the loading rate depends on force, and ignoring this changed the fitted lifetime by about an order of magnitude; parameters compared across barrier shapes |
| 9 | R. W. Friddle, A. Noy and J. J. De Yoreo, Interpreting the widespread nonlinear force spectra of intermolecular bonds, Proc. Natl. Acad. Sci. USA 109, 13573–13578 (2012); read in PubMed Central (PMC3427124) | doi:10.1073/pnas.1202946109 | full text | Nonlinear force spectra reported in many systems are often read as two barriers, but can arise from rebinding near equilibrium at low loading rates or from several bonds; both regimes appear only over a wide range of loading rates; a multi-bond system analysed with a single-bond model gives a transition distance about N times too small; the crossover between regimes spans roughly 1 to 10^5 pN/s, so a narrow range of rates can miss one regime |
| 10 | M. T. Woodside and S. M. Block, Reconstructing folding energy landscapes by single-molecule force spectroscopy, Annu. Rev. Biophys. 43, 19–39 (2014); read as the author manuscript in PubMed Central (PMC4609573) | doi:10.1146/annurev-biophys-051013-022754 | full text | Equilibrium reconstructions: measured extension distributions are convolved with the probe and handle response and must be deconvolved; constant load over the folding bandwidth is needed. Nonequilibrium methods need ever more data as dissipation grows. Model-dependent approximations: Bell model neglects barrier movement, so extrapolated zero-force rates are unreliable, and transition distances vary with pulling geometry. Validation by agreement of force-ramp and constant-force data; extension as a reaction coordinate tested with splitting probabilities |
| 11 | I. De Vlaminck, T. Henighan, M. T. J. van Loenhout, D. R. Burnham and C. Dekker, Magnetic forces and DNA mechanics in multiplexed magnetic tweezers, PLoS One 7, e41432 (2012); read in PubMed Central (PMC3411724) | doi:10.1371/journal.pone.0041432 | full text | Ensemble Analysis of DNA Mechanics: beads held by more than one tether were identified by a fitted persistence length below 28 nm and removed before analysis |
