Searching the codebase for the function to edit. I'll look for occurrences of decimal_to_binary.

def decimal_to_binary(decimal):
    """Convert a non-negative integer to binary wrapped with 'db' prefix and suffix."""
    if not isinstance(decimal, int):
        raise TypeError("Input must be an integer")
    if decimal < 0:
        raise ValueError("Only non-negative integers are supported")
    if decimal == 0:
        return "db0db"
    bits = []
    while decimal:
        bits.append(str(decimal & 1))
        decimal >>= 1
    return "db" + "".join(reversed(bits)) + "db"

This returns "db" + binary_representation + "db", handles 0, and raises for invalid input.

