import time

from sensores.sensor import Sensor


class SoundView:
    def __init__(self, pin_in=4):
        self.sensor = Sensor(pin_in)

    def leer(self):
        print("Para detener la lectura pulsa Ctrl + C")
        while True:
            print(self.sensor.read())
