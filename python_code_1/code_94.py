Here's a concise implementation that finds the largest prime in the list and returns the sum of its digits (returns 0 if no prime found):

def skjkasdkd(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    maxp = -1
    for x in lst:
        if isinstance(x, int) and is_prime(x) and x > maxp:
            maxp = x
    if maxp == -1:
        return 0
    return sum(int(d) for d in str(abs(maxp)))

This chooses the largest prime >1 and returns the sum of its decimal digits.

