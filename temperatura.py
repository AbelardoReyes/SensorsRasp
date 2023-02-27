import Adafruit_DHT


class TempHum:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = 4

    def getTemp(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return temperature

    def getHum(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return humidity

    def getTempHum(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return temperature, humidity
