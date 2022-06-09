# Asteroid Field
# CPA 2022

from asteriod import *

while True:

    if button_a.was_pressed():
       
        lifes_count = 3
        level = 0
        start_msg()
        life_set(lifes_count)
        ship_set(2)
        #while lifes_count > 0:
        
    elif button_b.was_pressed():
       life_set(0)
       stop_msg()
    

