x = int(input())

mult = 1
while x != 0:
    y = x % 10
    x = x // 10
    if y % 2 != 0 and y != 0:
        mult *= y
print(mult)