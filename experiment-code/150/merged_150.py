def x_or_y(n, x, y):
    """Return x if n is prime, otherwise return y."""
    if not isinstance(n, int) or n < 2:
        return y
    if n in (2, 3):
        return x
    if n % 2 == 0:
        return y
    import math
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return y
    return x

