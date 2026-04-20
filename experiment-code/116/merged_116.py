def sort_array(arr):
    """
    Sort array by number of ones in binary representation (ascending).
    For equal number of ones, sort by decimal value.
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

