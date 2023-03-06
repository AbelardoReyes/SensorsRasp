from sensores.ultrasonico import Ultrasonico
from sensores.led import Led
from sensores.sonido import SoundSensor
from sensores.temperatura import Temperatura
from views.distance_view import DistanceView
from views.led_view import LedView
from views.sound_view import SoundView


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
                print("Si")
            elif opcion == 2:
                DistanceView().leer()
            elif opcion == 3:
                LedView().menu()
            elif opcion == 4:
                SoundView().leer()
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
        ultrasonico = Ultrasonico(24, 23)
        print("Distancia: ", ultrasonico.medir(), "cm")

    def led(self):
        print("Led")
        led = Led(22)
        led.blink()
    
    def sonido(self):
        sonido = SoundSensor(17)
        print("Sonido: ", sonido.read_sound())
    
    def todos(self):
        print("Todos")
        self.distancia()
        self.led()


if __name__ == "__main__":
    menu = main()
    menu.main()
