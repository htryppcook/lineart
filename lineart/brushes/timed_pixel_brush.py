
import random
from PIL import ImageDraw

from ..brush import Brush

class TimedPixelBrush(Brush):
  def __init__(self):
    self.count = 0
    self.max = random.randrange(0,100)
    self.last = None
    self.offsets = (
      (-1,-1), (0,-1), (1,-1),
      (-1, 0),         (1, 0),
      (-1, 1), (0, 1), (1, 1)
    )
    self.background = (255,255,255)
    self.foreground = (0,0,0)
    self.outline    = (0,0,255)

  def paint(self, image, coords):
    if self.count >= self.max:
      self.last = None
      return False

    draw = ImageDraw.Draw(image)
    draw.point(coords, self.foreground)
    #self.outline_point(draw, image, coords)

    self.last = coords
    self.count += 1
    return True

  def outline_point(self, draw, image, coords):
    for offset in self.offsets:
      new_coords = (coords[0]+offset[0], coords[1]+offset[1])
      if new_coords[0] <= 1 or new_coords[0] >= image.width-1 \
         or new_coords[1] <= 1 or new_coords[1] >= image.height-1:
        continue
      pixel = image.getpixel(new_coords)
      if pixel == self.background:
        draw.point(new_coords, self.outline)
