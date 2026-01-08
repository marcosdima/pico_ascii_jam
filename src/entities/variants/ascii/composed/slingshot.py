from .composed import Composed
from ..base.v import V
from ..base.asciicircum import AsciiCircum
from ..ascii import Ascii
from .....types import Color, Anchor, Size


class Slingshot(Composed):
    ''' Slingshot entity class. '''


    ''' Composed overrides. '''
    def get_asciis(self) -> list[Ascii]:
        if not hasattr(self, 'v') or not hasattr(self, 'ascii_circum'):
            self.v = V(surface=self.surface,)
            self.ascii_circum = AsciiCircum(surface=self.surface)

        size = 150 # Harcided
        part = size / 10
        height = part * 4
        width = part * 3

        self.v.set_color(color=Color.BEIGE)  # Set V color.
        self.v.set_transform(size=(width, height))  # Set V size and position.
        self.v.set_sign_anchor(anchor=Anchor.TOP_CENTER)

        self.ascii_circum.set_color(color=Color(94, 147, 108))  # Set AsciiCircum color.
        self.ascii_circum.set_transform(size=(width, part * 2), position=(0, height))  # Set AsciiCircum size and position.
        self.ascii_circum.set_sign_anchor(anchor=Anchor.BOTTOM_CENTER)

        return [self.v, self.ascii_circum]
    

    ''' Entity overrides. '''
    def get_size(self):
        aux = Size()
        for ascii in self.asciis:
            if ascii is self.v:
                aux += ascii.get_size()
        return aux