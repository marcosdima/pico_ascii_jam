from ..ascii import Ascii
from .....utils import create_coord


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
            create_coord(0, 1, content=color),
            create_coord(1, 0, content=color),
            create_coord(1, 2, content=color),
        ]
