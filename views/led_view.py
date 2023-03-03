

from led import Led


class LedView:
    def __init__(self, pin_number = 0):
        self.led = Led(pin_number)

    def menu(self):
        while True:
            print("1. Encender")
            print("2. Apagar")
            print("3. Parpadear")
            print("4. Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                self.led.on()
            if opcion == 2:
                self.led.off()
            if opcion == 3:
                self.led.blink()
            if opcion == 4:
                print("Saliendo...")
                return
            else:
                print("Opcion invalida")

