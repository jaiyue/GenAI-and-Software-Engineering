import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    def f(x): return poly(xs, x)

    # try to find an interval [a,b] with opposite signs (odd-degree guarantees existence)
    a, b = -1.0, 1.0
    fa, fb = f(a), f(b)
    if fa == 0:
        return a
    if fb == 0:
        return b

    for _ in range(100):
        if fa * fb < 0:
            break
        a *= 2.0
        b *= 2.0
        fa, fb = f(a), f(b)
        if fa == 0:
            return a
        if fb == 0:
            return b

    # fallback: wide symmetric search if above didn't find sign change
    if fa * fb > 0:
        a, b = -1.0, 1.0
        for i in range(1, 101):
            a, b = - (2.0 ** i), 2.0 ** i
            fa, fb = f(a), f(b)
            if fa == 0:
                return a
            if fb == 0:
                return b
            if fa * fb < 0:
                break

    # bisection method on [a,b]
    for _ in range(200):
        m = 0.5 * (a + b)
        fm = f(m)
        if abs(fm) < 1e-14:
            return m
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm

    # last resort: Newton-Raphson starting at midpoint
    x = 0.5 * (a + b)
    for _ in range(200):
        fx = f(x)
        if abs(fx) < 1e-14:
            return x
        # derivative
        d = 0.0
        for i, coeff in enumerate(xs):
            if i == 0:
                continue
            d += i * coeff * math.pow(x, i - 1)
        if d == 0:
            break
        x -= fx / d
    return float(x)

