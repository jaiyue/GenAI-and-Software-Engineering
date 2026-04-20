def cycpattern_check(a, b):
    if not b:
        return True
    if len(b) > len(a):
        return False
    for i in range(len(b)):
        rot = b[i:] + b[:i]
        if rot in a:
            return True
    return False

