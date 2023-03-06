import time
import Adafruit_DHT

import RPi.GPIO as GPIO


class Sensor:
    def __init__(self, pin_in=0, pin_out=0):
        self.adafruit = Adafruit_DHT.DHT11
        self.pin_in = pin_in
        self.pin_out = pin_out
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_in, GPIO.IN)
        GPIO.setup(pin_out, GPIO.OUT)

    def read(self):
        return GPIO.input(self.pin_in)

    def on(self):
        GPIO.output(self.pin_out, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin_out, GPIO.LOW)

    def blink(self):
        self.on()
        time.sleep(1)
        self.off()
        time.sleep(1)

    def get_temperatura_humedad(self):
        temperatura, humedad = Adafruit_DHT.read(self.adafruit, self.pin_in)
        if temperatura is not None and humedad is not None:
            datos = [temperatura, humedad]
            return datos
        else:
            return [0, 0]

    def medir(self):
        GPIO.output(self.pin_out, False)
        time.sleep(0.00001)
        GPIO.output(self.pin_out, True)

        while GPIO.input(self.pin_in) == False:
            pulse_start = time.time()
        while GPIO.input(self.pin_in) == True:
            pulse_end = time.time()
        sig_time = pulse_end - pulse_start
        distance = sig_time / 0.000058
        return distance

    def __del__(self):
        GPIO.cleanup()
