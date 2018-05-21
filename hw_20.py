import random


def diff_even_odd(num_limit, lower_bound, upper_bound):
    even = 0
    odd = 0
    for i in range(num_limit):
        rnd_num = random.randint(lower_bound, upper_bound)
        # print(rnd_num)
        if rnd_num % 2 == 0:
            even += rnd_num
        else:
            odd += rnd_num
    return even - odd


print(diff_even_odd(5, 20, 60))
