from ..ascii import Ascii
from ......utils import Coordinate


class AsciiCircum(Ascii):
    ''' AsciiCircum entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0x005E
    

    def get_default_dimensions(self):
        return (2, 3)
  

    def get_square_values(self):
        color = { 'color': self.color }
        return [
            Coordinate.create_coord(0, 1, content=color),
            Coordinate.create_coord(1, 0, content=color),
            Coordinate.create_coord(1, 2, content=color),
        ]
