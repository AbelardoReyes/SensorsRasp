import time

from sensores.sensor import Sensor


class TempView:
    def __init__(self, pin_in=16):
        self.sensor = Sensor(pin_in)

    def temHum(self):
        try:
            while True:
            print("Temperatura y humedad")
            datos = self.sensor.get_temperatura_humedad()
            print("Temperatura: ", datos[0], "C")
            print("Humedad: ", datos[1], "%")
            time.sleep(1)
        except KeyboardInterrupt:
            print("Fin de la lectura")
            return
