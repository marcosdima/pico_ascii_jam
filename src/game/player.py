from ..entities import Avatar, Slingshot, Entity
from ..types import Color, Size, Resource
from .logic import Resources


class Player(Entity):
    def __init__(self):
        super().__init__()

        # Set entity.
        self.body = Avatar()
        self.body.modules.set_wasd(speed=200.0)
        self.body.set_color(color=Color.YELLOW)
        self.body.set_transform(size=(200, 200), position=(100, 100))
        self.add_child(self.body)
        #self.body.modules.set_debug()
        #self.body.modules.set_background()

        # Set resources.
        self.resources = Resources()
        self.resources.recolect(Resource.ROCK, 10)
        
        # Set slingshot.
        self.slingshot = Slingshot()
        self.body.add_child(self.slingshot)

        slingshot_size = Size(50, 80)
        body_size = self.body.get_size()
        self.slingshot.set_transform(
            size=(slingshot_size.x, slingshot_size.y),
            position=(body_size.x, body_size.y / 2 - slingshot_size.y),
        )
