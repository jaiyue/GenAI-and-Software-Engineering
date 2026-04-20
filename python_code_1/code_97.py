def multiply(a, b):
    """Return the product of the unit digits of two integers."""
    return (abs(a) % 10) * (abs(b) % 10)

# Examples:
# multiply(148, 412) -> 16
# multiply(14, -15)  -> 20

