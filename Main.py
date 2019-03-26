import time
import TSL2561
import RPi.GPIO as GPIO

print("Welcome")
y = input("Press y to start the procedure!")

if y == "y":
    GPIO.cleanup
    GPIO.setmode(GPIO.BOARD)


    lux = TSL2561.getLux()
    print(lux)


