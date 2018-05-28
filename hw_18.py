def sum_symbol_codes(first, last):
    summ = 0
    first = ord(first)
    last = ord(last)
    summ = (last * (last + 1) - first * (first - 1)) / 2
    return int(summ)


print(sum_symbol_codes('a', 'd'))

"""
a = 97
b = 98
c = 99
d = 100
sum = 394
"""