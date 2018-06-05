a = float(input())
b = float(input())
c = 10

x = abs(c - a)
y = abs(c - b)

if x > y:
    print(b)
else:
    print(a)