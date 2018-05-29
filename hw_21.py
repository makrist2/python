import random

# ---------------- B -------------------


def get_max_digit_b(number):
    m = 0
    while number > 0:
        if number % 10 > m:
            m = number % 10
        number = number // 10
    return m

# ---------------- A -------------------


def get_max_digit_a(number):
    s = str(number)
    m = max(s, key=int)
    return m


rnd_num = random.randint(1e11, 1e12-1)
# print(rnd_num)
print(get_max_digit_b(rnd_num))

print(get_max_digit_a(rnd_num))