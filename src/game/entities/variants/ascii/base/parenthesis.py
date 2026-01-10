from ..ascii import Ascii
from ......utils import Coordinate
from ......types import Color


class Parenthesis(Ascii):
    ''' Parenthesis entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0x0028
    

    def get_default_dimensions(self):
        return (5, 2)
                

    ''' Lifecycle methods. '''
    def get_square_values(self):
        color = { 'color': Color.BROWN }
        return (
            [Coordinate.create_coord(0, 1, content=color), Coordinate.create_coord(4, 1, content=color)]
            + Coordinate.create_column(0, 3, 1, content=color)
        )