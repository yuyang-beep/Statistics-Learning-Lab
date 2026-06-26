"""
Tests for stats-distributions/src/distributions.py

Each function is tested for:
1. Mathematical properties (integrate to 1, symmetry, etc.)
2. Agreement with scipy.stats reference implementation
"""

import numpy as np
import pytest
from scipy import stats

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from distributions import (
    bernoulli_pmf, binomial_pmf, poisson_pmf,
    normal_pdf, normal_cdf, exponential_pdf, uniform_pdf,
)


class TestBernoulliPMF:
    def test_p_at_one(self):
        assert bernoulli_pmf(1, p=0.3) == pytest.approx(0.3)

    def test_p_at_zero(self):
        assert bernoulli_pmf(0, p=0.3) == pytest.approx(0.7)

    def test_sums_to_one(self):
        assert bernoulli_pmf(0, 0.6) + bernoulli_pmf(1, 0.6) == pytest.approx(1.0)

    def test_matches_scipy(self):
        x = np.array([0, 1])
        np.testing.assert_allclose(bernoulli_pmf(x, 0.4), stats.bernoulli.pmf(x, 0.4))


class TestBinomialPMF:
    def test_known_value(self):
        # P(X=2 | n=4, p=0.5) = C(4,2) * 0.5^4 = 6/16 = 0.375
        assert binomial_pmf(2, n=4, p=0.5) == pytest.approx(0.375)

    def test_sums_to_one(self):
        n = 10
        x = np.arange(n + 1)
        assert binomial_pmf(x, n=n, p=0.3).sum() == pytest.approx(1.0, abs=1e-10)

    def test_matches_scipy(self):
        x = np.arange(11)
        np.testing.assert_allclose(
            binomial_pmf(x, n=10, p=0.4),
            stats.binom.pmf(x, n=10, p=0.4),
            rtol=1e-10,
        )


class TestPoissonPMF:
    def test_known_value(self):
        # P(X=0 | λ=1) = e^-1 ≈ 0.3679
        assert poisson_pmf(0, lam=1.0) == pytest.approx(np.exp(-1))

    def test_sums_to_one(self):
        x = np.arange(50)
        assert poisson_pmf(x, lam=3.0).sum() == pytest.approx(1.0, abs=1e-6)

    def test_matches_scipy(self):
        x = np.arange(20)
        np.testing.assert_allclose(
            poisson_pmf(x, lam=5.0),
            stats.poisson.pmf(x, mu=5.0),
            rtol=1e-10,
        )


class TestNormalPDF:
    def test_peak_at_mean(self):
        # Peak of standard normal = 1/√(2π)
        assert normal_pdf(0.0) == pytest.approx(1 / np.sqrt(2 * np.pi))

    def test_integrates_to_one(self):
        x = np.linspace(-10, 10, 10_000)
        assert np.trapz(normal_pdf(x), x) == pytest.approx(1.0, abs=1e-5)

    def test_symmetric(self):
        x = np.array([-2.0, -1.0, 1.0, 2.0])
        pdf = normal_pdf(x)
        np.testing.assert_allclose(pdf[0], pdf[3], rtol=1e-12)
        np.testing.assert_allclose(pdf[1], pdf[2], rtol=1e-12)

    def test_matches_scipy(self):
        x = np.linspace(-5, 5, 200)
        np.testing.assert_allclose(normal_pdf(x, 2, 3), stats.norm.pdf(x, 2, 3), rtol=1e-12)


class TestNormalCDF:
    def test_at_mean(self):
        assert normal_cdf(0.0) == pytest.approx(0.5)

    def test_symmetry(self):
        assert normal_cdf(-1.0) == pytest.approx(1 - normal_cdf(1.0), rel=1e-12)

    def test_matches_scipy(self):
        x = np.linspace(-4, 4, 100)
        np.testing.assert_allclose(normal_cdf(x), stats.norm.cdf(x), rtol=1e-12)


class TestExponentialPDF:
    def test_at_zero(self):
        assert exponential_pdf(0.0, lam=2.0) == pytest.approx(2.0)

    def test_negative_is_zero(self):
        assert exponential_pdf(-1.0, lam=1.0) == 0.0

    def test_integrates_to_one(self):
        x = np.linspace(0, 30, 10_000)
        assert np.trapz(exponential_pdf(x, lam=1.0), x) == pytest.approx(1.0, abs=1e-4)

    def test_matches_scipy(self):
        x = np.linspace(0, 10, 100)
        np.testing.assert_allclose(
            exponential_pdf(x, lam=2.0),
            stats.expon.pdf(x, scale=0.5),
            rtol=1e-12,
        )


class TestUniformPDF:
    def test_within_support(self):
        assert uniform_pdf(0.5, a=0, b=1) == pytest.approx(1.0)

    def test_outside_support(self):
        assert uniform_pdf(2.0, a=0, b=1) == 0.0

    def test_integrates_to_one(self):
        x = np.linspace(0, 1, 10_000)
        assert np.trapz(uniform_pdf(x), x) == pytest.approx(1.0, abs=1e-4)
