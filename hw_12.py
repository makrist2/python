def sum_of_digits_a(number):
    return int(number[0]) + int(number[1]) + int(number[2])


print(sum_of_digits_a('123'))


def sum_of_digits_b(number):
    n1 = number % 10
    n2 = number % 100 // 10
    n3 = number // 100
    return n1 + n2 + n3


print(sum_of_digits_b(123))