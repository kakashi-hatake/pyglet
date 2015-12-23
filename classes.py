import pyglet
import math
from functions import *

class Portal(pyglet.sprite.Sprite):
  def __init__(self, image, x=0, y=0, batch=None):
    super(Portal,self).__init__(image, x, y,batch=batch)
    self.x = x
    self.y = y


class Ship(pyglet.sprite.Sprite):
  def __init__(self,eoff_image,eon_image,
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
    self.friction = 10.0
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
    ## fricx = self.friction * accelx * dt
    ## fricy = self.friction * accely * dt
    ## if(self.dx > 0):
    ##   self.dx -= min(fricx,self.dx)
    ## else:
    ##   self.dx += min(fricx,self.dx)
    ## #if(self.dy > 0):
    ## #  self.dy -= min(fricy,self.dy)
    ## #else:
    ## #  self.dy += min(fricy,self.dy)
    if self.engines:
      self.image = self.eon_image
      self.dx += self.thrust * accelx * dt
      self.dy += self.thrust * accely * dt
    if self.brakes:
      self.dx -= self.thrust * accelx * dt * 0.5
      self.dy -= self.thrust * accely * dt * 0.5
    self.x += self.dx *dt
    self.y += self.dy *dt
    self.x = wrap(self.x, self.maxx)
    self.y = wrap(self.y, self.maxy)
    print("{0:.3f} {1:.3f} {2:.3f} {3:.3f}".format(*(self.dx,self.dy,self.x,self.y)))

    



      
