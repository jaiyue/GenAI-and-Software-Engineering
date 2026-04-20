def is_multiply_prime(a):
    if a < 2:
        return False
    count = 0
    n = a
    p = 2
    while p * p <= n:
        while n % p == 0:
            count += 1
            n //= p
            if count > 3:
                return False
        p += 1 if p == 2 else 2
    if n > 1:
        count += 1
    return count == 3

