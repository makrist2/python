import random

list1 = []
for i in range(1, 101, 2):
    list1.append(i)


def shuffle_list(list_to_shuffle):
    n = len(list_to_shuffle)
    for j in range(n):
        k = random.randint(0, j)
        list_to_shuffle[j], list_to_shuffle[k] = list_to_shuffle[k], list_to_shuffle[j]
    return list_to_shuffle


print(shuffle_list(list1))