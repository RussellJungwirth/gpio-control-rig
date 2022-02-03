import random
from re import L
import string
import RPi.GPIO as gpio  # noqa: N813
import gpiozero
from . import config

def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_int(min=0, max=99999999):
    return random.randint(min, max)


def hook_handler(func):
    if callable(func):
        return func()


def gpio_wrapper(func):
    def wrapper():
        print("gpio setup")
        gpio.setmode(gpio.BOARD)
        try:
            func()
        except KeyboardInterrupt:
            print("keyboard interrupt")
        finally:
            gpio.cleanup()
            print("gpio teardown")
    return wrapper


def gpiozero_wrapper(func):
    def wrapper():
        if config.ENVIRONMENT == 'dev':
            gpiozero.Device.pin_factory = gpiozero.pins.mock.MockFactory()
        try:
            func()
        except KeyboardInterrupt:
            print("keyboard interrupt")
        finally:
            pass
    return wrapper
