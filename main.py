# Asteroid Field
# CPA 2022

# TEST ZONE 

from microbit import *
from asteriod import *
from characters import *

start_msg()
sleep(300)

xwing = space_object(2,4,9)
xwing.set_coor()
tie0 = space_object(0,0,0)
tie1 = space_object(0,0,0)
tie2 = space_object(0,0,0)
tie3 = space_object(0,0,0)
tie4 = space_object(0,0,0)

score = 0
vida = 3
while vida > 0:
    if tie4.x_pos == xwing.x_pos and tie4.y_pos == xwing.y_pos:
        display.clear()
        vida = vida - 1
        display.scroll(vida)
        display.show(Image.HEART)
        sleep(500)
        display.clear()
        tie0 = space_object(0,0,0)
        tie1 = space_object(0,0,0)
        tie2 = space_object(0,0,0)
        tie3 = space_object(0,0,0)
        tie4 = space_object(0,0,0)
        xwing.set_coor()
    else:
        score = score+1
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
        xwing.x_nav(1)

display.show(Image.SAD)
sleep(500)
stop_msg(score)


            


