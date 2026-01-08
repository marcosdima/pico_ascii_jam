from ..ascii import Ascii
from .....utils import create_coord, create_row


class Parenthesis(Ascii):
    ''' Parenthesis entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0x0028
    

    def get_default_dimensions(self):
        return (5, 2)
                

    ''' Lifecycle methods. '''
    def get_square_values(self):
        color = { 'color': self.color }
        return [
            *create_row(0, 1, 3, content=color),
            *create_row(1, 1, 3, content=color),
            *create_row(2, 0, 4, content=color),
            *create_row(3, 1, 3, content=color),
            create_coord(4, 1, content=color),
            create_coord(4, 3, content=color),
        ]

