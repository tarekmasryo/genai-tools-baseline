# 🤖 Generative AI Tools & Platforms 2025 — EDA + Baseline

EDA → baseline classifiers → transparent metrics & confusion matrix.

[![Python](https://img.shields.io/badge/Python-3.10%E2%80%933.12-blue)](#)
[![Notebook](https://img.shields.io/badge/Format-Jupyter%20Notebook-orange)](#)

---

## 🚀 Why this notebook?

- **Clear EDA**: release trends, categories, companies, open vs closed-source, modalities  
- **Baseline models**: Logistic Regression, RandomForest, HistGradientBoosting  
- **Evaluation**: Accuracy, Macro-F1, ROC-AUC, classification report, confusion matrix  
- **Derived features**: `years_since_release`, `modality_count`  
- **Reproducible**: fixed seed + stratified split, lightweight dependencies

---

## 📂 Dataset

- **Source file**: `Generative AI Tools - Platforms 2025.csv`
- **Rows**: ~110 curated tools/platforms
- **Target**: `open_source` (0/1)

Columns (high level):
- `tool_name`, `company`
- `category_canonical`, `modality_canonical`
- `api_available`, `open_source`, `release_year`

**Local (recommended):**
- Put the CSV under: `data/raw/`

**Kaggle:**
- The notebook falls back to `/kaggle/input/...` automatically  
- Typical Kaggle path:
  `/kaggle/input/generative-ai-tools-and-platforms-2025/Generative AI Tools - Platforms 2025.csv`

---

## 🧱 Notebook outline

1. Setup & Imports  
2. Load & Audit (shape, dtypes, missing values)  
3. Cleaning + derived columns  
4. EDA (distributions + relationships + entities)  
5. Baseline modeling (preprocess + train + compare)  
6. Best baseline + confusion matrix  

---

## 📈 Results (holdout)

| model         | accuracy | macro_f1 | roc_auc |
|---------------|----------|----------|---------|
| logreg        | **0.609** | **0.596** | 0.663 |
| random_forest | 0.609    | 0.462    | **0.667** |
| hgb           | 0.609    | 0.462    | 0.635 |

**Best baseline**: Logistic Regression  
Small dataset → treat these as **baseline-level** signals, not production performance.

---

## 🔍 Notes on methodology

- **No leakage**: encoders are fit on train only  
- **Derived features** enrich predictive signal  
- **Models stay simple** for transparency, not SOTA  
- **Small dataset** → results are a benchmark, not a final conclusion  
- **Reproducibility**: `SEED=42`, stratified split  

---

## 📁 Repo layout

```text
.
├── generative-ai-tools-platforms-2025-eda-m.ipynb
├── data/
│   └── raw/               # local dataset file goes here
├── artifacts/             # saved outputs (kept out of git by default)
├── repo_utils/
│   └── pathing.py         # local + Kaggle path helper
├── CASE_STUDY.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🛠️ Environment

Install dependencies:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Open the notebook and run top-to-bottom (Jupyter / VS Code).

**Optional:** set a full path via environment variable:
- `DATA_PATH=/full/path/to/Generative AI Tools - Platforms 2025.csv`

---

## 🧾 Case study

See **CASE_STUDY.md** (project story + decisions, without repeated run steps).

---

## 📜 License

MIT (code). Dataset remains subject to its original license.

---

## 🙌 Credits

Dataset: **Generative AI Tools & Platforms 2025** (curated)  
Author: **Tarek Masryo**

## Related repositories
- 📂 Generative AI Tools Dataset: https://github.com/tarekmasryo/genai-tools-dataset
