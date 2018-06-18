def gen_primes():
    n = 100
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


print(gen_primes())