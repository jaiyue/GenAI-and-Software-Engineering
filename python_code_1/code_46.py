def fib4(n: int):
    """The Fib4 number sequence defined in the docstring. Non-recursive implementation."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    a, b, c, d = 0, 0, 2, 0  # fib4(0), fib4(1), fib4(2), fib4(3)
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    return d

# Iterative O(n) time, O(1) space.

