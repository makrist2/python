import math

a = 10
b = 6
c = 60

test1 = a + b * (c / 2)
print(test1)

test2 = (a*a + b*b) % 2
print(test2)

test3 = (a + b) / 12 * c % 4 + b
print(test3)

test4 = (a - b * c) / (a + b) % c
print(test4)

test5 = abs(a - b) / (a + b)**3 - math.cos(c)
print(test5)

test6 = (math.log(1 + c) / -b)**4 + abs(a)
print(test6)