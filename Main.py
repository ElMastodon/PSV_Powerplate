import time
import TSL2561
import RPi.GPIO as GPIO

print("Welcome")
y = input("Press y to start the procedure!")

if y == "y":
    GPIO.cleanup
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(12, GPIO.LOW)
    GPIO.cleanup

    while True:
        lux = TSL2561.getLux()



