import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if r1 + r2 >= d >= abs(r1 - r2):
        return True
    else:
        return False
