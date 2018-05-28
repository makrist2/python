import random
import enum


class Prs(enum.IntEnum):
    paper = 1
    rock = 2
    scissors = 3


def is_user_winner(user_choice, computer_choice):
    if user_choice == Prs.paper and computer_choice == Prs.scissors:
        return False
    elif user_choice == Prs.scissors and computer_choice == Prs.rock:
        return False
    elif user_choice == Prs.rock and computer_choice == Prs.paper:
        return False
    return True


def game():
    while True:
        input_data = input("""
1 - PAPER
2 - ROCK
3 - SCISSORS
Please make your choice (\'q\' for exit):""")

        if input_data == 'q':
            print('Bye!')
            break

        if not input_data.isnumeric():
            print('Invalid data!')
            continue

        user_choice = int(input_data)
        if not (1 <= user_choice <= 3):
            print('Invalid data!')
            continue

        computer_choice = random.choice(list(Prs))
        if user_choice == computer_choice:
            print('Tie!')
        else:
            if is_user_winner(user_choice, computer_choice):
                print('User is winner! %d vs %d' % (user_choice, computer_choice))
            else:
                print('AI is winner! %d vs %d' % (user_choice, computer_choice))

game()