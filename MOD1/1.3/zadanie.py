def prime_factors(number):
    if number <= 0:
        raise ValueError('Number must be greater than 0')
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
