class TempHum:
    def __init__(self):
        self.dht = Adafruit_DHT.DHT11
        self.pin = 4

    def getTemp(self):
        humedad, temperatura = Adafruit_DHT.read_retry(self.dht, self.pin)
        return temperatura

    def getHum(self):
        humedad, temperatura = Adafruit_DHT.read_retry(self.dht, self.pin)
        return humedad