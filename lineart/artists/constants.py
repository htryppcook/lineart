''' Constants used by artists (colors, directions, etc.) '''

from random import randrange

DIRECTIONS = {
    'UP_LEFT'    : (-1, -1),
    'UP'         : (0, -1),
    'UP_RIGHT'   : (1, -1),
    'RIGHT'      : (1, 0),
    'DOWN_RIGHT' : (1, 1),
    'DOWN'       : (0, 1),
    'DOWN_LEFT'  : (-1, 1),
    'LEFT'       : (-1, 0),
}

COLORS = {
    'WHITE'      : (0xFF, 0xFF, 0xFF),
    'BLACK'      : (0x00, 0x00, 0x00),
    'GOLD'       : (0xDD, 0xB6, 0x36),
    'BLACK_BLUE' : (0x0F, 0x13, 0x29),
}

ADJACENCY = {
    (-1, -1) : ((0, -1), (-1, 0)),
    (0, -1)  : ((-1, -1), (1, -1)),
    (1, -1)  : ((0, -1), (1, 0)),
    (1, 0)   : ((1, -1), (1, 1)),
    (1, 1)   : ((1, 0), (0, 1)),
    (0, 1)   : ((1, 1), (-1, 1)),
    (-1, 1)  : ((0, 1), (-1, 0)),
    (-1, 0)  : ((-1, 1), (-1, -1))
}

PERIMETER_ADJACENCY = {
    (-1, -1) : ((-2, -2), (-2, -1), (-1, -2), (-2, 0), (0, -2)),
    (0, -1)  : ((-1, -2), (0, -2), (1, -2)),
    (1, -1)  : ((1, -2), (2, -2), (2, -1), (0, -2), (2, 0)),
    (1, 0)   : ((2, -1), (2, 0), (2, 1)),
    (1, 1)   : ((2, 1), (2, 2), (1, 2), (2, 0), (0, 2)),
    (0, 1)   : ((1, 2), (0, 2), (-1, 2)),
    (-1, 1)  : ((-1, 2), (-2, 2), (-2, 1), (0, 2), (-2, 0)),
    (-1, 0)  : ((-2, 1), (-2, 0), (-2, -1))
}

REVERSE = {
    (-1, -1) : (1, 1),
    (0, -1)  : (0, 1),
    (1, -1)  : (-1, 1),
    (1, 0)   : (-1, 0),
    (1, 1)   : (-1, -1),
    (0, 1)   : (0, -1),
    (-1, 1)  : (1, -1),
    (-1, 0)  : (1, 0)
}

def random_rgb():
    ''' Returns a random RGB color as a tuple. '''
    return tuple([randrange(0, 255) for _ in range(0, 3)])

def out_of_bounds(coords, width, height):
    '''
        Returns True if coords is out of the image's bounds,
        False otherwise
    '''
    return bool(coords[0] < 1 or coords[0] >= width-1
                or coords[1] < 1 or coords[1] >= height-1)

def rotato(seq, places):
    '''
        Rotates the sequence a specified number of places.
        examples:
        >>> rotato([1,2,3], 0)
        [1, 2, 3]
        >>> rotato([1,2,3], 1)
        [2, 3, 1]
        >>> rotato([1,2,3], 2)
        [3, 1, 2]
        >>> rotato([1,2,3], 3)
        [1, 2, 3]
    '''
    return seq[places:] + seq[:places]
