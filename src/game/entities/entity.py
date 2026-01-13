import pygame

from .modules import Modules
from .components import Components


class Entity(Components):
    ''' Entity base class. '''
    def __init__(self):
        super().__init__()
        
        # Initialize components.
        self.modules = Modules(self)
        self.__freed = False


    def __str__(self):
        return f'<Entity id={self.id}>'
    

    def free(self):
        """Remove body and all its shapes from the physics space."""
        self.update.clear_callbacks()
        self.draw.clear_callbacks()
        self.handle_event.clear_callbacks()
        if self.space is not None:
            # Remove all shapes attached to the body
            for shape in list(self.body.shapes):
                self.space.remove(shape)
            
            # Remove the body itself
            self.space.remove(self.body)
        self.__freed = True

        


    def was_freed(self) -> bool:
        return self.__freed


    def call_draw(self, surface: pygame.Surface) -> pygame.Surface:
        self.base_surface = surface
        self.draw()


    def call_update(self, delta_time: float):
        self.update(delta_time)


    def call_handle_event(self, event: pygame.event.Event):
        self.handle_event(event)
