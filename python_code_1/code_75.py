Here's a simple implementation — it returns True when the integer's prime factorization has exactly three primes (counting multiplicity):

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

Example: is_multiply_prime(30) -> True (2*3*5), is_multiply_prime(12) -> True (2*2*3).

