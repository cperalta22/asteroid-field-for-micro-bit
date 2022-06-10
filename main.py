# Asteroid Field
# CPA 2022

from microbit import *
from asteriod import *
from characters import *
import random

#start_msg()
sleep(300)
startGame = True

while True:

    xwing = space_object(2,4,9)
    xwing.set_coor()
    tie0 = space_object(0,0,0)
    tie1 = space_object(0,0,0)
    tie2 = space_object(0,0,0)
    tie3 = space_object(0,0,0)
    tie4 = space_object(0,0,0)

    score = 0
    vida = 3
    ammo = False
    reload = 0
    veloc = 1
    vels = [1,0.8,0.6,0.4,0.2,0.1]
    clevel = 0

    if button_a.was_pressed():
        startGame = True

    while vida > 0 and startGame is True:
              
        life_set(vida)
        missile_set(ammo)
        
        if tie4.x_pos == xwing.x_pos and tie4.y_pos == xwing.y_pos:
            display.clear()
            vida = vida - 1
            life_set(vida)
            ammo = False
            missile_set(ammo)
            display.scroll(vida)
            display.show(Image.HEART)
            sleep(500)
            display.clear()
            tie0.to_zeros()
            tie1.to_zeros()
            tie2.to_zeros()
            tie3.to_zeros()
            tie4.to_zeros()
            xwing.set_coor()
            
        else:
            missile_set(ammo)
            score = scoreCalc(clevel,ammo,score, vida)
            reload = reload + 1
            tie4.off()
            tie4 = tie3
            tie4.attack()
            tie3 = tie2
            tie3.attack()
            tie2 = tie1
            tie2.attack()
            tie1 = tie0
            tie1.attack()
            tie0 = space_object(random.randint(0,4),0,4)
            tie0.set_coor()
            xwing.action(veloc, ammo)
            if button_b.was_pressed() and ammo is True:
                music.play(music.JUMP_DOWN,wait=False)
                display.clear()
                display.show(Image.CHESSBOARD)
                tie0.to_zeros()
                tie1.to_zeros()
                tie2.to_zeros()
                tie3.to_zeros()
                tie4.to_zeros()
                sleep(200)
                display.clear()
                xwing.set_coor()
                ammo=False

        if reload == 25:
            clevel = clevel +1
            ammo = True
            if clevel > 5:
                startGame = False
                victory_msg(score)
            else:
                veloc = vels[clevel]
                reload = 0

    if startGame is True:
        display.show(Image.SAD)
        sleep(500)
        stop_msg(score)
        
    startGame = False
    
                
    
    
