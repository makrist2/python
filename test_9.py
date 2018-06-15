import random

new_list = [random.randint(-9, 9) for i in range(7)]
maxx = 0
for i in new_list:
    if abs(maxx) < abs(i):
        maxx = i

print(maxx, '\n')

for j in new_list:
    j /= abs(maxx)
    print(j)

