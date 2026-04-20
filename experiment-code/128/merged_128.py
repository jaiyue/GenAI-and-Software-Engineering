def prod_signs(arr):
    if not arr:
        return None
    total = sum(abs(x) for x in arr)
    prod = 1
    for x in arr:
        if x == 0:
            return 0
        prod *= 1 if x > 0 else -1
    return total * prod

