from .modules import Modules
from ..types import Transform, Color
from ..interfaces import JointInterface


class Entity(JointInterface):
    ''' Overrides. '''
    def set_transform(
            self,
            transform: Transform = None,
            position: tuple[float, float] = None,
            size: tuple[float, float] = None,
            scale: tuple[float, float] = None,
            z_index: int = None
        ):
        new_transform = self.transform.copy()

        # Check values provided.
        if transform is not None:
            new_transform = transform
        else:
            if position is not None:
                new_transform.set_position(*position)
            if size is not None:
                new_transform.set_size(*size)
            if scale is not None:
                new_transform.set_scale(*scale)
            if z_index is not None:
                new_transform.set_z_index(z_index)
        
        super().set_transform(transform=new_transform)
    

    ''' Python special methods. '''
    def __init__(self):
        super().__init__()
        # Initialize components.
        self.modules = Modules(self)


    def __str__(self):
        return f'<Entity id={self.id}>'