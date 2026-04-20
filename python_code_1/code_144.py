def simplify(x, n):
    a, b = map(int, x.split('/'))
    c, d = map(int, n.split('/'))
    return (a * c) % (b * d) == 0

This parses the fractions, multiplies numerators and denominators, and returns True iff the product is an integer.

