import string
import random


def gen_password():

    pass_len = 8

    lowercase = list(string.ascii_lowercase + "_")
    uppercase = list(string.ascii_uppercase + "_")
    digits = [str(random.randrange(10)) for _ in range(len(lowercase))]

    [random.shuffle(dict_) for dict_ in [lowercase, uppercase]]

    strong_list = []
    for section in zip(lowercase, uppercase, digits):
        strong_list.extend(section)

    strong_pwd = strong_list[:pass_len]
    random.shuffle(strong_pwd)

    return "".join(strong_pwd)


print(gen_password())