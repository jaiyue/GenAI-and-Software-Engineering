def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

Uses an iterative O(n) time, O(1) space approach and raises on non-positive input.

