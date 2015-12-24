import pyglet
from pyglet.window import key
from classes import Portal, Ship, Bullet
from functions import *
from globals import *


portal = Portal(portal_image, center_x, center_y, None)

ship = Ship(eoff_image=ship_image,eon_image=ship_image_on,
            die_image=kaboom,
            maxx=window.width,maxy=window.height,
            image=ship_image,
            x=center_x + 300, y = center_y, dx=0, dy=00, rotv=-90,
            batch=None)

altship = Ship(eoff_image=altship_image,eon_image=altship_image_on,
            die_image=kaboom,
            maxx=window.width,maxy=window.height,
            image=altship_image,
            x=center_x - 300, y = center_y, dx=0, dy=00, rotv=-90,
            batch=None)

##altship.thrust=1000000000

score=pyglet.text.Label('Score: 0',font_name='Arial',font_size=16,
                        x=window.width-150,y=10,anchor_x='left',anchor_y='bottom')
score.color=(0,0,255,255)

altscore=pyglet.text.Label('Score: 0',font_name='Arial',font_size=16,
                        x=10,y=10,anchor_x='left',anchor_y='bottom')
altscore.color=(255,0,0,255)

def update(dt):
  ship.update(dt,altship)
  altship.update(dt,ship)
  if ship.deaths + altship.deaths > 11:
    print "Red:  %d" % altship.score
    print "Blue: %d" % ship.score
    if ship.score > altship.score:
      print "Boo hoo! I'm sad"
    pyglet.app.exit()
  
  
pyglet.clock.schedule_interval(update, 1/60.0)

@window.event
def on_draw():
  window.clear()
  portal.draw()
  ship.draw()
  altship.draw()
  bullets.draw()
  score.text="Score: %d" % ship.score
  score.draw()
  altscore.text="Score: %d" % altship.score
  altscore.draw()

@window.event
def on_key_press(symbol, modifiers):
  ## print(symbol)
  if symbol == key.LEFT:
    ship.rot_left = True
  if symbol == key.RIGHT:
    ship.rot_right = True
  if symbol == key.UP:
    ship.engines = True
  if symbol == key.DOWN:
    ship.brakes = True
  if symbol == key.SPACE:
    ship.firing = True
  if symbol == 97: # a
    altship.rot_left = True
  if symbol == 100:  # d
    altship.rot_right = True
  if symbol == 119: # w
    altship.engines = True
  if symbol == 115: # s
    altship.brakes = True
  if symbol == 120 or symbol == 122:
    altship.firing = True
    
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
  if symbol == key.SPACE:
    ship.firing = False
  if symbol == 97: # a
    altship.rot_left = False
  if symbol == 100:  # d
    altship.rot_right = False
  if symbol == 119: # w
    altship.engines = False
  if symbol == 115: # s
    altship.brakes = False
  if symbol == 120 or symbol == 122:
    altship.firing = False

  

pyglet.app.run()
