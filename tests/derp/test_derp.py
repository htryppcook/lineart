
import unittest
from PIL import Image, ImageDraw

class TestDerp(unittest.TestCase):

  def setUp(self):
    pass
    
  def test_derp(self):
    im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))
    draw = ImageDraw.Draw(im)
    draw.line((100,200, 150,300), fill=128)
    im.save('/code/tests/derp/derp.gif')
