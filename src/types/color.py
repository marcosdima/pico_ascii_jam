from typing import Sequence
import pygame


class Color:
    '''Simple RGBA color container with helpers and presets.'''
    BLACK: 'Color' = None
    WHITE: 'Color' = None
    RED: 'Color' = None
    GREEN: 'Color' = None
    BLUE: 'Color' = None
    CYAN: 'Color' = None
    MAGENTA: 'Color' = None
    YELLOW: 'Color' = None
    GRAY: 'Color' = None

    
    def __init__(self, r: int, g: int, b: int, a: int = 255):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        self.a = int(a)


    ''' Type conversion methods. '''
    def to_tuple(self) -> tuple[int, int, int, int]:
        '''Return color as RGBA tuple.'''
        return (self.r, self.g, self.b, self.a)


    def to_rgb(self) -> tuple[int, int, int]:
        '''Return color as RGB tuple (drops alpha).'''
        return (self.r, self.g, self.b)


    def to_pygame_color(self) -> 'pygame.Color':
        '''Return color as pygame.Color.'''
        return pygame.Color(self.r, self.g, self.b, self.a)


    def copy(self) -> 'Color':
        '''Return a copy of the color.'''
        return Color(self.r, self.g, self.b, self.a)


    '''  Python special methods. '''
    def __repr__(self) -> str:
        return f'Color(r={self.r}, g={self.g}, b={self.b}, a={self.a})'
    

    @classmethod
    def from_sequence(cls, values: Sequence[int]) -> 'Color':
        '''Create Color from a sequence (len 3 or 4).'''
        if len(values) == 3:
            return cls(values[0], values[1], values[2])
        if len(values) == 4:
            return cls(values[0], values[1], values[2], values[3])
        raise ValueError('Color sequence must have length 3 or 4')


    @classmethod
    def from_hex(cls, hex_value: str) -> 'Color':
        '''Create Color from hex string (#RRGGBB or #RRGGBBAA).'''
        h = hex_value.lstrip('#')
        if len(h) not in (6, 8):
            raise ValueError('Hex color must be RRGGBB or RRGGBBAA')

        r = int(h[0:2], 16)
        g = int(h[2:4], 16)
        b = int(h[4:6], 16)
        a = int(h[6:8], 16) if len(h) == 8 else 255
        return cls(r, g, b, a)


# Common presets
Color.BLACK = Color(0, 0, 0)
Color.WHITE = Color(255, 255, 255)
Color.RED = Color(255, 0, 0)
Color.GREEN = Color(0, 255, 0)
Color.BLUE = Color(0, 0, 255)
Color.CYAN = Color(0, 255, 255)
Color.MAGENTA = Color(255, 0, 255)
Color.YELLOW = Color(255, 255, 0)
Color.GRAY = Color(128, 128, 128)