def unique_digits(x):
    """Return a sorted list of elements from x that contain no even digit."""
    return sorted(n for n in x if all(int(d) % 2 == 1 for d in str(n)))

