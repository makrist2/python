import random


def numb():
    rand = random.randint(1, 10)
    while True:
        number = int(input('Plz input number from 1 to 10'))
        if number > rand:
            print('Calm down, mate. The actual number is lower')
        elif number < rand:
            print('It\'s higher')
        elif number == rand:
            print('Congratulations! You won!')
            break

numb()