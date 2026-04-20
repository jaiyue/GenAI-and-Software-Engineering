def max_fill(grid, capacity):
    return sum((sum(row) + capacity - 1) // capacity for row in grid)

Explanation: Count ones per row and add ceil division by capacity for each row, then sum across rows.

