
import abc

from python_toolbox.plugin_manager import Plugin

class Brush(Plugin, abc.ABC):

  def __init__(self):
    super().__init__()

  def run(self, canvas, coords):
    self.paint(canvas, coords)

  @abc.abstractmethod
  def paint(self, canvas, coords):
    """ Paint method """
