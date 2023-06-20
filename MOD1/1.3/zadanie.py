# ITERACJA 1

mport pytest

def test_prime_factors():
    assert prime_factors(2) == [2]
    assert prime_factors(4) == [2, 2]
    assert prime_factors(10) == [2, 5]

with pytest.raises(NameError):
    test_prime_factors()

# ITERACJA 2

def prime_factors(number):
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

test_prime_factors()  # powinno przejść bez błędów

# ITERACJA 3
def test_prime_factors():
    assert prime_factors(1) == [1]
    assert prime_factors(2) == [2]
    assert prime_factors(3) == [3]
    assert prime_factors(4) == [2, 2]
    assert prime_factors(10) == [2, 5]
    assert prime_factors(3958159172) == [2, 2, 11, 2347, 38329]
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-1)

def prime_factors(number):
    if number <= 0:
        raise ValueError("Number must be greater than 0")
    if number == 1:
        return [1]
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

test_prime_factors()  # powinno przejść bez błędów

