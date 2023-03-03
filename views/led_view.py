

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
            match opcion:
                case 1:
                    self.led.on()
                case 2:
                    self.led.off()
                case 3:
                    self.led.blink()
                case 4:
                    print("Saliendo...")
                    return
                case _:
                    print("Opcion invalida")
            return opcion
