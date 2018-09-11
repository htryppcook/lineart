
import abc

from python_toolbox.plugin_manager import Plugin

class Brush(Plugin, abc.ABC):
    ''' Brush ABC '''

    def run(self, canvas, coords):
        self.paint(canvas, coords)

    @abc.abstractmethod
    def paint(self, canvas, coords):
        """ Paint method """
