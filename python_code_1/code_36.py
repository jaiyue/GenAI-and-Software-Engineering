def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(str(i).count('7') for i in range(max(0, n)) if i % 11 == 0 or i % 13 == 0)

This counts '7' occurrences in each integer < n that is divisible by 11 or 13.

