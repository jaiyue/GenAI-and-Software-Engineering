def compare_one(a, b):
    import math
    def to_num(x):
        if isinstance(x, str):
            s = x.strip().replace(',', '.')
            return float(s)
        if isinstance(x, (int, float)):
            return float(x)
        raise TypeError("Unsupported type")
    na, nb = to_num(a), to_num(b)
    if math.isclose(na, nb, rel_tol=1e-9, abs_tol=1e-12):
        return None
    return a if na > nb else b

