# 🤖 Generative AI Tools & Platforms 2025 — EDA + Baseline

EDA → baseline classifiers (LogReg, RandomForest, GradBoost) → transparent metrics & confusion matrix.

---

## 🚀 Why this notebook?
- **Kaggle-ready**: clean imports, reproducible random seeds, minimal dependencies.  
- **Clear EDA**: release trends, categories, companies, open vs closed-source, modalities.  
- **Baseline models**: Logistic Regression, RandomForest, GradientBoosting.  
- **Evaluation**: Accuracy, Macro-F1, ROC-AUC, classification report, confusion matrices.  
- **Derived features**: `years_since_release`, `modality_count`.  

---

## 📂 Dataset
- **Source file**: `Generative AI Tools - Platforms 2025.csv`  
- **Rows**: ~110 curated tools/platforms  
- **Columns**:
  - `tool_name` — product / project name  
  - `company` — publisher / developer  
  - `category_canonical` — taxonomy label  
  - `modality_canonical` — delimited modalities (e.g., `Text|Image|Video`)  
  - `open_source` — 0 (closed) / 1 (open)  
  - `api_available` — 0 (no API) / 1 (API available)  
  - `release_year` — first public release year  
  - `years_since_release` — derived (current year − release_year)  
  - `modality_count` — total modalities inferred  

> Default path (Kaggle):  
`/kaggle/input/generative-ai-tools-and-platforms-2025/Generative AI Tools - Platforms 2025.csv`

---

## 🧱 Notebook Outline
1. **Setup & Imports**  
2. **Load & Audit** (shape, dtypes, missing values)  
3. **Cleaning** (trimming, numeric coercion, derived columns)  
4. **EDA — Distributions** (release year, categories, open vs closed, API availability, modality counts)  
5. **EDA — Relationships** (Category × Open Source, API × Open Source, Open-Source Rate by Year)  
6. **EDA — Entities** (Top companies, modalities coverage, correlations)  
7. **Class balance check**  
8. **Baseline Modeling**  
   - Preprocessing (OHE, imputation)  
   - Models: Logistic Regression, RandomForest, GradientBoost  
   - Evaluation (accuracy, macro-F1, ROC-AUC)  
9. **Best model selection** + confusion matrix  
10. **Appendix — Data Dictionary**  

---

## 📈 Results (Holdout Set)

| model          | accuracy | macro_f1 | roc_auc |
|----------------|----------|----------|---------|
| logreg         | **0.609** | **0.596** | 0.663   |
| random_forest  | 0.609    | 0.462    | **0.667** |
| grad_boost     | 0.609    | 0.462    | 0.635   |

**Best model**: Logistic Regression  
- Accuracy: ~0.61  
- Macro-F1: ~0.60  
- ROC-AUC: ~0.66  

Confusion Matrix (LogReg): balanced but still moderate signal → dataset is small and imbalanced.

---

## 🛠️ Environment
- **Python**: 3.10–3.12  
- **Core**: `pandas`, `numpy`, `matplotlib`, `scikit-learn`  

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## ⚡ Quick Start
```bash
git clone https://github.com/tarekmasryo/generative-ai-tools-platforms-2025
cd generative-ai-tools-platforms-2025
jupyter notebook generative_ai_tools_eda_baseline.ipynb
```

- Place `Generative AI Tools - Platforms 2025.csv` under `./data/` if not running on Kaggle.

---

## 🔍 Notes on Methodology
- **No leakage**: encoders fitted on train only.  
- **Derived features** enrich predictive signal.  
- **Models kept simple** for transparency, not SOTA.  
- **Small dataset** → results are baseline-level, not production-ready.  
- **Reproducibility**: `SEED=42`, stratified split.  

---

## 📜 License
MIT (code) — dataset subject to its original license.

---

## 🙌 Credits
Dataset: **Generative AI Tools & Platforms 2025** (curated).  
Author: **Tarek Masryo** · [GitHub](https://github.com/tarekmasryo) · [Kaggle](https://www.kaggle.com/tarekmasryo) · [HuggingFace](https://huggingface.co/TarekMasryo)
