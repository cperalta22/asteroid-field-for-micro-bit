from microbit import *
import utime
import music

class space_object:
    def __init__(self, x, y, b):
        self.x_pos = x
        self.y_pos = y
        self.bright = b
    
    def new_coor(self,x,y):
        display.set_pixel(self.x_pos,self.y_pos,0)
        self.x_pos = x
        self.y_pos = y
        self.set_coor()
    
    def set_coor(self):
        display.set_pixel(self.x_pos,self.y_pos,self.bright)

    def action(self,seconds,ammo):
        mb_time = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(),mb_time) < seconds*1000:
            if pin1.is_touched():
                if self.x_pos >= 1:
                    self.new_coor(self.x_pos-1,self.y_pos)
                    sleep(100)
                else:
                    music.play(music.BA_DING,wait=False)
            
            if pin2.is_touched():
                if self.x_pos <= 3:
                    self.new_coor(self.x_pos+1,self.y_pos)
                    sleep(100)
                else:
                    music.play(music.BA_DING,wait=False)
                    
            if button_b.is_pressed() and ammo is True:
                break
                


    def attack(self):
        self.new_coor(self.x_pos,self.y_pos+1)

    def off(self):
        self.bright = 0
        self.set_coor()

    def to_zeros(self):
        self.bright = 0
        self.x_pos = 0
        self.y_pos = 0
        self.set_coor()
                    

        