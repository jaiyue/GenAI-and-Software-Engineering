import math
def max_fill(grid, capacity):
    return sum((sum(row) + capacity - 1) // capacity for row in grid)

