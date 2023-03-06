
from sensores.sensor import Sensor


class DistanceView:
    def __init__(self, pin_in=6, pin_out=5):
        self.sensor = Sensor(pin_in, pin_out)

    def leer(self):
        print("Para detener la lectura pulsa Ctrl + C")
        while True:
            print("Distancia: ", self.sensor.medir(), "cm")
            
