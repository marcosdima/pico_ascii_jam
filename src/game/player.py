from pygame import Surface


from ..entities import Avatar, Slingshot, H18533
from ..types import Color, Size, Resource
from .logic import Resources


class Player:
    def __init__(self, surface: Surface):
        # Set entity.
        self.entity = Avatar(surface=surface)
        self.entity.modules.set_wasd(speed=200.0)
        self.entity.set_color(color=Color.RED)
        self.entity.set_transform(size=(200, 200), position=(100, 100))

        # Set resources.
        self.resources = Resources()
        self.resources.recolect(Resource.ROCK, 10)

        # Set slingshot.
        self.slingshot = Slingshot(surface=surface)
        self.entity.modules.family.add_child(self.slingshot.modules.family)

        slingshot_size = Size(50, 80)
        entity_size = self.entity.get_size()
        self.slingshot.set_transform(
            size=(slingshot_size.x, slingshot_size.y),
            position=(entity_size.x, entity_size.y / 2 - slingshot_size.y),
        )

        # Test.
        h = H18533(surface=surface)
        h.set_color(color=Color.GREEN)
        h.set_transform(size=(50, 50), position=(300, 300))
        self.entity.modules.family.add_child(h.modules.family)
