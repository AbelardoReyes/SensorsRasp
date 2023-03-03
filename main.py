import threading
from ultrasonico import Ultrasonico
from led import Led
import os


class main:
    def main(self):
        opcion = 10
        while opcion != 0:
            print("1. Temperatura y humedad")
            print("2. Distancia")
            print("3. Enceder Led")
            print("4. Apagar Led")
            print("0. Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                self.temHum()
            elif opcion == 2:
                self.distancia()
            elif opcion == 3:
                self.led()
            elif opcion == 4:
                self.todos()
            elif opcion == 0:
                print("Saliendo...")
            else:
                print("Opcion invalida")

    def temHum(self):
        print("Temperatura y humedad")

    def distancia(self):
        print("Distancia")
        ultrasonico = Ultrasonico(5, 6)
        print("Distancia: ", ultrasonico.medir(), "cm")

    def led(self):
        os.system("cls")
        print("Led")
        led = Led(13)
        led.blink()
    
    def todos(self):
        print("Todos")
        self.distancia()
        self.led()


if __name__ == "__main__":
    menu = main()
    menu.main()
