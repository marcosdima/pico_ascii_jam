from pygame import Surface
import pygame


from .modules import Modules
from ..types import Transform, Position, Color, Vector2, Size
from ..interfaces import Anfitrion, Coloreable, Visible


class Entity(Anfitrion, Coloreable, Visible):
    __count = 0


    ''' Base class for all entities. '''
    def get_position(self) -> Position:
        offset = Position()

        # Check if has a parent entity through the family module...
        if self.modules.family.has_parent():
            # If has it, then get offset from parent..
            parent = self.modules.family.get_parent()
            offset = parent.get_position()

        return (self.transform.position * self.get_scale()) + offset
    

    def get_size(self) -> Size:
        real_size = self.transform.size
        return real_size * self.get_scale()
    

    def get_rect(self) -> tuple[float, float, float, float]:
        position = self.get_position()
        size = self.get_size()
        return (position.x, position.y, size.x, size.y)
    

    def get_scale(self) -> Vector2:
        scale = self.transform.scale

        # Get parent scale.
        if self.modules.family.has_parent():
            parent_scale = self.modules.family.get_parent().transform.scale
            scale = scale * parent_scale

        return scale


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
        
        if new_transform != self.transform:
            self.on_transform_changed(prev=self.transform, new=new_transform)
            self.transform = new_transform
        

    ''' Lifecycle methods. '''
    def setup(self):
        pass


    def update(self, delta_time: float):
        self.on_update(delta_time=delta_time)


    def draw(self):
        if self.is_visible():
            self.on_draw()


    def handle_event(self, event: pygame.event.Event):
        self.on_event(event=event)


    ''' Coloreable interface methods. '''
    def get_default_color(self):
        return Color.WHITE


    ''' Python special methods. '''
    def __init__(self, surface: Surface):
        super().__init__()

        # Set id.
        self.id = Entity.__count
        Entity.__count += 1

        # Set surface.
        self.surface = surface

        # Initialize components.
        self.modules = Modules(self)
        self.transform = Transform()

        # Call setup.
        self.setup()


    def __str__(self):
        return f'<Entity id={id(self)}>'