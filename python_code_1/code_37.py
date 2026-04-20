Here's a simple implementation that sorts values at even indices (0-based) and leaves odd indices unchanged:

def sort_even(l: list):
    evens = sorted(l[0::2])
    res = l.copy()
    for i, v in enumerate(evens):
        res[2*i] = v
    return res

This returns a new list with even-indexed elements sorted while odd-indexed elements remain in their original positions.

