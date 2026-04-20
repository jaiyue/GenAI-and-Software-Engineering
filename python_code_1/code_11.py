def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Pad to equal length (left) then XOR bitwise
    L = max(len(a), len(b))
    a, b = a.zfill(L), b.zfill(L)
    return ''.join('1' if xa != xb else '0' for xa, xb in zip(a, b))

