def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # strip factors of 2
    max_pf = 1
    while n % 2 == 0:
        max_pf = 2
        n //= 2
    # test odd factors
    p = 3
    while p * p <= n:
        while n % p == 0:
            max_pf = p
            n //= p
        p += 2
    # if remaining n > 1 it's a prime and the largest factor
    if n > 1:
        max_pf = max(max_pf, n)
    return int(max_pf)

