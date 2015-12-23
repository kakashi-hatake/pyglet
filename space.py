import pyglet
from classes import Portal, Ship


window = pyglet.window.Window(fullscreen=True)
pyglet.resource.path.append('./resources')
pyglet.resource.reindex()

def center_anchor(img):
  img.anchor_x = img.width // 2 ## "//" is the integer division function
  img.anchor_y = img.height // 2

portal_image = pyglet.resource.image('portal.jpg')
center_anchor(portal_image)

ship_image = pyglet.resource.image('ship.png')
center_anchor(ship_image)

center_x = int(window.width/2)
center_y = int(window.height/2)

portal = Portal(portal_image, center_x, center_y, None)

ship = Ship(ship_image,
            x=center_x + 300, y = center_y, dx=0, dy=150, rotv=0)


@window.event
def on_draw():
  window.clear()
  portal.draw()
  ship.draw()

pyglet.app.run()
