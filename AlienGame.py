from sys import platform
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window, Sprite
from enum import Enum,auto
window = Window(background_image="Game.Background.jpg")
window.background_sprite.scale=1.3

class OwlState(Enum):
    WAIT = auto()
    JUMP = auto()
    RESET = auto()

class Owl (Sprite):    
    def on_create(self):
        self.image="owl-a.png"
        self.x = 300
        self.y = 320
        self.scale = 0.6
        self.x_speed = 0
        self.y_speed = 0
        self.state = OwlState.WAIT

    def on_click_anywhere(self, mouse_event: MouseEvent):
        cursor_dist_x = mouse_event.position.x - self.x
        cursor_dist_y = mouse_event.position.y - self.y
        if self.state == OwlState.WAIT:
            self.x_speed = cursor_dist_x * 0.05
            self.y_speed = cursor_dist_y * 0.05
            self.state = OwlState.JUMP
            
    def on_update(self, dt):
        if self.state == OwlState.JUMP:
            self.x += self.x_speed
            self.y += self.y_speed
            self.y_speed -= 1  
            if self.is_touching_any_sprite_with_tag('platform'):
                self.state = OwlState.WAIT

class Platform (Sprite):
    def on_create(self):
        self.image = "building-a.png"
        self.scale = 0.5
        


class Enemy (Sprite):
    def on_create(self):
        self.image = "frank-a.png"
        self.x = 1200
        self.y = 200
        self.scale = 0.5

class PlatformTop1(Sprite):
    def on_create(self):
        self.x= 640
        self.y= 440
        self.height = 1
        self.width = 210
        self.add_tag('platform')
        


window.create_sprite (Enemy)
window.create_sprite (Platform,x=300,y=250)
window.create_sprite (PlatformTop1)
window.create_sprite (Platform,x=640,y=400)
window.create_sprite (Platform,x=960,y=190)
window.create_sprite(Owl)

window.run()