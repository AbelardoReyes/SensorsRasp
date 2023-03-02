import time
import RPi.GPIO as GPIO


class Ultrasonico:
    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def medir(self):
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)
        start = time.time()
        while GPIO.input(self.echo) == 0:
            start = time.time()
        while GPIO.input(self.echo) == 1:
            stop = time.time()
        elapsed = stop - start
        distance = (elapsed * 34300)/2
        return distance

    def __del__(self):
        GPIO.cleanup()
