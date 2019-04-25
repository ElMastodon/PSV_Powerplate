import time
import TSL2561
import Motoren
import RPi.GPIO as GPIO
import threading

print("Willkommen")
print ("-----------" * 6)

bool = True

while bool == True:

    #while True:
    #    GPIO.setmode(GPIO.BCM)
    #    GPIO.setup(14, GPIO.IN)
    #    print(GPIO.input(14))

    print("Sie können folgende Sachen machen:")
    print("Drücken Sie 0 + Entertaste um den ganzen Prozess durchzuführen!")
    print("Drücken Sie 1 + Entertaste um die Sortierplattform anzuheben.")
    print("Drücken Sie 2 + Entertaste um die Sortierplattform runterzulassen")
    print("Drücken Sie 3 + Entertaste um die Schublade zu öffnen")
    print("Drücken Sie 4 + Entertaste um die Schublade zu schliessen")
    print("Drücken Sie 5 + Entertaste um die Sortierplattform zu vibrieren")
    print("Drücken Sie 6 + Entertaste um die Anordnungsplattform zu vibrieren")
    print("Drücken Sie 7 + Entertaste um die Prüflingsform zu prüfen")
    print("Drücken Sie 8 + Entertaste umd das Programm zu beenden")
    print ("-----------" * 6)

    inputVal = int(input("Geben Sie eine Option an!"))

    if (inputVal <= 6) and (inputVal >0) :
        dc = int(input("Geben Sie die eine Zahl zwischen 10-100 ein um die Leistung zu bestimmen"))
        sec = int(input("Geben Sie die Laufzeit in Sekunden ein"))
        print("-----------" * 6)



    if inputVal == 1:
        Motoren.anhebenOben(dc,sec)
    elif inputVal == 2:
        Motoren.anhebenUnten(dc,sec)
    elif inputVal == 3:
        Motoren.schubOeffnen(dc,sec)
    elif inputVal == 4:
        Motoren.schubSchliessen(dc,sec)
    elif inputVal == 5:
        Motoren.vibSort(dc,sec)
    elif inputVal == 6:
        Motoren.vibAnord(dc,sec)
    elif inputVal == 7:
        TSL2561.getLux()
    elif inputVal == 8:
        bool = False
    elif inputVal ==9:
        konstantesAnheben(70,10)
    elif inputVal == 0:
        Motoren.initAnfangszustand()
        print("INIT ERLEDIGT!")
        print ("-----------" * 6)
        time.sleep(3)
        Motoren.konstantesAnheben(90,75,10)
        print("Schublade wird geöffnet")
        print("-----------" * 6)
        time.sleep(2)
        Motoren.anhebenUnten(40,5)
        Motoren.schubOeffnen(90,5)
        time.sleep(2)
        Motoren.konstantesAnheben(90,85,10)
        print("Vibration der Anordnungsplattform wird durchgeführt")
        print("-----------" * 6)
        time.sleep(2)
        Motoren.vibAnord(100,20)
        print("Lichtdurchlässigkeit wird getestet")
        print("-----------" * 6)
        time.sleep(2)
        Motoren.anhebenUnten(40, 1)

   # elif inputVal == 9:

