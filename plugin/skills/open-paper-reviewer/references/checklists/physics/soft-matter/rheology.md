---
id: T-RHEOLOGY
name: Rheology
type: technique
field: physics/soft-matter
applies_when: the paper reports viscosity, flow curves, yield stress, storage and loss moduli, normal stress differences or extensional viscosity of a complex fluid or soft solid measured with a rheometer, or bases a claim about flow, elasticity, yielding, thixotropy or ageing on them
version: "0.1"
---

# Rheology

Rheometry is used to claim how a complex fluid or soft solid flows and deforms: its viscosity and flow curve, its storage and loss moduli (G′ and G″) from small-amplitude oscillatory shear (SAOS), its yield stress, its normal stress differences (N1 and N2), its extensional viscosity, and how these change with time and shear history. All of them are inferred from torque, force and displacement measured at the boundaries of the sample, on the assumption that the flow inside is the ideal one for the geometry.

## 1. Linear regime

**Question.** For each oscillatory or creep data set presented as linear viscoelastic, does the paper show an amplitude sweep at the relevant frequencies and temperatures, and state that the strain or stress used lies inside the range where the moduli do not depend on amplitude?

**Why it matters.** G′ and G″ are defined for a sinusoidal response. Once the amplitude is large enough for the response to become nonlinear, they are no longer uniquely defined, and values reported from such data depend on the amplitude and the analysis rather than on the material alone. Where the response turns nonlinear depends on the frequency and, in time-dependent materials, on the sweep protocol, so one sweep does not establish the linear range for every condition used.

**Resolved by.** Amplitude sweeps shown, with the chosen strain or stress marked inside the plateau; the sweep repeated at the lowest and highest frequencies used, or after ageing; where larger amplitudes are used on purpose, the analysis of the nonlinear response named and the harmonics or waveforms shown, not a single G′ and G″ pair.

**Benchmark.** [1], [3]

## 2. Torque and inertia limits

**Question.** Does the paper show that each reported point lies within the measurable window of the instrument and geometry: above the low-torque limit, and below the frequency or rate at which instrument or sample inertia dominates?

**Why it matters.** At low torque, surface tension and contact-line forces at the free edge add a torque that can exceed the viscous one, appearing as apparent shear thinning in steady shear or as an apparent elastic modulus in oscillation. At high frequency, the inertia of the rotating parts couples with a soft sample near a resonance, and small errors in the inertia correction then produce large errors in G′; the sample's own inertia sets a further limit. Data outside these limits can look like a real material response.

**Resolved by.** The minimum resolvable torque and the inertia correction stated; the limits drawn on the plots of viscosity or moduli, or the excluded points identified; for soft samples, the raw phase angle or the coupled resonance frequency reported; consistency shown between geometries of different size; a calibration fluid of known properties measured over the same range.

**Benchmark.** [4], [5], [9], [14]

## 3. Wall slip

**Question.** Does the paper test for wall slip, for example by repeating the measurement at different gaps or with roughened or serrated surfaces or a vane, and does it show that the reported flow curve, yield stress or moduli do not change?

**Why it matters.** Many suspensions, emulsions, gels and pastes slip at smooth walls. Slip shifts the apparent flow curve to higher shear rates and can produce a kink or plateau at a stress below the true yield stress, so the measured quantity depends on the surface rather than on the material. Corrections that compare gaps assume that slip depends only on stress and is the same at both walls.

**Resolved by.** The wall surfaces stated; data from at least two gaps or two surface roughnesses agreeing, or a slip-corrected flow curve with its assumptions stated; roughness on the scale of the microstructure, with a check that it does not introduce secondary flows; where available, local velocity measurements at the wall.

**Benchmark.** [1], [2]

## 4. Homogeneous flow and choice of geometry

**Question.** Does the paper show, or argue from the geometry and the material, that the deformation in the gap is homogeneous, and does it consider shear banding or shear localisation before reading a stress plateau or a sharp change in the flow curve as a material property?

**Why it matters.** Converting torque and rotation rate into a flow curve assumes a uniform shear rate across the gap. Many complex fluids form bands of different shear rate, and in a wide-gap Couette cell the stress falls across the gap, so a yield stress fluid can flow in only part of it. A global flow curve cannot tell these cases apart from homogeneous flow.

**Resolved by.** The geometry, gap and curvature stated with the reason for the choice; for materials prone to banding or localisation, local velocity profiles (by particle tracking, ultrasound, light scattering or magnetic resonance imaging) or flow visualisation; agreement between geometries with different stress gradients; the time to reach steady state shown rather than assumed.

**Benchmark.** [1], [2]

## 5. Thixotropy, ageing and shear history

**Question.** Does the paper state the full protocol before each measurement (loading, pre-shear, rest time, ramp rate or step duration) and show how the result depends on it?

**Why it matters.** In thixotropic and ageing materials the viscosity, moduli and yield stress depend on the time since loading or pre-shear and on the rate at which stress or shear rate is ramped. Yield stresses from different protocols can differ by more than an order of magnitude, and a value obtained under one history is not a material constant.

**Resolved by.** The protocol given in enough detail to repeat; a pre-shear or rejuvenation step with a stated rest time before each test; up and down ramps or step tests showing any hysteresis; results at more than one waiting time or ramp rate; the yield stress method named and, where the claim depends on it, compared with a second method.

**Benchmark.** [1], [6], [7]

## 6. Sample loading, free surface and edge fracture

**Question.** Does the paper describe how the sample was loaded and trimmed, how evaporation was prevented, and whether the free edge was observed during the test, in particular at high shear rates?

**Why it matters.** Drying, and movement or asymmetry of the contact line at the free edge, add a torque that is not from the sample. Above a rate that depends on the material and the gap, the free surface of many viscoelastic fluids becomes unstable and fractures, and the measured stress then no longer describes the material.

**Resolved by.** Loading and trimming procedure stated; a solvent trap, sealing fluid or humidity control described, with the stability of a reference measurement over the test duration; images or observations of the edge at the highest rates; data affected by edge instability excluded; the accessible rate range checked with a smaller gap or a different geometry.

**Benchmark.** [2], [5], [8]

## 7. Normal stress differences

**Question.** When N1 or N2 are reported, does the paper state how they were obtained from the measured thrust, which corrections were applied, and whether the values are above the resolution of the force transducer?

**Why it matters.** The axial force transducer has a minimum resolvable force that excludes much of the low-rate range of polymer solutions and suspensions. Fluid inertia and secondary flows reduce the measured thrust, and N2 is usually obtained by subtracting two nearly equal quantities, which magnifies their uncertainty. The second normal stress difference also controls the onset of edge fracture, so the reliable range for normal stresses can be narrower than for shear stress.

**Resolved by.** The geometry and formula used to convert thrust into N1 and N2; the transducer resolution stated and points below it excluded; inertia corrections described; for N2, the two measurements combined and the propagated uncertainty shown.

**Benchmark.** [8], [9], [10]

## 8. Extensional rheometry

**Question.** When an extensional viscosity or relaxation time is reported, does the paper show that the deformation was homogeneous and close to the intended uniaxial extension, and does it state the model used to extract the quantity from the measured force or filament diameter?

**Why it matters.** Extensional flows are hard to generate without shear and without necking, rupture or detachment from the end-plates. A sample that deforms unevenly can produce an apparent maximum in the measured viscosity that is not a material property. In capillary thinning methods the extension rate is chosen by the fluid, and the relaxation time inferred from the thinning rests on model assumptions that do not hold for every polymer.

**Resolved by.** Images or diameter measurements showing uniform deformation and the actual local strain rate; the strain reached and whether a steady state was attained; necking, rupture or end-plate effects identified and the affected data excluded; the model behind any extracted relaxation time stated, with its assumptions checked or the value compared with an independent extensional measurement.

**Benchmark.** [11], [12], [13]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | D. Bonn, M. M. Denn, L. Berthier, T. Divoux and S. Manneville, Yield stress materials in soft condensed matter, Rev. Mod. Phys. 89, 035005 (2017); read as preprint arXiv:1502.05281 | doi:10.1103/RevModPhys.89.035005 | full text | Sec. I.3.1: measured yield stresses can differ by more than an order of magnitude with the method used. Sec. I.4: thixotropic yield stress and viscosity depend on rest time and shear history; up and down ramps reveal hysteresis that depends on ramp rate. Sec. II.1 to II.2: dynamic, static, creep and large-amplitude oscillatory estimates of yield stress depend on protocol, sweep rate, sample age and pre-shear. Sec. II.2.3: amplitude sweeps show a linear plateau of G′ followed by a nonlinear regime; estimates depend on frequency and ramp protocol, and the nonlinear response should be analysed with its full harmonic content rather than G′ and G″ alone. Sec. II.3: slip shifts the apparent flow curve and can give a plateau below the true yield stress; detected by local velocimetry or gap variation, whose assumptions are rarely checked locally; suppressed by roughness on the scale of the microstructure, which if too large can trigger secondary flows. Sec. III.1.3: local velocity profiles distinguish shear banding, localisation and slip |
| 2 | T. Divoux, M. A. Fardin, S. Manneville and S. Lerouge, Shear banding of complex fluids, Annu. Rev. Fluid Mech. 48, 81–103 (2016); read as preprint arXiv:1503.04130 | doi:10.1146/annurev-fluid-122414-034416 | full text | Sec. II.1: the standard flow curve assumes a homogeneous shear rate; banding was revealed by local methods such as birefringence and NMR velocimetry; in cone-and-plate flows edge effects limit the accessible range; slip on the high-shear band is coupled to banding. Sec. II.2: edge effects or other experimental artefacts have been proposed as the origin of some reported banding in polymer solutions; slip competes with banding and can be limited by surface roughness or treatment. Sec. III.2: in wide-gap Couette cells the stress falls as 1/r², so flow can localise from the geometry alone; wall chemistry and pre-shear strongly affect results. Sec. III intro: long relaxation times mean steady state must be checked |
| 3 | K. Hyun, M. Wilhelm, C. O. Klein, K. S. Cho, J. G. Nam, K. H. Ahn, S. J. Lee, R. H. Ewoldt and G. H. McKinley, A review of nonlinear oscillatory shear tests: analysis and application of large amplitude oscillatory shear (LAOS), Prog. Polym. Sci. 36, 1697–1753 (2011) | doi:10.1016/j.progpolymsci.2011.02.002 | abstract | Abstract (MIT repository record): at large enough strain amplitude the response becomes nonlinear and the linear functions used for SAOS no longer describe it; G′ and G″ assume a sinusoidal stress and are not uniquely defined for a nonlinear response, so other analysis methods are needed |
| 4 | S. A. Klemuk and I. R. Titze, Determining motor inertia of a stress-controlled rheometer, J. Rheol. 53, 765–780 (2009) | doi:10.1122/1.3119056 | abstract | Abstract (University of Iowa record): motor inertia is the largest contributor to system inertia and its value is rarely given with a precision; below the coupled motor, plate and sample resonance frequency inertia uncertainty has negligible effect, above it G′ of soft viscoelastic materials errs quadratically |
| 5 | M. T. Johnston and R. H. Ewoldt, Precision rheometry: surface tension effects on low-torque measurements in rotational rheometers, J. Rheol. 57, 1515–1532 (2013) | doi:10.1122/1.4819914 | abstract | Abstract (University of Illinois record): a torque from surface tension and contact-line forces can exceed the viscous torque by more than two orders of magnitude for water, mimics shear thinning in steady shear and an elastic modulus in oscillation, cannot be reliably subtracted and so raises the low-torque limit; reduced by symmetric contact lines, limiting evaporation and contact-line migration |
| 6 | J. Mewis and N. J. Wagner, Thixotropy, Adv. Colloid Interface Sci. 147–148, 214–227 (2009) | doi:10.1016/j.cis.2008.09.005 | abstract | Abstract (Europe PMC record): thixotropy is a reversible, flow-induced, time-dependent change in viscosity linked to nonlinear viscoelasticity; the review covers its rheological signatures and the methods used to measure it |
| 7 | P. C. F. Møller, J. Mewis and D. Bonn, Yield stress and thixotropy: on the difficulty of measuring yield stresses in practice, Soft Matter 2, 274–283 (2006) | doi:10.1039/b517840a | abstract | Abstract (Europe PMC record): many difficulties in measuring yield stress disappear once thixotropy is taken into account; with thixotropy the yield stress depends on shear history and is not a material property; a protocol is given that yields reproducible critical stresses |
| 8 | E. J. Hemingway, H. Kusumaatmaja and S. M. Fielding, Edge fracture in complex fluids, Phys. Rev. Lett. 119, 028006 (2017); read as preprint arXiv:1703.05013 | doi:10.1103/PhysRevLett.119.028006 | full text | Abstract, introduction and results: above a material- and device-dependent shear rate the free surface destabilises and accurate measurement becomes impossible; edge fracture is cited as a limiting factor in rotational rheometry; the onset criterion involves the shear-rate dependence of N2 and of the shear stress, the interfacial stress jump, surface tension and gap size; mitigation by immersing the sample in an immiscible bath fluid more viscous than air |
| 9 | R. V. More, R. Patterson, E. Pashkovski and G. H. McKinley, Rod-climbing rheometry revisited, Soft Matter 19, 4073–4087 (2023); read as preprint arXiv:2302.06010 | doi:10.1039/D3SM00181D | full text | Sec. I: inertia and secondary flows reduce the thrust measured in cone-and-plate tests; N2 from combined thrust measurements requires subtracting two nearly equal values and is often a small fraction of N1. Secs. I and IV: the minimum resolvable axial force restricts the shear rates over which N1 can be measured, often excluding the low-rate regime; low SAOS frequencies can fall below instrument sensitivity |
| 10 | O. Maklad and R. J. Poole, A review of the second normal-stress difference; its importance in various flows, measurement techniques, results for various complex fluids and theoretical predictions, J. Non-Newtonian Fluid Mech. 292, 104522 (2021) | doi:10.1016/j.jnnfm.2021.104522 | abstract | Abstract (University of Greenwich record): shear characterisation is usually limited to viscosity and at best N1, while N2 is largely neglected although for many fluids it is not small and it matters in some flows; the review surveys the experimental techniques proposed for measuring N2 |
| 11 | G. H. McKinley and T. Sridhar, Filament-stretching rheometry of complex fluids, Annu. Rev. Fluid Mech. 34, 375–415 (2002) | doi:10.1146/annurev.fluid.34.083001.125207 | abstract | Abstract (MIT laboratory page): filament stretching approximates ideal homogeneous uniaxial elongation; tensile stress and molecular conformation are followed with strain rate and strain; coupling between filament dynamics and extensional rheology can cause necking, rupture and elastic peeling from the end-plates |
| 12 | V. Calabrese, A. Q. Shen and S. J. Haward, How do polymers stretch in capillary-driven extensional flows?, Macromolecules 57, 9668–9676 (2024); read as preprint arXiv:2403.04103 | doi:10.1021/acs.macromol.4c01604 | full text | Introduction: in the elastocapillary regime the extension rate is selected by the fluid; the relaxation time from thinning rests on Oldroyd-B and FENE-P assumptions. Results and summary: the assumptions hold for highly extensible polymers but the thinning time can be far shorter than an independent birefringence measurement for less extensible ones; the thinning-derived time is compared with birefringence in an independent cross-slot extensional flow, and the authors advise care in interpreting capillary-thinning relaxation times for less extensible polymers |
| 13 | T. I. Burghelea, Z. Starý and H. Münstedt, On the "viscosity overshoot" during the uniaxial extension of a low density polyethylene, J. Non-Newtonian Fluid Mech. 166, 1198–1209 (2011); read as preprint arXiv:1001.2093, which carries a different title | doi:10.1016/j.jnnfm.2011.07.007 | abstract | Abstract: combined global and local measurements show that an apparent maximum in the transient extensional viscosity coincides with secondary necks forming along the sample, so it reflects inhomogeneous deformation rather than the material; local viscosity shows a plateau |
| 14 | R. H. Ewoldt, M. T. Johnston and L. M. Caretta, Experimental challenges of shear rheology: how to avoid bad data, in Complex Fluids in Biological Systems, ed. S. E. Spagnolie, pp. 207–241 (Springer, 2015) | doi:10.1007/978-1-4939-2065-5_6 | abstract | Abstract (Springer chapter page): measurement artefacts can make a material appear shear thinning, shear thickening or viscoelastic; instrument resolution, instrument and sample inertia, boundary effects and volumetric effects complicate the conversion of boundary loads and displacements into stress and strain |
