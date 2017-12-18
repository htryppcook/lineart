
import unittest
import shutil

from io import StringIO
from contextlib import redirect_stdout

from lineart.main import Main

class MainTest(unittest.TestCase):

  def setUp(self):
    pass

  def test_main_help(self):
    expected = ('usage: setup.py [-h] [--out_file [OUT_FILE]] ' +
      '[--width [WIDTH]]\n' +
      '                [--height [HEIGHT]]\n' + 
      '                {LineArtist,NaiveLineArtist}\n' +
      '\n' +
      'make some happy little lines\n' +
      '\n' +
      'positional arguments:\n' +
      '  {LineArtist,NaiveLineArtist}\n'
      '                        chosen artist for this performance\n' +
      '\n' +
      'optional arguments:\n' +
      '  -h, --help            show this help message and exit\n' +
      '  --out_file [OUT_FILE]\n' +
      '                        output filename\n' +
      '  --width [WIDTH]       output image width.\n' +
      '  --height [HEIGHT]     output image height.\n')
    captured = StringIO()
    with redirect_stdout(captured):
      try:
        Main().run(['-h'])
      except SystemExit as e:
        pass
    print(captured.getvalue())
    print(expected)
    self.assertEquals(captured.getvalue(), expected)

  def test_main(self):
    captured = StringIO()
    with redirect_stdout(captured):
      Main().run(['LineArtist', '--width=100', '--height=100',
        '--out_file=/code/tests/main/test_main1.gif'])
    with open('/code/tests/main/test_main1.txt','w') as f:
      captured.seek(0)
      shutil.copyfileobj(captured, f)
    #self.assertEquals(captured.getvalue(), '')
    self.assertTrue(False)
