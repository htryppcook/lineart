''' test for lineart.brushes.pixel_brush.PixelBrush '''
import unittest

from lineart.brushes.pixel_brush import PixelBrush

class TestPixelBrush(unittest.TestCase):
    ''' tests for lineart.brushes.pixel_brush.PixelBrush '''
    def setUp(self):
        pass

    def test_pixel_brush_can_init(self):
        ''' test to verify PixelBrush initializes correctly. '''
        pixel_brush = PixelBrush()
        self.assertTrue(pixel_brush != None)
