import RPi.GPIO as GPIO
import time


class Led:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        self.pin = pin

    def on(self):
        GPIO.output(self.pin, True)

    def off(self):
        GPIO.output(self.pin, False)

    def blink(self):
            self.on()
            input("Presione cualquier tecla para continuar...")