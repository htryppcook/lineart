
from PIL import Image

from python_toolbox.plugin_manager import PluginManager

from .artist import Artist
from .brush import Brush

class ArtistNotFoundException(Exception):
  pass

class LineArt:
  
  def __init__(self):
    self.artists = PluginManager()
    self.artists.register_plugin('lineart.artists')

    self.brushes = PluginManager()
    self.brushes.register_plugin('lineart.brushes')

  def run(self, artist, x, y, out_file):
    self.img = Image.new('RGB', (x, y), (255, 255, 255))

    if artist not in self.artists.registered:
      raise ArtistNotFoundException(
        'Available artists: {}'.format(self.artists.registered))

    self.artists.__dict__[artist].run(self.img, self.brushes)
    self.img.save(out_file)
