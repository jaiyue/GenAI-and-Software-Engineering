Searching the repository for any triangle_area definition so it can be updated to return the correct area (0.5 * a * h). Running a code search now.

Replace the body with the standard formula (base * height / 2):

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 2.0

