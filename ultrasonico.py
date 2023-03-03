import time
import RPi.GPIO as GPIO


class Ultrasonico:
    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def medir(self):
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        while GPIO.input(self.echo) == 0:
            start = time.time()

        while GPIO.input(self.echo) == 1:
            end = time.time()

        sig_time = end-start

        # CM:
        distance = sig_time / 0.000058

        # inches:
        # distance = sig_time / 0.000148

        print('Distance: {} centimeters'.format(distance))


GPIO.cleanup()


def __del__(self):
    GPIO.cleanup()
