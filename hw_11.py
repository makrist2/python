import math


def degrees2radians(degrees):
    return degrees*180/math.pi


print('Cosine of 45: %.2f' % math.cos(degrees2radians(45)))
print('Cosine of 40: %.2f' % math.cos(degrees2radians(40)))
print('Cosine of 60: %.2f' % math.cos(degrees2radians(60)))