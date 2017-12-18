
from PIL import ImageDraw

from ..brush import Brush

class PixelBrush(Brush):
  def __init__(self):
    pass

  def paint(self, canvas, coords):
    draw = ImageDraw.Draw(canvas)
    draw.point(coords, (0,0,0))
    return True
