import random
import string
import re


def gen_password():
    max_pass_len = 8
    first = 2
    second = 5
    third = 7
    pass_ = []
    chars_str = str(string.ascii_letters + string.ascii_lowercase + string.digits + '_')
    for i in range(max_pass_len):
        pass_ += str(random.choice(chars_str))
    if re.search('[0-9]', str(pass_)) not in pass_:
        pass_[random.randint(0, first)] = random.choice(string.digits)
    if re.search('[A-Z]', str(pass_)) not in pass_:
        pass_[random.randint(first, second)] = random.choice(string.ascii_uppercase)
    if re.search('[a-z]', str(pass_)) not in pass_:
        pass_[random.randint(second, third)] = random.choice(string.ascii_lowercase)
    joined_pass = ''.join(pass_)
    return joined_pass


print(gen_password())