lst = [1, 2, 3, 4]
print(lst)
lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
print(lst)