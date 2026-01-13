from ..composed.__composed import Composed
from ..ascii.base.avatar import Avatar
from ...interfaces import Life
from .....types import Color, ColliderGroup


class Zombie(Life, Composed):
    def __init__(self):
        super().__init__()

        # Avatar setup.
        self.avatar = Avatar()
        self.avatar.set_ascii_size(20)
        self.avatar.set_color(Color.GREEN)


        # Add all parts to the composed player
        self.add_part(self.avatar, offset=(0, 0))


    def _on_space_change(self, space):
        super()._on_space_change(space)
        
        self.set_collision_type(ColliderGroup.ENEMY)
        self.size = self.avatar.size
        self.create_own_shape()
        self.modules.set_debug()
