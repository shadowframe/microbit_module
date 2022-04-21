from microbit import *
from emoji import *
import os

all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
print( os.listdir())
while True:
    display.show(😃)
    if accelerometer.was_gesture('shake'):
        display.show(😡)
        sleep(2000)
    if button_a.was_pressed():
        display.show(💖)
        sleep(2000)
    elif button_b.was_pressed():
        display.show(all_boats, delay=200)
        print("Hallo1")
        print(os.listdir())
        sleep(2000)
    sleep(100)
    
