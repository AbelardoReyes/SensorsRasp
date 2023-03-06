import time

from sensores.sensor import Sensor


class TempView:
    def __init__(self, pin_in=4):
        self.sensor = Sensor(pin_in)

    def temHum(self):
        print("Temperatura y humedad")
        temperatura = self.sensor.get_temperatura_humedad()
        datos = temperatura.get_temperatura_humedad()
        print("Temperatura: ", datos[0], "C")
        print("Humedad: ", datos[1], "%")