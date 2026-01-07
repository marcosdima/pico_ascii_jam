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
    BEIGE: 'Color' = None
    WHEAT: 'Color' = None
    BROWN: 'Color' = None
    ORANGE: 'Color' = None
    PURPLE: 'Color' = None
    PINK: 'Color' = None
    LIME: 'Color' = None
    NAVY: 'Color' = None
    TEAL: 'Color' = None
    TRANSPARENT: 'Color' = None

    
    def __init__(self, r: int, g: int, b: int, a: int = 255):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        self.a = int(a)


    def copy(self) -> 'Color':
        '''Return a copy of the color.'''
        return Color(self.r, self.g, self.b, self.a)
    

    def brighter(self, factor: float = 0.2) -> 'Color':
        '''Return a brighter version of the color.'''
        r = min(int(self.r + (255 - self.r) * factor), 255)
        g = min(int(self.g + (255 - self.g) * factor), 255)
        b = min(int(self.b + (255 - self.b) * factor), 255)
        return Color(r, g, b, self.a)
    

    def darker(self, factor: float = 0.2) -> 'Color':
        '''Return a darker version of the color.'''
        r = max(int(self.r * (1 - factor)), 0)
        g = max(int(self.g * (1 - factor)), 0)
        b = max(int(self.b * (1 - factor)), 0)
        return Color(r, g, b, self.a)


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
Color.BEIGE = Color(245, 245, 220)
Color.WHEAT = Color(245, 222, 179)
Color.BROWN = Color(165, 42, 42)
Color.ORANGE = Color(255, 165, 0)
Color.PURPLE = Color(128, 0, 128)
Color.PINK = Color(255, 192, 203)
Color.LIME = Color(0, 255, 0)
Color.NAVY = Color(0, 0, 128)
Color.TEAL = Color(0, 128, 128)
Color.TRANSPARENT = Color(0, 0, 0, 0)