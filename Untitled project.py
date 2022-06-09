from microbit import *
import random

def radar(cuadrante):
    if cuadrante == 0:
        for i in range(0,3):
            display.set_pixel(2,i,3)
    elif cuadrante == 1:
        for i in range (2,5):
            display.set_pixel(i,2,2)
    elif cuadrante == 2:
        for i in range (2,5):
            display.set_pixel(2,i,2)
    elif cuadrante == 3:
        for i in range (0,3):
            display.set_pixel(i,2,2)

def enemigos():
    x = random.randint(0,4)
    y = random.randint(0,4)
    display.set_pixel(x,y,9)

    

while True:
    if button_a.was_pressed():
        for i in range(4):
            display.clear()
            enemigos()
            radar(i)
            sleep(3000)
        display.clear()
        


