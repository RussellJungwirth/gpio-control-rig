import time
from .. import utils
import RPi.GPIO as GPIO # noqa: N814

class PwmState:
    state = None

    def __init__(self, pin=12, frequency=500, initial_value=0):
        self.state = GPIO.PWM(pin, frequency)
        self.state.start(initial_value)
    
    def __del__(self):
        self.state.stop()

    def set(self, value):
        self.state.ChangeDutyCycle(value)

INTERVAL = 0.5

@utils.gpio_wrapper
def run():
    pwm = PwmState()
    pwm_states = range(1, 101)
    while True:
        [pwm.set(level) for level in pwm_states]
        time.sleep(INTERVAL)
        [pwm.set(level) for level in reversed(pwm_states)]


if __name__ == '__main__':
    run()
