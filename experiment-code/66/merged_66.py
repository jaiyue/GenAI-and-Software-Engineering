def digitSum(s):
    """Return the sum of ASCII codes for uppercase letters in s."""
    return sum(ord(c) for c in s if 'A' <= c <= 'Z')

