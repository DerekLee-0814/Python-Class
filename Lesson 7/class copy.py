from math import sqrt
from pycat.core import Window, Sprite
from pycat.geometry.point import Point
w= Window() 
# point_a = Point(100,200)
# point_b = Point(300,200)
# c = point_b.x-point_a.x
# a = c/2
# b = sqrt(c**2-a**2)
# point_c = (point_a+point_b)/2
# point_c.y += b

# w.create_line(point_a.x,point_a.y,point_b.x,point_b.y)
# w.create_line(point_b.x,point_b.y,point_c.x,point_c.y)
# w.create_line(point_c.x,point_c.y,point_a.x,point_a.y)

class Turtle(Sprite):
    def on_create(self):
        pass

    def create_triangle(self, length):
        a = self.position
        self.move_forward(length)
        b = self.position
        self.rotation += 120
        self.move_forward(length)
        c = self.position

        w.create_line(a.x, a.y, b.x ,b.y)
        w.create_line(b.x, b.y, c.x,c.y)
        w.create_line(c.x,c.y, a.x,a.y)


t = w.create_sprite(Turtle)
t.position = w.center

for i in range(100):
    t.position = w.center
    t.rotation += 5
    t.create_triangle(i*4)


w.run()