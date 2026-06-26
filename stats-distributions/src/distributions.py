"""
Core probability distribution implementations.

All distributions are implemented from scratch using NumPy only.
Each is validated against scipy.stats in the corresponding test file.
"""

import numpy as np


# ---------------------------------------------------------------------------
# Discrete Distributions
# ---------------------------------------------------------------------------

def bernoulli_pmf(x: np.ndarray, p: float) -> np.ndarray:
    """
    Bernoulli PMF: P(X = x) = p^x * (1-p)^(1-x), x ∈ {0, 1}

    Parameters
    ----------
    x : array-like of int
        Values in {0, 1}
    p : float
        Success probability, 0 < p < 1
    """
    x = np.asarray(x)
    return np.where(x == 1, p, 1 - p)


def binomial_pmf(x: np.ndarray, n: int, p: float) -> np.ndarray:
    """
    Binomial PMF: P(X = x) = C(n,x) * p^x * (1-p)^(n-x)

    Parameters
    ----------
    x : array-like of int
        Number of successes, 0 ≤ x ≤ n
    n : int
        Number of trials
    p : float
        Success probability per trial
    """
    from math import comb
    x = np.asarray(x)
    coeffs = np.array([comb(n, int(k)) for k in x.ravel()]).reshape(x.shape)
    return coeffs * (p ** x) * ((1 - p) ** (n - x))


def poisson_pmf(x: np.ndarray, lam: float) -> np.ndarray:
    """
    Poisson PMF: P(X = x) = e^(-λ) * λ^x / x!

    Parameters
    ----------
    x : array-like of int
        Non-negative integers
    lam : float
        Rate parameter λ > 0
    """
    from math import factorial
    x = np.asarray(x)
    facts = np.array([factorial(int(k)) for k in x.ravel()]).reshape(x.shape)
    return np.exp(-lam) * (lam ** x) / facts


# ---------------------------------------------------------------------------
# Continuous Distributions
# ---------------------------------------------------------------------------

def normal_pdf(x: np.ndarray, mu: float = 0.0, sigma: float = 1.0) -> np.ndarray:
    """
    Normal PDF: f(x) = (1 / (σ√(2π))) * exp(-½ ((x-μ)/σ)²)

    Parameters
    ----------
    x : array-like
        Real values
    mu : float
        Mean μ
    sigma : float
        Standard deviation σ > 0
    """
    x = np.asarray(x, dtype=float)
    z = (x - mu) / sigma
    return np.exp(-0.5 * z ** 2) / (sigma * np.sqrt(2 * np.pi))


def normal_cdf(x: np.ndarray, mu: float = 0.0, sigma: float = 1.0) -> np.ndarray:
    """
    Normal CDF: F(x) = Φ((x-μ)/σ), where Φ is the standard normal CDF.

    Uses scipy.special.erf for numerical stability.
    """
    from scipy.special import erf
    x = np.asarray(x, dtype=float)
    z = (x - mu) / (sigma * np.sqrt(2))
    return 0.5 * (1 + erf(z))


def exponential_pdf(x: np.ndarray, lam: float = 1.0) -> np.ndarray:
    """
    Exponential PDF: f(x) = λ * exp(-λx), x ≥ 0

    Parameters
    ----------
    x : array-like
        Non-negative real values
    lam : float
        Rate parameter λ > 0 (mean = 1/λ)
    """
    x = np.asarray(x, dtype=float)
    return np.where(x >= 0, lam * np.exp(-lam * x), 0.0)


def uniform_pdf(x: np.ndarray, a: float = 0.0, b: float = 1.0) -> np.ndarray:
    """
    Uniform PDF: f(x) = 1/(b-a) for x ∈ [a, b], else 0.

    Parameters
    ----------
    x : array-like
    a, b : float
        Lower and upper bounds, a < b
    """
    x = np.asarray(x, dtype=float)
    return np.where((x >= a) & (x <= b), 1.0 / (b - a), 0.0)
