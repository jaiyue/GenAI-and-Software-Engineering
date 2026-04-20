def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    x = n
    odds = set()
    while True:
        if x % 2 == 1:
            odds.add(x)
        if x == 1:
            break
        x = x // 2 if x % 2 == 0 else 3 * x + 1
    return sorted(odds)

