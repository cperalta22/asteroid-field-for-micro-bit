# Test script to check clases functionality

# CPA 2022

# TEST ZONE 

from asteriod_b import *
from characters_b import *

xwing = space_object(2,4,9)

xwing.set_coor()
sleep(1000)
sense = 'up'
while True:
    if sense == 'up':
        if xwing.y_pos >= 1:
            xwing.new_coor(xwing.x_pos,xwing.y_pos-1)
            sleep(500)
        else:
            sense = 'down'
    else:
        if xwing.y_pos <= 3:
            xwing.new_coor(xwing.x_pos,xwing.y_pos+1)
            sleep(500)
        else:
            sense = 'up'
        

