
from PIL import ImageDraw

from ..brush import Brush

class PixelBrush(Brush):
    ''' A brush that paints a single pixel at a time. '''

    def paint(self, canvas, coords):
        draw = ImageDraw.Draw(canvas)
        draw.point(coords, (0, 0, 0))
        return True
