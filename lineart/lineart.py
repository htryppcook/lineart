
from PIL import Image

from python_toolbox.plugin_manager import PluginManager

class ArtistNotFoundException(Exception):
    ''' Exception thrown when an artist cannot be found. '''
    pass

class LineArt:
    '''
        The LineArt class. Responsible for locating, loading, and running all
        requested artists and brushes.
    '''

    def __init__(self):
        self.artists = PluginManager()
        self.artists.register_plugin('lineart.artists')

        self.brushes = PluginManager()
        self.brushes.register_plugin('lineart.brushes')

        self.img = None

    def run(self, artist, width, height, out_file):
        ''' Builds the base image and hands it off to the selected artist '''
        self.img = Image.new('RGB', (width, height), (255, 255, 255))

        if artist not in self.artists.registered:
            raise ArtistNotFoundException(
                'Available artists: {}'.format(self.artists.registered))

        self.artists.__dict__[artist].run(self.img, self.brushes)
        self.img.save(out_file)
