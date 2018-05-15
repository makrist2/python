def remove_duplicate(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
assert [12, 24, 35, 88, 120, 155] == remove_duplicate(lst)
