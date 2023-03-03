import threading
from ultrasonico import Ultrasonico
from led import Led
from temperatura import Temperatura
import os


class main:
    def main(self):
        opcion = 10
        while opcion != 0:
            print("1. Temperatura y humedad")
            print("2. Distancia")
            print("3. Led")
            print("4. Sonido")
            print("5. Leer todos los sensores")
            print("0. Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                self.temHum()
            elif opcion == 2:
                self.distancia()
            elif opcion == 3:
                self.led()
            elif opcion == 5:
                self.todos()
            elif opcion == 0:
                print("Saliendo...")
            else:
                print("Opcion invalida")

    def temHum(self):
        print("Temperatura y humedad")
        temperatura = Temperatura()
        datos = temperatura.get_temperatura_humedad()
        print("Temperatura: ", datos[0], "C")
        print("Humedad: ", datos[1] , "%")

    def distancia(self):
        print("Distancia")
        ultrasonico = Ultrasonico(5, 6)
        print("Distancia: ", ultrasonico.medir(), "cm")

    def led(self):
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
