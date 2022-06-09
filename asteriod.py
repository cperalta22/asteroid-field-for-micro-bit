from microbit import *
import music

def ship_set(position):
    display.set_pixel(position,4,9)

def start_msg():
    music.play(music.CHASE,wait=False)
    display.scroll("asteroid field",delay=(70),monospace=True)
    for i in range(10):
        display.set_pixel(2,4,i)
        sleep(200)
    
def stop_msg():
    music.play(music.WAWAWAWAA,wait=False)
    for i in range(4,-1,-1):
        display.clear()
        display.set_pixel(2,i,5)
        sleep(200)
    display.set_pixel(2,0,9)
    sleep(500)
    display.clear()
    display.show(Image.CHESSBOARD)
    sleep(500)
    display.scroll("bye",delay=50,monospace=True)
    display.clear()

def life_set(lifes_count):
    if lifes_count == 3:
        lct = [1,1,1]
    elif lifes_count == 2:
        lct = [1,1,0]
    elif lifes_count == 1:
        lct = [1,0,0]
    elif lifes_count < 1 :
        lct = [0,0,0]
    pin14.write_digital(lct[0])
    pin15.write_digital(lct[1])
    pin16.write_digital(lct[2])
