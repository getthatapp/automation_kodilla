import pytest
from zadanie import prime_factors


def test_prime_factors_correct_result():
    assert prime_factors(2) == [2]
    assert prime_factors(4) == [2, 2]
    assert prime_factors(10) == [2, 5]
    assert prime_factors(1) == [1]


def test_prime_factors_raises_exception():
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-1)
