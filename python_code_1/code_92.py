Here's a simple implementation that requires all three values to be of type int and checks whether any one equals the sum of the other two:

def any_int(x, y, z):
    """
    Returns True if all inputs are integers and one of them equals the sum of the other two.
    """
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return x == y + z or y == x + z or z == x + y

This returns the expected results for the examples provided.

