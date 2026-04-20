def sort_third(l: list):
    """Return a new list where elements at indices divisible by three are sorted in ascending order,
    other elements remain in their original positions."""
    thirds = [l[i] for i in range(len(l)) if i % 3 == 0]
    thirds.sort()
    res = l.copy()
    it = iter(thirds)
    for i in range(len(res)):
        if i % 3 == 0:
            res[i] = next(it)
    return res
