def chess_reward():
    i = 1
    c = 1
    while c <= 64:
        i *= 2
        c += 1
        if i > 1000000:
            return c, i


print(chess_reward())