from pygame import Surface


from ..entities import Avatar
from ..types import Color, Resource
from .logic import Resources


class Player:
    def __init__(self, surface: Surface):
        # Set entity.
        self.entity = Avatar(surface=surface)
        self.entity.modules.set_wasd(speed=200.0) # Set speed to 200 units.
        self.entity.set_color(color=Color.RED)  # Set avatar color to red.
        self.entity.set_transform(size=(200, 200))  # Set avatar size to 200x200 pixels.

        # Set resources.
        self.resources = Resources()
        
        # Add some initial resources for testing
        self.resources.recolect(Resource.ROCK, 10)
        self.resources.recolect(Resource.IRON, 5)
        self.resources.recolect(Resource.GOLD, 2)
