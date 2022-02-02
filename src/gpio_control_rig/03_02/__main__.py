import time
from .. import config  # noqa: F401
from .. import utils
import gpiozero  # noqa: N814

LED_PINS = [
    "J8:11",
    "J8:12",
    "J8:13",
    "J8:15",
    "J8:16",
    "J8:18",
    "J8:22",
    "J8:3",
    "J8:5",
    "J8:24",
]

INTERVAL = 0.3
LEDS = gpiozero.LEDBoard(*LED_PINS, active_high=False)

def toggle_pin(pin_index):
    if config.ENVIRONMENT == 'dev':
        print(f"toggle pin {pin_index}")
    LEDS.on(pin_index)
    time.sleep(INTERVAL)
    LEDS.off(pin_index)

@utils.gpiozero_wrapper
def run():
    led_indexes = list(range(0, len(LED_PINS)))
    led_reverse = reversed(list(range(1, len(LED_PINS) - 1)))
    while True:
        [toggle_pin(pin) for pin in led_indexes]
        [toggle_pin(pin) for pin in reversed(led_indexes)]


if __name__ == '__main__':
    run()
