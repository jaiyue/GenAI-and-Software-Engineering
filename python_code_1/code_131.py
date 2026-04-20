def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    prod = 1
    found_odd = False
    for ch in str(n):
        d = int(ch)
        if d % 2 == 1:
            prod *= d
            found_odd = True
    return prod if found_odd else 0

This iterates the digits, multiplies the odd ones, and returns 0 if no odd digits were found.

