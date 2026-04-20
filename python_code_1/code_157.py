Searching the repository for the function definition to implement. Running quick code search for "def right_angle_triangle".

def right_angle_triangle(a, b, c):
    sides = sorted([a, b, c])
    x, y, z = sides
    if x <= 0:
        return False
    return abs(z*z - (x*x + y*y)) < 1e-9

Sorts sides, checks positivity, and compares squares with a small tolerance to account for floating-point inputs.

