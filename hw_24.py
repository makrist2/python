def group_by_surname(list_of_enrollees):
    first = 'ABCDEFGHI'
    f = 0
    second = 'JKLMOP'
    s = 0
    third = 'QRST'
    t = 0
    fourth = 'UVWXYZ'
    fo = 0
    for _ in list_of_enrollees:
        for j in list_of_enrollees:
            sur = j.split()[1][0]
            print(sur)
            if sur in first:
                f += 1
            elif sur in second:
                s += 1
            elif sur in third:
                t += 1
            elif sur in fourth:
                fo += 1
        return f, s, t, fo


lst = ['Will Smith', 'Jay Z', 'Leonardo DiCaprio', 'George Orwell']
print(group_by_surname(lst))

