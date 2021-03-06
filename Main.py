import time
import TSL2561
import Motoren
import RPi.GPIO as GPIO


print("Willkommen")
print ("-----------" * 6)

bool = True

while bool == True:

    Motoren.secStandard()

    print("Sie koennen folgende Sachen machen:")
    print("Druecken Sie 0 + Entertaste um den ganzen Prozess durchzufuehren!")
    print("Druecken Sie 1 + Entertaste um die Sortierplattform anzuheben.")
    print("Druecken Sie 2 + Entertaste um die Sortierplattform runterzulassen")
    print("Druecken Sie 3 + Entertaste um die Schublade zu oeffnen")
    print("Druecken Sie 4 + Entertaste um die Schublade zu schliessen")
    print("Druecken Sie 5 + Entertaste um die Sortierplattform zu vibrieren")
    print("Druecken Sie 6 + Entertaste um die Anordnungsplattform zu vibrieren")
    print("Druecken Sie 7 + Entertaste um die Prueflingsform zu pruefen")
    print("Druecken Sie 8 + Entertaste umd das Programm zu beenden")
    print ("-----------" * 6)

    print("Druecken Sie 99 + Entertaste um das System ueber die Knoepfe zu steuern")
    print("-----------" * 6)


    inputVal = 99 #int(input("Geben Sie eine Option an!"))



    while inputVal == 99:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(24, GPIO.IN)  # Sortieren SortP
            GPIO.setup(25, GPIO.IN)  # Anordnen
            GPIO.setup(8, GPIO.IN)  # Ganzes System
            GPIO.setup(7, GPIO.IN)  # Stopp

            GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen

            if (GPIO.input(24)) == 1:          #Sortieren SortP



                Motoren.initAnfangszustand()

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(7, GPIO.IN)  # Stop

                Motoren.vibSort(80,5)

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(7, GPIO.IN)  # Stop

                if GPIO.input(7):
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                    GPIO.setup(25, GPIO.IN)  # Anordnen
                    GPIO.setup(8, GPIO.IN)  # Ganzes System
                    GPIO.setup(7, GPIO.IN)  # Stopp
                    GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen
                    break
                print("INIT ERLEDIGT!")
                print("-----------" * 6)
                time.sleep(3)
                Motoren.konstantesAnheben(90, 75, 10)

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(7, GPIO.IN)  # Stopp

                if GPIO.input(7):
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                    GPIO.setup(25, GPIO.IN)  # Anordnen
                    GPIO.setup(8, GPIO.IN)  # Ganzes System
                    GPIO.setup(7, GPIO.IN)  # Stopp
                    GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen
                    break
                print("Schublade wird geoeffnet")
                print("-----------" * 6)
                time.sleep(2)
                Motoren.anhebenUnten(40, 5)

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(7, GPIO.IN)  # Stopp

                if GPIO.input(7):
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                    GPIO.setup(25, GPIO.IN)  # Anordnen
                    GPIO.setup(8, GPIO.IN)  # Ganzes System
                    GPIO.setup(7, GPIO.IN)  # Stopp
                    GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen
                    break
                Motoren.schubOeffnen(90, 5)

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(7, GPIO.IN)  # Stopp

                if GPIO.input(7):
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                    GPIO.setup(25, GPIO.IN)  # Anordnen
                    GPIO.setup(8, GPIO.IN)  # Ganzes System
                    GPIO.setup(7, GPIO.IN)  # Stopp
                    GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen
                    break
                time.sleep(2)
                Motoren.konstantesAnheben(90, 85, 10)

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(7, GPIO.IN)  # Stopp

                if GPIO.input(7):
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                    GPIO.setup(25, GPIO.IN)  # Anordnen
                    GPIO.setup(8, GPIO.IN)  # Ganzes System
                    GPIO.setup(7, GPIO.IN)  # Stopp
                    GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen
                    break
                Motoren.anhebenUnten(40,3)

            GPIO.setmode(GPIO.BCM)
            GPIO.setup(24, GPIO.IN)  # Sortieren SortP
            GPIO.setup(25, GPIO.IN)  # Anordnen
            GPIO.setup(8, GPIO.IN)  # Ganzes System
            GPIO.setup(7, GPIO.IN)  # Stopp
            GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen

            if (GPIO.input(25)) == 1:               #Anordnungsplattform

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                GPIO.setup(25, GPIO.IN)  # Anordnen
                GPIO.setup(8, GPIO.IN)  # Ganzes System
                GPIO.setup(7, GPIO.IN)  # Stopp
                GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen

                if (GPIO.input(23)) == 0:
                    Motoren.schubOeffnen(90, 3)
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(7, GPIO.IN)  # Stopp


                    if GPIO.input(7):
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                        GPIO.setup(25, GPIO.IN)  # Anordnen
                        GPIO.setup(8, GPIO.IN)  # Ganzes System
                        GPIO.setup(7, GPIO.IN)  # Stopp
                        GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen
                        break

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                GPIO.setup(25, GPIO.IN)  # Anordnen
                GPIO.setup(8, GPIO.IN)  # Ganzes System
                GPIO.setup(7, GPIO.IN)  # Stopp
                GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen

                Motoren.vibAnord(90, 30)

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                GPIO.setup(25, GPIO.IN)  # Anordnen
                GPIO.setup(8, GPIO.IN)  # Ganzes System
                GPIO.setup(7, GPIO.IN)  # Stopp
                GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen

            if (GPIO.input(8)) == 1:                #Ganzes System

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                GPIO.setup(25, GPIO.IN)  # Anordnen
                GPIO.setup(8, GPIO.IN)  # Ganzes System
                GPIO.setup(7, GPIO.IN)  # Stopp
                GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen

                Motoren.ganzesSystemDurchlaufen()

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                GPIO.setup(25, GPIO.IN)  # Anordnen
                GPIO.setup(8, GPIO.IN)  # Ganzes System
                GPIO.setup(7, GPIO.IN)  # Stopp
                GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen
            if (GPIO.input(7)) == 1:         #stopp

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                GPIO.setup(25, GPIO.IN)  # Anordnen
                GPIO.setup(8, GPIO.IN)  # Ganzes System
                GPIO.setup(7, GPIO.IN)  # Stopp
                GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen

                Motoren.schubSchliessen(80,3)
                Motoren.anhebenUnten(40,3)
                time.sleep(0.5)
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(24, GPIO.IN)  # Sortieren SortP
                GPIO.setup(25, GPIO.IN)  # Anordnen
                GPIO.setup(8, GPIO.IN)  # Ganzes System
                GPIO.setup(7, GPIO.IN)  # Stopp
                GPIO.setup(23, GPIO.IN)  # Endschalter Schublade offen


        finally:
            GPIO.cleanup()

    if ((inputVal <= 6) and (inputVal >0)) or (inputVal ==9) :
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
        Motoren.vibSort(80,1.5)
        time.sleep(0.8)
        Motoren.konstantesAnheben(85,dc,sec)
    elif inputVal == 0:
        Motoren.ganzesSystemDurchlaufen()

   # elif inputVal == 9:

