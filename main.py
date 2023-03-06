from views.distance_view import DistanceView
from views.led_view import LedView
from views.sound_view import SoundView
from views.temp_view import TempView


class main:
    def main(self):
        opcion = 10
        while opcion != 0:
            print("1. Temperatura y humedad")
            print("2. Distancia")
            print("3. Led")
            print("4. Sonido")
            print("0. Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                TempView().temHum()
            elif opcion == 2:
                DistanceView().leer()
            elif opcion == 3:
                LedView().menu()
            elif opcion == 4:
                SoundView().leer()
            elif opcion == 0:
                print("Saliendo...")
            else:
                print("Opcion invalida")


if __name__ == "__main__":
    menu = main()
    menu.main()
