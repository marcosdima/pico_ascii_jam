from .composed import Composed
from ..base.v import V
from ..base.parenthesis import Parenthesis
from ..ascii import Ascii
from .....types import Color, Anchor


class Pickaxe(Composed):
    ''' Pickaxe entity class. '''


    ''' Composed overrides. '''
    def get_initial_asciis(self) -> list[Ascii]:
        self.top = Parenthesis(anchor=Anchor.TOP_CENTER)

        size = 150 # Hardcoded
        part = size / 10
        height = part * 5
        width = part * 2

        self.top.set_color(color=Color.BEIGE)
        self.top.set_transform(size=(width, height))

        return [self.top]
