def generate_integers(a, b):
    lo, hi = min(a, b), max(a, b)
    return [n for n in range(lo, hi + 1) if 0 <= n <= 9 and n % 2 == 0]

