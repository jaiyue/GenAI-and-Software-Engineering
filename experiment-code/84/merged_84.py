def solve(N):
    """Return the sum of decimal digits of N as a binary string."""
    total = sum(int(d) for d in str(N))
    return format(total, "b")

