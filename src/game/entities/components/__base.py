import pygame, pymunk


from ....types import Transform, Size
from ....utils import Event


class Base:
    __count = 0


    def __init__(self):
        # Set unique ID.
        self.id = Base.__count
        Base.__count += 1

        # Set base surface.
        self.base_surface: pygame.Surface = None

        # Set body and space.
        self.size = Size()
        self.body: pymunk.Body = pymunk.Body()
        self.space: pymunk.Space = None

        # Set lyfe cycle callbacks.
        self.update = Event[float]()
        self.draw = Event[None]()
        self.handle_event = Event[pygame.event.Event]()
        self.size_change = Event[[Size, Size]]()


    def set_space(self, space: pymunk.Space):
        self.space = space
    

    def call_draw(self, surface: pygame.Surface) -> pygame.Surface:
        self.base_surface = surface
        self.draw()


    def call_update(self, delta_time: float):
        self.update(delta_time)


    def set_size(self, size: Size):
        """Set the size of the entity."""
        if self.size != size:
            prev = self.size
            self.size = size
            self.size_change(prev, size)
