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

    inputVal = input("Geben Sie eine Option an!")


    if inputVal == 1:
        Motoren.anheben1()
    elif inputVal == 2:
        Motoren.vibSortier()
    elif inputVal == 3:
        Motoren.vibAnordnung()
    elif inputVal == 4:
        print("Test")
    elif inputVal == 5:
        break

