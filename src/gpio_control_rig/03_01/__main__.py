import time
from .. import utils
import RPi.GPIO as GPIO # noqa: N814

LED_PINS = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

INTERVAL = 0.2

def toggle_pin(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(INTERVAL)
    GPIO.output(pin, GPIO.HIGH)

@utils.gpio_wrapper
def run():
    GPIO.setup(LED_PINS, GPIO.OUT)
    GPIO.output(LED_PINS, GPIO.HIGH)
    while True:
        [toggle_pin(pin) for pin in LED_PINS]
        [toggle_pin(pin) for pin in reversed(LED_PINS)]


if __name__ == '__main__':
    run()
