from ..ascii import Ascii


class H18533(Ascii):
    ''' V entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0x25CF
  

    ''' Lifecycle methods. '''
    def setup(self):
        super().setup()
        self.create_squares([
            *self.from_row(0, 3, 1),
            *self.from_row(1, 2), self.get_coord(1, 4),
            *self.from_row(2, 4),
            *self.from_row(3, 4),
            *self.from_row(4, 3, 1),
        ])
