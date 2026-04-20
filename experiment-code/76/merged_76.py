def is_simple_power(x, n):
    if x == 1:
        return True
    if n == 1:
        return False
    if n == 0:
        return x == 0
    if n == -1:
        return x in (1, -1)
    if x == 0:
        return n == 0

    # For other n, repeatedly divide while divisible
    while x % n == 0:
        x //= n
    return x == 1
