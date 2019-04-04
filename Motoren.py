import RPi.GPIO as GPIO
import pigpio
import time


# Pin 12 (GPIO17) um Plattform anzuheben

def anhebenOben():

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)

    time.sleep(10)
    GPIO.setmode(GPIO.BCM)
    GPIO.output(17, GPIO.LOW)
    GPIO.cleanup()


def anhebenUnten():
    GPIO.cleanup
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    time.sleep(1)
    GPIO.cleanup


def vibSortier():
    pass
    GPIO.cleanup
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(12, GPIO.LOW)
    GPIO.cleanup


def vibAnordnung():
    pass
    GPIO.cleanup
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(12, GPIO.LOW)
    GPIO.cleanup