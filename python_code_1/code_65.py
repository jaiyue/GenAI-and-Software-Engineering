def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    sign = ''
    if s.startswith('-'):
        sign = '-'
        s = s[1:]
    n = len(s)
    if n == 0:
        return sign + s
    if shift > n:
        return sign + s[::-1]
    shift = shift % n
    if shift == 0:
        return sign + s
    return sign + s[-shift:] + s[:-shift]

