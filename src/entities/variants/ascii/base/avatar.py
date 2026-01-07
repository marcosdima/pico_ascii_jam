from ..ascii import Ascii
from .....types import Color, Transform


class Avatar(Ascii):
    ''' Avatar entity class. '''


    ''' Ascii overrides. '''
    def get_unicode() -> int:
        ''' Get the Unicode code point for this avatar. '''
        return 0xC6C3
    

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


    def on_transform_changed(self, prev: Transform, new: Transform):
        super().on_transform_changed(prev, new)
        self.grid.set_transform(size=new.size.to_tuple())
