from pycat.base.color import Color
from pycat.core import Window,Sprite
from random import choice, random
from pyglet import window

from pyglet.gl.glext_arb import PFNGLVARIANTBVEXTPROC
from pyglet.image import create

WIDTH =500 
HEIGHT=700
w= Window(width=WIDTH, height=HEIGHT)
BUTTONSIZE = 54
GAP = 40
GAPYSIZE = 160
BUTTONAMOUNT = 4

class ColorButton(Sprite):
    current_color=None
    def on_create(self):
        self.scale=BUTTONSIZE
        self.x = BUTTONSIZE/2 + GAP
        self.y = BUTTONSIZE
    def on_left_click(self):
        ColorButton.current_color = self.color


def is_match():
    for i in range (BUTTONAMOUNT-1):
        if code_list[i].color!=guess_list[i].color:
            return False
    return True

def win():
    print('you win')

def lose():
    print('try again')

def guess_amount():
    pass
  
def create_new_row(guess):
    guess_list.clear()
    for i in range(BUTTONAMOUNT):
        c = w.create_sprite(ColorChoice)
        c.x +=(GAP+BUTTONSIZE)*i
        c.y += guess*(5+BUTTONSIZE)
        guess_list.append(c)

def draw_pegs(red_pegs, guess):
    print(red_pegs)
    print(guess)
    for i in range (red_pegs):
        r = w.create_sprite()
        r.scale = 12
        r.x = w.width - r.scale - i * (3+r.scale)                                                                                                          
        r.y=BUTTONSIZE*2.5
        r.y += guess*(5+BUTTONSIZE)
        r.color = Color.RED

        
class CheckButton(Sprite):
    def on_create(self):
        self.scale = BUTTONSIZE/2 
        self.x = BUTTONSIZE*BUTTONAMOUNT + GAP*(BUTTONAMOUNT+1)+self.scale/2
        self.color = Color.WHITE
        self.y = BUTTONSIZE
        self.guess = 0
        self.red_pegs= 0


    def get_score(self):
        self.red_pegs= 0
        for i in range (BUTTONAMOUNT):
            if code_list[i].color == guess_list[i].color:
                self.red_pegs += 1
        print (self.red_pegs)
    def on_left_click(self):
        self.get_score()
        draw_pegs(self.red_pegs,self.guess)
        if is_match():
            win()
        else: 
            if self.guess > 8 :
                lose()
            self.guess += 1
            create_new_row(self.guess)


colorlist = [Color.RED, Color.GREEN, Color.BLUE, Color.PURPLE]

class ColorCode(Sprite):
    def on_create(self):
        self.scale=BUTTONSIZE
        self.x = BUTTONSIZE/2 + GAP
        self.y = w.height - BUTTONSIZE


class ColorChoice (Sprite):
    def on_create(self):
        self.scale=BUTTONSIZE
        self.x = BUTTONSIZE/2 + GAP
        self.y = BUTTONSIZE*2.5  
        self.color = Color.WHITE

    def on_left_click(self):
        if ColorButton.current_color:
            self.color = ColorButton.current_color


code_list =[]



guess_list=[]


for i in range(BUTTONAMOUNT):
    c = w.create_sprite(ColorCode)
    c.color = choice(colorlist)
    c.x +=(GAP+BUTTONSIZE)*i
    code_list.append(c)

for i in range(BUTTONAMOUNT):
    c = w.create_sprite(ColorButton)
    c.color = colorlist[i]
    c.x +=(GAP+BUTTONSIZE)*i
    

for i in range(BUTTONAMOUNT):
    c = w.create_sprite(ColorChoice)
    c.x +=(GAP+BUTTONSIZE)*i
    guess_list.append(c)
# def code_list(self):
#     for i in range (BUTTONAMOUNT-1):
#         self.


w.create_sprite (CheckButton)

w.run()