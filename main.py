import keyboard
import threading
from distancia import Distancia
from temperatura import TempHum
from led import Led


class main:
    def main(self):
        opcion = 0
        while opcion != 3:
            print("1. Temperatura y humedad")
            print("2. Distancia")
            print("3. Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                self.temHum()
            elif opcion == 2:
                self.distancia()
            elif opcion == 3:
                print("Saliendo...")
            else:
                print("Opcion invalida")

    def temHum(self):
        print("Temperatura y humedad")
        tempHum = TempHum()
        print("Temperatura: " + str(tempHum.getTemp()))
        print("Humedad: " + str(tempHum.getHum()))
        print("Presione cualquier tecla para continuar...")
        keyboard.wait()

    def distancia(self):
        print("Distancia")
        distancia = Distancia(17, 27)
        print("Distancia: " + str(distancia.getDistancia()))
        print("Presione cualquier tecla para continuar...")
        keyboard.wait()

    def led(self):
        print("Led")
        led = Led(18)
        led.blink(3, 0.5)
        print("Presione cualquier tecla para continuar...")
        keyboard.wait()

