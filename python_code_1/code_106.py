def f(n):
    import math
    res = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            res.append(math.factorial(i))
        else:
            res.append(i * (i + 1) // 2)
    return res

