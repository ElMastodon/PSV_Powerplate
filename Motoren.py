import RPi.GPIO as GPIO
import pigpio
import time


# Pin 12 (GPIO17) um Plattform anzuheben


#Motor 2
def init2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)

#Motor 3
def init3():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)



def anhebenOben():

    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(17, GPIO.LOW)

        p = GPIO.PWM(18, 50)
        p.start(40)


        GPIO.output(27, GPIO.HIGH)

        time.sleep(10)
        p.stop()
        GPIO.output(27, GPIO.LOW)
    finally:
        print("Fertig!")
        GPIO.cleanup()



def anhebenUnten():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(17, GPIO.LOW)

        time.sleep(10)
        GPIO.output(27, GPIO.LOW)
    finally:
        print("Fertig!")
        GPIO.cleanup()


def vibSortier():
    try:
        GPIO.output(22, GPIO.LOW)
        GPIO.output(10, GPIO.HIGH)

        time.sleep(10)
        GPIO.output(10, GPIO.LOW)
    finally:
        print("Fertig!")
        GPIO.cleanup()


def vibAnordnung():
    pass
    GPIO.cleanup
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(12, GPIO.LOW)
    GPIO.cleanup