
import random
from itertools import product as itertools_product

from ..artist import Artist
from .constants import DIRECTIONS
from .constants import COLORS
from .constants import ADJACENCY
from .constants import PERIMETER_ADJACENCY
from .constants import REVERSE
from .constants import random_rgb
from .constants import out_of_bounds
from .constants import rotato

class LineArtist(Artist):

    ''' Draws maze-like doodles, with lines that never touch. '''

    # pylint: disable=too-many-instance-attributes

    def __init__(self, line_color=COLORS['BLACK'],
                 background_color=COLORS['WHITE'],
                 line_start_color=COLORS['GOLD'], random_line_color=False):
        super().__init__()
        self.offsets = (
            DIRECTIONS['UP_LEFT'], DIRECTIONS['UP'],
            DIRECTIONS['UP_RIGHT'], DIRECTIONS['RIGHT'],
            DIRECTIONS['DOWN_RIGHT'], DIRECTIONS['DOWN'],
            DIRECTIONS['DOWN_LEFT'], DIRECTIONS['LEFT'],
        )
        self.initial_probabilities = (
            0.05, 0.70, 0.05, 0.20, 0.05, 0.70, 0.05, 0.20
        )

        self.line_color = line_color
        self.background_color = background_color
        self.line_start_color = line_start_color
        self.random_line_color = random_line_color
        self.minimum = 4096
        self.maximum = 0
        self.prev = None
        self.valid_starts = None

    def paint(self, image, brushes):
        total_lines, longest_line = 0, 0
        self.minimum = int((image.width + image.height)/8)
        self.maximum = int((image.width + image.height))
        self.valid_starts = set(itertools_product(
            range(1, image.width-1), range(1, image.height-1)))

        selected = brushes.__dict__[self.select_brush(brushes.registered)]
        selected.background = self.background_color
        selected.foreground = self.line_color
        self.prev = None

        current = (0, 0)
        limit = 0
        while limit < 5000:
            limit += 1
            selected.max = random.randrange(self.minimum, self.maximum)
            try:
                current = random.sample(self.valid_starts, k=1)[0]
            except ValueError:
                print('Ran out of valid start locations.')
                break

            if current is None:
                break

            total_lines += 1
            line_length, selected.count = 0, 0
            offset_tracker = [0, 0]
            selected.foreground = self.line_start_color

            selected.paint(image, current)
            print('painted: {}, color: {}'.format(current, selected.foreground))
            offset = self.select_offset(image, current)
            print('chose offset: {}'.format(offset))

            if offset is None:
                continue

            if self.random_line_color:
                selected.foreground = random_rgb()
            else:
                selected.foreground = self.line_color

            while True:
                current = (current[0] + offset[0], current[1] + offset[1])

                print('painted: {}, color: {}'.format(current,
                                                      selected.foreground))
                if selected.paint(image, current) is False:
                    break
                line_length += 1

                offset = self.select_offset(image, current)
                print('chose offset: {}'.format(offset))

                if offset is None:
                    break

                offset_tracker[0] += offset[0]
                offset_tracker[1] += offset[1]

            print('line length: {}\noffset tracker: {}'.format(line_length,
                                                               offset_tracker))
            if line_length > longest_line:
                longest_line = line_length
            self.prev = None

        print('longest line: {}\ntotal lines: {}'.format(longest_line,
                                                         total_lines))
        return True

    def select_brush(self, brush_names):
        if 'TimedPixelBrush' in brush_names:
            return 'TimedPixelBrush'
        return brush_names[0]

    def select_offset(self, image, coords):
        ''' Choose the next direction we should start painting '''
        offsets, probabilities = self.remove_adjacencies(image, coords)

        for offset in list(offsets):
            new_coords = (coords[0]+offset[0], coords[1]+offset[1])

            if out_of_bounds(new_coords, image.width, image.height):
                del probabilities[offsets.index(offset)]
                offsets.remove(offset)
                continue

            pixel = image.getpixel(new_coords)

            if pixel != self.background_color:
                del probabilities[offsets.index(offset)]
                offsets.remove(offset)

        if not offsets:
            return None
        else:
            choice = random.choices(offsets, weights=probabilities, k=1)[0]
            if self.prev:
                distance = \
                    self.offsets.index(self.prev) - self.offsets.index(choice)
            else:
                distance = 0
            # Rotate the probabilities list a number of spaces equal to the
            #   distance between the previous choice and the current choice.
            # This increases the probability that we paint straighter lines.
            rotato(probabilities, distance)
            self.prev = REVERSE[choice]
            return choice

    def remove_adjacencies(self, image, coords):
        '''
            Removes all pixels adjacent to the previously painted pixel from
            the list of valid start locations.
        '''
        offsets = list(self.offsets)
        probabilities = list(self.initial_probabilities)

        if self.prev != None:
            # remove pixels adjacent to previous from the set of valid starts
            prev_coords = (coords[0]+self.prev[0], coords[1]+self.prev[1])
            if prev_coords in self.valid_starts:
                self.valid_starts.remove(prev_coords)
                print('removed: {}'.format(prev_coords))
            for offset in self.offsets:
                to_remove = (prev_coords[0]+offset[0], prev_coords[1]+offset[1])
                if to_remove in self.valid_starts:
                    self.valid_starts.remove(to_remove)
                    print('removed: {}'.format(to_remove))
            # remove offsets adjacent to previous from the set of valid starts
            adjacencies = ADJACENCY[self.prev]
            for to_remove in [self.prev, adjacencies[0], adjacencies[1]]:
                del probabilities[offsets.index(to_remove)]
                offsets.remove(to_remove)

        for offset in list(offsets):
            adjacencies = ADJACENCY[offset] + PERIMETER_ADJACENCY[offset]
            for adjacent in adjacencies:
                to_check = (coords[0]+adjacent[0], coords[1]+adjacent[1])
                if offset in offsets \
                  and not out_of_bounds(to_check, image.width, image.height) \
                  and image.getpixel(to_check) != self.background_color:
                    del probabilities[offsets.index(offset)]
                    offsets.remove(offset)
                    break

        return offsets, probabilities
