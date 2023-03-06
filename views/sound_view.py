import time

from sensores.sensor import Sensor


class SoundView:
    def __init__(self, pin_in=4):
        self.sensor = Sensor(pin_in)

    def leer(self):
        print("Para detener la lectura pulsa Ctrl + C")
        try:
            while True:
                print(self.sensor.read())
                time.sleep(1)
        except KeyboardInterrupt:
            print("Fin de la lectura")
            return
