from ..ascii import Ascii, Anchor
from .....types import Color, Transform
from .....utils import create_full_rows, create_row, create_coord


class Avatar(Ascii):
    ''' Avatar entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0xC6C3
    

    def get_default_dimensions(self):
        return (5, 5)
    
                
    def get_square_values(self):
        color = { 'color': self.color }
        return [
            *create_row(0, 3, 1, content=color),
            *create_row(1, 3, 1, content=color),
            *create_row(2, 4, 0, content=color),
            *create_row(3, 3, 1, content=color),
            create_coord(4, 1, content=color),
            create_coord(4, 3, content=color),
        ]
