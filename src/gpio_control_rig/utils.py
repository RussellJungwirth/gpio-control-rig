import random
import string
import RPi.GPIO as gpio  # noqa: N813


def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_int(min=0, max=99999999):
    return random.randint(min, max)


def gpio_wrapper(func):
    def wrapper():
        gpio.setmode(gpio.BOARD)
        try:
            func()
        except KeyboardInterrupt:
            print("keyboard interrupt")
        finally:
            gpio.cleanup()
            print("cleanup called")
    return wrapper
