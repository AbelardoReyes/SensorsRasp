import RPi.GPIO as GPIO
import time


class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, True)

    def off(self):
        GPIO.output(self.pin, False)

    def blink(self, times, delay):
        for i in range(times):
            self.on()
            time.sleep(delay)
            self.off()
            time.sleep(delay)
