def exchange(lst1, lst2):
    """Return "YES" if by exchanging elements between lst1 and lst2 (any number of swaps)
    it's possible to make all elements of lst1 even, otherwise "NO"."""
    odd_in_lst1 = sum(1 for x in lst1 if x % 2 != 0)
    even_in_lst2 = sum(1 for x in lst2 if x % 2 == 0)
    return "YES" if even_in_lst2 >= odd_in_lst1 else "NO"

