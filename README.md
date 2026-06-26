# Statistics-Learning-Lab

A progressive portfolio of statistical learning, implementation, and financial modeling.

Built as part of **MindOS** — an AI-Native Cognitive Operating System for lifelong learning.

---

## Structure

| Module | Course | Description |
|--------|--------|-------------|
| [`stats-distributions/`](stats-distributions/) | Statistical Distribution Theory | Probability distributions implemented from scratch |
| [`stats-methods/`](stats-methods/) | Introduction to Statistical Methods | Estimation, hypothesis testing, bootstrap |
| [`econometrics/`](econometrics/) | Econometrics | OLS, IV, discrete choice, time series |
| [`financial-math/`](financial-math/) | Financial Mathematics | GBM, Black-Scholes, portfolio optimization |
| [`capstone/`](capstone/) | All courses | Financial Statistical Analysis Platform |

---

## Capstone: Financial Statistical Analysis Platform

One evolving project that grows with every course:

- **Distribution Explorer** — fit and visualize probability distributions on real financial data
- **Inference Lab** — hypothesis tests, confidence intervals, bootstrap methods
- **Regression Studio** — OLS, IV, ARIMA, Fama-French factor models
- **Financial Toolkit** — VaR, CVaR, Black-Scholes, portfolio optimization
- **Visualization Dashboard** — publication-quality statistical visualizations

---

## Tech Stack

Python 3.11 · NumPy · Matplotlib · Pandas · SciPy · Statsmodels · Scikit-learn

---

## Setup

```bash
conda env create -f environment.yml
conda activate mindos
pytest -v
```

---

## Commit Convention

Every commit follows a three-section format:

```
Short description

Learning objective: what concept this advances
Implementation: what was built or modified
Reflection: what was learned; what to improve
```
