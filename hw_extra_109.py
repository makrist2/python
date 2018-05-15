def flatten(lst):
    new_lst = []
    for value in lst:
        if isinstance(value, list):
            new_lst.extend(flatten(value))
        else:
            new_lst.append(value)
    return new_lst


lst = [[1], [], [[[2, 3]]], [4, [5, [6]]], 7, 8]
assert [1, 2, 3, 4, 5, 6, 7, 8] == flatten(lst)

