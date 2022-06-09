from microbit import *
import utime

class space_object:
    def __init__(self, x, y, b):
        self.x_pos = x
        self.y_pos = y
        self.bright = b
        self.location = [self.x_pos,self.y_pos,self.bright]
    
    def get_coor(self):
        return self.location

    def new_coor(self,x,y):
        display.set_pixel(self.x_pos,self.y_pos,0)
        self.x_pos = x
        self.y_pos = y
        self.set_coor()
    
    def set_coor(self):
        display.set_pixel(self.x_pos,self.y_pos,self.bright)

    def x_nav(self,seconds):
        mb_time = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(),mb_time) < seconds*1000:
            if button_a.is_pressed():
                if self.x_pos >= 1:
                    self.new_coor(self.x_pos-1,self.y_pos)
                    sleep(100)
            
            if button_b.is_pressed():
                if self.x_pos <= 3:
                    self.new_coor(self.x_pos+1,self.y_pos)
                    sleep(100)

    def attack(self):
        self.new_coor(self.x_pos,self.y_pos+1)

    def off(self):
        self.bright = 0
        self.set_coor()
            

        