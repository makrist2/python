import random

test_lst = [1, 1, 1, 1, 1, -1, -1, 0, 0, 0, 0]
print(test_lst)
new_list = [random.randint(-1, 1) for i in range(11)]
# print(new_list)


def calc_frequency(lst):
    lst_set = set(lst)
    most_common = 0
    qty_most_common = 0
    zero = 0
    one = 0
    minone = 0
    for i in lst_set:
        qty = lst.count(i)
        if i == 1:
            one += qty
        elif i == 0:
            zero += qty
        elif i == -1:
            minone += qty
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = i
    if zero == one or zero == minone or one == minone:
        return None
    return most_common


print(calc_frequency(test_lst))