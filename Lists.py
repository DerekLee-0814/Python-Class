from pycat.base.color import Color
from pycat.core import Window, Sprite
from pycat.label import Label
from pyglet import window
from pyglet.image import create
w=Window()

my_list = [
    [3,6,9,12],
    [2,5,8,11],
    [1,4,7,10]
]
print (my_list)

class Cell(Sprite):
    def on_create(self):
        self.height=50
        self.width =90
        self.color=Color.RED

    def create_label(self, value):
        self.value = value
        self.label = w.create_label()
        self.label.text = str(value)
        self.label.x= self.x - self.width/2
        self.label.y= self.y + self.height/2
        print(value)

    def set_color(self,min,max):
        scale=(self.value-min)/(max-min)
        self.color = Color(255, (1-scale) *255,(1-scale) *255)





list_min= list_max = my_list[0][0]
for i in range (3):
    for j in range (4):
        val=my_list[i][j]
        if val < list_min:
            list_min=val
        if val > list_max:
            list_max = val
print (list_min, list_max)


for i in range (3):
    for j in range (4):
        # label = w.create_label()
        # label.text = str(my_list[i][j])
        # label.x = 300 + j * 50
        # label.y = 300  + i * 50
        # print(my_list[i][j],end=' ')
        
        cell = w.create_sprite(Cell)
        cell.x = 300 + j * (cell.width +1)
        cell.y = 300+ i * (cell.height +1)
        cell.create_label(my_list[i][j])
        cell.set_color(list_min, list_max)
        # label.text=str(my_list[i][j])
        

        
w.run()