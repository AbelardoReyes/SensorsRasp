

from sensores.led import Led
from sensores.sensor import Sensor


class LedView:
    def __init__(self):
        self.sensor = Sensor(pin_out=4)

    def menu(self):
        while True:
            print("1. Encender")
            print("2. Apagar")
            print("3. Parpadear")
            print("4. Cambiar pin")
            print("5. Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                self.sensor.on()
            if opcion == 2:
                self.sensor.off()
            if opcion == 3:
                self.sensor.blink()
            if opcion == 4:
                try:
                    pin = int(input("Pin: "))
                    self.led = Led(pin)
                except ValueError:
                    print("Pin invalido")
                    continue
            if opcion == 5:
                print("Saliendo...")
                break
            else:
                print("Opcion invalida")

