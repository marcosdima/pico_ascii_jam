from ..ascii import Ascii, Anchor
from .....types import Color, Transform


class Avatar(Ascii):
    ''' Avatar entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        ''' Get the Unicode code point for this avatar. '''
        return 0xC6C3
    

    ''' Coloreable interface methods. '''
    def get_default_color(self):
        return Color.GREEN
                

    ''' Lifecycle methods. '''
    def setup(self):
        super().setup()

        coord = lambda r, c: ((r, c), self.color)
        from_row = lambda r, f, t: (coord(r, c) for c in range(f, t + 1))

        self.create_squares([
            *from_row(0, 1, 3),
            *from_row(1, 1, 3),
            *from_row(2, 0, 4),
            *from_row(3, 1, 3),
            coord(4, 1),
            coord(4, 3),
        ])
