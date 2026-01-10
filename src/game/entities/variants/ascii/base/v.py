from ..ascii import Ascii
from ......utils import Coordinate

class V(Ascii):
    ''' V entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0x0056
    

    def get_default_dimensions(self):
        return (5, 3)
  

    def get_square_values(self):
        color = { 'color': self.color }
        return [
            Coordinate.create_coord(0, 0, content=color), Coordinate.create_coord(0, 2, content=color),
            Coordinate.create_coord(1, 0, content=color), Coordinate.create_coord(1, 2, content=color),
            Coordinate.create_coord(2, 0, content=color), Coordinate.create_coord(2, 2, content=color),
            *Coordinate.create_row(3, 2, content=color),
            Coordinate.create_coord(4, 1, content=color),
        ]
