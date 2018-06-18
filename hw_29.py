import string
import random


def gen_password():
    password = ''
    while len(password) < 8:
        for i in range(1):
            i = ''.join(random.choice(string.ascii_lowercase) for _ in range(1))
            password += i
            i = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
            password += i
            if len(password) == 8:
                break
            i = ''.join(random.choice(string.digits) for _ in range(1))
            password += i
    return password


pw = gen_password()
print(pw)
