from .composed import Composed
from ..base.v import V
from ..base.asciicircum import AsciiCircum
from .....types import Color, Anchor


class Slingshot(Composed):
    ''' Slingshot entity class. '''


    ''' Composed overrides. '''
    def set_asciis(self):
        acc = super().set_asciis()
        self.v = V(surface=self.surface,)
        self.ascii_circum = AsciiCircum(surface=self.surface)

        height = 40

        self.v.set_color(color=Color.BEIGE)  # Set V color.
        self.v.set_transform(size=(30, height))  # Set V size and position.
        self.v.set_sign_anchor(anchor=Anchor.CENTER_RIGHT)

        self.ascii_circum.set_color(color=Color(94, 147, 108))  # Set AsciiCircum color.
        self.ascii_circum.set_transform(size=(30, 20), position=(0, height))  # Set AsciiCircum size and position.
        self.ascii_circum.set_sign_anchor(anchor=Anchor.CENTER_RIGHT)
        
        return acc + [self.v, self.ascii_circum]