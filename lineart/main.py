
import sys
import argparse

from .lineart import LineArt

class Main:
    '''
        Main class
    '''

    def run(self, argv):
        '''
            Parses command line arguments then initializes a LineArt instance
            and begins drawing.
        '''
        lineart = LineArt()

        parser = argparse.ArgumentParser(
            description='make some happy little lines')
        parser.add_argument('artist',
                            help='chosen artist for this performance',
                            choices=lineart.artists.registered)
        parser.add_argument('--out_file', default='./canvas.gif', nargs='?',
                            help='output filename',)
        parser.add_argument('--width', type=int, default=100, nargs='?',
                            help='output image width.')
        parser.add_argument('--height', type=int, default=100, nargs='?',
                            help='output image height.')

        args = parser.parse_args(argv)
        lineart.run(args.artist, args.width, args.height, args.out_file)

if __name__ == '__main__':
    Main().run(sys.argv)
