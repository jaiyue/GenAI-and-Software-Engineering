def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing."""
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))

