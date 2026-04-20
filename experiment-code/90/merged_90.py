def next_smallest(lst):
    """Return the 2nd smallest distinct element or None if it doesn't exist."""
    uniq = sorted(set(lst))
    return uniq[1] if len(uniq) >= 2 else None

