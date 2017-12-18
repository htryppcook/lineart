
import unittest

from lineart.brushes.pixel_brush import PixelBrush

class TestPixelBrush(unittest.TestCase):
  def setUp(self):
    pass

  def test_pixel_brush_can_init(self):
    pb = PixelBrush()