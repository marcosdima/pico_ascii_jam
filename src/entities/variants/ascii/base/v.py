from ..ascii import Ascii


class V(Ascii):
    ''' V entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0x0056
    

    def get_default_dimensions(self):
        return (5, 3)
  

    ''' Lifecycle methods. '''
    def setup(self):
        super().setup()
        self.create_squares([
            self.get_coord(0, 0), self.get_coord(0, 2),
            self.get_coord(1, 0), self.get_coord(1, 2),
            self.get_coord(2, 0), self.get_coord(2, 2),
            *self.from_row(3, 2),
            self.get_coord(4, 1),
        ])
