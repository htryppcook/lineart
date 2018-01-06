
import unittest
import shutil
import os

from io import StringIO
from contextlib import redirect_stdout

from lineart.main import Main

class MainTest(unittest.TestCase):
    ''' Tests for lineart.main.Main '''

    def test_main_help(self):
        ''' Verifies help produces output. '''

        captured = StringIO()
        with redirect_stdout(captured):
            try:
                Main().run(['-h'])
            except SystemExit:
                pass
        print(captured.getvalue())
        self.assertTrue(captured.getvalue() != None)

    def test_main(self):
        ''' Verifies main produces output with simple parameters. '''

        local_dir = os.path.dirname(__file__)
        gif_output = os.path.join(local_dir, 'test_main1.gif')
        log_output = os.path.join(local_dir, 'test_main1.log')

        captured = StringIO()
        with redirect_stdout(captured):
            Main().run(['LineArtist', '--width=100', '--height=100',
                        '--out_file={}'.format(gif_output)])

        with open(log_output, 'w') as log_file:
            captured.seek(0)
            shutil.copyfileobj(captured, log_file)
