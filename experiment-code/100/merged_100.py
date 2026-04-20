def make_a_pile(n):
    """
    Given a positive integer n, returns a list with n levels starting at n
    and increasing by 2 each level (keeping parity).
    """
    return [n + 2 * i for i in range(n)]

