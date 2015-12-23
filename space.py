import pyglet

window = pyglet.window.Window(fullscreen=False)
pyglet.resource.path.append('./resources')
pyglet.resource.reindex()

def center_anchor(img):
  img.anchor_x = img.width // 2 ## "//" is the integer division function
  img.anchor_y = img.height // 2

portal_image = pyglet.resource.image('portal.jpg')
center_anchor(portal_image)

class Portal(pyglet.sprite.Sprite):
  def __init__(self, image, x=0, y=0, batch=None):
    super(Portal,self).__init__(image, x, y,batch=batch)
    self.x = x
    self.y = y

center_x = int(window.width/2)
center_y = int(window.height/2)
portal = Portal(portal_image, center_x, center_y, None)

@window.event
def on_draw():
  window.clear()
  portal.draw()


pyglet.app.run()
