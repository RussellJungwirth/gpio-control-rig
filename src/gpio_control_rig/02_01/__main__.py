from .. import config  # noqa: F401
from .. import utils
import RPi.GPIO as GPIO  # noqa: N814

LED_PIN = 11
BUTTON_PIN = 12


@utils.gpio_wrapper
def run():
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('led turned on >>>')
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('led turned off <<<')


if __name__ == '__main__':
    run()
