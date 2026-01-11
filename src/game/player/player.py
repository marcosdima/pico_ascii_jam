from ..entities import Avatar, Entity
from ...types import Color, Size, Resource
from .rosources import Resources


class Player(Entity):
    def __init__(self):
        super().__init__()

        # Set entity.
        self.avatar = Avatar()
        self.avatar.size = Size(125, 125)
        self.avatar.modules.set_wasd()
        self.avatar.set_color(color=Color.YELLOW)
        #self.avatar.set_transform(size=(125, 125), position=(100, 100))
        #self.avatar.set_group(ColliderGroup.PLAYER)
        self.avatar.update.add_callback(self.__on_update)
        self.add_child(self.avatar)
        self.avatar.modules.set_debug()

        # Set resources.
        self.resources = Resources()
        self.resources.recolect(Resource.ROCK, 10)
        
        # Set slingshot.
        self.slingshot = Slingshot()
        #self.body.add_child(self.slingshot)

        # Set pickaxe.
        self.pickaxe = Pickaxe()
        self.avatar.add_child(self.pickaxe)
        self.main_tool = self.pickaxe


    def __on_update(self, delta_time: float):
        '''Handle update event.'''
        slingshot_size = Size(50, 80)
        body_size = self.body.transform.size
        self.slingshot.set_transform(
            size=(slingshot_size.x, slingshot_size.y),
            position=(body_size.x, body_size.y / 2 - slingshot_size.y),
        )
