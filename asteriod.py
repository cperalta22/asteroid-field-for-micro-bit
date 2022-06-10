from microbit import *
import music

def start_msg():
    music.play(music.CHASE,wait=False)
    display.scroll("asteroid field",delay=(70),monospace=True)
    for i in range(10):
        display.set_pixel(2,4,i)
        sleep(200)
    
def stop_msg(score):
    music.play(music.WAWAWAWAA,wait=False)
    for i in range(4,-1,-1):
        display.clear()
        display.set_pixel(2,i,5)
        sleep(200)
    display.set_pixel(2,0,9)
    sleep(500)
    display.clear()
    display.scroll("score:"+str(score),delay=150)
    display.clear()

def victory_msg(score):
    display.clear()
    music.play(music.ODE,wait=False)
    display.scroll("Victory", delay = 80)
    display.scroll("score"+ str(score), delay= 150)
    display.show(Image.HAPPY)
    sleep(1000)
    display.clear()

def life_set(lifes_count):
    if lifes_count == 3:
        lct = [1,1,1]
    elif lifes_count == 2:
        lct = [1,1,0]
    elif lifes_count == 1:
        lct = [1,0,0]
    else:
        lct = [0,0,0]

    pin14.write_digital(lct[0])
    pin15.write_digital(lct[1])
    pin16.write_digital(lct[2])

def missile_set(ammo):
    if ammo is True:
        pin13.write_digital(1)
    else:
        pin13.write_digital(0)

def scoreCalc(clevel,ammo,score,vida):
    lev = clevel + 1
    if ammo is True:
        nscore = (lev * 5) + score + vida
    else:
        nscore = (lev * 2) + score + vida
    return nscore
    
