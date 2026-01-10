from .modules import Modules
from ..types import Transform, Position, Size, Hook
from ..interfaces import JointInterface


class Entity(JointInterface):
    ''' Entity base class. '''
    def __str__(self):
        return f'<Entity id={self.id}>'


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
                new_transform.position = Position(*position)
                if new_transform.position != self.transform.position:
                    self.on_position_change(self.transform.position, new_transform.position)
            if size is not None:
                new_transform.size = Size(*size)
                if new_transform.size != self.transform.size:
                    self.on_size_change(self.transform.size, new_transform.size)
            if scale is not None:
                new_transform.scale = scale
            if z_index is not None:
                new_transform.z_index = z_index      
        
        super().set_transform(transform=new_transform)
    

    ''' Python special methods. '''
    def __init__(self):
        super().__init__()
        # Initialize components.
        self.modules = Modules(self)

        # Own hooks.
        self.on_position_change = Hook[Position, Position]()
        self.on_size_change = Hook[Size, Size]()


    