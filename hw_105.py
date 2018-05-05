import re


def is_valid_credit_card(credit_card):
    credit_card = credit_card.replace(" ", "")
    sum = 0
    num_digits = len(credit_card)
    odd_even = num_digits & 1

    for count in range(0, num_digits):

        digit = int(credit_card[count])

        if not ((count & 1) ^ odd_even):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ((sum % 10) == 0)

score = input("Input your credit card number: \n")
# print re.sub(r'\s', '', kio)
print(is_valid_credit_card(score))

