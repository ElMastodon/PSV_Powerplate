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

    if inputVal == 5:
        setFalse()


    if bool == False:
        break

    def sys(arg):
        switcher = {
            1: Motoren.anheben1(),
            2: Motoren.vibSortier(),
            3: Motoren.vibAnordnung(),
            4: print("Test")
            }

    def setFalse():
        bool = False