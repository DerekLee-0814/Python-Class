from enum import Enum
import random
from pycat.base.color import Color
from pycat.core import Window
from pycat.sprite import Sprite
from pycat.scheduler import Scheduler
from random import randint, choice

w = Window(enforce_window_limits=False)

fruits_list = ["apples","bananas","kiwis","pears","guavas","grapes","bell-fruits","watermelons","peaches"] 
shapes_list = ["triangles","circles","rectangles","squares","trapezoids","ovals","parallelograms","semi-cirlces","pyramids","cubes"]
color_list = ["purple","green","grey","black","blue","yellow","cyan","lime","magenta","pink","red"]
words = fruits_list+shapes_list+color_list

class State (Enum):
    FRUITS = 0
    SHAPES = 1
    COLORS = 2


state_list = [State.FRUITS, State.COLORS, State.SHAPES]

state = choice(state_list)

class Word (Sprite):
    def on_create(self):
        self.color= Color.PURPLE
        self.label = w.create_label()

    def setup (self, x, y, text):
        self.label.text = text
        self.width = self.label.content_width
        self.height = self.label.content_height
        self.x = x
        self.y = y
        self.label.x = x - self.width/2
        self.label.y = y + self.height/2
    def on_update(self,dt):
        self.y -= 2
        self.label.y  -=2
        if self.label.y < 0:
            self.delete() 
            self.label.delete()
    def on_left_click(self):



        self.delete() 
        self.label.delete()


def create_words():
    word = w.create_sprite (Word)
    word.setup(random.randint(10,w.width),w.height,random.choice(words))

Scheduler.update(create_words, delay=0.3)

def changestate(dt):
    global state
    state = choice(state_list)
    print (str(state))


Scheduler.update(changestate, delay=4)




w.run()


