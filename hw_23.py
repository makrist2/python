def chess_reward():
    for i in range(0, 64):
        for x in range(i):
            i = 2 ** x - 1
            if i > 1000000:
                return i, x


print(chess_reward())