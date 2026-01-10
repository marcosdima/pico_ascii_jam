import pygame


from ..types import Transform, Hook


class Base:
    __count = 0


    def __init__(self):
        # Set unique ID.
        self.id = Base.__count
        Base.__count += 1

        # Set default transform.
        self.transform = Transform()

        # Set lyfe cycle callbacks.
        self.update = Hook[float]()
        self.draw = Hook[None]()
        self.handle_event = Hook[pygame.event.Event]()
        self.transform_changed = Hook[[Transform, Transform]]()


    def call_draw(self, surface: pygame.Surface) -> pygame.Surface:
        self.surface = surface
        self.draw()


    def call_update(self, delta_time: float):
        self.update(delta_time)


    ''' Transform methods. '''
    def set_transform(self, transform: Transform):
        """Set the transform of the entity."""
        if self.transform != transform:
            prev = self.transform
            self.transform = transform
            self.transform_changed(prev, transform)

    
    def get_size(self):
        """Get the size of the entity."""
        return self.transform.size
    

    def get_position(self):
        """Get the position of the entity."""
        return self.transform.position
    

    def get_scale(self):
        """Get the scale of the entity."""
        return self.transform.scale
    

    def get_global_position(self) -> pygame.Rect:
        ''' Get the start point of the entity. '''
        return self.get_position()


    def get_rect(self) -> pygame.Rect:
        position = self.get_global_position()
        size = self.get_size()
        return pygame.Rect(position.x, position.y, size.x, size.y)