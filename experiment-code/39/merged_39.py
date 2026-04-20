import math

def prime_fib(n: int) -> int:
    """
    prime_fib returns the n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x in (2, 3):
            return True
        if x % 2 == 0:
            return False
        r = math.isqrt(x)
        for i in range(3, r + 1, 2):
            if x % i == 0:
                return False
        return True

    a, b = 0, 1
    found = 0
    while True:
        a, b = b, a + b
        if a > 1 and is_prime(a):
            found += 1
            if found == n:
                return a

