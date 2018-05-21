import random


def diff_min_max(num_limit, lower_bound, upper_bound):
    diff = []
    for i in range(num_limit):
        rnd_num = random.randint(lower_bound, upper_bound)
        diff.append(rnd_num)
    return max(diff) - min(diff)



print(diff_min_max(5, 20, 60))
