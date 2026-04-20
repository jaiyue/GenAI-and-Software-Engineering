def largest_smallest_integers(lst):
    """
    Return (largest_negative, smallest_positive) from lst; use None if absent.
    """
    max_neg = None
    min_pos = None
    for x in lst:
        if x < 0:
            if max_neg is None or x > max_neg:
                max_neg = x
        elif x > 0:
            if min_pos is None or x < min_pos:
                min_pos = x
    return (max_neg, min_pos)

# Examples:
# largest_smallest_integers([2, 4, 1, 3, 5, 7]) -> (None, 1)
# largest_smallest_integers([]) -> (None, None)
# largest_smallest_integers([0]) -> (None, None)

