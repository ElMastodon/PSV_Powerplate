import RPi.GPIO as GPIO
import pigpio
import time


# Pin 12 (GPIO17) um Plattform anzuheben

def anhebenOben(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)  # PWM
        GPIO.setup(26, GPIO.IN)  # Endschalter
        GPIO.output(17, GPIO.LOW)

        p = GPIO.PWM(18, 2000)
        p.start(dc)

        while (GPIO.input(26)) == 0 and sec > 0:
            print(GPIO.input(26))
            GPIO.output(27, GPIO.HIGH)
            time.sleep(1)
            sec -=1

        p.stop()
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
    finally:
        print("Anordnungsplattform angehoben!")
        GPIO.cleanup()


def anhebenUnten(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(14, GPIO.IN)  # Endschalter

        GPIO.output(27, GPIO.LOW)

        p = GPIO.PWM(18, 2000)
        p.start(dc)

        while (GPIO.input(14)) == 0 and sec > 0:
            print(GPIO.input(14))
            GPIO.output(17, GPIO.HIGH)
            time.sleep(1)
            sec -= 1

        p.stop()
        GPIO.output(17, GPIO.LOW)
    finally:
        print("Fertig!")
        GPIO.cleanup()



def schubOeffnen(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(23, GPIO.IN)  # Endschalter Schublade aussen

        GPIO.output(22, GPIO.LOW)

        p = GPIO.PWM(10, 2000)
        p.start(dc)

        while (GPIO.input(23)) == 0 and sec > 0:
            print(GPIO.input(23))
            GPIO.output(10, GPIO.HIGH)
            time.sleep(1)
            sec -= 1

        time.sleep(sec)
        p.stop()
        GPIO.output(10, GPIO.LOW)
    finally:
        print("Fertig!")
        GPIO.cleanup()


def schubSchliessen(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.IN)  # Endschalter Schublade innen

        GPIO.output(22, GPIO.LOW)

        p = GPIO.PWM(10, 2000)
        p.start(dc)

        while (GPIO.input(15)) == 0 and sec > 0:
            print(GPIO.input(15))
            GPIO.output(10, GPIO.HIGH)
            time.sleep(1)
            sec -= 1

        time.sleep(sec)
        p.stop()
        GPIO.output(22, GPIO.LOW)

    finally:
        print("Fertig!")
        GPIO.cleanup()


def vibSort(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(9, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)

        GPIO.output(9, GPIO.LOW)

        p = GPIO.PWM(19, 2000)
        p.start(dc)

        GPIO.output(11, GPIO.HIGH)

        time.sleep(sec)
        p.stop()
        GPIO.output(11, GPIO.LOW)

    finally:
        print("Fertig!")
        GPIO.cleanup()


def vibAnord(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)

        GPIO.output(9, GPIO.LOW)

        p = GPIO.PWM(19, 2000)
        p.start(dc)

        GPIO.output(11, GPIO.HIGH)

        time.sleep(sec)
        p.stop()
        GPIO.output(11, GPIO.LOW)

    finally:
        print("Fertig!")
        GPIO.cleanup()
