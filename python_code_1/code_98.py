def count_upper(s):
    """Return the number of uppercase vowels (A,E,I,O,U) found at even indices (0-based)."""
    vowels = set("AEIOU")
    return sum(1 for i in range(0, len(s), 2) if s[i] in vowels)

# Examples:
# count_upper('aBCdEf') -> 1
# count_upper('abcdefg') -> 0
# count_upper('dBBE') -> 0

