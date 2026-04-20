Any even integer n can be written as 2+2+2+(n-6), so it's possible exactly when n is even and n >= 8. Here's the implementation:

def is_equal_to_sum_even(n):
    """Return True if n can be written as the sum of exactly 4 positive even numbers."""
    return isinstance(n, int) and n >= 8 and n % 2 == 0

