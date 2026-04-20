def iscube(a):
    """
    Return True if integer a is a perfect cube.
    """
    if a == 0:
        return True
    sign = 1 if a > 0 else -1
    n = int(round(abs(a) ** (1/3)))
    for candidate in (n-1, n, n+1):
        if candidate >= 0 and (sign * candidate) ** 3 == a:
            return True
    return False

Explanation: computes the integer cube-root estimate and checks nearby integers to avoid floating-point rounding issues.

