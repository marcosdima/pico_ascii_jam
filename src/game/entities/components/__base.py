import pygame, pymunk


from ....types import Position, Size
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
        self.z_index = 0
        self.space: pymunk.Space = None
        self.body_type: pymunk.Body = pymunk.Body.DYNAMIC
        self.body: pymunk.Body = pymunk.Body(mass=1, moment=1, body_type=self.body_type)

        # Set lyfe cycle callbacks.
        self.update = Event[float]()
        self.draw = Event[None]()
        self.handle_event = Event[pygame.event.Event]()
        self.size_change = Event[[Size, Size]]()


    def set_space(self, space: pymunk.Space):
        self.space = space
        self.space.add(self.body)


    def set_body_type(self, body_type: pymunk.Body):
        ''' Set body type. '''
        if self.body_type != body_type:
            self.body_type = body_type
            self.body.body_type = body_type

            if body_type is pymunk.Body.DYNAMIC:
                self.body.mass = 1
                self.body.moment = 1
    

    def set_size(self, size: tuple[tuple] | Size):
        """Set the size of the entity."""
        size = Size(*size) if isinstance(size, tuple) else size
        if self.size != size:
            prev = self.size
            self.size = size
            self.size_change(prev, size)
