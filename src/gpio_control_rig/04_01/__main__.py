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

PWM_INTERVAL = 0.1
PAUSE_INTERVAL = 1
STATUS_INTERVAL = 15
LED_PIN = 12

@utils.gpio_wrapper
def run():
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)
    pwm = PwmState(pin=LED_PIN)
    pwm_states = list(range(101))
    while True:
        for level in pwm_states:
            pwm.set(level)
            if level % STATUS_INTERVAL == 0:
                print(f"pwm level {level}")
            time.sleep(PWM_INTERVAL)
        print("pause")
        time.sleep(PAUSE_INTERVAL)
        pwm_states.reverse()

if __name__ == '__main__':
    run()
