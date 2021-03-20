from inspect import istraceback
from pycat.base.base_sprite import RotationMode
from pycat.base.event.mouse_event import MouseButton, MouseEvent
from pycat.core import Color, KeyCode,Scheduler, Sprite, Window
import random
from pyglet import image

from pyglet.gl.glext_arb import GL_AMD_name_gen_delete, GL_VERTEX_WEIGHT_ARRAY_EXT
from pyglet.gl.glu import GLU_DOMAIN_DISTANCE
from pyglet.window.key import DELETE 
window = Window()


class Player(Sprite):

    def on_create(self):
        self.scale = .3
        self.speed = 10
        self.x = 100
        self.y = 50
        self.is_melee_active = False
        self.health = 100
        self.image = "GunMan.png"

    def on_update(self, dt):
        if player.health > 0:
            if window.get_key(KeyCode.W):
                self.y += self.speed
            # fill in code for keys A, S, D
            if window.get_key(KeyCode.D):
                self.x += self.speed
            if window.get_key(KeyCode.S):
                self.y -= self.speed
            if window.get_key(KeyCode.A):
                self.x -= self.speed
                
            
        
    def on_left_click_anywhere(self):
        if player.health > 0:
            window.create_sprite(Bullet)

    def on_click_anywhere(self, mouse_event: MouseEvent):
        if player.health > 0:
            if mouse_event.button == MouseButton.RIGHT:
                window.create_sprite(Melee)
            # if self.is_melee_active == False:
            #     Scheduler.update(spawn_melee,5)
            #     self.is_melee_active = True
                
player: Player = window.create_sprite(Player)           


class Restart_Button(Sprite):
    def on_create(self):
        self.image = 'reset.png'
        self.scale = 20
        self.x = 650
        self.y = 275

    def on_click_anywhere():  
        player.health = 100

class Player_Health(Sprite):
    def on_create(self):
        self.color = Color.GREEN
        self.scale_y = 20
        self.scale_x = 500
        self.x = 650
        self.y = 600
    def on_update(self, dt):
        self.scale_x = -5 * player.health
        if player.health <= 0:
            self.delete()
        if player.health <= 0:
            print("You Died,Restart?")
            player.scale= 0.5
            player.image = "death.png"
            player.x = 650
            player.y = 350
            Scheduler.cancel_update(spawn_shotgun)
            Scheduler.cancel_update(spawn_rifle)
            Scheduler.cancel_update(spawn_sniper)
            window.create_sprite(Restart_Button)
window.create_sprite(Player_Health)
     

class Restart_Button(Sprite):
    def on_create(self):
        self.image = 'reset.png'
        self.scale = .2
        self.x = 650
        self.y = 235

    def on_left_click (self):
        player.health = 100
        print ("check")
        
class Bullet (Sprite):

    def on_create(self):
        self.scale = .1
        self.position = player.position
        self.speed = 20
        self.point_toward_mouse_cursor()
        self.add_tag('bullet')
        self.image = "bulit.png"
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()

class Melee (Sprite):

    def on_create(self):
        self.opacity = 100
        self.scale = 1
        self.position = player.position
        self.add_tag ('MeleeDamage')

    def on_update(self, dt):
        self.position = player.position
        if self.scale < 200:
            self.scale += 7
            
        else: 
            self.delete()           

     


class RifleEnemy(Sprite):

    def on_create(self):
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale = .3
        self.speed = 5
        self.time = 0
        self.image = "pistol.png"
        


    def on_update(self,dt):
        self.time += dt 
        self.move_forward(self.speed)
        self.point_toward(player.position)
        if self.touching_window_edge():
            self.delete()
        if self.touching_any_sprite_with_tag('bullet'):
            self.delete()
        if self.touching_any_sprite_with_tag('MeleeDamage'):
            self.delete()
        if self.time > 1 :
            bullet = window.create_sprite(RifleAmmo)
            bullet.position = self.position
            bullet.point_toward_sprite (player)
            self.time = 0
        if player.health <= 0:
            self.delete()
        if self.touching_sprite(player):
            player.health -= .1

class RifleAmmo(Sprite):
    
    def on_create(self):
            self.scale = .07
            self.speed = 10
            self.add_tag('RifleDamage')
            
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()
        if self.touching_sprite(player):
            player.health -= 10
            print(player.health)
            self.delete()
        if self.touching_any_sprite_with_tag('MeleeDamage'):
            self.delete()            
        self.image = "Pistol123.png"

  
class SniperEnemy(Sprite):
                                                                                                                                               
    def on_create(self):
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale = .5
        self.speed = 2
        self.time = 0
        self.image = "Sniperman.png"
    def on_update(self,dt):
        self.time += dt 
        self.move_forward(self.speed)
        self.point_toward(player.position)
        if self.touching_window_edge():
            self.delete()

        if self.touching_any_sprite_with_tag('bullet'):
            self.delete()
        if self.touching_any_sprite_with_tag('MeleeDamage'):
            self.delete()
        if self.time > 2.5 :
            bullet = window.create_sprite(SniperAmmo)
            bullet.position = self.position
            bullet.point_toward_sprite (player)
            self.time = 0
        if player.health <= 0:
            self.delete()
        if self.touching_sprite(player):
            player.health -= .1
        
        
        
class SniperAmmo(Sprite):
    def on_create(self):
            self.color = Color.CHARTREUSE
            self.scale = .08
            self.speed = 15
            self.image = "Picture1.png"          
    def on_update(self, dt):
        self.move_forward(self.speed)
        self.point_toward(player.position)
        if self.touching_window_edge():
            self.delete()
        if self.touching_sprite(player):
            player.health -= 40
            print(player.health)
        if self.touching_sprite(player):
            self.delete()
        if self.touching_any_sprite_with_tag('MeleeDamage'):
            self.delete()


class ShotgunEnemy(Sprite):
    def fire_shotgun1(self):
        # rotation_list=[10,7.5,5,2.5,0,-2.5,-5,-7.5,-10]
        rotation_list=list(range(-10, 11, 2))
        for r in rotation_list:
            
            b = window.create_sprite(ShotgunAmmo)
            b.position = self.position
            b.point_toward_sprite(player)
            b.rotation += r 
 
    def on_create(self):
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale = .3
        self.speed = 8
        self.time = 2
        self.image = "shotgunmanv2.png"

    def on_update(self,dt):
        self.time += dt 
        self.move_forward(self.speed)
        self.point_toward(player.position)
        if self.touching_window_edge():
            self.delete()
        if self.touching_any_sprite_with_tag('bullet'):
            self.delete()
        if self.touching_any_sprite_with_tag('MeleeDamage'):
            self.delete()
        if self.time > 2 :
            self.fire_shotgun1()
            self.time = 0
        if player.health <= 0:
            self.delete()
        if self.touching_sprite(player):
            player.health -= .1
            
class ShotgunAmmo (Sprite):
    def on_create(self):
            self.scale = .05
            self.speed = 10
            
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()
        if self.touching_sprite(player):
            player.health -= 4
            print(player.health)
        if self.touching_sprite(player):
            self.delete()
        if self.touching_any_sprite_with_tag('MeleeDamage'):
            self.delete()
        if player.health <= 0:
            self.delete()
        self.image = "sho.png"
def spawn_rifle(dt):
    window.create_sprite(RifleEnemy)
Scheduler.update(spawn_rifle, delay= 2)


def spawn_sniper(dt):
    window.create_sprite(SniperEnemy)
Scheduler.update(spawn_sniper,delay= 4)

def spawn_shotgun(dt):
    window.create_sprite(ShotgunEnemy)
Scheduler.update(spawn_shotgun,delay= 6)

def spawn_melee():
    window.create_sprite(Melee)
# Scheduler.update(spawn_melee,delay=5)

window.run()

