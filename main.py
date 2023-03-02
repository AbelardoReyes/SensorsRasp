import threading
from ultrasonico import Ultrasonico
from temperatura import Temperatura
from led import Led


class main:
    def main(self):
        opcion = 10
        while opcion != 0:
            print("1. Temperatura y humedad")
            print("2. Distancia")
            print("3. Led")
            print("0. Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                self.temHum()
            elif opcion == 2:
                self.distancia()
            elif opcion == 3:
                self.led()
            elif opcion == 0:
                print("Saliendo...")
            else:
                print("Opcion invalida")

    def temHum(self):
        print("Temperatura y humedad")
        temperatura = Temperatura(4)
        print("Temperatura: ", temperatura.leer()[1], "C")
        input("Presione cualquier tecla para continuar...")


    def distancia(self):
        print("Distancia")
        ultrasonico = Ultrasonico(23, 24)
        print("Distancia: ", ultrasonico.medir(), "cm")
        input("Presione cualquier tecla para continuar...")
        

    def led(self):
        print("Led")
        led = Led(18)
        led.blink()
        input("Presione cualquier tecla para continuar...")


if __name__ == "__main__":
    menu = main()
    menu.main()
