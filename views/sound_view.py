import time

from sensores.sensor import Sensor


class SoundView:
    def __init__(self, pin_in=4):
        self.sensor = Sensor(pin_in)
        self.statusFalse = False

    def leer(self):
        print("Para detener la lectura pulsa Ctrl + C")
        try:
            while True:
                if self.sensor.read():
                    print("Sonido detectado")
                else:
                    print("...")

        except KeyboardInterrupt:
            print("Fin de la lectura")
            return
