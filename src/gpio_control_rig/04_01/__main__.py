import time
from .. import utils
import RPi.GPIO as GPIO # noqa: N814


class PwmState:
    state = None

    def __init__(self, pin, frequency=500, initial_value=0):
        self.state = GPIO.PWM(pin, frequency)
        self.state.start(initial_value)
    
    def __del__(self):
        self.state.stop()

    def set(self, value):
        self.state.ChangeDutyCycle(value)

INTERVAL = 0.5
LED_PIN = 12

@utils.gpio_wrapper
def run():
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)
    pwm = PwmState(pin=LED_PIN)
    pwm_states = range(1, 101)
    while True:
        [pwm.set(level) for level in pwm_states]
        time.sleep(INTERVAL)
        [pwm.set(level) for level in reversed(pwm_states)]


if __name__ == '__main__':
    run()
