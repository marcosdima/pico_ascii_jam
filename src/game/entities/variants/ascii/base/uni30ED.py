from ..ascii import Ascii
from ......utils import Coordinate

class Uni30ED(Ascii):
    ''' Unicode U+30ED entity class. '''
    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0x30ED
    

    def get_default_dimensions(self):
        return (5, 5)
    
                
    def get_square_values(self):
        color = { 'color': self.color }
        return (
            Coordinate.create_full_rows([0, 4], 5, content=color)
            + [
                Coordinate.create_coord(1, 0, content=color), Coordinate.create_coord(1, 4, content=color),
                Coordinate.create_coord(2, 0, content=color), Coordinate.create_coord(2, 4, content=color),
                Coordinate.create_coord(3, 0, content=color), Coordinate.create_coord(3, 4, content=color),
            ]
        )