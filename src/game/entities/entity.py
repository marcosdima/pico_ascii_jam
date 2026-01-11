import pygame

from .modules import Modules
from .components import Components


class Entity(Components):
    ''' Entity base class. '''
    def __str__(self):
        return f'<Entity id={self.id}>'


    ''' Python special methods. '''
    def __init__(self):
        super().__init__()
        
        # Initialize components.
        self.modules = Modules(self)


    def call_draw(self, surface: pygame.Surface) -> pygame.Surface:
        self.base_surface = surface
        self.draw()


    def call_update(self, delta_time: float):
        self.update(delta_time)


    def call_handle_event(self, event: pygame.event.Event):
        self.handle_event(event)