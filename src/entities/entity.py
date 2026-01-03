import pygame


from ..types import Transform
from ..core.interfaces import Coloreable, ImmuneSystem


class Entity(Coloreable, ImmuneSystem):
    __count = 0


    def set_transform(
            self,
            position: tuple[float, float] = None,
            size: tuple[float, float] = None,
            scale: tuple[float, float] = None,
        ):
        '''Set the entity's transform.'''
        if position is not None:
            self.transform.set_position(*position)
        if size is not None:
            self.transform.set_size(*size)
        if scale is not None:
            self.transform.set_scale(*scale)
        return self


    ''' Life cycle. '''
    def setup(self):
        # Set default attributes.
        self.parent: 'Entity' = None
        self.children = []
        self.transform = Transform()

        # Set an unique name.
        self.name = f'Entity_{Entity.__count}'
        Entity.__count += 1


    def update(self, dt):
        self.handle_update(dt)
        for child in self.children:
            child.update(dt)


    def draw(self):
        self.handle_draw()
        for child in self.children:
            child.draw()


    ''' Python special methods. '''
    def __init__(self, surface: pygame.Surface):
        super().__init__()
        self.surface = surface
        self.setup()


    def __str__(self):
        return f'<Entity name={self.name} transform={self.transform} color={self.get_color()}>'
