import time

from sensores.sensor import Sensor


class SoundView:
    def __init__(self, pin_in=4):
        self.sensor = Sensor(pin_in)
        self.status = True

    def menu(self):
        print("Selecciona alguna accion :")
        print("1. Leer sensor")
        print("3. Salir")

        opcion = int(input("Opcion: "))
        if opcion == 1:
            while self.status:
            self.sensor.read()
        if opcion == 2:
            self.sensor.off()
        if opcion == 3:
            self.sensor.blink()