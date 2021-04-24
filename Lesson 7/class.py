from math import sqrt
from pycat.core import Window
from pycat.geometry.point import Point
w= Window() 
point_a = Point(100,200)
point_b = Point(300,200)
c = point_b.x-point_a.x
a = c/2
b = sqrt(c**2-a**2)

point_c = (point_a+point_b)/2
point_c.y += b

w.create_line(point_a.x,point_a.y,point_b.x,point_b.y)
w.create_line(point_b.x,point_b.y,point_c.x,point_c.y)
w.create_line(point_c.x,point_c.y,point_a.x,point_a.y)
w.run()