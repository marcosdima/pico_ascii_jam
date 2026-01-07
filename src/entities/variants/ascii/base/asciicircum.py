from ..ascii import Ascii


class AsciiCircum(Ascii):
    ''' AsciiCircum entity class. '''


    ''' Ascii overrides. '''
    def get_unicode(self) -> int:
        return 0x005E
    

    def get_default_dimensions(self):
        return (2, 3)
  

    ''' Lifecycle methods. '''
    def setup(self):
        super().setup()

        self.create_squares([
            self.get_coord(0, 1),
            self.get_coord(1, 0), self.get_coord(1, 2),
        ])
