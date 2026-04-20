def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    import math
    if n <= 1:
        raise ValueError("n must be greater than 1")
    # find smallest factor > 1, then the corresponding cofactor is the largest proper divisor
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return n // i
    return 1

