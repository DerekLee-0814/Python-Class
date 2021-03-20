from pycat.core import Sprite, Window
import random

from pyglet.image import create


class Particle(Sprite):

    def on_create(self):
        self.add_tag('particle')
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale = 5

    def on_update(self, dt):
        self.move_forward(5)
        if self.touching_window_edge():
            self.rotation += 180


class CreateButton(Sprite):
    def on_create(self):
        self.scale = 100

    def on_left_click(self):
        window.create_sprite (Particle)



class TimedExplosionParticle(Sprite):
    def on_create(self):
        self.timer = 0
        self.scale = 2
        

    def on_update(self, dt):
        self.timer += dt
        self.move_forward(5)
        if self.timer > 1:
            self.delete()
        
window = Window()

class ExplosionButton(Sprite):
    def on_create(self):
        self.scale = 100

    def on_left_click(self):
        my_list = window.get_sprites_with_tag ('particle')
        for p in my_list :
            for i in range (20):
                q = window.create_sprite (TimedExplosionParticle)
                q.position = p.position
                q.rotation = random.randint (0,360)
            p.delete()

bluebutton = window.create_sprite(CreateButton)
bluebutton.x = 100
bluebutton.y = 150
bluebutton.color = (0,0,255 )
redbutton = window.create_sprite(ExplosionButton)
redbutton.x = 280
redbutton.y = 150
redbutton.color = (255,0,0)

window.run()
