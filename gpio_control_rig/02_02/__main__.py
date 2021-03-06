import time
from .. import config  # noqa: F401
from .. import utils
import RPi.GPIO as GPIO  # noqa: N814

LED_PIN = 11
BUTTON_PIN = 12
LAST_STATE = False


class ButtonState:
    last_state = False

    def button_handler(self, channel):
        self.last_state = not self.last_state
        if self.last_state:
            print('led turned on >>>')
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            print('led turned off >>>')
            GPIO.output(LED_PIN, GPIO.LOW)


@utils.gpio_wrapper
def run():
    state_tracker = ButtonState()
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=state_tracker.button_handler, bouncetime=300)
    while True:
        time.sleep(0.005)


if __name__ == '__main__':
    run()
