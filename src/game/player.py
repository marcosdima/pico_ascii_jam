from ..entities import Avatar, Slingshot, Entity
from ..types import Color, Size, Resource, ColliderGroup, Trajectory
from .logic import Resources


class Player(Entity):
    def __init__(self):
        super().__init__()

        # Set entity.
        self.body = Avatar()
        self.body.modules.set_wasd()
        self.body.set_color(color=Color.YELLOW)
        self.body.set_transform(size=(125, 125), position=(100, 100))
        self.body.set_group(ColliderGroup.PLAYER)
        self.body.on_collision.add_callback(self.__bounce_on_collision)
        self.add_child(self.body)

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


    def __bounce_on_collision(self, other: Entity):
        '''Handle collision with another entity.'''
        if other.group == ColliderGroup.DEFAULT:
            #self.body.modules.movement.bounce()
            pass

