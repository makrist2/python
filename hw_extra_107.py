def bin_search(lst, element):
    left_b = 0
    right_b = len(lst) - 1
    while left_b < right_b:
        middle = (left_b + right_b) // 2
        if element > lst[middle]:
            left_b = middle + 1
        else:
            right_b = middle
    if lst[right_b] == element:
        return right_b
    else:
        return None


lst = [2, 5, 7, 9, 11, 12, 17, 222]
assert 0 == bin_search(lst, 2)
assert 4 == bin_search(lst, 11)
assert 7 == bin_search(lst, 222)
assert None == bin_search(lst, 42)
