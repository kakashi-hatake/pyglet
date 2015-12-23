import pyglet
from pyglet.window import key
from classes import Portal, Ship, Bullet
from functions import *

### Set up main resources (window, images, ...)
window = pyglet.window.Window(fullscreen=False)
pyglet.resource.path.append('./resources')
pyglet.resource.reindex()

portal_image = pyglet.resource.image('portal.jpg')
center_anchor(portal_image)

ship_image = pyglet.resource.image('ship.png')
center_anchor(ship_image)

ship_image_on = pyglet.resource.image('ship_on.png')
center_anchor(ship_image_on)

kaboom = pyglet.resource.image('kaboom.png')
center_anchor(kaboom)

bullet_img = pyglet.resource.image('bullet.png')
center_anchor(bullet_img)

center_x = int(window.width/2)
center_y = int(window.height/2)

portal = Portal(portal_image, center_x, center_y, None)

ship = Ship(eoff_image=ship_image,eon_image=ship_image_on,
            die_image=kaboom,
            maxx=window.width,maxy=window.height,
            image=ship_image,
            x=center_x + 300, y = center_y, dx=0, dy=00, rotv=-90,
            batch=None)

#bullet=Bullet(bullet_img,x=center_x + 300, y=center_y+50,rotv=-90)

def update(dt):
  ship.update(dt)
  
pyglet.clock.schedule_interval(update, 1/60.0)

@window.event
def on_draw():
  window.clear()
  portal.draw()
  ship.draw()
 # bullet.draw()

@window.event
def on_key_press(symbol, modifiers):
  if symbol == key.LEFT:
    ship.rot_left = True
  if symbol == key.RIGHT:
    ship.rot_right = True
  if symbol == key.UP:
    ship.engines = True
  if symbol == key.DOWN:
    ship.brakes = True
    
@window.event
def on_key_release(symbol, modifiers):
  if symbol == key.LEFT:
    ship.rot_left = False
  if symbol == key.RIGHT:
    ship.rot_right = False
  if symbol == key.UP:
    ship.engines = False
  if symbol == key.DOWN:
    ship.brakes = False

  

pyglet.app.run()
