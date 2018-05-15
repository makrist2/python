import math


def cone_square_and_volume(radius, height):
    l = math.hypot(radius, height)
    square = math.pi * radius**2 + math.pi * radius * l
    volume = 1/3 * math.pi * radius**2 * height
    return square, volume


print(cone_square_and_volume(3, 4))