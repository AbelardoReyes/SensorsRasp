import threading
from distancia import Distancia
from temperatura import TempHum
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
        tempHum = TempHum()
        print("Temperatura: " + str(tempHum.getTemp()))
        print("Humedad: " + str(tempHum.getHum()))
        input("Presione cualquier tecla para continuar...")

    def distancia(self):
        print("Distancia")
        distancia = Distancia(17, 27)
        print("Distancia: " + str(distancia.getDistancia()))
        input("Presione cualquier tecla para continuar...")

    def led(self):
        print("Led")
        led = Led(18)
        led.blink(3, 10)
        input("Presione cualquier tecla para continuar...")


if __name__ == "__main__":
    menu = main()
    menu.main()
