def minPath(grid, k):
    N = len(grid)
    # find coordinates of the global minimum (works even if min != 1)
    min_val = min(min(row) for row in grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j] == min_val:
                r, c = i, j
                break
        else:
            continue
        break

    path = [min_val]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for _ in range(k-1):
        best_val = float('inf')
        best_pos = None
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                v = grid[nr][nc]
                if v < best_val:
                    best_val = v
                    best_pos = (nr, nc)
        # move to the smallest neighbor
        r, c = best_pos
        path.append(best_val)
    return path

