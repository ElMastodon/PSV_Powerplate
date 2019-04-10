import RPi.GPIO as GPIO
import pigpio
import time
import _thread


# Pin 12 (GPIO17) um Plattform anzuheben


def initAnfangszustand():
    anhebenUnten(30,5)
    schubSchliessen(85,5)
    GPIO.cleanup()


def konstantesAnheben(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(26, GPIO.IN)  # Endschalter Oben

        GPIO.output(27, GPIO.LOW)

        p = GPIO.PWM(18, 2000)
        p.start(dc)

        while sec > 0:
            print(GPIO.input(26))
            GPIO.output(17, GPIO.HIGH)
            time.sleep(0.01)
            sec -= 0.01

        GPIO.output(17, GPIO.LOW)



    finally:
        GPIO.cleanup()
        print("%s: %s" % (thread1, time.ctime(time.time())))
        print("Fertig!")

def anhebenOben(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(26, GPIO.IN)  # Endschalter Oben

        GPIO.output(27, GPIO.LOW)

        p = GPIO.PWM(18, 2000)
        p.start(dc)

        while (GPIO.input(26)) == 0 and sec > 0:
            print(GPIO.input(26))
            GPIO.output(17, GPIO.HIGH)
            time.sleep(0.01)
            sec -= 0.01

        GPIO.output(17, GPIO.LOW)



    finally:
        GPIO.cleanup()
        print("Fertig!")




def anhebenUnten(dc,sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)    #Signal zu H-Brücke 1
        GPIO.setup(27, GPIO.OUT)    #Signal zu H-Brücke 2
        GPIO.setup(18, GPIO.OUT)  # PWM
        GPIO.setup(14, GPIO.IN)  # Endschalter Unten

        GPIO.output(17, GPIO.LOW)  #Beides auf Low stellen
        GPIO.output(27, GPIO.LOW)


        p = GPIO.PWM(18, 2000)
        p.start(dc)
        print("Schritt 1")

        print(GPIO.input(14))
        print("Sek: " + str(sec))

        while (GPIO.input(14)) == 0 and sec > 0:
            print("Schritt 2")
            print(GPIO.input(14))
            GPIO.output(27, GPIO.HIGH)
            time.sleep(0.01)
            sec -=0.01


        p.stop()
        GPIO.output(27, GPIO.LOW)
        print("Schritt 3")

    finally:
        print("Schritt 4")
        GPIO.cleanup()



def schubOeffnen(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)  # PWM SIgnal
        GPIO.setup(23, GPIO.IN)  # Endschalter Schublade aussen

        GPIO.output(22, GPIO.LOW)

        p = GPIO.PWM(13, 2000)
        p.start(dc)

        while (GPIO.input(23)) == 0 and sec > 0:
            print(GPIO.input(23))
            GPIO.output(10, GPIO.HIGH)
            time.sleep(0.01)
            sec -= 0.01

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
        GPIO.setup(13, GPIO.OUT) # PWM SIgnal
        GPIO.setup(15, GPIO.IN)  # Endschalter Schublade innen


        GPIO.output(22, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)

        p = GPIO.PWM(13, 2000)
        p.start(dc)

        while (GPIO.input(15)) == 0 and sec > 0:
            print(GPIO.input(15))
            GPIO.output(22, GPIO.HIGH)
            time.sleep(0.01)
            sec -= 0.01


        p.stop()
        GPIO.output(22, GPIO.LOW)

    finally:
        print("Fertig!")
        GPIO.cleanup()


def vibSortThreaded(thread2,dc, sec):

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
        print("%s: %s" % (thread2, time.ctime(time.time())))
        GPIO.cleanup()

def vibSort(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(9, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(26, GPIO.IN)


        GPIO.output(9, GPIO.LOW)

        p = GPIO.PWM(19, 2000)
        p.start(dc)

        GPIO.output(11, GPIO.HIGH)
        time.sleep(sec)


        while sec > 0:
            GPIO.output(11, GPIO.HIGH)
            if (GPIO.input(26))== 0:
                anhebenOben(85,0.5)
            time.sleep(0.05)
            sec -= 0.05



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
        GPIO.setup(12, GPIO.OUT) #PWM

        GPIO.output(5, GPIO.LOW) #Auf 0 setzen
        GPIO.output(6, GPIO.LOW)


        p = GPIO.PWM(12, 2000)
        p.start(dc)

        GPIO.output(6, GPIO.HIGH)

        time.sleep(sec)
        p.stop()
        GPIO.output(6, GPIO.LOW)

    finally:
        print("Fertig!")
        GPIO.cleanup()
