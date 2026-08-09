---
title: Water Safety Risk Calculator
date: 2026-02-06
description: Water Safety Risk Calculator water-tool { font-family: system-ui; max-width: 800px; margin: 0 auto; padding: 20px; background: f9f9f9; border-radius: 8px; } wat
---
# Water Safety Risk Calculator

#water-tool { font-family: system-ui; max-width: 800px; margin: 0 auto; padding: 20px; background: #f9f9f9; border-radius: 8px; }
#water-tool label { display: block; margin-top: 15px; font-weight: 600; }
#water-tool select, #water-tool input { width: 100%; padding: 8px; margin-top: 5px; border: 1px solid #ddd; border-radius: 4px; }
#water-tool button { margin-top: 20px; padding: 10px 20px; background: #2d6a4f; color: white; border: none; border-radius: 4px; cursor: pointer; }
#water-tool .result { margin-top: 20px; padding: 15px; border-radius: 6px; }
#water-tool .low { background: #d4edda; border-left: 4px solid #28a745; }
#water-tool .medium { background: #fff3cd; border-left: 4px solid #ffc107; }
#water-tool .high { background: #f8d7da; border-left: 4px solid #dc3545; }

  
## Water Safety Risk Assessment Tool

  
This tool helps assess the food safety risk level of water based on source, treatment, and storage parameters.

  
  Water Source:
  
    Municipal / Treated Supply
    Private Well / Groundwater
    Surface Water (River, Lake)
    Rainwater Harvested
  
  
  Treatment Level:
  
    Advanced (RO, UV + Filtration + Chlorination)
    Standard (Chlorination + Filtration)
    Basic (Boiling or Simple Filtration)
    None / Untreated
  
  
  Storage Condition:
  
    Sealed / Sanitary Tank
    Covered but Not Sealed
    Open Container / Exposed
  
  
  Intended Use:
  
    Food Ingredient / Direct Contact
    Processing Aid (Washing, Cleaning)
    Non-Food (Cooling, Sanitation Only)
  
  
  Calculate Risk Score
  
  

function calculateRisk() {
  const sourceRisk = { municipal: 1, well: 3, surface: 4, rainwater: 3 };
  const treatRisk = { advanced: 0.5, standard: 1, basic: 3, none: 5 };
  const storageRisk = { sealed: 0.5, covered: 2, open: 4 };
  const usageRisk = { ingredient: 3, processing: 2, nonfood: 1 };
  
  const source = document.getElementById('water-source').value;
  const treatment = document.getElementById('treatment').value;
  const storage = document.getElementById('storage').value;
  const usage = document.getElementById('usage').value;
  
  const score = (sourceRisk[source] + treatRisk[treatment] + storageRisk[storage]) * usageRisk[usage];
  const resultDiv = document.getElementById('result');
  resultDiv.style.display = 'block';
  
  let level, color;
  if (score