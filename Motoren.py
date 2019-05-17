import RPi.GPIO as GPIO
import time
import _thread

def secStandard():
    secSchub = 3
    secAnord = 30
    secSort = 10
    secAnheben = 3
    secAnhebenSort = 10

    return secSchub,secAnord,secSort,secAnheben,secAnhebenSort

def secSet0():
    secSchub = 0
    secAnord = 0
    secSort = 0
    secAnheben = 0
    secAnhebenSort = 0

    return secSchub, secAnord, secSort, secAnheben, secAnhebenSort


# Pin 12 (GPIO17) um Plattform anzuheben
def ganzesSystemDurchlaufen():
    try:

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(7, GPIO.IN)  # Stopp

        secSchub = 3
        secAnord = 30
        secSort = 10
        secAnheben = 3
        secAnhebenSort = 10
        if GPIO.input(7) == 1:
            secSet0()

        initAnfangszustand()

        print("INIT ERLEDIGT!")
        print("-----------" * 6)
        time.sleep(1)
        vibSort(80,secSort)
        if GPIO.input(7) == 1:
            secSet0()

        time.sleep(0.5)
        konstantesAnheben(90, 70, secAnhebenSort)
        if GPIO.input(7) == 1:
            secSet0()

        print("Schublade wird geöffnet")
        print("-----------" * 6)
        time.sleep(2)
        anhebenUnten(40, secAnheben)
        if GPIO.input(7) == 1:
            secSet0()

        schubOeffnen(85, secSchub)
        if GPIO.input(7) == 1:
            secSet0()

        time.sleep(0.5)
        konstantesAnheben(90, 90, secAnhebenSort)
        if GPIO.input(7) == 1:
            secSet0()

        print("Vibration der Anordnungsplattform wird durchgeführt")
        print("-----------" * 6)
        time.sleep(2)
        vibAnord(90, secAnord)
        if GPIO.input(7) == 1:
            secSet0()

        print("-----------" * 6)
        time.sleep(0)
        anhebenUnten(40, secAnheben)
        if GPIO.input(7) == 1:
            secSet0()

    finally:
        GPIO.cleanup()

def initAnfangszustand():
    anhebenUnten(40,1)
    schubSchliessen(90,4)

def konstantesAnheben(dcAn,dcVib , sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(26, GPIO.IN)  # Endschalter Oben
        GPIO.setup(9, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(7, GPIO.IN)  # Stopp

        GPIO.output(27, GPIO.LOW)
        GPIO.output(9, GPIO.LOW)

        p1 = GPIO.PWM(19, 2000)
        p1.start(dcVib)

        GPIO.output(11, GPIO.HIGH)
        p2 = GPIO.PWM(18, 2000)
        p2.start(dcAn)

        print(GPIO.input(26))

        while sec > 0:
            GPIO.output(17, GPIO.HIGH)
            time.sleep(0.01)
            sec -= 0.01
            if (GPIO.input(7)) == 1:
                sec = 0

        GPIO.output(17, GPIO.LOW)
        p1.stop
        p2.stop


    finally:
        GPIO.cleanup()

def anhebenOben(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(26, GPIO.IN)  # Endschalter Oben
        GPIO.setup(7, GPIO.IN)  # Stopp

        GPIO.output(27, GPIO.LOW)

        p = GPIO.PWM(18, 2000)
        p.start(dc)

        while (GPIO.input(26)) == 0 and sec > 0:
            print(GPIO.input(26))
            GPIO.output(17, GPIO.HIGH)
            time.sleep(0.01)
            sec -= 0.01
            if (GPIO.input(7)) == 1:
                sec = 0

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
        GPIO.setup(7, GPIO.IN)  # Stopp

        GPIO.output(17, GPIO.LOW)  #Beides auf Low stellen
        GPIO.output(27, GPIO.LOW)


        p = GPIO.PWM(18, 2000)
        p.start(dc)





        while (GPIO.input(14)) == 0 and sec > 0:
            GPIO.output(27, GPIO.HIGH)
            time.sleep(0.04)
            sec -=0.04
            if (GPIO.input(7)) == 1:
                sec = 0


        p.stop()
        GPIO.output(27, GPIO.LOW)

    finally:
        GPIO.cleanup()



def schubOeffnen(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)  # PWM SIgnal
        GPIO.setup(23, GPIO.IN)  # Endschalter Schublade aussen
        GPIO.setup(15, GPIO.IN)  # Endschalter Schublade innen
        GPIO.setup(7, GPIO.IN)  # Stopp

        GPIO.output(22, GPIO.LOW)

        p = GPIO.PWM(13, 2000)

        while (GPIO.input(23)) == 0 and sec > 0:

            if GPIO.input(15) == 1:
                p.start(100)
                GPIO.output(10, GPIO.HIGH)
                time.sleep(0.3)
                sec -= 0.3

            if GPIO.input(15) == 0:
                p.start(dc)
                GPIO.output(10, GPIO.HIGH)
                time.sleep(0.01)
                sec -= 0.01




            if (GPIO.input(7)) == 1:
                sec = 0

        p.stop()
        GPIO.output(10, GPIO.LOW)
    finally:
        GPIO.cleanup()


def schubSchliessen(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT) # PWM SIgnal
        GPIO.setup(15, GPIO.IN)  # Endschalter Schublade innen
        GPIO.setup(7, GPIO.IN)  # Stopp


        GPIO.output(22, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)

        p = GPIO.PWM(13, 2000)
        p.start(dc)

        secStart = sec

        time.sleep(1)

        while (GPIO.input(15)) == 0 and sec > 0:

            if sec > (secStart -0.3):
                p.start(100)
                GPIO.output(22, GPIO.HIGH)
                time.sleep(0.01)
                sec -= 0.01

            if sec <= (secStart - 0.3):
                p.start(dc)
                GPIO.output(22, GPIO.HIGH)
                time.sleep(0.01)
                sec -= 0.01

            if (GPIO.input(7)) == 1:
                sec = 0


        p.stop()
        GPIO.output(22, GPIO.LOW)

    finally:
        GPIO.cleanup()


def vibSort(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(9, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(26, GPIO.IN)
        GPIO.setup(7, GPIO.IN)  # Stopp


        GPIO.output(9, GPIO.LOW)

        p = GPIO.PWM(19, 2000)
        p.start(dc)

        GPIO.output(11, GPIO.HIGH)
        while sec >= 0:
            sec -= 0.01
            time.sleep(0.01)
            if (GPIO.input(7)) == 1:
                sec = 0

        p.stop()
        GPIO.output(11, GPIO.LOW)

    finally:
        GPIO.cleanup()


def vibAnord(dc, sec):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT) #PWM
        GPIO.setup(7, GPIO.IN)  # Stopp

        GPIO.output(5, GPIO.LOW) #Auf 0 setzen
        GPIO.output(6, GPIO.LOW)


        p = GPIO.PWM(12, 2000)
        p.start(dc)

        GPIO.output(6, GPIO.HIGH)

        while sec > 0:
            time.sleep(0.01)
            sec -= 0.01
            if (GPIO.input(7)) == 1:
                sec = 0
                time.sleep(0.5)


        p.stop()
        GPIO.output(6, GPIO.LOW)

    finally:
        GPIO.cleanup()
