# 🧠 Case Study — Generative AI Tools & Platforms 2025

## Problem

The GenAI tooling landscape is broad and fast-moving. A useful catalog needs more than a list of tools; it needs a clear view of structure, coverage, metadata quality, and whether simple fields carry useful signal.

This project turns a curated GenAI tools catalog into a practical analysis workflow that answers:

- What does the dataset contain, and is it internally consistent?
- Which categories, modalities, release years, and API patterns dominate the catalog?
- How does open-source availability vary by category and modality?
- Can simple reusable metadata predict `open_source` without leaking identifiers?

---

## Data

**File**

```text
Generative AI Tools - Platforms 2025.csv
```

**Grain**

One row per AI tool or platform.

**Core fields**

- `tool_name`
- `company`
- `category_canonical`
- `modality_canonical`
- `open_source`
- `api_available`
- `api_status`
- `website`
- `source_domain`
- `release_year`
- `mod_*` modality flags

---

## Key data decision

The notebook preserves the original `modality_count` for audit, then computes a reliable replacement:

```text
modality_count_recomputed
```

This avoids relying on an inconsistent source field and keeps modality-based analysis aligned with the active `mod_*` flags.

---

## Approach

### 1. Data audit

The workflow starts with structural checks:

- Shape and schema
- Missing values
- Duplicate rows
- Duplicate tool names
- Numeric field ranges
- Target balance

### 2. EDA

The notebook then explores:

- Release-year distribution
- Category distribution
- Company/publisher concentration
- Open-source balance
- API availability
- Category-level open-source and API rates
- Primary modality distribution
- Recomputed modality flag counts

### 3. Baseline modeling

The model is intentionally simple and leak-aware.

Excluded identifier-like fields:

- `tool_name`
- `company`
- `website`
- `source_domain`

Used metadata features include:

- categories
- modalities
- API status
- release year
- derived age features
- recomputed modality flags/counts

The comparison includes a dummy majority baseline to make the model lift easier to interpret.

---

## Evaluation

The notebook uses:

- Stratified cross-validation
- Accuracy
- Macro-F1
- ROC-AUC
- Average precision
- Hold-out sanity check
- Confusion matrix
- Permutation importance for directional feature inspection

Macro-F1 is emphasized because open-source classification can be imbalanced, and accuracy alone can overstate performance.

---

## Interpretation

The baseline is an exploratory benchmark. It checks whether catalog metadata carries signal without treating the result as a deployable classifier.

That distinction matters: the dataset is valuable as a structured catalog and analysis asset, while the model is a lightweight way to inspect metadata signal.

---

## Takeaways

- The dataset is suitable for structured EDA and metadata-signal testing.
- The recomputed modality count is safer than the original count field.
- API availability is high in the catalog, so it is not a strong separator by itself.
- Modality flags behave mostly like primary labels, so strong modality co-occurrence claims are avoided.
- Open-source prediction from simple metadata carries some signal, but should be interpreted as exploratory.

---

## Next steps

Good next extensions would be:

- Add more records over time.
- Track source dates and evidence links where available.
- Add richer metadata when reliably sourced.
- Re-run the same notebook after catalog updates to compare distribution shifts.
