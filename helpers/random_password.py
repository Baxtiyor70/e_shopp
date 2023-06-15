import random
import string


def random_password(x):
    password = random.randint(10**(x-1), (10**x)-1)
    return password


def generate_code_token(lenght):
    password = ''.join(random.choice(string.printable) for i in range(lenght))

    return password

