def solve(s):
    # If there is at least one letter, toggle case for letters and keep others unchanged.
    if any(ch.isalpha() for ch in s):
        return ''.join(ch.swapcase() if ch.isalpha() else ch for ch in s)
    # If there are no letters, return the reversed string.
    return s[::-1]
