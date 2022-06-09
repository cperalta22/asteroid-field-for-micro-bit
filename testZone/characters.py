from microbit import *

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

        