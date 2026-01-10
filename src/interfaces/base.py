import pygame, math


from ..types import Transform, Hook, Position


class Base:
    __count = 0


    def __init__(self):
        # Set unique ID.
        self.id = Base.__count
        Base.__count += 1

        # Set default transform.
        self.transform = Transform()
        self.world_transform = self.transform.copy()

        # Set base surface.
        self.base_surface: pygame.Surface = None

        # Set lyfe cycle callbacks.
        self.update = Hook[float]()
        self.draw = Hook[None]()
        self.handle_event = Hook[pygame.event.Event]()
        self.transform_changed = Hook[[Transform, Transform]]()


    def call_draw(self, surface: pygame.Surface) -> pygame.Surface:
        self.base_surface = surface
        self.draw()


    def call_update(self, delta_time: float):
        self.update(delta_time)


    def get_transformed_surface(self, surface: pygame.Surface) -> pygame.Surface:
        t = self.get_world_transform()
        
        transformed = surface
        if t.scale != 1:
            transformed = pygame.transform.scale_by(transformed, t.scale)
        if t.rotation != 0:
            transformed = pygame.transform.rotate(transformed, t.rotation)

        return transformed


    ''' Transform methods. '''
    def set_transform(self, transform: Transform):
        """Set the transform of the entity."""
        if self.transform != transform:
            prev = self.transform
            self.transform = transform
            self.transform_changed(prev, transform)


    def get_world_transform(self) -> Transform:
        ''' Get the start point of the entity. '''
        return self.world_transform
    

    def get_world_position(self) -> Position:
        transform = self.get_world_transform()
        return transform.position


    def get_rect(self) -> pygame.Rect:
        position = self.transform.position
        size = self.transform.size
        return pygame.Rect(position.x, position.y, size.x, size.y)


    def get_world_rect(self) -> pygame.Rect:
        transform = self.get_world_transform()
        position = transform.position
        size = transform.size
        return pygame.Rect(position.x, position.y, size.x, size.y)
    

    def rotate_point(self, position: Position, rotation: float) -> Position:
        ''' Rotate a point by an angle in degrees. '''
        rad = -rotation * (3.14159265 / 180.0)
        cos_theta = math.cos(rad)
        sin_theta = math.sin(rad)

        x = position.x * cos_theta - position.y * sin_theta
        y = position.x * sin_theta + position.y * cos_theta

        return Position(x, y)