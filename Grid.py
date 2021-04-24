from functools import reduce
from random import randint
from typing import List
from pycat.base import color
from pycat.core import Window,Sprite,Color
from pyglet.image import create

ROWS=8
COLS=12
CELL_SIZE = 100
w=Window(width= COLS * CELL_SIZE,height=ROWS*CELL_SIZE)



class Cell (Sprite):
    def on_create(self):
        self.color = Color.WHITE
        self.scale = CELL_SIZE-1
    def setij (self,i,j):
        self.i = i
        self.j = j
        
    def toggle (self):
        if self.color == Color.RED:
            self.color = Color.WHITE
        else:
            self.color = Color.RED
    def change_neighbor_color(self):
        i = self.i
        j = self.j
        if i+1 < ROWS:
            grid[i+1][j].toggle()
        if i-1 >= 0:
            grid[i-1][j].toggle()
        if j+1 < COLS:
            grid[i][j+1].toggle()
        if j-1 >= 0:
            grid[i][j-1].toggle()


    def on_left_click(self):
        self.change_neighbor_color()
        self.check_for_win()
        
    def check_for_win(self):
        for i in range (ROWS):
            for j in range (COLS):
                if grid[i][j].color == Color.RED:
                    return
        print ('You Win!')

grid: List[List[Cell]] = []
for i in range (ROWS):
    row = []
    for j in range (COLS):     
        create_cell = w.create_sprite(Cell)
        create_cell.x = j*CELL_SIZE+CELL_SIZE/2
        create_cell.y = i*CELL_SIZE+CELL_SIZE/2
        create_cell.setij(i, j)
        row.append(create_cell)
    grid.append(row)

for _ in range (7):
    i = randint (0, ROWS-1)
    j = randint (0, COLS-1)
    grid[i][j].change_neighbor_color()

grid[2][5].change_neighbor_color()
w.run()