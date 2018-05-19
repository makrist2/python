def have_trains_crashed(v1, v2):
    first = 4/v1
    second = 6/v2
    if not first < second:
        return True
    else:
        return False

print(have_trains_crashed(5, 6))