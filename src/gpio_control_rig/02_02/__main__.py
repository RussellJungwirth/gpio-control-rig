import time
from .. import config  # noqa: F401
from .. import utils
import RPi.GPIO as GPIO  # noqa: N814

LED_PIN = 11
BUTTON_PIN = 12
LAST_STATE = False


def button_handler(channel):
    global LAST_STATE
    LAST_STATE = not LAST_STATE
    if LAST_STATE:
        print('led turned on >>>')
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        print('led turned on >>>')
        GPIO.output(LED_PIN, GPIO.LOW)


@utils.gpio_wrapper
def run():
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_handler, bouncetime=300)
    while True:
        time.sleep(0.005)


if __name__ == '__main__':
    run()
