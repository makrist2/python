def bin_search(lst, element):
    left_b = 0
    right_b = len(lst) - 1
    while left_b < right_b:
        middle = int((left_b + right_b) / 2)
        if element > lst[middle]:
            left_b = middle + 1
        else:
            right_b = middle
    if lst[right_b] == element:
        return right_b
    else:
        return None


lst = [2, 5, 7, 9, 11, 12, 17, 222]
print(bin_search(lst, 222))