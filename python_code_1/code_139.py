def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be an integer >= 1")
    result = 1
    fact = 1
    for k in range(1, n + 1):
        fact *= k
        result *= fact
    return result

Explanation: computes successive factorials iteratively (fact) and multiplies them into result.

