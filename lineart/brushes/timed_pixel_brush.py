
import random
from PIL import ImageDraw

from ..brush import Brush

class TimedPixelBrush(Brush):
    ''' PixelBrush that draws a specified number of pixels and no more. '''
    def __init__(self):
        self.count = 0
        self.max = random.randrange(0, 100)
        self.last = None
        self.foreground = (0, 0, 0)
        self.outline = (0, 0, 255)

    def paint(self, image, coords):
        if self.count >= self.max:
            self.last = None
            return False

        draw = ImageDraw.Draw(image)
        draw.point(coords, self.foreground)

        self.last = coords
        self.count += 1
        return True
