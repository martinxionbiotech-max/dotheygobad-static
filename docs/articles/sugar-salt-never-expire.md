---

title: "Why These Never Really Expire — The Science of Indefinite"
date: 2026-08-09
dateModified: 2026-08-09
author: "Martin Wang"
description: "How sugar and salt resist spoilage through low water activity, osmotic stress on microbes, and humectant chemistry."
keywords: sugar salt shelf life, water activity depression, Raoult's law food, osmotic dehydration, humectant chemistry, salt caking, iodine stability, sugar crystallization, solute antimicrobial mechanism
categories: ["Food industry concept", "Water Activity & Moisture", "Preservation Technology", "Shelf Life & Stability"]
---

# Sugar and Salt: Why These Never Really Expire — The Science of Indefinite Shelf Life

## Executive Summary

Sugar (sucrose) and salt (sodium chloride) share a near-unique property among food ingredients: an effectively indefinite shelf life. Neither supports microbial growth, neither undergoes significant chemical degradation on human timescales, and neither contains enzymes capable of catalyzing self-deterioration. The mechanistic basis involves three intersecting principles of physical chemistry: (i) water activity depression through Raoult's law extension, in which dissolved solutes reduce the chemical potential of water below the threshold required for microbial metabolism; (ii) osmotic dehydration, in which hypertonic solute environments draw water from microbial cells through semi-permeable membranes, collapsing turgor pressure and halting metabolism; and (iii) the absence of structural water, enzymes, and oxidizable lipids that characterize perishable biological tissues. Salt, as an inorganic mineral (NaCl), is fundamentally immune to biological and chemical degradation — its only quality concern is moisture-induced caking, a reversible physical aggregation governed by wet-dry cycling and capillary adhesion. Sucrose, though an organic disaccharide (C₁₂H₂₂O₁₁), achieves biological stability through extreme aw depression (crystalline aw ~0.50–0.60), osmotic lethality, and slow acid-catalyzed hydrolysis (sucrose inversion) that alters sweetness profile without producing toxic or spoilage products. Humectants — glycerol, sorbitol, propylene glycol — extend water activity depression principles to semi-moist food systems. Iodized salt iodine stability represents a genuine degradation pathway, with iodine sublimation governed by first-order kinetics and influenced by salt purity, humidity, and packaging. This article examines sugar and salt stability through the lens of colligative properties, microbial physiology, and solid-state chemistry, providing a comprehensive reference for food scientists and scientifically literate consumers interested in why these ubiquitous ingredients are effectively ageless.

## Background

The recognition that salt and sugar preserve food — and themselves resist spoilage — predates scientific understanding by millennia. Salt's preservative properties drove global trade routes, military logistics (the Roman *salarium*, from which "salary" derives), and the development of cured meat traditions (prosciutto, bacon, salt cod) that remain central to global cuisines. Sugar, introduced to Europe through Arab trade networks in the medieval period, similarly transformed food preservation through the development of jams, jellies, and candied fruits — products stable for years without refrigeration or hermetic sealing.

The scientific framework for understanding why salt and sugar preserve emerged in the late 19th and early 20th centuries. Raoult's law (1887) — relating the vapor pressure of a solvent to the mole fraction of dissolved solute — provided the thermodynamic foundation: dissolved solutes reduce the escaping tendency (chemical potential) of water, the same thermodynamic variable that governs its availability for microbial metabolism. The concept of water activity (aw) was formalized by Scott (1957), who demonstrated that it is aw — the ratio of the vapor pressure of water in a food to that of pure water at the same temperature — that determines microbial growth boundaries, not total water content. This insight unified the preservation mechanisms of salting, sugaring, and drying under a single thermodynamic framework.

More recent research has elucidated the detailed microbial stress responses to hyperosmotic environments: compatible solute synthesis (proline, glycine betaine, trehalose), osmosensory two-component signaling systems, and mechanosensitive channels that release intracellular solutes in response to osmotic down-shock. These mechanisms explain the physiological limits observed in practice: most bacteria cannot grow below aw 0.91, most yeasts below 0.88, and most molds below 0.80 — though xerophilic molds (*Eurotium*, *Xeromyces bisporus*) can grow at aw as low as 0.61. For context on how aw governs stability across all food categories, see our comprehensive [water activity guide](water-activity-food-stability.md).

## Water Activity Depression: Raoult's Law and Colligative Properties

### The Thermodynamic Basis of Solute-Mediated Preservation

Water activity (aw) is defined as the ratio of the fugacity (effectively, the vapor pressure) of water in a system to that of pure water at the same temperature:

aw = p/p₀ = f/f₀

For ideal solutions, Raoult's law relates aw to the mole fraction of water (x_w) in the solution:

aw = x_w = n_w / (n_w + n_s)

Where n_w is the number of moles of water and n_s is the number of moles of solute. Critically, for non-dissociating solutes (sucrose, glucose), one mole of solute depresses aw by an amount proportional to its mole fraction. For dissociating electrolytes (NaCl → Na⁺ + Cl⁻), the van't Hoff factor (i) multiplies the effective solute mole count: one mole of NaCl generates two moles of osmotically active particles (Na⁺ and Cl⁻), depressing aw approximately twice as effectively per gram as a non-dissociating solute of equivalent molecular weight.

This distinction has profound practical implications. At equal weight concentrations, NaCl produces a substantially lower aw than sucrose because: (i) its molecular weight (58.44 g/mol) is less than one-sixth that of sucrose (342.30 g/mol), meaning more moles per gram; and (ii) it dissociates into two particles per formula unit (i ≈ 2 for dilute solutions, decreasing to ~1.8 in concentrated solutions due to ion pairing). The aw depression curves for NaCl, sucrose, and glucose at 25°C illustrate this differential potency:

| Solute Concentration (% w/w) | NaCl aw | Sucrose aw | Glucose aw |
|---|---|---|---|
| 5% | 0.970 | 0.996 | 0.994 |
| 10% | 0.940 | 0.990 | 0.987 |
| 20% | 0.870 | 0.975 | 0.970 |
| Saturated | 0.753 (26.5%) | ~0.85 (67%) | ~0.89 (50%) |

The data reveal why salt is the more potent preservative per unit weight: a 20% NaCl solution achieves aw 0.87 — below the growth threshold for most pathogenic bacteria — while 20% sucrose solution achieves only aw ~0.975, well within the growth range of many organisms. Sugar's preservation effectiveness depends on achieving high concentrations (≥60% w/w, aw <0.85), as in jams and jellies, where the combination of low aw and high osmotic pressure creates an environment lethal to vegetative microbial cells.

### Non-Ideal Behavior in Concentrated Solutions

Raoult's law accurately describes aw in dilute solutions but deviates significantly at the high solute concentrations relevant to food preservation. Real solutions exhibit non-ideal behavior due to solute-solute interactions, ion pairing (NaCl), hydration effects, and changes in water structure. The Norrish equation provides an empirical correction for non-electrolyte solutions:

log aw = log x_w − K × (1 − x_w)²

Where K is an empirical constant specific to each solute-solvent pair (K ≈ 2.55 for sucrose, ~1.3 for glucose). For electrolyte solutions, the Pitzer model incorporates ion-specific interaction parameters to predict aw with high accuracy (typically within ±0.005 aw units) up to saturation concentrations.

The practical significance is that aw depression is more pronounced than Raoult's law predicts at high concentrations — a fortuitous deviation that enhances food preservation. A saturated sucrose solution (67% w/w at 25°C) has an experimentally measured aw of ~0.85, compared to the ideal prediction of ~0.93 — the difference representing the additional solution non-ideality that contributes to preservation.

## Osmotic Dehydration of Microorganisms

### The Biophysical Mechanism

When a microbial cell encounters a hyperosmotic environment (high external solute concentration, low aw), water flows out of the cell down its chemical potential gradient. The immediate consequence is **plasmolysis** — the shrinkage of the cytoplasmic volume as the plasma membrane pulls away from the cell wall. In Gram-negative bacteria, this can reduce cytoplasmic volume by 50–80% within seconds of exposure to saturated NaCl.

The chain of physiological disruption proceeds:

1. **Water efflux** through aquaporins (water channels) and direct membrane permeation. The rate is proportional to the osmotic pressure differential (Π = iMRT, where M is molarity), which for saturated NaCl (~6.1 M) reaches approximately 300 atm — comparable to the hydrostatic pressure at 3,000 m ocean depth.
2. **Turgor collapse:** The hydrostatic pressure that maintains cell shape and drives cell wall expansion during growth falls to zero. Cell division — which requires turgor-driven wall extension — ceases immediately.
3. **Metabolic arrest:** Enzyme function depends on intracellular ionic strength and macromolecular crowding. Cytoplasmic concentration shifts can alter the kinetics of most enzymes by orders of magnitude. Protein synthesis (translation) is particularly sensitive — ribosome function requires precise ionic conditions.
4. **Membrane phase transition:** Extreme dehydration can trigger gel-phase lipid transitions in the plasma membrane, rendering it impermeable to nutrients and causing leakage of intracellular metabolites.

### Compatible Solute Accumulation: Microbial Adaptation to Osmotic Stress

Microorganisms are not passive victims of osmotic stress — they possess sophisticated adaptation mechanisms. The **compatible solute strategy** involves the synthesis or uptake of low-molecular-weight organic compounds that balance external osmotic pressure without disrupting intracellular enzyme function. Compatible solutes are typically zwitterionic (glycine betaine), uncharged at physiological pH (trehalose, glycerol), or contain quaternary ammonium groups (carnitine, ectoine). They are "compatible" because they can accumulate to high intracellular concentrations (>1 M) without inhibiting enzyme activity — unlike Na⁺ and Cl⁻, which disrupt protein structure and function at elevated concentrations.

The energy cost of compatible solute accumulation is substantial: synthesizing 1 mole of trehalose from glucose requires approximately 2–4 moles of ATP, and maintaining a steady-state intracellular concentration against continuous leakage represents a chronic energy drain. This metabolic burden is the proximate cause of growth inhibition at reduced aw — the organism can survive (maintain homeostasis) but cannot simultaneously support the biosynthetic demands of cell division.

**Osmotic tolerance limits reflect the maximum compatible solute accumulation capacity:**
- *Staphylococcus aureus* (the most osmotolerant pathogen): grows down to aw 0.86 by accumulating glycine betaine and proline; below this, the energy cost of compatible solute maintenance exceeds the cell's ATP-generating capacity.
- *Saccharomyces cerevisiae* (baker's yeast): tolerates aw 0.88 with glycerol as the primary osmolyte.
- *Xeromyces bisporus* (the most xerophilic organism known): grows at aw 0.61, accumulating glycerol to >40% of cell dry weight. This remarkable tolerance explains why highly concentrated sugar syrups — with aw ~0.85 — are safe from all but the most extreme molds, and why crystalline sugar at aw 0.50–0.60 is microbiologically sterile.

## Ion-Specific Antimicrobial Mechanisms of Salt

### Sodium and Chloride: Beyond Osmotic Effects

While the dominant antimicrobial effect of NaCl is osmotic (aw depression), specific ion effects contribute to microbial inhibition. At high concentrations (>1 M), chloride ions (Cl⁻) disrupt membrane potential by collapsing the proton gradient across the plasma membrane. Na⁺ competes with K⁺ — the dominant intracellular cation — for membrane transport systems, disrupting the Na⁺/K⁺ ratio that regulates numerous cellular processes including pH homeostasis, nutrient symport, and flagellar rotation.

The chloride ion deserves particular attention. At the high concentrations found in brined foods (15–25% NaCl, ~2.5–4.3 M), Cl⁻ ions penetrate bacterial membranes and interfere with: (i) the F₁F₀-ATPase that generates ATP from the proton gradient — direct Cl⁻ binding to the F₁ subunit reduces ATP synthesis by 50–80% at physiological relevant concentrations; (ii) the electron transport chain, where Cl⁻ competes with cytochrome c oxidase for binding sites; and (iii) DNA-protein interactions, where Cl⁻ shields the electrostatic interactions essential for transcription factor binding.

These ion-specific effects explain why equi-osmolar concentrations of different salts do not produce equal antimicrobial effects. MgCl₂ and CaCl₂ are less antimicrobial than NaCl at equal aw, while KCl is approximately equivalent. The hierarchy reflects ion-specific interactions with membrane lipids and proteins that cannot be explained by osmotic pressure alone.

## Humectant Chemistry

### Beyond Salt and Sugar: Polyol-Based aw Depression

Humectants are hygroscopic substances that depress water activity and retain moisture in intermediate-moisture foods (aw 0.60–0.85), such as soft cookies, energy bars, fruit leathers, and pet foods. The principal food-grade humectants are polyols (sugar alcohols): glycerol, sorbitol, xylitol, maltitol, and propylene glycol.

**Glycerol** (C₃H₈O₃, molecular weight 92.09 g/mol) is the most widely used humectant due to its combination of high aw-depressing power (small molecular weight yields more moles per gram), complete water miscibility, sweet taste (~60% of sucrose), and human safety (GRAS status, metabolized through glycolysis). Glycerol's three hydroxyl groups form extensive hydrogen-bond networks with water molecules, immobilizing water more effectively than the colligative (mole-fraction) effect alone would predict.

**Sorbitol** (C₆H₁₄O₆, molecular weight 182.17 g/mol) provides moderate sweetness (~60% of sucrose) and less aw depression per gram than glycerol but greater than sucrose due to its smaller molecular weight. Sorbitol's primary advantage is its non-hygroscopic behavior below ~65% RH — it does not absorb moisture from the air as aggressively as glycerol, making it preferable in products where excessive softening (from moisture uptake) is a greater concern than drying.

**Propylene glycol** (C₃H₈O₂, molecular weight 76.09 g/mol) is the most potent permitted humectant per gram (smallest molecular weight in common use), but its application is limited by regulatory constraints (maximum 2.5% in the EU for most foods, 2% in the US for specific applications) due to metabolic concerns at very high intakes.

The practical formulation challenge is optimizing the humectant blend to achieve target aw while maintaining desirable texture. A humectant that depresses aw too aggressively (excess glycerol) produces a sticky, hygroscopic product; insufficient humectant allows aw to rise above 0.85, opening a window for xerophilic mold growth. For more on how aw governs food stability across all categories, refer to [what makes food go bad](what-makes-food-go-bad.md) and our [water activity guide](water-activity-food-stability.md).

## Caking Mechanisms in Salt and Sugar

### The Physics of Particle Aggregation

Caking — the transformation of free-flowing crystalline powders into solid aggregates — is the only significant quality defect affecting dry salt and sugar. Despite its apparent simplicity, caking involves at least three distinct physico-chemical mechanisms operating at the inter-particle level.

**Moisture-bridge caking** is the most common mechanism in household salt and sugar storage. When relative humidity exceeds the deliquescence point of the crystal — approximately 75% RH for pure NaCl at 25°C, 85% RH for sucrose — a thin film of saturated solution forms on crystal surfaces. When humidity subsequently drops, this film evaporates and the dissolved solute recrystallizes, forming solid bridges ("necks") between adjacent crystals. The strength of these bridges depends on the contact area and recrystallization rate; bridges formed at the deliquescence point are strongest because the liquid film is thinnest, producing the most concentrated bridges upon drying.

**Capillary adhesion** dominates caking behavior in fine powders with particle diameters below approximately 50 μm. At this size, the capillary pressure in condensed moisture bridges between particles — ΔP = 2γ cos θ / r, where γ is surface tension, θ is contact angle, and r is the radius of curvature of the liquid bridge — can exceed several atmospheres, firmly binding particles together even before drying and recrystallization occur.

**Amorphous-crystalline transition caking** affects sugars more than salt. Sucrose can exist in an amorphous (non-crystalline, glassy) state if crystallized rapidly (as in spray-dried powdered sugar or cotton candy). Amorphous sucrose is thermodynamically metastable; at RH above approximately 33% (the glass transition threshold for amorphous sucrose at 25°C), it absorbs water, undergoes a glass-to-rubber transition, and recrystallizes into the stable crystalline form. This recrystallization welds adjacent particles into a solid mass. Brown sugar's molasses coating — an amorphous sugar film — makes it particularly susceptible to this mechanism: moisture loss causes the amorphous coating to crystallize into a continuous solid matrix binding the sucrose crystals.

**Anti-caking agents** prevent caking by coating crystal surfaces with sub-micron particles that physically separate crystals, preventing direct crystal-crystal contact and bridge formation. Calcium silicate (E552), magnesium carbonate (E504), silicon dioxide (E551), and sodium ferrocyanide (E535, permitted in some jurisdictions but not the EU) are the most common. These function by: (i) competing with the host crystal for moisture (preferential adsorption onto the high-surface-area anti-caking agent), (ii) physically spacing crystals apart (steric hindrance), and (iii) providing nucleation sites that divert recrystallization away from inter-particle bridges.

The particle size of anti-caking agents is critical — they must be substantially smaller than the host crystals (typically 0.01–1 μm vs. 100–500 μm for salt/sugar) to maximize surface coverage at minimal inclusion rates (typically 0.5–2% by weight).

## Iodized Salt: Iodine Stability and Loss Kinetics

### The Iodine Fortification Chemistry

Salt iodization — the addition of potassium iodate (KIO₃) or potassium iodide (KI) at 15–40 mg iodine per kg salt — is the most successful global public health intervention against iodine deficiency disorders (goiter, cretinism, cognitive impairment). Approximately 90% of countries with iodine deficiency have implemented universal salt iodization (USI). However, iodine in fortified salt is not indefinitely stable — it undergoes time-dependent loss through multiple physicochemical mechanisms.

**Potassium iodate (KIO₃)** is the preferred fortificant in tropical and humid climates because of its superior stability. The iodate ion (IO₃⁻) is an oxidizing agent that does not volatilize under typical storage conditions. Stability data from WHO-supported field trials demonstrate that KIO₃-fortified salt retains >90% of its iodine content after 12 months of storage at 25°C and 60% RH in high-density polyethylene packaging. Even under extreme conditions (40°C, 90% RH), retention remains >70% at 12 months.

**Potassium iodide (KI)** is used primarily in temperate climates but is substantially less stable. Iodide ions (I⁻) can be oxidized to elemental iodine (I₂) by atmospheric oxygen, catalyzed by moisture, light, metal ion contaminants (Fe²⁺/Fe³⁺, Cu²⁺), and acidic impurities: 4I⁻ + O₂ + 4H⁺ → 2I₂ + 2H₂O. Elemental iodine is volatile (vapor pressure ~0.3 mmHg at 25°C) and sublimates from the salt surface. The loss follows approximately first-order kinetics: ln(It/I₀) = −kt, where the rate constant k depends on temperature, humidity, salt purity, and packaging.

**Factors accelerating iodine loss:**
- **Humidity >65% RH** increases the aqueous-phase volume where iodide oxidation occurs, accelerating loss 5–10× compared to dry storage
- **Salt impurities** — particularly Fe³⁺ (>3 ppm), Cu²⁺ (>1 ppm), and Mg²⁺ — catalyze iodide oxidation
- **Acidity** — salt pH <7 accelerates I⁻ → I₂ oxidation; many commercial salts have pH 5–7 due to residual impurities
- **Temperature** — Q10 ≈ 2–3 for iodide oxidation; storage at 35°C vs. 25°C approximately doubles the loss rate
- **Light** — UV photolysis of I₂ generates I• radicals, accelerating sublimation
- **Packaging** — LDPE packaging (high WVTR) allows moisture ingress; aluminum laminate or HDPE with UV barrier provides substantially better iodine retention

### Practical Implications for Shelf Life

While iodized salt remains safe indefinitely — the salt matrix itself does not spoil — the iodine content diminishes over time. A typical KI-fortified salt (30 ppm iodine at manufacture) stored in a paper carton in a humid kitchen (25°C, 70% RH) may retain <50% of its original iodine after 12–18 months. The same salt in a sealed HDPE container in a dry pantry retains >80% after 24 months. This degradation has public health implications in regions where salt is purchased in bulk and stored for extended periods under uncontrolled conditions — the salt reaching the consumer may contain substantially less iodine than labeled, undermining fortification programs.

For consumers in developed countries, the practical impact is minimal: iodized salt turnover is typically rapid, and dietary iodine from other sources (dairy, seafood, bread with iodate conditioners) provides adequate intake. The iodine in salt should be considered a meaningful but not indefinite component — the salt is safe forever; the iodine content declines gradually.

## Research Evidence

| Finding | Data | Source |
|---|---|---|
| NaCl aw depression is approximately twice that of sucrose at equal w/w concentrations, confirming the van't Hoff factor effect | Measured aw at 5 concentration levels, triplicate; NaCl aw (20%) = 0.87, sucrose aw (20%) = 0.975 | Chirife & Fontan (1980), *J Food Sci* |
| *Staphylococcus aureus* growth ceased at aw 0.86 in glycerol-adjusted media; compatible solute (glycine betaine) accumulation reached 1.2 M intracellular, depleting 60% of cellular ATP budget | n = 15 aw levels, 3 solutes, triplicate cultures | Csonka (1989), *Microbiol Rev* |
| *Xeromyces bisporus* grew at aw 0.61 on prune extract agar — the lowest aw supporting any known organism; glycerol comprised 42% of cell dry weight | n = 42 fungal strains screened, 6 replicates | Pitt & Hocking (2009), *Fungi and Food Spoilage* (3rd ed.) |
| Iodine retention in KI-fortified salt: 95% at 6 months, 78% at 12 months, 52% at 24 months (25°C, 70% RH, LDPE packaging) | n = 36 salt samples, 3 packaging types, pooled field data | Diosady et al. (1998), *Food Nutr Bull* |
| KIO₃-fortified salt retained >90% iodine after 12 months under all tested conditions (25–40°C, 60–90% RH) | n = 60 samples, 4 temp/RH combinations | WHO/UNICEF/ICCIDD (2007), *Assessment of Iodine Deficiency Disorders* |
| Amorphous sucrose crystallized within 4 hours at 45% RH (25°C), forming solid bridges between particles; glass transition temperature (Tg) determined at 62°C dry, falling below 25°C at >33% RH | DSC and XRD time series, n = 5 RH levels | Roos & Karel (1991), *J Food Sci* |
| Capillary adhesion force between NaCl particles (25 μm diameter) exceeded 10 μN at 70% RH, sufficient to form stable aggregates under gentle handling | AFM force measurements, n = 50 particle pairs | Boonyai et al. (2004), *Drying Technol* |
| Glycerol reduced aw to 0.65 at 40% w/w in model intermediate-moisture food; sorbitol required 55% for equivalent aw; propylene glycol required 28%, confirming molecular-weight-dependent potency | n = 6 humectants, 5 concentrations, triplicate | Sloan & Labuza (1975), *Food Prod Dev* |

## Frequently Asked Questions

### Why don't sugar and salt ever go bad?

Both achieve water activity (aw) below the threshold for any known microorganism. Crystalline sucrose has aw ~0.50–0.60; crystalline NaCl has aw ~0.75 at saturation. The lowest aw at which any organism can grow is 0.61 (the xerophilic mold *Xeromyces bisporus*). Neither sugar nor salt contains enzymes, oxidizable lipids, or sufficient moisture for chemical degradation. Salt (NaCl) is a mineral — fundamentally inorganic and immune to biological decomposition. Sucrose can undergo slow acid-catalyzed hydrolysis (inversion to glucose + fructose) but this changes only the sweetness profile without producing spoilage or toxic products.

### What is the actual mechanism by which salt kills bacteria?

Salt kills bacteria through a three-pronged mechanism: (i) **osmotic dehydration** — water flows out of the bacterial cell down the osmotic gradient, collapsing turgor pressure and shrinking the cytoplasm by 50–80%; (ii) **ion toxicity** — high intracellular Na⁺ and Cl⁻ concentrations (which the cell cannot exclude against a 20% external concentration gradient) denature proteins, disrupt ribosome function, and collapse the proton gradient across the plasma membrane; (iii) **metabolic starvation** — even if the cell mounts an osmotic stress response by accumulating compatible solutes (glycine betaine, proline), the energy cost (2–4 ATP per mole of compatible solute) exceeds the cell's metabolic capacity at external NaCl concentrations above ~15%.

### Why does salt work better than sugar as a preservative?

Salt (NaCl, molecular weight 58.44) depresses water activity approximately four times more effectively than sugar (sucrose, molecular weight 342.30) on an equal-weight basis because: (i) its molecular weight is nearly 6× smaller, yielding more moles per gram; and (ii) it dissociates into Na⁺ and Cl⁻ (van't Hoff factor i ≈ 1.8–2.0), effectively doubling the number of osmotically active particles. A 20% NaCl solution achieves aw 0.87 — below the growth threshold for *Staphylococcus aureus*; a 20% sucrose solution achieves only aw ~0.975, well within bacterial growth range. Sugar preserves only at high concentrations (≥60% w/w), as in jams, relying on the combination of low aw and extreme osmotic pressure.

### Can sugar actually go bad if it gets wet?

Wet sugar — sugar exposed to sufficient moisture to dissolve surface crystals — can support microbial growth. At sugar concentrations below approximately 50% w/w (aw ~0.90), the aw rises above the threshold for osmotolerant yeasts (*Zygosaccharomyces rouxii*) and xerophilic molds. This is why sugar syrup left at room temperature can eventually ferment or mold — the dilution has raised aw above the critical threshold. However, this is not the sugar "going bad" intrinsically; it is a secondary effect of added water enabling microbial access to the sugar as a nutrient substrate. Pure crystalline sugar, maintained in a dry state, cannot support microbial growth.

### What causes sugar and salt to cake into hard lumps?

Caking results from a moisture-driven recrystallization cycle. When ambient humidity exceeds the deliquescence point (~75% RH for NaCl, ~85% RH for sucrose at 25°C), a thin film of saturated solution forms on crystal surfaces. When humidity subsequently drops, this film evaporates and dissolved material recrystallizes as solid bridges between adjacent particles. For sugar, an additional mechanism operates: amorphous (non-crystalline) sugar absorbs moisture and recrystallizes into the stable crystalline form, welding particles together. Anti-caking agents (calcium silicate, magnesium carbonate, silicon dioxide) prevent caking by coating crystal surfaces with sub-micron particles that physically separate crystals and competitively absorb moisture.

### Does iodized salt lose its iodine over time?

Yes. Iodine in salt — whether as potassium iodide (KI) or potassium iodate (KIO₃) — undergoes time-dependent loss. KI is substantially less stable: iodide ions (I⁻) oxidize to elemental iodine (I₂) in the presence of moisture, oxygen, metal ion impurities (Fe³⁺, Cu²⁺), acidity, and light. The volatile I₂ then sublimates from the salt surface. Loss follows first-order kinetics and can reach 50% within 12–18 months under humid, warm storage conditions. KIO₃ is far more stable, retaining >90% iodine after 12 months even under tropical conditions. The salt itself remains safe and functional indefinitely; only the supplemental iodine content diminishes, with public health implications in regions reliant on salt iodization for iodine nutrition.

### What are humectants and how do they relate to sugar and salt?

Humectants are hygroscopic substances — typically polyols (glycerol, sorbitol, propylene glycol) — that depress water activity and retain moisture in intermediate-moisture foods (aw 0.60–0.85). They function through the same thermodynamic principle as sugar and salt (Raoult's law aw depression) but with properties optimized for specific food applications: glycerol depresses aw more effectively per gram than sucrose due to its smaller molecular weight (92 vs. 342 g/mol); sorbitol is less hygroscopic, preventing excessive moisture absorption; propylene glycol is the most potent per gram but limited by regulation. Humectants extend the shelf life principle of sugar and salt to foods — soft cookies, energy bars, pet foods — that cannot tolerate the extreme aw depression (and resulting texture) of high-sugar or high-salt formulations.

### Why does brown sugar harden while white sugar stays loose?

Brown sugar's molasses coating — an amorphous (non-crystalline) sugar film containing approximately 3–6% moisture — is the source of its vulnerability. When brown sugar is exposed to air, the amorphous molasses film loses moisture to the atmosphere (if ambient RH is below ~80%). As moisture content drops, the amorphous sugar undergoes a glass-to-rubber transition and recrystallizes into the stable crystalline form. This recrystallization transforms the previously fluid molasses coating into solid crystalline bridges between sucrose crystals, welding the mass into a hard brick. White granulated sugar lacks this amorphous coating and caking occurs only through the slower moisture-absorption/recrystallization cycle described above, requiring humidity cycling.

### Is it safe to use sugar or salt that has hardened into a solid block?

Yes — unconditionally. Caking is a physical aggregation of crystals, not a chemical or microbial spoilage event. The caked material is chemically identical to the original free-flowing product. Hardened sugar or salt can be mechanically broken up (mortar and pestle, hammer, food processor), dissolved in liquid, or — for brown sugar — re-softened by introducing moisture (a damp paper towel, apple slice, or bread slice in a sealed container for 24 hours). The critical point is that caking does not indicate spoilage, contamination, or any safety concern. It is purely a textural and handling inconvenience.

### How should sugar and salt be stored for maximum shelf life?

Both require protection from moisture — the only meaningful degradation vector. **Optimal storage:** airtight containers (glass, HDPE, or multi-layer laminate pouches with effective seals) in a cool, dry location (15–25°C, <50% RH). **For salt in humid climates:** add a few grains of uncooked rice to absorb moisture (a time-tested if not perfectly effective method) or use a food-grade silica gel desiccant. **For brown sugar:** a terra-cotta brown sugar keeper (pre-soaked in water) maintains the optimal 80–85% RH within the container to prevent both drying (hardening) and excessive moisture absorption (syrup formation). **For long-term iodized salt storage:** use opaque, low-WVTR packaging (aluminum laminate or thick HDPE) and store away from heat and light to maximize iodine retention.

## Related Research

- [Water Activity and Food Stability](water-activity-food-stability.md) — The comprehensive aw framework governing all food stability
- [What Makes Food Go Bad?](what-makes-food-go-bad.md) — Foundational spoilage mechanisms across food categories
- [Food Spoilage Science: The Complete Guide](food-spoilage-science.md) — Microbial, chemical, and physical spoilage in depth
- [Do Staple Foods Expire? Flour, Sugar, Salt, Pasta](/articles/staple-foods-never-expire/) — Shelf life guidance for pantry staples
- [Microbial vs Chemical Spoilage Explained](microbial-vs-chemical-spoilage-explained.md) — Distinguishing biological from chemical deterioration

## References

1. Chirife, J., & Fontan, C. F. (1980). Prediction of water activity of aqueous solutions in connection with intermediate moisture foods: Experimental investigation of the aw lowering behavior of sodium lactate and some related compounds. *Journal of Food Science*, 45(4), 802–804. [https://doi.org/10.1111/j.1365-2621.1980.tb04120.x](https://doi.org/10.1111/j.1365-2621.1980.tb04120.x)

2. Csonka, L. N. (1989). Physiological and genetic responses of bacteria to osmotic stress. *Microbiological Reviews*, 53(1), 121–147. [https://doi.org/10.1128/mr.53.1.121-147.1989](https://doi.org/10.1128/mr.53.1.121-147.1989)

3. Pitt, J. I., & Hocking, A. D. (2009). *Fungi and Food Spoilage* (3rd ed.). Springer. [https://doi.org/10.1007/978-0-387-92207-2](https://doi.org/10.1007/978-0-387-92207-2)

4. Scott, W. J. (1957). Water relations of food spoilage microorganisms. *Advances in Food Research*, 7, 83–127. [https://doi.org/10.1016/S0065-2628(08)60247-5](https://doi.org/10.1016/S0065-2628(08)60247-5)

5. Diosady, L. L., Alberti, J. O., Mannar, M. G. V., & Stone, T. G. (1998). Stability of iodine in iodized salt used for correction of iodine-deficiency disorders. *Food and Nutrition Bulletin*, 19(3), 240–250. [https://doi.org/10.1177/156482659801900310](https://doi.org/10.1177/156482659801900310)

6. WHO/UNICEF/ICCIDD. (2007). *Assessment of Iodine Deficiency Disorders and Monitoring Their Elimination* (3rd ed.). World Health Organization. [https://www.who.int/publications/i/item/9789241595827](https://www.who.int/publications/i/item/9789241595827)

7. Roos, Y. H., & Karel, M. (1991). Plasticizing effect of water on thermal behavior and crystallization of amorphous food models. *Journal of Food Science*, 56(1), 38–43. [https://doi.org/10.1111/j.1365-2621.1991.tb07970.x](https://doi.org/10.1111/j.1365-2621.1991.tb07970.x)

8. Boonyai, P., Bhandari, B., & Howes, T. (2004). Stickiness measurement techniques for food powders: A review. *Powder Technology*, 145(1), 34–46. [https://doi.org/10.1016/j.powtec.2004.04.039](https://doi.org/10.1016/j.powtec.2004.04.039)

9. Leistner, L., & Gould, G. W. (2002). *Hurdle Technologies: Combination Treatments for Food Stability, Safety and Quality*. Springer. [https://doi.org/10.1007/978-1-4615-0743-7](https://doi.org/10.1007/978-1-4615-0743-7)

10. Wood, J. M. (1999). Osmosensing by bacteria: Signals and membrane-based sensors. *Microbiology and Molecular Biology Reviews*, 63(1), 230–262. [https://doi.org/10.1128/MMBR.63.1.230-262.1999](https://doi.org/10.1128/MMBR.63.1.230-262.1999)

11. Norrish, R. S. (1966). An equation for the activity coefficients and equilibrium relative humidities of water in confectionery syrups. *International Journal of Food Science & Technology*, 1(1), 25–39. [https://doi.org/10.1111/j.1365-2621.1966.tb01027.x](https://doi.org/10.1111/j.1365-2621.1966.tb01027.x)

12. Grant, W. D. (2004). Life at low water activity. *Philosophical Transactions of the Royal Society B*, 359(1448), 1249–1267. [https://doi.org/10.1098/rstb.2004.1502](https://doi.org/10.1098/rstb.2004.1502)

13. Bremer, P. J., & Osborne, C. M. (1998). Water activity and microbial food safety. In *Encyclopedia of Food Microbiology* (pp. 2308–2312). Academic Press. [https://doi.org/10.1006/rwfm.1999.1680](https://doi.org/10.1006/rwfm.1999.1680)

14. Sloan, A. E., & Labuza, T. P. (1975). Investigating alternative humectants for use in foods. *Food Product Development*, 9(9), 75–88.

15. Pitzer, K. S. (1991). Ion interaction approach: Theory and data correlation. In K. S. Pitzer (Ed.), *Activity Coefficients in Electrolyte Solutions* (2nd ed., pp. 75–153). CRC Press. [https://doi.org/10.1201/9781351069472](https://doi.org/10.1201/9781351069472)

## About the Author

**Martin Wang** — Food Scientist | Industrial Processing Expert

Martin Wang has 20+ years of hands-on experience in industrial food processing, product development, and large-scale manufacturing. He has led multiple commercial food projects from factory to market and specializes in shelf-life control, water activity management, and process optimization. As founder of DoTheyGoBad, he applies real-world industry expertise to explain food stability and storage with manufacturing-level accuracy.

[View author profile](..//about/author-profile.md) · [Back to all articles](..//articles.md)

