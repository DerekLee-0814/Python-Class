from pycat.core import Window, Sprite
from typing import List
from random import randint

window = Window()


class Turtle(Sprite):
    def on_create(self):
        self.is_visible = False

    def draw_forward(self, distance):
        x = self.x
        y = self.y
        self.move_forward(distance)
        window.create_line(x, y, self.x, self.y)

    def draw_rectangle(self, width, height):
        for _ in range(4):
            turtle.draw_forward(width)
            turtle.rotation += 90
            turtle.draw_forward(height)
            turtle.rotation += 90

class WindowsRect:
    def __init__(self, start_x, start_y, width, height):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height

    def draw(self, turtle: Turtle):
        turtle.x = self.start_x
        turtle.y = self.start_y
        turtle.draw_rectangle(self.width, self.height)


class Building:
    def __init__(self, start_x, start_y, width, height):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height
        self.windows = [[WindowsRect(x,y,11,11) 
                        for y in range (self.start_y-10,self.start_y-10+self.height,35)
                        for x in range (self.start_x+11,self.start_x+self.width-20,35)]
                        ]

    def draw(self, turtle: Turtle):
        turtle.x = self.start_x
        turtle.y = self.start_y
        turtle.draw_rectangle(self.width, self.height)
        for rows in self.windows:
            for w in rows:
                w.draw(turtle)




turtle = window.create_sprite(Turtle)
rect_list:List[Building]=[]
for i in range (10):
    x=i*200
    y=1
    r = Building(x,y,randint(100,200),randint(100,600))
    rect_list.append(r)
for r in rect_list:
    r.draw(turtle)



window.run()