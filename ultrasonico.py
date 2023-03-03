import time
import RPi.GPIO as GPIO
from pynput import keyboard as kb


class Ultrasonico:
    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def medir(self):
        while kb.is_pressed('q') == False:
            GPIO.output(self.trigger, False)
            time.sleep(0.00001)
            GPIO.output(self.trigger, True)

            while GPIO.input(self.echo) == False:
                pulse_start = time.time()
            while GPIO.input(self.echo) == True:
                pulse_end = time.time()
            sig_time = pulse_end - pulse_start
            distance = sig_time / 0.000058
            return distance

    def __del__(self):
        GPIO.cleanup()
