# 🤖 Generative AI Tools & Platforms 2025 — EDA + Baseline Modeling

A practical Kaggle/GitHub notebook for exploring a curated 2025 GenAI tools catalog: data quality, category structure, modality coverage, API availability, open-source patterns, and a simple metadata baseline.

[![Python](https://img.shields.io/badge/Python-3.10%E2%80%933.12-blue)](#)
[![Notebook](https://img.shields.io/badge/Format-Jupyter%20Notebook-orange)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## ✨ What this repo provides

- 🔎 **Data audit first** — schema, missingness, duplicates, target balance, and field checks.
- 🧹 **Clean feature handling** — preserves the original `modality_count` and uses a recomputed version from active `mod_*` flags.
- 📊 **Focused EDA** — release years, categories, companies, modality labels, API availability, and open-source patterns.
- 🧠 **Leak-aware baseline modeling** — excludes identifier-like fields such as tool names, companies, websites, and source domains.
- 📈 **Cross-validated comparison** — includes a dummy majority baseline plus simple reusable metadata models.
- 🧾 **Clear interpretation** — treats the model as an exploratory benchmark, not a production classifier.

---

## 📂 Dataset

Expected dataset file:

```text
Generative AI Tools - Platforms 2025.csv
```

The notebook checks common Kaggle paths first, then local paths.

### Kaggle

Attach the dataset to the notebook. The loader searches common `/kaggle/input/...` locations automatically.

### Local / GitHub workflow

Place the CSV here:

```text
data/raw/Generative AI Tools - Platforms 2025.csv
```

The raw data file is intentionally not committed to this repo by default.

---

## 🧱 Notebook workflow

1. **Config and imports**
2. **Data loading**
3. **Initial data audit**
4. **Cleaning and derived features**
5. **Exploratory data analysis**
6. **Leak-aware modeling setup**
7. **Cross-validated baselines**
8. **Hold-out sanity check**
9. **Feature signal check**
10. **Decisions, takeaways, and data dictionary**

---

## 🧪 Modeling approach

The target is:

```text
open_source
```

The baseline uses reusable metadata features such as:

- `category_canonical`
- `modality_canonical`
- `api_status`
- `api_available`
- `release_year`
- `years_since_release_2025`
- recomputed modality flags/counts

Identifier-like fields are excluded from modeling:

- `tool_name`
- `company`
- `website`
- `source_domain`

This keeps the benchmark focused on general metadata signal instead of memorizing specific tools or publishers.

---

## 📁 Repo layout

```text
.
├── generative-ai-tools-platforms-2025-eda-baseline.ipynb
├── data/
│   └── raw/
│       └── .gitkeep
├── artifacts/
│   └── .gitkeep
├── scripts/
│   └── validate_notebook.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── CASE_STUDY.md
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🛠️ Run locally

Create an environment and install dependencies:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Then open and run:

```text
generative-ai-tools-platforms-2025-eda-baseline.ipynb
```

---

## ✅ Static validation

This repo includes a lightweight CI check that validates the notebook JSON and Python syntax of all code cells.

Run locally:

```bash
python scripts/validate_notebook.py generative-ai-tools-platforms-2025-eda-baseline.ipynb
```

The validation is intentionally static; it does not require the dataset file.

---

## 📌 Notes

- The notebook is designed for analysis and benchmarking, not deployment.
- The baseline model is useful for checking whether simple metadata carries signal.
- Dataset-level conclusions stay tied to fields available in the catalog.

---

## 🧾 Case study

See [`CASE_STUDY.md`](CASE_STUDY.md) for the project story, design choices, and interpretation boundaries.

---

## 📜 License

Code is released under the MIT License.  
Dataset usage should follow the license and terms on the dataset page.

---

## 👤 Author

**Tarek Masryo**

## 🔗 Related

- 📂 Generative AI Tools Dataset: https://github.com/tarekmasryo/genai-tools-dataset
