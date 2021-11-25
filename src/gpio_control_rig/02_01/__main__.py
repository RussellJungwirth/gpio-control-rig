from .. import config  # noqa: F401
from .. import utils
import RPi.GPIO as GPIO  # noqa: N814

LED_PIN = 11
BUTTON_PIN = 12


@utils.gpio_wrapper
def run():
    states = [
        {"channel": LED_PIN, "state": GPIO.OUT},
        {"channel": BUTTON_PIN, "state": GPIO.IN, "initial": 0, "pull_up_down": GPIO.PUD_UP},
    ]
    for state in states:
        GPIO.setup(**state)
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('led turned on >>>')
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('led turned off <<<')


if __name__ == '__main__':
    run()
