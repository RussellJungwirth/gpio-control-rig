import time
import random
from .. import utils
import RPi.GPIO as GPIO # noqa: N814


class RgbLed:
    states = [None, None, None]

    def __init__(self, pins, frequency=2000, initial_value=0):
        self.pins = pins
        self.frequency = frequency
        self.initial_value = initial_value

    def startup(self):
        for index in range(len(self.states)):
            self.states[index] = GPIO.PWM(self.pins[index], self.frequency)
            self.states[index].start(self.initial_value)

    def teardown(self):
        for state in self.states:
            if state:
                state.stop()

    def set(self, values):
        for x in range(len(values)):
            self.states[x].ChangeDutyCycle(values[x])

PAUSE_INTERVAL = 1
LED_PINS = [11, 12, 13]

PWM = RgbLed(pins=LED_PINS)

@utils.gpio_wrapper(start_hook=PWM.startup, stop_hook=PWM.teardown)
def run():
    GPIO.setup(LED_PINS, GPIO.OUT)
    GPIO.output(LED_PINS, GPIO.LOW)
    while True:
        PWM.set([random.randint(0, 100) for _ in range(3)])
        time.sleep(PAUSE_INTERVAL)

if __name__ == '__main__':
    run()
