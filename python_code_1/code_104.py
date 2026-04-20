Here's a concise implementation:

def unique_digits(x):
    """Return a sorted list of elements from x that contain no even digit."""
    return sorted(n for n in x if all(int(d) % 2 == 1 for d in str(n)))

This converts each number to a string and keeps it only if every digit is odd, then returns the results sorted.

