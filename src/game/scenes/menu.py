from .__scene import Scene
from ...entities import Rock, Sign
from ...types import Resource, Anchor, Color

class Menu(Scene):
    '''Menu scene class.'''
    def __init__(self):
        super().__init__()

        # Set a rock.
        rock = Rock(resource=Resource.ROCK)
        self.add_entity(rock)
        rock.set_transform(size=(200, 200), position=(200, 150))

        # Set a sign.
        sign = Sign('Start', rock, anchor=Anchor.BOTTOM_CENTER, offset=10)
        sign.set_color(Color.WHEAT)
        self.add_entity(sign)
        sign.set_transform(size=(200, 100), position=(400, 150))
