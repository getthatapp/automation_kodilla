import pytest
from zadanie import prime_factors


# ITERACJA 1
def test_prime_factors():
    assert prime_factors(2) == [2]
    assert prime_factors(4) == [2, 2]
    assert prime_factors(10) == [2, 5]

# ITERACJA 2

    assert prime_factors(1) == [1]

    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-1)
