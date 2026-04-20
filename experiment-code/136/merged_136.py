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

