# importeer GPIO en time package
import RPi.GPIO as GPIO
import time

# gebruik BCM mode voor de pin nummering (conform breakout)
GPIO.setmode(GPIO.BCM)

# zet de pin als input
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# loop through 20 times
for i in range(20):
    if GPIO.input(4):
        print("button pressed")
    else:
        print("button released")

    time.sleep(0.5)
GPIO.cleanup()
