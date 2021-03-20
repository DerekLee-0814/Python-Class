from random import randint
from pycat.core import Window , KeyCode, Label
from pycat.scheduler import Scheduler 
from pycat.sprite import Sprite
from pyglet.window.key import DELETE
window = Window(enforce_window_limits=False)

class Player (Sprite):
    def on_create(self):
        self.image = "bird.gif"
        self.scale = 0.3
        self.y = window.height/2
        self.x = 150
    def on_update(self, dt):
        self.y -= 1
        if window.is_key_down (KeyCode.SPACE):
            self.y += 40

class Pipe (Sprite):
    def on_create(self):
        self.image = "pipe.png"
        self.x = window.width + self.width/2
        # self.y = randint(0,100)
    def on_update(self, dt):
        self.x -= 4
        if self.x < -self.width/2:
            self.delete ()





def make_pipes():

    bottom_pipe = window.create_sprite(Pipe)
    top_pipe = window.create_sprite(Pipe)
    top_pipe.y = window.height
    top_pipe.rotation = 180
    a=int(bottom_pipe.height/2)
    offset = randint(-a,a)
    bottom_pipe.y += offset
    top_pipe.y += offset
    
    
 

class Score (Label):
    def on_create(self):
        self.text = "Score"
    

Scheduler.update (make_pipes,2)
window.create_sprite(Player)
window.create_label(Score)
window.run()