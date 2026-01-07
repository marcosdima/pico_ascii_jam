from pygame import Surface


from ..entities import Avatar, Slingshot
from ..types import Color
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

        # Set slingshot.
        entity_size = self.entity.get_size()
        self.slingshot = Slingshot(surface=surface)
        self.slingshot.set_transform(position=(entity_size.x, 0))  # Set slingshot size and position.
        self.entity.modules.family.add_child(self.slingshot.modules.family) # Add slingshot as child of avatar.
