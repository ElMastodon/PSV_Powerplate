import time
import TSL2561
import Motoren


print("Welcome")

bool = True

while bool == True:

    print("Sie können folgende Sachen machen:")
    print("Drücken Sie 1 + Entertaste um die Sortierplattform anzuheben.")
    print("Drücken Sie 2 + Entertaste um die Sortierplattform zu vibrieren")
    print("Drücken Sie 3 + Entertaste um die Anordnungsplattform zu vibrieren")
    print("Drücken Sie 4 + Entertaste um die Prüflingsform zu prüfen")
    print("Drücken Sie 5 + Entertaste umd das Programm zu beenden")
    print ("-----------" * 6)

    inputVal = int(input("Geben Sie eine Option an!"))

    if inputVal == 1:
        Motoren.anhebenOben()
    elif inputVal == 2:
        Motoren.vibSortier()
    elif inputVal == 3:
        Motoren.vibAnordnung()
    elif inputVal == 4:
        TSL2561.getLux()
    elif inputVal == 5:
        bool = False

