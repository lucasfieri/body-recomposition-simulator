# 💪 Body Recomposition Simulator

An interactive, evidence-based body composition simulator built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/python/). It projects changes in weight, fat mass, lean mass, and body fat percentage over time — using peer-reviewed physiological models instead of simplistic "3500 kcal = 1 lb" assumptions.

> **Try it live:** [body-recomposition-simulator.streamlit.app](https://body-recomposition-simulator.streamlit.app)

## Features

- **Three scenario modes** — Cut, Recomp, and Bulk — each with independent macro and calorie configurations
- **Evidence-based engine** — Mifflin-St Jeor + Katch-McArdle BMR, Forbes non-linear P-ratio, adaptive thermogenesis, and Aragon muscle gain ceilings
- **Carb cycling** — redistribute carb calories across high/low days while preserving weekly averages
- **AI body fat estimation** — optional HuggingFace MLP model for body fat prediction from anthropometric measurements
- **Interactive Plotly charts** — weight evolution, body composition breakdown, BF% gauge, muscle gain rate, and macro split
- **Bilingual UI** — English and Portuguese with automatic browser language detection
- **Dynamic glycogen model** — smooth exponential transitions instead of static resets

## Project Structure

```text
├── app.py                  # Streamlit entry point
├── pyproject.toml           # Project metadata and dependencies
├── .streamlit/
│   └── config.toml          # Streamlit deployment configuration
├── src/
│   ├── model.py             # Physiological simulation engine
│   ├── charts.py            # Plotly chart builders
│   ├── ui.py                # Sidebar and scenario panel UI components
│   ├── hf_bodyfat.py        # HuggingFace body fat estimation panel
│   ├── i18n.py              # Internationalization (en/pt)
│   ├── references.py        # Scientific references accordion
│   └── utils.py             # Date and helper utilities
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

## Scientific Evidence

The simulator is grounded in the following peer-reviewed research:

| Model | Formula | Reference |
| ------- | --------- | ----------- |
| **Mifflin-St Jeor** | BMR = 10w + 6.25h − 5a + 5 (male) | Mifflin et al. (1990). *Am J Clin Nutr*, 51(2), 241–247. [doi:10.1093/ajcn/51.2.241](https://doi.org/10.1093/ajcn/51.2.241) |
| **Katch-McArdle** | BMR = 370 + 21.6 × LBM | McArdle, Katch & Katch (2010). *Exercise Physiology* (7th ed.). Lippincott Williams & Wilkins. |
| **Deurenberg BF%** | BF% = 1.20 × BMI + 0.23 × age − 10.8 × sex − 5.4 | Deurenberg et al. (1991). *Br J Nutr*, 65(2), 105–114. [doi:10.1079/BJN19910073](https://doi.org/10.1079/BJN19910073) |
| **Adaptive Thermogenesis** | 5–15% TDEE reduction during sustained deficit | Trexler et al. (2014). *JISSN*, 11, 7. [doi:10.1186/1550-2783-11-7](https://doi.org/10.1186/1550-2783-11-7) |
| **Aragon Muscle Ceiling** | Beginner 1–1.5%, Intermediate 0.5–1%, Advanced 0.25–0.5% BW/month | Aragon & Schoenfeld (2020). *Strength Cond J*, 42(5), 79–86. [doi:10.1519/SSC.0000000000000539](https://doi.org/10.1519/SSC.0000000000000539) |
| **Forbes P-Ratio** | P_fat = FM / (FM + 10.4) — non-linear fat/lean partitioning | Forbes (1987). *Nutr Rev*, 45(8), 225–231. [doi:10.1111/j.1753-4887.1987.tb07489.x](https://doi.org/10.1111/j.1753-4887.1987.tb07489.x) |
| **TEF** | Protein ~25%, Carbs ~7%, Fat ~3% of intake | Westerterp (2004). *Nutr Metab*, 1, 5. [doi:10.1186/1743-7075-1-5](https://doi.org/10.1186/1743-7075-1-5) |
| **ISSN Protein** | 1.4–2.0 g/kg/day for active individuals | Jäger et al. (2017). *JISSN*, 14, 20. [doi:10.1186/s12970-017-0177-8](https://doi.org/10.1186/s12970-017-0177-8) |
| **HuggingFace MLP** | Body fat from anthropometric measurements (R² ≈ 0.97) | [ChanMeng666/bodyfat-estimation-mlp](https://huggingface.co/ChanMeng666/bodyfat-estimation-mlp) |

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/lucasfieri/body-recomposition-simulator.git
cd body-recomposition-simulator

# Install dependencies
uv sync

# (Optional) Install AI body fat estimation
uv sync --extra ai
```

### Running

```bash
uv run streamlit run app.py
```

The app will open at `http://localhost:8501`.

## Tech Stack

- **[Streamlit](https://streamlit.io/)** — interactive web UI
- **[Plotly](https://plotly.com/python/)** — charts and gauges
- **[NumPy](https://numpy.org/)** — numerical simulation
- **[Pandas](https://pandas.pydata.org/)** — time-series data
- **[TensorFlow](https://www.tensorflow.org/)** + **[HuggingFace Hub](https://huggingface.co/)** — optional AI body fat estimation

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is open source. See [LICENSE](LICENSE) for details.
