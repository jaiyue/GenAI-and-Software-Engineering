def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if -x in seen:
            return True
        seen.add(x)
    return False

This uses a set to check if the negation of any element was seen earlier (handles zero correctly by requiring a second zero).

