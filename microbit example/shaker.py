from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        print("shake")
        display.clear()
        display.scroll("STOP IT!")
        sleep(1000)
        accelerometer.reset_gestures()
        sleep(1000)
