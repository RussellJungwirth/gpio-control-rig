from .. import config as env
from .. import utils
import RPi.GPIO as GPIO
import time

GPIO_PIN = 11

@utils.gpio_wrapper
def run():
    GPIO.setup(GPIO_PIN, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(GPIO_PIN, GPIO.LOW)  # make ledPin output LOW level 
    while True:
        GPIO.output(GPIO_PIN, GPIO.HIGH)
        print ('led turned on >>>')
        time.sleep(1)
        GPIO.output(GPIO_PIN, GPIO.LOW)
        print ('led turned off <<<')
        time.sleep(1)



if __name__ == '__main__':
    run()
