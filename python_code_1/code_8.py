def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    total = 0
    prod = 1
    for n in numbers:
        total += n
        prod *= n
    return total, prod

This iterates once over the list, returning 0 and 1 for an empty list as required.

