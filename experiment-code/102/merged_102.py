import math

def choose_num(x, y):
    if x > y:
        return -1
    # largest integer <= y
    fy = math.floor(y)
    # make it even
    if fy % 2 != 0:
        fy -= 1
    return fy if fy >= math.ceil(x) else -1

