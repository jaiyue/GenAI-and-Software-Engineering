def reverse_delete(s, c):
    """Delete from s all characters present in c, then return (result, is_palindrome)."""
    remove = set(c)
    res = ''.join(ch for ch in s if ch not in remove)
    return res, res == res[::-1]

# Examples:
# reverse_delete("abcde", "ae") -> ('bcd', False)
# reverse_delete("abcdedcba", "ab") -> ('cdedc', True)

This removes every character from s that appears in c and checks palindrome by comparing the result to its reverse.

