import pyglet

class Portal(pyglet.sprite.Sprite):
  def __init__(self, image, x=0, y=0, batch=None):
    super(Portal,self).__init__(image, x, y,batch=batch)
    self.x = x
    self.y = y


class Ship(pyglet.sprite.Sprite):
  def __init__(self, image, x=0, y=0,
               dx=0, dy=0, rotv=0, batch=None):
    super(Ship, self).__init__(image, x, y, batch=batch)
    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy
    self.rotation = rotv
    self.thrust = 200.0
    self.rot_spd = 100.0

    
