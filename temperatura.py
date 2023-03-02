import Adrafruit_DHT


class Temperatura:
    def __init__(self, pin):
        self.pin = pin

    def leer(self):
        humedad, temperatura = Adrafruit_DHT.read_retry(11, self.pin)
        return humedad, temperatura
