from ..ascii.ascii import Ascii
from ...entity import Entity
from ..ascii.base.H18533 import H18533
from ....types import Resource, ColliderGroup

class Drop(Entity):
    '''Base class for drop entities.'''
    def __init__(self, resource: Resource):
        super().__init__()

        # Set ascii representation.
        self.resource = resource
        self.ascii = self.get_ascii()
        self.add_child(self.ascii)

        # Just player can recolect drops.
        #self.add_vip_group(ColliderGroup.PLAYER)

        # Update ascii transform on drop transform change.
        self.transform_changed.add_callback(
            lambda prev, new: self.ascii.set_transform(
                position=(0, 0),
                size=new.size.to_tuple()
            )
        )

        self.ascii.on_collision.add_callback(
            lambda other: print(f'Recolected {self.resource.name} by {other.group}!')
        )


    def get_ascii(self) -> Ascii:
        '''Get the ASCII representation of this drop.'''
        self.ascii = H18533()
        self.ascii.set_color(color=self.resource.get_color())
        return self.ascii