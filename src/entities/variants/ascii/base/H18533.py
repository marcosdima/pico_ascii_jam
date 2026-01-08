from ..ascii import Ascii
from .....utils import create_coord, create_row

class H18533(Ascii):
    ''' V entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0x25CF
  

    def get_default_dimensions(self):
        return (5, 5)


    def get_square_values(self):
        color = { 'color': self.color }
        return [
            *create_row(0, 3, 1, content=color),
            *create_row(1, 2, content=color), create_coord(1, 4, content=color),
            *create_row(2, 4, content=color),
            *create_row(3, 4, content=color),
            *create_row(4, 3, 1, content=color),
        ]
