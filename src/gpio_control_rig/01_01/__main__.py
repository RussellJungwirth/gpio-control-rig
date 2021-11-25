import time
from .. import config  # noqa: F401
from .. import utils
import RPi.GPIO as GPIO  # noqa: N814

LED_PIN = 11


@utils.gpio_wrapper
def run():
    states = [
        {"channel": LED_PIN, "state": GPIO.OUT},
    ]
    for state in states:
        GPIO.setup(**state)   # set the ledPin to OUTPUT mode
    GPIO.output(LED_PIN, GPIO.LOW)  # make ledPin output LOW level
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print('led turned on >>>')
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        print('led turned off <<<')
        time.sleep(1)


if __name__ == '__main__':
    run()
