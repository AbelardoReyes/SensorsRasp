import Adafruit_DHT
import RPi.GPIO as GPIO

class Temperatura:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = 4
        self.relay_pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_pin, GPIO.OUT)
        GPIO.output(self.relay_pin, GPIO.HIGH)

    def get_temperatura_humedad(self):
        temperatura, humedad = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if temperatura is not None and humedad is not None:
            datos = [temperatura, humedad]
            return datos
        else:
            return [0, 0]

    def encender_relay(self):
        GPIO.output(self.relay_pin, GPIO.LOW)

    def apagar_relay(self):
        GPIO.output(self.relay_pin, GPIO.HIGH)

    def __del__(self):
        GPIO.cleanup()