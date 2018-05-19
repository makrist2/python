import math


def solve_quadratic_equation(a, b, c):
    discr = b**2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr == 0:
        x1 = -b / (2 * a)
        x2 = None
        return x1, x2
    else:
        x1 = None
        x2 = None
        return x1, x2