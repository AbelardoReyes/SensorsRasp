import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
import time

class Led: 
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def blink(self):
        self.on()
        time.sleep(1)
        self.off()
        time.sleep(1)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup()