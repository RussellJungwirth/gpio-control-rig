from .. import config  # noqa: F401
from .. import utils
import RPi.GPIO as GPIO  # noqa: N814

LED_PIN = 11
BUTTON_PIN = 12


@utils.gpio_wrapper
def run():
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    last_state = 0
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            GPIO.output(LED_PIN, GPIO.HIGH)
            if last_state == 0:
                print('led turned on >>>')
            last_state = 1
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            if last_state == 1:
                print('led turned off <<<')
            last_state = 0


if __name__ == '__main__':
    run()
