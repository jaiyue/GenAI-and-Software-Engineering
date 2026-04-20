def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple (even_count, odd_count) of integer
    palindromes in the range 1..n (inclusive).
    """
    even = odd = 0
    for i in range(1, n + 1):
        s = str(i)
        if s == s[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)

# Examples:
# even_odd_palindrome(3) -> (1, 2)
# even_odd_palindrome(12) -> (4, 6)

