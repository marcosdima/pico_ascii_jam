import pymunk
import math

from .__base import Base
from ....utils import CollisionHandler, Event
from ....types import ColliderGroup


class Collision(Base):
    '''Collision component class.'''
    def __init__(self):
        super().__init__()
        self.handlers: set[CollisionHandler] = set()
        self.collision_type: int = ColliderGroup.DEFAULT.value


    def set_new_handler(self, collision_handler: CollisionHandler):
        '''Set a new collision handler.'''
        if not collision_handler in self.handlers:
            self.handlers.add(collision_handler)
            self.space.on_collision(*collision_handler.as_params())
    

    def get_handler(
        self,
        a: int | tuple[int | int] = 1,
        b: int = None,
    ) -> set[CollisionHandler]:
        if isinstance(a, tuple):
            a, b = a
        elif not b:
            b = a
        
        for handler in self.handlers:
            if handler.a == a and handler.b == b:
                return handler
        
        print(f'No collision handler found for groups {a} and {b}.')
        return None
    

    def set_collision_type(self, coll_type: int | ColliderGroup):
        '''Set collision type for owner shapes.'''
        if isinstance(coll_type, ColliderGroup):
            coll_type = coll_type.value
        self.collision_type = coll_type
        for shape in self.body.shapes:
            shape.collision_type = coll_type
    

    def create_own_shape(self):
        '''Create a box shape for this entity.'''
        shape = pymunk.Poly.create_box(self.body, self.size.to_tuple())
        shape.collision_type = self.collision_type
        shape.entity = self  # attach owner for collision context
        self.space.add(shape)


    def add_shape(self, shape: pymunk.Shape):
        '''Add an existing shape to this entity's collision.
        
        Args:
            shape: Pymunk shape to add (will be attached to this body)
        '''
        shape.collision_type = self.collision_type
        shape.entity = self  # attach owner for collision context
        self.space.add(shape)


    def create_box_shape(self, size: tuple[float, float], offset: tuple[float, float] = (0, 0), angle: float = 0):
        '''Create and add a box shape at a specific offset with rotation.
        
        Args:
            size: (width, height) of the box
            offset: (x, y) offset from body center
            angle: rotation angle in radians
        '''
        # Create base vertices for unrotated box
        half_w = size[0] / 2
        half_h = size[1] / 2
        base_vertices = [
            (-half_w, -half_h),
            (half_w, -half_h),
            (half_w, half_h),
            (-half_w, half_h),
        ]
        
        # Rotate vertices if angle is provided
        if angle != 0:
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            rotated_vertices = []
            for x, y in base_vertices:
                rotated_x = x * cos_a - y * sin_a
                rotated_y = x * sin_a + y * cos_a
                rotated_vertices.append((rotated_x, rotated_y))
            base_vertices = rotated_vertices
        
        # Apply offset to all vertices
        vertices = [(x + offset[0], y + offset[1]) for x, y in base_vertices]
        
        shape = pymunk.Poly(self.body, vertices)
        shape.collision_type = self.collision_type
        shape.entity = self  # attach owner for collision context
        self.space.add(shape)
