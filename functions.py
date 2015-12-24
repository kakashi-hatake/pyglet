import math

def center_anchor(img):
  img.anchor_x = img.width // 2 ## "//" is the integer division function
  img.anchor_y = img.height // 2

def wrap(value, width):
  if width == 0:
    return 0
  if value > width:
    value -=width
  if value < 0:
    value += width
  return value

def to_radians(degrees):
  return math.pi * degrees / 180.0


def distance_to(source, target):
  dx=source.x-target.x
  dy=source.y-target.y
  return math.sqrt(dx**2 + dy**2)
