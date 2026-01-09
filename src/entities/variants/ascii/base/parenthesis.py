from ..ascii import Ascii
from .....utils import create_coord, create_column
from .....types import Color


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
        return [
            create_coord(0, 1, content=color),
            *create_column(0, 3, 1, content=color),
            create_coord(4, 1, content=color),
        ]

