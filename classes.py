import pyglet
import math
import random
from functions import *
from globals import *

class Portal(pyglet.sprite.Sprite):
  def __init__(self, image, x=0, y=0, batch=None):
    super(Portal,self).__init__(image, x, y,batch=batch)
    self.x = x
    self.y = y


class Bullet(pyglet.sprite.Sprite):
  def __init__(self, x=0, y=0, dx=0, dy=0, rotv=0, batch=bullets):
    super(Bullet,self).__init__(rbullet_img, x, y,batch=batch)
    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy
    self.rotation = rotv
    self.radius = self.image.width / 2
    self.timer = 1.0
    ##print(self.dx,self.dy)

  def hits(self,target):
    if distance_to(self,target) < target.radius:
      return True
    return False
    
  def update(self, dt):
    self.x = wrap(self.x + self.dx * dt, window.width)
    self.y = wrap(self.y + self.dy * dt, window.height)
    self.timer -= dt

## TODO!! Check if bullet hit anything!

class Ship(pyglet.sprite.Sprite):
  def __init__(self,eoff_image,eon_image,die_image,
               maxx,maxy,
               image, x=0, y=0,
               dx=0, dy=0, rotv=0, batch=None):               
    super(Ship, self).__init__(image, x, y, batch=batch)
    self.eoff_image=eoff_image
    self.eon_image=eon_image
    self.die_image=die_image
    self.maxx=maxx
    self.maxy=maxy
    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy
    self.rotation = rotv
    self.engines = False
    self.brakes = False
    self.rot_left = False
    self.rot_right = False
    self.firing = False
    self.bullets = []
    self.alive = True
    self.lifetimer=2.0
    self.radius = max(self.image.width,self.image.height) /2
    self.thrust = 500.0
    self.friction = 0.005 ## percent drop in speed per dt
    self.brake_power = 0.01 ## percent drop in speed per dt when brakes are on
    self.rot_spd = 200.0
    self.maxdamage=50
    self.deaths=0
    self.damage=self.maxdamage
    self.score = 0
    self.shot_timer = 0.1
    self.reload_timer = self.shot_timer

  def reset(self):
    self.alive=True
    self.lifetimer=2.0
    self.x=random.random()*self.maxx
    self.y=random.random()*self.maxy
    self.dx=0
    self.dy=0
    self.image=self.eoff_image
    self.thrust += 500
    self.rot_spd += 100
    self.maxdamage +=10
    self.damage=self.maxdamage
    
  def update(self, dt, target):
    if not self.alive:
      self.image=self.die_image
      self.lifetimer -= dt
      if self.lifetimer > 0:
        return
      else:
        self.reset()
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
    #print("{0:.3f} {1:.3f} {2:.3f} {3:.3f}".format(*(self.dx,self.dy,self.x,self.y)))
    if self.reload_timer > 0:
      self.reload_timer -= dt
    elif self.firing:
      self.bullets.append(Bullet(self.x+(45*accelx), self.y+(45*accely),
                                accelx*1000+self.dx,
                                accely*1000+self.dy,
                                self.rotation))
      self.reload_timer = self.shot_timer
      self.score -=1
    for b in self.bullets:
      b.update(dt)
      if b.timer < 0:
        self.bullets.remove(b)
      if b.hits(target):
        self.score += 5
        target.damage -= 10
        if target.damage<0:
          self.score += 100
        self.bullets.remove(b)
    if self.score < 0:
      self.score = 0
    if self.damage<0:
      self.alive=False
      self.deaths += 1
      for b in self.bullets:
        self.bullets.remove(b)

      
 
