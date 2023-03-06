import time

from sensor import Sensor


class DistanceView:
    def __init__(self, pin_in=6, pin_out=5):
        self.sensor = Sensor(pin_in, pin_out)

    def leer(self):
        print("Para detener la lectura pulsa Ctrl + C")
        try:
            while True:
                print("Distancia: ", self.sensor.medir(), "cm")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Fin de la lectura")
            return
