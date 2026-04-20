from typing import List
import math

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n == 0:
        return [0]
    if n == 1:
        return []
    factors: List[int] = []
    if n < 0:
        factors.append(-1)
        n = -n
    # factor out 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # factor odd numbers
    f = 3
    max_f = int(math.isqrt(n)) + 1
    while f <= max_f and n > 1:
        while n % f == 0:
            factors.append(f)
            n //= f
            max_f = int(math.isqrt(n)) + 1
        f += 2
    if n > 1:
        factors.append(n)
    return factors

