import pygame, pymunk, math
from typing import Literal


from ....types import Size
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
        self.handle_event = Event[[pygame.event.Event]]()
        self.size_change = Event[[Size, Size]]()
        self.space_change = Event[[pymunk.Space | None]]()


    def set_space(self, space: pymunk.Space):
        self.space = space
        self.space.add(self.body)
        self.space_change(space)


    def set_body_type(self, body_type: pymunk.Body | Literal['dynamic', 'static', 'kinematic']):
        ''' Set body type. '''
        # Convert string to pymunk.Body type.
        if isinstance(body_type, str):
            body_type = {
                'dynamic': pymunk.Body.DYNAMIC,
                'static': pymunk.Body.STATIC,
                'kinematic': pymunk.Body.KINEMATIC,
            }[body_type.lower()]
        
        # Set body type, if different.
        if self.body_type != body_type:
            self.body_type = body_type
            self.body.body_type = body_type

            if body_type is pymunk.Body.DYNAMIC:
                self.body.mass = max(1, self.body.mass)
                self.body.moment = max(1, self.body.mass)
    

    def set_size(self, size: tuple[tuple] | Size):
        """Set the size of the entity."""
        size = Size(*size) if isinstance(size, tuple) else size
        if self.size != size:
            prev = self.size
            self.size = size
            self.size_change(prev, size)


    def rotate(self, degrees: float):
        """Rotate the entity by the given angle in degrees."""
        self.body.angle = math.radians(degrees)


    def get_rect(self) -> pygame.Rect:
        """Get an axis-aligned bounding rect of the entity in world space.

        The rect accounts for current rotation by computing the rotated
        bounding box size analytically, centered at the body's position.
        """
        w = float(self.size.x)
        h = float(self.size.y)

        # Handle empty sizes gracefully
        if w <= 0 or h <= 0:
            return pygame.Rect(int(self.body.position.x), int(self.body.position.y), 0, 0)

        angle = float(self.body.angle)
        cos_a = abs(math.cos(angle))
        sin_a = abs(math.sin(angle))

        bw = w * cos_a + h * sin_a
        bh = w * sin_a + h * cos_a

        cx = float(self.body.position.x)
        cy = float(self.body.position.y)

        x = int(round(cx - bw / 2))
        y = int(round(cy - bh / 2))
        rw = int(round(bw))
        rh = int(round(bh))
        return pygame.Rect(x, y, rw, rh)
