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


def gpio_wrapper(*args, **kwargs):
    def wrapper(func):
        gpio.setmode(gpio.BOARD)
        try:
            hook_handler(kwargs.get('start_hook'))
            func()
        except KeyboardInterrupt:
            print("keyboard interrupt")
        finally:
            hook_handler(kwargs.get('stop_hook'))
            gpio.cleanup()
            print("cleanup called")
    return wrapper


def gpiozero_wrapper(*args, **kwargs):
    def wrapper(func):
        if config.ENVIRONMENT == 'dev':
            gpiozero.Device.pin_factory = gpiozero.pins.mock.MockFactory()
        try:
            hook_handler(kwargs.get('start_hook'))
            func()
        except KeyboardInterrupt:
            print("keyboard interrupt")
        finally:
            hook_handler(kwargs.get('stop_hook'))
    return wrapper
