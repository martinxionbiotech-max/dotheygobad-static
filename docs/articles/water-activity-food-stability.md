---
title: What is Water Activity (aw)? The Complete Industrial Guide to Food Stability, Safety and Quality
date: 2026-08-09
description: "Water activity (aw) is the single most predictive parameter in food stability science. Learn how aw governs microbial growth thresholds, chemical reaction rates, and texture at every aw level from 0 to 1.0."
keywords: water activity, aw, food stability, food safety, microbial growth, shelf life, moisture, food science
---

# What is Water Activity (aw)? The Complete Industrial Guide to Food Stability, Safety and Quality

## Executive Summary

Water activity (aw) — the ratio of the vapor pressure of water in a food to the vapor pressure of pure water at the same temperature — is arguably the single most important parameter in food preservation science. It governs every major degradation pathway: microbial growth (bacteria require aw ≥ 0.91, molds can survive to 0.61), enzymatic activity, lipid oxidation (maximized at aw 0.3-0.5), Maillard browning (peak at aw 0.5-0.7), and physical texture transitions. Understanding aw enables predictive shelf life modeling, hurdle technology design, and formulation decisions that extend product stability from days to years. This comprehensive guide covers the thermodynamic principles, measurement technology, regulatory framework (FDA 21 CFR, HACCP critical control points), and practical formulation strategies across every food category.

## Background

The concept of water activity was established by W.J. Scott in 1957, building on earlier work in physical chemistry that defined the thermodynamic activity of a solvent. Scott demonstrated that microbial growth correlated with water activity — not total moisture content — explaining why honey (aw 0.50-0.60, 17% moisture) never spoils while fresh meat (aw 0.98-0.99, 75% moisture) spoils within days. This insight fundamentally reoriented food preservation from an art to a science.

The thermodynamic definition provides the mathematical rigor: aw = p/p₀ = ERH/100, where p is the partial vapor pressure of water above the food and p₀ is the saturation vapor pressure of pure water at the same temperature. In equilibrium, aw equals the equilibrium relative humidity (ERH) divided by 100 — which is how all aw measurements are actually made.

Crucially, aw is NOT the same as moisture content. This confusion persists even in some food industry contexts and is responsible for formulation failures, spoilage incidents, and incorrect shelf life predictions. Two foods can have identical moisture content but dramatically different water activities:
- Fresh meat: 75% moisture, aw 0.98-0.99 (most water is free)
- Jam: 65-70% moisture, aw 0.75-0.85 (much of the water is "bound" by dissolved sugar)
- Crackers: <3% moisture, aw 0.15-0.30 (extremely little free water)

The jam has 20× more water than the cracker but a lower aw — because the sugar "binds" the water, making it thermodynamically unavailable to microorganisms and chemical reactions.

## The Thermodynamic Foundation: Why aw, Not Moisture Content

### Raoult's Law and Colligative Properties

Water activity in aqueous solutions follows Raoult's law: aw = x_w × γ_w, where x_w is the mole fraction of water and γ_w is the activity coefficient (deviation from ideality). In simple terms, dissolved solutes reduce aw by reducing the mole fraction of water molecules at the liquid-vapor interface.

This is why NaCl at 2% concentration only reduces aw by approximately 0.01 — a small effect — while sucrose or glycerol at 50% concentration can reduce aw below 0.90. The molar mass matters: one mole of NaCl (58.5 g) has the same colligative effect as one mole of glucose (180 g), but you need 3× more glucose by weight to achieve the same concentration.

### The Moisture Sorption Isotherm

Every food has a characteristic moisture sorption isotherm (MSI) — a curve relating moisture content to water activity at constant temperature. The MSI is typically sigmoidal (Type II in the BET classification) and reveals three distinct regions:

**Region I (aw 0-0.25):** Monolayer water. Water molecules are tightly bound to polar sites on proteins (-NH₃⁺, -COO⁻), carbohydrates (-OH groups), and minerals via hydrogen bonds and ion-dipole interactions. This water has enthalpy of vaporization 5-15 kJ/mol higher than bulk water, does not freeze at −40°C, and is unavailable for chemical reactions or microbial growth. The monolayer value is critical — it represents the moisture content for maximum stability.

**Region II (aw 0.25-0.75):** Multilayer water. Additional water molecules hydrogen-bond to the monolayer, forming 2-5 molecular layers. This water has intermediate mobility and participates in chemical reactions (Maillard browning peak at aw 0.5-0.7, lipid oxidation).

**Region III (aw 0.75-1.0):** Capillary and free water. Water fills pores and capillaries in the food matrix (condensed by capillary forces per the Kelvin equation) and exists as bulk-like free water. This water is available for microbial growth, enzyme activity, and dissolution of solutes. Freezing and ice crystal formation occur in this region.

The sorption isotherm exhibits hysteresis — the curve differs depending on whether water is being added (adsorption) or removed (desorption). This has practical implications: a cracker that absorbs moisture to aw 0.65 during storage may have a different moisture content than the same cracker dried to aw 0.65 during manufacturing, affecting texture and stability predictions.

### Temperature Dependence

Water activity is temperature-dependent. The Clausius-Clapeyron relationship governs the effect: d(ln aw)/d(1/T) = ΔH/R, where ΔH is the net isosteric heat of sorption. For most foods, aw increases by approximately 0.002-0.01 per °C temperature increase (at constant moisture content).

This temperature dependence has critical practical implications:
- An aw measurement at 25°C may overestimate the aw at 4°C (refrigeration) by 0.01-0.04
- A product that measured aw 0.85 at the QC lab (20°C) could be aw 0.87-0.88 in a hot warehouse (35°C) — potentially crossing the mold growth threshold
- For formal shelf life studies, aw must be measured at the intended storage temperature or corrected to it

## Microbial Growth Thresholds: The aw Barrier Concept

The most practically important application of water activity is predicting which microorganisms can grow — and therefore which spoilage and safety risks exist — in a given food.

### Definitive Thresholds

| aw Range | Microorganisms That Can Grow | Example Foods | Shelf Life Implication |
|----------|------------------------------|---------------|----------------------|
| 0.98-1.00 | All pathogens and spoilage organisms | Fresh meat, milk, seafood | Days (refrigerated) |
| 0.95-0.98 | Most spoilage bacteria, all pathogens except *S. aureus* | Soft cheese, processed meat | 1-4 weeks |
| 0.91-0.95 | *S. aureus* (enterotoxin production stops below 0.90), most LAB | Semi-hard cheese, fermented sausage | 2-8 weeks |
| 0.88-0.91 | Most yeasts, few bacteria | Cured ham, aged cheese | 2-6 months |
| 0.80-0.88 | Most molds, osmophilic yeasts | Jam, dried fruit, fruit cake | 3-12 months |
| 0.70-0.80 | Xerophilic molds (*Eurotium*, *Wallemia*) | Dried fruit, honey (surface) | 6-24 months |
| 0.61-0.70 | Extreme xerophiles (*Xeromyces bisporus*) | Dried fruit, flour | Years |
| <0.60 | No microbial growth possible | Crackers, dried pasta, honey | Indefinite |

These thresholds are well-established in the scientific literature and referenced in FDA and USDA FSIS guidance documents. The key regulatory threshold is aw 0.85 — the boundary between "potentially hazardous food" (TCS food requiring time/temperature control) and non-TCS food under the FDA Food Code. Foods with aw ≤ 0.85 are considered non-potentially-hazardous and exempt from refrigeration requirements.

### Why aw Matters More Than Moisture Content

The classic demonstration: *Staphylococcus aureus* grows in a food with 50% moisture at aw 0.92 but NOT in a food with 60% moisture at aw 0.88 — because the solutes that raised the moisture content (sugar, salt) also "bound" the water, making it thermodynamically unavailable.

This principle explains why:
- Fresh meat (75% H₂O, aw 0.99) spoils in days
- Soy sauce (71% H₂O, aw 0.80) is shelf-stable for years — the 16-18% salt binds the water
- Jam (65% H₂O, aw 0.80-0.85) is shelf-stable for months
- Honey (17% H₂O, aw 0.50-0.60) lasts centuries — the sugar concentration binds water so tightly that even xerophilic molds cannot germinate (unless honey absorbs surface moisture from humid air)

## Chemical Reactions as a Function of aw

### The U-Shaped Lipid Oxidation Curve

Lipid oxidation rates display a characteristic U-shaped dependence on water activity, with minimum oxidation rate at aw 0.2-0.4 (approximately monolayer coverage):

- **aw < 0.20 (Below monolayer):** Water is insufficient to hydrate metal catalysts and quench free radicals. Oxidation proceeds rapidly because exposed lipid surfaces contact oxygen without the protective effect of water.
- **aw 0.20-0.40 (Monolayer region):** Water hydrogen-bonds to lipid hydroperoxides, slowing their decomposition into free radicals. Metal catalysts (Fe, Cu) are hydrated and less catalytically active. Oxidation rate is minimized.
- **aw 0.40-0.70 (Multilayer region):** Water mobilizes metal catalysts, increases reactant mobility, and swells the food matrix (increasing oxygen diffusion). Oxidation rate increases.
- **aw > 0.70:** Continued acceleration, but effects become complex as water dilutes reactants, microbial growth introduces enzymatic oxidation pathways, and structural changes affect oxygen diffusion. In high-moisture foods, microbial spoilage typically overtakes chemical spoilage before lipid oxidation becomes the limiting factor.

This U-shape explains the counterintuitive observation that extremely dry foods (crackers, milk powder) oxidize faster than slightly moist foods, and is the basis for understanding [why some foods don't need refrigeration](shelf-stable-foods-science.md).

### Maillard Browning: The Bell Curve

The Maillard reaction between reducing sugars and amino groups shows a characteristic peak at aw 0.5-0.7:

- **aw < 0.20:** Reactants are diffusion-limited; reaction is essentially stopped.
- **aw 0.20-0.50:** Increasing water content increases reactant mobility without excessive dilution.
- **aw 0.50-0.70:** Maximum reaction rate — optimal balance of reactant mobility and concentration.
- **aw > 0.70:** Water dilutes reactants, and the reaction is reversed thermodynamically (hydrolysis of the Schiff base intermediate).

This is why milk powder and infant formula stored above aw 0.30 brown progressively during storage — the Maillard reaction consumes lysine (reducing nutritional quality) and produces brown melanoidins, off-flavors, and measurable loss of protein digestibility. A 6-month shelf life at 25°C requires maintaining aw below 0.25 for these products.

### Enzymatic Activity

Enzymes require a hydration shell to maintain their native conformation and catalytic activity. Below aw 0.70-0.75, most enzymes are essentially inactive because the water necessary for the hydration shell is thermodynamically unavailable. However:
- Lipases can remain active to aw 0.30-0.40 in some matrices because the lipid substrate provides sufficient hydrophobic environment for interfacial activation
- Polyphenol oxidase (PPO) requires aw > 0.70 for significant activity
- Some enzymes show residual activity even in freeze-dried powders if aw exceeds 0.25-0.30, which is why freeze-dried enzyme preparations are stored with desiccants

## Industrial Measurement Methods

### Reference Methods

**Chilled Mirror Dew Point (AOAC 978.18):** The gold standard for aw measurement. A sample is equilibrated in a sealed chamber, and a cooled mirror detects the dew point of the headspace. Accuracy: ±0.003 aw. Measurement time: 2-5 minutes. This is the method required by FDA, USDA, and USDA FSIS for regulatory compliance testing.

**Capacitance/Impedance Sensors:** Polymer film sensors that change capacitance or resistance as a function of relative humidity. Accuracy: ±0.01-0.02 aw. Response time: 30 seconds-5 minutes. Suitable for routine QC but require regular calibration against saturated salt standards.

**Resistive (Electrolytic) Sensors:** Older technology using lithium chloride or other hygroscopic electrolytes. Accuracy: ±0.02 aw. Slower response (5-15 minutes). Less common in modern labs but still used in some inline process monitoring applications.

### Best Practices for Industrial Measurement

Sample temperature must be controlled to ±0.2°C because aw is temperature-dependent. Sample preparation: High-fat samples may require extended equilibration (30-60 min) because fat slows water vapor diffusion. Samples should fill at least 50% of the measurement cup volume. Calibration should be performed daily with saturated salt solutions (LiCl: aw 0.113, MgCl₂: aw 0.328, NaCl: aw 0.753, KCl: aw 0.851).

## Research Evidence & Data Summary

| Finding | Key Data | Source & Year |
|---------|----------|---------------|
| Water activity definition validated for microbial growth | Bacterial growth requires aw ≥ 0.91; no growth below 0.60 | Scott, 1957 |
| Microbial growth minima by organism class | Bacteria: 0.91 (most), 0.86 (S. aureus); Yeasts: 0.88; Molds: 0.80 (0.61 Xeromyces) | Beuchat, 1981, J. Food Prot. 44(9) |
| Lipid oxidation vs aw: U-shaped curve | Minimum at aw 0.2-0.4 (monolayer) | Labuza, 1980, Food Technol. 34(5) |
| Maillard reaction peak aw | Maximum rate at aw 0.5-0.7 | Labuza & Saltmarch, 1981 |
| FDA critical control point | aw ≤ 0.85 — non-TCS food, exempt from refrigeration | FDA Food Code, 2022 |
| Glycerol aw reduction efficiency | aw reduced to 0.80 at ~50% glycerol (w/w) | Chirife et al., 1980, J. Food Sci. |
| Sucrose aw reduction | aw 0.90 at ~55% sucrose; aw 0.80 at ~65% | Sloan & Labuza, 1975 |
| Measurement accuracy | Dew point: ±0.003 aw; Capacitance: ±0.01-0.02 aw | AOAC 978.18 |
| aw temperature coefficient | aw increases 0.002-0.01/°C | Rahman, 2007, Food Properties Handbook |
| Moisture sorption isotherm hysteresis | Desorption aw > adsorption aw by 0.02-0.10 | Al-Muhtaseb et al., 2002, J. Food Eng. |

## Current Scientific Understanding

The scientific consensus on water activity as a preservation parameter is robust and mature — rare in food science. The glass transition (Tg) concept introduced by Levine and Slade in the 1990s initially challenged aw doctrine by proposing that molecular mobility — not thermodynamic water activity — was the true determinant of food stability. However, the current synthesis recognizes both aw and Tg as complementary: aw governs equilibrium thermodynamic properties (microbial growth, chemical potential), while Tg governs kinetic properties (diffusion-limited reactions, physical state).

In practical terms, aw remains the primary specification for food safety (microbial growth control) and the secondary specification for quality (chemical reaction rates), while Tg is the primary specification for physical stability (caking, collapse, crystallization) in low-moisture foods.

Open questions include the molecular-level mechanism by which water activity influences reaction kinetics in heterogeneous food matrices (as opposed to homogeneous solutions), the role of aw gradients in multi-component foods (e.g., a sandwich cookie where the cream and cookie have different aw), and the validation of predictive models for aw-controlled hurdle technologies in novel food matrices.

## Frequently Asked Questions

<div class="faq-container">
  <div class="faq-item">
<h3 class="faq-question">What is the difference between water activity and moisture content?</h3>
<p>Moisture content is the total amount of water in a food, expressed as a percentage of weight. Water activity (aw) is the thermodynamic availability of that water — how much is "free" to participate in reactions and support microbial growth. Two foods can have identical moisture content but very different aw. Soy sauce (71% moisture, aw 0.80) has much more water than honey (17% moisture, aw 0.55), but honey's water is "freer" because soy sauce's high salt concentration binds its water. This is why aw, not moisture content, is the regulatory standard for food safety classification.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">Why is aw 0.85 the critical regulatory threshold?</h3>
<p>The FDA Food Code designates aw 0.85 as the boundary between Time/Temperature Control for Safety (TCS) foods and non-TCS foods. This threshold is based on the minimum aw for growth of *Staphylococcus aureus* enterotoxin production (aw 0.86-0.90) with a safety margin. If aw ≤ 0.85 and pH ≤ 4.6, the food is considered non-potentially-hazardous and does not require refrigeration. This regulatory framework, grounded in decades of food microbiology research, enables the ambient-stable distribution of products like jerky, dried fruit, jam, and hard cheese without cold chain infrastructure.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">How does temperature affect water activity?</h3>
<p>Water activity increases with temperature (approximately 0.002-0.01 per °C at constant moisture content), following the Clausius-Clapeyron relationship. A product that measures aw 0.83 at 20°C could reach aw 0.85-0.86 at 35°C — potentially crossing the regulatory TCS threshold or the mold growth boundary. This is why aw must always be reported with measurement temperature and why QC specifications must account for the temperature range the product will experience throughout distribution. For accurate shelf life prediction, measure aw at the intended storage temperature or apply a validated correction factor.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">Can I reduce water activity just by adding salt or sugar?</h3>
<p>Yes, but the amount required depends on the target aw. Sodium chloride at 2% concentration reduces aw by only ~0.01 — negligible for microbial control. At 10% (~aw 0.93), NaCl inhibits most pathogens. At 18-20% (~aw 0.80-0.85), NaCl prevents all bacterial growth. Sugar (sucrose) is less effective per gram — you need approximately 55% sucrose to reach aw 0.90 and 65% to reach aw 0.80. Glycerol and propylene glycol are more efficient humectants: glycerol at 30% concentration can reduce aw below 0.85. The practical implication is that salt-preserved foods must be very salty (unpalatable as-is), while sugar-preserved foods (jam, condensed milk) can be quite sweet but fundamentally stable.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">Why do some chemical reactions peak at intermediate aw values?</h3>
<p>The bell-shaped curve for Maillard browning (peak aw 0.5-0.7) and U-shaped curve for lipid oxidation reflect the competing effects of water as reactant mobilizer vs reactant diluter. At very low aw, reactants are immobilized and diffusion-limited. As aw increases, molecular mobility enables reactants to encounter each other. At high aw, water simply dilutes the reactants, slowing the reaction despite maximum mobility. The exact peak depends on the specific reactants, temperature, and food matrix — this is why barrier packaging that maintains aw at the "sweet spot" for stability (not too dry, not too wet) is a critical formulation consideration for intermediate-moisture foods.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">How is aw measured in an industrial QC lab?</h3>
<p>The industry standard is the chilled mirror dew point instrument (Meter AquaLab, Rotronic HygroLab), which measures the dew point of air equilibrated with the sample in a sealed chamber. Measurement takes 2-5 minutes with ±0.003 aw accuracy. The sample is placed in a disposable cup, loaded into the chamber, and the instrument automatically detects equilibrium (typically when the rate of change falls below 0.001 aw/min). Daily calibration uses saturated salt standards. Capacitance-based instruments (±0.01-0.02 aw) are used for rapid screening. Key QC requirements: sample temperature must be controlled to ±0.2°C, high-fat samples need 30-60 minutes equilibration, and results should be reported with measurement temperature and instrument type.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">Can molds grow on dry foods in the refrigerator?</h3>
<p>Yes, if condensation occurs. The food itself may have aw < 0.60 (microbiologically stable), but condensation from temperature fluctuations creates a thin surface layer of water with aw ~1.0 — ideal for mold spore germination. This is why bread stored in a plastic bag in the refrigerator develops surface mold at the condensation points, why cheese wrapped in plastic wrap molds at the plastic-food interface, and why opened jam jars mold at the surface where water activity increases due to moisture absorption. The solution: for low-aw foods, prevent condensation (use breathable packaging, avoid temperature cycling); for refrigerated foods, maintain stable, low temperature to minimize condensation cycles.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What happens to aw during freezing?</h3>
<p>Freezing concentrates solutes in the unfrozen water phase, reducing the aw of the unfrozen fraction. At −18°C, the effective aw of the unfrozen phase is approximately 0.82 (determined by the freezing point depression equation: ln(aw) = −ΔH_f/R × (1/T − 1/T_f), where T_f is the freezing point of pure water). This is why frozen foods are microbiologically stable — no microorganism can grow at aw 0.82 at −18°C despite free water being physically present. However, as temperature increases during thawing, aw rapidly returns to its pre-freezing value (~0.98-0.99 for most foods), and thawed product is more susceptible to microbial growth due to cell damage and released nutrients.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">How does humidity affect dry goods even through packaging?</h3>
<p>Most consumer packaging (paperboard, thin LDPE, cellophane) is NOT an effective moisture barrier — it has moisture vapor transmission rates (MVTR) of 1-100 g/m²/day depending on material and thickness. Over weeks to months, significant moisture can penetrate. A 0.5 mm LDPE bag with MVTR ~5 g/m²/day at 75% RH will transmit enough moisture to raise aw of 200g of crackers by 0.02 per month in a humid environment. This is why "best by" dates on dry goods often reflect moisture absorption as the limiting factor, not microbial or chemical stability per se. Industrial moisture barrier packaging (aluminum foil laminates, metallized PET, EVOH) has MVTR < 0.1 g/m²/day and can maintain aw for years.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What is the relationship between aw and the glass transition temperature (Tg)?</h3>
<p>Water is a powerful plasticizer — it lowers the glass transition temperature by increasing molecular mobility in the amorphous (non-crystalline) regions of foods. A cracker at aw 0.20 may have Tg > 40°C (glassy, crisp), while the same cracker at aw 0.50 may have Tg below 20°C (rubbery, soft, stale). The critical practical implication: for crisp, brittle texture stability, the product temperature must remain BELOW Tg, which requires maintaining aw below the value that plasticizes the matrix to Tg = ambient temperature. This aw-Tg relationship, not microbial stability, is often the true shelf life limiter for dry snack foods, breakfast cereals, and crackers.</p>
</div>
</div>

## Related Research

- [What Makes Food Go Bad?](what-makes-food-go-bad.md) — The five fundamental spoilage mechanisms explained
- [Microbial vs Chemical Spoilage Explained](microbial-vs-chemical-spoilage-explained.md) — How aw determines which pathway dominates
- [Food Science Basics](food-science-basics.md) — Foundational principles of industrial food stability
- [Shelf-Stable Foods Science](shelf-stable-foods-science.md) — Why some foods don't need refrigeration
- [Cold Chain Management](cold-chain-management-complete-guide.md) — How temperature control extends or fails to extend shelf life

## References

<ol class="references">
<li id="ref1">Scott, W.J. (1957). Water relations of food spoilage microorganisms. <em>Advances in Food Research</em>, 7, 83-127. DOI: 10.1016/S0065-2628(08)60247-5</li>
<li id="ref2">Beuchat, L.R. (1981). Microbial stability as affected by water activity. <em>Journal of Food Protection</em>, 44(9), 632-640. DOI: 10.4315/0362-028X-44.9.632</li>
<li id="ref3">Labuza, T.P. (1980). The effect of water activity on reaction kinetics of food deterioration. <em>Food Technology</em>, 34(5), 36-40.</li>
<li id="ref4">Labuza, T.P., Saltmarch, M. (1981). The nonenzymatic browning reaction as affected by water in foods. In: <em>Water Activity: Influences on Food Quality</em>. Academic Press, pp. 605-650.</li>
<li id="ref5">Slade, L., Levine, H. (1991). Beyond water activity: Recent advances based on an alternative approach to the assessment of food quality and safety. <em>Critical Reviews in Food Science and Nutrition</em>, 30(2-3), 115-360. DOI: 10.1080/10408399109527543</li>
<li id="ref6">Chirife, J., Ferro Fontán, C., Benmergui, E.A. (1980). The prediction of water activity in aqueous solutions in connection with intermediate moisture foods. <em>Journal of Food Technology</em>, 15(1), 59-70. DOI: 10.1111/j.1365-2621.1980.tb00917.x</li>
<li id="ref7">Rahman, M.S. (2007). <em>Handbook of Food Preservation</em>, 2nd ed. CRC Press, Boca Raton, FL. DOI: 10.1201/9781420017373</li>
<li id="ref8">Al-Muhtaseb, A.H., McMinn, W.A.M., Magee, T.R.A. (2002). Moisture sorption isotherm characteristics of food products: A review. <em>Food and Bioproducts Processing</em>, 80(2), 118-128. DOI: 10.1205/09603080252938753</li>
<li id="ref9">FDA (2022). <em>Food Code</em>, Chapter 1, Section 1-201.10(B): Definition of Time/Temperature Control for Safety Food. U.S. Department of Health and Human Services.</li>
<li id="ref10">Pitt, J.I., Hocking, A.D. (2009). <em>Fungi and Food Spoilage</em>, 3rd ed. Springer, New York. DOI: 10.1007/978-0-387-92207-2</li>
<li id="ref11">Rockland, L.B., Beuchat, L.R. (1987). <em>Water Activity: Theory and Applications to Food</em>. Marcel Dekker, New York.</li>
<li id="ref12">Fennema, O.R. (1996). Water and ice. In: <em>Food Chemistry</em>, 3rd ed. Marcel Dekker, pp. 17-94.</li>
<li id="ref13">AOAC International (2019). Official Method 978.18: Water Activity of Canned Vegetables. <em>Official Methods of Analysis</em>, 21st ed.</li>
<li id="ref14">Leistner, L. (2000). Basic aspects of food preservation by hurdle technology. <em>International Journal of Food Microbiology</em>, 55(1-3), 181-186. DOI: 10.1016/S0168-1605(00)00161-6</li>
<li id="ref15">Sloan, A.E., Labuza, T.P. (1975). Prediction of water activity lowering ability of food humectants. <em>Food Product Development</em>, 9(9), 68-78.</li>
</ol>
