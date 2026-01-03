import pygame


from ..types import Transform
from ..core.interfaces import Coloreable, ImmuneSystem


class Entity(Coloreable, ImmuneSystem):
    __count = 0


    def __init__(self, surface: pygame.Surface):
        super().__init__()

        self.parent: 'Entity' = None
        self.surface = surface
        self.children = []
        self.transform = Transform()

        # Set an unique name.
        self.name = f'Entity_{Entity.__count}'
        Entity.__count += 1


    def get_global_position(self):
        '''Get the global position considering parent transforms.'''
        if self.parent is None:
            return self.transform.position
        
        parent_pos = self.parent.get_global_position()
        return parent_pos + self.transform.position


    ''' Children management. '''
    def add_child(self, child: 'Entity'):
        '''Add a child entity.'''
        child.parent = self
        self.children.append(child)

    
    def remove_child(self, child: 'Entity'):
        '''Remove a child entity.'''
        if child in self.children:
            child.parent = None
            self.children.remove(child)


    ''' Life cycle. '''
    def update(self, dt):
        self.handle_update(dt)
        for child in self.children:
            child.update(dt)


    def draw(self):
        self.handle_draw()
        for child in self.children:
            child.draw()

    ''' Python special methods. '''
    def __str__(self):
        return f'<Entity name={self.name} position={self.get_position()} size={self.get_size()} color={self.get_color()}>'
    

    

