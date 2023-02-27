import RPi.GPIO as GPIO
import time


class Led:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, True)

    def off(self):
        GPIO.output(self.pin, False)

    def blink(self):
            self.on()
            time.sleep(3)
            self.off()
            time.sleep(3)
