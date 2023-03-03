import Adafruit_DHT

class Temperatura:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = 4

    def get_temperatura(self):
        temperatura = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return temperatura

    def get_humedad(self):
        humedad = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return humedad