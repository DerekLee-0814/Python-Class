from pycat.base.color import Color
from pycat.core import (Window)
from pycat.sprite import Sprite
w= Window()
my_list = []


PIXEL_SIZE = 100


class Pixel(Sprite):    
    def on_create(self):
        self.scale = PIXEL_SIZE
        self.color = Color.AZURE

for i in range (len(my_list)):
    for j in range (len(my_list[i])):
        s = w.create_sprite(Pixel)
        s.x = PIXEL_SIZE/2
        s.y = w.height-PIXEL_SIZE/2
        
        
        



w.run()
