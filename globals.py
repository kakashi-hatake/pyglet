import pyglet
import math
from functions import *


rbullet_img = pyglet.resource.image('resources/bullet_red.png')
center_anchor(rbullet_img)

bbullet_img = pyglet.resource.image('resources/bullet_blue.png')
center_anchor(bbullet_img)

bullets = pyglet.graphics.Batch()

### Set up main resources (window, images, ...)
window = pyglet.window.Window(fullscreen=True)
pyglet.resource.path.append('./resources')
pyglet.resource.reindex()

portal_image = pyglet.resource.image('portal.jpg')
center_anchor(portal_image)

ship_image = pyglet.resource.image('ship.png')
center_anchor(ship_image)

ship_image_on = pyglet.resource.image('ship_on.png')
center_anchor(ship_image_on)

altship_image = pyglet.resource.image('altship.png')
center_anchor(altship_image)

altship_image_on = pyglet.resource.image('altship_on.png')
center_anchor(altship_image_on)

kaboom = pyglet.resource.image('kaboom.png')
center_anchor(kaboom)

center_x = int(window.width/2)
center_y = int(window.height/2)
