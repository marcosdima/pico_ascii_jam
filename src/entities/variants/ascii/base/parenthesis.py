from ..ascii import Ascii
from .....types import Color, Transform


class Parenthesis(Ascii):
    ''' Parenthesis entity class. '''


    ''' Ascii overrides. '''
    def get_unicode() -> int:
        ''' Get the Unicode code point for this parenthesis. '''
        return 0x0028  # Unicode for '('
    

    def get_default_dimensions(self):
        return (5, 2)
    

    ''' Coloreable interface methods. '''
    def get_default_color(self):
        return Color.GREEN
                

    ''' Lifecycle methods. '''
    def setup(self):
        super().setup()

        from_row = lambda r, f, t: (((r, c), self.color) for c in range(f, t + 1))

        self.create_squares([
            *from_row(0, 1, 3),
            *from_row(1, 1, 3),
            *from_row(2, 0, 4),
            *from_row(3, 1, 3),
            ((4, 1), self.color),
            ((4, 3), self.color),
        ])

