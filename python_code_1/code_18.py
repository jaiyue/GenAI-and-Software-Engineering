def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases. """
    if not substring:
        return 0
    sub_len = len(substring)
    return sum(1 for i in range(len(string) - sub_len + 1) if string[i:i+sub_len] == substring)

This returns 0 for an empty substring and counts overlapping matches.

