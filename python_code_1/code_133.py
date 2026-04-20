import math

def sum_squares(lst):
    return sum((math.ceil(x))**2 for x in lst)

This rounds each element up with math.ceil and returns the sum of their squares.

