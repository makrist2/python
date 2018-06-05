def print_mult_table(n, m):
    for i in range(n, m):
        for j in range(n, m):
            print("%5d" % (i * j), end='')
        print()


print_mult_table(1, 10)