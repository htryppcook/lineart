
import abc

from python_toolbox.plugin_manager import Plugin

class Artist(Plugin):
    ''' Artist ABC '''

    def run(self, canvas, brushes):
        '''
            Artist uses the built-in Plugin class for now, so we alias run to
            paint so the interface is easier to understand.
        '''
        self.paint(canvas, brushes)

    @abc.abstractmethod
    def paint(self, canvas, brushes):
        ''' Paint a picture '''

    @abc.abstractmethod
    def select_brush(self):
        ''' Select a brush to use '''
