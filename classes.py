import pyglet
import math
from functions import *

class Portal(pyglet.sprite.Sprite):
  def __init__(self, image, x=0, y=0, batch=None):
    super(Portal,self).__init__(image, x, y,batch=batch)
    self.x = x
    self.y = y



class Bullet(pyglet.sprite.Sprite):
  def __init__(self, image, x=0, y=0, rotv=0, batch=None):
    super(Bullet,self).__init__(image, x, y,batch=batch)
    self.x = x
    self.y = y
    self.rotation = rotv


class Ship(pyglet.sprite.Sprite):
  def __init__(self,eoff_image,eon_image,die_image,
               maxx,maxy,
               image, x=0, y=0,
               dx=0, dy=0, rotv=0, batch=None):               
    super(Ship, self).__init__(image, x, y, batch=batch)
    self.eoff_image=eoff_image
    self.eon_image=eon_image
    self.maxx=maxx
    self.maxy=maxy
    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy
    self.rotation = rotv
    self.engines = False
    self.brakes = False
    self.thrust = 200.0
    self.friction = 0.005 ## percent drop in speed per dt
    self.brake_power = 0.01 ## percent drop in speed per dt when brakes are on
    self.rot_spd = 100.0
    self.rot_left = False
    self.rot_right = False

  def update(self, dt):
    self.image = self.eoff_image
    if self.rot_left:
      self.rotation -= self.rot_spd * dt
    if self.rot_right:
      self.rotation += self.rot_spd * dt
    self.rotation = wrap(self.rotation, 360.0)
    accelx = math.cos(to_radians(self.rotation))
    accely = math.sin(to_radians(-self.rotation))
    ## ## friction slows the ship
    self.dx = self.dx * (1.0 - self.friction)
    self.dy = self.dy * (1.0 - self.friction)
    ## engines speed the ship
    if self.engines:
      self.image = self.eon_image
      self.dx += self.thrust * accelx * dt
      self.dy += self.thrust * accely * dt
    if self.brakes:
      self.dx = self.dx * (1.0 - self.brake_power)
      self.dy = self.dy * (1.0 - self.brake_power)
    self.x += self.dx *dt
    self.y += self.dy *dt
    self.x = wrap(self.x, self.maxx)
    self.y = wrap(self.y, self.maxy)
    print("{0:.3f} {1:.3f} {2:.3f} {3:.3f}".format(*(self.dx,self.dy,self.x,self.y)))

    



      
