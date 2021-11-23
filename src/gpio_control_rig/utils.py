import random
import string


def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_int(min=0, max=99999999):
    return random.randint(min, max)
