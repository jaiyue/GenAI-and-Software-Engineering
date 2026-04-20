def count_up_to(n):
    """Return a list of prime numbers less than n (n is a non-negative integer)."""
    if n <= 2:
        return []
    sieve = [True] * n
    sieve[0:2] = [False, False]  # 0 and 1 are not prime
    p = 2
    import math
    limit = int(math.sqrt(n - 1)) + 1
    while p <= limit:
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n:step] = [False] * (((n - 1) - start) // step + 1)
        p += 1
    return [i for i in range(2, n) if sieve[i]]

