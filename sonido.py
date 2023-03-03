import RPi.GPIO as GPIO

class SoundSensor:
    def __init__(self, pin_number):
        self.pin_number = pin_number
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_number, GPIO.IN)

    def read_sound(self):
        return GPIO.input(self.pin_number)

    def cleanup(self):
        GPIO.cleanup()