def sort_even(l: list):
    evens = sorted(l[0::2])
    res = l.copy()
    for i, v in enumerate(evens):
        res[2*i] = v
    return res

