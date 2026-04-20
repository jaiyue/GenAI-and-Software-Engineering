def rounded_avg(n, m):
    """Compute rounded average of integers from n to m inclusive and return its binary string, or -1 if n>m."""
    if n > m:
        return -1
    avg = (n + m) / 2
    return bin(int(round(avg)))

