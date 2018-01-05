''' tests for lineart.artists.line_artist.LineArtist '''
import unittest

from lineart.artists.line_artist import LineArtist

class TestLineArtist(unittest.TestCase):
    ''' tests for lineart.artists.line_artist.LineArtist '''

    def setUp(self):
        pass

    def test_line_artist_can_init(self):
        ''' test to verify LineArtist initializes correctly '''
        line_artist = LineArtist()
