from ..ascii import Ascii


class Avatar(Ascii):
    ''' An ASCII entity that represents an avatar character. '''
    def setup(self):
        super().setup()
        self.set_unicode(0xC6C3)