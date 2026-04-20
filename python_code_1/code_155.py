Implementation below:

def even_odd_count(num):
    """Given an integer, return (number_of_even_digits, number_of_odd_digits)."""
    s = str(abs(int(num)))
    even = sum(1 for ch in s if int(ch) % 2 == 0)
    odd = len(s) - even
    return (even, odd)

