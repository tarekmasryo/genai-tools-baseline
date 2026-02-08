# 🧠 Case Study — Generative AI Tools & Platforms 2025 (EDA + Baseline)

## Problem
Build a clear, reproducible baseline that answers:

- What patterns show up across **GenAI tools/platforms** (release trends, categories, modalities)?
- Can we predict whether a tool is **open-source** using only the available metadata?

**Output:** EDA insights + a simple classifier comparison with transparent metrics.

---

## Data
- **File:** `Generative AI Tools - Platforms 2025.csv`
- **Grain:** one row per tool/platform
- **Target:** `open_source` (0/1)

Key fields used:
- `release_year`, `category_canonical`, `modality_canonical`, `api_available`, `company`

Feature engineering:
- `years_since_release` (reference year fixed for reproducibility)
- `modality_count` (parsed from the modality list)

---

## Approach
EDA focus:
- Category mix and release-year distribution
- Open vs closed-source rate and how it changes across time
- Company concentration (who appears most)
- Modality coverage (Text/Image/Video/Audio, etc.)

Modeling:
- Train/holdout split with stratification (small dataset)
- Simple preprocessing (impute + one-hot encode categorical)
- Baselines compared:
  - Logistic Regression
  - Random Forest
  - HistGradientBoosting

Evaluation:
- Accuracy, Macro-F1 (handles imbalance better than accuracy alone)
- ROC-AUC (probability ranking quality)
- Confusion matrix for the selected baseline

---

## Results (baseline-level)
The best baseline in this notebook is **Logistic Regression**, with moderate signal.

Interpretation:
- Dataset is small → variance is high, confidence is limited.
- Metrics are useful as a **starting point**, not a “final model”.

---

## Decisions & Takeaways
- Keep models simple and explainable first (baseline before “SOTA”).
- Treat results as a reference benchmark; prioritize data enrichment if higher accuracy is needed.
- Use stratification and Macro-F1 to reduce misleading wins from class imbalance.

---

## Next Steps
- Add more rows/tools (coverage improves both EDA and modeling stability).
- Add richer features (pricing tier, region, funding stage, integrations, user count).
- Evaluate calibration + thresholding if the output is used for a decision workflow.
